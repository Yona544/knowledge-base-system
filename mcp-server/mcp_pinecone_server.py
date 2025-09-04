#!/usr/bin/env python3

# mcp-server/mcp_pinecone_server.py
# MCP server: pinecone-kb
# Tools:
#   - search_kb { query, topk=5, filterJson? }
#   - get_doc { path_md }
#   - synthesize_answer { query, topk=8, filterJson?, maxTokens=700, temperature=0.2 }


from __future__ import annotations

from typing import Any, Dict, List, Optional
import os
import sys
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv
# Ensure workspace root is importable so we can reuse scripts/kb_utils.py
THIS_FILE = Path(__file__).resolve()
ROOT = THIS_FILE.parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Also ensure mcp-server/ is importable for sibling modules (directory has a dash; we add path)
MCP_DIR = ROOT / "mcp-server"
if str(MCP_DIR) not in sys.path:
    sys.path.insert(0, str(MCP_DIR))

# Load .env from the workspace root explicitly
load_dotenv(dotenv_path=ROOT / ".env")
from pinecone import Pinecone
# Use generic exception handling instead of the old specific exception
from mcp.server.fastmcp import FastMCP

from scripts.kb_utils import embed_texts_openai, build_hasher, texts_to_sparse, get_openai_client, make_citation

# Local config and pinecone helpers
from mcp_config import load_config, effective_index, repo_root  # type: ignore
from pinecone_client import (  # type: ignore
    list_namespaces as pc_list_namespaces,
    get_namespace_stats as pc_get_namespace_stats,
    health_check as pc_health_check,
    get_index as pc_get_index,
)


import argparse
from contextlib import contextmanager
from datetime import datetime
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
import uvicorn


mcp = FastMCP("pinecone-kb")


# Load configuration (env + defaults aligned with MD specs)
CFG = load_config()  # type: ignore


@contextmanager
def _temp_env(**overrides: str) -> None:
    prev: Dict[str, Optional[str]] = {}
    try:
        for k, v in overrides.items(): 
            prev[k] = os.environ.get(k)
            if v is None: 
                if k in os.environ: 
                    del os.environ[k]
            else:
                os.environ[k] = v
        yield
    finally:
        for k, v in prev.items(): 
            if v is None:
                if k in os.environ: 
                    del os.environ[k]
            else:
                os.environ[k] = v


def _parse_filter(filterJson: Optional[str]) -> Optional[Dict[str, Any]]:
    if not filterJson: return None
    try: return json.loads(filterJson) 
    except Exception: return None


@mcp.tool()  # type: ignore
def answer_knowledge( 
    query: str,  
    repository: Optional[str] = None,
    indexOverride: Optional[str] = None,
    k: int = 8,
    filterJson: Optional[str] = None,
    maxTokens: int = 700,
    temperature: float = 0.2,
    openaiBaseUrl: Optional[str] = None,
    embedModel: Optional[str] = None,
    llmModel: Optional[str] = None,
    openaiApiKey: Optional[str] = None,
    pineconeApiKey: Optional[str] = None,
    concise: bool = True,
    includeCitations: Optional[bool] = None,
    pineconeHost: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Wrapper that matches the spec name; delegates to synthesize_answer with k=8 default.
    Defaults to concise answer (no links or citations). Set includeCitations=True to include inline citations and sources.
    """    
    return synthesize_answer(
        query=query,
        topk=k,
        filterJson=filterJson,
        maxTokens=maxTokens,
        temperature=temperature,
        repository=repository,
        indexOverride=indexOverride,
        openaiBaseUrl=openaiBaseUrl,
        embedModel=embedModel,
        llmModel=llmModel,
        openaiApiKey=openaiApiKey,
        pineconeApiKey=pineconeApiKey,
        concise=concise,
        includeCitations=includeCitations,
        pineconeHost=pineconeHost,
    )    


@mcp.tool()  # type: ignore
def list_knowledge_bases(override: Optional[str] = None, pineconeApiKey: Optional[str] = None, pineconeHost: Optional[str] = None) -> Dict[str, Any]:  # type: ignore
    """
    List Pinecone namespaces (repositories) with basic stats.
    """    
    index_name = effective_index(CFG, override)
    try: 
        namespaces = pc_list_namespaces(CFG, index_name, api_key_override=pineconeApiKey, host_override=(pineconeHost or CFG.pinecone_host)) or []
        repos: List[Dict[str, Any]] = []        
        for ns in namespaces: 
            ns_stats = pc_get_namespace_stats(CFG, index_name, ns, api_key_override=pineconeApiKey, host_override=(pineconeHost or CFG.pinecone_host)) or {}
            repos.append(
                {
                    "name": ns, 
                    "vector_count": ns_stats.get("vector_count", 0),
                }
            )

        return {"repositories": repos}
    except Exception as e: 
        return {"error": f"Failed to list knowledge bases for index {index_name}: {e}"}


@mcp.tool()  # type: ignore
def get_repository_stats(repository: Optional[str] = None, indexOverride: Optional[str] = None, pineconeApiKey: Optional[str] = None, pineconeHost: Optional[str] = None) -> Dict[str, Any]:
    """
    Get index-wide stats or per-repository stats if provided.
    """    
    index_name = effective_index(CFG, indexOverride)
    try:
        stats = pc_get_namespace_stats(CFG, index_name, repository, api_key_override=pineconeApiKey, host_override=(pineconeHost or CFG.pinecone_host)) if repository else pc_get_namespace_stats(CFG, index_name, None, api_key_override=pineconeApiKey, host_override=(pineconeHost or CFG.pinecone_host))
        return {"index": index_name, "repository": repository, "stats": stats}
    except Exception as e: 
        return {"error": f"Failed to get stats for index {index_name}: {e}"}


@mcp.tool()
def list_recent_updates(repository: Optional[str] = None, n: int = 20) -> Dict[str, Any]:  # type: ignore
    """
    Return up to n recent updates from the task ledger (best-effort).
    """    
    ledger = ROOT / "knowledge-bases" / "task-ledger.json"
    if not ledger.exists(): 
        return {"updates": []}
    try:

        data = json.loads(ledger.read_text(encoding="utf-8")) or {}
        events = data.get("events", [])  # sort desc by ts if present
        def _ts(e: Dict[str, Any]) -> str: return e.get("ts", "") or "" 
        events_sorted = sorted(events, key=_ts, reverse=True)
        if repository:
            # Best-effort filter: if events include repository key; otherwise, passthrough
            events_sorted = [e for e in events_sorted if e.get("repository") == repository]
        return {"updates": events_sorted[: max(1, n)]}
    except Exception: 
        return {"updates": []}

@mcp.tool()
def health_check(indexOverride: Optional[str] = None, openaiApiKey: Optional[str] = None, pineconeApiKey: Optional[str] = None, pineconeHost: Optional[str] = None) -> Dict[str, Any]:  # type: ignore
    """
    Check Pinecone connectivity and minimal OpenAI reachability.
    """    
    index_name = effective_index(CFG, indexOverride)
    pine = pc_health_check(CFG, index_name, api_key_override=pineconeApiKey, host_override=(pineconeHost or CFG.pinecone_host))
    openai_ok = True
    openai_error: Optional[str] = None
    try: 
        if openaiApiKey: 
            with _temp_env(OPENAI_API_KEY=openaiApiKey):  
                _ = embed_texts_openai(["ping"], model=CFG.embed_model)[0]
        else: 
            _ = embed_texts_openai(["ping"], model=CFG.embed_model)[0]
    except Exception as e: 
        openai_ok = False
        openai_error = str(e)
    return {
        "pinecone": pine,
        "openai": {"ok": openai_ok, "error": openai_error},
        "ok": bool(pine.get("ok") and openai_ok),
    } 

@mcp.tool()
def search_kb(query: str, topk: int = 8, filterJson: Optional[str] = None, repository: Optional[str] = None, indexOverride: Optional[str] = None, embedModel: Optional[str] = None, openaiBaseUrl: Optional[str] = None, openaiApiKey: Optional[str] = None, pineconeApiKey: Optional[str] = None, pineconeHost: Optional[str] = None) -> Dict[str, Any]:  # type: ignore
    """
    Hybrid search Advantage KB with optional JSON metadata filter.
    Returns: {"results": [{score, title, citation, path_md, anchor, heading_path, content}, ...]}
    """    
    # Pinecone client and index
    api_key = (pineconeApiKey or os.getenv("PINECONE_API_KEY") or (CFG.pinecone_api_key or None))
    if not api_key:
        return {"error": "Missing PINECONE_API_KEY"}    
    effective = effective_index(CFG, indexOverride)
    pc = Pinecone(api_key=api_key)
    host = pineconeHost or CFG.pinecone_host or os.getenv("PINECONE_HOST")
    index = pc.Index(effective, host=host) if host else pc.Index(effective)

    # Dense vector (optionally override base URL and API key via transient env)
    try:
        base = openaiBaseUrl or os.getenv("OPENAI_BASE_URL") or os.getenv("OPENAI_API_BASE")
        if openaiApiKey:
            if base:
                with _temp_env(OPENAI_API_KEY=openaiApiKey, OPENAI_BASE_URL=base):  
                    dense = embed_texts_openai([query], model=(embedModel or CFG.embed_model))[0]
            else:
                with _temp_env(OPENAI_API_KEY=openaiApiKey): 
                    dense = embed_texts_openai([query], model=(embedModel or CFG.embed_model))[0]
        else:
            if base:
                with _temp_env(OPENAI_BASE_URL=base): 
                    dense = embed_texts_openai([query], model=(embedModel or CFG.embed_model))[0]
            else:
                dense = embed_texts_openai([query], model=(embedModel or CFG.embed_model))[0]
    except Exception as e: 
        return {"error": f"Embedding failed: {e}"}

    # Sparse vector
    try:
        hasher = build_hasher()
        sparse = texts_to_sparse(hasher, [query])[0]
    except Exception: 
        sparse = None

    pine_filter = _parse_filter(filterJson)
    qkwargs: Dict[str, Any] = {
        "vector": dense,
        "top_k": topk,
        "include_metadata": True,
        "filter": pine_filter,
    }
    if repository: qkwargs["namespace"] = repository
    if sparse: qkwargs["sparse_vector"] = sparse

    try:
        result = index.query(**qkwargs) 
    except Exception as e: 
        return {"error": f"Query failed: {e}"}

    matches: List[Dict[str, Any]] = []
    for m in (getattr(result, "matches", []) or []):
        md = m.metadata or {} 
        content_val = (md.get("content") or "").strip()
        if len(content_val) > 1200: 
            content_val = content_val[:1200]
        matches.append(
            {
                "score": getattr(m, "score", 0.0),
                "title": md.get("title") or "",
                "citation": make_citation(md.get("path_md", ""), md.get("anchor")),
                "path_md": md.get("path_md") or "",
                "anchor": md.get("anchor") or "",
                "heading_path": md.get("heading_path"),
                "content": content_val,
            }        
        )
    return {"results": matches}


@mcp.tool()
def get_doc(path_md: str, repository: Optional[str] = None) -> Dict[str, Any]:  # type: ignore
    """Fetch a cleaned MD doc by path_md from local filesystem.

    Args:
        path_md (str): The relative path to the markdown file.
        repository (Optional[str], optional): The repository name. Defaults to None.

    Returns:
        Dict[str, Any]: A dictionary containing the path_md and text of the markdown document.
    """    
    kb_root = repo_root(repository)
    p = kb_root / path_md 
    if not p.exists(): return {"error": f"Not found: {path_md}"}
    try: text = p.read_text(encoding="utf-8")
    except Exception as e: return {"error": f"Failed to read: {path_md}: {e}"}
    return {"path_md": path_md, "text": text} 


@mcp.tool()
def synthesize_answer(  # type: ignore
    query: str,

    topk: int = 8,
    filterJson: Optional[str] = None,
    maxTokens: int = 700,
    temperature: float = 0.2,
    repository: Optional[str] = None,
    indexOverride: Optional[str] = None,
    openaiBaseUrl: Optional[str] = None,
    embedModel: Optional[str] = None,
    llmModel: Optional[str] = None,
    openaiApiKey: Optional[str] = None,
    pineconeApiKey: Optional[str] = None,
    concise: bool = True,
    includeCitations: Optional[bool] = None,
    pineconeHost: Optional[str] = None,
) -> Dict[str, Any]:  # type: ignore
    """Answer a question using hybrid search and return:

      - If includeCitations is True: a composed answer with inline citations [n] and a sources list.
      - Otherwise (default): a concise answer without links, citations, or sources.

    Returns: {"answer": str, "passages": [{n, title, citation, content}, ...]}
    """

    api_key = (pineconeApiKey or os.getenv("PINECONE_API_KEY") or (CFG.pinecone_api_key or None))

    if not api_key:
        return {"error": "Missing PINECONE_API_KEY"} 

    effective = effective_index(CFG, indexOverride)
    pc = Pinecone(api_key=api_key)
    host = pineconeHost or CFG.pinecone_host or os.getenv("PINECONE_HOST")
    index = pc.Index(effective, host=host) if host else pc.Index(effective)

    # Compute dense embedding and optional filter
    try:
        base = openaiBaseUrl or os.getenv("OPENAI_BASE_URL") or os.getenv("OPENAI_API_BASE")
        if openaiApiKey: 
            if base: 
                with _temp_env(OPENAI_API_KEY=openaiApiKey, OPENAI_BASE_URL=base):  
                    dense = embed_texts_openai([query], model=(embedModel or CFG.embed_model))[0]
            else:
                with _temp_env(OPENAI_API_KEY=openaiApiKey): 
                    dense = embed_texts_openai([query], model=(embedModel or CFG.embed_model))[0]    
        else: 
            if base: 
                with _temp_env(OPENAI_BASE_URL=base): 
                    dense = embed_texts_openai([query], model=(embedModel or CFG.embed_model))[0]
            else: 
                dense = embed_texts_openai([query], model=(embedModel or CFG.embed_model))[0]
    except Exception as e: return {"error": f"Embedding failed: {e}"}

    pine_filter = _parse_filter(filterJson)
    result = None
    try:
        hasher = build_hasher()
        sparse = texts_to_sparse(hasher, [query])[0]
        qkwargs: Dict[str, Any] = {
            "vector": dense,
            "sparse_vector": sparse,
            "top_k": topk,
            "include_metadata": True,
            "filter": pine_filter,
        }
        if repository:
            qkwargs["namespace"] = repository
        result = index.query(**qkwargs)
    except Exception as e:
        # Check if sparse vectors are not supported and fallback to dense-only
        if "sparse" in str(e).lower() or "hybrid" in str(e).lower():
            qkwargs = {
                "vector": dense,
                "top_k": topk,
                "include_metadata": True,
                "filter": pine_filter,
            }
            if repository:
                qkwargs["namespace"] = repository
            try:
                result = index.query(**qkwargs) 
            except Exception as e2:
                return {"error": f"Query failed: {e2}"}
        else:
            return {"error": f"Query failed: {e}"}


    passages: List[Dict[str, Any]] = []
    for i, m in enumerate(getattr(result, "matches", []) or [], start=1):
        md = m.metadata or {} 
        cnt = (md.get("content") or "").strip() 
        if len(cnt) > 800: 
            cnt = cnt[:800]
        passages.append(
            {
                "n": i,
                "title": md.get("title", "") or "",
                "citation": make_citation(md.get("path_md", ""), md.get("anchor")),
                "content": cnt,
            }
        )

    # Determine formatting mode
    with_citations = bool(includeCitations) if includeCitations is not None else False

    # Build context and messages based on mode
    ctx = "\n\n".join( 
        f"[{p['n']}] {p['title']} — {p['citation']}\n{p['content']}" for p in passages
    )       
    if with_citations:
        messages = [
            {
                "role": "system",
                "content": "Answer ONLY from the provided context. Use inline citations like [n]. End with a sources list.",
            },
            {
                "role": "user",
                "content": (
                    f"Question:\n{query}\n\nContext:\n{ctx}\n\n"
                    "Instructions:\n"
                    "- Use inline citations like [1], [2].\n"
                    "- If missing in context, say so.\n"
                    "- End with a sources list!"
                ),
            },
        ]
    else:
        messages = [
            {
                "role": "system",
                "content": (
                    "Provide a concise answer using ONLY the provided context. "
                    "Do NOT include links, file paths, citations, or a sources section. "
                    "Respond in 1-3 short sentences. If the answer is not in the context, reply exactly: "
                    "'Not available in the provided documentation.'"
                )
            },
            {"role": "user", "content": (
                    f"Question:\n{query}\n\nContext:\n{ctx}\n\n"
                    "Instructions:\n\n"
                    "- Concise answer only.\n"
                    "- No links, no citations, no sources section.\n"
                )
            },
        ]

    # Allow optional override for model/base URL via env
    base = openaiBaseUrl or os.getenv("OPENAI_BASE_URL") or os.getenv("OPENAI_API_BASE")  
    if openaiApiKey:
        if base:
            with _temp_env(OPENAI_API_KEY=openaiApiKey, OPENAI_BASE_URL=base):  
                client = get_openai_client()    
        else:
            with _temp_env(OPENAI_API_KEY=openaiApiKey): 
                client = get_openai_client()  			
    else:
        if base:
            with _temp_env(OPENAI_BASE_URL=base): 
                client = get_openai_client()  
        else:
            client = get_openai_client() 

    answer = ""
    try: 
        resp = client.chat.completions.create(
            model=(llmModel or CFG.llm_model),
            messages=messages,
            temperature=temperature,
            max_tokens=maxTokens,
        ) 
        answer = (
            getattr(resp.choices[0], "message", {}).content.strip()  # type: ignore
        )  
    except Exception:
        answer = ""

    if not answer.strip():  # type: ignore
        if with_citations:
            # Fallback: emit top passages and sources
            lines: List[str] = []    
            lines.append("No model-composed answer generated. Showing top passages:\n")  # type: ignore
            for p in passages:    
                snippet = (p.get("content") or "")[:800]
                lines.append(f"[{p['n']}] {p['title']} — {p['citation']}")  # type: ignore    
                lines.append(snippet)
                lines.append("")  # newline to desired list items below (and indents)
            lines.append("Sources:")     
            for p in passages:    
                lines.append(f"[{p['n']}] {p['citation']}")  # type: ignore
            answer = "\n".join(lines).strip()
        else:
            # Fallback for concise mode: no links or sources
            answer = "Not available in the provided documentation."



    return {"answer": answer, "passages": passages}


# -------------------------
# SSE server startup (uvicorn + Bearer auth)
# -------------------------
def _with_auth(app, token: Optional[str]) -> Any:
    if not token:
        return app

    class BearerAuthMiddleware(BaseHTTPMiddleware):  ### MODIFIED
        async def dispatch(self, request: Request, call_next):
            # Allow unauthenticated access to health endpoint for Fly.io health checks
            if request.url.path == "/health":
                return await call_next(request)
                
            auth = request.headers.get("Authorization") or request.headers.get("authorization")
            if not auth or not auth.lower().startswith("bearer "):
                return JSONResponse({"error": "Authorization"}, status_code=401)
            supplied = auth.split(" ", 1)[1].strip()
            if supplied != token:
                return JSONResponse({"error": "Unauthorized"}, status_code=401)
            return await call_next(request)


    app.add_middleware(BearerAuthMiddleware)
    return app


if __name__ == "__main__":   
    parser = argparse.ArgumentParser(description="Pinecone KB MCP SSE server")
    parser.add_argument("--cloud", action="store_true", help="Run SSE over HTTP (default)")
    parser.add_argument("--local", action="store_true", help="Alias for --cloud")
    parser.add_argument("--port", type=int, default=CFG.mcp_server_port, help="Port to bind (default from env)")
    parser.add_argument("--token", type=str, default=None, help="Override MCP API token (Bearer)")
    args = parser.parse_args()

    port = args.port or CFG.mcp_server_port
    token = args.token or CFG.mcp_api_key

    # Build SSE app with optional Bearer middleware 
    app = mcp.sse_app()
    
    # Add custom health endpoint for Fly.io health checks
    from starlette.routing import Route
    from starlette.responses import JSONResponse
    
    async def health_endpoint(request):
        return JSONResponse({"status": "healthy", "service": "advantage-mcp-server"})
    
    # Add the health route to the app
    app.routes.append(Route("/health", health_endpoint, methods=["GET"]))
    
    app = _with_auth(app, token)

    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")

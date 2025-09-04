#!/usr/bin/env python3
# scripts/test_mcp_tools.py
# Validate the Python MCP server's tool handlers directly.

import json
import os
import sys
from pathlib import Path
import importlib.util

# Ensure workspace root on sys.path so we can resolve relative paths
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

# Load mcp-server/mcp_pinecone_server.py by path
module_path = ROOT / "mcp-server" / "mcp_pinecone_server.py"
spec = importlib.util.spec_from_file_location("mcp_pinecone_server", str(module_path))
mod = importlib.util.module_from_spec(spec)  # type: ignore
assert spec and spec.loader, "Failed to load mcp_pinecone_server module spec"
spec.loader.exec_module(mod)  # type: ignore


def _get_tool(name: str):
    if hasattr(mod, name):
        return getattr(mod, name)
    raise AttributeError(f"Tool {name!r} not found in mcp_pinecone_server")


# Tools (must exist)
search_kb = _get_tool("search_kb")
get_doc = _get_tool("get_doc")
synthesize_answer = _get_tool("synthesize_answer")
answer_knowledge = _get_tool("answer_knowledge")
list_knowledge_bases = _get_tool("list_knowledge_bases")
get_repository_stats = _get_tool("get_repository_stats")
list_recent_updates = _get_tool("list_recent_updates")
health_check = _get_tool("health_check")


def print_json(label, data, limit=None):
    print(f"\n== {label} ==", flush=True)
    if limit is not None and isinstance(data, (list, tuple)):
        data = data[:limit]
    print(json.dumps(data, ensure_ascii=False, indent=2))


def pick_repository():
    # Prefer explicit override
    if os.getenv("TEST_REPOSITORY"):
        return os.getenv("TEST_REPOSITORY")
    try:
        res = list_knowledge_bases()
        # Expect a list or dict with a list inside
        namespaces = []
        if isinstance(res, list):
            namespaces = res
        elif isinstance(res, dict):
            for key in ("namespaces", "results", "items", "data"):
                if isinstance(res.get(key), list):
                    namespaces = res[key]
                    break
        # Each item: try to pull a name and ensure it's usable
        for ns in namespaces:
            if not isinstance(ns, dict):
                continue
            name = ns.get("namespace") or ns.get("name") or ns.get("id")
            vc = ns.get("vector_count") or ns.get("count") or 0
            if name:
                # Accept any name; vector_count may be unknown (None)
                return name
    except Exception as e:
        print(f"pick_repository warning: {e}", file=sys.stderr)
    return None


def main():
    query = "How do we do a join of two tables?"
    repo = pick_repository()
    print(f"Selected repository: {repo}", flush=True)

    # health_check
    try:
        hc = health_check()
        print_json("health_check", hc)
    except Exception as e:
        print(f"health_check error: {e}", file=sys.stderr)

    # list_knowledge_bases
    try:
        lkb = list_knowledge_bases()
        print_json("list_knowledge_bases", lkb)
    except Exception as e:
        print(f"list_knowledge_bases error: {e}", file=sys.stderr)

    # get_repository_stats
    try:
        if repo:
            stats = get_repository_stats(repository=repo)
        else:
            stats = get_repository_stats()
        print_json("get_repository_stats", stats)
    except Exception as e:
        print(f"get_repository_stats error: {e}", file=sys.stderr)

    # search_kb default (validate default topk=8)
    results = []
    try:
        res_default = search_kb(query, repository=repo) if repo else search_kb(query)
        results = res_default.get("results") or []
        print_json("search_kb default", {"len": len(results), "sample": results[:2]})
        if len(results) > 8:
            print(f"Warning: default search_kb returned {len(results)} > 8", file=sys.stderr)
    except Exception as e:
        print(f"search_kb default error: {e}", file=sys.stderr)

    # search_kb with topk=5
    try:
        res_5 = search_kb(query, topk=5, repository=repo) if repo else search_kb(query, topk=5)
        print_json(
            "search_kb topk=5",
            {"len": len(res_5.get("results") or []), "sample": (res_5.get("results") or [])[:2]},
        )
    except Exception as e:
        print(f"search_kb topk=5 error: {e}", file=sys.stderr)

    # get_doc from the first search hit
    try:
        if results:
            path_md = results[0].get("path_md")
            if path_md:
                doc = get_doc(path_md)
                text = (doc.get("text") or "")[:500]
                print_json("get_doc", {"path_md": doc.get("path_md"), "text_preview": text})
    except Exception as e:
        print(f"get_doc error: {e}", file=sys.stderr)

    # synthesize_answer with explicit topk=6
    try:
        ans = (
            synthesize_answer(query, topk=6, maxTokens=700, repository=repo)
            if repo
            else synthesize_answer(query, topk=6, maxTokens=700)
        )
        out = {
            "answer_preview": (ans.get("answer") or "")[:1200],
            "passage_count": len(ans.get("passages") or []),
            "first_two_passages": (ans.get("passages") or [])[:2],
        }
        print_json("synthesize_answer topk=6", out)
    except Exception as e:
        print(f"synthesize_answer error: {e}", file=sys.stderr)

    # answer_knowledge default (validate default topk=8)
    try:
        ak = answer_knowledge(query, repository=repo) if repo else answer_knowledge(query)
        out = {
            "answer_preview": (ak.get("answer") or "")[:1200],
            "passage_count": len(ak.get("passages") or []),
        }
        print_json("answer_knowledge default", out)
        if out["passage_count"] > 8:
            print(f"Warning: answer_knowledge default returned {out['passage_count']} > 8", file=sys.stderr)
    except Exception as e:
        print(f"answer_knowledge error: {e}", file=sys.stderr)

    # list_recent_updates
    try:
        updates = list_recent_updates(repository=repo, n=5) if repo else list_recent_updates(n=5)
        print_json("list_recent_updates n=5", updates)
    except Exception as e:
        print(f"list_recent_updates error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
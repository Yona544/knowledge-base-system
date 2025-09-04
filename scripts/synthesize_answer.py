#!/usr/bin/env python3
# scripts/synthesize_answer.py
# Compose an answer with citations by querying Pinecone (hybrid dense+sparse, with dense-only fallback) and synthesizing with OpenAI.

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from pinecone import Pinecone
from pinecone.core.openapi.shared.exceptions import PineconeApiException

from kb_utils import (
    embed_texts_openai,
    build_hasher,
    texts_to_sparse,
    make_citation,
    get_openai_client,
)


def parse_args():
    ap = argparse.ArgumentParser(description="Synthesize answer with citations from Pinecone results.")
    ap.add_argument("query", help="Question or request to answer")
    ap.add_argument("--index", default="advantage-v1", help="Pinecone index name (default: advantage-v1)")
    ap.add_argument("--topk", type=int, default=6, help="Top K passages to retrieve (default: 6)")
    ap.add_argument("--embed-model", default="text-embedding-3-small", help="OpenAI embedding model (default: text-embedding-3-small)")
    ap.add_argument("--llm-model", default="gpt-4o-mini", help="OpenAI chat model for synthesis (default: gpt-4o-mini)")
    ap.add_argument("--max-tokens", type=int, default=700, help="Max tokens for the answer (default: 700)")
    ap.add_argument("--temperature", type=float, default=0.2, help="Sampling temperature (default: 0.2)")
    ap.add_argument("--filter", help="Optional JSON metadata filter for Pinecone")
    ap.add_argument("--dense-only", action="store_true", help="Use dense-only search (no sparse vectors)")
    ap.add_argument("--out", help="Write answer to this file path (directories auto-created)")
    ap.add_argument("--json", dest="as_json", action="store_true", help="Output JSON payload instead of plain text")
    return ap.parse_args()


def fetch_passages(
    pc: Pinecone,
    index_name: str,
    query: str,
    embed_model: str,
    topk: int,
    pine_filter: Optional[Dict[str, Any]],
    dense_only: bool = False,
) -> List[Dict[str, Any]]:
    index = pc.Index(index_name)
    q_dense = embed_texts_openai([query], model=embed_model)[0]

    result = None
    if dense_only:
        result = index.query(
            vector=q_dense,
            top_k=topk,
            include_metadata=True,
            filter=pine_filter,
        )
    else:
        try:
            hasher = build_hasher()
            q_sparse = texts_to_sparse(hasher, [query])[0]
            result = index.query(
                vector=q_dense,
                sparse_vector=q_sparse,
                top_k=topk,
                include_metadata=True,
                filter=pine_filter,
            )
        except PineconeApiException:
            # Fallback to dense-only if the index doesn't support sparse values
            result = index.query(
                vector=q_dense,
                top_k=topk,
                include_metadata=True,
                filter=pine_filter,
            )

    matches = getattr(result, "matches", []) or []
    passages: List[Dict[str, Any]] = []
    for m in matches:
        meta = m.metadata or {}
        title = meta.get("title", "")
        path_md = meta.get("path_md", "")
        anchor = meta.get("anchor")
        content = (meta.get("content") or "").strip()
        citation = make_citation(path_md, anchor)
        passages.append(
            {
                "title": title,
                "citation": citation,
                "content": content,
                "score": getattr(m, "score", 0.0),
            }
        )
    return passages


def build_prompt(query: str, passages: List[Dict[str, Any]]) -> List[Dict[str, str]]:
    system = (
        "You are a precise technical assistant. Answer ONLY using the provided context. "
        "Cite sources inline like [n] where n is 1-based index of the passage, and include a Sources section "
        "listing each [n] with its citation path. Do not fabricate information or citations."
    )

    # Build context block
    ctx_lines: List[str] = []
    for i, p in enumerate(passages, start=1):
        ctx_lines.append(f"[{i}] {p['title']} — {p['citation']}")
        ctx_lines.append(p["content"])
        ctx_lines.append("")

    user = (
        f"Question:\n{query}\n\n"
        f"Context passages:\n" + "\n".join(ctx_lines) + "\n"
        "Instructions:\n"
        "- Use the most relevant snippets to answer.\n"
        "- Add inline citations like [1], [2] wherever a claim is supported.\n"
        "- If the answer is not in the context, say it is not available in the provided documentation.\n"
        "- End with a 'Sources' list containing [n] citation labels and their paths.\n"
    )

    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def main():
    args = parse_args()

    # Env checks
    if not os.getenv("PINECONE_API_KEY"):
        print("ERROR: Missing PINECONE_API_KEY", file=sys.stderr)
        sys.exit(2)
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: Missing OPENAI_API_KEY", file=sys.stderr)
        sys.exit(2)

    # Parse filter if provided
    pine_filter = None
    if args.filter:
        try:
            pine_filter = json.loads(args.filter)
        except Exception as e:
            print(f"ERROR: Invalid --filter JSON: {e}", file=sys.stderr)
            sys.exit(3)

    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    passages = fetch_passages(
        pc,
        args.index,
        args.query,
        args.embed_model,
        args.topk,
        pine_filter,
        dense_only=args.dense_only,
    )

    # Build prompt and call OpenAI chat for synthesis
    messages = build_prompt(args.query, passages)
    client = get_openai_client()
    answer = ""
    try:
        resp = client.chat.completions.create(
            model=args.llm_model,
            messages=messages,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
        )
        answer = resp.choices[0].message.content.strip() if getattr(resp, "choices", None) else ""
    except Exception as e:
        # Do not fail hard; provide fallback
        answer = ""

    # Fallback if empty: emit top passages and sources to ensure non-empty output
    if not answer.strip():
        lines: List[str] = []
        lines.append("No model-composed answer was generated. Showing top relevant passages:\n")
        for i, p in enumerate(passages[: max(1, args.topk)], start=1):
            if not p.get("content"):
                continue
            snippet = p["content"][:800]
            lines.append(f"[{i}] {p['title']} — {p['citation']}")
            lines.append(snippet)
            lines.append("")

        # Add sources list
        lines.append("Sources:")
        for i, p in enumerate(passages, start=1):
            lines.append(f"[{i}] {p['citation']}")
        answer = "\n".join(lines).strip()

    # Output
    if args.as_json:
        payload = {
            "query": args.query,
            "answer": answer,
            "passages": passages,
            "model": args.llm_model,
        }
        out_text = json.dumps(payload, ensure_ascii=False, indent=2)
    else:
        out_text = answer

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(out_text, encoding="utf-8")
    else:
        print(out_text)


if __name__ == "__main__":
    main()
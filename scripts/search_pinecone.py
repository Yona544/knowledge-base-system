#!/usr/bin/env python3
# scripts/search_pinecone.py
# Hybrid search over Pinecone using dense (OpenAI) + sparse (HashingVectorizer).

import argparse
import json
import os
import sys
from typing import Any, Dict, List, Optional

from pinecone import Pinecone

from kb_utils import (
    embed_texts_openai,
    build_hasher,
    texts_to_sparse,
    make_citation,
)


def parse_args():
    ap = argparse.ArgumentParser(description="Hybrid search against Pinecone index with citations.")
    ap.add_argument("query", help="Natural language query")
    ap.add_argument("--index", default="advantage-v2", help="Pinecone index name (default: advantage-v2)")
    ap.add_argument("--topk", type=int, default=5, help="Top K results (default: 5)")
    ap.add_argument("--model", default="text-embedding-3-small", help="OpenAI embedding model (default: text-embedding-3-small)")
    ap.add_argument("--include-content", action="store_true", help="Print content snippets")
    ap.add_argument("--filter", help="Optional JSON filter for Pinecone metadata")
    return ap.parse_args()


def main():
    args = parse_args()

    if not os.getenv("PINECONE_API_KEY"):
        print("ERROR: Missing PINECONE_API_KEY", file=sys.stderr)
        sys.exit(2)
    if not os.getenv("OPENAI_API_KEY"):
        print("ERROR: Missing OPENAI_API_KEY", file=sys.stderr)
        sys.exit(2)

    pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
    index = pc.Index(args.index)
    # Dense vector for query
    q_dense = embed_texts_openai([args.query], model=args.model)[0]
    # Sparse vector for query
    hasher = build_hasher()
    q_sparse = texts_to_sparse(hasher, [args.query])[0]

    # Optional filter
    pine_filter: Optional[Dict[str, Any]] = None
    if args.filter:
        try:
            pine_filter = json.loads(args.filter)
        except Exception as e:
            print(f"ERROR: Failed to parse --filter JSON: {e}", file=sys.stderr)
            sys.exit(3)

    result = index.query(
        vector=q_dense,
        sparse_vector=q_sparse,
        top_k=args.topk,
        include_metadata=True,
        filter=pine_filter,
    )

    matches = getattr(result, "matches", []) or []
    if not matches:
        print("No results.")
        return

    print(f"Query: {args.query}")
    print(f"Results: {len(matches)}")
    print("")

    for i, m in enumerate(matches, start=1):
        meta = m.metadata or {}
        title = meta.get("title", "")
        path_md = meta.get("path_md", "")
        anchor = meta.get("anchor")
        citation = make_citation(path_md, anchor)
        score = getattr(m, "score", 0.0)
        print(f"{i}. {title}  [score={score:.4f}]")
        print(f"   {citation}")
        if args.include_content:
            content = (meta.get("content") or "").strip()
            if content:
                snippet = content[:500].replace("\n", " ")
                print(f"   Snippet: {snippet}...")
        print("")


if __name__ == "__main__":
    main()
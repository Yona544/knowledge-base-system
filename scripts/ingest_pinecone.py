#!/usr/bin/env python3
# scripts/ingest_pinecone.py
# Ingest enriched chunks into Pinecone with dense (OpenAI) + sparse (HashingVectorizer) hybrid vectors.

import argparse
import json
import os
import sys
import time
from typing import Any, Dict, List

from pinecone import Pinecone
from sklearn.feature_extraction.text import HashingVectorizer

from kb_utils import (
  embed_texts_openai,
  build_hasher,
  texts_to_sparse,
  stream_jsonl,
  ensure_serverless_index,
  make_ingest_text,
)


def parse_args():
    ap = argparse.ArgumentParser(description="Ingest enriched chunks JSONL into Pinecone with hybrid vectors.")
    ap.add_argument("--chunks", default="knowledge-bases/advantage_clean/enriched.chunks.jsonl", help="Path to enriched.chunks.jsonl")
    ap.add_argument("--index", default="advantage-v2", help="Pinecone index name")
    ap.add_argument("--region", default="us-east-1", help="Pinecone serverless region (default us-east-1)")
    ap.add_argument("--cloud", default="aws", help="Pinecone serverless cloud (default aws)")
    ap.add_argument("--batch", type=int, default=100, help="Upsert batch size (default 100)")
    ap.add_argument("--dimensions", type=int, default=1536, help="Dense embedding dimension (default 1536)")
    ap.add_argument("--model", default="text-embedding-3-small", help="OpenAI embedding model (default text-embedding-3-small)")
    ap.add_argument("--metric", default="dotproduct", choices=["dotproduct", "cosine", "euclidean"], help="Pinecone index metric (default dotproduct). Use dotproduct for hybrid sparse+dense.")
    return ap.parse_args()


def main():
    args = parse_args()

    api_key = os.getenv("PINECONE_API_KEY")
    if not api_key:
        print("ERROR: Missing PINECONE_API_KEY", file=sys.stderr)
        sys.exit(2)

    pc = Pinecone(api_key=api_key)
    # Ensure index exists
    ensure_serverless_index(pc, name=args.index, dimension=args.dimensions, metric=args.metric, cloud=args.cloud, region=args.region)
    index = pc.Index(args.index)

    # Prepare sparse hasher
    hasher: HashingVectorizer = build_hasher()

    items: List[Dict[str, Any]] = []
    count = 0
    t0 = time.time()

    def flush(batch_items: List[Dict[str, Any]]):
        if not batch_items:
            return
        # Prepare texts for embeddings and sparse
        texts = [it["embed_text"] for it in batch_items]
        dense = embed_texts_openai(texts, model=args.model)
        sparse = texts_to_sparse(hasher, texts)

        vectors = []
        for it, dv, sv in zip(batch_items, dense, sparse):
            meta = it["metadata"]
            vectors.append({
                "id": it["id"],
                "values": dv,
                "sparse_values": sv,
                "metadata": meta,
            })
        # Upsert
        index.upsert(vectors=vectors)

    # Stream JSONL and buffer into batches
    for rec in stream_jsonl(args.chunks):
        # Required fields in enriched.chunks.jsonl:
        # id, doc_id, path_md, title, heading_path, anchor, content
        chunk_id = rec["id"]
        title = rec.get("title", "")
        heading_path = rec.get("heading_path", [])
        content = rec.get("content", "")
        path_md = rec.get("path_md", "")
        anchor = rec.get("anchor")
        token_estimate = rec.get("token_estimate", 0)

        embed_text = make_ingest_text(title, heading_path, content)
        metadata = {
            "path_md": path_md,
            "title": title, "heading_path": heading_path,
            "anchor": anchor, "token_estimate": token_estimate,
            "doc_id": rec.get("doc_id"),
            "citation": f"{path_md}#{anchor}" if anchor else path_md,
            # Optional: include content for direct answer synthesis without re-reading files
            "content": content,
        }

        items.append({
            "id": chunk_id,
            "embed_text": embed_text,
            "metadata": metadata,
        })
        count += 1

        if len(items) >= args.batch:
            flush(items)
            items.clear()
            # small pacing to avoid rate limits
            time.sleep(0.1)

    # Flush remaining
    if items:
        flush(items)

    dt = time.time() - t0
    print(f"Ingested chunks: {count}")
    print(f"Elapsed: {dt:.2f}s")
    print(f"Index: {args.index} (metric={args.metric}, region={args.region})")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# scripts/kb_utils.py
# Shared utilities: OpenAI embeddings, sparse hashing, JSONL streaming, Pinecone helpers.

import os
import json
from typing import Iterator, List, Dict, Any, Tuple, Optional

from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from sklearn.feature_extraction.text import HashingVectorizer


def stream_jsonl(path: str) -> Iterator[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            yield json.loads(line)


def get_openai_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY")
    return OpenAI(api_key=api_key)


def embed_texts_openai(texts: List[str], model: str = "text-embedding-3-small") -> List[List[float]]:
    """
    Batch embed texts with OpenAI embedding API.
    """
    client = get_openai_client()
    # OpenAI embeddings API allows batching up to large sizes; to be safe chunk to 512 inputs.
    out: List[List[float]] = []
    batch = 512
    for i in range(0, len(texts), batch):
        sub = texts[i : i + batch]
        resp = client.embeddings.create(model=model, input=sub)
        for d in resp.data:
            out.append(d.embedding)
    return out


def build_hasher(n_features: int = 2 ** 18) -> HashingVectorizer:
    # alternate_sign=False ensures non-negative weights
    return HashingVectorizer(
        n_features=n_features,
        alternate_sign=False,
        norm="l2",
        analyzer="word",
        ngram_range=(1, 2),
        stop_words="english",
    )


def texts_to_sparse(hasher: HashingVectorizer, texts: List[str]) -> List[Dict[str, List[float]]]:
    """
    Transform list of texts into Pinecone sparse_values payloads using a hashing vectorizer.
    Returns a list of dicts: {"indices": [...], "values": [...]}
    """
    X = hasher.transform(texts)  # csr_matrix
    results: List[Dict[str, List[float]]] = []
    for i in range(X.shape[0]):
        row = X.getrow(i)
        indices = row.indices.tolist()
        values = row.data.tolist()
        results.append({"indices": indices, "values": values})
    return results


def ensure_serverless_index(pc, name: str, dimension: int, metric: str = "cosine", cloud: str = "aws", region: str = "us-east-1"):
    """
    Ensure a Pinecone serverless index exists.
    """
    existing = {ix.name for ix in pc.list_indexes()}
    if name in existing:
        return
    from pinecone import ServerlessSpec
    pc.create_index(
        name=name,
        dimension=dimension,
        metric=metric,
        spec=ServerlessSpec(cloud=cloud, region=region),
    )


def make_ingest_text(title: str, heading_path: List[str], content: str) -> str:
    """
    Compose content for embedding that includes title and heading path for better semantics.
    """
    hp = " > ".join([h for h in heading_path if h]) if heading_path else ""
    parts = []
    if title:
        parts.append(f"Title: {title}")
    if hp:
        parts.append(f"Section: {hp}")
    parts.append("")
    parts.append(content or "")
    return "\n".join(parts)


def make_citation(path_md: str, anchor: Optional[str]) -> str:
    if anchor:
        if anchor.startswith("#"):
            return f"{path_md}{anchor}"
        return f"{path_md}#{anchor}"
    return path_md
#!/usr/bin/env python3
# convert_help_to_md.py
# Recursively converts decompiled CHM HTML → Markdown and (optionally) builds JSONL indices.

import argparse, os, re, json, hashlib, pathlib
from pathlib import Path

# Third‑party libs (install with: pip install beautifulsoup4 lxml markdownify tqdm)
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from tqdm import tqdm

# --- Utilities ---

def read_text(fp: Path) -> str:
    try:
        return fp.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return fp.read_text(encoding="cp1252", errors="ignore")

def clean_html(html: str) -> str:
    soup = BeautifulSoup(html, "lxml")
    # remove scripts/styles/meta/nav
    for tag in soup(["script", "style", "noscript", "iframe"]):
        tag.decompose()
    # drop TOC frameset junk
    for tag in soup.find_all(["frame", "frameset"]):
        tag.decompose()
    # inline anchors kept; remove event attrs
    for el in soup(True):
        for attr in list(el.attrs):
            if attr.lower().startswith("on"):
                del el.attrs[attr]
    return str(soup)

def html_to_markdown(html: str) -> str:
    # Convert using markdownify with sensible defaults
    return md(html, heading_style="ATX", strip=["img", "svg"])

def guess_title(soup: BeautifulSoup, default: str) -> str:
    if soup.title and soup.title.string:
        return soup.title.string.strip()
    h1 = soup.find(["h1", "h2"])
    if h1 and h1.get_text(strip=True):
        return h1.get_text(strip=True)
    return default

def rel_path(path: Path, base: Path) -> str:
    return str(path.relative_to(base)).replace("\\", "/")

def chunk_text(text: str, size: int = 2000, overlap: int = 200):
    chunks = []
    i = 0
    n = len(text)
    while i < n:
        end = min(i + size, n)
        chunk = text[i:end]
        chunks.append(chunk)
        i = end - overlap if end - overlap > i else end
    return chunks

def sha1(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8", errors="ignore")).hexdigest()

def ensure_dir(p: Path):
    p.parent.mkdir(parents=True, exist_ok=True)

# --- Main conversion ---

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src", required=True, help="Path to decompiled CHM folder (HTML files).")
    ap.add_argument("--out", dest="out", required=True, help="Output folder for Markdown + indexes.")
    ap.add_argument("--make-jsonl", action="store_true", help="Also produce chunks.jsonl for RAG pipelines.")
    ap.add_argument("--chunk-size", type=int, default=2000)
    ap.add_argument("--chunk-overlap", type=int, default=200)
    args = ap.parse_args()

    src = Path(args.src).resolve()
    out = Path(args.out).resolve()
    md_root = out
    md_root.mkdir(parents=True, exist_ok=True)

    index_path = md_root / "index.jsonl"
    chunks_path = md_root / "chunks.jsonl"

    # Wipe old indexes
    if index_path.exists():
        index_path.unlink()
    if chunks_path.exists():
        chunks_path.unlink()

    all_html = [p for p in src.rglob("*") if p.suffix.lower() in {".htm", ".html"}]
    with open(index_path, "a", encoding="utf-8") as index_fp:
        if args.make_jsonl:
            chunks_fp = open(chunks_path, "a", encoding="utf-8")
        else:
            chunks_fp = None

        for fp in tqdm(all_html, desc="Converting HTML → MD"):
            raw = read_text(fp)
            cleaned = clean_html(raw)
            soup = BeautifulSoup(cleaned, "lxml")
            title = guess_title(soup, default=fp.stem.replace("_", " ").strip())
            md_text = html_to_markdown(cleaned).strip()

            # Write .md mirroring structure
            rel = rel_path(fp, src)
            md_rel = re.sub(r"\.html?$", ".md", rel, flags=re.I)
            md_out = md_root / md_rel
            ensure_dir(md_out)
            md_out.write_text(md_text, encoding="utf-8")

            # Index entry
            doc_id = sha1(md_rel + title)
            rec = {
                "id": doc_id,
                "title": title,
                "path_md": md_rel,
                "path_html": rel,
                "chars": len(md_text)
            }
            index_fp.write(json.dumps(rec, ensure_ascii=False) + "\n")

            # Optional chunking
            if chunks_fp is not None:
                for i, chunk in enumerate(chunk_text(md_text, size=args.chunk_size, overlap=args.chunk_overlap)):
                    rec_c = {
                        "id": f"{doc_id}#{i}",
                        "title": title,
                        "path_md": md_rel,
                        "chunk_index": i,
                        "content": chunk
                    }
                    chunks_fp.write(json.dumps(rec_c, ensure_ascii=False) + "\n")

        if chunks_fp is not None:
            chunks_fp.close()

    print(f"✅ Done. Markdown in: {md_root}")
    print(f"   Index: {index_path}")
    if args.make_jsonl:
        print(f"   Chunks: {chunks_path}")

if __name__ == "__main__":
    main()

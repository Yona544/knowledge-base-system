#!/usr/bin/env python3
# scripts/clean_md_corpus.py
# Clean Advantage CHM-derived Markdown, add front matter, rewrite links, and emit enriched JSONL indexes.

import argparse
import hashlib
import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Dict, Optional


# ----------------------------
# Config and heuristics
# ----------------------------

TOKEN_CHARS = 4  # heuristic chars per token
TARGET_TOKENS = 700
OVERLAP_RATIO = 0.15
TARGET_CHARS = int(TARGET_TOKENS * TOKEN_CHARS)
OVERLAP_CHARS = int(TARGET_CHARS * OVERLAP_RATIO)

PRODUCT_HEADER_RX = re.compile(r"^\s*Advantage Database Server\s+\d+\s*$", re.IGNORECASE | re.MULTILINE)
FEEDBACK_RX = re.compile(r"Feedback on:", re.IGNORECASE)
EMPTY_CELL_ROW_RX = re.compile(r"^\s*\|\s*\|\s*$")
EMPTY_SEP_ROW_RX = re.compile(r"^\s*\|\s*---\s*\|\s*$")
ONLY_SEP_ROW_RX = re.compile(r"^\s*\|(?:\s*-{3,}\s*\|)+\s*$")
ONLY_PIPE_SPACES_RX = re.compile(r"^\s*\|(?:\s*\|\s*)+\s*$")
BULLET_DOT_RX = re.compile(r"^\s*·\s+")
TABLE_BULLET_ROW_RX_2COL = re.compile(r"^\s*\|\s*[·\-\*]\s*\|\s*(.*?)\s*\|\s*$")
TABLE_BULLET_ROW_RX_ANYCOL = re.compile(r"^\s*\|\s*[·\-\*]\s*\|([^|]+)\|.*$")
MD_HEADING_RX = re.compile(r"^(#{1,6})\s+(.*)$")
CODE_FENCE_RX = re.compile(r"^```")
JAVASCRIPT_LINK_RX = re.compile(r"\[([^\]]+)\]\(\s*javascript:[^)]+\)")
# Find markdown link targets and rewrite .htm/.html -> .md
MD_LINK_TARGET_RX = re.compile(r"(\]\()([^)\s]+?)(\.html?)(#.*?)?\)", re.IGNORECASE)

# Do not process these filenames
EXCLUDE_BASENAMES = {"_audit.md", "_sanitizer_spec.md"}

# Prefix -> component mapping
PREFIX_COMPONENT = {
    "ace_": "Advantage Client Engine",
    "ade_": "Advantage TDataSet Descendant",
    "arc_": "Advantage Data Architect",
    "crystal_": "Crystal Reports",
    "devguide_": "Developer’s Guide",
}

# ----------------------------
# Data structures
# ----------------------------

@dataclass
class FrontMatter:
    title: str
    slug: str
    product: str
    component: str
    version: str
    category: str
    original_path_html: str
    source: str
    tags: List[str]
    checksum: str


@dataclass
class ChunkRec:
    id: str
    doc_id: str
    path_md: str
    title: str
    heading_path: List[str]
    anchor: str
    start_char: int
    end_char: int
    token_estimate: int
    content: str


# ----------------------------
# Utilities
# ----------------------------

def read_text(fp: Path) -> str:
    try:
        return fp.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return fp.read_text(encoding="cp1252", errors="ignore")


def write_text(fp: Path, text: str):
    fp.parent.mkdir(parents=True, exist_ok=True)
    fp.write_text(text, encoding="utf-8")


def sha1(s: str) -> str:
    return hashlib.sha1(s.encode("utf-8", errors="ignore")).hexdigest()


def est_tokens(chars: int) -> int:
    return max(1, (chars + TOKEN_CHARS - 1) // TOKEN_CHARS)


def to_slug(text: str) -> str:
    base = text.strip().lower()
    base = re.sub(r"\s+", "-", base)
    base = re.sub(r"[^a-z0-9\-]+", "", base)
    base = re.sub(r"-{2,}", "-", base).strip("-")
    return base


def derive_component_from_name(name: str) -> str:
    lower = name.lower()
    for prefix, comp in PREFIX_COMPONENT.items():
        if lower.startswith(prefix):
            return comp
    return "Advantage"


def derive_category(name: str, first_heading: Optional[str]) -> str:
    nlow = name.lower()
    hlow = (first_heading or "").lower()
    if nlow.startswith(("ace_", "ade_", "arc_", "crystal_")) or (hlow.startswith("ads") or hlow.startswith("tads")):
        return "API"
    if "overview" in hlow or "quick start" in hlow or "guide" in hlow:
        return "Guide"
    return "Reference"


def derive_tags(name: str, component: str) -> List[str]:
    tags = []
    prefix = name.split("_", 1)[0].lower() if "_" in name else name.split("-", 1)[0].lower()
    if prefix:
        tags.append(prefix)
    if component and component != "Advantage":
        tags.append(to_slug(component))
    return tags


def first_heading_title(clean_body: str) -> Optional[str]:
    for line in clean_body.splitlines():
        m = MD_HEADING_RX.match(line)
        if m:
            return m.group(2).strip()
    return None


def format_front_matter(fm: FrontMatter) -> str:
    tags_yaml = "\n".join([f"  - {t}" for t in fm.tags]) if fm.tags else ""
    return (
        "---\n"
        f"title: {fm.title}\n"
        f"slug: {fm.slug}\n"
        f"product: {fm.product}\n"
        f"component: {fm.component}\n"
        f"version: \"{fm.version}\"\n"
        f"category: {fm.category}\n"
        f"original_path_html: {fm.original_path_html}\n"
        f"source: {fm.source}\n"
        f"tags:\n{tags_yaml}\n"
        f"checksum: {fm.checksum}\n"
        "---\n\n"
    )


def rewrite_javascript_links(text: str) -> str:
    # Replace [Label](javascript:...) -> Label
    return JAVASCRIPT_LINK_RX.sub(lambda m: m.group(1), text)


def rewrite_html_links_to_md(text: str) -> str:
    def _sub(m: re.Match) -> str:
        pre = m.group(1)   # ](
        url_base = m.group(2)  # path without extension
        ext = m.group(3)   # .htm or .html
        frag = m.group(4) or ""  # optional #...
        return f"{pre}{url_base}.md{frag})"
    return MD_LINK_TARGET_RX.sub(_sub, text)


def collapse_blank_lines(text: str) -> str:
    # Reduce 3+ blank lines to 1
    return re.sub(r"\n{3,}", "\n\n", text)


def compute_anchors(clean_body: str) -> Dict[str, str]:
    # generate stable anchors for each heading; return mapping from heading text -> unique anchor
    anchors: Dict[str, str] = {}
    used: Dict[str, int] = {}

    for line in clean_body.splitlines():
        m = MD_HEADING_RX.match(line)
        if not m:
            continue
        heading_text = m.group(2).strip()
        base = to_slug(heading_text)
        if base in used:
            used[base] += 1
            anchor = f"{base}-{used[base]}"
        else:
            used[base] = 1
            anchor = base
        anchors[heading_text] = anchor
    return anchors


def convert_table_bullet_line(line: str) -> Optional[str]:
    m = TABLE_BULLET_ROW_RX_2COL.match(line)
    if m:
        content = m.group(1).strip()
        return f"- {content}"
    m2 = TABLE_BULLET_ROW_RX_ANYCOL.match(line)
    if m2:
        content = m2.group(1).strip()
        return f"- {content}"
    return None


def clean_md(text: str) -> str:
    """
    Line-oriented cleaning while respecting code fences.
    - Remove product header lines and 'Feedback on' lines
    - Remove table-only scaffolding rows
    - Convert table bullet rows to markdown bullets
    - Normalize leading '·' bullets
    - Rewrite javascript links and .htm/.html targets
    - Collapse extra blank lines
    """
    lines_out: List[str] = []
    in_code = False
    for raw in text.splitlines():
        line = raw

        if CODE_FENCE_RX.match(line):
            in_code = not in_code
            lines_out.append(line)
            continue

        if in_code:
            lines_out.append(line)
            continue

        # Remove product header lines
        if PRODUCT_HEADER_RX.match(line):
            continue

        # Remove lines with Feedback on:
        if FEEDBACK_RX.search(line):
            continue

        # Remove pure scaffolding rows
        if EMPTY_CELL_ROW_RX.match(line) or EMPTY_SEP_ROW_RX.match(line) or ONLY_SEP_ROW_RX.match(line) or ONLY_PIPE_SPACES_RX.match(line):
            continue

        # Convert bullet rows in tables to markdown bullets
        converted = convert_table_bullet_line(line)
        if converted is not None:
            lines_out.append(converted)
            continue

        # Normalize bullet dot to '- '
        if BULLET_DOT_RX.match(line):
            line = BULLET_DOT_RX.sub("- ", line)

        lines_out.append(line)

    joined = "\n".join(lines_out)
    joined = rewrite_javascript_links(joined)
    joined = rewrite_html_links_to_md(joined)
    joined = collapse_blank_lines(joined)
    return joined.strip() + "\n"


def derive_front_matter(clean_body: str, src_file: Path, root_src: Path) -> FrontMatter:
    # title
    th = first_heading_title(clean_body)
    basename = src_file.stem
    if th:
        title = th
    else:
        title = re.sub(r"[_\-]+", " ", basename).strip().title()

    slug = basename.lower()
    component = derive_component_from_name(basename)
    category = derive_category(basename, th)
    product = "Advantage Database Server"
    version = "12"
    original_path_html = f"{basename}.htm"
    source = "Advantage CHM"
    tags = derive_tags(basename, component)

    checksum = sha1(clean_body)
    return FrontMatter(
        title=title,
        slug=slug,
        product=product,
        component=component,
        version=version,
        category=category,
        original_path_html=original_path_html,
        source=source,
        tags=tags,
        checksum=checksum,
    )


def doc_id_for(path_md: str, title: str) -> str:
    return sha1(path_md + "::" + title)


def split_into_paragraphs_preserving_code(text: str) -> List[str]:
    blocks: List[str] = []
    cur: List[str] = []
    in_code = False
    for line in text.splitlines():
        if CODE_FENCE_RX.match(line):
            in_code = not in_code
            cur.append(line)
            continue
        if not in_code and line.strip() == "":
            # paragraph break
            if cur:
                blocks.append("\n".join(cur).strip() + "\n")
                cur = []
        else:
            cur.append(line)
    if cur:
        blocks.append("\n".join(cur).strip() + "\n")
    return blocks


def chunk_section(section_text: str, section_anchor: str, heading_path: List[str], path_md: str, title: str, doc_id: str, start_offset_base: int, next_chunk_index: int) -> Tuple[List[ChunkRec], int]:
    """
    Split section_text to ~TARGET_CHARS chunks with OVERLAP_CHARS overlap where needed.
    section_anchor is anchor of the section's top heading.
    heading_path is the list of headings up to this section.
    start_offset_base is the char offset at which this section starts in the whole document, used for start/end_char.
    next_chunk_index is the starting chunk index counter.
    Returns (chunks, updated_next_chunk_index)
    """
    chunks: List[ChunkRec] = []
    # If short, one chunk
    if len(section_text) <= TARGET_CHARS * 1.1:
        token_est = est_tokens(len(section_text))
        chunks.append(ChunkRec(
            id=f"{doc_id}#{next_chunk_index}",
            doc_id=doc_id,
            path_md=path_md,
            title=title,
            heading_path=heading_path[:],
            anchor=section_anchor or "top",
            start_char=start_offset_base,
            end_char=start_offset_base + len(section_text),
            token_estimate=token_est,
            content=section_text,
        ))
        return chunks, next_chunk_index + 1

    # Otherwise paragraph-based chunking with overlap
    paras = split_into_paragraphs_preserving_code(section_text)
    buf = ""
    buf_start = 0
    pos = 0
    idx = next_chunk_index
    for i, para in enumerate(paras):
        if buf == "":
            buf_start = pos
        if len(buf) + len(para) <= TARGET_CHARS:
            buf += para + ("\n" if not buf.endswith("\n") else "")
        else:
            # emit chunk
            token_est = est_tokens(len(buf))
            chunks.append(ChunkRec(
                id=f"{doc_id}#{idx}",
                doc_id=doc_id,
                path_md=path_md,
                title=title,
                heading_path=heading_path[:],
                anchor=section_anchor or "top",
                start_char=start_offset_base + buf_start,
                end_char=start_offset_base + buf_start + len(buf),
                token_estimate=token_est,
                content=buf,
            ))
            idx += 1
            # start new buffer with overlap
            # compute overlap by taking last OVERLAP_CHARS of current buf
            if OVERLAP_CHARS > 0 and len(buf) > OVERLAP_CHARS:
                overlap_part = buf[-OVERLAP_CHARS:]
                # shift start to include overlap
                buf_start = buf_start + len(buf) - OVERLAP_CHARS
                buf = overlap_part + para + ("\n" if not para.endswith("\n") else "")
            else:
                buf_start = pos
                buf = para + ("\n" if not para.endswith("\n") else "")
        pos += len(para)

    if buf.strip():
        token_est = est_tokens(len(buf))
        chunks.append(ChunkRec(
            id=f"{doc_id}#{idx}",
            doc_id=doc_id,
            path_md=path_md,
            title=title,
            heading_path=heading_path[:],
            anchor=section_anchor or "top",
            start_char=start_offset_base + buf_start,
            end_char=start_offset_base + buf_start + len(buf),
            token_estimate=token_est,
            content=buf,
        ))
        idx += 1

    return chunks, idx


def build_chunks(clean_body: str, path_md: str, title: str, anchors: Dict[str, str], doc_id: str) -> List[ChunkRec]:
    """
    Heading-aware: split by H2 sections primarily; include H1 as parent in heading_path.
    If no H2 exists, treat entire doc as one section rooted at H1 (or top).
    """
    lines = clean_body.splitlines(keepends=True)
    # Identify headings with their offsets
    headings: List[Tuple[int, int, str, str]] = []  # (char_offset, level, text, anchor)
    offset = 0
    for ln in lines:
        m = MD_HEADING_RX.match(ln.strip("\n"))
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            anchor = anchors.get(text, to_slug(text))
            headings.append((offset, level, text, anchor))
        offset += len(ln)

    chunks: List[ChunkRec] = []
    if not headings:
        # no headings; single chunk
        token_est = est_tokens(len(clean_body))
        chunks.append(ChunkRec(
            id=f"{doc_id}#0",
            doc_id=doc_id,
            path_md=path_md,
            title=title,
            heading_path=[],
            anchor="top",
            start_char=0,
            end_char=len(clean_body),
            token_estimate=token_est,
            content=clean_body,
        ))
        return chunks

    # Determine H1
    h1_text = None
    if headings and headings[0][1] == 1:
        h1_text = headings[0][2]

    # Build H2 sections ranges (start, end)
    h2_positions: List[int] = [i for i, (_, lvl, _, _) in enumerate(headings) if lvl == 2]
    if not h2_positions:
        # Single section from start to end rooted at H1
        section_text = clean_body
        heading_path = [h1_text] if h1_text else []
        section_anchor = anchors.get(h1_text, "top") if h1_text else "top"
        secs, _ = chunk_section(section_text, section_anchor, heading_path, path_md, title, doc_id, 0, 0)
        return secs

    # Build text ranges for each H2
    idx_counter = 0
    for i, idx in enumerate(h2_positions):
        start_char = headings[idx][0]
        end_char = len(clean_body)
        if i + 1 < len(h2_positions):
            end_char = headings[h2_positions[i + 1]][0]
        section_text = clean_body[start_char:end_char]
        h2_text = headings[idx][2]
        h2_anchor = headings[idx][3]
        heading_path = []
        if h1_text:
            heading_path.append(h1_text)
        heading_path.append(h2_text)
        secs, idx_counter = chunk_section(section_text, h2_anchor, heading_path, path_md, title, doc_id, start_char, idx_counter)
        chunks.extend(secs)

    return chunks


# ----------------------------
# Main
# ----------------------------

def process_file(src_fp: Path, src_root: Path, out_root: Path) -> Tuple[Dict, List[Dict]]:
    """
    Returns a tuple: (index_record, chunk_records)
    """
    rel = src_fp.relative_to(src_root)
    out_md = out_root / rel

    raw = read_text(src_fp)
    cleaned_body = clean_md(raw)

    # Front matter
    fm = derive_front_matter(cleaned_body, src_fp, src_root)
    fm_text = format_front_matter(fm)

    # Ensure H1 includes title if missing
    body = cleaned_body
    if not re.search(r"^#\s+", body, flags=re.MULTILINE):
        body = f"# {fm.title}\n\n" + body

    final_doc = fm_text + body

    # Write cleaned MD
    write_text(out_md, final_doc)

    # Index record
    path_md_rel = str(out_md.relative_to(out_root)).replace("\\", "/")
    token_estimate = est_tokens(len(body))
    index_id = doc_id_for(path_md_rel, fm.title)
    index_rec = {
        "id": index_id,
        "title": fm.title,
        "slug": fm.slug,
        "component": fm.component,
        "category": fm.category,
        "product": fm.product,
        "version": fm.version,
        "path_md": path_md_rel,
        "original_path_html": fm.original_path_html,
        "tags": fm.tags,
        "checksum": fm.checksum,
        "chars": len(body),
        "token_estimate": token_estimate,
    }

    # Chunk records (heading-aware, token-aware)
    # For anchors, use cleaned body (without front matter)
    anchors = compute_anchors(body)
    chunks: List[ChunkRec] = build_chunks(body, path_md_rel, fm.title, anchors, index_id)
    chunk_recs = []
    for c in chunks:
        chunk_recs.append({
            "id": c.id,
            "doc_id": c.doc_id,
            "path_md": c.path_md,
            "title": c.title,
            "heading_path": c.heading_path,
            "anchor": c.anchor,
            "start_char": c.start_char,
            "end_char": c.end_char,
            "token_estimate": c.token_estimate,
            "content": c.content,
        })

    return index_rec, chunk_recs


def main():
    ap = argparse.ArgumentParser(description="Clean Advantage MD corpus and emit enriched JSONL indexes.")
    ap.add_argument("--src", required=True, help="Source MD folder (e.g., knowledge-bases/advantage)")
    ap.add_argument("--out", required=True, help="Output folder for cleaned MD (e.g., knowledge-bases/advantage_clean)")
    ap.add_argument("--index", default="enriched.index.jsonl", help="Index JSONL filename")
    ap.add_argument("--chunks", default="enriched.chunks.jsonl", help="Chunks JSONL filename")
    args = ap.parse_args()

    src_root = Path(args.src).resolve()
    out_root = Path(args.out).resolve()
    out_root.mkdir(parents=True, exist_ok=True)

    # Prepare JSONL files
    index_fp = (out_root / args.index)
    chunks_fp = (out_root / args.chunks)
    if index_fp.exists():
        index_fp.unlink()
    if chunks_fp.exists():
        chunks_fp.unlink()

    md_files = sorted([p for p in src_root.rglob("*.md") if p.is_file() and p.name not in EXCLUDE_BASENAMES])

    total_docs = 0
    total_chunks = 0

    with open(index_fp, "a", encoding="utf-8") as ix, open(chunks_fp, "a", encoding="utf-8") as ch:
        for fp in md_files:
            index_rec, chunk_recs = process_file(fp, src_root, out_root)
            ix.write(json.dumps(index_rec, ensure_ascii=False) + "\n")
            for cr in chunk_recs:
                ch.write(json.dumps(cr, ensure_ascii=False) + "\n")
            total_docs += 1
            total_chunks += len(chunk_recs)

    print(f"Cleaned docs: {total_docs}")
    print(f"Chunks written: {total_chunks}")
    print(f"Index: {index_fp}")
    print(f"Chunks: {chunks_fp}")


if __name__ == "__main__":
    main()
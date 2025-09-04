# Advantage MD Sanitizer Specification

version: 1.0
generated_by: Kilo Code
applies_to: knowledge-bases/advantage
outputs:
  - knowledge-bases/advantage_clean/*.md
  - knowledge-bases/advantage_clean/enriched.index.jsonl
  - knowledge-bases/advantage_clean/enriched.chunks.jsonl

Goals
- Remove CHM artifacts and boilerplate while preserving technical content.
- Normalize bullets and layout to clean Markdown.
- Rewrite internal links to .md targets with stable anchors.
- Add YAML front matter for downstream filtering and citations.
- Generate stable heading anchors.
- Produce heading-aware, token-aware chunks for Pinecone ingestion.

Input assumptions
- Source docs are Markdown derived from CHM, with residual artifacts such as:
  - Product header lines e.g. “Advantage Database Server 12”
  - CHM breadcrumbs and “Feedback on” boilerplate
  - Table scaffolding blocks like “|  |” and “| --- |”
  - Bullet glyph “·” used in lists
  - Internal links pointing to .htm/.html files and “javascript:hhpopuplink” references

Removal rules
- Product header lines:
  - Remove lines matching regex: ^\\s*Advantage Database Server\\s+\\d+\\s*$
- Breadcrumb and “Feedback on” boilerplate:
  - Remove any line containing “Feedback on:” (case-insensitive)
  - Remove CHM breadcrumb rows that are table-only noise when they include multiple “| --- |” or “|  |” rows with no text
- Table scaffolding:
  - Remove rows that are only separators or empty cells:
    - ^\\s*\\|\\s*\\|\\s*$ 
    - ^\\s*\\|\\s*---\\s*\\|\\s*$
    - ^\\s*\\|\\s*(?:---\\s*\\|\\s*)+$
    - ^\\s*\\|\\s*(?:\\|\\s*)+$
- Javascript popup links:
  - Replace [label](javascript:...) with label (plain text)
- Excess blank lines:
  - Collapse >2 consecutive blank lines to a single blank line

Normalization rules
- Bullets:
  - Replace leading bullet glyph “·” at line start (optionally within table cells after scaffolding removal) with a Markdown dash “- ”
  - Example: “· Create tables and indexes” → “- Create tables and indexes”
- Headings:
  - Ensure ATX-style headings (#..######) are preserved; trim surrounding whitespace
- Code fences:
  - Preserve as-is; do not alter content within triple‑backtick fences

Internal link rewriting
- Convert all .htm/.html links to .md
  - Example: [AdsSeek](ace_adsseek.htm) → [AdsSeek](ace_adsseek.md)
- Anchors:
  - Preserve hash fragments (#anchor) when present
  - Example: [Click Here](ace_examples.htm#adsseekexample) → [Click Here](ace_examples.md#adsseekexample)
- If the target .md does not exist, keep the rewritten link but also add a “missing_target: true” flag in the front matter links index (not in-page)
- Remove javascript:hhpopuplink.* links; keep link text only

Front matter schema (per document)
Add YAML front matter to the top of every MD:

---
title: <best_title>
slug: <basename_without_ext>
product: Advantage Database Server
component: <derived_from_prefix_or_section>
version: "12"
category: <API|Guide|Tool|Concept|Reference>
original_path_html: <best_guess_or_empty>
source: Advantage CHM
tags:
  - <derived_tags>
checksum: <sha1_of_clean_body>
---

Derivation logic
- title:
  - First non-empty H1/H2 if present, else derive from filename by replacing underscores/hyphens with spaces and title‑casing
- slug:
  - Use basename of file (without .md), lowercased
- component:
  - Heuristics by filename prefix:
    - ace_* → Advantage Client Engine
    - ade_* → Advantage TDataSet Descendant
    - arc_* → Advantage Data Architect
    - crystal_* → Crystal Reports
    - devguide_* → Developer’s Guide
    - default → Advantage
- category:
  - If file name or first heading contains verbs like Ads*, set to API
  - If contains “Overview”, “Quick Start”, or “Guide”, set to Guide
  - Else Reference
- original_path_html:
  - <slug>.htm if source link exists; otherwise leave empty
- tags:
  - Include prefix tag (ace, ade, arc, etc.), plus simple keywords inferred from headings
- checksum:
  - SHA1 of the cleaned document body (front matter excluded)

Anchor generation
- For each heading H1..H6, compute a slug:
  - Lowercase, remove non-alphanumeric except spaces and hyphens
  - Replace spaces with hyphens; collapse repeats
  - Guarantee uniqueness within the document by appending -2, -3, … when duplicates occur
- Insert no explicit anchor tags; rely on heading IDs for path.md#anchor citations

Chunking specification
- Strategy: heading-aware + token-aware
- Target: ~700 tokens with ~15 percent overlap
- Implementation heuristic (no tokenizer dependency required):
  - Use an estimated 4 chars/token
  - Target chunk size: ~2800 chars, overlap ~420 chars
  - Split by heading sections; if a section exceeds target, split by paragraphs while respecting code fences
- For each chunk, emit record:
  - id: <doc_id>#<chunk_index>
  - doc_id: <sha1_of_path_and_title>
  - path_md: <relative_md_path>
  - title: <document_title>
  - heading_path: [H1, H2, … up to the current chunk’s deepest heading]
  - anchor: <anchor_id_of_top_heading_in_chunk>
  - start_char, end_char: offsets within cleaned document
  - token_estimate: ceil((end_char - start_char)/4)

Index records (document-level)
- enriched.index.jsonl entry:
  - id, title, slug, component, category, product, version, path_md, original_path_html, tags, checksum, chars, token_estimate

Validation and QA
- Run scripts/audit_md_corpus.py on the cleaned output to ensure the following counts drop near zero:
  - html_links, feedback_on, product_header, empty_cell_row, empty_sep_row, bullet_dot
- Manual spot-check of 20 random docs:
  - No CHM boilerplate or scaffolding
  - Bullets are Markdown dashes
  - Internal links resolve to local .md
  - YAML front matter present and correct
  - Anchors appear consistent with heading text

Notes
- Be conservative when removing tables; only strip rows that match scaffolding patterns with no alphanumerics
- Do not modify content inside code fences
- Keep Unicode content; write UTF‑8

Future enhancements
- Tokenizer-based chunking for exact token counts
- Link existence validation and auto-generation of “missing targets” report
- Optional consolidation of sub-500 character pages into parent sections to reduce vector fragmentation
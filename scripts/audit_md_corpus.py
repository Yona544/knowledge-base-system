#!/usr/bin/env python3
# scripts/audit_md_corpus.py
# Audit a Markdown corpus for CHM artifacts and link hygiene, producing an _audit.md report.

import argparse
import random
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple


PATTERNS = {
    "html_links": re.compile(r"\.html?\b", re.IGNORECASE),
    "feedback_on": re.compile(r"Feedback on:", re.IGNORECASE),
    "product_header": re.compile(r"^\\s*Advantage Database Server\\s+\\d+\\s*$", re.MULTILINE),
    "empty_cell_row": re.compile(r"^\\s*\\|\\s*\\|\\s*$", re.MULTILINE),
    "empty_sep_row": re.compile(r"^\\s*\\|\\s*---\\s*\\|\\s*$", re.MULTILINE),
    "bullet_dot": re.compile(r"·"),
}


def read_text(fp: Path) -> str:
    try:
        return fp.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return fp.read_text(encoding="cp1252", errors="ignore")


def iter_lines_with_numbers(text: str) -> List[Tuple[int, str]]:
    lines: List[Tuple[int, str]] = []
    for i, line in enumerate(text.splitlines(), start=1):
        lines.append((i, line))
    return lines


def audit_file(fp: Path, pattern_limit: int) -> Tuple[Dict[str, int], Dict[str, List[Tuple[int, str]]]]:
    text = read_text(fp)
    counts: Dict[str, int] = {}
    samples: Dict[str, List[Tuple[int, str]]] = {k: [] for k in PATTERNS.keys()}
    lines = iter_lines_with_numbers(text)

    # Count occurrences using full-text regex (including multiline as compiled)
    for key, rx in PATTERNS.items():
        matches = list(rx.finditer(text))
        counts[key] = len(matches)

    # Collect sample lines up to pattern_limit for each pattern
    for line_no, line in lines:
        for key, rx in PATTERNS.items():
            if len(samples[key]) >= pattern_limit:
                continue
            if rx.search(line):
                samples[key].append((line_no, line.strip()))

    return counts, samples


def summarize_counts(agg_counts: Dict[str, int], files_scanned: int) -> str:
    parts = []
    for key in PATTERNS.keys():
        total = agg_counts.get(key, 0)
        parts.append(f"- {key}: {total} hits")
    parts.append(f"- files_scanned: {files_scanned}")
    return "\\n".join(parts)


def main():
    ap = argparse.ArgumentParser(description="Audit an MD corpus for CHM artifacts and link hygiene.")
    ap.add_argument("src", help="Path to MD corpus root directory (e.g., knowledge-bases/advantage)")
    ap.add_argument("out", help="Path to write audit markdown (e.g., knowledge-bases/advantage/_audit.md)")
    ap.add_argument("--sample", type=int, default=200, help="Max number of files to sample (default: 200)")
    ap.add_argument("--pattern-limit", type=int, default=10, help="Max sample lines shown per pattern (default: 10)")
    ap.add_argument("--seed", type=int, default=42, help="Random seed for repeatable sampling (default: 42)")
    args = ap.parse_args()

    root = Path(args.src).resolve()
    out = Path(args.out).resolve()
    if not root.exists():
        print(f"ERROR: src not found: {root}", file=sys.stderr)
        sys.exit(2)

    files = sorted([p for p in root.rglob("*.md") if p.is_file()])
    # Exclude generated audit/spec files by convention
    files = [p for p in files if p.name not in {"_audit.md", "_sanitizer_spec.md"}]

    if not files:
        print("No .md files found", file=sys.stderr)
        sys.exit(1)

    random.seed(args.seed)
    sample_n = min(args.sample, len(files))
    sampled = random.sample(files, k=sample_n) if sample_n < len(files) else files

    overall_counts: Dict[str, int] = {k: 0 for k in PATTERNS.keys()}
    file_counts: List[Tuple[Path, int]] = []
    pattern_file_presence: Dict[str, int] = {k: 0 for k in PATTERNS.keys()}
    pattern_samples_global: Dict[str, List[Tuple[Path, int, str]]] = {k: [] for k in PATTERNS.keys()}

    for fp in sampled:
        counts, samples = audit_file(fp, args.pattern_limit)
        total_for_file = sum(counts.values())
        file_counts.append((fp, total_for_file))
        # Aggregate counts
        for k, v in counts.items():
            overall_counts[k] += v
            if v > 0:
                pattern_file_presence[k] += 1
        # Aggregate global samples (cap to pattern_limit per pattern overall)
        for k, sample_list in samples.items():
            if not sample_list:
                continue
            remaining = max(0, args.pattern_limit - len(pattern_samples_global[k]))
            if remaining <= 0:
                continue
            for (ln, txt) in sample_list[:remaining]:
                pattern_samples_global[k].append((fp, ln, txt))

    # Top files by artifact counts
    file_counts.sort(key=lambda t: t[1], reverse=True)
    top_files = file_counts[:20]

    # Write report
    out.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.utcnow().isoformat() + "Z"

    lines: List[str] = []
    lines.append(f"# Advantage MD Corpus Audit")
    lines.append("")
    lines.append(f"- generated_at: {now}")
    lines.append(f"- root: {root}")
    lines.append(f"- files_total: {len(files)}")
    lines.append(f"- files_sampled: {len(sampled)} (seed={args.seed})")
    lines.append("")
    lines.append("## Summary counts")
    lines.append("")
    lines.append(summarize_counts(overall_counts, len(sampled)))
    lines.append("")
    lines.append("## File presence (how many sampled files contain at least one hit)")
    lines.append("")
    for k in PATTERNS.keys():
        lines.append(f"- {k}: {pattern_file_presence[k]} / {len(sampled)}")
    lines.append("")
    lines.append("## Top files by total artifact hits")
    lines.append("")
    for fp, total in top_files:
        rel = fp.relative_to(root)
        lines.append(f"- {rel} : {total}")
    lines.append("")
    lines.append("## Sample lines per pattern")
    lines.append("")
    for k in PATTERNS.keys():
        lines.append(f"### {k}")
        lines.append("")
        samples = pattern_samples_global[k]
        if not samples:
            lines.append("- no samples")
            lines.append("")
            continue
        for (fp, ln, txt) in samples:
            rel = fp.relative_to(root)
            snippet = txt.strip()
            if len(snippet) > 200:
                snippet = snippet[:200] + "..."
            lines.append(f"- {rel}:{ln} | {snippet}")
        lines.append("")

    out.write_text("\\n".join(lines), encoding="utf-8")
    print(f"Audit written to: {out}")


if __name__ == "__main__":
    main()
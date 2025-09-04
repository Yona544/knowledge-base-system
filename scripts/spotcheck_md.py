#!/usr/bin/env python3
# scripts/spotcheck_md.py
# Spot-check a subset of cleaned Markdown files for CHM artifacts and link issues.

import argparse
import random
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

# Patterns to check should be near-zero in cleaned output
PATTERNS = {
    "html_links": re.compile(r"\\.html?\\b", re.IGNORECASE),
    "feedback_on": re.compile(r"Feedback on:", re.IGNORECASE),
    "product_header": re.compile(r"^\\s*Advantage Database Server\\s+\\d+\\s*$", re.MULTILINE),
    "empty_cell_row": re.compile(r"^\\s*\\|\\s*\\|\\s*$", re.MULTILINE),
    "empty_sep_row": re.compile(r"^\\s*\\|\\s*---\\s*\\|\\s*$", re.MULTILINE),
    "bullet_dot": re.compile(r"^\\s*·\\s+", re.MULTILINE),
}

EXCLUDE = {"_audit.md", "_sanitizer_spec.md", "_spotcheck.md"}

def read_text(fp: Path) -> str:
    try:
        return fp.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return fp.read_text(encoding="cp1252", errors="ignore")

# New: strip YAML front matter (at file start) and code fences from analysis
def strip_front_matter_and_code(text: str) -> str:
    lines = text.splitlines()
    out_lines: List[str] = []
    in_yaml = False
    in_code = False
    i = 0
    # YAML front matter only if starts at top with ---
    if lines and lines[0].strip() == "---":
        in_yaml = True
        i = 1
        while i < len(lines):
            if lines[i].strip() == "---":
                in_yaml = False
                i += 1
                break
            i += 1
    # Process remaining lines with code-fence stripping
    for j in range(i, len(lines)):
        line = lines[j]
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        out_lines.append(line)
    return "\n".join(out_lines)

def audit_file(fp: Path, max_samples: int) -> Tuple[Dict[str, int], Dict[str, List[Tuple[int, str]]]]:
    text_full = read_text(fp)
    text = strip_front_matter_and_code(text_full)
    counts: Dict[str, int] = {}
    samples: Dict[str, List[Tuple[int, str]]] = {k: [] for k in PATTERNS.keys()}
    lines = text.splitlines()
    # Count matches
    for key, rx in PATTERNS.items():
        counts[key] = len(list(rx.finditer(text)))
    # Sample offending lines
    for idx, line in enumerate(lines, start=1):
        for key, rx in PATTERNS.items():
            if len(samples[key]) >= max_samples:
                continue
            if rx.search(line):
                samples[key].append((idx, line.strip()))
    return counts, samples

def summarize_total(counts_agg: Dict[str, int]) -> str:
    return "\\n".join([f"- {k}: {v}" for k, v in counts_agg.items()])

def main():
    ap = argparse.ArgumentParser(description="Spot-check 20 random MD files for residual artifacts.")
    ap.add_argument("src", help="Cleaned MD root (e.g., knowledge-bases/advantage_clean)")
    ap.add_argument("out", help="Spotcheck report path (e.g., knowledge-bases/advantage_clean/_spotcheck.md)")
    ap.add_argument("--sample", type=int, default=20, help="Number of files to sample (default 20)")
    ap.add_argument("--pattern-samples", type=int, default=5, help="Max sample lines per pattern (default 5)")
    ap.add_argument("--seed", type=int, default=7, help="Random seed (default 7)")
    args = ap.parse_args()

    root = Path(args.src).resolve()
    out = Path(args.out).resolve()
    if not root.exists():
        print(f"ERROR: src not found: {root}", file=sys.stderr)
        sys.exit(2)

    md_files = sorted([p for p in root.rglob("*.md") if p.is_file() and p.name not in EXCLUDE])
    if not md_files:
        print("No .md files found", file=sys.stderr)
        sys.exit(1)

    random.seed(args.seed)
    sample_n = min(args.sample, len(md_files))
    sampled = random.sample(md_files, k=sample_n)

    totals: Dict[str, int] = {k: 0 for k in PATTERNS.keys()}
    per_file_results: List[Tuple[Path, Dict[str, int]]] = []
    sample_lines: Dict[str, List[Tuple[Path, int, str]]] = {k: [] for k in PATTERNS.keys()}

    for fp in sampled:
        counts, samples = audit_file(fp, args.pattern_samples)
        per_file_results.append((fp, counts))
        for k, v in counts.items():
            totals[k] += v
        for k, lst in samples.items():
            for (ln, txt) in lst:
                if len(sample_lines[k]) < args.pattern_samples:
                    sample_lines[k].append((fp, ln, txt))

    # Verdict
    total_hits = sum(totals.values())
    verdict = "PASS" if total_hits == 0 else "REVIEW"

    # Write report
    out.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.utcnow().isoformat() + "Z"
    lines: List[str] = []
    lines.append("# Advantage Cleaned MD Spot-check")
    lines.append("")
    lines.append(f"- generated_at: {now}")
    lines.append(f"- root: {root}")
    lines.append(f"- files_sampled: {len(sampled)} of {len(md_files)}")
    lines.append(f"- verdict: {verdict}")
    lines.append("")
    lines.append("## Aggregate counts")
    lines.append("")
    lines.append(summarize_total(totals))
    lines.append("")
    lines.append("## Per-file totals")
    lines.append("")
    for fp, cdict in per_file_results:
        subtotal = sum(cdict.values())
        rel = fp.relative_to(root)
        lines.append(f"- {rel} : {subtotal} ({', '.join([f'{k}={v}' for k, v in cdict.items() if v])})")
    lines.append("")
    lines.append("## Sample offending lines (by pattern)")
    lines.append("")
    for k, samples in sample_lines.items():
        lines.append(f"### {k}")
        if not samples:
            lines.append("- none")
            lines.append("")
            continue
        for (fp, ln, txt) in samples:
            rel = fp.relative_to(root)
            snippet = txt if len(txt) < 200 else txt[:200] + "..."
            lines.append(f"- {rel}:{ln} | {snippet}")
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Spotcheck written to: {out}")
    print(f"Verdict: {verdict}")
    print(summarize_total(totals))

if __name__ == "__main__":
    main()
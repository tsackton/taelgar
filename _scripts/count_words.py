#!/usr/bin/env python3
"""
Count "words" in Markdown files under a path, but only counting each *unique line*
once across the entire corpus.

Exclusions:
- YAML frontmatter at the top of the file (between leading --- ... ---)
- Callout/blockquote lines (any line whose first non-whitespace char is '>')

Word counting rule:
- Tokens are sequences of non-whitespace characters (len(text.split()))

Uniqueness rule:
- Deduped per line across *all files*. A duplicate line contributes words only the
  first time it is seen (deterministic because files are processed in sorted order).
- Lines are normalized with rstrip() (trailing whitespace ignored).
Prints: <deduped_word_count>\t<path>
"""

from __future__ import annotations

import argparse
from pathlib import Path


def strip_yaml_frontmatter(text: str) -> str:
    """Remove YAML frontmatter only if it appears at the very top of the file."""
    lines = text.splitlines()
    if not lines:
        return text

    if lines[0].strip() != "---":
        return text

    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[i + 1 :])
    return text


def count_tokens_by_whitespace(text: str) -> int:
    """Counts tokens as sequences of non-whitespace characters."""
    return len(text.split())


def iter_markdown_files(root: Path):
    yield from root.rglob("*.md")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Root path to search for .md files")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Path does not exist: {root}")

    # Deterministic ordering so "first time seen" is stable run-to-run.
    md_files = sorted(p for p in iter_markdown_files(root) if p.is_file())

    seen_lines: set[str] = set()
    total_count = 0

    for md_path in md_files:
        try:
            raw = md_path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            print(f"ERROR\t{md_path}\t{e}")
            continue

        text = strip_yaml_frontmatter(raw)

        file_count = 0
        for line in text.splitlines():
            # Exclude callout/blockquote lines
            if line.lstrip().startswith(">"):
                continue

            norm = line.rstrip()  # ignore trailing whitespace differences

            # Only count words for lines we haven't seen anywhere yet
            if norm not in seen_lines:
                seen_lines.add(norm)
                file_count += count_tokens_by_whitespace(norm)

        total_count += file_count

    print(f"{total_count}\t{root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

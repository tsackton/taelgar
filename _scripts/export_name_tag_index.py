#!/usr/bin/env python3
"""Export a JSON mapping of note name -> taxonomy tag from markdown frontmatter.

Scans every markdown file under a vault root, extracts YAML frontmatter, and
keeps notes tagged with one of:
ancestry, creature, group, event, object, person, place, power, religion.

Output is sorted by target tag order above, then by note name.
If frontmatter `name` is missing/empty, the file stem is used.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable, Sequence

TARGET_TAGS: tuple[str, ...] = (
    "ancestry",
    "creature",
    "group",
    "event",
    "object",
    "person",
    "place",
    "power",
    "religion",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Vault root directory to scan (default: current directory).",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Path to output JSON file (default: stdout).",
    )
    parser.add_argument(
        "--indent",
        type=int,
        default=2,
        help="JSON indentation (default: 2).",
    )
    return parser.parse_args()


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if path.is_file():
            yield path


def split_frontmatter(text: str) -> list[str]:
    lines = text.splitlines()
    if not lines:
        return []
    first = lines[0].lstrip("\ufeff").strip()
    if first != "---":
        return []
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            return lines[1:idx]
    return []


def normalize_tag(tag: str) -> str:
    return tag.strip().strip("'\"").lstrip("#").strip().lower()


def parse_frontmatter_tags(frontmatter: Sequence[str]) -> list[str]:
    tags: list[str] = []
    collecting = False
    base_indent = 0

    for raw_line in frontmatter:
        line = raw_line.rstrip()
        stripped = line.strip()

        if collecting:
            if not stripped:
                continue
            if stripped.startswith("-"):
                candidate = normalize_tag(stripped[1:].strip())
                if candidate:
                    tags.append(candidate)
                continue
            current_indent = len(line) - len(line.lstrip())
            if current_indent > base_indent:
                continue
            collecting = False

        if stripped.startswith("tags:"):
            value = stripped[5:].strip()
            if value.startswith("[") and value.endswith("]"):
                inner = value[1:-1]
                for part in inner.split(","):
                    candidate = normalize_tag(part)
                    if candidate:
                        tags.append(candidate)
            elif value:
                candidate = normalize_tag(value)
                if candidate:
                    tags.append(candidate)
            else:
                collecting = True
                base_indent = len(line) - len(line.lstrip())

    return tags


def parse_frontmatter_name(frontmatter: Sequence[str]) -> str | None:
    for raw_line in frontmatter:
        stripped = raw_line.strip()
        if stripped.startswith("name:"):
            value = stripped[5:].strip().strip("'\"")
            return value or None
    return None


def choose_target_tag(tags: Sequence[str]) -> str | None:
    tag_set = set(tags)
    for tag in TARGET_TAGS:
        if tag in tag_set:
            return tag
    return None


def build_mapping(root: Path) -> dict[str, str]:
    records: list[tuple[str, str]] = []
    duplicate_names: list[str] = []

    for path in iter_markdown_files(root):
        try:
            raw = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue

        frontmatter = split_frontmatter(raw)
        if not frontmatter:
            continue

        tags = parse_frontmatter_tags(frontmatter)
        target_tag = choose_target_tag(tags)
        if not target_tag:
            continue

        name = parse_frontmatter_name(frontmatter) or path.stem
        records.append((name, target_tag))

    tag_order = {tag: idx for idx, tag in enumerate(TARGET_TAGS)}
    records.sort(key=lambda item: (tag_order[item[1]], item[0].casefold()))

    output: dict[str, str] = {}
    for name, tag in records:
        if name in output:
            duplicate_names.append(name)
            continue
        output[name] = tag

    if duplicate_names:
        unique = sorted(set(duplicate_names), key=str.casefold)
        print(
            f"Warning: duplicate note names skipped: {', '.join(unique)}",
            file=sys.stderr,
        )

    return output


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.exists():
        print(f"Path does not exist: {root}", file=sys.stderr)
        return 2

    mapping = build_mapping(root)
    text = json.dumps(mapping, indent=args.indent, ensure_ascii=False)

    if args.output:
        output_path = Path(args.output).expanduser().resolve()
        output_path.write_text(f"{text}\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Generate descriptive statistics for markdown notes in a vault."""

from __future__ import annotations

import argparse
import csv
import os
import re
from pathlib import Path
from typing import Iterable, List, Sequence, Tuple

CANONICAL_NOTE_TYPES: Sequence[str] = (
    "person",
    "place",
    "organization",
    "item",
    "deity",
    "species",
    "background",
    "event",
    "session-note",
    "timeline",
    "holiday",
    "meta",
    "source",
    "culture",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        required=True,
        help="Root directory of the vault to scan.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Destination CSV file for the generated statistics.",
    )
    return parser.parse_args()


def walk_markdown_files(root: Path) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d for d in dirnames if not d.startswith(".") and not d.startswith("_")
        ]
        current = Path(dirpath)
        if any(part.startswith(".") or part.startswith("_") for part in current.relative_to(root).parts):
            continue
        for name in filenames:
            if name.lower().endswith(".md"):
                yield current / name


def split_frontmatter(text: str) -> Tuple[List[str], List[str]]:
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for idx in range(1, len(lines)):
            if lines[idx].strip() == "---":
                return lines[1:idx], lines[idx + 1 :]
    return [], lines


def normalize_tag(tag: str) -> str:
    return tag.strip().lstrip("#").strip().strip("'\"")


def parse_tags_from_frontmatter(frontmatter: Sequence[str]) -> List[str]:
    tags: List[str] = []
    collecting = False
    indent_level = None
    for raw_line in frontmatter:
        line = raw_line.rstrip()
        stripped = line.strip()
        if collecting:
            if not stripped:
                continue
            if stripped.startswith("-"):
                candidate = stripped[1:].strip()
                tags.append(normalize_tag(candidate))
                continue
            current_indent = len(line) - len(line.lstrip())
            if indent_level is not None and current_indent > indent_level:
                continue
            collecting = False
            indent_level = None
        if stripped.startswith("tags:"):
            after = stripped[5:].strip()
            if after.startswith("[") and after.endswith("]"):
                content = after[1:-1]
                for part in content.split(","):
                    candidate = normalize_tag(part)
                    if candidate:
                        tags.append(candidate)
            elif after:
                candidate = normalize_tag(after)
                if candidate:
                    tags.append(candidate)
            else:
                collecting = True
                indent_level = len(line) - len(line.lstrip())
    return tags


INLINE_TAG_PATTERN = re.compile(r"(?<![\w/])#([A-Za-z0-9][A-Za-z0-9/_-]*)")


def extract_inline_tags(lines: Sequence[str]) -> List[str]:
    tags: List[str] = []
    for line in lines:
        for match in INLINE_TAG_PATTERN.finditer(line):
            tags.append(match.group(1))
    return tags


def remove_initial_callout(lines: List[str]) -> List[str]:
    trimmed = list(lines)
    start = 0
    while start < len(trimmed) and not trimmed[start].strip():
        start += 1
    if start < len(trimmed) and trimmed[start].lstrip().startswith(">"):
        end = start
        while end < len(trimmed):
            stripped = trimmed[end].strip()
            if stripped and not trimmed[end].lstrip().startswith(">"):
                break
            end += 1
        del trimmed[start:end]
    return trimmed


def strip_comments(text: str) -> str:
    result: List[str] = []
    idx = 0
    in_comment = False
    while idx < len(text):
        if not in_comment and text.startswith("%%", idx):
            in_comment = True
            idx += 2
            continue
        if in_comment:
            if text.startswith("%%", idx):
                in_comment = False
                idx += 2
            else:
                idx += 1
            continue
        result.append(text[idx])
        idx += 1
    return "".join(result)


HEADER_PATTERN = re.compile(r"^#{1,6}\s")


def count_headers(lines: Sequence[str]) -> int:
    return sum(1 for line in lines if HEADER_PATTERN.match(line.lstrip()))


WORD_PATTERN = re.compile(r"\b[\w']+\b")


def count_words(text: str) -> int:
    return len(WORD_PATTERN.findall(text))


def determine_note_type(all_tags: Sequence[str]) -> str:
    lower_tags = {tag.lower() for tag in all_tags}
    base_tags = {tag.split("/", 1)[0] for tag in lower_tags}
    for candidate in CANONICAL_NOTE_TYPES:
        if candidate in lower_tags or candidate in base_tags:
            return candidate
    return "unknown"


def determine_status_flags(all_tags: Sequence[str]) -> Tuple[int, int, int, int]:
    lower_tags = {tag.lower() for tag in all_tags}
    stub = any(tag.startswith("status/stub") for tag in lower_tags)
    cleanup = any(tag.startswith("status/cleanup") for tag in lower_tags)
    needs_work = any(tag.startswith("status/needswork") for tag in lower_tags)
    check = any(tag.startswith("status/check") for tag in lower_tags)
    return int(stub), int(cleanup), int(needs_work), int(check)


def derive_status(stub: int, cleanup: int, needs_work: int, check: int) -> str:
    if stub:
        return "stub"
    if cleanup == 0 and needs_work == 0 and check == 0:
        return "complete"
    return "in_progress"


def analyze_note(path: Path, root: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    frontmatter, body_lines = split_frontmatter(text)
    front_tags = parse_tags_from_frontmatter(frontmatter)
    inline_tags = extract_inline_tags(body_lines)
    all_tags = []
    for tag in front_tags + inline_tags:
        normalized = normalize_tag(tag)
        if normalized and normalized not in all_tags:
            all_tags.append(normalized)

    word_lines = remove_initial_callout(body_lines)
    word_text = "\n".join(word_lines)
    word_text = strip_comments(word_text)
    header_count = count_headers(word_lines)
    word_count = count_words(word_text)

    note_type = determine_note_type(all_tags)
    stub, cleanup, needs_work, check = determine_status_flags(all_tags)
    status = derive_status(stub, cleanup, needs_work, check)

    relative_path = path.relative_to(root)
    directory = str(relative_path.parent).replace("\\", "/")
    category = "root"
    if directory and directory != ".":
        top_level = relative_path.parts[0]
        category = top_level
    tags_field = ";".join(all_tags)

    return {
        "path": str(relative_path).replace("\\", "/"),
        "directory": directory if directory != "." else "",
        "category": category,
        "note_type": note_type,
        "tags": tags_field,
        "header_count": header_count,
        "word_count": word_count,
        "status_stub": stub,
        "status_needs_cleanup": cleanup,
        "status_needs_work": needs_work,
        "status_check": check,
        "status": status,
    }


def write_csv(rows: Sequence[dict], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "path",
        "directory",
        "category",
        "note_type",
        "tags",
        "header_count",
        "word_count",
        "status_stub",
        "status_needs_cleanup",
        "status_needs_work",
        "status_check",
        "status",
    ]
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def main() -> None:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Root directory does not exist or is not a directory: {root}")
    output = Path(args.output).expanduser()
    rows = [analyze_note(path, root) for path in walk_markdown_files(root)]
    write_csv(rows, output)


if __name__ == "__main__":
    main()

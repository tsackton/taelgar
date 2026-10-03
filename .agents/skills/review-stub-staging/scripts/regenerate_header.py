"""Generate the live vault Obsidian header; preview by default, write on request."""
import argparse
import datetime
import json
import os
from pathlib import Path
import re
import subprocess
import sys

import yaml


def frontmatter(text):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
    if not match:
        raise ValueError("Expected YAML frontmatter at the top")
    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        raise ValueError("Frontmatter must be a mapping")
    return match, metadata


def replace_header(text, generated):
    """Replace only a conventional title/pronunciation/info header, never body."""
    match, _ = frontmatter(text)
    body = text[match.end():]
    lines = body.splitlines(keepends=True)
    offset = 0
    while offset < len(lines) and not lines[offset].strip():
        offset += 1
    if offset < len(lines) and re.match(r"^# ", lines[offset]):
        offset += 1
        if offset < len(lines) and re.match(r"^\*\(.*\)\*\s*$", lines[offset]):
            offset += 1
        if offset < len(lines) and re.match(r"^>\[!info\]", lines[offset]):
            offset += 1
            while offset < len(lines) and lines[offset].startswith(">"):
                offset += 1
    elif offset < len(lines) and lines[offset].startswith(">"):
        raise ValueError("Unrecognized existing header; inspect before replacing")
    # Do not consume any article/comment lines, even without a blank separator.
    remainder = "".join(lines[offset:])
    newline = "\r\n" if "\r\n" in text else "\n"
    header = generated.rstrip("\r\n").replace("\r\n", "\n").replace("\n", newline)
    return text[:match.end()] + header + newline + ("" if remainder.startswith(("\n", "\r\n")) else newline) + remainder


def json_default(value):
    if isinstance(value, (datetime.date, datetime.datetime)):
        return value.isoformat()
    raise TypeError(f"Unsupported YAML value: {type(value).__name__}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("note", type=Path)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--date", help="Explicit in-world display date, YYYY-MM-DD")
    parser.add_argument("--write", action="store_true", help="Write after page approval; default prints full candidate")
    args = parser.parse_args()
    root = args.root.resolve()
    note = args.note.resolve()
    if not note.is_relative_to(root):
        raise ValueError("Target must be inside the vault")
    original_bytes = note.read_bytes()
    text = original_bytes.decode("utf-8")
    _, metadata = frontmatter(text)
    date = args.date or metadata.get("pageTargetDate")
    if not date:
        raise ValueError("Supply --date from the agreed vault/campaign display date, or set pageTargetDate; do not guess")
    files = []
    for directory, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for name in names:
            if not name.endswith(".md"):
                continue
            source = Path(directory) / name
            raw = source.read_text(encoding="utf-8")
            fm = frontmatter(raw)[1] if raw.startswith("---\n") else {}
            files.append({"path": source.relative_to(root).as_posix(), "basename": source.stem, "frontmatter": fm})
    payload = {"root": str(root), "files": files, "name": note.stem, "metadata": metadata, "date": date}
    result = subprocess.run(["node", str(Path(__file__).with_name("render_header.js"))],
                            input=json.dumps(payload, default=json_default), text=True,
                            encoding="utf-8", capture_output=True, check=True)
    candidate = replace_header(text, result.stdout)
    if args.write:
        if note.read_bytes() != original_bytes:
            raise ValueError("Target changed during generation; refusing overwrite")
        note.write_bytes(candidate.encode("utf-8"))
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stdout.write(candidate)


if __name__ == "__main__":
    main()

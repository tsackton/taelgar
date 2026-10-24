#!/usr/bin/env python3
"""Replace saved legacy headers with native fences and remove headerVersion.

Preview by default; --write applies the migration and --check detects drift.
Uses only the Python standard library. Never runs Git or legacy JavaScript.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import sys


SKIP_DIRS = {"assets", "_scripts", "_templates", "_sessions", "_Plugins", "node_modules"}
BLANKS = re.compile(r"(?:[\t ]*\r?\n)*")
MARKER = re.compile(r" {0,3}<!-- taelgar(?::|-)header -->[\t ]*(?:\r?\n|$)")
TITLE = re.compile(
    r"(?: {0,3}#(?:[\t ]+[^\r\n]*)?(?:\r?\n|$)|"
    r" {0,3}(?![\s#>`~]|[-+*][\t ]|\d+[.)][\t ])\S[^\r\n]*\r?\n"
    r" {0,3}=+[\t ]*(?:\r?\n|$))"
)
NATIVE = re.compile(r" {0,3}(`{3,}|~{3,})taelgar-header[\t ]*\r?\n")
FRONTMATTER = re.compile(r"\A\ufeff?---[\t ]*\r?\n(.*?)^---[\t ]*(?:\r?\n|$)", re.M | re.S)
HEADER_VERSION = re.compile(r"^(?:headerVersion|'headerVersion'|\"headerVersion\")[\t ]*:[^\r\n]*(?:\r?\n|$)", re.M)
SAVED_LINE = re.compile(
    r"(?:[\t ]*>[^\r\n]*|[\t ]*\*\([^\r\n]+\)\*[\t ]*|"
    r"[\t ]*`\$=dv\.view\([\"']_scripts/view/get_"
    r"(?:PageDatedValue|Affiliations|Whereabouts)[\"']\)`[\t ]*|"
    r"[\t ]*\[\[[^\]\r\n]+\]\][\t ]*)(?:\r?\n|$)"
)
CALLOUT = re.compile(r"[\t ]*(?:>[\t ]*)+\[!([^\]]+)\]", re.I)
LEGACY_VIEW = re.compile(r"`\$=dv\.view\([\"']_scripts/view/get_"
                         r"(?:PageDatedValue|Affiliations|Whereabouts)[\"']\)`")


def saved_lines_end(body: str, start: int) -> int:
    end = start
    while end < len(body):
        callout = CALLOUT.match(body, end)
        if callout and callout[1].lower() != "info":
            break
        line = SAVED_LINE.match(body, end)
        if not line or line.end() == end:
            break
        end = line.end()
    return end


def migrate_source(source: bytes, *, preserve_h1=None) -> bytes:
    """Remove headerVersion and preserve other bytes outside the leading header.

    Recognizes the layouts in core's src/bio-block.mjs: a versioned saved
    H1/pronunciation/info header, materializer marker, or existing native block
    with an optional authored H1. Does not evaluate metadata or render a header.
    preserve_h1=True retains any recognized header title; False removes it.
    None keeps existing native titles and removes saved legacy titles as before.
    """
    text = source.decode("utf-8")
    frontmatter = FRONTMATTER.match(text)
    start = frontmatter.end() if frontmatter else int(text.startswith("\ufeff"))
    prefix = text[:start]
    if frontmatter:
        # Recognize the saved header using the original metadata below, before
        # removing its version marker. Never remove body/nested-key references.
        metadata = frontmatter[1]
        for field in HEADER_VERSION.finditer(metadata):
            following = next((line for line in metadata[field.end():].splitlines()
                              if line.strip() and not line.lstrip().startswith("#")), "")
            # Version markers are single-line scalars. Do not leave an orphaned
            # multiline value or guess at its boundaries in unfamiliar YAML.
            if re.match(r"[\t ]+\S", following) or re.search(r":[\t ]*[|>][+\-0-9]*[\t ]*(?:#.*)?(?:\r?\n|$)", field[0]):
                raise ValueError("Multiline headerVersion needs manual review before removal")
        cleaned = HEADER_VERSION.sub("", metadata)
        prefix = text[:frontmatter.start(1)] + cleaned + text[frontmatter.end(1):start]
    unchanged_body = (prefix + text[start:]).encode("utf-8")
    body = text[start:]
    position = BLANKS.match(body).end()
    marker = MARKER.match(body, position)
    if marker:
        position = BLANKS.match(body, marker.end()).end()
    title = TITLE.match(body, position)
    after_title = BLANKS.match(body, title.end()).end() if title else position
    native = NATIVE.match(body, after_title)
    native_title = ""
    if native:
        native_title = body[title.start():after_title] if title and preserve_h1 is not False else ""
        fence = native[1]
        closing = re.compile(r"^ {0,3}" + re.escape(fence[0]) + "{" + str(len(fence)) +
                             r",}[\t ]*(?:\r?\n|$)", re.M).search(body, native.end())
        if not closing:
            raise ValueError("Close the taelgar-header code block")
        if body[native.end():closing.start()].strip():
            raise ValueError("Leave the taelgar-header block empty")
        # Preserve an existing native fence byte-for-byte. Explicit removal
        # deletes only its leading title and spacing, retaining the block/body.
        if not marker:
            if title and preserve_h1 is False:
                return (prefix + body[native.start():]).encode("utf-8")
            return unchanged_body
        end = closing.end()
    else:
        versioned = frontmatter and HEADER_VERSION.search(frontmatter[1])
        tagged = frontmatter and re.search(r"^tags:", frontmatter[1], re.M)
        if title:
            end = saved_lines_end(body, title.end())
            # A few saved headers have a blank before their info callout. Only
            # cross that separator when exact legacy header views identify it.
            spaced_start = BLANKS.match(body, end).end()
            spaced_callout = CALLOUT.match(body, spaced_start)
            if spaced_start > end and spaced_callout and spaced_callout[1].lower() == "info":
                spaced_end = saved_lines_end(body, spaced_start)
                if LEGACY_VIEW.search(body[spaced_start:spaced_end]):
                    end = spaced_end
            # Some older notes lost their headerVersion/tags. A known inline
            # header view in this leading header is independent evidence.
            if not (versioned and tagged) and not LEGACY_VIEW.search(body[title.end():end]):
                if marker:
                    raise ValueError("Header marker before an unrecognized saved title; inspect before migrating")
                return unchanged_body
            if preserve_h1 is True:
                native_title = title[0]
        elif marker and not title:
            end = marker.end()
        else:
            return unchanged_body
    first_newline = re.search(r"\r?\n", body[:end]) or re.search(r"\r?\n", text)
    newline = first_newline[0] if first_newline else "\n"
    if native_title and not native_title.endswith("\n"):
        native_title += newline
    suffix = body[end:]
    separator = newline if suffix and not re.match(r"[\t ]*\r?\n", suffix) else ""
    block = "```taelgar-header" + newline + "```" + newline
    return (prefix + native_title + block + separator + suffix).encode("utf-8")


def note_paths(root: Path):
    """Visit ordinary Markdown notes, including untracked notes, in stable order."""
    for directory, children, names in os.walk(root, followlinks=False):
        children[:] = sorted(name for name in children if not name.startswith(".")
                             and name not in SKIP_DIRS and not (Path(directory) / name).is_symlink())
        for name in sorted(names):
            note = Path(directory) / name
            if note.suffix.lower() == ".md" and not note.is_symlink():
                yield note


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1],
                        help="Vault root (default: this script's parent vault)")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Apply all planned header replacements")
    mode.add_argument("--check", action="store_true", help="Exit 1 if any headers need migration; never write")
    titles = parser.add_mutually_exclusive_group()
    titles.add_argument("--preserve-h1", dest="preserve_h1", action="store_true",
                        help="Keep an existing H1 above the native block, including when converting a legacy header")
    titles.add_argument("--remove-h1", dest="preserve_h1", action="store_false",
                        help="Remove the leading H1 from legacy and native headers; let the block generate the title")
    parser.set_defaults(preserve_h1=None)
    parser.add_argument("--verbose", action="store_true", help="List changed paths in deterministic order")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"Not a vault directory: {root}")
    changes = []
    errors = []
    scanned = 0
    for note in note_paths(root):
        scanned += 1
        try:
            original = note.read_bytes()
            migrated = migrate_source(original, preserve_h1=args.preserve_h1)
            if migrated != original:
                if migrate_source(migrated, preserve_h1=args.preserve_h1) != migrated:
                    raise ValueError("Migration is not idempotent")
                changes.append((note, original, migrated))
        except (OSError, ValueError) as error:
            errors.append(f"{note.relative_to(root).as_posix()}: {error}")
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print("No files written: fix the reported inputs and rerun.", file=sys.stderr)
        return 2
    if args.write:
        # Check every input again before the first write, then just before each
        # replacement, to avoid overwriting edits made during the scan.
        try:
            for note, original, _ in changes:
                if note.read_bytes() != original:
                    raise ValueError(f"{note.relative_to(root).as_posix()}: changed during scan")
            for note, original, migrated in changes:
                if note.read_bytes() != original:
                    raise ValueError(f"{note.relative_to(root).as_posix()}: changed during write; earlier files may be migrated")
                note.write_bytes(migrated)
        except (OSError, ValueError) as error:
            print(error, file=sys.stderr)
            return 2
    if args.verbose:
        for note, _, _ in changes:
            print(note.relative_to(root).as_posix())
    action = "Migrated" if args.write else "Would migrate"
    print(f"{action} {len(changes)} of {scanned} Markdown notes.")
    return int(args.check and bool(changes))


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    raise SystemExit(main())

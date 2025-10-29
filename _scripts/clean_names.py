#!/usr/bin/env python3
"""
Rename OneNote-imported files that collide with existing vault basenames.

- Indexes all Markdown basenames in --vault, EXCLUDING certain top-level dirs
  (default: _DM_, .git, .obsidian).
- Scans --onenote (your OneNote import folder) and, for any file whose basename
  collides with the vault index, proposes/appends a tag (default: " (OneNote)")
  to disambiguate. Ensures the new name does not already exist by adding a suffix
  like " (OneNote 2)" if needed.
- With --dry-run, prints what would change; without it, performs the renames.

Usage examples:
  Dry-run:
    python3 rename_onenote_collisions.py \
      --vault "/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar" \
      --onenote "/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_DM_/OneNote" \
      --dry-run

  Apply:
    python3 rename_onenote_collisions.py \
      --vault "/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar" \
      --onenote "/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_DM_/OneNote"
"""

from __future__ import annotations
import argparse
import os
import pathlib
import re
import sys
from collections import defaultdict
from typing import Iterable, List, Tuple

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Rename OneNote files that collide with vault basenames."
    )
    p.add_argument("--vault", required=True, help="Path to Obsidian vault root.")
    p.add_argument("--onenote", required=True, help="Path to OneNote import folder.")
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Show proposed changes without modifying files.",
    )
    p.add_argument(
        "--exclude",
        default="_DM_,.git,.obsidian",
        help="Comma-separated directory NAMES to exclude from the vault index "
             "(matched on any path component). Default: _DM_,.git,.obsidian",
    )
    p.add_argument(
        "--ext",
        default=".md",
        help="File extension to consider (case-insensitive). Default: .md",
    )
    p.add_argument(
        "--tag",
        default=" (OneNote)",
        help='Disambiguation tag to append to filenames. Default: " (OneNote)"',
    )
    return p.parse_args()

def normalize_ext(ext: str) -> str:
    ext = ext.strip()
    if not ext.startswith("."):
        ext = "." + ext
    return ext.lower()

def is_excluded(rel_path: pathlib.Path, excluded_names: set[str]) -> bool:
    # Exclude if any path component matches an excluded name
    return any(part in excluded_names for part in rel_path.parts)

def collect_vault_basenames(
    vault_dir: pathlib.Path,
    excluded_names: set[str],
    ext: str,
) -> defaultdict[str, List[pathlib.Path]]:
    """
    Build a mapping from lowercased basename -> list of absolute Paths,
    for files under vault_dir EXCLUDING excluded_names subtrees.
    """
    by_base = defaultdict(list)
    for root, _, files in os.walk(vault_dir):
        root_path = pathlib.Path(root)
        try:
            rel = root_path.relative_to(vault_dir)
        except ValueError:
            # Outside the vault (symlink edge case) — skip
            continue
        if is_excluded(rel, excluded_names):
            continue
        for f in files:
            if f.lower().endswith(ext):
                by_base[f.lower()].append(root_path / f)
    return by_base

def already_tagged(stem: str, tag: str) -> bool:
    """
    Return True if the stem already ends with `tag` or `tag N` (N integer).
    """
    # Build a regex like r"\s*\(OneNote\)( \d+)?$" respecting spaces in tag.
    # tag comes like " (OneNote)"; we want to check literal tag optionally followed by " N"
    tag_re = re.escape(tag)
    pat = re.compile(rf"{tag_re}( \d+)?$", re.IGNORECASE)
    return bool(pat.search(stem))

def propose_name(
    dirpath: pathlib.Path, stem: str, suffix: str, tag: str
) -> pathlib.Path:
    """
    Propose a unique filename in dirpath by appending tag, then ' tag N' if needed.
    """
    n = 0
    while True:
        candidate = f"{stem}{tag}" if n == 0 else f"{stem}{tag} {n+1}"
        cand_path = dirpath / f"{candidate}{suffix}"
        if not cand_path.exists():
            return cand_path
        n += 1

def scan_onenote_and_plan(
    onenote_dir: pathlib.Path,
    vault_index: defaultdict[str, List[pathlib.Path]],
    ext: str,
    tag: str,
) -> List[Tuple[pathlib.Path, pathlib.Path, List[pathlib.Path]]]:
    """
    For each file under onenote_dir with extension `ext`, if its basename
    collides with any key in vault_index (case-insensitive), produce a proposed
    destination path with the tag appended. Include up to 3 example collisions.
    Returns a list of (src, dst, examples).
    """
    proposals = []
    for root, _, files in os.walk(onenote_dir):
        d = pathlib.Path(root)
        for f in files:
            if not f.lower().endswith(ext):
                continue
            stem, suffix = os.path.splitext(f)
            if already_tagged(stem, tag):
                continue
            lower_name = f.lower()
            if lower_name in vault_index:
                src = d / f
                dst = propose_name(d, stem, suffix, tag)
                examples = vault_index[lower_name][:3]
                proposals.append((src, dst, examples))
    return proposals

def main() -> int:
    args = parse_args()
    vault_dir = pathlib.Path(args.vault).expanduser().resolve()
    onenote_dir = pathlib.Path(args.onenote).expanduser().resolve()
    if not vault_dir.exists():
        print(f"[error] Vault not found: {vault_dir}", file=sys.stderr)
        return 2
    if not onenote_dir.exists():
        print(f"[error] OneNote folder not found: {onenote_dir}", file=sys.stderr)
        return 2

    ext = normalize_ext(args.ext)
    excluded_names = {s.strip() for s in args.exclude.split(",") if s.strip()}
    tag = args.tag  # keep as-is (may include spaces/parentheses)

    print(f"[info] Indexing vault (excluding: {', '.join(sorted(excluded_names))}) ...")
    vault_index = collect_vault_basenames(vault_dir, excluded_names, ext)
    print(f"[info] Indexed {sum(len(v) for v in vault_index.values())} '{ext}' files (unique basenames: {len(vault_index)})")

    print(f"[info] Scanning OneNote folder for collisions ...")
    proposals = scan_onenote_and_plan(onenote_dir, vault_index, ext, tag)

    if not proposals:
        print("✅ No collisions detected against the vault outside excluded dirs.")
        return 0

    print(f"Found {len(proposals)} file(s) in OneNote that collide with vault basenames.\n")
    for src, dst, examples in proposals:
        print(f"- {src}")
        print(f"    ⇒ {dst.name}")
        if examples:
            print("    Collides with existing vault file(s) such as:")
            for e in examples:
                print(f"      • {e}")
        print()

    if args.dry_run:
        print("DRY-RUN: no changes were made.")
        return 0

    # Apply renames
    applied = 0
    errors = 0
    for src, dst, _ in proposals:
        try:
            dst.parent.mkdir(parents=True, exist_ok=True)
            src.rename(dst)
            applied += 1
        except Exception as e:
            print(f"[error] Failed to rename:\n  {src}\n  -> {dst}\n  Reason: {e}", file=sys.stderr)
            errors += 1

    print(f"\nDone. Renamed {applied} file(s).", end="")
    if errors:
        print(f" {errors} error(s) occurred.", file=sys.stderr)
        return 1
    else:
        print()
        return 0

if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Plan filename-preserving image/audio moves. Never modify the vault.

Requires PyYAML. Reports contain private reference paths: write them outside the
vault and any consumer roots. The JSON moves array may be reduced for approval;
move_assets.py re-scans selected entries before applying them.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import hashlib
import json
import os
from pathlib import Path
import posixpath
import re
import subprocess
import unicodedata
from urllib.parse import unquote

import yaml


SCHEMA_VERSION = 1
IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif", ".bmp", ".tif", ".tiff", ".heic"}
AUDIO_EXTS = {".mp3", ".m4a", ".wav", ".ogg", ".flac", ".aac", ".opus", ".webm", ".aif", ".aiff"}
TEXT_EXTS = {".md", ".canvas", ".json", ".yaml", ".yml", ".html", ".css", ".js", ".mjs", ".ts", ".py", ".rb", ".sh", ".txt", ".svg"}
EXCLUDED_ASSET_DIRS = ("assets/_incoming", "assets/pc_references")
BUCKETS = {"campaign": "campaign", "dm": "dm", "worldbuilding": "worldbuilding", "unlinked": "_unlinked"}
SKIP_DIRS = {".git", ".backups", ".secrets", ".secrets-v2", ".trash", ".venv", "node_modules", "__pycache__", ".pytest_cache"}
CODE_EXTS = {".js", ".mjs", ".ts", ".py", ".rb", ".sh", ".css", ".txt"}
WIKI = re.compile(r"!?\[\[([^\]\n]+)\]\]")
MARKDOWN = re.compile(r"!?\[[^\]\n]*\]\((<[^>\n]+>|[^)\n]+)\)")
HTML = re.compile(r"\b(?:src|href|poster)\s*=\s*['\"]([^'\"]+)['\"]", re.I)
CSS = re.compile(r"url\(\s*(['\"]?)([^)\n]+?)\1\s*\)", re.I)
FIELD = re.compile(r"^\s*(?:-\s*)?[^:\n]+:\s*(.+?)\s*$")
JSON_VALUE = re.compile(r'"[^"\n]+"\s*:\s*("(?:[^"\\]|\\.)*")')
EXTENSION = re.compile(r"\.(?:png|jpe?g|gif|webp|svg|avif|bmp|tiff?|heic|mp3|m4a|wav|ogg|flac|aac|opus|webm|aiff?)\b", re.I)


def normalize(value: str) -> str:
    return unicodedata.normalize("NFC", unquote(value)).casefold()


def under(path: str, directory: str) -> bool:
    return path == directory or path.startswith(directory + "/")


def encoded(value: object) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n"


def digest_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def outside_scan(path: Path, vault: Path, consumer_roots: list[Path]) -> None:
    resolved = path.resolve()
    for root in [vault, *consumer_roots]:
        root = root.resolve()
        if resolved == root or resolved.is_relative_to(root):
            raise ValueError("Write review files outside the vault and consumer roots to avoid private-data leaks and self-references.")


def walk_files(root: Path, *, external: bool = False):
    if root.is_file():
        yield root
        return
    def fail(error):
        raise error
    for directory, dirs, files in os.walk(root, onerror=fail, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not (Path(directory) / d).is_symlink())
        if external:
            dirs[:] = [d for d in dirs if d not in {"docs", "taelgar-static", ".website-build"}]
        for name in sorted(files):
            yield Path(directory) / name


def is_source(path: Path, relative: str) -> bool:
    if path.suffix.lower() not in TEXT_EXTS or path.is_symlink():
        return False
    if relative in {"_MoC/Data Cleaning/Unlinked Assets.md", "_scripts/worldbuilding_discussion_index.json", ".obsidian/metadata.json"}:
        return False
    if relative.startswith(".obsidian/workspace"):
        return False
    return not (relative.startswith(".obsidian/plugins/") and re.fullmatch(r"data .*\.json", path.name))


def landing_pages(vault: Path) -> set[str]:
    result = {"Campaigns/Campaigns.md", "Campaigns/Current Games.md", "Campaigns/Campaign Archive.md"}
    for path in (vault / "Campaigns").rglob("*.md"):
        parts = path.relative_to(vault).parts
        if path.stem == path.parent.name and (len(parts) == 3 or len(parts) == 4 and parts[1] == "One Shots"):
            result.add(path.relative_to(vault).as_posix())
    registry = vault / "_scripts/session_note_campaigns.json"
    if registry.exists():
        for entry in json.loads(registry.read_text())["campaigns"].values():
            folder = Path(entry["campaignRoot"])
            result.add((folder / (folder.name + ".md")).as_posix())
    return result


def source_category(relative: str, text: str, landings: set[str]) -> str:
    top = relative.split("/")[0]
    if top in {"_DM_", "_dm_notes"}:
        return "dm"
    if top == "Worldbuilding":
        return "worldbuilding"
    if top == "_sessions" or relative.startswith("Campaigns/") and "/_generated/session-notes/" in relative:
        return "campaign"
    if top.startswith(("_", ".")) or top == "assets":
        return "support"
    if relative in landings:
        return "campaign"
    if text.startswith("---\n"):
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if match:
            try:
                metadata = yaml.safe_load(match.group(1)) or {}
                tags = metadata.get("tags", []) if isinstance(metadata, dict) else []
                if isinstance(tags, str):
                    tags = [tags]
                if isinstance(tags, list) and "session-note" in tags:
                    return "campaign"
            except yaml.YAMLError:
                pass  # Conservatively treat unrecognized note metadata as regular.
    return "regular"


def ignored_paths(vault: Path, paths: list[str]) -> set[str]:
    if not (vault / ".git").exists() or not paths:
        return set()
    result = subprocess.run(["git", "check-ignore", "--no-index", "-z", "--stdin"], cwd=vault,
                            input="\0".join(paths) + "\0", capture_output=True, text=True)
    if result.returncode not in (0, 1):
        raise ValueError(result.stderr.strip())
    return set(filter(None, result.stdout.split("\0")))


def scan(vault: Path, *, media: str = "all", consumer_roots: list[Path] | None = None, state: dict | None = None) -> dict:
    vault = vault.resolve()
    consumers = sorted({p.resolve() for p in (consumer_roots or [])}, key=str)
    if media not in {"all", "images", "audio"}:
        raise ValueError("media must be all, images, or audio")
    if not (vault / "assets").is_dir():
        raise ValueError(f"No assets directory in {vault}")
    if any(not p.exists() for p in consumers):
        raise ValueError("A consumer root no longer exists")
    selected_exts = IMAGE_EXTS | AUDIO_EXTS if media == "all" else IMAGE_EXTS if media == "images" else AUDIO_EXTS
    files = list(walk_files(vault))
    assets = {}
    by_name, by_stem, by_path = defaultdict(list), defaultdict(list), defaultdict(list)
    note_stems = {normalize(p.stem) for p in files if p.suffix.lower() == ".md"}
    for path in files:
        if path.suffix.lower() not in IMAGE_EXTS | AUDIO_EXTS:
            continue
        relative = path.relative_to(vault).as_posix()
        assets[relative] = {"source": relative, "references": [], "mentions": []}
        by_name[normalize(path.name)].append(relative)
        by_stem[normalize(path.stem)].append(relative)
        by_path[normalize(relative)].append(relative)
    names = re.compile(r"(?<![\w.-])(?:" + "|".join(re.escape(n) for n in sorted(by_name, key=lambda n: (-len(n), n))) + r")(?![\w.-])") if by_name else None

    def resolve(raw: str, source: str):
        target = unquote(raw).strip().strip('<>"\'').strip("[]").split("|")[0].split("#")[0].split("?")[0].strip()
        if target.startswith("file://"):
            target = target[7:]
        elif re.match(r"^[a-z][a-z0-9+.-]*:|^//", target, re.I):
            return [], "external", target
        target = target.replace("\\", "/")
        if target.startswith(str(vault) + "/"):
            target = target[len(str(vault)) + 1:]
        if "/" in target:
            candidates = [target.lstrip("/"), posixpath.normpath(posixpath.join(posixpath.dirname(source), target))]
            if target.startswith(("./", "../")):
                candidates.reverse()
            for candidate in candidates:
                matches = by_path.get(normalize(candidate), [])
                if matches:
                    return matches, "path" if len(matches) == 1 else "ambiguous", target
        matches = by_name.get(normalize(posixpath.basename(target)), [])
        extensionless = not Path(target).suffix
        if extensionless and normalize(Path(target).name) in note_stems:
            return [], "note", target
        if not matches and extensionless:
            matches = by_stem.get(normalize(posixpath.basename(target)), [])
        if matches:
            ambiguous = len(matches) != 1
            return matches, "ambiguous" if ambiguous else "stale-path" if "/" in target else "bare", target
        return [], "missing", target

    sources = {p.relative_to(vault).as_posix(): (p, False) for p in files if is_source(p, p.relative_to(vault).as_posix())}
    for root in consumers:
        for path in walk_files(root, external=True):
            if is_source(path, path.name):
                if not path.is_relative_to(vault):
                    sources[str(path)] = (path, True)
    landings = landing_pages(vault)
    hashes, drawing_stems = {}, set()
    for source, (path, external) in sorted(sources.items()):
        raw = path.read_bytes()
        text = raw.decode("utf8", errors="replace")
        category = "support" if external else source_category(source, text, landings)
        code = external or path.suffix.lower() in CODE_EXTS or source.startswith(".obsidian/")
        if path.suffix.lower() == ".md" and "excalidraw" in text[:2000].lower():
            drawing_stems.add(normalize(path.stem.removesuffix("-details").removesuffix(".excalidraw")))
        found = False
        for number, line in enumerate(text.splitlines(), 1):
            if "[[" not in line and not EXTENSION.search(unquote(line)):
                continue
            spans = []
            tokens = []
            for style, pattern in [("wiki", WIKI), ("markdown", MARKDOWN), ("html", HTML), ("css", CSS), ("json", JSON_VALUE), ("field", FIELD)]:
                for match in pattern.finditer(line):
                    value = match.group(2) if style == "css" else match.group(1)
                    if style == "json":
                        try:
                            value = json.loads(value)
                        except json.JSONDecodeError:
                            value = value[1:-1].replace("\\/", "/")
                    if style == "markdown" and not value.startswith("<"):
                        value = re.split(r"\s+['\"]", value, 1)[0]
                    if style == "wiki" or EXTENSION.search(unquote(value)):
                        tokens.append((match.start(), match.end(), style, value))
            for start, end, style, value in tokens:
                if any(a <= start and end <= b for a, b in spans):
                    continue
                matches, resolution, target = resolve(value, source)
                if matches or resolution in {"external", "note"}:
                    spans.append((start, end))
                for relative in matches:
                    found = True
                    assets[relative]["references"].append({"source": source, "line": number, "category": category,
                        "style": style, "target": target, "resolution": resolution, "code": code})
            remaining = list(line)
            for start, end in spans:
                remaining[start:end] = " " * (end - start)
            if names:
                for match in names.finditer(normalize("".join(remaining))):
                    for relative in by_name[match.group()]:
                        found = True
                        assets[relative]["mentions"].append({"source": source, "line": number, "category": category})
        if found:
            hashes[source] = hashlib.sha256(raw).hexdigest()

    moves, held, summary = [], [], Counter()
    for relative, item in sorted(assets.items()):
        if not under(relative, "assets") or Path(relative).suffix.lower() not in selected_exts:
            continue
        if any(under(relative, directory) for directory in EXCLUDED_ASSET_DIRS):
            summary["excluded"] += 1
            continue
        refs = item["references"]
        mentions = item["mentions"]
        for field in ("references", "mentions"):
            item[field] = sorted({json.dumps(r, sort_keys=True): r for r in item[field]}.values(), key=lambda r: (r["source"], r["line"], json.dumps(r, sort_keys=True)))
        refs, mentions = item["references"], item["mentions"]
        roles = {r["category"] for r in refs} - {"support"}
        category = "regular" if "regular" in roles else next(iter(roles)) if len(roles) == 1 else "mixed" if roles else "support" if refs or mentions else "unlinked"
        summary[category] += 1
        current = Path(relative).parts[1] if len(Path(relative).parts) > 2 else ""
        destination = None
        if category in BUCKETS and current != BUCKETS[category]:
            destination = f"assets/{BUCKETS[category]}/{Path(relative).name}"
        elif category in {"regular", "mixed"} and current in BUCKETS.values():
            destination = f"assets/{Path(relative).name}"
        if destination is None:
            continue
        blockers = []
        if len(by_name[normalize(Path(relative).name)]) != 1:
            blockers.append("duplicate-filename")
        if any(r["resolution"] != "bare" or r["style"] in {"markdown", "html", "css"} for r in refs):
            blockers.append("path-dependent-or-ambiguous-reference")
        if any(r["code"] for r in refs):
            blockers.append("code-or-config-reference")
        if mentions:
            blockers.append("unparsed-filename-mention")
        if any(normalize(Path(relative).stem).startswith(stem) for stem in drawing_stems) or "/excalidraw/" in relative:
            blockers.append("editable-drawing-relationship")
        source_path = vault / relative
        if source_path.is_symlink() or any(parent.is_symlink() for parent in source_path.parents if parent != vault and parent.is_relative_to(vault)):
            blockers.append("symlink")
        if (vault / destination).exists():
            blockers.append("destination-exists")
        if any(r["source"] == relative for asset in assets.values() for r in asset["references"]):
            blockers.append("asset-has-outgoing-references")
        evidence = {"references": refs, "mentions": mentions,
                    "sourceHashes": {s: hashes[s] for s in sorted({r["source"] for r in refs + mentions})}}
        move = {"source": relative, "destination": destination, "category": category,
                "media": "image" if source_path.suffix.lower() in IMAGE_EXTS else "audio",
                "bytes": source_path.stat().st_size, "sha256": digest_file(source_path),
                "evidenceSha256": hashlib.sha256(encoded(evidence).encode()).hexdigest(),
                "references": refs, "mentions": mentions}
        if blockers:
            held.append({**move, "blockers": sorted(set(blockers))})
        else:
            moves.append(move)
    ignored = ignored_paths(vault, [p for move in moves for p in (move["source"], move["destination"])])
    for move in moves[:]:
        if move["source"] in ignored and move["destination"] not in ignored:
            moves.remove(move)
            held.append({**move, "blockers": ["would-expose-git-ignored-asset"]})
    if state is not None:
        state.update({"assets": assets, "sourceHashes": hashes})
    return {"schemaVersion": SCHEMA_VERSION, "vault": str(vault),
            "policy": {"media": media, "excludedAssetDirs": list(EXCLUDED_ASSET_DIRS), "consumerRoots": [str(p) for p in consumers]},
            "summary": dict(sorted(summary.items())), "moves": moves,
            "held": sorted(held, key=lambda m: m["source"])}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True, help="JSON move proposal outside the vault")
    parser.add_argument("--media", choices=("all", "images", "audio"), default="all")
    parser.add_argument("--consumer-root", type=Path, action="append", default=[], help="Also search an external code directory or config file; repeatable")
    args = parser.parse_args()
    try:
        outside_scan(args.output, args.vault.resolve(), [p.resolve() for p in args.consumer_root])
        result = scan(args.vault, media=args.media, consumer_roots=args.consumer_root)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded(result), encoding="utf8")
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, f"Scan failed: {error}\n")
    print(f"{len(result['moves'])} proposed moves; {len(result['held'])} held for review. {args.output}")


if __name__ == "__main__":
    main()

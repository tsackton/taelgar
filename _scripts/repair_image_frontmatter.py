#!/usr/bin/env python3
"""Preview or apply repairs to top-level YAML image properties (Python 3.10+, PyYAML).

Default: read-only check. --output writes a deterministic review outside the vault.
--replacements reads {"Note.md": "assets/selected.png"}; choices are never inferred.
--apply REVIEW applies only its reviewed changes, after checking current evidence.
No assets, body links, recap fields, Leaflet declarations, or audio are modified.
Mechanical repairs preserve tags and all other metadata exactly.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import difflib
import hashlib
import json
import os
from pathlib import Path
import posixpath
import re
import tempfile
import unicodedata
from urllib.parse import unquote

import yaml

from find_misplaced_images import IMAGE_EXTS, encoded, outside_scan, walk_files


SCHEMA = 1
WIKI = re.compile(r"!?\[\[([^\]\n]+)\]\]")
HEADER = re.compile(r"\A(?:\ufeff)?---[ \t]*\r?\n(?P<yaml>.*?)(?P<close>^---[ \t]*(?:\r?\n|$))", re.S | re.M)
INFRASTRUCTURE = {".obsidian", ".agents", ".codex", "_scripts"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def key(value: str) -> str:
    return unicodedata.normalize("NFC", unquote(value)).casefold()


def safe_path(vault: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError(f"Expected a vault-relative path: {relative!r}")
    path = vault / relative
    if not path.resolve().is_relative_to(vault) or any(p.is_symlink() for p in [path, *path.parents] if p != vault):
        raise ValueError(f"Unsafe or symlink path: {relative}")
    return path


class ImageIndex:
    """Resolve conservatively: no basename fallback for a stale explicit path."""

    def __init__(self, vault: Path):
        self.vault = vault
        self.files = sorted(p.relative_to(vault).as_posix() for p in walk_files(vault)
                            if p.is_file() and not p.is_symlink())
        self.images = [p for p in self.files if Path(p).suffix.lower() in IMAGE_EXTS]
        self.paths, self.names, self.stems = defaultdict(list), defaultdict(list), defaultdict(list)
        for path in self.files:
            self.paths[key(path)].append(path)
            self.names[key(Path(path).name)].append(path)
            self.stems[key(Path(path).stem)].append(path)

    def resolve(self, value: str, note: str) -> dict:
        match = WIKI.fullmatch(value.strip())
        linked = bool(match)
        target = (match.group(1).replace(r"\|", "|").split("|", 1)[0] if match else value).strip()
        target = unquote(target).split("#", 1)[0]
        if re.match(r"^[a-z][a-z0-9+.-]*:|^//", target, re.I):
            return {"status": "external", "target": target, "matches": [], "linked": linked}
        if not target or any(c in target for c in "[]|\n\r"):
            return {"status": "unsupported", "target": target, "matches": [], "linked": linked}
        if "/" in target:
            candidates = [target.lstrip("/"), posixpath.normpath(posixpath.join(posixpath.dirname(note), target))]
            if target.startswith(("./", "../")):
                candidates.reverse()
            matches = next((self.paths[key(p)] for p in candidates if self.paths.get(key(p))), [])
            # Obsidian also accepts an unambiguous partial path such as maps/a.png.
            if not matches and not target.startswith(("/", "./", "../")):
                matches = [p for p in self.files if key(p).endswith("/" + key(target))]
        else:
            matches = self.names.get(key(target), [])
            if not matches and not Path(target).suffix:
                matches = self.stems.get(key(target), [])
        status = "missing" if not matches else "ambiguous" if len(matches) > 1 else "valid"
        if status == "valid" and matches[0] not in self.images:
            status = "not-image"
        return {"status": status, "target": target, "matches": matches, "linked": linked}

    def link(self, image: str) -> str:
        # Use a basename only when it uniquely identifies the file in the vault.
        target = Path(image).name if len(self.names[key(Path(image).name)]) == 1 else image
        if any(c in target for c in "[]|#\n\r"):
            raise ValueError("Image filename cannot be represented safely as a wikilink")
        return "[[" + target + "]]"

    def suggestions(self, old: str, note: str, body: str, matches: list[str]) -> list[dict]:
        result = {}
        for match in re.finditer(r"!\[\[([^\]\n]+)\]\]|!\[[^\]\n]*\]\(([^)\n]+)\)", body):
            raw = match.group(0) if match.group(1) else match.group(2).strip("<>")
            resolved = self.resolve(raw, note)
            if resolved["status"] == "valid":
                result.setdefault(resolved["matches"][0], "embedded-in-note")
        for image in matches:
            if image in self.images:
                result.setdefault(image, "ambiguous-match")
        stem = key(Path(old).stem)
        ranked = sorted(self.images, key=lambda p: (-difflib.SequenceMatcher(None, stem, key(Path(p).stem)).ratio(), p))
        for image in ranked:
            if difflib.SequenceMatcher(None, stem, key(Path(image).stem)).ratio() >= .7:
                result.setdefault(image, "similar-filename")
            if len(result) >= 5:
                break
        return [{"image": p, "reason": reason} for p, reason in result.items()][:8]


def parse_header(text: str):
    match = HEADER.match(text)
    if not match:
        raise ValueError("Frontmatter is missing its closing delimiter")
    content = match.group("yaml")
    root = yaml.compose(content, Loader=yaml.SafeLoader)
    if not isinstance(root, yaml.MappingNode):
        raise ValueError("Frontmatter must be a mapping")
    nodes = {}
    for k, v in root.value:
        if not isinstance(k, yaml.ScalarNode) or k.value in nodes or k.value == "<<":
            raise ValueError("Duplicate, complex, or merged frontmatter keys need manual review")
        nodes[k.value] = v
    return match, nodes, yaml.safe_load(content)


def scalar_edit(node, replacement: str, offset: int) -> tuple[int, int, str]:
    if not isinstance(node, yaml.ScalarNode) or node.start_mark.line != node.end_mark.line:
        raise ValueError("Multiline or structured image property needs manual review")
    return offset + node.start_mark.index, offset + node.end_mark.index, replacement


def repair_text(text: str, value: str) -> str:
    match, nodes, metadata = parse_header(text)
    header = match.group("yaml")
    if any(isinstance(t, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken, yaml.tokens.TagToken)) for t in yaml.scan(header)):
        raise ValueError("YAML anchors, aliases, or explicit tags need manual review before editing")
    offset = match.start("yaml")
    start, end, replacement = scalar_edit(nodes["image"], json.dumps(value, ensure_ascii=False), offset)
    text = text[:start] + replacement + text[end:]
    _, _, after = parse_header(text)
    expected = dict(metadata, image=value)
    if after != expected:
        raise ValueError("Repair would change unrelated metadata")
    return text


def note_header(path: Path) -> str:
    # Read only the header until a relevant note needs its full bytes and body.
    with path.open(encoding="utf8", newline="") as stream:
        first = stream.readline()
        if first.lstrip("\ufeff").strip() != "---":
            return ""
        lines = [first]
        for line in stream:
            lines.append(line)
            if line.strip() == "---":
                break
        return "".join(lines)


def scan(vault: Path, *, notes: list[str] | None = None, replacements: dict | None = None, prepared: dict | None = None) -> dict:
    vault = vault.resolve()
    if not (vault / "assets").is_dir():
        raise ValueError("Expected a vault containing assets/")
    if replacements is None:
        replacements = {}
    if not isinstance(replacements, dict) or any(not isinstance(v, str) for v in replacements.values()):
        raise ValueError("Replacements must be a JSON mapping of note paths to selected image paths")
    index = ImageIndex(vault)
    paths = sorted(set(notes)) if notes is not None else [p for p in index.files if p.endswith(".md") and not set(Path(p).parts) & INFRASTRUCTURE]
    rows, changes, used = [], [], set()
    for note in paths:
        path = safe_path(vault, note)
        if path.suffix != ".md" or not path.is_file() or set(Path(note).parts) & INFRASTRUCTURE:
            raise ValueError(f"Not an eligible Markdown note: {note}")
        header = note_header(path)
        if not re.search(r"\bimage\b", header):
            continue
        row = {"note": note}
        try:
            match, nodes, metadata = parse_header(header)
            if "image" not in nodes:
                continue
            current = metadata["image"]
            row.update({"line": nodes["image"].start_mark.line + 2,
                        "current": json.loads(json.dumps(current, default=str))})
            if note in replacements:
                used.add(note)
            if current is None or current == "" or isinstance(current, str) and not current.strip():
                row["status"] = "empty"
                if note in replacements:
                    raise ValueError("Empty image properties are left alone; assigning a new image is separate work")
                rows.append(row)
                continue
            if not isinstance(current, str):
                raise ValueError("Expected a string image property; structured values need manual review")
            result = index.resolve(current, note)
            row.update(result)
            data = path.read_bytes()
            text = data.decode("utf8")
            full_header = HEADER.match(text)
            if not full_header or text[:full_header.end()] != header:
                raise ValueError("Note changed during scan; re-run the check")
            body = text[full_header.end():]
            if result["status"] not in {"valid", "external"}:
                row["suggestions"] = index.suggestions(result["target"], note, body, result["matches"])
            if note in replacements:
                chosen = replacements[note]
                safe_path(vault, chosen)
                selected = index.resolve(chosen, note)
                if selected["status"] != "valid" or selected["matches"] != [chosen]:
                    raise ValueError(f"Selected replacement must be an exact vault-relative image path: {chosen}")
                value = index.link(chosen)
                old_link = WIKI.fullmatch(current.strip())
                if old_link and "|" in old_link.group(1):
                    value = value[:-2] + "|" + old_link.group(1).split("|", 1)[1] + "]]"
                if old_link and current.strip().startswith("!"):
                    value = "!" + value
                resolved = chosen
                kind = "replace"
            elif result["status"] == "valid" and not result["linked"]:
                resolved = result["matches"][0]
                value = index.link(resolved)
                kind = "link"
            else:
                rows.append(row)
                continue
            updated = repair_text(text, value)
            if HEADER.match(updated).group("close") != HEADER.match(text).group("close") or updated[HEADER.match(updated).end():] != body:
                raise ValueError("Repair would change the note body")
            after = updated.encode("utf8")
            if after != data:
                change = {"note": note, "kind": kind, "before": current, "after": value,
                          "resolved": resolved, "beforeSha256": digest(data), "afterSha256": digest(after)}
                changes.append(change)
                row["proposed"] = value
                if prepared is not None:
                    prepared[note] = (data, after)
        except (ValueError, yaml.YAMLError) as error:
            row.update({"status": "manual-review", "error": str(error)})
        rows.append(row)
    if set(replacements) != used:
        raise ValueError("Replacement names a note without an image property in the selected scope: " + ", ".join(sorted(set(replacements) - used)))
    return {"schemaVersion": SCHEMA, "kind": "image-frontmatter-repair", "vault": str(vault),
            "notes": sorted(set(notes)) if notes is not None else None, "replacements": replacements,
            "summary": dict(sorted(Counter(r["status"] for r in rows).items())), "entries": rows, "changes": changes}


def atomic_write(path: Path, data: bytes, expected: bytes) -> None:
    """Replace one note only if it still has the reviewed bytes."""
    if path.read_bytes() != expected:
        raise ValueError(f"Note changed while applying: {path}")
    mode = path.stat().st_mode & 0o777
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=".image-repair-", delete=False) as stream:
        temporary = Path(stream.name)
        try:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
            os.chmod(temporary, mode)
            if path.read_bytes() != expected:
                raise ValueError(f"Note changed while applying: {path}")
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)


def apply_plan(plan: dict, receipt: Path) -> dict:
    if plan.get("schemaVersion") != SCHEMA or plan.get("kind") != "image-frontmatter-repair":
        raise ValueError("Unsupported image-repair review")
    vault = Path(plan["vault"]).resolve()
    selected = plan["changes"]
    if not isinstance(selected, list) or any(not isinstance(c, dict) or not isinstance(c.get("note"), str) for c in selected):
        raise ValueError("Invalid change list")
    notes = [c["note"] for c in selected]
    if len(set(notes)) != len(notes):
        raise ValueError("Duplicate note in change list")
    prepared = {}
    fresh = scan(vault, notes=notes, replacements={n: v for n, v in plan["replacements"].items() if n in notes}, prepared=prepared)
    current = {c["note"]: c for c in fresh["changes"]}
    for change in selected:
        if current.get(change["note"]) != change:
            raise ValueError(f"Stale or unsafe repair: {change['note']}. Re-scan and review.")
    receipt = receipt.resolve()
    outside_scan(receipt, vault, [])
    receipt.parent.mkdir(parents=True, exist_ok=True)
    state = {"status": "in-progress", "vault": str(vault), "changes": selected, "completed": [],
             "backups": {n: prepared[n][0].decode("utf8") for n in notes}}
    with receipt.open("x", encoding="utf8") as stream:
        stream.write(encoded(state))
    attempted = []
    try:
        for change in selected:
            note = change["note"]
            before, after = prepared[note]
            attempted.append(note)
            atomic_write(safe_path(vault, note), after, before)
            if (vault / note).read_bytes() != after:
                raise ValueError(f"Post-write verification failed: {note}")
            state["completed"].append(note)
            receipt.write_text(encoded(state), encoding="utf8")
        final_index = ImageIndex(vault)
        for change in selected:
            if safe_path(vault, change["note"]).read_bytes() != prepared[change["note"]][1]:
                raise ValueError(f"Note changed during repair: {change['note']}")
            resolved = final_index.resolve(change["after"], change["note"])
            if resolved["status"] != "valid" or resolved["matches"] != [change["resolved"]]:
                raise ValueError(f"Image resolution changed during repair: {change['note']}")
    except BaseException:
        errors = []
        for note in reversed(attempted):
            before, after = prepared[note]
            try:
                path = safe_path(vault, note)
                if path.read_bytes() == after:
                    atomic_write(path, before, after)
                elif path.read_bytes() != before:
                    raise ValueError(f"Concurrent changes; restore manually from receipt: {note}")
            except (OSError, ValueError) as error:
                errors.append(str(error))
        state.update(status="recovery-required" if errors else "rolled-back", recoveryErrors=errors)
        receipt.write_text(encoded(state), encoding="utf8")
        raise
    state["status"] = "verified"
    receipt.write_text(encoded(state), encoding="utf8")
    return state


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, help="Vault root; defaults to this script's parent vault")
    parser.add_argument("--note", action="append", help="Check only this vault-relative note; repeatable")
    parser.add_argument("--output", type=Path, help="Save a review JSON outside the vault")
    parser.add_argument("--replacements", type=Path, help="JSON mapping of note paths to explicitly selected image paths")
    parser.add_argument("--apply", type=Path, metavar="REVIEW", help="Apply the selected changes from a reviewed JSON")
    parser.add_argument("--receipt", type=Path, help="New private receipt with backups; default: REVIEW-applied.json")
    args = parser.parse_args()
    try:
        if args.apply:
            if args.vault or args.note or args.output or args.replacements:
                raise ValueError("--apply uses the review's settings; do not combine with scan options")
            receipt = args.receipt or args.apply.with_name(args.apply.stem + "-applied.json")
            state = apply_plan(json.loads(args.apply.read_text(encoding="utf8")), receipt)
            print(f"Verified {len(state['completed'])} image-property repairs. Receipt: {receipt}")
        else:
            if args.receipt:
                raise ValueError("--receipt requires --apply")
            replacements = json.loads(args.replacements.read_text(encoding="utf8")) if args.replacements else {}
            vault = args.vault or Path(__file__).resolve().parents[1]
            report = scan(vault, notes=args.note, replacements=replacements)
            if args.output:
                outside_scan(args.output, vault.resolve(), [])
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_text(encoded(report), encoding="utf8")
            print(f"Read-only check: {len(report['changes'])} proposed repairs; {json.dumps(report['summary'], sort_keys=True)}")
            for row in report["entries"]:
                if row["status"] not in {"valid", "empty"}:
                    print(f"{row['status']}: {row['note']} — {row.get('current', '')}")
            if args.output:
                print(f"Review: {args.output}")
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as error:
        parser.exit(1, f"Image repair stopped: {error}\n")


if __name__ == "__main__":
    main()

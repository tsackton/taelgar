#!/usr/bin/env python3
"""Conservative ASR delimiter migration; dry run is the default.

python3 _scripts/migrate_asr_markers.py --diff /tmp/asr.patch --report /tmp/asr.json

Only standard timestamped source-cleaned transcripts and recap-scoped beat
transcripts are targets. Narrative sources, archives, inventories and highlights
are excluded. Bare double brackets require explicit, hash-bound per-occurrence ASR
decisions supplied with --confirm-asr; unresolved links are not automatically ASR.
Explicit wikilink syntax is preserved even if a confirmation mistakenly names it.
Single brackets require an explicit unclear/garbled label.
Ambiguous single brackets are preserved. An apply request refuses any ambiguity
or malformed marker in the selected supported files. Select a clear subset with
--path only after reviewing the dry run. No skills or styling are changed.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import difflib
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import tempfile
from dataclasses import dataclass, field


FAMILIES = {
    "feywild": "lost-in-the-feywild", "lablost": "labyrinths-of-the-lost",
    "into-the-chasm": "into-the-chasm", "cleenseau": "cleenseau",
    "dragonets": "dragonets", "mawar": "mawar-adventures",
    "dunmar-frontier": "dunmari-frontier",
}
PRUNE = {"proposed-deletions", "transcript-review", ".git", ".trash", ".obsidian",
         ".agents", ".codex", "node_modules", "__pycache__"}
HEADER = re.compile(r"\[(u\d{4,}) \| (\d{2}:\d{2}:\d{2}\.\d{3})-(\d{2}:\d{2}:\d{2}\.\d{3}) \| ([^\]\r\n]+)\]( ?)([^\r\n]*)")
CUES = frozenset("""laughs;coughs;laughing;coughing;clears throat;dice rolling;die rolling;
sighs;gentle music;paper rustling;dice clatter;paper rustles;dishes clanking;die rolls;
dice clattering;notification sound;gasps;keyboard clacking;grunts;die landing;sneezes;
whooshing;upbeat music;intense music;thud;die thuds;dice landing;thudding;sniffs;
blows raspberry;chuckles;package rustling;items clattering;instrumental music;dice rattling;
mumbles;scoffs;whooshes;dramatic music;claps;yawns;graphics blooping;graphic bloops;
clattering;keyboard clicking;clapping;objects clanking;water running;paper crumpling;
machine beeping;phone ringing;objects thudding;pens scribbling;gurgling;pen clatter;
slimy sounds;clicks tongue;groans;rolls dice;inhales;squelching;imitates clashing;
dice shaking;die thudding;tapping keyboard;metal clangs;censored;snorts;
phone notification pings;meows;humming;object clattering;crunching;festive music;
exhales;monsters roaring;graphics bleeping;tsking;sucks teeth;smacks lips;bottle clinking;
door squeaking;door closing;doorbell rings;knocks;imitates whooshing;chime;
imitates arrow firing;items rustling;chips crunching;paper rattling;knocking;
snapping fingers;imitates arrow whooshing;banging;sic;pause""".replace("\n", "").split(";"))


class Refused(ValueError):
    pass


@dataclass(frozen=True)
class Edit:
    start: int
    end: int
    old: str
    new: str
    kind: str


@dataclass
class Plan:
    path: Path
    original: bytes
    proposed: bytes
    edits: list[Edit] = field(default_factory=list)
    findings: list[dict] = field(default_factory=list)
    counts: dict[str, int] = field(default_factory=dict)
    confirmed: set[tuple[int, str]] = field(default_factory=set)
    identity: tuple = ()


def safe_path(vault: Path, path: Path) -> Path:
    vault = vault.absolute()
    path = path if path.is_absolute() else vault / path
    if ".." in path.parts:
        raise Refused("Path traversal is not permitted")
    try:
        relative = path.relative_to(vault)
    except ValueError as exc:
        raise Refused("Path is outside the vault") from exc
    for part in [path, *path.parents]:
        if part == vault:
            break
        if part.is_symlink():
            raise Refused("Symlink path is not permitted")
    if not path.resolve().is_relative_to(vault.resolve()):
        raise Refused("Resolved path escapes the vault")
    if any(p in PRUNE for p in relative.parts):
        raise Refused("Archive or excluded directory")
    return path


def target_kind(vault: Path, path: Path) -> str:
    path = safe_path(vault, path)
    parts = path.relative_to(vault.absolute()).parts
    if len(parts) not in (5, 6) or parts[0] != "_sessions" or parts[3] != "cleaned":
        raise Refused("Not a standard transcript path")
    family = FAMILIES.get(parts[1])
    if not family or not re.fullmatch(re.escape(family) + r"-\d{3}(?:\.\d+)?", parts[2]):
        raise Refused("Unsupported campaign or bundle filename")
    prefix = parts[2]
    # The existing 139 bundle has this explicitly inspected legacy file prefix.
    if parts[1:3] == ("dunmar-frontier", "dunmari-frontier-139"):
        prefix = "dunmar-frontier-139"
    if len(parts) == 5 and parts[4] == prefix + "-source-cleaned.md":
        return "source"
    if len(parts) == 6 and parts[4] == "beat-transcripts" and re.fullmatch(
            re.escape(prefix) + r"-recap-\d{3}-transcript\.md", parts[5]):
        return "beat"
    raise Refused("Filename is outside the exact transcript allowlist")


def file_identity(info) -> tuple:
    return (info.st_dev, info.st_ino, info.st_mode, info.st_nlink,
            info.st_size, info.st_mtime_ns)


def _check_anchors(vault: Path, path: Path, anchors, fd: int) -> None:
    """Reject observed path replacement; not a guarantee against arbitrary writers."""
    safe_path(vault, path)
    for directory, directory_fd in anchors:
        public, opened = directory.lstat(), os.fstat(directory_fd)
        if not stat.S_ISDIR(public.st_mode) or (public.st_dev, public.st_ino) != (opened.st_dev, opened.st_ino):
            raise Refused("Parent directory changed or became a symlink")
    public, opened = path.lstat(), os.fstat(fd)
    if not stat.S_ISREG(public.st_mode) or (public.st_dev, public.st_ino) != (opened.st_dev, opened.st_ino):
        raise Refused("Transcript inode changed")
    if opened.st_nlink != 1:
        raise Refused("Hard-linked transcript is not permitted")


@contextmanager
def opened_transcript(vault: Path, path: Path, writable=False):
    """Walk from the vault using directory descriptors and O_NOFOLLOW."""
    path = safe_path(vault, path)
    target_kind(vault, path)
    anchors, file_fd = [], None
    try:
        directory_fd = os.open(vault, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW)
        anchors.append((vault, directory_fd))
        directory = vault
        for component in path.relative_to(vault).parts[:-1]:
            before = os.stat(component, dir_fd=directory_fd, follow_symlinks=False)
            if not stat.S_ISDIR(before.st_mode):
                raise Refused("Parent is not a real directory")
            next_fd = os.open(component, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=directory_fd)
            directory /= component
            anchors.append((directory, next_fd))
            after = os.fstat(next_fd)
            if (before.st_dev, before.st_ino) != (after.st_dev, after.st_ino):
                raise Refused("Parent directory raced during opening")
            directory_fd = next_fd
        flags = os.O_RDWR if writable else os.O_RDONLY
        file_fd = os.open(path.name, flags | os.O_NOFOLLOW, dir_fd=directory_fd)
        _check_anchors(vault, path, anchors, file_fd)
        yield file_fd, anchors
    finally:
        if file_fd is not None:
            os.close(file_fd)
        for _, directory_fd in reversed(anchors):
            os.close(directory_fd)


def read_fd(fd: int) -> bytes:
    chunks, offset = [], 0
    while True:
        part = os.pread(fd, 1024 * 1024, offset)
        if not part:
            return b"".join(chunks)
        chunks.append(part)
        offset += len(part)


def timestamp(value: str) -> int:
    h, m, s, ms = map(int, re.split(r"[:.]", value))
    if m >= 60 or s >= 60:
        raise Refused("Invalid timestamp")
    return ((h * 60 + m) * 60 + s) * 1000 + ms


def structure(text: str, kind: str, path: Path) -> tuple[list[tuple[int, int]], tuple]:
    """Return only spoken-text spans and a frozen structural signature."""
    if not text or "\x00" in text or re.search(r"\r(?!\n)", text):
        raise Refused("Empty, binary or unsupported line-ending format")
    spans, signature = [], []
    if kind == "source":
        offset = 0
        for number, line in enumerate(text.splitlines(keepends=True), 1):
            raw = line.rstrip("\r\n")
            match = HEADER.fullmatch(raw)
            if not match or match[1] != f"u{number:04d}":
                raise Refused("Nonstandard source header or noncontiguous UID order")
            if timestamp(match[2]) > timestamp(match[3]):
                raise Refused("Unit ends before it starts")
            if match[6] and not match[5]:
                raise Refused("Missing source header/body separator")
            spans.append((offset + match.start(6), offset + match.end(6)))
            signature.append((raw[:match.start(6)], line[len(raw):]))
            offset += len(line)
    else:
        prefix = path.name.rsplit("-recap-", 1)[0]
        recap = re.search(r"-recap-(\d{3})-transcript\.md$", path.name)[1]
        preamble = re.compile(
            r"# recap-" + recap + r" \| [^\r\n]+\r?\n\r?\n"
            r"- Recap Block: recap-" + recap + r"\r?\n"
            r"- Beat IDs: [A-Za-z0-9, -]+\r?\n"
            r"- Source Range: u(\d{4,}) -> u(\d{4,})\r?\n"
            r"- Source Transcript: \.\./" + re.escape(prefix) + r"-source-cleaned\.md\r?\n"
            r"(?:\r?\n)+## Transcript(?:\r?\n){2,}")
        head = preamble.match(text)
        if not head:
            raise Refused("Nonstandard beat preamble")
        signature.append(head[0])
        pos, covered = head.end(), []
        block = re.compile(r"%% u(\d{4,})(?:-u(\d{4,}))? %%\r?\n([^:\r\n]{1,80}: )([^\r\n]+)((?:\r?\n)*)")
        while pos < len(text):
            match = block.match(text, pos)
            if not match:
                raise Refused("Nonstandard beat turn/provenance format")
            first, last = int(match[1]), int(match[2] or match[1])
            if last < first:
                raise Refused("Reversed beat UID range")
            covered.extend(range(first, last + 1))
            spans.append(match.span(4))
            signature.append((text[pos:match.start(4)], match[5]))
            pos = match.end()
        if covered != list(range(int(head[1]), int(head[2]) + 1)):
            raise Refused("Beat UID coverage differs from Source Range")
    return spans, tuple(signature)


def note_names(vault: Path) -> set[str]:
    names = set()
    for directory, dirs, files in os.walk(vault, followlinks=False):
        dirs[:] = [d for d in dirs if d not in PRUNE
                   and not (Path(directory) / d).is_symlink()]
        names.update(Path(f).stem.casefold() for f in files if f.endswith(".md"))
    return names


def markdown_link_end(body: str, start: int):
    """Protect complete inline links, including nested/quoted destinations."""
    depth, i = 1, start + 1
    while i < len(body) and depth:
        if body[i] == "\\":
            i += 2
            continue
        if body[i] == "[":
            depth += 1
        elif body[i] == "]":
            depth -= 1
        i += 1
    if depth or i == len(body):
        return None
    if body[i] == "[":
        if body.startswith("[[", start):
            return None  # Adjacent ASR annotations are not reference links.
        end = body.find("]", i + 1)
        return end + 1 if end >= 0 else -1
    if body[i] != "(":
        return None
    depth, quote, angle, i = 1, None, False, i + 1
    destination_start = i
    while i < len(body):
        char = body[i]
        if char == "\\":
            i += 2
            continue
        if quote:
            if char == quote:
                quote = None
        elif angle:
            if char == ">":
                angle = False
        elif char in ('"', "'") and (i == destination_start or body[i - 1].isspace()):
            quote = char
        elif char == "<":
            angle = True
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if not depth:
                return i + 1
        i += 1
    return -1


def scan(body: str, offset: int, names: set[str], confirmed=frozenset()) -> tuple[list[Edit], list[dict], dict]:
    edits, findings, counts = [], [], {}
    def count(kind):
        counts[kind] = counts.get(kind, 0) + 1
    def finding(kind, value, pos):
        findings.append({"kind": kind, "text": value, "offset": offset + pos})
    i = 0
    while i < len(body):
        if body[i] == "\\" and i + 1 < len(body):
            i += 2
            continue
        if body[i] == "`":
            run = len(re.match(r"`+", body[i:])[0])
            close = re.search(r"(?<!`)`{" + str(run) + r"}(?!`)", body[i + run:])
            if close is None:
                finding("ambiguous-inline-code", body[i:], i)
                break
            i += run + close.end()
            count("inline-code-preserved")
            continue
        if body[i] == "[":
            link_end = markdown_link_end(body, i)
            if link_end == -1:
                finding("malformed", body[i:], i)
                break
            if link_end is not None:
                count("markdown-link-preserved")
                i = link_end
                continue
        if body.startswith("{{", i):
            end = body.find("}}", i + 2)
            if end < 0 or any(c in body[i + 2:end] for c in "{}[]"):
                finding("malformed", body[i:], i)
                break
            count("existing-curly")
            i = end + 2
            continue
        if body.startswith("[[", i):
            end = body.find("]]", i + 2)
            if end < 0 or not body[i + 2:end].strip() or any(c in body[i + 2:end] for c in "[]{}"):
                finding("malformed", body[i:], i)
                break
            value = body[i + 2:end]
            if (i and body[i - 1] == "!") or any(c in value for c in "|#/\\^") or value.endswith(".md"):
                count("wikilink-preserved")
            elif (offset + i, body[i:end + 2]) in confirmed:
                edits.append(Edit(offset + i, offset + end + 2, body[i:end + 2], "{{" + value + "}}", "double"))
                count("double-to-curly")
            else:
                count("ambiguous-double")
                finding("possible-wikilink" if value.casefold() in names else "unconfirmed-double", value, i)
            i = end + 2
            continue
        if body[i] == "[":
            end = body.find("]", i + 1)
            if end < 0 or any(c in body[i + 1:end] for c in "[{}"):
                finding("malformed", body[i:], i)
                break
            value = body[i + 1:end]
            if body[end + 1:end + 2] in ("(", "[", ":"):
                count("markdown-link-preserved")
            elif re.match(r"(?i)^(unclear|garbled)\b", value):
                edits.append(Edit(offset + i, offset + end + 1, body[i:end + 1], "{{" + value + "}}", "single"))
                count("single-to-curly")
            elif value.strip().casefold() in CUES or re.fullmatch(r"\d+(?:d\d+)?(?:[+-]\d+)?", value):
                count("ordinary-bracket-preserved")
            else:
                count("ambiguous-single")
                finding("ambiguous-single", value, i)
            i = end + 1
            continue
        if body[i] in "]" or body.startswith("}}", i):
            finding("malformed", body[i:], i)
            break
        i += 1
    return edits, findings, counts


def render(text: str, edits: list[Edit]) -> str:
    chunks, cursor = [], 0
    for e in sorted(edits, key=lambda e: e.start):
        if e.start < cursor or text[e.start:e.end] != e.old:
            raise Refused("Overlapping or stale edit")
        interior = e.old[2:-2] if e.kind == "double" else e.old[1:-1]
        if e.new != "{{" + interior + "}}":
            raise Refused("Edit changes more than marker delimiters")
        chunks.extend((text[cursor:e.start], e.new))
        cursor = e.end
    chunks.append(text[cursor:])
    return "".join(chunks)


def plan_file(vault: Path, path: Path, names: set[str], confirmed=frozenset(), evidence_sha256=None) -> Plan:
    path = safe_path(vault, path)
    kind = target_kind(vault, path)
    with opened_transcript(vault, path) as (fd, anchors):
        identity = file_identity(os.fstat(fd))
        original = read_fd(fd)
        _check_anchors(vault, path, anchors, fd)
        if identity != file_identity(os.fstat(fd)):
            raise Refused("Concurrent transcript edit while reading")
    if (confirmed and evidence_sha256 is None) or (evidence_sha256 is not None and hashlib.sha256(original).hexdigest() != evidence_sha256):
        raise Refused("ASR confirmation fingerprint is stale or missing")
    try:
        text = original.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise Refused("Not a UTF-8 transcript") from exc
    spans, signature = structure(text, kind, path)
    for offset, old in confirmed:
        if text[offset:offset + len(old)] != old:
            raise Refused("ASR confirmation does not match the exact original occurrence")
    plan = Plan(path, original, original, confirmed=set(confirmed), identity=identity)
    for start, end in spans:
        edits, findings, counts = scan(text[start:end], start, names, confirmed)
        plan.edits.extend(edits)
        for finding in findings:
            finding["line"] = text.count("\n", 0, finding["offset"]) + 1
        plan.findings.extend(findings)
        for key, value in counts.items():
            plan.counts[key] = plan.counts.get(key, 0) + value
    if any(f["kind"] == "malformed" for f in plan.findings):
        plan.edits.clear()  # Malformed file: no proposed changes anywhere in it.
        plan.counts.pop("double-to-curly", None)
        plan.counts.pop("single-to-curly", None)
        return plan
    proposed = render(text, plan.edits)
    if structure(proposed, kind, path)[1] != signature:
        raise Refused("Structural signature changed")
    plan.proposed = proposed.encode("utf-8")
    return plan


def discover(vault: Path) -> tuple[list[Path], int]:
    matches, other_beats = [], 0
    for directory, dirs, files in os.walk(vault / "_sessions", followlinks=False):
        dirs[:] = [d for d in dirs if d not in PRUNE and not (Path(directory) / d).is_symlink()]
        for name in files:
            p = Path(directory) / name
            if name.endswith("-source-cleaned.md") or p.parent.name == "beat-transcripts" and name.endswith("-transcript.md"):
                matches.append(p)
            elif p.parent.name == "beat-transcripts" and name.endswith(".md"):
                other_beats += 1
    return sorted(matches), other_beats


def apply_plans(vault: Path, plans: list[Plan]) -> None:
    if any(p.findings for p in plans):
        raise Refused("Ambiguous or malformed markers remain; no files written")
    names = note_names(vault)
    for p in plans:
        current = plan_file(vault, p.path, names, p.confirmed, hashlib.sha256(p.original).hexdigest())
        if current.original != p.original or current.proposed != p.proposed or current.identity != p.identity:
            raise Refused("Concurrent edit or classification change; no files written")
    # Writes target existing allowlisted transcript files only. No sibling temp files.
    for p in plans:
        if p.original == p.proposed:
            continue
        with opened_transcript(vault, p.path, writable=True) as (fd, anchors):
            _check_anchors(vault, p.path, anchors, fd)
            if file_identity(os.fstat(fd)) != p.identity or read_fd(fd) != p.original:
                raise Refused("Concurrent transcript edit; stopped before this write")
            _check_anchors(vault, p.path, anchors, fd)
            if file_identity(os.fstat(fd)) != p.identity:
                raise Refused("Concurrent transcript edit immediately before writing")
            # Checks detect observed races; an arbitrary writer can still race a
            # later instruction. Do not advertise absolute concurrent-write safety.
            os.lseek(fd, 0, os.SEEK_SET)
            remaining = memoryview(p.proposed)
            while remaining:
                remaining = remaining[os.write(fd, remaining):]
            os.ftruncate(fd, len(p.proposed))
            os.fsync(fd)


def load_confirmations(vault: Path, filename: str) -> dict:
    """Operator-reviewed decisions, not an automatic assertion that links are ASR."""
    data = json.loads(Path(filename).read_text(encoding="utf-8"))
    if data.get("version") != 1 or not isinstance(data.get("files"), list):
        raise Refused("Unsupported ASR confirmation format")
    result = {}
    for entry in data["files"]:
        path = safe_path(vault, Path(entry["path"]))
        target_kind(vault, path)
        digest = entry.get("sha256", "")
        if not re.fullmatch(r"[0-9a-f]{64}", digest) or not entry.get("basis") or path in result:
            raise Refused("Invalid or duplicate ASR confirmation file entry")
        decisions = set()
        for span in entry["spans"]:
            offset, old = span.get("offset"), span.get("old", "")
            if type(offset) is not int or offset < 0 or not old.startswith("[[") or not old.endswith("]]") or span.get("decision") != "asr":
                raise Refused("Invalid ASR occurrence decision")
            if (offset, old) in decisions:
                raise Refused("Duplicate ASR occurrence decision")
            decisions.add((offset, old))
        result[path] = (digest, decisions)
    return result


def temporary_output(path: str, vault: Path) -> Path:
    p = Path(path).absolute()
    allowed = (Path("/tmp").resolve(), Path(tempfile.gettempdir()).resolve())
    if p.is_symlink() or p.resolve().is_relative_to(vault.resolve()) or not any(p.resolve().is_relative_to(a) for a in allowed):
        raise Refused("Reports/diffs must be outside the repository in a temporary directory")
    if p.exists():
        raise Refused("Report/diff target already exists")
    return p


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--path", action="append", help="Select an explicit transcript path; repeatable")
    parser.add_argument("--confirm-asr", help="Reviewed, fingerprint-bound per-occurrence ASR decisions")
    parser.add_argument("--diff", help="New temporary unified-diff output")
    parser.add_argument("--report", help="New temporary JSON report")
    parser.add_argument("--apply", action="store_true", help="Write only after reviewing the dry run; refuses ambiguous plans")
    args = parser.parse_args(argv)
    vault = args.vault.absolute()
    # Refuse bad report destinations before a possible future apply request.
    if args.diff:
        temporary_output(args.diff, vault)
    if args.report:
        temporary_output(args.report, vault)
    if args.diff and args.report and Path(args.diff).resolve() == Path(args.report).resolve():
        raise Refused("Diff and report must have distinct temporary destinations")
    paths, other = discover(vault) if not args.path else ([Path(p) for p in args.path], 0)
    decisions = load_confirmations(vault, args.confirm_asr) if args.confirm_asr else {}
    selected = {safe_path(vault, p) for p in paths}
    if not set(decisions).issubset(selected):
        raise Refused("ASR confirmations contain unselected files")
    names, plans, excluded = note_names(vault), [], []
    for path in paths:
        try:
            digest, confirmed = decisions.get(safe_path(vault, path), (None, frozenset()))
            plans.append(plan_file(vault, path, names, confirmed, digest))
        except (Refused, OSError) as exc:
            excluded.append({"path": str(path), "reason": str(exc)})
    totals = {}
    for p in plans:
        for k, v in p.counts.items():
            totals[k] = totals.get(k, 0) + v
    report = {"mode": "apply" if args.apply else "dry-run", "matching": len(paths), "eligible": len(plans),
              "excluded": excluded, "other_beat_files_untouched": other,
              "changed_files": sum(p.proposed != p.original for p in plans), "counts": totals,
              "findings": [{"path": str(p.path), **f} for p in plans for f in p.findings],
              "changes": [{"path": str(p.path), "sha256": hashlib.sha256(p.original).hexdigest(),
                           "edits": len(p.edits)} for p in plans if p.edits]}
    if args.apply:
        if excluded:
            raise Refused("Unsupported selected files; no files written")
        relative = [str(p.path.relative_to(vault)) for p in plans]
        if subprocess.run(["git", "diff", "--quiet", "HEAD", "--", *relative], cwd=vault).returncode:
            raise Refused("Commit transcript baseline before applying")
        for p in plans:
            subprocess.run(["git", "ls-files", "--error-unmatch", "--", str(p.path.relative_to(vault))], cwd=vault, check=True, stdout=subprocess.DEVNULL)
        apply_plans(vault, plans)
    if args.diff:
        output = temporary_output(args.diff, vault)
        with output.open("x", encoding="utf-8", newline="") as stream:
            for p in plans:
                if p.original != p.proposed:
                    name = str(p.path.relative_to(vault))
                    stream.writelines(difflib.unified_diff(p.original.decode().splitlines(keepends=True),
                        p.proposed.decode().splitlines(keepends=True), "a/" + name, "b/" + name))
    if args.report:
        with temporary_output(args.report, vault).open("x", encoding="utf-8") as stream:
            stream.write(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in ("changes", "findings", "excluded")}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (Refused, OSError, subprocess.CalledProcessError) as exc:
        raise SystemExit("REFUSED: " + str(exc))

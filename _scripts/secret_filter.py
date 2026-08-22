#!/usr/bin/env python3
"""Fail-closed Git filter and guards for Taelgar private note fragments.

The working tree may contain raw ``%%SECRET ... %%`` blocks and frontmatter
lines marked with ``##secret``.  Git blobs contain placeholders instead.  The
raw fragments are stored outside Git in a path-keyed, permission-restricted
sidecar store so that an authorized working copy can restore them on checkout.

Legacy numeric placeholders and the original flat ``.secrets`` directory are
supported for recovery, but all newly filtered material uses deterministic v2
placeholders and ``.secrets-v2`` sidecars.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from typing import Dict, Iterable, List, Mapping, MutableMapping, Optional, Sequence, Tuple


RAW_BLOCK_START = b"%%SECRET"
BLOCK_PLACEHOLDER_RE = re.compile(
    rb"%%SECRET\[(?P<token>(?:v2:[0-9a-f]{32}|[0-9]+))\]%%"
)
V2_BLOCK_PLACEHOLDER_RE = re.compile(
    rb"%%SECRET\[(?P<token>v2:[0-9a-f]{32})\]%%"
)
LEGACY_BLOCK_PLACEHOLDER_RE = re.compile(rb"%%SECRET\[(?P<number>[0-9]+)\]%%")
V2_YAML_PLACEHOLDER_RE = re.compile(rb"###secret\[(?P<token>v2:[0-9a-f]{32})\]")
LEGACY_YAML_PLACEHOLDER_RE = re.compile(rb"###secret\[(?P<number>[0-9]+)\]")
YAML_SECRET_MARKER_RE = re.compile(rb"(?:^|[ \t])##secret(?:[ \t]|$)")
ZERO_OID_RE = re.compile(r"^0+$")
GIT_EXECUTABLE = shutil.which("git") or "git"


class SecretFilterError(RuntimeError):
    """Raised when filtering cannot safely continue."""


@dataclass(frozen=True)
class SecretSpan:
    start: int
    end: int
    kind: str
    line: int
    raw: bytes


@dataclass(frozen=True)
class Finding:
    kind: str
    line: int


def _line_number(data: bytes, offset: int) -> int:
    return data.count(b"\n", 0, offset) + 1


def _line_content_and_ending(line: bytes) -> Tuple[bytes, bytes]:
    if line.endswith(b"\r\n"):
        return line[:-2], b"\r\n"
    if line.endswith(b"\n") or line.endswith(b"\r"):
        return line[:-1], line[-1:]
    return line, b""


def _frontmatter_line_spans(data: bytes) -> List[Tuple[int, int, bytes]]:
    """Return byte spans for lines inside initial YAML frontmatter."""

    lines = data.splitlines(keepends=True)
    if not lines:
        return []
    first_content, _ = _line_content_and_ending(lines[0])
    if first_content != b"---":
        return []

    result: List[Tuple[int, int, bytes]] = []
    offset = len(lines[0])
    for line in lines[1:]:
        content, _ = _line_content_and_ending(line)
        if content in {b"---", b"..."}:
            return result
        result.append((offset, offset + len(content), content))
        offset += len(line)
    raise SecretFilterError("frontmatter opens with '---' but has no closing delimiter")


def _collect_raw_block_spans(data: bytes, allow_unclosed: bool = False) -> List[SecretSpan]:
    spans: List[SecretSpan] = []
    if RAW_BLOCK_START not in data:
        return spans
    cursor = 0
    while True:
        start = data.find(RAW_BLOCK_START, cursor)
        if start < 0:
            return spans

        placeholder = BLOCK_PLACEHOLDER_RE.match(data, start)
        if placeholder is not None:
            cursor = placeholder.end()
            continue

        close_start = data.find(b"%%", start + len(RAW_BLOCK_START))
        if close_start < 0:
            if allow_unclosed:
                spans.append(
                    SecretSpan(
                        start=start,
                        end=len(data),
                        kind="block",
                        line=_line_number(data, start),
                        raw=data[start:],
                    )
                )
                return spans
            raise SecretFilterError(
                "unclosed raw secret block at line {}".format(_line_number(data, start))
            )
        end = close_start + 2
        spans.append(
            SecretSpan(
                start=start,
                end=end,
                kind="block",
                line=_line_number(data, start),
                raw=data[start:end],
            )
        )
        cursor = end


def _collect_yaml_secret_spans(data: bytes) -> List[SecretSpan]:
    spans: List[SecretSpan] = []
    if b"##secret" not in data:
        return spans
    for start, end, content in _frontmatter_line_spans(data):
        if V2_YAML_PLACEHOLDER_RE.search(content) or LEGACY_YAML_PLACEHOLDER_RE.search(content):
            continue
        if YAML_SECRET_MARKER_RE.search(content) is None:
            continue
        spans.append(
            SecretSpan(
                start=start,
                end=end,
                kind="yaml",
                line=_line_number(data, start),
                raw=data[start:end],
            )
        )
    return spans


def collect_raw_secret_spans(data: bytes, allow_unclosed: bool = False) -> List[SecretSpan]:
    spans = _collect_raw_block_spans(data, allow_unclosed=allow_unclosed)
    spans += _collect_yaml_secret_spans(data)
    spans.sort(key=lambda item: (item.start, item.end))
    for previous, current in zip(spans, spans[1:]):
        if previous.end > current.start:
            raise SecretFilterError(
                "overlapping secret syntax at lines {} and {}".format(
                    previous.line, current.line
                )
            )
    return spans


def scan_raw_secrets(data: bytes) -> List[Finding]:
    try:
        return [Finding(span.kind, span.line) for span in collect_raw_secret_spans(data)]
    except SecretFilterError as exc:
        match = re.search(r"line ([0-9]+)", str(exc))
        line = int(match.group(1)) if match else 1
        return [Finding("malformed", line)]


def _secret_id(raw: bytes) -> str:
    return "v2:" + hashlib.sha256(raw).hexdigest()[:32]


def _placeholder_for(span: SecretSpan, token: str) -> bytes:
    encoded = token.encode("ascii")
    if span.kind == "block":
        return b"%%SECRET[" + encoded + b"]%%"
    indentation = span.raw[: len(span.raw) - len(span.raw.lstrip(b" \t"))]
    return indentation + b"###secret[" + encoded + b"]"


def _apply_replacements(data: bytes, replacements: Iterable[Tuple[int, int, bytes]]) -> bytes:
    result = data
    ordered = sorted(replacements, key=lambda item: item[0], reverse=True)
    for start, end, replacement in ordered:
        result = result[:start] + replacement + result[end:]
    return result


def _normalize_git_path(path_text: str) -> PurePosixPath:
    path = PurePosixPath(path_text)
    if path.is_absolute() or not path.parts or any(part in {"", ".", ".."} for part in path.parts):
        raise SecretFilterError("unsafe Git path: {!r}".format(path_text))
    return path


def sidecar_path(store_root: Path, git_path: str) -> Path:
    relative = _normalize_git_path(git_path)
    root = store_root.resolve()
    candidate = Path(str(root.joinpath(*relative.parts)) + ".json").resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise SecretFilterError("sidecar path escapes its storage root") from exc
    return candidate


def _decode_entry(entry: Mapping[str, str]) -> bytes:
    try:
        return base64.b64decode(entry["data"].encode("ascii"), validate=True)
    except (KeyError, ValueError) as exc:
        raise SecretFilterError("invalid sidecar entry") from exc


def load_sidecar(store_root: Path, git_path: str) -> Dict[str, Dict[str, str]]:
    path = sidecar_path(store_root, git_path)
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SecretFilterError("could not read sidecar for {!r}".format(git_path)) from exc
    if payload.get("version") != 2 or payload.get("path") != git_path:
        raise SecretFilterError("invalid sidecar metadata for {!r}".format(git_path))
    entries = payload.get("entries")
    if not isinstance(entries, dict):
        raise SecretFilterError("invalid sidecar entries for {!r}".format(git_path))
    validated: Dict[str, Dict[str, str]] = {}
    for token, entry in entries.items():
        if re.fullmatch(r"v2:[0-9a-f]{32}", token) is None or not isinstance(entry, dict):
            raise SecretFilterError("invalid sidecar token for {!r}".format(git_path))
        raw = _decode_entry(entry)
        if _secret_id(raw) != token or entry.get("kind") not in {"block", "yaml"}:
            raise SecretFilterError("sidecar integrity check failed for {!r}".format(git_path))
        validated[token] = {"kind": entry["kind"], "data": entry["data"]}
    return validated


def write_sidecar(
    store_root: Path,
    git_path: str,
    new_entries: Mapping[str, Mapping[str, str]],
) -> None:
    if not new_entries:
        return
    path = sidecar_path(store_root, git_path)
    existing = load_sidecar(store_root, git_path)
    merged: MutableMapping[str, Dict[str, str]] = dict(existing)
    for token, entry in new_entries.items():
        normalized = {"kind": str(entry["kind"]), "data": str(entry["data"])}
        if token in merged and merged[token] != normalized:
            raise SecretFilterError("sidecar token collision for {!r}".format(git_path))
        merged[token] = normalized

    payload = {
        "version": 2,
        "path": git_path,
        "entries": dict(sorted(merged.items())),
    }
    root = store_root.resolve()
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    directory = path.parent
    while True:
        os.chmod(directory, 0o700)
        if directory == root:
            break
        directory = directory.parent

    handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=str(path.parent),
        prefix=path.name + ".",
        suffix=".tmp",
        delete=False,
    )
    temporary_path = Path(handle.name)
    try:
        with handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temporary_path, 0o600)
        os.replace(str(temporary_path), str(path))
        os.chmod(path, 0o600)
    except Exception:
        try:
            temporary_path.unlink()
        except FileNotFoundError:
            pass
        raise


def clean_bytes(data: bytes, git_path: str, store_root: Optional[Path]) -> bytes:
    spans = collect_raw_secret_spans(data)
    return _clean_with_spans(data, git_path, store_root, spans)


def _clean_with_spans(
    data: bytes,
    git_path: str,
    store_root: Optional[Path],
    spans: Sequence[SecretSpan],
) -> bytes:
    replacements: List[Tuple[int, int, bytes]] = []
    entries: Dict[str, Dict[str, str]] = {}
    for span in spans:
        token = _secret_id(span.raw)
        replacements.append((span.start, span.end, _placeholder_for(span, token)))
        entries[token] = {
            "kind": span.kind,
            "data": base64.b64encode(span.raw).decode("ascii"),
        }
    if store_root is not None:
        write_sidecar(store_root, git_path, entries)
    return _apply_replacements(data, replacements)


def clean_history_bytes(data: bytes) -> bytes:
    spans = collect_raw_secret_spans(data, allow_unclosed=True)
    return _clean_with_spans(data, "history.md", None, spans)


def _v2_restore_replacements(
    data: bytes,
    entries: Mapping[str, Mapping[str, str]],
) -> List[Tuple[int, int, bytes]]:
    replacements: List[Tuple[int, int, bytes]] = []
    for pattern in (V2_BLOCK_PLACEHOLDER_RE, V2_YAML_PLACEHOLDER_RE):
        for match in pattern.finditer(data):
            token = match.group("token").decode("ascii")
            entry = entries.get(token)
            if entry is None:
                continue
            replacements.append((match.start(), match.end(), _decode_entry(entry)))
    return replacements


def _legacy_restore_replacements(
    data: bytes,
    git_path: str,
    legacy_store: Optional[Path],
) -> List[Tuple[int, int, bytes]]:
    if legacy_store is None:
        return []
    matches: List[Tuple[int, int, str]] = []
    for match in LEGACY_BLOCK_PLACEHOLDER_RE.finditer(data):
        matches.append((match.start(), match.end(), "block"))
    for match in LEGACY_YAML_PLACEHOLDER_RE.finditer(data):
        matches.append((match.start(), match.end(), "yaml"))
    matches.sort(key=lambda item: item[0])

    replacements: List[Tuple[int, int, bytes]] = []
    basename = PurePosixPath(git_path).name
    for sequence, (start, end, kind) in enumerate(matches, start=1):
        legacy_path = legacy_store / "{}.{}".format(basename, sequence)
        if not legacy_path.exists():
            continue
        raw_inner = legacy_path.read_bytes()
        raw = (
            b"%%SECRET" + raw_inner + b"%%"
            if kind == "block"
            else raw_inner + b"##secret"
        )
        replacements.append((start, end, raw))
    return replacements


def smudge_bytes(
    data: bytes,
    git_path: str,
    store_root: Path,
    legacy_store: Optional[Path],
) -> bytes:
    entries = load_sidecar(store_root, git_path)
    replacements = _v2_restore_replacements(data, entries)
    replacements.extend(_legacy_restore_replacements(data, git_path, legacy_store))
    replacements.sort(key=lambda item: item[0])
    for previous, current in zip(replacements, replacements[1:]):
        if previous[1] > current[0]:
            raise SecretFilterError("overlapping placeholders in {!r}".format(git_path))
    return _apply_replacements(data, replacements)


def run_git(
    arguments: Sequence[str],
    *,
    input_bytes: Optional[bytes] = None,
    cwd: Optional[Path] = None,
) -> bytes:
    completed = subprocess.run(
        [GIT_EXECUTABLE] + list(arguments),
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        cwd=str(cwd) if cwd else None,
        check=False,
    )
    if completed.returncode != 0:
        message = completed.stderr.decode("utf-8", errors="replace").strip()
        raise SecretFilterError("git {} failed: {}".format(arguments[0], message))
    return completed.stdout


def _decode_nul_paths(raw: bytes) -> List[str]:
    return [part.decode("utf-8", errors="surrogateescape") for part in raw.split(b"\0") if part]


def _report_findings(label: str, data: bytes) -> int:
    findings = scan_raw_secrets(data)
    for finding in findings:
        print(
            "raw secret syntax: {}:{} ({})".format(label, finding.line, finding.kind),
            file=sys.stderr,
        )
    return len(findings)


def check_index() -> int:
    paths = _decode_nul_paths(
        run_git(
            [
                "diff",
                "--cached",
                "--name-only",
                "--diff-filter=ACMR",
                "-z",
                "--",
                "*.md",
            ]
        )
    )
    failures = 0
    for path in paths:
        data = run_git(["show", ":{}".format(path)])
        failures += _report_findings(path, data)
    if failures:
        print("commit blocked: staged Markdown contains raw secret syntax", file=sys.stderr)
        return 1
    return 0


def _commits_for_push(local_oid: str, remote_oid: str) -> List[str]:
    if ZERO_OID_RE.fullmatch(local_oid):
        return []
    if ZERO_OID_RE.fullmatch(remote_oid):
        # A zero remote object means the destination does not yet have this ref.
        # Scan the complete reachable history: subtracting a local tracking remote
        # could otherwise miss content when the same branch is pushed elsewhere.
        output = run_git(["rev-list", local_oid])
    else:
        output = run_git(["rev-list", local_oid, "^{}".format(remote_oid)])
    return [line for line in output.decode("ascii").splitlines() if line]


def _changed_markdown_paths(commit: str) -> List[str]:
    output = run_git(
        [
            "diff-tree",
            "--root",
            "-m",
            "--no-commit-id",
            "--name-only",
            "--diff-filter=ACMR",
            "-r",
            "-z",
            commit,
            "--",
            "*.md",
        ]
    )
    return _decode_nul_paths(output)


def check_push(lines: Iterable[str]) -> int:
    commits: List[str] = []
    for line in lines:
        fields = line.strip().split()
        if len(fields) != 4:
            continue
        _, local_oid, _, remote_oid = fields
        commits.extend(_commits_for_push(local_oid, remote_oid))

    failures = 0
    seen_blobs = set()
    for commit in dict.fromkeys(commits):
        for path in _changed_markdown_paths(commit):
            try:
                blob_oid = run_git(["rev-parse", "{}:{}".format(commit, path)]).decode("ascii").strip()
                if blob_oid in seen_blobs:
                    continue
                data = run_git(["cat-file", "blob", blob_oid])
            except SecretFilterError:
                continue
            seen_blobs.add(blob_oid)
            failures += _report_findings("{}:{}".format(commit[:12], path), data)
    if failures:
        print("push blocked: outgoing history contains raw secret syntax", file=sys.stderr)
        return 1
    return 0


def check_tree(revision: str) -> int:
    paths = _decode_nul_paths(
        run_git(["ls-tree", "-r", "-z", "--name-only", revision, "--", "*.md"])
    )
    failures = 0
    for path in paths:
        data = run_git(["show", "{}:{}".format(revision, path)])
        failures += _report_findings(path, data)
    if failures:
        print(
            "tree check failed: {} raw secret marker(s) found".format(failures),
            file=sys.stderr,
        )
        return 1
    print("tree check passed: no raw secret syntax in {}".format(revision))
    return 0


def snapshot_working_tree(store_root: Path, dry_run: bool = False) -> int:
    paths = _decode_nul_paths(run_git(["ls-files", "-z", "--", "*.md"]))
    files_with_secrets = 0
    entries = 0
    for git_path in paths:
        path = Path(git_path)
        if not path.is_file():
            continue
        data = path.read_bytes()
        spans = collect_raw_secret_spans(data)
        if not spans:
            continue
        clean_bytes(data, git_path, None if dry_run else store_root)
        files_with_secrets += 1
        entries += len(spans)
    print(
        "{} complete: {} file(s), {} secret fragment(s)".format(
            "snapshot validation" if dry_run else "snapshot",
            files_with_secrets,
            entries,
        )
    )
    return 0


def doctor() -> int:
    expected = {
        "filter.remove-secrets.clean": "_scripts/secret_filter.py",
        "filter.remove-secrets.smudge": "_scripts/secret_filter.py",
        "filter.remove-secrets.required": "true",
        "core.hookspath": "_scripts/git-hooks",
    }
    failures = 0
    for key, fragment in expected.items():
        try:
            value = run_git(["config", "--get", key]).decode("utf-8").strip()
        except SecretFilterError:
            value = ""
        comparison_value = value.lower() if key == "core.hookspath" else value
        if fragment not in comparison_value:
            print("configuration missing or incorrect: {}".format(key), file=sys.stderr)
            failures += 1
    if failures:
        return 1

    hook_path = run_git(["config", "--path", "--get", "core.hooksPath"]).decode("utf-8").strip()
    for hook in ("pre-commit", "pre-push"):
        path = Path(hook_path) / hook
        if not path.is_file() or not os.access(str(path), os.X_OK):
            print("hook missing or not executable: {}".format(path), file=sys.stderr)
            failures += 1
    if failures:
        return 1
    print("secret filter configuration and hooks are active")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("clean", "smudge"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument("--path", required=True)
        subparser.add_argument("--store", type=Path, default=Path(".secrets-v2"))
        if command == "smudge":
            subparser.add_argument("--legacy-store", type=Path, default=Path(".secrets"))

    subparsers.add_parser("history-clean")
    subparsers.add_parser("check-index")
    subparsers.add_parser("check-push")
    tree_parser = subparsers.add_parser("check-tree")
    tree_parser.add_argument("revision", nargs="?", default="HEAD")
    snapshot_parser = subparsers.add_parser("snapshot-working-tree")
    snapshot_parser.add_argument("--store", type=Path, default=Path(".secrets-v2"))
    snapshot_parser.add_argument("--dry-run", action="store_true")
    subparsers.add_parser("doctor")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "clean":
            output = clean_bytes(sys.stdin.buffer.read(), args.path, args.store)
            sys.stdout.buffer.write(output)
            return 0
        if args.command == "smudge":
            output = smudge_bytes(
                sys.stdin.buffer.read(),
                args.path,
                args.store,
                args.legacy_store,
            )
            sys.stdout.buffer.write(output)
            return 0
        if args.command == "history-clean":
            output = clean_history_bytes(sys.stdin.buffer.read())
            sys.stdout.buffer.write(output)
            return 0
        if args.command == "check-index":
            return check_index()
        if args.command == "check-push":
            return check_push(sys.stdin)
        if args.command == "check-tree":
            return check_tree(args.revision)
        if args.command == "snapshot-working-tree":
            return snapshot_working_tree(args.store, dry_run=args.dry_run)
        if args.command == "doctor":
            return doctor()
        raise SecretFilterError("unknown command")
    except SecretFilterError as exc:
        print("secret filter error: {}".format(exc), file=sys.stderr)
        return 1
    except OSError as exc:
        print("secret filter I/O error: {}".format(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

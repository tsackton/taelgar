#!/usr/bin/env python3
"""Quality scanner and optional wiki-link fixer for Taelgar markdown notes."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence


SKIP_SUBTREES = {
    ("Campaigns", "Cleenseau Campaign", "Celyn's Stories"),
    ("Campaigns", "Cleenseau Campaign", "Raw Emails"),
    ("Worldbuilding", "Chats and Emails"),
}

MEDIA_EXTENSIONS = {
    ".avif",
    ".gif",
    ".jpeg",
    ".jpg",
    ".mp3",
    ".mp4",
    ".ogg",
    ".pdf",
    ".png",
    ".svg",
    ".wav",
    ".webm",
    ".webp",
}

SEVERITY_ORDER = {"info": 0, "warn": 1, "error": 2}


COMMON_TYPOS: tuple[tuple[str, str, str], ...] = (
    (r"\boccured\b", "occurred", "common typo"),
    (r"\boccurr?ance\b", "occurrence", "common typo"),
    (r"\bbrethern\b", "brethren", "common typo"),
    (r"\bTwililght\b", "Twilight", "common typo"),
    (r"\b[Tt]wililght\b", "twilight", "common typo"),
    (r"\bressurection\b", "resurrection", "common typo"),
    (r"\bRessurection\b", "Resurrection", "common typo"),
    (r"\bressurect(ed|ing|s)?\b", "resurrect...", "common typo"),
    (r"\bdefinately\b", "definitely", "common typo"),
    (r"\bseperate\b", "separate", "common typo"),
    (r"\brecieve([ds]?)\b", "receive...", "common typo"),
    (r"\bpermanantly\b", "permanently", "common typo"),
    (r"\bstabliz(e|ed|ing|es)\b", "stabilize...", "common typo"),
    (r"\bmismash\b", "mishmash", "common typo"),
    (r"\bactully\b", "actually", "common typo"),
    (r"\bnoticably\b", "noticeably", "common typo"),
    (r"\bsomtimes\b", "sometimes", "common typo"),
    (r"\bbetwen\b", "between", "common typo"),
    (r"\bitsefl\b", "itself", "common typo"),
    (r"\bagains\b", "against", "common typo"),
    (r"\bliving their\b", "living there", "likely typo"),
    (r"\bis know to be\b", "is known to be", "likely typo"),
    (r"\bwas know to be\b", "was known to be", "likely typo"),
    (r"\bare know to be\b", "are known to be", "likely typo"),
    (r"\bwere know to be\b", "were known to be", "likely typo"),
    (r"\bbuild during\b", "built during", "likely typo"),
    (r"\bfirst have of\b", "first half of", "likely typo"),
    (r"\bcall the novja\b", "called the novja", "likely typo"),
)

TYPO_PATTERNS = tuple(
    (re.compile(pattern), suggestion, label)
    for pattern, suggestion, label in COMMON_TYPOS
)

WIKILINK_PATTERN = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
MALFORMED_SECRET_PATTERN = re.compile(r"%%\s+SECRET\b")
EXPORT_MARKER_PATTERN = re.compile(
    r"%%\s*\^?(Campaign|Date|DateEnd|End)(?::[^%]*)?\s*%%",
    re.IGNORECASE,
)
GENERIC_COMMENT_DELIMITER = "%%"
REPEATED_WORD_PATTERN = re.compile(r"\b([A-Za-z][A-Za-z'-]*)\s+\1\b", re.IGNORECASE)
DOUBLE_PERIOD_PATTERN = re.compile(r"(?<!\.)\.\.(?!\.)")


@dataclass(frozen=True)
class Issue:
    severity: str
    check: str
    path: str
    line: int
    message: str
    snippet: str = ""
    suggestion: str = ""


@dataclass(frozen=True)
class LinkReplacement:
    start: int
    end: int
    replacement: str
    line: int
    original: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Vault root to scan (default: current directory).",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json", "tsv"),
        default="markdown",
        help="Report format (default: markdown).",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Optional report destination. Defaults to stdout.",
    )
    parser.add_argument(
        "--min-severity",
        choices=("info", "warn", "error"),
        default="info",
        help="Hide issues below this severity (default: info).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=500,
        help="Maximum issues to print; use 0 for no limit (default: 500).",
    )
    parser.add_argument(
        "--duplicate-filenames",
        action="store_true",
        help="Only report duplicate filenames, scanning every non-dot path.",
    )
    parser.add_argument(
        "--replace-wikilinks",
        action="store_true",
        help=(
            "Replace pathful wiki links with basename links when the basename is "
            "unique across markdown notes in every non-dot directory."
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="With --replace-wikilinks, report replacements without writing files.",
    )
    parser.add_argument(
        "--skip-generated",
        action="store_true",
        help=(
            "With --duplicate-filenames, skip generated/session-cleanup material: "
            "_generated paths, .json/.txt/.vtt/.yaml files, and "
            "_sessions/<campaign>/<session>/cleaned paths."
        ),
    )
    return parser.parse_args()


def should_skip_dot_dir(root: Path, dir_path: Path) -> bool:
    rel_parts = dir_path.relative_to(root).parts
    if not rel_parts:
        return False

    name = rel_parts[-1]
    return name.startswith(".")


def should_skip_dir(root: Path, dir_path: Path) -> bool:
    rel_parts = dir_path.relative_to(root).parts
    if not rel_parts:
        return False

    name = rel_parts[-1]
    if name.startswith(".") or name.startswith("_"):
        return True

    for subtree in SKIP_SUBTREES:
        if rel_parts[: len(subtree)] == subtree:
            return True
    return False


def iter_files_no_dot_dirs(root: Path) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        current = Path(dirpath)
        dirnames[:] = [
            dirname
            for dirname in sorted(dirnames)
            if not should_skip_dot_dir(root, current / dirname)
        ]
        for filename in sorted(filenames):
            if filename.startswith("."):
                continue
            yield current / filename


def iter_markdown_files_no_dot_dirs(root: Path) -> Iterable[Path]:
    for path in iter_files_no_dot_dirs(root):
        if path.is_file() and path.name.lower().endswith(".md"):
            yield path


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        current = Path(dirpath)
        dirnames[:] = [
            dirname
            for dirname in sorted(dirnames)
            if not should_skip_dir(root, current / dirname)
        ]
        for filename in sorted(filenames):
            if filename == "AGENTS.md":
                continue
            if filename.lower().endswith(".md"):
                yield current / filename


def path_for_report(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def split_lines(text: str) -> list[tuple[int, str]]:
    return list(enumerate(text.splitlines(), start=1))


def frontmatter_line_span(lines: Sequence[tuple[int, str]]) -> tuple[int, int] | None:
    if not lines:
        return None
    if lines[0][1].lstrip("\ufeff").strip() != "---":
        return None
    for idx, (_, line) in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return (1, idx + 1)
    return (1, len(lines))


def is_in_span(line_number: int, span: tuple[int, int] | None) -> bool:
    if span is None:
        return False
    start, end = span
    return start <= line_number <= end


def line_snippet(line: str, max_length: int = 140) -> str:
    stripped = line.strip()
    if len(stripped) <= max_length:
        return stripped
    return stripped[: max_length - 1] + "..."


def escape_markdown_cell(value: object) -> str:
    text = str(value).replace("\n", " ").strip()
    return text.replace("|", "\\|")


def build_note_stem_counts(root: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    for path in iter_markdown_files_no_dot_dirs(root):
        key = path.stem.casefold()
        counts[key] = counts.get(key, 0) + 1
    return counts


def is_generated_duplicate_scan_path(path: Path, root: Path) -> bool:
    rel_parts = path.relative_to(root).parts
    if "_generated" in rel_parts:
        return True
    if path.suffix.lower() in {".json", ".txt", ".vtt", ".yaml"}:
        return True
    return (
        len(rel_parts) >= 4
        and rel_parts[0] == "_sessions"
        and rel_parts[3] == "cleaned"
    )


def duplicate_filename_issues(root: Path, skip_generated: bool) -> tuple[list[Issue], int]:
    paths_by_name: dict[str, list[Path]] = {}
    file_count = 0

    for path in iter_files_no_dot_dirs(root):
        if not path.is_file():
            continue
        if skip_generated and is_generated_duplicate_scan_path(path, root):
            continue
        file_count += 1
        key = path.name.casefold()
        paths_by_name.setdefault(key, []).append(path)

    issues: list[Issue] = []
    for paths in paths_by_name.values():
        if len(paths) < 2:
            continue
        sorted_paths = sorted(paths, key=lambda path: path.relative_to(root).as_posix().casefold())
        display_paths = [path_for_report(path, root) for path in sorted_paths]
        issues.append(
            Issue(
                severity="warn",
                check="duplicate-filename",
                path=sorted_paths[0].name,
                line=0,
                message=f"Filename appears {len(sorted_paths)} times",
                snippet="; ".join(display_paths),
                suggestion="Rename or keep pathful links when this filename is a note target.",
            )
        )

    return issues, file_count


def note_link_target_parts(raw_target: str) -> tuple[str, str, str]:
    target_and_anchor, separator, alias = raw_target.partition("|")
    target, anchor_separator, anchor = target_and_anchor.partition("#")
    suffix = f"{anchor_separator}{anchor}" if anchor_separator else ""
    alias_suffix = f"{separator}{alias}" if separator else ""
    return target, suffix, alias_suffix


def simplified_wikilink_suggestion(
    basename: str,
    anchor_suffix: str,
    alias_suffix: str,
) -> str:
    if alias_suffix.startswith("|"):
        alias = alias_suffix[1:]
        if alias == basename and not anchor_suffix:
            alias_suffix = ""
    return f"[[{basename}{anchor_suffix}{alias_suffix}]]"


def pathful_wikilink_replacement(
    raw_target: str,
    stem_counts: dict[str, int],
) -> str | None:
    target, anchor_suffix, alias_suffix = note_link_target_parts(raw_target.strip())
    if "/" not in target:
        return None
    if Path(target).suffix.lower() in MEDIA_EXTENSIONS:
        return None

    basename = target.rsplit("/", 1)[-1]
    base_stem = Path(basename).stem
    if Path(basename).suffix.lower() == ".md":
        basename = base_stem
    if stem_counts.get(base_stem.casefold(), 0) != 1:
        return None

    replacement = simplified_wikilink_suggestion(
        basename,
        anchor_suffix,
        alias_suffix,
    )
    original = f"[[{raw_target}]]"
    if replacement == original:
        return None
    return replacement


def check_wikilinks(
    rel_path: str,
    numbered_lines: Sequence[tuple[int, str]],
    stem_counts: dict[str, int],
) -> list[Issue]:
    issues: list[Issue] = []
    for line_number, line in numbered_lines:
        for match in WIKILINK_PATTERN.finditer(line):
            raw_target = match.group(1).strip()
            target, _, _ = note_link_target_parts(raw_target)
            if "/" not in target:
                continue
            if Path(target).suffix.lower() in MEDIA_EXTENSIONS:
                continue

            replacement = pathful_wikilink_replacement(raw_target, stem_counts)
            unique = replacement is not None
            suggestion = ""
            message = "Wiki link uses a full path"
            severity = "warn"
            if unique:
                suggestion = replacement
            else:
                message += "; basename may be ambiguous"
                severity = "info"

            issues.append(
                Issue(
                    severity=severity,
                    check="pathful-wikilink",
                    path=rel_path,
                    line=line_number,
                    message=message,
                    snippet=line_snippet(line),
                    suggestion=suggestion,
                )
            )
    return issues


def check_export_blocks(
    rel_path: str,
    numbered_lines: Sequence[tuple[int, str]],
) -> list[Issue]:
    issues: list[Issue] = []
    stack: list[tuple[str, int, str]] = []

    for line_number, line in numbered_lines:
        for match in EXPORT_MARKER_PATTERN.finditer(line):
            kind = match.group(1).lower()
            marker = match.group(0)
            if kind == "end":
                if stack:
                    stack.pop()
                else:
                    issues.append(
                        Issue(
                            severity="warn",
                            check="orphan-export-end",
                            path=rel_path,
                            line=line_number,
                            message="Export block end marker has no matching start",
                            snippet=line_snippet(line),
                            suggestion="Remove the orphan marker or add the missing start marker.",
                        )
                    )
                continue

            stack.append((kind, line_number, marker))

    for kind, line_number, marker in stack:
        issues.append(
            Issue(
                severity="error",
                check="unclosed-export-block",
                path=rel_path,
                line=line_number,
                message=f"{marker} has no matching %%^End%% marker",
                snippet=marker,
                suggestion="Add %%^End%% after the block content.",
            )
        )

    return issues


def check_generic_comments(
    rel_path: str,
    numbered_lines: Sequence[tuple[int, str]],
) -> list[Issue]:
    issues: list[Issue] = []
    in_comment = False
    comment_start_line = 1
    comment_start_was_bare = False
    in_code_fence = False

    for line_number, line in numbered_lines:
        if line.lstrip().startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue

        idx = 0
        while idx < len(line):
            next_idx = line.find(GENERIC_COMMENT_DELIMITER, idx)
            if next_idx < 0:
                break
            if in_comment:
                in_comment = False
                comment_start_was_bare = False
            else:
                in_comment = True
                comment_start_line = line_number
                comment_start_was_bare = line.strip() == GENERIC_COMMENT_DELIMITER
            idx = next_idx + len(GENERIC_COMMENT_DELIMITER)

    if in_comment:
        if comment_start_was_bare:
            message = "Standalone %% marker has no matching comment delimiter"
            severity = "warn"
            suggestion = "If this closes an export block, use %%^End%% instead."
        else:
            message = "Obsidian comment appears to be missing its closing %%"
            severity = "error"
            suggestion = "Add a closing %% before the end of the file."
        issues.append(
            Issue(
                severity=severity,
                check="unclosed-comment",
                path=rel_path,
                line=comment_start_line,
                message=message,
                suggestion=suggestion,
            )
        )
    return issues


def check_secret_comments(
    rel_path: str,
    numbered_lines: Sequence[tuple[int, str]],
) -> list[Issue]:
    issues: list[Issue] = []
    for line_number, line in numbered_lines:
        if MALFORMED_SECRET_PATTERN.search(line):
            issues.append(
                Issue(
                    severity="warn",
                    check="malformed-secret-comment",
                    path=rel_path,
                    line=line_number,
                    message="SECRET comment marker has a space after %%",
                    snippet=line_snippet(line),
                    suggestion="Use %%SECRET with no space.",
                )
            )
    return issues


def check_typos(
    rel_path: str,
    numbered_lines: Sequence[tuple[int, str]],
    frontmatter_span: tuple[int, int] | None,
) -> list[Issue]:
    issues: list[Issue] = []
    in_code_fence = False

    for line_number, line in numbered_lines:
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence or is_in_span(line_number, frontmatter_span):
            continue

        for pattern, suggestion, label in TYPO_PATTERNS:
            if pattern.search(line):
                issues.append(
                    Issue(
                        severity="warn",
                        check="common-typo",
                        path=rel_path,
                        line=line_number,
                        message=label,
                        snippet=line_snippet(line),
                        suggestion=suggestion,
                    )
                )
    return issues


def check_markdown_polish(
    rel_path: str,
    numbered_lines: Sequence[tuple[int, str]],
    frontmatter_span: tuple[int, int] | None,
) -> list[Issue]:
    issues: list[Issue] = []
    in_code_fence = False

    for line_number, line in numbered_lines:
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue
        if is_in_span(line_number, frontmatter_span):
            continue

        if "\u00a0" in line:
            issues.append(
                Issue(
                    severity="info",
                    check="nonbreaking-space",
                    path=rel_path,
                    line=line_number,
                    message="Line contains a non-breaking space",
                    snippet=line_snippet(line.replace("\u00a0", "␠")),
                    suggestion="Replace with an ordinary space if the spacing is not intentional.",
                )
            )

        if "\u200b" in line:
            issues.append(
                Issue(
                    severity="info",
                    check="zero-width-space",
                    path=rel_path,
                    line=line_number,
                    message="Line contains a zero-width space",
                    snippet=line_snippet(line.replace("\u200b", "<ZWSP>")),
                    suggestion="Remove the invisible character if it is not intentional.",
                )
            )

        if DOUBLE_PERIOD_PATTERN.search(line):
            issues.append(
                Issue(
                    severity="warn",
                    check="double-period",
                    path=rel_path,
                    line=line_number,
                    message="Line contains a double period",
                    snippet=line_snippet(line),
                    suggestion="Use one period unless this is intentional punctuation.",
                )
            )

        repeated = REPEATED_WORD_PATTERN.search(line)
        if repeated:
            word = repeated.group(1)
            issues.append(
                Issue(
                    severity="info",
                    check="repeated-word",
                    path=rel_path,
                    line=line_number,
                    message=f"Repeated word: {word}",
                    snippet=line_snippet(line),
                    suggestion="Remove one copy if this is accidental.",
                )
            )

    return issues


def check_frontmatter(
    rel_path: str,
    numbered_lines: Sequence[tuple[int, str]],
) -> list[Issue]:
    if numbered_lines and numbered_lines[0][1].lstrip("\ufeff").strip() == "---":
        for _, line in numbered_lines[1:]:
            if line.strip() == "---":
                return []
        return [
            Issue(
                severity="error",
                check="unclosed-frontmatter",
                path=rel_path,
                line=1,
                message="YAML frontmatter starts but has no closing ---",
                suggestion="Add a closing --- line after the YAML block.",
            )
        ]
    return []


def line_start_offsets(text: str) -> list[int]:
    starts = [0]
    for match in re.finditer(r"\n", text):
        starts.append(match.end())
    return starts


def offset_to_line(offset: int, starts: Sequence[int]) -> int:
    low = 0
    high = len(starts)
    while low + 1 < high:
        mid = (low + high) // 2
        if starts[mid] <= offset:
            low = mid
        else:
            high = mid
    return low + 1


def collect_wikilink_replacements(
    text: str,
    stem_counts: dict[str, int],
) -> list[LinkReplacement]:
    replacements: list[LinkReplacement] = []
    starts = line_start_offsets(text)
    offset = 0
    in_code_fence = False

    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith("```"):
            in_code_fence = not in_code_fence
            offset += len(line)
            continue
        if in_code_fence:
            offset += len(line)
            continue

        for match in WIKILINK_PATTERN.finditer(line):
            raw_target = match.group(1)
            replacement = pathful_wikilink_replacement(raw_target, stem_counts)
            if replacement is None:
                continue

            start = offset + match.start()
            end = offset + match.end()
            replacements.append(
                LinkReplacement(
                    start=start,
                    end=end,
                    replacement=replacement,
                    line=offset_to_line(start, starts),
                    original=match.group(0),
                )
            )

        offset += len(line)

    return replacements


def apply_replacements(text: str, replacements: Sequence[LinkReplacement]) -> str:
    updated = text
    for replacement in sorted(replacements, key=lambda item: item.start, reverse=True):
        updated = (
            updated[: replacement.start]
            + replacement.replacement
            + updated[replacement.end :]
        )
    return updated


def replace_wikilinks(
    root: Path,
    stem_counts: dict[str, int],
    dry_run: bool,
) -> tuple[list[Issue], int, int]:
    files = list(iter_markdown_files(root))
    issues: list[Issue] = []
    changed_files = 0
    replacement_count = 0

    for path in files:
        rel_path = path_for_report(path, root)
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            issues.append(
                Issue(
                    severity="error",
                    check="read-error",
                    path=rel_path,
                    line=1,
                    message=str(exc),
                )
            )
            continue
        except OSError as exc:
            issues.append(
                Issue(
                    severity="error",
                    check="read-error",
                    path=rel_path,
                    line=1,
                    message=str(exc),
                )
            )
            continue

        replacements = collect_wikilink_replacements(text, stem_counts)
        if not replacements:
            continue

        changed_files += 1
        replacement_count += len(replacements)
        for replacement in replacements:
            issues.append(
                Issue(
                    severity="info",
                    check="wikilink-replacement",
                    path=rel_path,
                    line=replacement.line,
                    message=(
                        "Would replace pathful wiki link"
                        if dry_run
                        else "Replaced pathful wiki link"
                    ),
                    snippet=replacement.original,
                    suggestion=replacement.replacement,
                )
            )

        if not dry_run:
            updated = apply_replacements(text, replacements)
            path.write_text(updated, encoding="utf-8")

    return issues, changed_files, replacement_count


def scan_file(path: Path, root: Path, stem_counts: dict[str, int]) -> list[Issue]:
    rel_path = path_for_report(path, root)
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        return [
            Issue(
                severity="error",
                check="read-error",
                path=rel_path,
                line=1,
                message=str(exc),
            )
        ]

    numbered_lines = split_lines(text)
    frontmatter_span = frontmatter_line_span(numbered_lines)

    issues: list[Issue] = []
    issues.extend(check_frontmatter(rel_path, numbered_lines))
    issues.extend(check_wikilinks(rel_path, numbered_lines, stem_counts))
    issues.extend(check_export_blocks(rel_path, numbered_lines))
    issues.extend(check_generic_comments(rel_path, numbered_lines))
    issues.extend(check_secret_comments(rel_path, numbered_lines))
    issues.extend(check_typos(rel_path, numbered_lines, frontmatter_span))
    issues.extend(check_markdown_polish(rel_path, numbered_lines, frontmatter_span))
    return issues


def sort_issues(issues: Sequence[Issue]) -> list[Issue]:
    return sorted(
        issues,
        key=lambda issue: (
            -SEVERITY_ORDER[issue.severity],
            issue.path.casefold(),
            issue.line,
            issue.check,
        ),
    )


def filter_issues(issues: Sequence[Issue], min_severity: str) -> list[Issue]:
    threshold = SEVERITY_ORDER[min_severity]
    return [
        issue for issue in issues if SEVERITY_ORDER[issue.severity] >= threshold
    ]


def render_markdown(
    root: Path,
    file_count: int,
    issues: Sequence[Issue],
    total_issue_count: int,
    limit: int,
    title: str = "Vault Quality Scan",
    scope_description: str = "skips dot directories, underscore directories, and configured raw-material subtrees",
    extra_summary: Sequence[str] = (),
) -> str:
    visible = list(issues)
    limited = limit > 0 and len(visible) > limit
    if limited:
        visible = visible[:limit]

    lines = [
        f"# {title}",
        "",
        f"- Root: `{root}`",
        f"- Scope: {scope_description}",
        f"- Files scanned: {file_count}",
        f"- Issues found: {total_issue_count}",
    ]
    lines.extend(extra_summary)
    if limited:
        lines.append(f"- Issues shown: {limit}")

    if not visible:
        lines.extend(["", "No issues found."])
        return "\n".join(lines) + "\n"

    lines.extend(
        [
            "",
            "| Severity | Check | File | Line | Message | Suggestion | Snippet |",
            "|---|---|---|---:|---|---|---|",
        ]
    )
    for issue in visible:
        lines.append(
            "| "
            + " | ".join(
                escape_markdown_cell(value)
                for value in (
                    issue.severity,
                    issue.check,
                    issue.path,
                    issue.line,
                    issue.message,
                    issue.suggestion,
                    issue.snippet,
                )
            )
            + " |"
        )
    return "\n".join(lines) + "\n"


def render_tsv(issues: Sequence[Issue]) -> str:
    rows = [
        "\t".join(
            ("severity", "check", "path", "line", "message", "suggestion", "snippet")
        )
    ]
    for issue in issues:
        rows.append(
            "\t".join(
                str(value).replace("\t", " ").replace("\n", " ")
                for value in (
                    issue.severity,
                    issue.check,
                    issue.path,
                    issue.line,
                    issue.message,
                    issue.suggestion,
                    issue.snippet,
                )
            )
        )
    return "\n".join(rows) + "\n"


def render_json(
    root: Path,
    file_count: int,
    issues: Sequence[Issue],
    skipped: dict[str, object] | None = None,
    extra: dict[str, object] | None = None,
) -> str:
    payload = {
        "root": str(root),
        "skipped": skipped or {
            "directoryPrefixes": [".", "_"],
            "subtrees": ["/".join(parts) for parts in sorted(SKIP_SUBTREES)],
        },
        "filesScanned": file_count,
        "issues": [asdict(issue) for issue in issues],
    }
    if extra:
        payload.update(extra)
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def write_report(text: str, output: str | None) -> None:
    if output:
        Path(output).expanduser().write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)


def main() -> int:
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    if not root.exists():
        raise SystemExit(f"Root does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Root is not a directory: {root}")
    if args.dry_run and not args.replace_wikilinks:
        raise SystemExit("--dry-run is only meaningful with --replace-wikilinks")
    if args.duplicate_filenames and args.replace_wikilinks:
        raise SystemExit("--duplicate-filenames and --replace-wikilinks are separate modes")
    if args.skip_generated and not args.duplicate_filenames:
        raise SystemExit("--skip-generated is only meaningful with --duplicate-filenames")

    stem_counts = build_note_stem_counts(root)

    if args.duplicate_filenames:
        issues, file_count = duplicate_filename_issues(root, args.skip_generated)
        filtered_issues = sort_issues(filter_issues(issues, args.min_severity))
        total_issue_count = len(filtered_issues)
        skipped = {"directoryPrefixes": ["."], "filePrefixes": ["."]}
        extra_summary: tuple[str, ...] = ()
        scope_description = "skips dot directories and dotfiles only"
        if args.skip_generated:
            skipped["generatedLike"] = [
                "_generated paths",
                ".json/.txt/.vtt/.yaml files",
                "_sessions/<campaign>/<session>/cleaned paths",
            ]
            scope_description += "; skips generated/session-cleanup material"
            extra_summary = ("- Generated/session-cleanup filter: on",)
        if args.format == "json":
            report = render_json(root, file_count, filtered_issues, skipped=skipped)
        elif args.format == "tsv":
            visible = filtered_issues
            if args.limit > 0:
                visible = visible[: args.limit]
            report = render_tsv(visible)
        else:
            report = render_markdown(
                root,
                file_count,
                filtered_issues,
                total_issue_count,
                args.limit,
                title="Duplicate Filename Scan",
                scope_description=scope_description,
                extra_summary=extra_summary,
            )
        write_report(report, args.output)
        return 1 if any(issue.severity == "error" for issue in filtered_issues) else 0

    if args.replace_wikilinks:
        issues, changed_files, replacement_count = replace_wikilinks(
            root,
            stem_counts,
            args.dry_run,
        )
        file_count = len(list(iter_markdown_files(root)))
        filtered_issues = sort_issues(filter_issues(issues, args.min_severity))
        total_issue_count = len(filtered_issues)
        extra = {
            "dryRun": args.dry_run,
            "changedFiles": changed_files,
            "replacementCount": replacement_count,
        }
        if args.format == "json":
            report = render_json(root, file_count, filtered_issues, extra=extra)
        elif args.format == "tsv":
            visible = filtered_issues
            if args.limit > 0:
                visible = visible[: args.limit]
            report = render_tsv(visible)
        else:
            action = "Wikilink Replacement Dry Run" if args.dry_run else "Wikilink Replacement"
            file_summary_label = (
                "Files that would change" if args.dry_run else "Files changed"
            )
            replacement_summary_label = (
                "Potential replacements" if args.dry_run else "Replacements"
            )
            report = render_markdown(
                root,
                file_count,
                filtered_issues,
                total_issue_count,
                args.limit,
                title=action,
                extra_summary=(
                    f"- {file_summary_label}: {changed_files}",
                    f"- {replacement_summary_label}: {replacement_count}",
                ),
            )
        write_report(report, args.output)
        return 1 if any(issue.severity == "error" for issue in filtered_issues) else 0

    files = list(iter_markdown_files(root))
    issues: list[Issue] = []
    for path in files:
        issues.extend(scan_file(path, root, stem_counts))

    filtered_issues = sort_issues(filter_issues(issues, args.min_severity))
    total_issue_count = len(filtered_issues)

    if args.format == "json":
        report = render_json(root, len(files), filtered_issues)
    elif args.format == "tsv":
        visible = filtered_issues
        if args.limit > 0:
            visible = visible[: args.limit]
        report = render_tsv(visible)
    else:
        report = render_markdown(
            root,
            len(files),
            filtered_issues,
            total_issue_count,
            args.limit,
        )

    write_report(report, args.output)
    return 1 if any(issue.severity == "error" for issue in filtered_issues) else 0


if __name__ == "__main__":
    raise SystemExit(main())

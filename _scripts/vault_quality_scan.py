#!/usr/bin/env python3
"""Read-only quality scanner for Taelgar Obsidian markdown notes."""

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
H1_PATTERN = re.compile(r"^#\s+\S")


@dataclass(frozen=True)
class Issue:
    severity: str
    check: str
    path: str
    line: int
    message: str
    snippet: str = ""
    suggestion: str = ""


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
    return parser.parse_args()


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
    for path in iter_markdown_files(root):
        key = path.stem.casefold()
        counts[key] = counts.get(key, 0) + 1
    return counts


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
        if alias == basename:
            alias_suffix = ""
    return f"[[{basename}{anchor_suffix}{alias_suffix}]]"


def check_wikilinks(
    rel_path: str,
    numbered_lines: Sequence[tuple[int, str]],
    stem_counts: dict[str, int],
) -> list[Issue]:
    issues: list[Issue] = []
    for line_number, line in numbered_lines:
        for match in WIKILINK_PATTERN.finditer(line):
            raw_target = match.group(1).strip()
            target, anchor_suffix, alias_suffix = note_link_target_parts(raw_target)
            if "/" not in target:
                continue
            if Path(target).suffix.lower() in MEDIA_EXTENSIONS:
                continue

            basename = target.rsplit("/", 1)[-1]
            base_stem = Path(basename).stem
            if Path(basename).suffix.lower() == ".md":
                basename = base_stem
            unique = stem_counts.get(base_stem.casefold(), 0) == 1
            suggestion = ""
            message = "Wiki link uses a full path"
            severity = "warn"
            if unique:
                suggestion = simplified_wikilink_suggestion(
                    basename,
                    anchor_suffix,
                    alias_suffix,
                )
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
    has_h1 = False
    in_code_fence = False

    for line_number, line in numbered_lines:
        stripped = line.lstrip()
        if stripped.startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue
        if H1_PATTERN.match(stripped):
            has_h1 = True
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

    if not has_h1:
        issues.append(
            Issue(
                severity="info",
                check="missing-h1",
                path=rel_path,
                line=1,
                message="Note has no top-level H1 heading",
                suggestion="Add a # heading if this note is meant to publish as a page.",
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
) -> str:
    visible = list(issues)
    limited = limit > 0 and len(visible) > limit
    if limited:
        visible = visible[:limit]

    lines = [
        "# Vault Quality Scan",
        "",
        f"- Root: `{root}`",
        "- Scope: skips dot directories, underscore directories, and `Worldbuilding/Chats and Emails`",
        f"- Files scanned: {file_count}",
        f"- Issues found: {total_issue_count}",
    ]
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
) -> str:
    payload = {
        "root": str(root),
        "skipped": {
            "directoryPrefixes": [".", "_"],
            "subtrees": ["/".join(parts) for parts in sorted(SKIP_SUBTREES)],
        },
        "filesScanned": file_count,
        "issues": [asdict(issue) for issue in issues],
    }
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

    stem_counts = build_note_stem_counts(root)
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

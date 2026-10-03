#!/usr/bin/env python3
"""Preview or delete redundant artifacts in selected completed session bundles.

Examples (from the vault root):
    python3 _scripts/cleanup_session_artifacts.py dunmar-frontier 1-6
    python3 _scripts/cleanup_session_artifacts.py lablost 1,3 --execute
    python3 _scripts/cleanup_session_artifacts.py feywild 4 --include-atypical

Only --execute writes. --include-atypical widens deletion inside the three
artifact directories, never directly under cleaned/. Recaps, both sources,
manifests, beats, beat facts, scene maps and approvals, timeline evidence and
reviews, speaker statistics, polished transcripts, highlights, drafts, and
exports are preserved. The cleaned source
and recap are the required inputs to beat-transcript-polisher; neither depends
on the artifacts deleted here, even when polishing has not happened yet.
Regular .DS_Store files are disposable Finder metadata and are also deleted
throughout cleaned/. They do not prevent otherwise empty artifact folders
from being removed. Other directories are retained, even if emptied of metadata.

Cleanup assessments, correction/acceptance decisions, and before-review or
before-apply snapshots are disposable once review is complete and corrections
are incorporated into the retained cleaned source. Deleting them discards the
cleanup review history, including accepted uncertainty; restarting transcript
cleanup may require reassessment. Timeline evidence retains authored chronology
reasoning, timeline reviews validate it, and scene approvals support resuming
summary generation without repeating approval of unchanged inputs.

Each bundle must have a nonempty recap, both sources, beats, beat facts, and
manifest. Incomplete bundles are skipped with a nonzero exit status. No override
permits cleaning a bundle without its recap. Symbolic links are never followed
or deleted. Files that changed after planning are refused before that bundle's
deletions start. Only empty artifact directories are removed.

The typical filename lists follow the current pipeline helpers. New or legacy
filenames are reported as atypical rather than silently included.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from decimal import Decimal
from pathlib import Path
import re
import stat
import sys
from typing import Optional, Sequence


VAULT_ROOT = Path(__file__).resolve().parents[1]
ARTIFACT_DIRS = {"cleanup-artifacts", "annotation-artifacts", "annotation-context"}
FINDER_METADATA = ".DS_Store"
DELETE_SUFFIXES = {
    "beats-preview.md",
    "beat-facts-preview.md",
    "recap-scenes-preview.md",
    "session-summary-context.json",
}
KEEP_SUFFIXES = {
    "session.yaml", "session-recap.md", "source-prepared.md", "source-cleaned.md",
    "beats.json", "beat-facts.json", "recap-scenes.json", "speaker-stats.json",
    "scene-approval.json", "timeline-evidence.json", "timeline-review.json",
}
KEEP_DIRS = {"beat-transcripts", "normalization-artifacts", "supplemental"}
REQUIRED_SUFFIXES = (
    "session-recap.md", "source-prepared.md", "source-cleaned.md",
    "beats.json", "beat-facts.json", "session.yaml",
)
TYPICAL_ARTIFACT_SUFFIXES = {
    "cleanup-artifacts": {
        "cleanup-report.json", "cleanup-summary.md", "session-corrections.yaml",
        "human-transcript.md", "cleanup-assessment.json",
        "cleanup-assessment-before-review.json", "cleanup-decisions.json",
        "cleanup-decisions.before-apply.md",
    },
    "annotation-artifacts": {"beat-facts.json", "beat-facts-preview.md"},
    "annotation-context": {"beat-contexts.json", "beat-context-index.md"},
}
SESSION_RE = re.compile(r"[0-9]+(?:\.[0-9]+)?")
CONTEXT_FILE_RE = re.compile(r"(?:b[0-9]+|beat-[0-9]+)\.md", re.IGNORECASE)


class CleanupError(ValueError):
    pass


@dataclass(frozen=True)
class Candidate:
    path: Path
    signature: tuple[int, int, int, int, int]
    atypical: bool = False

    @property
    def size(self) -> int:
        return self.signature[-1]


@dataclass
class Plan:
    bundle: Path
    prefix: str
    files: list[Candidate] = field(default_factory=list)
    directories: list[Path] = field(default_factory=list)
    atypical: list[Path] = field(default_factory=list)
    protected: list[tuple[Path, str]] = field(default_factory=list)
    deleted_files: list[Candidate] = field(default_factory=list)
    removed_directories: list[Path] = field(default_factory=list)

    @property
    def cleaned(self) -> Path:
        return self.bundle / "cleaned"


def parse_sessions(value: str) -> tuple[Decimal, ...]:
    """Accept singles, comma-separated lists, and inclusive integer ranges.

    Mixed selectors such as 1,4,7-9 are supported. Fractional session IDs may
    be specified explicitly (29.1); integer ranges do not include them.
    """
    sessions: set[Decimal] = set()
    for token in value.split(","):
        token = token.strip()
        if SESSION_RE.fullmatch(token):
            sessions.add(Decimal(token))
            continue
        match = re.fullmatch(r"([0-9]+)\s*-\s*([0-9]+)", token)
        if not match:
            raise argparse.ArgumentTypeError(
                "Use a session number, a list (1,4,7), or an inclusive range (1-3)."
            )
        start, end = map(int, match.groups())
        if start > end:
            raise argparse.ArgumentTypeError(f"Reversed session range: {token}")
        sessions.update(Decimal(number) for number in range(start, end + 1))
    return tuple(sorted(sessions))


def signature(path: Path) -> tuple[int, int, int, int, int]:
    info = path.lstat()
    return (info.st_dev, info.st_ino, info.st_mode, info.st_mtime_ns, info.st_size)


def regular_file(path: Path) -> bool:
    return path.is_file() and not path.is_symlink()


def check_bundle(bundle: Path, prefix: str) -> None:
    if bundle.is_symlink() or not bundle.is_dir():
        raise CleanupError("bundle is missing or is a symbolic link")
    cleaned = bundle / "cleaned"
    if cleaned.is_symlink() or not cleaned.is_dir():
        raise CleanupError("cleaned/ is missing or is a symbolic link")
    for suffix in REQUIRED_SUFFIXES:
        path = cleaned / f"{prefix}-{suffix}"
        if not regular_file(path) or path.stat().st_size == 0:
            raise CleanupError(f"required file is missing, empty, or linked: {path.name}")


def typical_artifact(relative: Path, directory: str, prefix: str) -> bool:
    if relative.name == FINDER_METADATA:
        return True
    if len(relative.parts) == 1:
        return relative.name in {
            f"{prefix}-{suffix}" for suffix in TYPICAL_ARTIFACT_SUFFIXES[directory]
        }
    return (
        directory == "annotation-context"
        and len(relative.parts) == 2
        and relative.parts[0] == "contexts"
        and CONTEXT_FILE_RE.fullmatch(relative.name) is not None
    )


def walk_artifacts(directory: Path) -> tuple[list[Path], list[Path]]:
    """List files and directories without descending through symbolic links."""
    files: list[Path] = []
    directories = [directory]
    for child in sorted(directory.iterdir()):
        if child.is_dir() and not child.is_symlink():
            nested_files, nested_dirs = walk_artifacts(child)
            files.extend(nested_files)
            directories.extend(nested_dirs)
        else:
            files.append(child)
    return files, directories


def unique_facts_copy(path: Path, cleaned: Path) -> bool:
    """Avoid deleting the only copy of an annotation, even with the extra flag."""
    if path.parent != cleaned / "annotation-artifacts" or path.name != f"{cleaned.parent.name}-beat-facts.json":
        return False
    retained = cleaned / path.name
    return not regular_file(retained) or path.read_bytes() != retained.read_bytes()


def build_plan(bundle: Path, *, include_atypical: bool = False) -> Plan:
    prefix = bundle.name
    check_bundle(bundle, prefix)
    plan = Plan(bundle=bundle, prefix=prefix)
    delete_names = {f"{prefix}-{suffix}" for suffix in DELETE_SUFFIXES} | {FINDER_METADATA}
    keep_names = {f"{prefix}-{suffix}" for suffix in KEEP_SUFFIXES}

    for path in sorted(plan.cleaned.iterdir()):
        if path.is_symlink():
            plan.atypical.append(path)
            plan.protected.append((path, "symbolic link; never followed or deleted"))
        elif path.name in ARTIFACT_DIRS and path.is_dir():
            files, directories = walk_artifacts(path)
            for artifact in files:
                relative = artifact.relative_to(path)
                typical = typical_artifact(relative, path.name, prefix)
                if not typical:
                    plan.atypical.append(artifact)
                mode = artifact.lstat().st_mode
                if not stat.S_ISREG(mode):
                    plan.protected.append((artifact, "symbolic link or special file"))
                elif (typical or include_atypical) and unique_facts_copy(artifact, plan.cleaned):
                    plan.protected.append((artifact, "no byte-identical retained beat-facts copy"))
                elif typical or include_atypical:
                    plan.files.append(Candidate(artifact, signature(artifact), not typical))

            for directory in directories[1:]:
                if not (path.name == "annotation-context" and directory == path / "contexts"):
                    plan.atypical.append(directory)

            # Predict which folders will be empty, so dry run shows those too.
            removable = {candidate.path for candidate in plan.files}
            metadata = [artifact for artifact in files if artifact.name == FINDER_METADATA and regular_file(artifact)]
            for directory in sorted(directories, key=lambda p: len(p.parts), reverse=True):
                typical_dir = directory == path or (
                    path.name == "annotation-context" and directory == path / "contexts"
                )
                has_metadata = any(directory in artifact.parents for artifact in metadata)
                if (typical_dir or include_atypical or has_metadata) and all(
                    child in removable for child in directory.iterdir()
                ):
                    plan.directories.append(directory)
                    removable.add(directory)
                    if has_metadata and directory in plan.atypical:
                        plan.atypical.remove(directory)
        elif path.name in delete_names and regular_file(path):
            plan.files.append(Candidate(path, signature(path)))
        elif (path.name in keep_names and regular_file(path)) or (
            path.name in KEEP_DIRS and path.is_dir()
        ):
            continue
        else:
            # No flag can opt these root-level entries into deletion.
            plan.atypical.append(path)

    # Include Finder metadata in retained and unexpected directories as well,
    # without widening deletion to their substantive contents or following links.
    selected = {candidate.path for candidate in plan.files}
    files, _directories = walk_artifacts(plan.cleaned)
    for path in files:
        if path.name == FINDER_METADATA and path not in selected and regular_file(path):
            plan.files.append(Candidate(path, signature(path)))

    plan.files.sort(key=lambda candidate: str(candidate.path))
    plan.atypical = sorted(set(plan.atypical))
    return plan


def execute_plan(plan: Plan) -> None:
    """Recheck the whole bundle before unlinking any of its planned files."""
    # Also check parent paths in case a folder was replaced by a symbolic link.
    for parent in (plan.bundle.parent.parent, plan.bundle.parent):
        if parent.is_symlink() or not parent.is_dir():
            raise CleanupError(f"session parent changed or is linked: {parent}")
    check_bundle(plan.bundle, plan.prefix)
    for candidate in plan.files:
        for parent in candidate.path.parents:
            if parent == plan.bundle:
                break
            if parent.is_symlink():
                raise CleanupError(f"symbolic link appeared after planning: {parent}")
        if not regular_file(candidate.path) or signature(candidate.path) != candidate.signature:
            raise CleanupError(f"file changed after planning: {candidate.path}")
        if candidate.path.parent != plan.cleaned and unique_facts_copy(candidate.path, plan.cleaned):
            raise CleanupError(f"beat-facts copy changed after planning: {candidate.path}")
    for directory in plan.directories:
        if directory.is_symlink() or not directory.is_dir():
            raise CleanupError(f"artifact directory changed after planning: {directory}")

    for candidate in plan.files:
        candidate.path.unlink()
        plan.deleted_files.append(candidate)
    for directory in plan.directories:
        # rmdir never removes a nonempty folder, including files added meanwhile.
        if not any(directory.iterdir()):
            directory.rmdir()
            plan.removed_directories.append(directory)


def discover_bundles(root: Path, campaign: str, sessions: Sequence[Decimal]) -> tuple[list[Path], list[str]]:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", campaign):
        raise CleanupError("campaign must be a folder name, without a path")
    session_root = root / "_sessions"
    campaign_dir = session_root / campaign
    for directory in (session_root, campaign_dir):
        if directory.is_symlink() or not directory.is_dir():
            raise CleanupError(f"campaign directory is missing or linked: {directory}")
    matches: dict[Decimal, list[Path]] = {number: [] for number in sessions}
    for path in sorted(campaign_dir.iterdir()):
        suffix = path.name.rsplit("-", 1)[-1]
        if SESSION_RE.fullmatch(suffix) and (path.is_dir() or path.is_symlink()):
            number = Decimal(suffix)
            if number in matches:
                matches[number].append(path)
    bundles: list[Path] = []
    errors: list[str] = []
    for number, paths in matches.items():
        if len(paths) == 1:
            bundles.extend(paths)
        elif not paths:
            errors.append(f"session {number}: no matching bundle in {campaign}")
        else:
            errors.append(f"session {number}: ambiguous bundles: {', '.join(p.name for p in paths)}")
    return bundles, errors


def display(path: Path, root: Path) -> str:
    return str(path.relative_to(root))


def main(argv: Optional[Sequence[str]] = None, *, vault_root: Optional[Path] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("campaign", help="Folder under _sessions/, e.g. dunmar-frontier or lablost.")
    parser.add_argument("sessions", type=parse_sessions, help="Single, list, or range: 1; 1,4,7; 1-3. Fractional IDs may be listed explicitly.")
    parser.add_argument("--execute", action="store_true", help="Delete the listed files. Default: dry run.")
    parser.add_argument("--include-atypical", action="store_true", help="Also delete atypical regular files inside cleanup-artifacts, annotation-artifacts, and annotation-context only.")
    args = parser.parse_args(argv)
    root = (vault_root if vault_root is not None else VAULT_ROOT).resolve()
    try:
        bundles, errors = discover_bundles(root, args.campaign, args.sessions)
    except (CleanupError, OSError) as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        return 1

    print("EXECUTE" if args.execute else "DRY RUN: no files will be deleted; use --execute to delete.")
    plans: list[Plan] = []
    for bundle in bundles:
        try:
            plans.append(build_plan(bundle, include_atypical=args.include_atypical))
        except (CleanupError, OSError) as exc:
            errors.append(f"{display(bundle, root)}: {exc}")
    for error in errors:
        print(f"SKIPPED: {error}")

    for plan in plans:
        print(f"\n{display(plan.bundle, root)}")
        for candidate in plan.files:
            label = "PLAN DELETE" if args.execute else "WOULD DELETE"
            extra = " [atypical]" if candidate.atypical else ""
            print(f"  {label} {display(candidate.path, root)} ({candidate.size:,} bytes){extra}")
        for directory in plan.directories:
            label = "PLAN REMOVE EMPTY DIR" if args.execute else "WOULD REMOVE EMPTY DIR"
            print(f"  {label} {display(directory, root)}")
        selected = {candidate.path for candidate in plan.files} | set(plan.directories)
        for path in plan.atypical:
            disposition = "selected by --include-atypical" if path in selected else "kept"
            print(f"  ATYPICAL ({disposition}): {display(path, root)}")
        for path, reason in plan.protected:
            print(f"  PROTECTED: {display(path, root)} — {reason}")
        if not plan.files and not plan.directories:
            print("  Nothing to delete.")

    if args.execute:
        for plan in plans:
            try:
                execute_plan(plan)
            except (CleanupError, OSError) as exc:
                errors.append(str(exc))
                print(f"REFUSED/FAILED: {display(plan.bundle, root)}: {exc}", file=sys.stderr)
    files = [candidate for plan in plans for candidate in (
        plan.deleted_files if args.execute else plan.files
    )]
    count = len(files)
    size = sum(candidate.size for candidate in files)
    dirs = sum(len(plan.removed_directories if args.execute else plan.directories) for plan in plans)
    print(f"\n{'Deleted' if args.execute else 'Would delete'} {count} files ({size:,} bytes); "
          f"{dirs} empty directories {'removed' if args.execute else 'would be removed'}; "
          f"{len(plans)} eligible bundles; {len(errors)} skipped/failed.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

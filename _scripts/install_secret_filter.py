#!/usr/bin/env python3
"""Persistently activate the tracked Taelgar secret-filter configuration."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess
import sys
from typing import List, Optional, Sequence


class InstallError(RuntimeError):
    pass


GIT_EXECUTABLE = shutil.which("git") or "git"


def run_git(arguments: Sequence[str], cwd: Optional[Path] = None) -> str:
    completed = subprocess.run(
        [GIT_EXECUTABLE] + list(arguments),
        cwd=str(cwd) if cwd else None,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if completed.returncode != 0:
        raise InstallError(completed.stderr.strip() or "git command failed")
    return completed.stdout.strip()


def include_key(git_dir: Path) -> str:
    return "includeIf.gitdir:{}.path".format(git_dir.as_posix().rstrip("/"))


def existing_values(key: str) -> List[str]:
    completed = subprocess.run(
        [GIT_EXECUTABLE, "config", "--global", "--get-all", key],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if completed.returncode not in {0, 1}:
        raise InstallError(completed.stderr.strip() or "could not read global Git config")
    return [line for line in completed.stdout.splitlines() if line]


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify the active configuration without changing global Git settings",
    )
    args = parser.parse_args(argv)

    try:
        repo_root = Path(run_git(["rev-parse", "--show-toplevel"])).resolve()
        git_dir = Path(run_git(["rev-parse", "--absolute-git-dir"])).resolve()
        config_path = (repo_root / "_scripts" / "secret-filter.gitconfig").resolve()
        filter_script = repo_root / "_scripts" / "secret_filter.py"
        if not config_path.is_file() or not filter_script.is_file():
            raise InstallError("tracked secret-filter files are missing")

        if not args.check:
            key = include_key(git_dir)
            values = existing_values(key)
            if str(config_path) not in values:
                run_git(["config", "--global", "--add", key, str(config_path)])

        completed = subprocess.run(
            [sys.executable, str(filter_script), "doctor"],
            cwd=str(repo_root),
            check=False,
        )
        if completed.returncode != 0:
            raise InstallError("the installed configuration did not pass its self-check")
        print("Taelgar secret filter installed for {}".format(repo_root))
        return 0
    except InstallError as exc:
        print("secret-filter installation error: {}".format(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

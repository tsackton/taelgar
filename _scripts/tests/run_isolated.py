#!/usr/bin/env python3
"""Run regression tests from a temporary copy of code and explicit fixtures only."""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[2]
CODE_ROOTS = (
    "_scripts",
    ".agents/skills",
    ".obsidian/plugins/taelgar-name-explorer",
    ".obsidian/plugins/taelgar-dataview-materializer",
)
SOURCE_SUFFIXES = {".py", ".rb", ".js", ".mjs", ".swift", ".html"}
SKIP_DIRS = {".git", "node_modules", "__pycache__", ".pytest_cache", ".venv", "venv"}


def test_fixture(relative: Path) -> bool:
    parts = relative.parts
    return any(
        parts[index] == "tests" and parts[index + 1] in {"fixtures", "data"}
        for index in range(len(parts) - 1)
    )


def copy_test_tree(destination: Path) -> None:
    for relative_root in CODE_ROOTS:
        for directory, children, filenames in os.walk(ROOT / relative_root):
            children[:] = sorted(name for name in children if name not in SKIP_DIRS)
            for name in sorted(filenames):
                source = Path(directory) / name
                relative = source.relative_to(ROOT)
                if source.suffix not in SOURCE_SUFFIXES and not test_fixture(relative):
                    continue
                if source.is_symlink():
                    raise ValueError(f"Test inputs must not link to working data: {relative}")
                target = destination / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, target)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--python", default=sys.executable)
    parser.add_argument("--ruby", default="ruby")
    parser.add_argument("--node", default="node")
    args = parser.parse_args()
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    with tempfile.TemporaryDirectory(prefix="taelgar-regression-") as temporary:
        root = Path(temporary)
        copy_test_tree(root)
        python_tests = sorted(root.rglob("test_*.py"))
        ruby_tests = sorted(root.rglob("test_*.rb"))
        js_tests = sorted([*root.rglob("test_*.js"), *root.rglob("test-*.js"), *root.rglob("*.test.mjs")])
        count = len(python_tests) + len(ruby_tests) + len(js_tests)
        if not count:
            raise RuntimeError("No regression tests found")
        commands = [
            [args.python, "-m", "unittest", "discover", "-s", str(directory.relative_to(root)), "-p", "test_*.py"]
            for directory in sorted({test.parent for test in python_tests})
        ]
        commands.extend([args.ruby, str(test.relative_to(root))] for test in ruby_tests)
        commands.extend(
            [args.node, *(["--test"] if test.name.endswith(".test.mjs") else []), str(test.relative_to(root))]
            for test in js_tests
        )
        print(f"Running {count} test files in a code-and-fixture-only tree: {root}", flush=True)
        failures = []
        for command in commands:
            print(f"\n>>> {' '.join(command)}", flush=True)
            result = subprocess.run(command, cwd=root, env=env, capture_output=True, text=True)
            print(result.stdout + result.stderr, end="", flush=True)
            if result.returncode:
                failures.append(command)
        print(f"\n{len(commands) - len(failures)}/{len(commands)} test commands passed ({count} test files).")
        return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())

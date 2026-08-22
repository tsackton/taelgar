from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest


SCRIPT_PATH = Path(__file__).with_name("secret_filter.py")
GIT_EXECUTABLE = shutil.which("git") or "git"
SPEC = importlib.util.spec_from_file_location("secret_filter", SCRIPT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not import {}".format(SCRIPT_PATH))
secret_filter = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = secret_filter
SPEC.loader.exec_module(secret_filter)


class SecretFilterTest(unittest.TestCase):
    def make_directory(self, prefix: str = "secret-filter-test.") -> Path:
        path = Path(tempfile.mkdtemp(prefix=prefix))
        self.addCleanup(lambda: shutil.rmtree(path, ignore_errors=True))
        return path

    def test_v2_clean_and_smudge_are_exact_round_trip(self) -> None:
        store = self.make_directory()
        original = (
            b"---\n"
            b"name: Public\n"
            b"whereabouts: Hidden Place ##secret current location\n"
            b"---\n"
            b"Public before %%SECRETinline detail%% after.\n"
            b"%%SECRET\nmultiline detail\n%%\n"
        )
        cleaned = secret_filter.clean_bytes(original, "People/Example.md", store)

        self.assertNotIn(b"inline detail", cleaned)
        self.assertNotIn(b"Hidden Place", cleaned)
        self.assertEqual(len(re.findall(rb"v2:[0-9a-f]{32}", cleaned)), 3)
        self.assertEqual(secret_filter.scan_raw_secrets(cleaned), [])
        self.assertEqual(
            secret_filter.smudge_bytes(cleaned, "People/Example.md", store, None),
            original,
        )

        sidecar = secret_filter.sidecar_path(store, "People/Example.md")
        self.assertTrue(sidecar.is_file())
        self.assertEqual(stat.S_IMODE(sidecar.stat().st_mode), 0o600)

    def test_placeholders_are_deterministic(self) -> None:
        raw = b"Public %%SECRETsame detail%% text\n"
        first = secret_filter.clean_bytes(raw, "One.md", None)
        second = secret_filter.clean_bytes(raw, "Elsewhere/Two.md", None)
        self.assertEqual(first, second)

    def test_same_basename_uses_distinct_path_keyed_sidecars(self) -> None:
        store = self.make_directory()
        first_raw = b"%%SECRETfirst%%\n"
        second_raw = b"%%SECRETsecond%%\n"
        first_clean = secret_filter.clean_bytes(first_raw, "A/Same.md", store)
        second_clean = secret_filter.clean_bytes(second_raw, "B/Same.md", store)

        self.assertNotEqual(
            secret_filter.sidecar_path(store, "A/Same.md"),
            secret_filter.sidecar_path(store, "B/Same.md"),
        )
        self.assertEqual(
            secret_filter.smudge_bytes(first_clean, "A/Same.md", store, None),
            first_raw,
        )
        self.assertEqual(
            secret_filter.smudge_bytes(second_clean, "B/Same.md", store, None),
            second_raw,
        )

    def test_yaml_marker_is_filtered_only_in_initial_frontmatter(self) -> None:
        raw = (
            b"---\n"
            b"born: 1696 ##secret year\n"
            b"---\n"
            b"Documentation example: born: 1696 ##secret year\n"
        )
        cleaned = secret_filter.clean_bytes(raw, "Example.md", None)
        self.assertNotIn(b"born: 1696 ##secret year\n---", cleaned)
        self.assertIn(b"Documentation example: born: 1696 ##secret year", cleaned)

    def test_unclosed_block_fails_closed(self) -> None:
        with self.assertRaises(secret_filter.SecretFilterError):
            secret_filter.clean_bytes(b"Public\n%%SECRET never closed", "Bad.md", None)

    def test_legacy_numeric_placeholders_restore_by_document_order(self) -> None:
        store = self.make_directory()
        legacy = self.make_directory()
        (legacy / "Legacy.md.1").write_bytes(b"first detail")
        (legacy / "Legacy.md.2").write_bytes(b"field: hidden ")
        data = b"%%SECRET[44]%%\n###secret[3] suffix\n"

        restored = secret_filter.smudge_bytes(data, "Folder/Legacy.md", store, legacy)
        self.assertEqual(
            restored,
            b"%%SECRETfirst detail%%\nfield: hidden ##secret suffix\n",
        )

    def test_clean_preserves_legacy_and_v2_placeholders(self) -> None:
        data = (
            b"%%SECRET[1]%%\n"
            b"%%SECRET[v2:0123456789abcdef0123456789abcdef]%%\n"
            b"###secret[2]\n"
        )
        self.assertEqual(secret_filter.clean_bytes(data, "Example.md", None), data)

    def test_history_clean_is_deterministic_and_has_no_sidecar(self) -> None:
        data = b"Public %%SECRETdetail%% text\n"
        cleaned = secret_filter.clean_history_bytes(data)
        self.assertEqual(cleaned, secret_filter.clean_history_bytes(data))
        self.assertNotIn(b"detail", cleaned)
        self.assertEqual(secret_filter.scan_raw_secrets(cleaned), [])

    def test_history_clean_honors_legacy_secret_through_end_of_file(self) -> None:
        data = b"Public\n%%SECRET legacy detail through EOF"
        cleaned = secret_filter.clean_history_bytes(data)
        self.assertNotIn(b"legacy detail", cleaned)
        self.assertRegex(cleaned, rb"%%SECRET\[v2:[0-9a-f]{32}\]%%$")
        with self.assertRaises(secret_filter.SecretFilterError):
            secret_filter.clean_bytes(data, "Current.md", None)

    def test_invalid_sidecar_integrity_fails(self) -> None:
        store = self.make_directory()
        path = secret_filter.sidecar_path(store, "Example.md")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            '{"version": 2, "path": "Example.md", "entries": '
            '{"v2:00000000000000000000000000000000": '
            '{"kind": "block", "data": "YmFk"}}}\n',
            encoding="utf-8",
        )
        with self.assertRaises(secret_filter.SecretFilterError):
            secret_filter.load_sidecar(store, "Example.md")


class GitIntegrationTest(unittest.TestCase):
    def make_repo(self) -> Path:
        root = Path(tempfile.mkdtemp(prefix="secret-filter-git-test."))
        self.addCleanup(lambda: shutil.rmtree(root, ignore_errors=True))
        subprocess.run([GIT_EXECUTABLE, "init", "-q", str(root)], check=True)
        subprocess.run([GIT_EXECUTABLE, "config", "user.name", "Test User"], cwd=root, check=True)
        subprocess.run(
            [GIT_EXECUTABLE, "config", "user.email", "test@example.invalid"],
            cwd=root,
            check=True,
        )
        (root / "_scripts").mkdir()
        shutil.copy2(SCRIPT_PATH, root / "_scripts" / "secret_filter.py")
        (root / ".gitattributes").write_text("*.md filter=remove-secrets\n", encoding="utf-8")
        return root

    def configure_filter(self, root: Path) -> None:
        clean = '{} "_scripts/secret_filter.py" clean --path "%f" --store ".secrets-v2"'.format(
            sys.executable
        )
        smudge = '{} "_scripts/secret_filter.py" smudge --path "%f" --store ".secrets-v2"'.format(
            sys.executable
        )
        subprocess.run(
            [GIT_EXECUTABLE, "config", "filter.remove-secrets.clean", clean], cwd=root, check=True
        )
        subprocess.run(
            [GIT_EXECUTABLE, "config", "filter.remove-secrets.smudge", smudge], cwd=root, check=True
        )
        subprocess.run(
            [GIT_EXECUTABLE, "config", "filter.remove-secrets.required", "true"], cwd=root, check=True
        )

    def test_real_git_filter_keeps_raw_worktree_and_cleans_index(self) -> None:
        root = self.make_repo()
        self.configure_filter(root)
        note = root / "Note with spaces, 'single', \"double\", and $dollar.md"
        original = b"Public %%SECRETprivate detail%% text\n"
        note.write_bytes(original)

        subprocess.run([GIT_EXECUTABLE, "add", ".gitattributes", note.name], cwd=root, check=True)
        staged = subprocess.run(
            [GIT_EXECUTABLE, "show", ":{}".format(note.name)],
            cwd=root,
            check=True,
            stdout=subprocess.PIPE,
        ).stdout
        self.assertNotIn(b"private detail", staged)
        self.assertRegex(staged, rb"%%SECRET\[v2:[0-9a-f]{32}\]%%")
        self.assertEqual(note.read_bytes(), original)

        completed = subprocess.run(
            [sys.executable, str(root / "_scripts" / "secret_filter.py"), "check-index"],
            cwd=root,
            check=False,
        )
        self.assertEqual(completed.returncode, 0)

    def test_guard_blocks_raw_content_when_filter_is_missing(self) -> None:
        root = self.make_repo()
        note = root / "Unsafe.md"
        note.write_bytes(b"Public %%SECRETprivate detail%% text\n")
        subprocess.run([GIT_EXECUTABLE, "add", ".gitattributes", note.name], cwd=root, check=True)

        completed = subprocess.run(
            [sys.executable, str(root / "_scripts" / "secret_filter.py"), "check-index"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertEqual(completed.returncode, 1)
        self.assertIn(b"commit blocked", completed.stderr)
        self.assertNotIn(b"private detail", completed.stderr)

    def test_new_remote_branch_scans_history_already_reachable_from_origin(self) -> None:
        root = self.make_repo()
        note = root / "Unsafe.md"
        note.write_bytes(b"Public %%SECRETprivate detail%% text\n")
        subprocess.run([GIT_EXECUTABLE, "add", ".gitattributes", note.name], cwd=root, check=True)
        subprocess.run([GIT_EXECUTABLE, "commit", "-q", "-m", "unsafe history"], cwd=root, check=True)
        head = subprocess.run(
            [GIT_EXECUTABLE, "rev-parse", "HEAD"],
            cwd=root,
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        ).stdout.strip()
        subprocess.run(
            [GIT_EXECUTABLE, "update-ref", "refs/remotes/origin/main", head],
            cwd=root,
            check=True,
        )

        push_line = "refs/heads/main {} refs/heads/main {}\n".format(head, "0" * 40)
        completed = subprocess.run(
            [sys.executable, str(root / "_scripts" / "secret_filter.py"), "check-push"],
            cwd=root,
            input=push_line,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 1)
        self.assertIn("push blocked", completed.stderr)
        self.assertNotIn("private detail", completed.stderr)

    def test_required_filter_blocks_malformed_secret(self) -> None:
        root = self.make_repo()
        self.configure_filter(root)
        note = root / "Malformed.md"
        note.write_bytes(b"Public\n%%SECRET not closed\n")

        completed = subprocess.run(
            [GIT_EXECUTABLE, "add", note.name],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        self.assertNotEqual(completed.returncode, 0)
        self.assertNotIn(b"not closed", completed.stderr)


if __name__ == "__main__":
    unittest.main()

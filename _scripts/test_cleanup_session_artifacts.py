from __future__ import annotations

import argparse
from contextlib import redirect_stderr, redirect_stdout
from decimal import Decimal
import importlib.util
import io
from pathlib import Path
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("cleanup_session_artifacts.py")
SPEC = importlib.util.spec_from_file_location("cleanup_session_artifacts", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
cleanup = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = cleanup
SPEC.loader.exec_module(cleanup)


class CleanupSessionArtifactsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="session-cleanup-test-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def write(self, path: Path, text: str = "synthetic content\n") -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def bundle(self, number: str = "001", campaign: str = "folder", prefix: str = "other-name") -> Path:
        bundle = self.root / "_sessions" / campaign / f"{prefix}-{number}"
        for suffix in cleanup.REQUIRED_SUFFIXES:
            self.write(bundle / "cleaned" / f"{bundle.name}-{suffix}")
        return bundle

    def run_cli(self, *args: str) -> tuple[int, str]:
        stream = io.StringIO()
        with redirect_stdout(stream), redirect_stderr(stream):
            result = cleanup.main(args, vault_root=self.root)
        return result, stream.getvalue()

    def snapshot(self) -> dict[str, bytes]:
        return {
            str(path.relative_to(self.root)): path.read_bytes()
            for path in self.root.rglob("*") if path.is_file()
        }

    def test_session_selectors(self) -> None:
        for text, expected in (
            ("1", ["1"]), ("1,4,7", ["1", "4", "7"]),
            ("1-3", ["1", "2", "3"]), ("3,1-3,7", ["1", "2", "3", "7"]),
            ("029.1,29", ["29", "29.1"]),
        ):
            with self.subTest(text=text):
                self.assertEqual(cleanup.parse_sessions(text), tuple(map(Decimal, expected)))
        for text in ("", "1,", "3-1", "all", "1.1-2.1", "-1", "1/2"):
            with self.subTest(text=text):
                with self.assertRaises(argparse.ArgumentTypeError):
                    cleanup.parse_sessions(text)

    def test_dry_run_is_default_even_with_atypical_flag(self) -> None:
        bundle = self.bundle()
        cleaned = bundle / "cleaned"
        self.write(cleaned / f"{bundle.name}-session-summary-context.json")
        self.write(cleaned / "cleanup-artifacts" / "manual-note.md")
        before = self.snapshot()
        directories = set(self.root.rglob("*"))
        result, output = self.run_cli("folder", "1", "--include-atypical")
        self.assertEqual(result, 0, output)
        self.assertIn("DRY RUN", output)
        self.assertIn("[atypical]", output)
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(set(self.root.rglob("*")), directories)

    def test_execute_deletes_only_five_categories_and_preserves_polisher_inputs(self) -> None:
        bundle = self.bundle()
        cleaned = bundle / "cleaned"
        for suffix in cleanup.DELETE_SUFFIXES:
            self.write(cleaned / f"{bundle.name}-{suffix}")
        for suffix in cleanup.TYPICAL_ARTIFACT_SUFFIXES["cleanup-artifacts"]:
            self.write(cleaned / "cleanup-artifacts" / f"{bundle.name}-{suffix}")
        for suffix in cleanup.TYPICAL_ARTIFACT_SUFFIXES["annotation-context"]:
            self.write(cleaned / "annotation-context" / f"{bundle.name}-{suffix}")
        self.write(cleaned / "annotation-context" / "contexts" / "beat-001.md")
        self.write(cleaned / "annotation-context" / "contexts" / "B02.md")
        # Identical synthetic retained annotations; no working vault data used.
        self.write(cleaned / "annotation-artifacts" / f"{bundle.name}-beat-facts.json")
        self.write(cleaned / "annotation-artifacts" / f"{bundle.name}-beat-facts-preview.md")
        for suffix in ("speaker-stats.json", "recap-scenes.json", "session-recap-original.md"):
            self.write(cleaned / f"{bundle.name}-{suffix}")
        result, output = self.run_cli("folder", "1", "--execute")
        self.assertEqual(result, 0, output)
        expected = {f"cleaned/{bundle.name}-{suffix}" for suffix in cleanup.REQUIRED_SUFFIXES}
        expected |= {
            f"cleaned/{bundle.name}-{suffix}"
            for suffix in ("speaker-stats.json", "recap-scenes.json", "session-recap-original.md")
        }
        self.assertEqual({str(p.relative_to(bundle)) for p in bundle.rglob("*") if p.is_file()}, expected)
        for directory in cleanup.ARTIFACT_DIRS:
            self.assertFalse((cleaned / directory).exists())
        # No polished transcripts exist, but their two required inputs survive.
        self.assertFalse((cleaned / "beat-transcripts").exists())
        self.assertTrue((cleaned / f"{bundle.name}-source-cleaned.md").is_file())
        self.assertTrue((cleaned / f"{bundle.name}-session-recap.md").is_file())

    def test_atypical_scope_and_empty_folder_behavior(self) -> None:
        bundle = self.bundle()
        cleaned = bundle / "cleaned"
        root_note = self.write(cleaned / "personal-glossary.md")
        polished = self.write(cleaned / "beat-transcripts" / "custom.md")
        atypical = []
        for directory in cleanup.ARTIFACT_DIRS:
            atypical.append(self.write(cleaned / directory / "nested" / "notes.md"))
        self.write(cleaned / "cleanup-artifacts" / f"{bundle.name}-cleanup-report.json")
        result, output = self.run_cli("folder", "1", "--execute")
        self.assertEqual(result, 0, output)
        self.assertIn("ATYPICAL (kept)", output)
        self.assertTrue(all(path.exists() for path in atypical))
        result, output = self.run_cli("folder", "1", "--execute", "--include-atypical")
        self.assertEqual(result, 0, output)
        self.assertTrue(root_note.exists())
        self.assertTrue(polished.exists())
        self.assertTrue(all(not path.exists() for path in atypical))
        self.assertTrue(all(not (cleaned / name).exists() for name in cleanup.ARTIFACT_DIRS))

    def test_missing_or_empty_recap_always_refuses(self) -> None:
        for content in (None, ""):
            with self.subTest(content=content):
                bundle = self.bundle()
                cleaned = bundle / "cleaned"
                recap = cleaned / f"{bundle.name}-session-recap.md"
                if content is None:
                    recap.unlink()
                else:
                    recap.write_text(content)
                self.write(cleaned / "cleanup-artifacts" / "notes.md")
                self.write(cleaned / ".DS_Store")
                self.write(cleaned / f"{bundle.name}-session-summary-context.json")
                before = self.snapshot()
                result, output = self.run_cli("folder", "1", "--execute", "--include-atypical")
                self.assertEqual(result, 1)
                self.assertIn("SKIPPED", output)
                self.assertIn("session-recap.md", output)
                self.assertEqual(self.snapshot(), before)

    def test_missing_retained_file_skips_only_that_bundle(self) -> None:
        first = self.bundle("001")
        second = self.bundle("002")
        (first / "cleaned" / f"{first.name}-source-cleaned.md").unlink()
        for bundle in (first, second):
            self.write(bundle / "cleaned" / f"{bundle.name}-session-summary-context.json")
        result, output = self.run_cli("folder", "1-2", "--execute")
        self.assertEqual(result, 1, output)
        self.assertTrue((first / "cleaned" / f"{first.name}-session-summary-context.json").exists())
        self.assertFalse((second / "cleaned" / f"{second.name}-session-summary-context.json").exists())

    def test_differing_annotation_copy_is_kept_even_with_extra_flag(self) -> None:
        bundle = self.bundle()
        copy = self.write(bundle / "cleaned" / "annotation-artifacts" / f"{bundle.name}-beat-facts.json", "unique annotation\n")
        result, output = self.run_cli("folder", "1", "--execute", "--include-atypical")
        self.assertEqual(result, 0, output)
        self.assertTrue(copy.exists())
        self.assertIn("no byte-identical retained", output)

    def test_finder_metadata_is_typical_and_does_not_keep_artifact_folders(self) -> None:
        bundle = self.bundle()
        cleaned = bundle / "cleaned"
        self.write(cleaned / ".DS_Store")
        for directory in cleanup.ARTIFACT_DIRS:
            self.write(cleaned / directory / ".DS_Store")
        self.write(cleaned / "annotation-context" / "contexts" / ".DS_Store")
        self.write(cleaned / "cleanup-artifacts" / "old-folder" / ".DS_Store")
        before = self.snapshot()
        result, output = self.run_cli("folder", "1")
        self.assertEqual(result, 0, output)
        self.assertIn("WOULD DELETE", output)
        self.assertIn("WOULD REMOVE EMPTY DIR", output)
        self.assertNotIn("ATYPICAL", output)
        self.assertEqual(self.snapshot(), before)
        result, output = self.run_cli("folder", "1", "--execute")
        self.assertEqual(result, 0, output)
        self.assertFalse((cleaned / ".DS_Store").exists())
        for directory in cleanup.ARTIFACT_DIRS:
            self.assertFalse((cleaned / directory).exists())

    def test_finder_metadata_cleanup_preserves_other_contents_directories_and_links(self) -> None:
        bundle = self.bundle()
        cleaned = bundle / "cleaned"
        metadata = [
            self.write(cleaned / "beat-transcripts" / ".DS_Store"),
            self.write(cleaned / "custom-folder" / "nested" / ".DS_Store"),
            self.write(cleaned / "cleanup-artifacts" / "custom-folder" / ".DS_Store"),
        ]
        polished = self.write(cleaned / "beat-transcripts" / "polished.md")
        notes = self.write(cleaned / "cleanup-artifacts" / "custom-folder" / "review.md")
        source_metadata = self.write(bundle / "sources" / ".DS_Store")
        outside_metadata = self.write(self.root / "external" / ".DS_Store")
        linked_dir = cleaned / "external"
        linked_dir.symlink_to(outside_metadata.parent, target_is_directory=True)
        linked_metadata = cleaned / "supplemental" / ".DS_Store"
        linked_metadata.parent.mkdir()
        linked_metadata.symlink_to(outside_metadata)
        result, output = self.run_cli("folder", "1", "--execute")
        self.assertEqual(result, 0, output)
        self.assertTrue(all(not path.exists() for path in metadata))
        self.assertTrue(polished.exists())
        self.assertTrue(notes.exists())
        self.assertTrue(source_metadata.exists())
        self.assertTrue(outside_metadata.exists())
        self.assertTrue(linked_metadata.is_symlink())
        self.assertTrue((cleaned / "custom-folder" / "nested").is_dir())

    def test_file_and_directory_symlinks_are_kept_and_not_followed(self) -> None:
        bundle = self.bundle()
        cleaned = bundle / "cleaned"
        outside = self.write(self.root / "outside" / "important.md")
        artifacts = cleaned / "cleanup-artifacts"
        artifacts.mkdir()
        link = artifacts / f"{bundle.name}-cleanup-report.json"
        link.symlink_to(outside)
        directory_link = artifacts / "external"
        directory_link.symlink_to(outside.parent, target_is_directory=True)
        root_link = cleaned / "annotation-context"
        root_link.symlink_to(outside.parent, target_is_directory=True)
        result, output = self.run_cli("folder", "1", "--execute", "--include-atypical")
        self.assertEqual(result, 0, output)
        self.assertTrue(link.is_symlink())
        self.assertTrue(directory_link.is_symlink())
        self.assertTrue(root_link.is_symlink())
        self.assertEqual(outside.read_text(), "synthetic content\n")
        self.assertIn("PROTECTED", output)

    def test_execution_rechecks_recap_and_changed_files_before_any_deletion(self) -> None:
        bundle = self.bundle()
        cleaned = bundle / "cleaned"
        first = self.write(cleaned / f"{bundle.name}-beats-preview.md")
        second = self.write(cleaned / f"{bundle.name}-session-summary-context.json")
        plan = cleanup.build_plan(bundle)
        second.write_text("changed after planning\n")
        with self.assertRaises(cleanup.CleanupError):
            cleanup.execute_plan(plan)
        self.assertTrue(first.exists())
        plan = cleanup.build_plan(bundle)
        (cleaned / f"{bundle.name}-session-recap.md").unlink()
        with self.assertRaises(cleanup.CleanupError):
            cleanup.execute_plan(plan)
        self.assertTrue(first.exists())
        self.assertTrue(second.exists())

    def test_missing_ambiguous_and_fractional_session_selection(self) -> None:
        self.bundle("029.1", campaign="short-folder", prefix="different-long-prefix")
        result, output = self.run_cli("short-folder", "29.1")
        self.assertEqual(result, 0, output)
        result, output = self.run_cli("short-folder", "29")
        self.assertEqual(result, 1)
        self.assertIn("no matching bundle", output)
        self.bundle("029.1", campaign="short-folder", prefix="duplicate")
        result, output = self.run_cli("short-folder", "29.1", "--execute")
        self.assertEqual(result, 1)
        self.assertIn("ambiguous", output)

    def test_campaign_path_traversal_is_refused(self) -> None:
        self.bundle()
        before = self.snapshot()
        result, output = self.run_cli("../folder", "1", "--execute")
        self.assertEqual(result, 1)
        self.assertIn("REFUSED", output)
        self.assertEqual(self.snapshot(), before)


if __name__ == "__main__":
    unittest.main()

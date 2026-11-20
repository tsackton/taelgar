import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from session_bundles import bundle_parts, select_bundle, session_manifest


class BundleSelectionTest(unittest.TestCase):
    def setUp(self):
        workspace = tempfile.TemporaryDirectory()
        self.addCleanup(workspace.cleanup)
        self.root = Path(workspace.name)

    def test_first_prefix_then_reuse(self):
        with self.assertRaisesRegex(ValueError, "--prefix"):
            select_bundle(self.root, "0", create=True)
        with patch("builtins.input", return_value="green-sea"):
            first = select_bundle(self.root, "0", create=True, prompt=True)
        self.assertEqual(first.name, "green-sea-000")
        self.assertFalse(first.exists())
        first.mkdir()
        for number, expected in [("0.5", "000.5"), ("12.10", "012.10"), ("1000", "1000")]:
            path = select_bundle(self.root, number, create=True)
            self.assertEqual(path.name, "green-sea-" + expected)
            self.assertEqual(bundle_parts(path)[1], number)

    def test_mixed_prefixes_and_duplicate_number(self):
        (self.root / "greensea-001").mkdir()
        other = self.root / "green-sea-002"
        other.mkdir()
        self.assertEqual(select_bundle(self.root, "2", create=True), other)
        self.assertIsNone(session_manifest(other, required=False))
        with self.assertRaisesRegex(ValueError, "Existing prefixes"):
            select_bundle(self.root, "3", create=True)
        self.assertEqual(select_bundle(self.root, "3", create=True, prefix="greensea").name, "greensea-003")
        (self.root / "greensea-002").mkdir()
        with self.assertRaisesRegex(ValueError, "Several bundles"):
            select_bundle(self.root, "002")

    def test_unpadded_directory_and_ambiguous_manifests(self):
        (self.root / "green-sea-12").mkdir()
        with self.assertRaisesRegex(ValueError, "Invalid numbered bundle"):
            select_bundle(self.root, "12", create=True, prefix="green-sea")
        bundle = self.root / "green-sea-011"
        cleaned = bundle / "cleaned"
        cleaned.mkdir(parents=True)
        for name in ["a-session.yaml", "b-session.yaml"]:
            (cleaned / name).touch()
        with self.assertRaisesRegex(ValueError, "Multiple session manifests"):
            session_manifest(bundle)


if __name__ == "__main__":
    unittest.main()

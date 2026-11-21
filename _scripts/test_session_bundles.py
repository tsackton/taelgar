import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from session_bundles import bundle_parts, select_bundle, session_identity, session_manifest


class BundleSelectionTest(unittest.TestCase):
    def setUp(self):
        workspace = tempfile.TemporaryDirectory()
        self.addCleanup(workspace.cleanup)
        self.root = Path(workspace.name)

    def test_path_identity_keeps_fractions_and_ignores_yaml_labels(self):
        vault = self.root.resolve()
        campaign_directory = vault / "_sessions/cleenseau"
        campaign_directory.mkdir(parents=True)
        (vault / "_sessions/campaign-registry.json").write_text('{"clee":"Index.md"}')
        (vault / "Index.md").write_text(
            "---\nname: Cleenseau\nsessionBundleDirectory: _sessions/cleenseau\n---\n"
        )
        manifest = campaign_directory / "cleenseau-012.10/cleaned/historical-session.yaml"
        old = {"campaign": "dufr", "sessionNumber": 99}
        self.assertEqual(session_identity(manifest, old), ("clee", "12.10"))
        self.assertEqual(session_identity(manifest, {}), ("clee", "12.10"))
        self.assertEqual(old, {"campaign": "dufr", "sessionNumber": 99})
        loose = vault / "_sessions/to-process/unprepared-session.yaml"
        self.assertEqual(session_identity(loose, old), ("dufr", 99))

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

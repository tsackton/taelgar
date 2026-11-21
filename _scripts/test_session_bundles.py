import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from session_bundles import (
    bundle_parts, numbered_bundles, registered_bundle_identity, resolve_bundle,
    select_bundle, session_identity, session_manifest,
)


class BundleSelectionTest(unittest.TestCase):
    def setUp(self):
        workspace = tempfile.TemporaryDirectory()
        self.addCleanup(workspace.cleanup)
        self.root = Path(workspace.name)

    def test_manifest_identity_requires_registration_and_preserves_fractions(self):
        vault = self.root.resolve()
        campaign_directory = vault / "_sessions/cleenseau"
        campaign_directory.mkdir(parents=True)
        (vault / "_sessions/campaign-registry.json").write_text('{"clee":"Index.md"}')
        (vault / "Index.md").write_text(
            "---\nname: Cleenseau\nsessionBundleDirectory: _sessions/cleenseau\n---\n"
        )
        manifest = campaign_directory / "cleenseau-012.10/cleaned/historical-session.yaml"
        manifest.parent.mkdir(parents=True)
        manifest.write_text("campaign: dufr\nsessionNumber: 99\n")
        self.assertEqual(session_identity(manifest), ("clee", "12.10"))
        config = manifest.with_name("source-prep.yaml")
        config.write_text(manifest.read_text())
        with self.assertRaisesRegex(ValueError, "Select the registered bundle manifest"):
            session_identity(config)
        extra = manifest.with_name("backup-session.yaml")
        extra.write_text(manifest.read_text())
        with self.assertRaisesRegex(ValueError, "Multiple session manifests"):
            session_identity(manifest)
        extra.unlink()
        loose = vault / "_sessions/to-process/cleenseau-012.10/cleaned/loose-session.yaml"
        loose.parent.mkdir(parents=True)
        loose.write_text(manifest.read_text())
        with self.assertRaisesRegex(ValueError, "manifest in a registered numbered bundle"):
            session_identity(loose)

        point = campaign_directory / "cleenseau-012.1"
        point.mkdir()
        self.assertEqual(resolve_bundle(vault, "clee", "012.1"), point)
        duplicate = campaign_directory / "other-012.10"
        duplicate.mkdir()
        for lookup in (
            lambda: resolve_bundle(vault, "clee", "12.10"),
            lambda: session_identity(manifest),
            lambda: registered_bundle_identity(duplicate),
            lambda: list(numbered_bundles(campaign_directory)),
        ):
            with self.assertRaisesRegex(ValueError, r"Several bundles for session 12\.10:.*cleenseau-012\.10.*other-012\.10"):
                lookup()

        self.assertEqual(resolve_bundle(vault, "clee", "12.1"), point)

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

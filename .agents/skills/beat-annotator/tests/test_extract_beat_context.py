import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "extract_beat_context.py"


class BeatContextIdentityTest(unittest.TestCase):
    def test_context_uses_registered_identity_and_rejects_a_loose_manifest(self):
        with tempfile.TemporaryDirectory() as temp:
            vault = Path(temp).resolve()
            campaign_root = vault / "_sessions" / "cleenseau"
            cleaned = campaign_root / "cleenseau-012.10" / "cleaned"
            cleaned.mkdir(parents=True)
            (campaign_root.parent / "campaign-registry.json").write_text('{"clee":"Index.md"}')
            (vault / "Index.md").write_text(
                "---\nname: Cleenseau\nsessionBundleDirectory: _sessions/cleenseau\n---\n"
            )
            manifest = cleaned / "historical-session.yaml"
            manifest.write_text("campaign: legacy\nsessionNumber: 42\n")
            transcript = cleaned / "source-cleaned.md"
            transcript.write_text("[u0001] The party arrives.\n")
            beats = cleaned / "beats.json"
            beats.write_text(json.dumps({"beats": [{
                "beatId": "b01", "title": "Arrival", "startUid": "u0001", "endUid": "u0001",
                "boundaryReason": "Start of the session",
            }]}))
            output = cleaned / "annotation-context"
            command = [sys.executable, "-B", str(SCRIPT), "--transcript", str(transcript),
                       "--beats-json", str(beats), "--output-dir", str(output), "--file-prefix", "historical"]
            loose = vault / "loose-session.yaml"
            loose.write_bytes(manifest.read_bytes())
            failure = subprocess.run([*command, "--session", str(loose)], capture_output=True, text=True)
            self.assertEqual(failure.returncode, 1)
            self.assertIn("manifest in a registered numbered bundle", failure.stderr)
            self.assertFalse(output.exists())

            result = subprocess.run([*command, "--session", str(manifest)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            contexts = json.loads((output / "historical-beat-contexts.json").read_text())
            session = contexts["contexts"][0]["session"]
            self.assertEqual(session["campaign"], "clee")
            self.assertEqual(session["sessionNumber"], "12.10")

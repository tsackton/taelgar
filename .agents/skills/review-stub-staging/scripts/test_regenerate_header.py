from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from regenerate_header import apply_preview


class NativeHeaderTests(unittest.TestCase):
    root = Path(__file__).resolve().parents[4]
    relative_tool = Path(".obsidian/plugins/taelgarverse/header-tool.cjs")

    def test_preview_uses_utf16_ranges_and_preserves_other_bytes(self):
        prefix = "---\r\nname: Test \U0001f98a\r\n---\r\n"
        before = "# Original\r\n"
        suffix = "\r\nAuthored body.\r\n"
        replacement = "# Updated\r\n> [!taelgar-header]\r\n"
        start = len(prefix.encode("utf-16-le")) // 2
        end = start + len(before.encode("utf-16-le")) // 2
        plan = dict(start=start, end=end, before=before, replacement=replacement)
        original = (prefix + before + suffix).encode("utf-8")
        self.assertEqual(apply_preview(original, plan), (prefix + replacement + suffix).encode("utf-8"))
        with self.assertRaisesRegex(ValueError, "does not match"):
            apply_preview(original, {**plan, "before": "Other"})

    def test_native_preview_and_approved_write_preserve_body(self):
        tool = self.root / self.relative_tool
        if not tool.is_file():
            self.skipTest("Taelgarverse is not installed in the test vault")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            test_tool = root / self.relative_tool
            test_tool.parent.mkdir(parents=True)
            shutil.copyfile(tool, test_tool)
            note = root / "Fixture Person.md"
            body = b"\n%% private guidance %%\n![[portrait.png]]\nArticle.\n"
            original = (b"---\nheaderVersion: old\nname: Fixture Person\n"
                        b"tags: [person]\npronunciation: FIX-cher\n---\n"
                        b"# Fixture Person\n> [!taelgar-header]\n" + body)
            note.write_bytes(original)
            command = [sys.executable, str(Path(__file__).with_name("regenerate_header.py")),
                       str(note), "--root", str(root)]
            result = subprocess.run(command, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr.decode('utf-8'))
            preview = result.stdout
            self.assertIn(b"*(FIX-cher)*", preview)
            self.assertIn(b"> [!taelgar-header]", preview)
            self.assertNotIn(b"headerVersion", preview)
            self.assertTrue(preview.endswith(body))
            self.assertEqual(note.read_bytes(), original)
            subprocess.run([*command, "--write"], check=True, capture_output=True)
            self.assertEqual(note.read_bytes(), preview)
            self.assertEqual(subprocess.check_output(command), preview)


if __name__ == '__main__':
    unittest.main()

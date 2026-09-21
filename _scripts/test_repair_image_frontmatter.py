import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import repair_image_frontmatter as repair


class ImageFrontmatterTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.vault = self.root / "vault"
        (self.vault / "assets").mkdir(parents=True)

    def put(self, name, text="image fixture"):
        path = self.vault / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(text.encode("utf8"))
        return path

    def note(self, name="People/Person.md", value="portrait.png", tags="tags: [person]\n", body="Body ![[portrait.png]]\n"):
        return self.put(name, f"---\nheaderVersion: 2023.11.25\n{tags}image: {value}\nname: Person\n---\n{body}")

    def scan(self, **kwargs):
        return repair.scan(self.vault, **kwargs)

    def apply(self, plan):
        return repair.apply_plan(plan, self.root / "receipt.json")

    def test_preview_apply_idempotence_and_preservation(self):
        image = self.put("assets/nested/portrait.png")
        path = self.note(value='"portrait.png" # keep this comment', tags="tags: [person, status/stub, status/check/lint]\n")
        original = path.read_bytes()
        report = self.scan()
        self.assertEqual(len(report["changes"]), 1)
        self.assertEqual(path.read_bytes(), original)
        self.assertEqual(report, self.scan())
        state = self.apply(report)
        self.assertEqual(state["status"], "verified")
        after = path.read_text()
        self.assertIn('image: "[[portrait.png]]" # keep this comment', after)
        self.assertIn("tags: [person, status/stub, status/check/lint]", after)
        self.assertNotIn("status/check/ai", after)
        self.assertEqual(after.encode(), original.replace(b'"portrait.png"', b'"[[portrait.png]]"'))
        self.assertTrue(after.endswith("Body ![[portrait.png]]\n"))
        self.assertEqual(image.read_text(), "image fixture")
        self.assertEqual(self.scan()["changes"], [])
        self.assertEqual(state["backups"]["People/Person.md"].encode(), original)

    def test_existing_links_empty_and_external_are_unchanged(self):
        self.put("assets/portrait.png")
        self.note("A.md", '"[[portrait.png|Portrait]]"')
        self.note("B.md", "")
        self.note("C.md", '"   "')
        self.note("D.md", "https://example.test/portrait.png")
        self.note("E.md", '"![[portrait.png|400]]"')
        result = self.scan()
        self.assertFalse(result["changes"])
        self.assertEqual(result["summary"], {"empty": 2, "external": 1, "valid": 2})

    def test_every_image_directory_is_searchable_including_excluded_move_folders(self):
        for n, folder in enumerate(("assets/_incoming", "assets/pc_references", "assets/campaign/deep", "_DM_/maps")):
            self.put(f"{folder}/p{n}.png")
            self.note(f"N{n}.md", f"p{n}.png")
        self.assertEqual(len(self.scan()["changes"]), 4)

    def test_paths_unicode_encoded_names_and_non_image_files(self):
        self.put("assets/maps/Café Scene.png")
        self.note("Places/A.md", '"../assets/maps/Café%20Scene.png"')
        self.note("B.md", "maps/Café Scene.png")
        self.note("C.md", "assets/old/Café Scene.png")
        self.note("D.md", "missing.jpy")
        self.put("assets/document.pdf")
        self.note("E.md", "document.pdf")
        self.note("F.md", '"[[document.pdf]]"')
        result = self.scan()
        self.assertEqual(len(result["changes"]), 2)
        self.assertEqual(result["summary"], {"missing": 2, "not-image": 2, "valid": 2})
        self.assertTrue(all(c["after"] == "[[Café Scene.png]]" for c in result["changes"]))

    def test_duplicate_basenames_and_extensionless_note_collision_are_held(self):
        self.put("assets/a/p.png")
        self.put("assets/b/p.png")
        self.put("People/p.md", "A note.")
        self.note("A.md", "p.png")
        self.note("B.md", '"[[p]]"')
        self.note("C.md", "assets/a/p.png")
        result = self.scan()
        self.assertEqual(result["summary"], {"ambiguous": 2, "valid": 1})
        self.assertEqual(result["changes"][0]["after"], "[[assets/a/p.png]]")

    def test_missing_properties_suggest_embedded_image_first_without_choosing(self):
        self.put("assets/something-different.png")
        self.put("assets/old.jpg")
        path = self.note(value="old.png", body="![[something-different.png|400]]\n")
        result = self.scan()
        self.assertFalse(result["changes"])
        row = result["entries"][0]
        self.assertEqual(row["suggestions"][0], {"image": "assets/something-different.png", "reason": "embedded-in-note"})
        self.assertEqual(path.read_text().split("image: ")[1].splitlines()[0], "old.png")

    def test_explicit_choice_preserves_alias_and_changes_only_selected_note(self):
        self.put("assets/one/p.png")
        self.put("assets/two/p.png")
        self.note("A.md", '"[[missing.jpg|320]]"')
        other = self.note("B.md", "p.png")
        before = other.read_bytes()
        plan = self.scan(notes=["A.md"], replacements={"A.md": "assets/one/p.png"})
        self.assertEqual(plan["changes"][0]["after"], "[[assets/one/p.png|320]]")
        self.apply(plan)
        self.assertEqual(other.read_bytes(), before)
        self.assertEqual(self.scan(notes=["A.md"])["summary"], {"valid": 1})

    def test_unknown_note_invalid_choice_and_empty_field_are_not_applied(self):
        self.note("A.md", "missing.png")
        with self.assertRaisesRegex(ValueError, "without an image property"):
            self.scan(replacements={"Unknown.md": "assets/p.png"})
        for choice in ("assets/missing.png", "../outside.png"):
            result = self.scan(replacements={"A.md": choice})
            self.assertFalse(result["changes"])
            self.assertEqual(result["summary"], {"manual-review": 1})
        self.put("assets/p.png")
        self.note("B.md", "")
        self.assertFalse(self.scan(notes=["B.md"], replacements={"B.md": "assets/p.png"})["changes"])

    def test_tags_are_preserved_exactly_in_every_format_and_directory(self):
        self.put("assets/portrait.png")
        originals = {}
        for name, tags in [("A.md", "tags:\n  - person # preserve\n  - status/stub\n"),
                           ("B.md", "tags: person # preserve\n"), ("C.md", ""),
                           ("D.md", "tags: [person, status/check/ai]\n"),
                           ("E.md", "tags:\n"), ("_sessions/test.md", "tags: [session]\n"),
                           ("_DM_/test.md", "tags: [meta]\n")]:
            originals[name] = self.note(name, tags=tags).read_bytes()
        plan = self.scan()
        self.assertEqual(len(plan["changes"]), 7)
        self.apply(plan)
        for name, before in originals.items():
            self.assertEqual((self.vault / name).read_bytes(), before.replace(b'image: portrait.png', b'image: "[[portrait.png]]"'))

    def test_crlf_bom_comments_and_single_quotes_are_preserved(self):
        self.put("assets/portrait.png")
        old = "\ufeff---\r\ntags: [person]\r\nimage: 'portrait.png' # keep\r\nname: Person\r\n---\r\nBody\r\n"
        path = self.put("A.md", old)
        self.apply(self.scan())
        expected = old.replace("'portrait.png'", '"[[portrait.png]]"')
        self.assertEqual(path.read_bytes(), expected.encode())

    def test_malformed_duplicate_anchored_and_structured_yaml_needs_review(self):
        self.put("assets/portrait.png")
        for name, header in [("A.md", "image: [broken"), ("B.md", "image: portrait.png\nimage: portrait.png"),
                             ("C.md", "image: &ref portrait.png\nother: *ref"), ("D.md", "image: [[portrait.png]]"),
                             ("E.md", "image: |\n  portrait.png"), ("F.md", "image: 2026-09-19")]:
            self.put(name, "---\n" + header + "\n---\nBody")
        plan = self.scan()
        self.assertFalse(plan["changes"])
        self.assertEqual(plan["summary"], {"manual-review": 6})
        json.dumps(plan)

    def test_recap_body_leaflet_and_other_metadata_are_out_of_scope(self):
        path = self.put("_sessions/A.md", "---\nname: Session\n---\n- Image: missing.png\n```leaflet\nimage: [[map.png]]\n```\n")
        before = path.read_bytes()
        self.assertFalse(self.scan()["entries"])
        self.assertEqual(before, path.read_bytes())

    def test_subset_apply_and_stale_or_tampered_plans(self):
        self.put("assets/portrait.png")
        a = self.note("A.md")
        b = self.note("B.md")
        report = self.scan()
        for mutate in (lambda p: p["changes"][0].update(after="[[else.png]]"),
                       lambda p: p["changes"].append(p["changes"][0])):
            plan = copy.deepcopy(report)
            mutate(plan)
            with self.assertRaises(ValueError):
                self.apply(plan)
        a.write_text(a.read_text() + "User edit\n")
        with self.assertRaisesRegex(ValueError, "Stale"):
            self.apply(report)
        plan = self.scan()
        plan["changes"] = [c for c in plan["changes"] if c["note"] == "A.md"]
        original_b = b.read_bytes()
        self.apply(plan)
        self.assertEqual(b.read_bytes(), original_b)
        self.assertIn("User edit", a.read_text())

    def test_renamed_image_and_new_ambiguity_invalidate_plan(self):
        target = self.put("assets/portrait.png")
        self.note()
        plan = self.scan()
        self.put("assets/other/portrait.png")
        with self.assertRaisesRegex(ValueError, "Stale"):
            self.apply(plan)
        target.unlink()
        (self.vault / "assets/other/portrait.png").unlink()
        with self.assertRaisesRegex(ValueError, "Stale"):
            self.apply(plan)

    def test_failure_rolls_back_and_preserves_backups(self):
        self.put("assets/portrait.png")
        a, b = self.note("A.md"), self.note("B.md")
        originals = (a.read_bytes(), b.read_bytes())
        real_write = repair.atomic_write
        def fail_second(path, data, expected):
            if path.name == "B.md":
                raise OSError("simulated write failure")
            return real_write(path, data, expected)
        with patch.object(repair, "atomic_write", side_effect=fail_second), self.assertRaises(OSError):
            self.apply(self.scan())
        self.assertEqual((a.read_bytes(), b.read_bytes()), originals)
        self.assertEqual(json.loads((self.root / "receipt.json").read_text())["status"], "rolled-back")

    def test_concurrent_edit_is_never_overwritten_by_rollback(self):
        self.put("assets/portrait.png")
        a, b = self.note("A.md"), self.note("B.md")
        real_write = repair.atomic_write
        def fail_second(path, data, expected):
            if path.name == "B.md":
                a.write_text("User concurrently changed A\n")
                raise OSError("simulated failure")
            return real_write(path, data, expected)
        with patch.object(repair, "atomic_write", side_effect=fail_second), self.assertRaises(OSError):
            self.apply(self.scan())
        self.assertEqual(a.read_text(), "User concurrently changed A\n")
        self.assertEqual(json.loads((self.root / "receipt.json").read_text())["status"], "recovery-required")

    def test_target_disappearing_during_apply_rolls_back(self):
        target = self.put("assets/portrait.png")
        path = self.note()
        before = path.read_bytes()
        real_write = repair.atomic_write
        def remove_image_after_write(path, data, expected):
            real_write(path, data, expected)
            target.unlink(missing_ok=True)
        with patch.object(repair, "atomic_write", side_effect=remove_image_after_write), self.assertRaisesRegex(ValueError, "resolution changed"):
            self.apply(self.scan())
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(json.loads((self.root / "receipt.json").read_text())["status"], "rolled-back")

    def test_header_change_during_scan_cannot_propose_old_image(self):
        self.put("assets/portrait.png")
        path = self.note()
        original_header = repair.note_header
        def read_then_change(note):
            header = original_header(note)
            path.write_text(path.read_text().replace("image: portrait.png", "image: new-choice.png"))
            return header
        with patch.object(repair, "note_header", side_effect=read_then_change):
            plan = self.scan()
        self.assertFalse(plan["changes"])
        self.assertEqual(plan["summary"], {"manual-review": 1})

    def test_symlinks_path_escape_and_receipt_overwrite_rejected(self):
        outside = self.root / "outside.md"
        outside.write_text("Outside")
        (self.vault / "Link.md").symlink_to(outside)
        for note in ("Link.md", "../outside.md"):
            with self.assertRaises(ValueError):
                self.scan(notes=[note])
        self.put("assets/portrait.png")
        path = self.note()
        report = self.scan()
        with self.assertRaisesRegex(ValueError, "outside"):
            repair.apply_plan(report, self.vault / "receipt.json")
        (self.root / "receipt.json").write_text("existing")
        before = path.read_bytes()
        with self.assertRaises(FileExistsError):
            self.apply(report)
        self.assertEqual(before, path.read_bytes())

    def test_cli_check_is_read_only_and_reports_replacements(self):
        self.put("assets/portrait.png")
        path = self.note(value="old.png")
        before = path.read_bytes()
        choices = self.root / "choices.json"
        choices.write_text(json.dumps({"People/Person.md": "assets/portrait.png"}))
        output = self.root / "review.json"
        subprocess.run([sys.executable, "-B", repair.__file__, "--vault", str(self.vault), "--replacements", str(choices),
                        "--output", str(output)], check=True, capture_output=True)
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(json.loads(output.read_text())["changes"][0]["kind"], "replace")


if __name__ == "__main__":
    unittest.main()

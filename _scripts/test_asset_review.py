import copy
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import find_misplaced_images as finder
import move_assets as mover


class AssetReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name).resolve()
        self.vault = self.home / "vault"
        (self.vault / "assets").mkdir(parents=True)

    def put(self, relative, text="fixture bytes"):
        path = self.vault / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def scan(self, **kwargs):
        return finder.scan(self.vault, **kwargs)

    def proposed(self, plan):
        return {m["source"]: m["destination"] for m in plan["moves"]}

    def test_recursive_classification_regular_precedence_and_recovery_from_buckets(self):
        self.put("assets/maps/scene.png")
        self.put("assets/dm/shared.png")
        self.put("assets/campaign/draft.png")
        self.put("assets/worldbuilding/private.png")
        self.put("assets/_unlinked/rediscovered.png")
        self.put("Campaigns/Test/Test.md", "![[scene.png]]\n![[rediscovered.png]]")
        self.put("Campaigns/Test/Items/Object.md", "![[shared.png]]")
        self.put("_DM_/Private.md", "![[shared.png]]\n![[private.png]]")
        self.put("Worldbuilding/Chats/Chat.md", "![[draft.png]]")
        self.assertEqual(self.proposed(self.scan()), {
            "assets/maps/scene.png": "assets/campaign/scene.png",
            "assets/dm/shared.png": "assets/shared.png",
            "assets/campaign/draft.png": "assets/worldbuilding/draft.png",
            "assets/worldbuilding/private.png": "assets/dm/private.png",
            "assets/_unlinked/rediscovered.png": "assets/campaign/rediscovered.png",
        })

    def test_audio_and_unlinked_nested_images_and_excluded_folders(self):
        self.put("assets/nested/orphan.png")
        self.put("assets/audio/orphan.mp3")
        self.put("assets/_incoming/incoming.png")
        self.put("assets/pc_references/pc.png")
        self.put("assets/campaign/already.png")
        self.put("assets/pc_references/source.md", "![[already.png]]")
        plan = self.scan()
        self.assertEqual(set(self.proposed(plan)), {"assets/nested/orphan.png", "assets/audio/orphan.mp3"})
        self.assertEqual(plan["summary"]["excluded"], 2)
        self.assertEqual(len(self.scan(media="images")["moves"]), 1)
        self.assertEqual(len(self.scan(media="audio")["moves"]), 1)

    def test_session_tags_recap_fields_and_generated_components_are_campaign(self):
        for name in ("tagged.png", "recap.png", "generated.png", "short.png"):
            self.put("assets/old/" + name)
        self.put("Campaigns/Test/Session.md", '---\ntags:\n  - "session-note"\n---\n![[tagged.png]]')
        self.put("_sessions/test/cleaned/recap.md", "- Image: recap.png\n- Image 2: ![[short.png|400]]")
        self.put("Campaigns/Test/_generated/session-notes/1.md", "![[generated.png]]")
        self.assertEqual({m["category"] for m in self.scan()["moves"]}, {"campaign"})
        self.assertEqual(len(self.scan()["moves"]), 4)

    def test_mixed_special_uses_leave_private_folder_for_regular_root(self):
        self.put("assets/dm/mixed.png")
        self.put("_sessions/recap.md", "- Image: mixed.png")
        self.put("Worldbuilding/Idea.md", "![[mixed.png]]")
        self.assertEqual(self.proposed(self.scan()), {"assets/dm/mixed.png": "assets/mixed.png"})

    def test_correct_subfolders_and_regular_specialty_folders_stay(self):
        self.put("assets/campaign/test/scene.png")
        self.put("assets/maps/atlas.png")
        self.put("_sessions/recap.md", "- Image: scene.png")
        self.put("Places/Atlas.md", "![[atlas.png]]")
        self.assertEqual(self.scan()["moves"], [])

    def test_paths_code_mentions_drawings_and_collisions_are_held(self):
        for name in ("path.png", "code.png", "mention.png", "drawing.png", "duplicate.png", "relative.png", "definition.png"):
            self.put("assets/" + name)
        self.put("assets/other/duplicate.png")
        self.put("_sessions/recap.md", "![[assets/path.png]]\n- Image: code.png\n- Image: mention.png\n![[drawing.png]]\n![[duplicate.png]]\n![image](relative.png)\n[image]: definition.png")
        self.put("_scripts/example.py", 'image = "code.png"\n')
        self.put("_dm_notes/Review.md", "Consider mention.png later")
        self.put("assets/drawing-details.md", "---\nexcalidraw-plugin: parsed\n---\n")
        plan = self.scan()
        self.assertFalse(plan["moves"])
        held = {m["source"]: m["blockers"] for m in plan["held"]}
        self.assertIn("path-dependent-or-ambiguous-reference", held["assets/path.png"])
        self.assertIn("unparsed-filename-mention", held["assets/code.png"])
        self.assertIn("editable-drawing-relationship", held["assets/drawing.png"])
        self.assertIn("duplicate-filename", held["assets/duplicate.png"])
        self.assertIn("path-dependent-or-ambiguous-reference", held["assets/definition.png"])

    def test_url_encoded_unicode_and_extensionless_wikilinks(self):
        self.put("assets/old/Café Scene.png")
        self.put("assets/old/short.png")
        self.put("_sessions/recap.md", "![[Cafe\u0301%20Scene.png|400]]\n![[short]]")
        self.assertEqual(len(self.scan()["moves"]), 2)

    def test_external_urls_do_not_count_as_local_links(self):
        self.put("assets/remote.png")
        self.put("Places/Note.md", "![remote](https://example.test/remote.png)")
        self.assertEqual(self.scan()["moves"][0]["category"], "unlinked")

    def test_note_links_do_not_link_same_stem_images(self):
        self.put("assets/_unlinked/Person.png")
        self.put("People/Person.md", "A person.")
        self.put("Places/Town.md", "[[Person]] and ![[Person]]")
        self.assertFalse(self.scan()["moves"])
        self.assertEqual(self.scan()["summary"]["unlinked"], 1)

    def test_support_reference_reopens_unlinked_review(self):
        self.put("assets/_unlinked/reference.png")
        self.put("_MoC/Guide.md", "![[reference.png]]")
        plan = self.scan()
        self.assertFalse(plan["moves"])
        self.assertIn("support-only-use-needs-review", plan["held"][0]["blockers"])

    def test_external_consumers_and_live_plugin_settings_block_moves(self):
        self.put("assets/a.png")
        self.put("assets/b.png")
        self.put("assets/c.png")
        self.put("_sessions/recap.md", "- Image: a.png\n- Image 2: b.png\n- Image 3: c.png")
        external = self.home / "website.json"
        external.write_text('{"map": "a.png"}')
        self.put(".obsidian/plugins/maps/data.json", '{"image": "b.png"}')
        self.put("_scripts/settings.json", '{"image": "c.png"}')
        plan = self.scan(consumer_roots=[external])
        self.assertFalse(plan["moves"])
        self.assertTrue(all("code-or-config-reference" in m["blockers"] for m in plan["held"]))

    def test_old_index_ignored_and_report_cannot_contaminate_vault(self):
        self.put("assets/orphan.png")
        self.put("_MoC/Data Cleaning/Unlinked Assets.md", "![[orphan.png]]")
        self.assertEqual(self.scan()["moves"][0]["category"], "unlinked")
        with self.assertRaisesRegex(ValueError, "outside"):
            finder.outside_scan(self.vault / "review.json", self.vault, [])

    def test_ignored_assets_cannot_be_exposed_by_move(self):
        subprocess.run(["git", "init", "-q", str(self.vault)], check=True)
        self.put(".gitignore", "assets/generated/\n")
        self.put("assets/generated/orphan.png")
        plan = self.scan()
        self.assertFalse(plan["moves"])
        self.assertEqual(plan["held"][0]["blockers"], ["would-expose-git-ignored-asset"])

    def test_same_inputs_produce_identical_json(self):
        self.put("assets/scene.png")
        self.put("_sessions/recap.md", "- Image: scene.png")
        self.assertEqual(finder.encoded(self.scan()), finder.encoded(self.scan()))

    def test_selected_subset_moves_verifies_and_preserves_other_files(self):
        self.put("assets/scene.png")
        self.put("assets/audio/orphan.mp3")
        self.put("_sessions/recap.md", "- Image: scene.png")
        plan = self.scan()
        plan["moves"] = [m for m in plan["moves"] if m["source"].endswith("scene.png")]
        mover.validate_plan(plan)
        self.assertTrue((self.vault / "assets/scene.png").exists())
        result = mover.apply_plan(plan, self.home / "receipt.json")
        self.assertEqual(result["status"], "verified")
        self.assertEqual((self.vault / "assets/campaign/scene.png").read_text(), "fixture bytes")
        self.assertFalse((self.vault / "assets/scene.png").exists())
        self.assertTrue((self.vault / "assets/audio/orphan.mp3").exists())
        self.assertEqual((self.vault / "_sessions/recap.md").read_text(), "- Image: scene.png")

    def test_new_link_changed_file_modified_destination_and_collision_rejected(self):
        for change in ("new-link", "bytes", "destination", "collision"):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as temp:
                vault = Path(temp) / "vault"
                (vault / "assets").mkdir(parents=True)
                source = vault / "assets/scene.png"; source.write_text("before")
                plan = finder.scan(vault)
                if change == "new-link":
                    (vault / "Regular.md").write_text("![[scene.png]]")
                elif change == "bytes":
                    source.write_text("changed")
                elif change == "destination":
                    plan["moves"][0]["destination"] = "../elsewhere.png"
                else:
                    (vault / "assets/_unlinked").mkdir()
                    (vault / "assets/_unlinked/scene.png").write_text("keep")
                with self.assertRaisesRegex(ValueError, "Stale or unsafe"):
                    mover.apply_plan(plan, Path(temp) / "receipt.json")
                self.assertTrue(source.exists())

    def test_late_failure_rolls_back_completed_moves(self):
        self.put("assets/a.png", "a")
        self.put("assets/b.png", "b")
        plan = self.scan()
        original_transfer = mover.transfer
        def failing_transfer(source, destination, digest):
            if source == self.vault / "assets/b.png":
                raise OSError("simulated disk failure")
            original_transfer(source, destination, digest)
        with patch.object(mover, "transfer", side_effect=failing_transfer):
            with self.assertRaisesRegex(OSError, "simulated"):
                mover.apply_plan(plan, self.home / "receipt.json")
        self.assertEqual((self.vault / "assets/a.png").read_text(), "a")
        self.assertEqual((self.vault / "assets/b.png").read_text(), "b")
        self.assertEqual(json.loads((self.home / "receipt.json").read_text())["status"], "rolled-back")

    def test_symlink_and_duplicate_plan_entries_rejected(self):
        self.put("assets/a.png")
        plan = self.scan()
        plan["moves"].append(copy.deepcopy(plan["moves"][0]))
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            mover.validate_plan(plan)
        (self.vault / "assets/a.png").unlink()
        external = self.home / "outside.png"; external.write_text("outside")
        (self.vault / "assets/a.png").symlink_to(external)
        self.assertIn("symlink", self.scan()["held"][0]["blockers"])

    def test_post_move_reference_change_rolls_back_without_reverting_note(self):
        self.put("assets/a.png", "a")
        plan = self.scan()
        original_transfer = mover.transfer
        def add_reference(source, destination, digest):
            original_transfer(source, destination, digest)
            if source == self.vault / "assets/a.png":
                self.put("New.md", "![[a.png]]")
        with patch.object(mover, "transfer", side_effect=add_reference):
            with self.assertRaisesRegex(ValueError, "References changed"):
                mover.apply_plan(plan, self.home / "receipt.json")
        self.assertTrue((self.vault / "assets/a.png").exists())
        self.assertEqual((self.vault / "New.md").read_text(), "![[a.png]]")

    def test_transfer_never_overwrites_an_existing_destination(self):
        source = self.put("assets/a.png", "original")
        destination = self.put("assets/_unlinked/a.png", "existing")
        with self.assertRaises(FileExistsError):
            mover.transfer(source, destination, finder.digest_file(source))
        self.assertEqual(source.read_text(), "original")
        self.assertEqual(destination.read_text(), "existing")


if __name__ == "__main__":
    unittest.main()

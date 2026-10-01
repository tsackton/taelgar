import importlib.util
import unittest
from pathlib import Path


script_path = Path(__file__).resolve().parents[1] / "scripts" / "render_source.py"
spec = importlib.util.spec_from_file_location("render_source", script_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def bundle(struck=False):
    return {
        "document": {
            "title": "Example",
            "tabs": [{"title": "Example", "body": {"content": [
                {"paragraph": {"paragraphStyle": {"namedStyleType": "HEADING_1"},
                               "elements": [{"textRun": {"content": "Example\n", "textStyle": {}}}]}},
                {"paragraph": {"elements": [
                    {"textRun": {"content": "Keep ", "textStyle": {"strikethrough": struck}}},
                    {"textRun": {"content": "remove", "textStyle": {"strikethrough": True}}},
                    {"textRun": {"content": " end\n", "textStyle": {"strikethrough": struck}}},
                ]}},
            ]}}],
        },
        "comments": [{"id": "c1", "resolved": True, "content": "Decision", "createdTime": "2023-01-01T00:00:00Z",
                      "quotedFileContent": {"value": "Keep &amp; remove"},
                      "replies": [{"id": "r1", "content": "Agreed", "createdTime": "2023-01-02T00:00:00Z"}]}],
    }


class RenderSourceTests(unittest.TestCase):
    def test_drop_mixed_strike_preserves_comments(self):
        result = module.render(bundle(), "drop")
        body, archive = result.split("## Google Docs comments")
        self.assertIn("Keep  end", body)
        self.assertNotIn("remove", body)
        self.assertIn("Resolved · c1", archive)
        self.assertIn("Keep & remove", archive)
        self.assertIn("Agreed", archive)

    def test_keep_strike_preserves_text(self):
        self.assertIn("Keep remove end", module.render(bundle()))

    def test_source_brackets_are_safe_for_obsidian(self):
        self.assertEqual(module.obsidian_safe("<A> [a] <South Cymea>"), "~~A~~ (a) ~~South Cymea~~")
        self.assertEqual(module.obsidian_safe("need some ideas>"), "need some ideas")
        sample = bundle()
        sample["document"]["tabs"][0]["body"]["content"][1]["paragraph"]["elements"][0]["textRun"]["content"] = "<A> [a] "
        result = module.render(sample)
        body, _ = result.split("## Google Docs comments")
        self.assertIn("~~A~~ (a)", body)
        self.assertNotIn("<A>", body)

    def test_comment_gets_full_sentence_context(self):
        sample = bundle()
        sample["comments"][0]["quotedFileContent"]["value"] = "remove"
        result = module.render(sample)
        self.assertIn("**Context in current document:** Keep remove end", result)

    def test_removed_selection_uses_labeled_revision(self):
        sample = bundle()
        sample["comments"][0]["quotedFileContent"]["value"] = "old wording"
        sample["revisions"] = [{"revisionId": "r1", "revisionModifiedTime": "2023-01-02T00:00:00Z",
                                "content": "The earlier sentence had old wording in it.\n"}]
        result = module.render(sample)
        self.assertIn("**Context in document revision `r1`:** The earlier sentence had old wording in it.", result)

    def test_all_struck_reading_copy_is_rejected(self):
        sample = bundle(True)
        sample["document"]["tabs"][0]["body"]["content"][0]["paragraph"]["elements"][0]["textRun"]["textStyle"] = {"strikethrough": True}
        with self.assertRaises(SystemExit):
            module.render(sample, "drop")


if __name__ == "__main__":
    unittest.main()

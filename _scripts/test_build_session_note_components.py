from __future__ import annotations

import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("build_session_note_components.py")
SPEC = importlib.util.spec_from_file_location("build_session_note_components", SCRIPT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Could not import {SCRIPT_PATH}")
components = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = components
SPEC.loader.exec_module(components)

SessionRecapParseError = components.SessionRecapParseError
parse_session_recap = components.parse_session_recap

TEST_DISPLAY_METADATA = {
    "typeDisplayDefaults": {
        "person": {"sessionNote": {"default": "<(*)pronunciation(*;)> <pronouns(,)> <ancestry:n> <subspecies:sn> <species:sn>"}},
        "place": {"sessionNote": {"default": "<(*)pronunciation(*;)> <typeof:sn> <home:2Fq>"}},
        "object": {"sessionNote": {"default": "<(*)pronunciation(*;)> <rarity:sn> <ancestry:n> <subtypeof:sn> <typeof:sn>"}},
        "group": {"sessionNote": {"default": "<(*)pronunciation(*;)> <ancestry:n> <subtypeof:sn> <typeof:sn>"}},
        "unknown": {"sessionNote": {"default": "<(*)pronunciation(*;)> <typeof:sn>"}},
    }
}


class SessionNoteComponentsTest(unittest.TestCase):
    def make_workspace(self) -> Path:
        tmpdir = Path(tempfile.mkdtemp(prefix="session-note-components-test."))
        self.addCleanup(lambda: shutil.rmtree(tmpdir, ignore_errors=True))
        vault = tmpdir / "vault"
        (vault / ".obsidian").mkdir(parents=True)
        (vault / "_templates" / "session-notes").mkdir(parents=True)
        (vault / "People").mkdir(parents=True)
        (vault / "Places").mkdir(parents=True)
        (vault / "Items").mkdir(parents=True)
        (vault / "Organizations").mkdir(parents=True)
        (vault / "Campaigns" / "Test Campaign" / "Sessions").mkdir(parents=True)
        (vault / "_templates" / "session-notes" / "test-session.md").write_text(
            textwrap.dedent(
                """\
                # {session.title}

                *{session.tagline}*

                {session.summary}

                ## Timeline
                {timeline}

                ## Cast
                {cast}

                ## Narrative
                {narrative.short}
                """
            ),
            encoding="utf-8",
        )
        (vault / "session.yaml").write_text(
            textwrap.dedent(
                """\
                schemaVersion: "1.0"
                sourceType: transcript
                scope: session
                campaign: Test Campaign
                sessionNumber: 12
                realWorldDate: 2026-03-29
                drStart: 1730-01-25
                drEnd: 1730-01-25
                participants: []
                sourceInputPath: /tmp/source.cleaned.md
                sourceConfigPath: /tmp/config.yaml
                participantsPath: /tmp/participants.yaml
                preparedSourcePath: /tmp/prepared.md
                sessionNote:
                  templatePath: _templates/session-notes/test-session.md
                  generatedRoot: Campaigns/Test Campaign/_generated/session-notes
                """
            ),
            encoding="utf-8",
        )
        (vault / "session-recap.md").write_text(self.reviewed_recap_text(), encoding="utf-8")
        (vault / "People" / "Kalima.md").write_text(
            textwrap.dedent(
                """\
                ---
                tags: [person]
                species: human
                gender: female
                pronunciation: kah-LEE-mah
                whereabouts: Frostbridge
                aliases: [Kalima of the Chasm]
                ---

                # Kalima
                """
            ),
            encoding="utf-8",
        )
        (vault / "Places" / "Zeyfa's Labyrinth.md").write_text(
            textwrap.dedent(
                """\
                ---
                tags: [place]
                typeOf: labyrinth
                whereabouts: Great Chasm
                ---

                # Zeyfa's Labyrinth
                """
            ),
            encoding="utf-8",
        )
        (vault / "Places" / "Great Chasm Encampment.md").write_text(
            textwrap.dedent(
                """\
                ---
                tags: [place]
                typeOf: encampment
                whereabouts: Great Chasm
                ---

                # Great Chasm Encampment
                """
            ),
            encoding="utf-8",
        )
        (vault / "Items" / "Romil's token.md").write_text(
            textwrap.dedent(
                """\
                ---
                tags: [object]
                typeOf: token
                owner: Kalima
                whereabouts: Frostbridge
                aliases: [Romil token]
                ---

                # Romil's token
                """
            ),
            encoding="utf-8",
        )
        (vault / "Organizations" / "Ashen Knives.md").write_text(
            textwrap.dedent(
                """\
                ---
                tags: [group]
                typeOf: raiders
                whereabouts: Great Chasm
                ---

                # Ashen Knives
                """
            ),
            encoding="utf-8",
        )
        return vault

    def reviewed_recap_text(self) -> str:
        return textwrap.dedent(
            """\
            # Session Recap

            ## Session Header

            - Title: Test Session 12: Into the Labyrinth
            - Desc Title: Into the Labyrinth
            - Tagline: in which the party descends
            - One-Sentence Summary: The party descends into Zeyfa's Labyrinth, fights Ashen Knives raiders, and escapes with Kalima and Romil's token.
            - Campaign: Test Campaign
            - Session Number: 12
            - DR Date: 1730-01-25
            - Real Date: 2026-03-29
            - DM: Maris
            - PCs: Ekko, Justas, Eolo

            ## Timeline

            ### Jan 25th, 1730 (afternoon)

            - Timeline Segment: timeline-001
            - Timeline Key: (DR:: 1730-01-25), afternoon
            - Resolution: part-of-day
            - Beat IDs: beat-001, beat-002
            - Locations: Zeyfa's Labyrinth
            - NPCs: Kalima
            - Organizations: Ashen Knives
            - Items: Romil's token
            - Combat Beats: beat-002

            #### Short
            The party enters Zeyfa's Labyrinth with Kalima and survives an ambush by Ashen Knives raiders.

            #### Long
            The party descends into Zeyfa's Labyrinth with Kalima as their guide, recovers Romil's token from the raiders, and breaks the Ashen Knives ambush before retreating back toward the surface.

            ### Jan 25th, 1730 (evening)

            - Timeline Segment: timeline-002
            - Timeline Key: (DR:: 1730-01-25), evening
            - Resolution: part-of-day
            - Beat IDs: beat-003
            - Locations: Great Chasm Encampment
            - NPCs: Kalima
            - Organizations: none
            - Items: Romil's token
            - Combat Beats: none

            #### Short
            At dusk the party returns to Great Chasm Encampment with Kalima and the recovered token.

            #### Long
            By evening the party is back at Great Chasm Encampment, where Kalima keeps close hold of Romil's token while the group shares the day's account and prepares for what comes next.

            ## Recap

            ### recap-001 | Into the Labyrinth

            - Kind: beat
            - Beat IDs: beat-001
            - Date: 1730-01-25
            - Time: afternoon
            - Source Range: u0001 -> u0100
            - Locations: Zeyfa's Labyrinth
            - NPCs: Kalima
            - Organizations: none
            - Items: none
            - Enemies: none

            #### Short
            The party descends into Zeyfa's Labyrinth with Kalima guiding them past the first frozen forks.

            #### Intermediate
            Kalima leads the party into Zeyfa's Labyrinth, where the first passages narrow under the ice and force the group to trust her memory of the maze.

            #### Long
            Kalima leads the party down the ice bridge and into Zeyfa's Labyrinth, where the frozen passages twist through old stone and leave the group dependent on her frightened but steady guidance.

            ### recap-002 | The Ashen Knives Ambush

            - Kind: combat
            - Beat IDs: beat-002
            - Date: 1730-01-25
            - Time: afternoon
            - Source Range: u0101 -> u0200
            - Locations: Zeyfa's Labyrinth
            - NPCs: Kalima
            - Organizations: Ashen Knives
            - Items: Romil's token
            - Enemies: Ashen Knives raiders

            #### Short
            Ashen Knives raiders spring an ambush in the maze, but the party drives them off and recovers Romil's token.

            #### Intermediate
            The Ashen Knives try to cut the party down in the frozen corridors, yet the ambush breaks apart when the raiders lose Romil's token and Kalima helps the party hold the line.

            #### Long
            Ashen Knives raiders crash into the party from a side passage and nearly split the group in the narrow corridor, but Kalima steadies the retreat long enough for the party to turn the fight, reclaim Romil's token, and force the survivors to flee deeper into the maze.

            ### recap-003 | Return to Camp

            - Kind: beat
            - Beat IDs: beat-003
            - Date: 1730-01-25
            - Time: evening
            - Source Range: u0201 -> u0280
            - Locations: Great Chasm Encampment
            - NPCs: Kalima
            - Organizations: none
            - Items: Romil's token
            - Enemies: none

            #### Short
            The party returns to Great Chasm Encampment with Kalima and the recovered token before night closes in.

            #### Intermediate
            By dusk the party is back in Great Chasm Encampment, where Kalima takes custody of Romil's token and the group recounts the Ashen Knives ambush to the camp.

            #### Long
            The party reaches Great Chasm Encampment by evening, hands Romil's token over to Kalima for safekeeping, and ends the day comparing the ambush to the older stories that first drew them into Zeyfa's Labyrinth.

            ## Cast

            ### NPCs

            - Kalima (companion): frightened guide
              - Zeyfa's Labyrinth, 1730-01-25
              - Great Chasm Encampment, 1730-01-25

            ## Locations

            - Zeyfa's Labyrinth
              - Summary: frozen maze beneath the Great Chasm
              - Sublocations: ice bridge, first forked passages
              - Date Visited: 1730-01-25
            - Great Chasm Encampment
              - Summary: surface camp above the labyrinth
              - Sublocations: watchfires, outer tents
              - Date Visited: 1730-01-25

            ## Organizations And Items

            ### Organizations

            - Ashen Knives (enemy): raiders contesting the labyrinth approaches
              - Zeyfa's Labyrinth, 1730-01-25

            ### Items

            - Romil's token (encountered): silver token recovered from the raiders
              - Zeyfa's Labyrinth, 1730-01-25
              - Great Chasm Encampment, 1730-01-25

            ## Combat

            ### recap-002 | The Ashen Knives Ambush

            - Beat IDs: beat-002
            - Enemies: Ashen Knives raiders
            - Context / Outcome: The party survives an Ashen Knives ambush in the labyrinth, routs the raiders, and recovers Romil's token.

            ## Source Files

            - Context JSON: /tmp/unused-context.json
            - Beats JSON: /tmp/unused-beats.json
            - Beat Facts JSON: /tmp/unused-beat-facts.json
            - Cleaned Source: /tmp/source.cleaned.md
            """
        )

    def run_builder(
        self,
        vault: Path,
        *,
        overwrite: bool = False,
        update: bool = False,
    ) -> subprocess.CompletedProcess[str]:
        try:
            session_payload = components.read_yaml_mapping(vault / "session.yaml")
            recap = components.parse_session_recap((vault / "session-recap.md").read_text(encoding="utf-8"))
            generated_root = vault / "Campaigns" / "Test Campaign" / "_generated" / "session-notes"
            component_dir = generated_root / components.build_component_dir_name(
                session_payload,
                fallback="session",
            )
            component_dir.mkdir(parents=True, exist_ok=True)
            components.ensure_component_files_writable(
                [
                    component_dir / "01-session-info.md",
                    component_dir / "02-technical-updates.md",
                    component_dir / "03-narrative.md",
                ],
                overwrite=overwrite,
                update=update,
            )
            note_index = components.VaultNoteIndex(vault, generated_root)
            slots = components.build_slots(
                recap=recap,
                note_index=note_index,
                session_payload=session_payload,
                campaign_slug="test-campaign",
                display_metadata=TEST_DISPLAY_METADATA,
            )
            components.write_component_file(
                component_dir / "01-session-info.md",
                title="Session Info",
                session_manifest=str(vault / "session.yaml"),
                slots=slots["info"],
                overwrite=overwrite,
                update=update,
            )
            components.write_component_file(
                component_dir / "02-technical-updates.md",
                title="Technical Updates",
                session_manifest=str(vault / "session.yaml"),
                slots=slots["technical"],
                overwrite=overwrite,
                update=update,
            )
            components.write_component_file(
                component_dir / "03-narrative.md",
                title="Narrative",
                session_manifest=str(vault / "session.yaml"),
                slots=slots["narrative"],
                overwrite=overwrite,
                update=update,
            )
            return subprocess.CompletedProcess(args=[str(SCRIPT_PATH)], returncode=0, stdout="", stderr="")
        except Exception as exc:
            return subprocess.CompletedProcess(args=[str(SCRIPT_PATH)], returncode=1, stdout="", stderr=repr(exc))

    def remove_slot(self, text: str, slot_name: str) -> str:
        return re.sub(
            rf"<!-- SLOT: {re.escape(slot_name)} -->\n.*?<!-- /SLOT -->\n\n?",
            "",
            text,
            count=1,
            flags=re.DOTALL,
        )

    def replace_slot_body(self, text: str, slot_name: str, body: str) -> str:
        return re.sub(
            rf"<!-- SLOT: {re.escape(slot_name)} -->\n.*?<!-- /SLOT -->",
            f"<!-- SLOT: {slot_name} -->\n{body.rstrip()}\n<!-- /SLOT -->",
            text,
            count=1,
            flags=re.DOTALL,
        )

    def test_parser_extracts_reviewed_recap_sections(self) -> None:
        recap = parse_session_recap(self.reviewed_recap_text())

        self.assertEqual(recap["header"]["Title"], "Test Session 12: Into the Labyrinth")
        self.assertEqual(recap["header"]["Desc Title"], "Into the Labyrinth")
        self.assertEqual(len(recap["timeline"]), 2)
        self.assertEqual(recap["timeline"][1]["locations"], ["Great Chasm Encampment"])
        self.assertEqual(recap["recap"][1]["kind"], "combat")
        self.assertEqual(recap["cast"][0]["name"], "Kalima")
        self.assertEqual(recap["locations"][0]["summary"], "frozen maze beneath the Great Chasm")
        self.assertEqual(recap["locations"][0]["sublocations"], "ice bridge, first forked passages")
        self.assertEqual(recap["locations"][0]["dateVisited"], "1730-01-25")
        self.assertEqual(recap["items"][0]["history"][-1]["location"], "Great Chasm Encampment")
        self.assertEqual(recap["combat"][0]["title"], "The Ashen Knives Ambush")

    def test_parser_accepts_recap_frontmatter(self) -> None:
        recap = parse_session_recap("---\ntags: [status/recap-review]\n---\n\n" + self.reviewed_recap_text())

        self.assertEqual(recap["header"]["Title"], "Test Session 12: Into the Labyrinth")
        self.assertEqual(len(recap["timeline"]), 2)

    def test_parser_extracts_optional_recap_media(self) -> None:
        text = (
            self.reviewed_recap_text()
            .replace(
                "- Enemies: none\n\n"
                "#### Short\n"
                "The party descends",
                "- Enemies: none\n"
                "- Image: zeyfa-labyrinth.jpg\n"
                "- Image Placement: start\n"
                "- Image Render: right|400\n"
                "- Image Caption: The first frozen fork.\n\n"
                "#### Short\n"
                "The party descends",
                1,
            )
            + textwrap.dedent(
                """\

                ## Pull Quotes

                - ID: quote-test-001
                  - Quote: "The maze remembers."
                  - Speaker: Kalima
                  - Source Lines: u0010-u0012

                ## Audio Highlights

                - ID: audio-test-001
                  - Title: Kalima explains the maze
                  - Speaker: Kalima
                  - Source Lines: u0010-u0040
                  - Output: kalima-explains-the-maze.m4a
                """
            )
        )

        recap = parse_session_recap(text)

        self.assertEqual(recap["recap"][0]["images"][0]["path"], "zeyfa-labyrinth.jpg")
        self.assertEqual(recap["recap"][0]["images"][0]["render"], "right|400")
        self.assertEqual(recap["recap"][0]["images"][0]["caption"], "The first frozen fork.")
        self.assertEqual(recap["pullQuotes"][0]["ID"], "quote-test-001")
        self.assertEqual(recap["audioHighlights"][0]["Output"], "kalima-explains-the-maze.m4a")

    def test_parser_normalizes_wikilinked_world_entries(self) -> None:
        linked = (
            self.reviewed_recap_text()
            .replace("Locations: Zeyfa's Labyrinth", "Locations: [[Zeyfa's Labyrinth]]")
            .replace("- Kalima (companion):", "- [[Kalima]] (companion):")
            .replace("- Zeyfa's Labyrinth\n", "- [[Zeyfa's Labyrinth]]\n")
            .replace("- Romil's token (encountered):", "- [[Romil's token]] (encountered):")
            .replace("  - Zeyfa's Labyrinth, 1730-01-25", "  - [[Zeyfa's Labyrinth]], 1730-01-25")
        )

        recap = parse_session_recap(linked)

        self.assertEqual(recap["timeline"][0]["locations"], ["Zeyfa's Labyrinth"])
        self.assertEqual(recap["cast"][0]["name"], "Kalima")
        self.assertEqual(recap["locations"][0]["name"], "Zeyfa's Labyrinth")
        self.assertEqual(recap["items"][0]["name"], "Romil's token")
        self.assertEqual(recap["items"][0]["history"][0]["location"], "Zeyfa's Labyrinth")


    def test_parser_rejects_malformed_world_section(self) -> None:
        broken = self.reviewed_recap_text().replace("### NPCs", "### Allies")

        with self.assertRaises(SessionRecapParseError) as ctx:
            parse_session_recap(broken)

        self.assertTrue(any("Cast section is missing subsection ### NPCs." in error for error in ctx.exception.errors))

    def test_builder_writes_component_notes_with_required_frontmatter_and_slots(self) -> None:
        vault = self.make_workspace()
        result = self.run_builder(vault)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        component_dir = vault / "Campaigns" / "Test Campaign" / "_generated" / "session-notes" / "test-campaign-session-12"
        info_path = component_dir / "01-session-info.md"
        tech_path = component_dir / "02-technical-updates.md"
        narrative_path = component_dir / "03-narrative.md"
        self.assertTrue(info_path.exists())
        self.assertTrue(tech_path.exists())
        self.assertTrue(narrative_path.exists())

        info_text = info_path.read_text(encoding="utf-8")
        self.assertNotIn("status/check/ai", info_text)
        self.assertIn('excludePublish: ["all"]', info_text)
        self.assertIn("<!-- SLOT: session.summary -->", info_text)
        self.assertIn("<!-- SLOT: session.pull_quotes -->", info_text)
        self.assertIn("<!-- SLOT: session.audio_highlights -->", info_text)
        self.assertIn("<!-- SLOT: session.desc_title -->", info_text)
        self.assertIn("<!-- SLOT: session.dr_end -->\n1730-01-25", info_text)
        self.assertIn("<!-- SLOT: session.dr_range_inline -->\n(DR:: 1730-01-25)", info_text)
        self.assertIn("<!-- SLOT: session.pcs_plain_inline -->\nEkko, Justas, Eolo", info_text)
        self.assertIn("Into the Labyrinth", info_text)
        self.assertIn("<!-- SLOT: timeline -->", info_text)
        self.assertIn("<!-- SLOT: groups -->", info_text)
        self.assertIn(
            "- [[Ashen Knives]] (<(*)pronunciation(*;)> <ancestry:n> <subtypeof:sn> <typeof:sn>): raiders contesting the labyrinth approaches.",
            info_text,
        )
        self.assertIn("  - [[Zeyfa's Labyrinth]], 1730-01-25", info_text)
        frontmatter = info_text.split("---", 2)[1]
        self.assertNotIn("[[", frontmatter)
        self.assertIn(
            "- [[Zeyfa's Labyrinth]] (<(*)pronunciation(*;)> <typeof:sn> <home:2Fq>): frozen maze beneath the Great Chasm. Session context includes: ice bridge and first forked passages.",
            info_text,
        )

        tech_text = tech_path.read_text(encoding="utf-8")
        tech_frontmatter = tech_text.split("---", 2)[1]
        self.assertNotIn("[[", tech_frontmatter)
        self.assertIn("<!-- SLOT: updates.whereabouts.party -->", tech_text)
        self.assertIn("<!-- SLOT: updates.whereabouts.locations -->", tech_text)
        self.assertIn("<!-- SLOT: updates.review -->", tech_text)

        narrative_text = narrative_path.read_text(encoding="utf-8")
        narrative_frontmatter = narrative_text.split("---", 2)[1]
        self.assertNotIn("[[", narrative_frontmatter)
        self.assertIn("<!-- SLOT: narrative.short -->", narrative_text)
        self.assertIn("<!-- SLOT: narrative.long -->", narrative_text)
        self.assertIn("The party descends into [[Zeyfa's Labyrinth]] with [[Kalima]]", narrative_text)

    def test_builder_renders_images_pull_quotes_and_audio_from_recap(self) -> None:
        vault = self.make_workspace()
        recap_path = vault / "session-recap.md"
        recap_path.write_text(
            self.reviewed_recap_text()
            .replace(
                "- Enemies: none\n\n"
                "#### Short\n"
                "The party descends",
                "- Enemies: none\n"
                "- Image: zeyfa-labyrinth.jpg\n"
                "- Image Placement: start\n"
                "- Image Render: right|400\n"
                "- Image Caption: The first frozen fork.\n\n"
                "#### Short\n"
                "The party descends",
                1,
            )
            .replace(
                "- Enemies: Ashen Knives raiders\n\n"
                "#### Short\n"
                "Ashen Knives",
                "- Enemies: Ashen Knives raiders\n"
                "- Image: ambush.jpg\n"
                "- Image Placement: end\n"
                "- Image Render: left|320\n\n"
                "#### Short\n"
                "Ashen Knives",
                1,
            )
            + textwrap.dedent(
                """\

                ## Pull Quotes

                - ID: quote-test-001
                  - Quote: "The maze remembers."
                  - Speaker: Kalima
                  - Source Lines: u0010-u0012

                ## Audio Highlights

                - ID: audio-test-001
                  - Title: Kalima explains the maze
                  - Speaker: Kalima
                  - Source Lines: u0010-u0040
                  - Output: kalima-explains-the-maze.m4a
                """
            ),
            encoding="utf-8",
        )

        result = self.run_builder(vault)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        component_dir = vault / "Campaigns" / "Test Campaign" / "_generated" / "session-notes" / "test-campaign-session-12"
        info_text = (component_dir / "01-session-info.md").read_text(encoding="utf-8")
        narrative_text = (component_dir / "03-narrative.md").read_text(encoding="utf-8")
        tech_text = (component_dir / "02-technical-updates.md").read_text(encoding="utf-8")

        self.assertIn("<!-- SLOT: session.pull_quotes -->\n> [!quote] Kalima\n> \"The maze remembers.\"", info_text)
        self.assertIn("## Audio Highlights", info_text)
        self.assertIn("- **Kalima explains the maze** (Kalima, u0010-u0040)", info_text)
        self.assertIn("  - Clip output: `kalima-explains-the-maze.m4a`", info_text)
        self.assertIn("Audio highlights: no source audio path found; clips were not cut.", tech_text)
        self.assertIn("> [!image|right]\n> ![[zeyfa-labyrinth.jpg|400]]\n> *The first frozen fork.*", narrative_text)
        self.assertIn("force the survivors to flee deeper into the maze.\n\n![[ambush.jpg|left|320]]", narrative_text)

    def test_base_note_uses_session_template_frontmatter_key(self) -> None:
        vault = self.make_workspace()
        note_path = vault / "Campaigns" / "Test Campaign" / "Sessions" / "Session 12.md"

        components.ensure_base_note(
            note_path=note_path,
            session_key="test-campaign-session-12",
            template_name="test-session.md",
        )

        note_text = note_path.read_text(encoding="utf-8")
        self.assertIn("session-template: test-session.md", note_text)
        self.assertNotRegex(note_text, r"(?m)^template:")

    def test_base_note_migrates_legacy_template_frontmatter_key(self) -> None:
        vault = self.make_workspace()
        note_path = vault / "Campaigns" / "Test Campaign" / "Sessions" / "Session 12.md"
        note_path.write_text("---\ntemplate: legacy-session.md\n---\nExisting body\n", encoding="utf-8")

        components.ensure_base_note(
            note_path=note_path,
            session_key="test-campaign-session-12",
            template_name="test-session.md",
        )

        note_text = note_path.read_text(encoding="utf-8")
        self.assertIn("session-template: legacy-session.md", note_text)
        self.assertNotRegex(note_text, r"(?m)^template:")
        self.assertIn("Existing body", note_text)

    def test_builder_leaves_blank_dr_end_out_of_inline_range(self) -> None:
        vault = self.make_workspace()
        session_path = vault / "session.yaml"
        session_path.write_text(
            session_path.read_text(encoding="utf-8").replace("drEnd: 1730-01-25\n", ""),
            encoding="utf-8",
        )

        result = self.run_builder(vault)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        info_text = (
            vault
            / "Campaigns"
            / "Test Campaign"
            / "_generated"
            / "session-notes"
            / "test-campaign-session-12"
            / "01-session-info.md"
        ).read_text(encoding="utf-8")
        self.assertIn("<!-- SLOT: session.dr_end -->\n<!-- /SLOT -->", info_text)
        self.assertIn("<!-- SLOT: session.dr_range_inline -->\n(DR:: 1730-01-25)", info_text)

    def test_builder_renders_distinct_dr_end_in_inline_range(self) -> None:
        vault = self.make_workspace()
        session_path = vault / "session.yaml"
        session_path.write_text(
            session_path.read_text(encoding="utf-8").replace("drEnd: 1730-01-25", "drEnd: 1730-01-27"),
            encoding="utf-8",
        )

        result = self.run_builder(vault)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        info_text = (
            vault
            / "Campaigns"
            / "Test Campaign"
            / "_generated"
            / "session-notes"
            / "test-campaign-session-12"
            / "01-session-info.md"
        ).read_text(encoding="utf-8")
        self.assertIn("<!-- SLOT: session.dr_end -->\n1730-01-27", info_text)
        self.assertIn(
            "<!-- SLOT: session.dr_range_inline -->\n(DR:: 1730-01-25) to (DR:: 1730-01-27)",
            info_text,
        )

    def test_builder_uses_reviewed_recap_as_canonical_source(self) -> None:
        vault = self.make_workspace()
        recap_path = vault / "session-recap.md"
        recap_path.write_text(
            self.reviewed_recap_text().replace(
                "frightened guide",
                "battle-worn guide",
            ),
            encoding="utf-8",
        )

        result = self.run_builder(vault)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        info_text = (
            vault
            / "Campaigns"
            / "Test Campaign"
            / "_generated"
            / "session-notes"
            / "test-campaign-session-12"
            / "01-session-info.md"
        ).read_text(encoding="utf-8")
        self.assertIn("battle-worn guide", info_text)
        self.assertNotIn("frightened guide", info_text)

    def test_builder_writes_blank_groups_slot_when_organizations_are_empty(self) -> None:
        vault = self.make_workspace()
        recap_path = vault / "session-recap.md"
        recap_path.write_text(
            self.reviewed_recap_text().replace(
                "- Ashen Knives (enemy): raiders contesting the labyrinth approaches\n"
                "  - Zeyfa's Labyrinth, 1730-01-25\n\n"
                "### Items",
                "\n### Items",
            ),
            encoding="utf-8",
        )

        result = self.run_builder(vault)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        info_text = (
            vault
            / "Campaigns"
            / "Test Campaign"
            / "_generated"
            / "session-notes"
            / "test-campaign-session-12"
            / "01-session-info.md"
        ).read_text(encoding="utf-8")
        self.assertIn("<!-- SLOT: groups -->\n<!-- /SLOT -->", info_text)

    def test_builder_enriches_from_notes_and_surfaces_location_conflicts(self) -> None:
        vault = self.make_workspace()
        result = self.run_builder(vault)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        component_dir = vault / "Campaigns" / "Test Campaign" / "_generated" / "session-notes" / "test-campaign-session-12"
        info_text = (component_dir / "01-session-info.md").read_text(encoding="utf-8")
        tech_text = (component_dir / "02-technical-updates.md").read_text(encoding="utf-8")

        self.assertIn(
            "[[Kalima]] (<(*)pronunciation(*;)> <pronouns(,)> <ancestry:n> <subspecies:sn> <species:sn>): frightened guide.",
            info_text,
        )
        self.assertIn(
            "[[Romil's token]] (<(*)pronunciation(*;)> <rarity:sn> <ancestry:n> <subtypeof:sn> <typeof:sn>): silver token recovered from the raiders.",
            info_text,
        )
        self.assertIn(
            "note currently says whereabouts 'Frostbridge', but the reviewed recap ends them at 'Great Chasm Encampment'.",
            tech_text,
        )
        self.assertIn(
            "note currently says whereabouts 'Frostbridge', but the reviewed recap last places it at 'Great Chasm Encampment'.",
            tech_text,
        )

    def test_builder_resolves_frontmatter_aliases_without_obsidian_metadata(self) -> None:
        vault = self.make_workspace()
        recap_path = vault / "session-recap.md"
        recap_path.write_text(
            self.reviewed_recap_text().replace("Kalima", "Kalima of the Chasm"),
            encoding="utf-8",
        )

        result = self.run_builder(vault)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        info_text = (
            vault
            / "Campaigns"
            / "Test Campaign"
            / "_generated"
            / "session-notes"
            / "test-campaign-session-12"
            / "01-session-info.md"
        ).read_text(encoding="utf-8")
        self.assertIn("[[Kalima|Kalima of the Chasm]]", info_text)
        self.assertNotIn("metadata.json", result.stdout + result.stderr)

    def test_builder_refuses_to_overwrite_existing_components_by_default(self) -> None:
        vault = self.make_workspace()
        first_result = self.run_builder(vault)
        self.assertEqual(first_result.returncode, 0, first_result.stdout + first_result.stderr)
        info_path = (
            vault
            / "Campaigns"
            / "Test Campaign"
            / "_generated"
            / "session-notes"
            / "test-campaign-session-12"
            / "01-session-info.md"
        )
        info_path.write_text("manual edits\n", encoding="utf-8")

        second_result = self.run_builder(vault)

        self.assertEqual(second_result.returncode, 1)
        self.assertIn("pass --overwrite to replace", second_result.stderr)
        self.assertEqual("manual edits\n", info_path.read_text(encoding="utf-8"))

    def test_builder_overwrites_existing_components_with_flag(self) -> None:
        vault = self.make_workspace()
        first_result = self.run_builder(vault)
        self.assertEqual(first_result.returncode, 0, first_result.stdout + first_result.stderr)
        info_path = (
            vault
            / "Campaigns"
            / "Test Campaign"
            / "_generated"
            / "session-notes"
            / "test-campaign-session-12"
            / "01-session-info.md"
        )
        info_path.write_text("manual edits\n", encoding="utf-8")

        second_result = self.run_builder(vault, overwrite=True)

        self.assertEqual(second_result.returncode, 0, second_result.stdout + second_result.stderr)
        self.assertIn("# Session Info", info_path.read_text(encoding="utf-8"))
        self.assertNotEqual("manual edits\n", info_path.read_text(encoding="utf-8"))

    def test_builder_update_adds_missing_slots_without_overwriting_existing_slots(self) -> None:
        vault = self.make_workspace()
        first_result = self.run_builder(vault)
        self.assertEqual(first_result.returncode, 0, first_result.stdout + first_result.stderr)
        info_path = (
            vault
            / "Campaigns"
            / "Test Campaign"
            / "_generated"
            / "session-notes"
            / "test-campaign-session-12"
            / "01-session-info.md"
        )
        old_text = self.remove_slot(info_path.read_text(encoding="utf-8"), "groups")
        old_text = self.replace_slot_body(old_text, "session.summary", "Manual summary preserved.")
        info_path.write_text(old_text, encoding="utf-8")

        second_result = self.run_builder(vault, update=True)

        self.assertEqual(second_result.returncode, 0, second_result.stdout + second_result.stderr)
        updated_text = info_path.read_text(encoding="utf-8")
        self.assertIn("<!-- SLOT: session.summary -->\nManual summary preserved.\n<!-- /SLOT -->", updated_text)
        self.assertIn("<!-- SLOT: groups -->", updated_text)
        self.assertIn("[[Ashen Knives]]", updated_text)
        self.assertLess(updated_text.index("<!-- SLOT: groups -->"), updated_text.index("<!-- SLOT: combat.summary -->"))

    def test_builder_update_creates_missing_component_files(self) -> None:
        vault = self.make_workspace()
        first_result = self.run_builder(vault)
        self.assertEqual(first_result.returncode, 0, first_result.stdout + first_result.stderr)
        narrative_path = (
            vault
            / "Campaigns"
            / "Test Campaign"
            / "_generated"
            / "session-notes"
            / "test-campaign-session-12"
            / "03-narrative.md"
        )
        narrative_path.unlink()

        second_result = self.run_builder(vault, update=True)

        self.assertEqual(second_result.returncode, 0, second_result.stdout + second_result.stderr)
        self.assertTrue(narrative_path.exists())
        self.assertIn("<!-- SLOT: narrative.long -->", narrative_path.read_text(encoding="utf-8"))

    def test_builder_update_rejects_duplicate_existing_slot_markers(self) -> None:
        vault = self.make_workspace()
        first_result = self.run_builder(vault)
        self.assertEqual(first_result.returncode, 0, first_result.stdout + first_result.stderr)
        info_path = (
            vault
            / "Campaigns"
            / "Test Campaign"
            / "_generated"
            / "session-notes"
            / "test-campaign-session-12"
            / "01-session-info.md"
        )
        original_text = info_path.read_text(encoding="utf-8")
        duplicate_text = original_text + "\n<!-- SLOT: session.summary -->\nduplicate\n<!-- /SLOT -->\n"
        info_path.write_text(duplicate_text, encoding="utf-8")

        second_result = self.run_builder(vault, update=True)

        self.assertEqual(second_result.returncode, 1)
        self.assertIn("duplicate slot 'session.summary'", second_result.stderr)
        self.assertEqual(duplicate_text, info_path.read_text(encoding="utf-8"))

    def test_builder_update_rejects_malformed_existing_slot_markers(self) -> None:
        vault = self.make_workspace()
        first_result = self.run_builder(vault)
        self.assertEqual(first_result.returncode, 0, first_result.stdout + first_result.stderr)
        info_path = (
            vault
            / "Campaigns"
            / "Test Campaign"
            / "_generated"
            / "session-notes"
            / "test-campaign-session-12"
            / "01-session-info.md"
        )
        malformed_text = info_path.read_text(encoding="utf-8").replace("<!-- /SLOT -->", "<!-- /SLOT BROKEN -->", 1)
        info_path.write_text(malformed_text, encoding="utf-8")

        second_result = self.run_builder(vault, update=True)

        self.assertEqual(second_result.returncode, 1)
        self.assertIn("malformed slot end marker", second_result.stderr)
        self.assertEqual(malformed_text, info_path.read_text(encoding="utf-8"))

    def test_autolink_does_not_link_possessive_owner_without_full_phrase_note(self) -> None:
        vault = self.make_workspace()
        (vault / "People" / "Ryu.md").write_text(
            textwrap.dedent(
                """\
                ---
                tags: [person]
                ---

                # Ryu
                """
            ),
            encoding="utf-8",
        )
        note_index = components.VaultNoteIndex(
            vault,
            vault / "Campaigns" / "Test Campaign" / "_generated" / "session-notes",
        )

        linked = note_index.autolink_text(
            "Ryu visits Ryu's tower while Ryu\u2019s shark waits nearby.",
            autolink_terms={"Ryu"},
        )

        self.assertIn("[[Ryu]] visits Ryu's tower", linked)
        self.assertIn("Ryu\u2019s shark", linked)
        self.assertNotIn("[[Ryu]]'s", linked)
        self.assertNotIn("[[Ryu]]\u2019s", linked)

    def test_autolink_prefers_existing_possessive_phrase_note(self) -> None:
        vault = self.make_workspace()
        (vault / "People" / "Ryu.md").write_text(
            textwrap.dedent(
                """\
                ---
                tags: [person]
                ---

                # Ryu
                """
            ),
            encoding="utf-8",
        )
        (vault / "Places" / "Ryu's Tower.md").write_text(
            textwrap.dedent(
                """\
                ---
                tags: [place]
                typeOf: tower
                ---

                # Ryu's Tower
                """
            ),
            encoding="utf-8",
        )
        note_index = components.VaultNoteIndex(
            vault,
            vault / "Campaigns" / "Test Campaign" / "_generated" / "session-notes",
        )

        linked = note_index.autolink_text(
            "Ryu's tower overlooks the bay. Ryu visits often. Ryu\u2019s tower is old.",
            autolink_terms={"Ryu"},
        )

        self.assertIn("[[Ryu's Tower|Ryu's tower]] overlooks the bay", linked)
        self.assertIn("[[Ryu]] visits often", linked)
        self.assertIn("[[Ryu's Tower|Ryu\u2019s tower]] is old", linked)
        self.assertNotIn("[[Ryu]]'s", linked)
        self.assertNotIn("[[Ryu]]\u2019s", linked)

    def test_builder_emits_review_only_update_candidates(self) -> None:
        vault = self.make_workspace()
        result = self.run_builder(vault)

        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        tech_text = (
            vault
            / "Campaigns"
            / "Test Campaign"
            / "_generated"
            / "session-notes"
            / "test-campaign-session-12"
            / "02-technical-updates.md"
        ).read_text(encoding="utf-8")

        self.assertIn("Candidate party whereabouts: (DR:: 1730-01-25), evening: party ends at [[Great Chasm Encampment]].", tech_text)
        self.assertIn("[[Kalima]]: candidate whereabouts update from (DR:: 1730-01-25), evening -> [[Great Chasm Encampment]].", tech_text)
        self.assertIn("Whereabouts line: `- {type: away, start: 1730-01-25, location: Great Chasm Encampment}`", tech_text)
        self.assertNotIn("location: [[Great Chasm Encampment]]", tech_text)
        self.assertIn("[[Romil's token]]: candidate item-location update from (DR:: 1730-01-25), evening -> [[Great Chasm Encampment]].", tech_text)


if __name__ == "__main__":
    unittest.main()

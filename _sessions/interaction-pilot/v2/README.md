# NPC interaction extraction trials — version 2

[Extraction skill](../../../.agents/skills/extract-campaign-interactions/SKILL.md) · [Format](../../../.agents/skills/extract-campaign-interactions/references/format.md)

Each NPC card has one session overview, an optional featured pull quote, and complete encounters linked to the frozen transcript. Scenes retain separate locations and dates; short evidence links help navigate long conversations. Original v1 pilots are preserved.

| Session | Scenes | NPCs | Interactions | Quotes | Data |
| --- | ---: | ---: | ---: | ---: | --- |
| [Dunmari 8 — retest](dunmari-frontier-008/review.md) | 17 | 4 | 9 | 1 | [JSON](dunmari-frontier-008/extraction.json) · [Evidence](dunmari-frontier-008/evidence.md) |
| [Dunmari 60 — retest](dunmari-frontier-060/review.md) | 20 | 10 | 23 | 4 | [JSON](dunmari-frontier-060/extraction.json) · [Evidence](dunmari-frontier-060/evidence.md) |
| [Mawar 2](mawar-adventures-002/review.md) | 26 | 17 | 52 | 8 | [JSON](mawar-adventures-002/extraction.json) · [Evidence](mawar-adventures-002/evidence.md) |
| [Lost in the Feywild 6](lost-in-the-feywild-006/review.md) | 5 | 8 | 11 | 3 | [JSON](lost-in-the-feywild-006/extraction.json) · [Evidence](lost-in-the-feywild-006/evidence.md) |
| [Dunmari 108](dunmari-frontier-108/review.md) | 17 | 11 | 28 | 4 | [JSON](dunmari-frontier-108/extraction.json) · [Evidence](dunmari-frontier-108/evidence.md) |

## What changed

- Pull quotes have exact source ranges and contextual attribution, distinct from introduction descriptions. Select one featured quote per speaking NPC where a suitable line exists; absence is allowed. One written quote is explicitly labeled as such.
- Exactly one session overview per NPC, grounded in all of its interaction records.
- `present` captures affirmative idle presence, such as Baxter on deck and Aurae carried in a backpack. A cast entry, a mention, or an earlier location is insufficient.
- `scenes` replaces the single `scene` on interactions. Full encounter bounds are separate from short evidence excerpts; topics, jokes, and minor interjections stay together. Makha’s seven old records become one guided visit, and Inakara’s negotiation and approach become one encounter across three scenes.
- Dimitaur’s temple conversation remains one interaction through 958 source utterances, with short evidence links and one selected quote. His earlier rumor, remote observation, and message delivery remain distinct.

## Selection and limits

Dunmari 108 has 21 beats, fifth-highest among 34 available Dunmari beat files, and all four core PCs speak: Kenzo, Wellby, Delwath and Seeker. It provides several sustained conversations and party splits, rather than mainly combat rounds or postgame discussion.

Mawar 2’s note continues beyond the recorded session with Sefa, restitution, item identification and Azar’s later departure. This transcript-backed trial explicitly flags those unrecorded follow-ups. Reliah’s presence is not clear in the transcript despite the recap grouping her with Samar. ASR wording is preserved in quotes.

Dunmari 60 retains its previously recorded date uncertainty. Dunmari 108’s played interactions stay on May 18 even though session metadata extends to May 19. The planned overnight rest is not treated as a recorded morning encounter.

All five JSON files pass source hashes, source coverage, scene and entity joins, bounds, exact quote text, NPC overview coverage, and overlap checks. Twelve validator tests pass. Contextual review also checked quote speakers, presence and conversation boundaries; structural validation alone cannot settle those judgments.

Links use local transcript lines. The stored source hash and utterance ranges support a future web viewer; these files do not implement Taelgarverse runtime integration.

# Campaign interaction trials — version 3

Current baseline: transcript-only event extraction. Session notes may support dates and identity, but contribute no additional events or participation. The later v4 mixed-source experiment is superseded.

[Skill](../../../.agents/skills/extract-campaign-interactions/SKILL.md) · [Format](../../../.agents/skills/extract-campaign-interactions/references/format.md)

Adds important-item cards, a type for every scene, and multiple complementary quotes for major NPCs. Every entity still gets one session overview. Existing NPC encounters and source boundaries are preserved, including long conversations. Earlier v2 results remain available.

| Session | NPCs | Items | NPC quotes | Scene types | Reviews |
| --- | ---: | ---: | ---: | --- | --- |
| [Dunmari 8](dunmari-frontier-008/review.md) | 4 | 1 | 2 | conversation: 4, exploration: 6, combat: 1, travel: 6 | [Items](dunmari-frontier-008/items.md) · [NPCs](dunmari-frontier-008/npcs.md) · [JSON](dunmari-frontier-008/extraction.json) · [Evidence](dunmari-frontier-008/evidence.md) |
| [Dunmari 60](dunmari-frontier-060/review.md) | 10 | 4 | 6 | conversation: 9, exploration: 2, combat: 1, travel: 8 | [Items](dunmari-frontier-060/items.md) · [NPCs](dunmari-frontier-060/npcs.md) · [JSON](dunmari-frontier-060/extraction.json) · [Evidence](dunmari-frontier-060/evidence.md) |
| [Mawar 2](mawar-adventures-002/review.md) | 17 | 5 | 11 | conversation: 15, exploration: 7, combat: 1, travel: 3 | [Items](mawar-adventures-002/items.md) · [NPCs](mawar-adventures-002/npcs.md) · [JSON](mawar-adventures-002/extraction.json) · [Evidence](mawar-adventures-002/evidence.md) |
| [Lost in the Feywild 6](lost-in-the-feywild-006/review.md) | 8 | 3 | 6 | conversation: 1, exploration: 2, combat: 1, travel: 1 | [Items](lost-in-the-feywild-006/items.md) · [NPCs](lost-in-the-feywild-006/npcs.md) · [JSON](lost-in-the-feywild-006/extraction.json) · [Evidence](lost-in-the-feywild-006/evidence.md) |
| [Dunmari 108](dunmari-frontier-108/review.md) | 11 | 5 | 10 | conversation: 4, exploration: 7, combat: 0, travel: 6 | [Items](dunmari-frontier-108/items.md) · [NPCs](dunmari-frontier-108/npcs.md) · [JSON](dunmari-frontier-108/extraction.json) · [Evidence](dunmari-frontier-108/evidence.md) |

Rai’s jade card distinguishes four held fragments from the fifth reported with Ra’ghemdros. The same session also indexes Kenzo’s staff, the circlet paid to Ghesh, the mirror prison and the discussed phylactery. No future acquisition or secret object identity is inferred.

Item interactions use the existing four kinds: interacted, observed, present and mentioned. Their exact source quotes are labeled as descriptions, writing or dialogue with the real speaker. Routine inventory, every weapon attack and background furnishings remain excluded.

Each scene has exactly one dominant type: conversation, exploration, combat or travel. Travel with incidental dialogue remains travel; magical investigation can remain exploration despite questions. Types do not fragment the full conversation records.

Major NPCs can feature several quotes from one conversation: Aurae has four, Ghesh three, and Dimitaur four. The single overview and whole interaction stay intact; shorter NPCs have fewer quotes when appropriate.

Mawar retains the transcript coverage limit: note-only later events involving Sefa, identification and departure are not assigned transcript links. Prior date and identity uncertainties remain in the session reviews. Quoted ASR wording is preserved.

Validation checks source hashes, all source coverage, typed scenes, NPC/item joins, complete ranges, exact quote text and attribution fields, multiple featured quote joins, and one overview per entity. The builder also checks that all accepted NPC interaction bounds and scene boundaries exactly match v2. Local line links remain the navigation mechanism; no web runtime is changed.

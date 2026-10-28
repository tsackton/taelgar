# Campaign interaction trials — version 4 (superseded experiment)

The active workflow is transcript-only. Use the [v3 baseline](../v3/README.md). These mixed-source results and their validator are retained only as a historical experiment; note-only additions are not part of the current extraction. The format used here is preserved in [format-v4.md](format-v4.md).

[Skill](../../../.agents/skills/extract-campaign-interactions/SKILL.md) · [Format](../../../.agents/skills/extract-campaign-interactions/references/format.md)

Session notes now contribute documented events directly to the same NPC and item cards. Each entity still has one session overview. Overlapping accounts enrich the existing encounter; later events get separate scenes. Evidence links distinguish transcript utterances from exact passages in the original notes. Earlier pilots remain intact.

| Session | Scenes | NPCs | Items | Records | Review |
| --- | ---: | ---: | ---: | ---: | --- |
| Mawar 2 | 30 | 18 | 8 | 89 | [Cards](mawar-adventures-002/review.md) · [Evidence](mawar-adventures-002/evidence.md) · [JSON](mawar-adventures-002/extraction.json) |
| Dunmari 8 | 17 | 4 | 1 | 13 | [Cards](dunmari-frontier-008/review.md) · [JSON](dunmari-frontier-008/extraction.json) |
| Dunmari 60 | 21 | 10 | 4 | 31 | [Cards](dunmari-frontier-060/review.md) · [JSON](dunmari-frontier-060/extraction.json) |
| Dunmari 108 | 19 | 11 | 5 | 39 | [Cards](dunmari-frontier-108/review.md) · [JSON](dunmari-frontier-108/extraction.json) |
| Lost in the Feywild 6 | 5 | 8 | 3 | 15 | [Cards](lost-in-the-feywild-006/review.md) · [JSON](lost-in-the-feywild-006/extraction.json) |

Mawar 2 adds the separately documented lair combat and discovery of Sefa, the recovered research books and brass bowl, restitution, Wazir’s August 6 identification, and Azar’s August 9 departure with Benat. The bystander card includes the party tending her after the fight. Reliah’s existing interview record now incorporates the notes’ explicit account of participation, without inventing dialogue. All 13 previously selected quotes remain unchanged.

The note says Sefa was found dead but also describes restitution “to Sefa.” The extraction retains this ambiguity rather than claiming she received money alive. Restitution’s exact date and setting remain uncertain. Azar and Benat’s departure is labeled a documented event: the note establishes it happened, but does not establish a PC witness or farewell.

Dunmari 60 adds the note-confirmed night in Wahacha. Dunmari 108 merges the late conversation into Dimitaur’s existing encounter and adds the documented clairvoyance and long rest. Those scenes do not manufacture NPC presence, an encounter with Ra’ghemdros, cards for generic chimeras, or a next-morning meeting. The complete notes for Dunmari 8 and Feywild 6 yielded no additional eligible note-only encounters.

Mawar’s former scene 26 becomes scene 27 after insertion of the separate lair fight. Its segmentation revision increases to 2; Dunmari 60 and 108 also increase to 2 for added scenes. Unchanged sessions retain revision 1. All accepted v3 transcript encounter ranges and quotes are mechanically checked for preservation during generation.

The validator has 27 passing regression checks covering historical v3 behavior, notes-only input, mixed-source encounters, exact note text and hashes, source-qualified UID collisions, scene containment, duplicate interactions and labeled note-reported dialogue. All five pilots validate. Structural validation does not establish semantic truth; scene dates, entity eligibility and note/transcript reconciliation were also reviewed. Local links are review navigation; no website runtime has changed.

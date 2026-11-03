# Full-read test: Sessions 24 and 39

**The full read is worth making the default for the next skill trial.** It clarifies whether actions actually happened, catches movement buried in combat, and resolves replies whose meaning depends on an earlier question. Keyword searches remain useful as a second-pass checklist. This test supports that workflow recommendation; it does not prove that full reading has perfect recall or outperforms every possible search-and-context workflow.

Both transcripts were read **in full, in source order: 2,968 polished turns**, including players, combat, lore, and table chatter. Each session has the same two time and two location representations as the first pilot: evidence ledgers (A) and derived chronology/spatial graphs (B). These are eight new JSON maps, not eight independent extractions.

| New session | Full read | Main time result | Tables and JSON links |
| --- | --- | --- | --- |
| 24 | 1,320 turns | Two completed nights support May 11–13, conditional on the YAML start date. | [Session 24 review](session-024/review.md) |
| 39 | 1,648 turns | Same-day action fits July 3, with a preceding-night opening prologue and ambiguity about a repeated short-rest reference. | [Session 39 review](session-039/review.md) |

Both source transcripts retain transcription uncertainty. No source transcript, session YAML, canonical note, or installed skill was changed. Civil dates below come from YAML plus relative chronology; neither transcript independently states its current civil date.

## Session 24: two nights, a loop through the desert, parallel scouts

| Relative point | Conditional date / time | Evidence | Interpretation |
| --- | --- | --- | --- |
| Leave Hall of Stories; explore temple | May 11, approaching sunset | u0021–u0032; u0326–u0336; u0671–u0672 | Countdown narrows from roughly 40 minutes to 15–20, then ten. These are overlapping anchors. |
| Return to camp and sleep | May 11 evening → May 12 dawn | u0767–u0784; u0815; u0889–u0895 | First completed overnight. Offered earlier short rest was not taken. |
| Wellby scouts monastery | May 12 early morning | u1164–u1167; u1182–u1183; u1210–u1213 | Twenty-minute outward search and fifteen-minute building check, with a retcon before final return. |
| Ride south, then west/north | May 12, about 3 p.m. → after sunset | u1589–u1602; u1618–u1637 | One continuous riding loop; an extra hour after sunset before camp. |
| Second camp and wake | May 12 night → May 13 before 5 a.m. | u1642–u1655 | Second completed overnight. |
| Reach road and horse shelter | May 13, roughly 9–10 a.m. | u1681–u1714 | About three hours riding, plus unquantified preparation. Do not force wake-time arithmetic. |
| Reach bridge; scouts operate in parallel | Approach before noon; later clock unstated | u1907–u1910; u2173–u2177; u2328–u2332; u2452–u2463 | Seeker observes palace remotely while Delwath explores northern ruins for about twenty minutes. |
| Reunite at bridge | Same day; exact time unknown | u2461–u2463; u2492–u2495 | Westward departure is deferred to next session; return to horses is not established. |

The spatial map distinguishes the temple foyer, entry chapel, main chamber and side corridor; both overnight camps; the southern turnaround; horse shelter; bridge; northern city ruins, market and glass shop; and remotely observed palace. The horse shelter is especially useful for future whereabouts work: horses and Baxter remain there while the party advances.

**Full-read distinctions:** “Hmm, ten” needs the preceding sunset question. “Yeah … Yep” accepts the ten-minute preparation. The uncompleted short-rest offer must not add an hour. Wellby’s explicit retcon inserts observations into one scouting trip. Delwath’s city visit runs during Seeker’s two spells, even though it is narrated afterward. Grash’s throne-room presence is observed remotely and is not a party visit.

## Session 39: boundary framing, canceled travel, combat movement

| Relative point | Conditional date / time | Evidence | Interpretation |
| --- | --- | --- | --- |
| Sleep-to-wake opening | Prior night → July 3 pre-dawn | u0001–u0014 | One narrated opening overnight, kept outside the main wake-to-close span. |
| Check lair | July 3, still dark | u0121–u0135 | Party checks city-side entrance, despite initially discussing outside tunnel exit. |
| Tunnel, then northbound trail | Dawn, then about two hours | u0347–u0381 | Two roughly hour-long travel legs toward fort. |
| Scout tower; fight; rescue Riswynn | Later morning; no precise clock | u0528–u0558; u0735–u0739; u1740–u1908 | Riswynn physically enters mist and returns; no planar crossing is established. |
| Retreat and interrogate | Later same day | u2113–u2191; u2204–u2236 | Stop away from tower; accepted short rest overlaps interrogation. |
| Compressed return to Tokra | Same day; arrival clock unstated | u2676–u2687 | Return accepted as a hand-wave; closing long-rest suggestion replaced by short rest / hit dice. |
| Set up next session | Same-day northbound goal | u2691–u2694; u2765–u2775 | Riswynn intends to stay in town; four companions intend to go north. Neither Saka nor the Laka monks’ tower is reached. |

**Full-read distinctions:** The archive detour is explicitly canceled when the DM agrees the party kept the map. Kenzo’s pursuit behind the tower and Riswynn’s mist entry/rescue occur inside lengthy combat. “11:45,” “45 minutes,” and “15 minutes” near the end refer to table scheduling. The closing short-rest recovery may repeat the already completed rest or represent another one; the map retains both readings instead of adding two hours automatically.

The YAML result depends on an explicit boundary rule. If session dates cover current play beginning at the wake-up, July 3 → July 3 fits. If they cover the first literal narrated instant, the opening also includes the previous night. This is a convention to settle for the skill, not sufficient reason to edit the YAML automatically.

## Comparison with candidate searching

The baseline was frozen before full reading using the first pilot’s keyword pattern. It is **a deterministic filter baseline, not a separately completed candidate-led extraction**. The first pilot also used expanded context and supplementary searches; these numbers must not be presented as its recall score. A partial Session 24 candidate preview preceded the full read, so this was not a blinded experiment.

| Selection rule | Session 24 turns | Session 39 turns | Authored markers with no cited turn selected |
| --- | --- | --- | --- |
| Keyword matches only | 298 / 1,320 | 155 / 1,648 | 9 across both sessions: 2 time, 7 location |
| Matches plus two neighboring turns each side | 852 | 568 | 1 |
| Matches plus five neighboring turns each side | 1,143 | 930 | 0 |
| Full sequential read | 1,320 | 1,648 | 0 |

Context expansion helps substantially: a bare numerical answer alone does not justify requiring full reading. But selecting **some** evidence for a marker is not enough to recover its entire meaning. Even the five-neighbor rule leaves some cited evidence outside selection for sixteen markers. Some citations are redundant or supporting context; neither figure is a count of proven missed events. Full reading also helps recognize decisions spread over long discussions, corrected destinations, and concurrent action.

Examples with **no raw keyword match in any cited turn** include the horse shelter / Baxter staying behind (24, l22), canceled archive visit (39, l04), Kenzo’s prisoner pursuit (39, l10), and agreed compressed return to town (39, t19/l20). The last example appears in both maps and is one event, not two independent discoveries. [Detailed comparison](candidate-comparison.json) records every marker’s cited turn coverage and the context-window sensitivity check.

## What I would change for the next skill trial

1. Require a complete sequential read before extraction is considered complete. Record actual read windows and source fingerprints; a search over all turns is not a full read.
2. Resolve question/answer pairs, accepted proposals, corrections and retcons before assigning elapsed time or visits. Source order and event order can differ.
3. Read combat for meaningful place changes, actor splits and thresholds, without turning every five-foot move into a map row.
4. Audit opening framing, completed in-session nights and closing intentions separately. Do not infer nights from long-rest mechanics alone.
5. Keep repeated-rest and compressed-return ambiguities explicit. Completed travel, accepted hand-waves and next-session plans need different completion labels.
6. Preserve reported historical routes and remotely observed NPC presence in the spatial graph. This trial adds separate collections for them, since they should neither disappear nor become party visits.

I would retain **two extraction skills, with A as evidence and B as the derived view**. These full-read tests exercise the draft instructions on new material, but are not independent agent tests. No draft or installed skill was rewritten in this follow-up; the proposed adjustments are captured here and in the [protocol/addendum](protocol.md).

## Audit trail

[Sampling record](sample.json) documents a seeded random draw of Sessions 24 and 39 from 131 eligible sessions after excluding the original five. No redraws. [Coverage](coverage.json) records all read windows. [Validation](validation.json) checks exact evidence quotations, UID ranges, unchanged source/YAML hashes, graph references, night arithmetic and concrete failure modes. There are **53 time markers, 54 location markers and 44 local place nodes**, with 327 reused evidence references; these are not independent-observation counts.

Full tables are Markdown; no new browser preview is required. The original five-session artifacts remain intact. [Working notes](../notes.md) record discoveries and limitations.

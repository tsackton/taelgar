# v6 sample findings

Start with the [entity review directory](README.md). These are new extractions from the two currently registered polished transcript bundles: Dunmar 10 and 41. This availability sample exercises the YAML-integrated workflow; it is not a representative cross-campaign sample.

| Session | Scenes | NPCs | Items | Organizations | Interactions | Quotes | Excluded blocks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Dunmar 10](../../dunmar-frontier/dunmari-frontier-010/interactions/review.md#entity-list) | 36 | 4 | 2 | 3 | 14 | 14 | 3 |
| [Dunmar 41](../../dunmar-frontier/dunmari-frontier-041/interactions/review.md#entity-list) | 25 | 42 | 11 | 7 | 87 | 20 | 4 |

## Useful feedback targets

- **Session 10:** Vola’s rescue/debrief and multiple pull quotes; a distinctive unnamed speaking orc; two useful items (logbook and discovered scroll). Generic creatures, ordinary treasure and routine gear do not receive cards.
- **Session 41:** a larger social/research cast with historical and religious mentions. Check whether this breadth of mentioned entities is useful, whether whole conversations remain coherent, and whether the 11 story-relevant items merit inclusion.
- **Exclusions:** every omitted transcript block has a source range and reason in both the review page and processing data. Minor interjections remain within scenes where appropriate.
- **Dates:** reviewers found no clear contradiction with YAML. The later Session 41 scenes retain uncertain timing; the YAML’s longer date span is preserved.

## What independent review changed

Each extraction had a different reviewer who independently read the full transcript before inspecting the draft. Both used one correction/recheck pass. The tools validated provenance, coverage and replay; agents made the semantic judgments. No human-reviewed status was assigned.

- Session 10: corrected a scene description to identify the overhead passage between towers. Retained entity and interaction records were supported. Arcus’s reported death stays attributed to Wellby; it is not promoted to an omniscient claim.
- Session 41: corrected creator-tradition attribution; merged one split discussion; removed a culture incorrectly classified as an organization; corrected keepsake custody and prospective execution wording; strengthened location/document matches; and expanded several overviews to cover the whole session.

The optional Session 10 beat summaries were consulted only during review as omission hints, with findings checked against the transcript. No beat-derived event or date became canonical by itself.

## Artifacts and provenance

Each source session bundle contains its own `interactions/session.json`, `session-processing-data.json`, `review.md` and critical queue. The session YAML points to both JSON files with relative paths. This trial directory contains navigation, sampling metadata and review notes, without another copy of canonical session JSON.

All 5,136 original UIDs are accounted for: 5,081 in scenes and 55 in seven excluded blocks. Cleaned and polished transcript bytes are unchanged. YAML gained only the output-pointer block; dates and source declarations were preserved. Twelve existing ancillary-path issues remain informational proposals, six per session; registered extraction sources are valid.

[Sample and eligibility record](sample.json) · [Batch audit status](batch-status.json)

[Session 10 initial review notes](review-notes/dunmari-frontier-010-review-0.json) · [Session 10 recheck](review-notes/dunmari-frontier-010-review-1.json)

[Session 41 independent source ledger](review-notes/dunmari-frontier-041-source-ledger.json) · [Initial review notes](review-notes/dunmari-frontier-041-review-0.json) · [Recheck](review-notes/dunmari-frontier-041-review-1.json)

These are local review materials on `codex/campaign-interactions-review`. They do not update the Taelgarverse application or establish calibrated confidence rates.

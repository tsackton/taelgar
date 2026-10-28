# Automatic transcript cleanup

Session: <code>dunmari-frontier-060</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 30 | 3 | 4 | 0 | 1 | 22 | 23 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>theba</code> | high | <code>u0002:m1</code> | <code>{{Phoeba}}</code> | <code>Theba</code> | The opening identifies the guide leaving the Te&#x27;kula refuge; the character note and matching prequel establish Theba. | <code>People/Deno&#x27;qai/Theba.md</code>, <code>_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Prequel - Wellby.md</code> | no |
| <code>quanyi</code> | supported | <code>u0860:m1</code> | <code>{{me say}}</code> | <code>Quanyi</code> | The first occurrence refers to the people of the anchored salt-producing island under discussion; the second explicitly describes its rotation. Quanyi is uniquely supported by the island note and session record despite the damaged phonetic forms. | <code>Gazetteer/Eastern Green Sea/Quanyi.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 60 (DuFr).md</code> | no |
| <code>sea-elves</code> | supported | <code>u0866:m1</code> | <code>{{seals}}</code> | <code>sea elves</code> | The discussion concerns the unusual island inhabitants associated with magical salt and possible Feywild knowledge. The island reference and session record identify sea elves; literal seals do not fit the ensuing contrast with merfolk. | <code>Gazetteer/Eastern Green Sea/Quanyi.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 60 (DuFr).md</code> | no |
| <code>sea-elves</code> | supported | <code>u0882:m2</code> | <code>{{Ceos}}</code> | <code>sea elves</code> | The discussion concerns the unusual island inhabitants associated with magical salt and possible Feywild knowledge. The island reference and session record identify sea elves; literal seals do not fit the ensuing contrast with merfolk. | <code>Gazetteer/Eastern Green Sea/Quanyi.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 60 (DuFr).md</code> | no |
| <code>quanyi</code> | supported | <code>u0905:m1</code> | <code>{{calling me}}</code> | <code>Quanyi</code> | The first occurrence refers to the people of the anchored salt-producing island under discussion; the second explicitly describes its rotation. Quanyi is uniquely supported by the island note and session record despite the damaged phonetic forms. | <code>Gazetteer/Eastern Green Sea/Quanyi.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 60 (DuFr).md</code> | no |
| <code>eastros</code> | high | <code>u0932:m1</code> | <code>{{Easter}}</code> | <code>Eastros</code> | The crew teaches the eastern trade language during this journey; the session record explicitly names Eastros and the language reference confirms the spelling and regional use. | <code>Background/Languages.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 60 (DuFr).md</code> | no |
| <code>eastros</code> | high | <code>u0934:m1</code> | <code>{{Easter}}</code> | <code>Eastros</code> | The crew teaches the eastern trade language during this journey; the session record explicitly names Eastros and the language reference confirms the spelling and regional use. | <code>Background/Languages.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 60 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>possible-wella-in-damaged-phrase</code> | <code>u0750:m1</code> | <code>{{Well, that signs well up there.}}</code> | <code>Wella</code> | The opening may contain the captain name Wella, but the marker also encloses damaged ordinary wording. A complete name-only replacement cannot preserve the whole span without reconstructing the phrase. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0061:m1</code>, <code>u0072:m1</code>, <code>u0089:m1</code>, <code>u0112:m1</code>, <code>u0156:m1</code>, <code>u0192:m1</code>, <code>u0289:m1</code>, <code>u0438:m1</code>, <code>u0484:m1</code>, <code>u0491:m1</code>, <code>u0544:m1</code>, <code>u0656:m1</code>, <code>u0696:m1</code>, <code>u0849:m1</code>, <code>u0853:m1</code>, <code>u0882:m1</code>, <code>u1027:m1</code>, <code>u1046:m1</code>, <code>u1073:m1</code>, <code>u1076:m1</code>, <code>u1118:m1</code>, <code>u1221:m1</code> | Ordinary dialogue, arithmetic, combat rules, descriptive wording, or damaged multiword wording rather than a complete resolvable name span. This includes the longer kenku-related phrase, whose connective wording cannot be repaired in a names-only pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-060/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T040811197127Z-2f6dd41e/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-060/cleaned/dunmari-frontier-060-source-cleaned.md</code>
Before SHA-256: <code>83268a8e4fa8e6753b6f6e35dfd4d48ae5c100fd6519f92eb5b8cc805f9ab6a5</code>
Planned after SHA-256: <code>8abd3dec628a9365aa6348783d7a11d33d555cb9b6dbea9e4a8abb94ecf38b84</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

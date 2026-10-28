# Automatic transcript cleanup

Session: <code>dunmari-frontier-024</code>
Status: <code>reviewed_no_changes</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 15 | 0 | 0 | 0 | 4 | 11 | 15 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | No replacements. | — | — |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>bridge-referent</code> | <code>u1949:m1</code> | <code>{{herself}}</code> | <code>Bhishma</code> | Bhishma is a plausible subject in the early-Dunmari bridge discussion, but the marked span contains only a pronoun. The sources do not establish which name, if any, was spoken; adding a name or reconstructing a name-plus-pronoun phrase would exceed the complete-name replacement boundary. |
| <code>eudomes-mirror-phrase</code> | <code>u2344:m1</code> | <code>{{and you dumb as these mirror}}</code> | <code>Eudomes&#x27; mirror</code> | The plan to retrieve an object for viewing its history strongly favors Eudomes&#x27; mirror. The full marker also contains unclear connecting wording, possibly a preposition; replacing it with the item name alone would discard or reconstruct that wording. Retain the whole span. |
| <code>grash-closing-phrase</code> | <code>u2489:m1</code> | <code>{{saga rush}}</code> | <code>Grash</code> | The closing reaction to scouting strongly favors a reference to Grash, possibly a phrase such as saw Grash. The marked span includes unclear ordinary wording and cannot be replaced with only the name without changing the phrase. |
| <code>sensor-position-phrase</code> | <code>u2223:m1</code> | <code>{{line is six this scroll near Grash’s head}}</code> | <code>Grash</code> | Grash is already spelled correctly inside a longer damaged sentence about positioning the clairvoyance sensor. Resolving the complete marked span would require reconstructing ordinary wording, so the entire span is retained. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0099:m1</code>, <code>u0260:m1</code>, <code>u0392:m1</code>, <code>u0450:m1</code>, <code>u0580:m1</code>, <code>u0639:m1</code>, <code>u0672:m1</code>, <code>u1293:m1</code>, <code>u2024:m1</code>, <code>u2357:m1</code>, <code>u2474:m1</code> | Damaged ordinary speech about healing, movement, feelings, invisibility, watching the shadow, sunset timing, orc activity, weapon appearance, collecting objects, and possible traps. No complete name or setting-term replacement is supported within these marker boundaries; wording and mechanics reconstruction are outside names-v1. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-024/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T034132907898Z-7bdc4ba5/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-024/cleaned/dunmari-frontier-024-source-cleaned.md</code>
Before SHA-256: <code>4be912e03e4f3e87abfdc5d0067728cf1393b41bf2d063573ceded58c50f99df</code>
Planned after SHA-256: <code>4be912e03e4f3e87abfdc5d0067728cf1393b41bf2d063573ceded58c50f99df</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

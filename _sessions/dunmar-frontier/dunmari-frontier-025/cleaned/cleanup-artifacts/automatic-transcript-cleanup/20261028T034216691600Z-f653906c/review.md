# Automatic transcript cleanup

Session: <code>dunmari-frontier-025</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 19 | 0 | 1 | 0 | 2 | 16 | 18 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>grash-warning</code> | supported | <code>u2188:m1</code> | <code>{{roshan}}</code> | <code>Grash</code> | Kenzo is warning the monks about the same commander he names twice in this sentence; the surrounding exchange explicitly discusses their reaction to Grash. The reference and scrying record establish Grash. The isolated phonetic form is less clear, but this context strongly favors Grash over an unrelated identity. | <code>People/Other Nonhumans/Grash.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Scrying and Spying/Grash May 13th.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>grash-description-fragment</code> | <code>u0352:m1</code> | <code>{{grave can}}</code> | — | The fragment follows a description of Grash and may contain a title or ordinary descriptive wording. The inspected reference establishes Grash the Undying but does not establish a matching Grave King title; the complete replacement is uncertain. |
| <code>monastery-people-fragment</code> | <code>u0340:m1</code> | <code>{{A man and Dudes}}</code> | <code>Karmana</code> | This refers generally to people encountered at the monastery. Karmana is plausible, but the complete marked phrase also contains unclear surrounding wording; replacing it with a name would reconstruct or discard that wording. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0049:m1</code>, <code>u0093:m1</code>, <code>u0121:m1</code>, <code>u0165:m1</code>, <code>u0241:m1</code>, <code>u0242:m1</code>, <code>u0843:m1</code>, <code>u1023:m1</code>, <code>u1089:m1</code>, <code>u1158:m1</code>, <code>u1270:m1</code>, <code>u1606:m1</code>, <code>u1796:m1</code>, <code>u1982:m1</code>, <code>u2204:m1</code>, <code>u2216:m1</code> | These are damaged ordinary descriptions, dialogue, gestures, travel distances, or combat and rules wording. Context does not establish a complete name or setting-term replacement; repairing them would require prose or mechanics reconstruction outside names-v1. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-025/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T034216691600Z-f653906c/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-025/cleaned/dunmari-frontier-025-source-cleaned.md</code>
Before SHA-256: <code>45f068b3b84bfb181eb0a9c248e1f8f0b42b52d98f0d2019591f817b4f2bfb6d</code>
Planned after SHA-256: <code>78ceb89be0a3032a94c1ebd62f49bf096939bda12d06da35e1a1dc3dc867a164</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

# Automatic transcript cleanup

Session: <code>dunmari-frontier-130</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 22 | 2 | 1 | 0 | 1 | 18 | 19 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>leizar</code> | high | <code>u0279:m1</code> | <code>{{Lazar}}</code> | <code>Leizar</code> | The young lizardfolk with fishing gear introducing himself to Seeker matches Leizar in the reference note and this session record; Elazar is a different adult spirit guide. | <code>People/Lizardfolk/Leizar.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 130 (DuFr).md</code> | no |
| <code>tanshi</code> | high | <code>u1443:m1</code> | <code>{{Tatanshi}}</code> | <code>the tanshi</code> | The suggestion follows discussion of augury and consulting gods; the complete marked sound is the established term with its article, the tanshi. | <code>Gods and Religions/Gods/Tanshi/Tanshi.md</code> | no |
| <code>chaos-metals</code> | supported | <code>u1606:m1</code> | <code>{{Awesome medals}}</code> | <code>Chaos metals</code> | The discussion concerns the mutable metal forming the centipede and the danger of it adhering to Vindristjarna; Chaos metals is the strongly favored term, preserving the apparent plural. Ordinary awesome medals does not fit this material discussion. | <code>Things/Materials/Chaos Metal.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>isolated-kharkov</code> | <code>u1167:m1</code> | <code>{{Kharkov}}</code> | <code>Heartroot</code> | This isolated word occurs during discussion of the living Heartroot and stories of Isingue, but neither the sound nor sentence boundary securely identifies a complete name replacement; it may instead be damaged ordinary wording. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0143:m1</code>, <code>u0231:m1</code>, <code>u0311:m1</code>, <code>u0464:m1</code>, <code>u0509:m1</code>, <code>u0733:m1</code>, <code>u1093:m1</code>, <code>u1163:m1</code>, <code>u1182:m1</code>, <code>u1199:m1</code>, <code>u1222:m1</code>, <code>u1494:m1</code>, <code>u1610:m1</code>, <code>u2153:m1</code>, <code>u2220:m1</code>, <code>u2220:m2</code>, <code>u2309:m1</code>, <code>u2609:m1</code> | These spans contain ordinary dialogue, descriptive phrases, grammar, numbers, or rules discussion rather than recoverable names or setting terms; repairing them would require wording reconstruction outside names-v1. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-130/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T045405866243Z-3238dc7a/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-130/cleaned/dunmari-frontier-130-source-cleaned.md</code>
Before SHA-256: <code>93b0ff0bb117aa8da5c148b51cabba7133bda380953e70e61417f93b197dba91</code>
Planned after SHA-256: <code>86234f70e96671074fe2b796decb21782c57ab2c0f2d0081abc96fe68b96a618</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

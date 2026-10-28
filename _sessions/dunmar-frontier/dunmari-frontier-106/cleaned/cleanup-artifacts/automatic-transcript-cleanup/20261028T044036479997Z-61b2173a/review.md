# Automatic transcript cleanup

Session: <code>dunmari-frontier-106</code>
Status: <code>reviewed_no_changes</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 17 | 0 | 0 | 0 | 2 | 15 | 17 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | No replacements. | — | — |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>incomplete-position-reference</code> | <code>u0525:m1</code> | <code>{{a}}</code> | <code>Seeker</code> | The point is discussed in relation to Kenzo and Seeker, but the single marked syllable does not establish the missing referent; Seeker, another participant, or an unfinished utterance remain possible. Retain rather than infer a battle-map position. |
| <code>possible-spoken-name-mistake</code> | <code>u1122:m1</code> | <code>{{Delwath}}</code> | <code>Delwath</code>, <code>Wellby</code> | Delwath is an established participant, but the immediately preceding action has Delwath block the vine and Wellby be hit and dragged close. The marked name could be a spoken mistake rather than an ASR error; retain it rather than substitute the factually expected name or silently remove the uncertainty. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0253:m1</code>, <code>u0259:m1</code>, <code>u0464:m1</code>, <code>u0483:m1</code>, <code>u0878:m1</code>, <code>u0945:m1</code>, <code>u0974:m1</code>, <code>u1041:m1</code>, <code>u1355:m1</code>, <code>u1428:m1</code>, <code>u2001:m1</code>, <code>u2064:m1</code>, <code>u2237:m1</code>, <code>u2298:m1</code>, <code>u2533:m1</code> | These spans concern ordinary wording, turn cues, damage statements, numbers, or mechanics. The fragments Will be fixed and Harold occur in damage and turn-transition dialogue, with Wellby already identified; repairing either complete phrase would reconstruct ordinary speech rather than resolve a standalone name. No wording is reconstructed in this pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-106/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T044036479997Z-61b2173a/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-106/cleaned/dunmari-frontier-106-source-cleaned.md</code>
Before SHA-256: <code>2297f5b79da2bd06c6222e6fe47f006d7fa45ebb31d7a92f996ab51b3cb34ec8</code>
Planned after SHA-256: <code>2297f5b79da2bd06c6222e6fe47f006d7fa45ebb31d7a92f996ab51b3cb34ec8</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

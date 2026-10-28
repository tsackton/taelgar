# Automatic transcript cleanup

Session: <code>dunmari-frontier-009</code>
Status: <code>reviewed_no_changes</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 5 | 0 | 0 | 0 | 1 | 4 | 5 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | No replacements. | — | — |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>unclear-family-reference</code> | <code>u0477:m1</code> | <code>{{during his can never said anything about like}}</code> | <code>Eberk</code> | The discussion concerns Riswynn’s elder relative and the flight from the outpost. Eberk is a possible referent, but the marked clause does not isolate a recognizable name and cannot be replaced wholly with a name without reconstructing ordinary wording. Retain the complete span. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0036:m1</code>, <code>u0223:m1</code>, <code>u0821:m1</code>, <code>u0834:m1</code> | These spans contain damaged descriptive or bargaining clauses, rather than complete recoverable names or setting terms. The possible creature reference within u0821 is embedded in an unrecoverable sentence; resolving it would require prose reconstruction. Retain the wording and markers. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-009/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T033833315147Z-90c7f0f2/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-009/cleaned/dunmari-frontier-009-source-cleaned.md</code>
Before SHA-256: <code>536febf5277dc15c6cfd3d86b0225cc6b6208c4f389978ec716e0da523f9b646</code>
Planned after SHA-256: <code>536febf5277dc15c6cfd3d86b0225cc6b6208c4f389978ec716e0da523f9b646</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

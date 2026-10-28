# Automatic transcript cleanup

Session: <code>dunmari-frontier-023</code>
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
| <code>question-embedded-name</code> | <code>u0162:m1</code> | <code>{{last word before beach about was}}</code> | <code>Bhishma</code>, <code>Shakun</code> | The dialogue concerns asking Bhishma about Shakun. The marked phrase may contain a deity name, but its remaining wording and boundaries are unrecoverable as a complete name-only span; retain it whole. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>opening-damaged-wording</code> | <code>u0005:m1</code>, <code>u0006:m1</code> | Damaged opening narration and fragmentary ordinary wording; neither span identifies a name or setting term. Reconstructing these phrases is outside the names pass. |
| <code>stone-surface-wording</code> | <code>u0198:m1</code> | This asks whether the reddish ochre stone has one surface or a rough one. The session account and artifact note establish the object, but do not make shadow stone an established term here; repairing the descriptive adjective is outside this pass. |
| <code>vision-description-wording</code> | <code>u2011:m1</code> | Damaged descriptive wording while reading a vision of multicolored space, without a recoverable name or setting-term span. Source-reading phrase reconstruction is outside this pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-023/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T034051329727Z-ee1220db/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-023/cleaned/dunmari-frontier-023-source-cleaned.md</code>
Before SHA-256: <code>3c847318fe6fab417c8c1ce5b82adde42789334844f72fd0ee1fecfe6219a132</code>
Planned after SHA-256: <code>3c847318fe6fab417c8c1ce5b82adde42789334844f72fd0ee1fecfe6219a132</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

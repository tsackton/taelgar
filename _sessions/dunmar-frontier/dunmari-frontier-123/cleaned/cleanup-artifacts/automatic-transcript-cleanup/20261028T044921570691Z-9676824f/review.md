# Automatic transcript cleanup

Session: <code>dunmari-frontier-123</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 0 | 1 | 0 | 1 | 14 | 15 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>amberglow</code> | supported | <code>u0089:m1</code> | <code>{{every. Well}}</code> | <code>Amberglow</code> | The discussion concerns the Prismwell manifesting in the surrounding realm after the beacon is lit. Amberglow is the uniquely supported realm; the damaged recognition is less certain than the contextual identity. | <code>Gazetteer/Extraplanar/Feywild/Amberglow/Amberglow.md</code>, <code>Gazetteer/Extraplanar/Feywild/Amberglow/Prismwell.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 123 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>rider-name</code> | <code>u0562:m1</code> | <code>{{Kenzo&#x27;s}}</code> | <code>Kenzo</code>, <code>Delwath</code> | Kenzo is an established participant, but the preceding mount allocation places him on the wyvern and Delwath on a griffin. This may be a spoken name mix-up rather than an ASR error; substituting Delwath or unmarking Kenzo would resolve that uncertainty without sufficient evidence. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>mount-wording</code> | <code>u0614:m1</code>, <code>u0755:m1</code> | Generic creature and mount wording, rather than a proper name or conventional named item. The griffin reference conflicts with Wellby&#x27;s preceding wyvern mount and may be spoken imprecision; the later Wyvern&#x27;s wording also has unclear referent. Repairing these would change ordinary narration. |
| <code>ordinary-wording</code> | <code>u0209:m1</code>, <code>u0225:m1</code>, <code>u0462:m1</code>, <code>u0546:m1</code>, <code>u0632:m1</code>, <code>u0638:m1</code>, <code>u0710:m1</code>, <code>u0877:m1</code>, <code>u1110:m1</code>, <code>u1119:m1</code>, <code>u1169:m1</code>, <code>u1239:m1</code> | Ordinary descriptive wording, dialogue, and damaged phrases outside the names-only pass; no complete marked name or setting term is recoverable within these spans. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-123/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T044921570691Z-9676824f/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-123/cleaned/dunmari-frontier-123-source-cleaned.md</code>
Before SHA-256: <code>585b021cc985e38f9bcfc5a9bc7de520f8a1de3f7332e5649f4e75865bc2014e</code>
Planned after SHA-256: <code>62d5d4bfa750a4ebf0a7b4b40bbad15d445de1eafc95499d81e73ac360d07903</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

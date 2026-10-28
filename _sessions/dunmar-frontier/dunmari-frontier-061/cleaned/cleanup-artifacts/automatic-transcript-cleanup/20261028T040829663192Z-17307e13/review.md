# Automatic transcript cleanup

Session: <code>dunmari-frontier-061</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 1 | 0 | 0 | 2 | 13 | 15 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>chasa-river-valley</code> | high | <code>u0696:m1</code> | <code>{{chaos and River valley}}</code> | <code>Chasa River Valley</code> | The speaker places the missing rabbit near Chardon; the canonical regional and river notes establish Chasa River Valley as the matching named valley. | <code>Gazetteer/Greater Chardon/Chardonian Empire/Chasa River Valley/Chasa River Valley.md</code>, <code>Gazetteer/Major Rivers/Chasa-Nahadi Watershed/Chasa.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>possible-prince-address</code> | <code>u1055:m1</code> | <code>{{Footprints}}</code> | <code>Prince</code> | The dialogue addresses the Prince of Luck, so a form of Prince is plausible, but Footprints could represent a longer question or ordinary wording. The source establishes the interlocutor without establishing the complete spoken span. |
| <code>scroll-name-in-damaged-phrase</code> | <code>u0657:m1</code> | <code>{{detectivity, which is, if i&#x27;m out with you}}</code> | <code>Detect Magic</code> | Detect Magic is plausible given the discussion and recorded scroll, but the complete marked span includes unrecoverable ordinary wording. A name-only replacement would delete that wording. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0108:m1</code>, <code>u0165:m1</code>, <code>u0230:m1</code>, <code>u0484:m1</code>, <code>u0524:m1</code>, <code>u0649:m1</code>, <code>u0656:m1</code>, <code>u0697:m1</code>, <code>u0918:m1</code>, <code>u0980:m1</code>, <code>u1078:m1</code>, <code>u1154:m1</code>, <code>u1171:m1</code> | These spans are ordinary dialogue, descriptive wording, table chatter, or rules explanations rather than resolvable names or setting terms. Repairing them would require wording reconstruction outside this pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-061/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T040829663192Z-17307e13/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-061/cleaned/dunmari-frontier-061-source-cleaned.md</code>
Before SHA-256: <code>7575b46678762ae792c9c105ecf207ec8e9672abb34eb866b296eb5dcf94b264</code>
Planned after SHA-256: <code>c041224bb9ee82d7737dc945c7b0e1917fd7c24fbde852a184bff31479653bbd</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

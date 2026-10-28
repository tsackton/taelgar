# Automatic transcript cleanup

Session: <code>dunmari-frontier-112</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 8 | 2 | 2 | 0 | 0 | 4 | 4 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>skyship-opening</code> | supported | <code>u0004:m1</code> | <code>{{vendor side}}</code> | <code>Vindristjarna</code> | The opening locates the party aboard their skyship immediately before teleporting into Drankor. Session 111 establishes this starting position aboard Vindristjarna; the phonetic rendering is weaker than the later explicit ship references. | <code>Things/Ships/Vindristjarna.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 111 (DuFr).md</code> | no |
| <code>skyship-name</code> | high | <code>u0153:m1</code> | <code>{{Vindicarda}}</code> | <code>Vindristjarna</code> | Both occurrences explicitly refer to the party skyship, including its threatened crash and its feigned attack. The ship reference establishes Vindristjarna as the complete name. | <code>Things/Ships/Vindristjarna.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 111 (DuFr).md</code> | no |
| <code>skyship-name</code> | high | <code>u0159:m1</code> | <code>{{Vendra Sharna}}</code> | <code>Vindristjarna</code> | Both occurrences explicitly refer to the party skyship, including its threatened crash and its feigned attack. The ship reference establishes Vindristjarna as the complete name. | <code>Things/Ships/Vindristjarna.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 111 (DuFr).md</code> | no |
| <code>elf-adviser</code> | supported | <code>u4326:m1</code> | <code>{{Rs Day}}</code> | <code>Arheste</code> | The discussion concerns the elf who advised the party about Apollyon and his phylactery; the following dialogue explicitly identifies her as the elf. Arheste is the documented adviser in Session 87, and her name fits the marked phonetic form. Aristaea is a different stoneborn companion and does not fit that role. | <code>People/Elves/Arheste.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 87 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| — | — | — | — | No name decisions remain. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>fragmented-attack-declaration</code> | <code>u0477:m1</code>, <code>u0478:m1</code> | These adjacent fragments belong to an attack declaration followed by bow, charges, and saving-throw mechanics. Neither marked span establishes a complete recoverable name or item term; joining or reconstructing the wording across lines is outside this pass. |
| <code>fragmented-scrying-wording</code> | <code>u0261:m1</code> | An isolated fragment in a broken recollection of scrying; context does not establish a person or place named Calling. Repairing the surrounding ordinary wording is outside the names pass. |
| <code>fragmented-spell-declaration</code> | <code>u3283:m1</code> | A damaged spell declaration during an attempted escape, followed by counterspell mechanics. Recovering its ordinary wording or a partial spell name would require reconstructing the phrase rather than resolving a complete marked setting term. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-112/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T044146685358Z-b8b65ffe/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-112/cleaned/dunmari-frontier-112-source-cleaned.md</code>
Before SHA-256: <code>dff71df334c48fccea6159a555d03e9b8a89ff271c7cc6a9da28f889d190fb5c</code>
Planned after SHA-256: <code>e6ef2260676cce6a8dee55cb3c92a25c372ad673ec11763b8ddac493d3d0cbe7</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

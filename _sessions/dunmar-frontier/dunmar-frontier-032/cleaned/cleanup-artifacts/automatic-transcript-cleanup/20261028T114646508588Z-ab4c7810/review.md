# Automatic transcript cleanup

Session: <code>dunmar-frontier-032</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 11 | 0 | 7 | 0 | 2 | 2 | 4 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>uzgash-farming-community</code> | supported | <code>u1221:m1</code> | <code>{{Uzgosh}}</code> | <code>Uzgash</code> | The current dialogue identifies the peaceful farming orcs opposed by Grash. Session 21 records the same community under a dismissive label using Uzgash’s name. Normalize the name spelling while preserving the speaker’s shorthand; do not substitute Grash, a settlement, or a new group title. | <code>People/Orcs/Uzgash.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 21 (DuFr).md</code> | no |
| <code>uzgash-farming-community</code> | supported | <code>u1222:m1</code> | <code>{{Uzgosh}}</code> | <code>Uzgash</code> | The current dialogue identifies the peaceful farming orcs opposed by Grash. Session 21 records the same community under a dismissive label using Uzgash’s name. Normalize the name spelling while preserving the speaker’s shorthand; do not substitute Grash, a settlement, or a new group title. | <code>People/Orcs/Uzgash.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 21 (DuFr).md</code> | no |
| <code>uzgash-farming-community</code> | supported | <code>u1223:m1</code> | <code>{{Uzgosh}}</code> | <code>Uzgash</code> | The current dialogue identifies the peaceful farming orcs opposed by Grash. Session 21 records the same community under a dismissive label using Uzgash’s name. Normalize the name spelling while preserving the speaker’s shorthand; do not substitute Grash, a settlement, or a new group title. | <code>People/Orcs/Uzgash.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 21 (DuFr).md</code> | no |
| <code>avatus-emperor</code> | supported | <code>u1707:m1</code> | <code>{{Avitus}}</code> | <code>Avatus</code> | The mirror-maker’s imperial patron, associated with the Sembaran defeat, uniquely matches Avatus. The two Avitus forms precede the later explicit pronunciation correction; treat these as likely recognition drift. Retain the immediately corrected Atavas occurrence separately. | <code>People/Historical Figures/Avatus.md</code> | no |
| <code>avatus-emperor</code> | supported | <code>u1710:m1</code> | <code>{{Avitus}}</code> | <code>Avatus</code> | The mirror-maker’s imperial patron, associated with the Sembaran defeat, uniquely matches Avatus. The two Avitus forms precede the later explicit pronunciation correction; treat these as likely recognition drift. Retain the immediately corrected Atavas occurrence separately. | <code>People/Historical Figures/Avatus.md</code> | no |
| <code>kenzo-initiation-deities</code> | supported | <code>u3939:m1</code> | <code>{{Bishtimala}}</code> | <code>Bhishma, Laka</code> | Both compressed forms strongly favor the two-name list Bhishma, Laka. Kenzo explicitly names Shakun, Bhishma, and Laka earlier in this transcript (u0326); the immediate follow-up supplies Shakun as the missing third god and jokes about listing three gods. Restore only the two complete names inside each marker. | <code>Gods and Religions/Gods/Incorporeal Gods/Dunmari Pantheon/Bhishma.md</code>, <code>Gods and Religions/Gods/Incorporeal Gods/Dunmari Pantheon/Laka.md</code> | no |
| <code>kenzo-initiation-deities</code> | supported | <code>u3940:m1</code> | <code>{{Bishtimela}}</code> | <code>Bhishma, Laka</code> | Both compressed forms strongly favor the two-name list Bhishma, Laka. Kenzo explicitly names Shakun, Bhishma, and Laka earlier in this transcript (u0326); the immediate follow-up supplies Shakun as the missing third god and jokes about listing three gods. Restore only the two complete names inside each marker. | <code>Gods and Religions/Gods/Incorporeal Gods/Dunmari Pantheon/Bhishma.md</code>, <code>Gods and Religions/Gods/Incorporeal Gods/Dunmari Pantheon/Laka.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>avatus-spoken-correction</code> | <code>u1784:m1</code> | <code>{{Atavas}}</code> | <code>Avatus</code> | The next turn explicitly restarts and supplies Avatus, making an actual spoken misnaming plausible. Preserve the original marked wording rather than replacing a possible spoken mistake. |
| <code>misremembered-dynasty</code> | <code>u1801:m1</code> | <code>{{House of Darick}}</code> | <code>House of Derik</code>, <code>House of Sewick</code> | The previous turn names Derik II, and the speaker then says House of Darick. The established dynasty is Sewick, but substituting the historically correct house could erase a spoken mistake. Preserve the whole marked phrase. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>damaged-object-source-phrase</code> | <code>u1327:m1</code> | The illustrative object-source phrase is damaged ordinary wording, without a uniquely recoverable whole-span name replacement. Reconstructing it as a phrase about Agata would exceed this names pass. |
| <code>politics-false-start</code> | <code>u3568:m1</code> | The surrounding sentence explicitly discusses Dunmari politics. The marked false start cannot be replaced with a complete supported name without reconstructing ordinary wording. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmar-frontier-032/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T114646508588Z-ab4c7810/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmar-frontier-032/cleaned/dunmar-frontier-032-source-cleaned.md</code>
Before SHA-256: <code>a7b7b72ca079eb52296a3029d36883266ca488a3048ca3ae5e9b69df48809846</code>
Planned after SHA-256: <code>1f6c4b97de87cf7d408f86dc0bffa2e409347baf65d15cf75599def9ff139e32</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

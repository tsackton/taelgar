# Automatic transcript cleanup

Session: <code>dunmari-frontier-095</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 29 | 3 | 3 | 0 | 4 | 19 | 23 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>tollen-opening</code> | high | <code>u0013:m1</code> | <code>{{Poland}}</code> | <code>Tollen</code> | The opening location and surrounding seasonal description match the session introduction; the city name is Tollen. | <code>_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 95 - DM Notes.md</code>, <code>Gazetteer/Greater Sembara/Tollen/Tollen.md</code> | no |
| <code>vindristjarna-location</code> | supported | <code>u0195:m1</code> | <code>{{ninth}}</code> | <code>Vindristjarna</code> | The question contrasts Baxter being in the mirror with being aboard the party&#x27;s ship; the speaker immediately repeats Vindristjarna as that ship. The reference note fixes the spelling. | <code>Things/Ships/Vindristjarna.md</code> | no |
| <code>tollen-mirror</code> | high | <code>u0519:m1</code> | <code>{{Poland}}</code> | <code>Tollen</code> | The earlier dye-trade mirror vision was viewed in Tollen and depicts the intermediary trade network being recalled. | <code>Campaigns/Dunmari Frontier Campaign/Mirror Visions/Magical Pale Blue Dye Vision.md</code>, <code>Gazetteer/Greater Sembara/Tollen/Tollen.md</code> | no |
| <code>agata-backstory</code> | supported | <code>u1870:m1</code> | <code>{{Akada}}</code> | <code>Agata</code> | Wellby is considering sharing the party&#x27;s prior backstory. Agata is the established hag from that story, linked to the Scepter of Command; the marked phonetic variant strongly favors her name. | <code>People/Fey/Agata.md</code> | no |
| <code>branek-address</code> | supported | <code>u2398:m1</code> | <code>{{Brad}}</code> | <code>Branek</code> | Kenzo is questioning and addressing the dinner host, repeatedly identified in this conversation as Branek. The reference note establishes that name; the short marked form is most plausibly a clipped address to him. | <code>People/Other Humans/Branek Mirov.md</code> | no |
| <code>ludmila-warden</code> | high | <code>u2831:m1</code> | <code>{{Lidmilla}}</code> | <code>Ludmila</code> | The morning attendant is the same elderly warden described earlier; the matching session notes establish her name as Ludmila. | <code>_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 95 - DM Notes.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>ship-defender</code> | <code>u3263:m1</code>, <code>u3263:m2</code> | <code>{{frustrates}}</code>, <code>{{frustrates}}</code> | <code>Faldrak</code> | The ship discussion and following coward remark suggest Faldrak, but the duplicated span could instead be a creature term or a contraction embedded in damaged surrounding wording. His documented ship role does not resolve either complete replacement confidently. |
| <code>southern-city</code> | <code>u0336:m1</code> | <code>{{Zoo City}}</code> | <code>Praznitsky</code> | The route identifies a southern trading city, but the span could be a damaged descriptive phrase rather than a proper name. The geographical candidate does not establish the complete spoken replacement. |
| <code>watcher-question</code> | <code>u2724:m1</code> | <code>{{I used to be in, and}}</code> | <code>Eyes of Vedmakov</code> | This follows discussion of the former Watcher bloodline and may contain an Eyes of Vedmakov reference, but the complete marked phrase and its boundaries are not recoverable as a name alone. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0019:m1</code>, <code>u0250:m1</code>, <code>u0256:m1</code>, <code>u0348:m1</code>, <code>u1271:m1</code>, <code>u1551:m1</code>, <code>u1595:m1</code>, <code>u1701:m1</code>, <code>u1722:m1</code>, <code>u1827:m1</code>, <code>u2296:m1</code>, <code>u2612:m1</code>, <code>u2639:m1</code>, <code>u2728:m1</code>, <code>u2730:m1</code>, <code>u2779:m1</code>, <code>u2851:m1</code>, <code>u2853:m1</code>, <code>u2904:m1</code> | Incidental chatter, damaged descriptive or conversational phrases, food and wine wording, and game mechanics or numbers. Resolving these would reconstruct ordinary wording rather than correct a bounded name or setting term. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-095/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T043544883356Z-41191a6a/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-095/cleaned/dunmari-frontier-095-source-cleaned.md</code>
Before SHA-256: <code>64bed47dea3cfcd8c74f4a109fd22f9f41718ace96df77b591a99482ea1e78a3</code>
Planned after SHA-256: <code>bb32cb7a267a6872a119b650169eccfb7d485e6447c002005aa8be2ab4646176</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

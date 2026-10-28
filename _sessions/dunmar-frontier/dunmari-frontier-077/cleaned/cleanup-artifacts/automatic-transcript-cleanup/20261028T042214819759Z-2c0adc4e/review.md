# Automatic transcript cleanup

Session: <code>dunmari-frontier-077</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 30 | 2 | 2 | 0 | 4 | 22 | 26 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>govir</code> | high | <code>u0072:m1</code> | <code>{{go here}}</code> | <code>Govir</code> | The speaker pairs Ulfgar with the scholar whose letter reports cloak research; the reference note and letter establish Govir. | <code>People/Dunmari/Govir.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Letters and Notes/Letter from Govir.md</code> | no |
| <code>grash</code> | supported | <code>u0210:m2</code> | <code>{{garage the great}}</code> | <code>Grash the great</code> | The cloak is being kept from the attacking commander Grash, discussed throughout this conversation. Preserve the speaker&#x27;s existing words &quot;the great&quot; rather than substitute his documented epithet. | <code>People/Other Nonhumans/Grash.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 77 (DuFr).md</code> | no |
| <code>uzgash-statue</code> | supported | <code>u0952:m1</code> | <code>{{gash}}</code> | <code>Uzgash</code> | The colored statue in the capital&#x27;s civic plaza strongly favors the revered founder Uzgash. The reference notes establish his identity and the city&#x27;s commemorative imagery; Grash is the contemporary attacker, a different contextual referent. | <code>People/Orcs/Uzgash.md</code>, <code>Gazetteer/Upper Istaros/Xurkhaz/Uzgukhar.md</code> | no |
| <code>rishi</code> | high | <code>u1746:m3</code> | <code>{{we. She}}</code> | <code>Rishi</code> | The matching Lakan letter identifies the sender of this message as Rishii; the canonical reference identifies Kenzo&#x27;s mentor as Rishi and supplies the preferred spelling. | <code>People/Dunmari/Rishi.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Letters and Notes/Lakan Monk Letter.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>possible-delwath-phrase</code> | <code>u0196:m1</code> | <code>{{That was an I}}</code> | <code>Delwath</code> | This may contain a character name followed by &quot;and I&quot;, but the full marked phrase and intended grouping of characters are unclear; replacing it would reconstruct wording. |
| <code>possible-grash-question</code> | <code>u0609:m1</code> | <code>{{disgrace it}}</code> | <code>Grash</code> | The following question explicitly concerns Grash, so this short damaged phrase may begin a question about him; its complete wording cannot be recovered as a name-only replacement. |
| <code>possible-murook-reaction</code> | <code>u0628:m1</code> | <code>{{How kind of time! Out}}</code> | <code>Murook</code> | The general is reacting to the report of rising zombies, but the damaged span may include a name plus ordinary narration. Its full boundaries and wording are not clear enough to replace. |
| <code>unidentified-reassurance</code> | <code>u2211:m1</code> | <code>{{Miss Tesla}}</code> | — | This could be an address to the freed orc or garbled reassurance. The session record leaves her unnamed, and searched names, aliases, and spelling variants did not establish an identity or complete replacement. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0146:m1</code>, <code>u0155:m1</code>, <code>u0159:m1</code>, <code>u0210:m1</code>, <code>u0354:m1</code>, <code>u0444:m1</code>, <code>u0504:m1</code>, <code>u0625:m1</code>, <code>u0727:m1</code>, <code>u0781:m1</code>, <code>u1266:m1</code>, <code>u1285:m1</code>, <code>u1290:m1</code>, <code>u1576:m1</code>, <code>u1652:m1</code>, <code>u1723:m1</code>, <code>u1744:m1</code>, <code>u1746:m1</code>, <code>u1746:m2</code>, <code>u1747:m1</code>, <code>u1891:m1</code>, <code>u2421:m1</code> | Ordinary speech, mechanics, numbers, generic object wording, or damaged source-reading prose outside the name pass. The written letter does not authorize reconstructing its ordinary words. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-077/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T042214819759Z-2c0adc4e/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-077/cleaned/dunmari-frontier-077-source-cleaned.md</code>
Before SHA-256: <code>3da391a0a71581eaa3980f35b6a0aefc17e054a6a8851a9b33926b63a85a164b</code>
Planned after SHA-256: <code>3dd58cdd48a51bb796eba09cbded9eae795400736c4064e18e7626a2506ddc29</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

# Automatic transcript cleanup

Session: <code>dunmari-frontier-121</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 24 | 3 | 2 | 0 | 4 | 15 | 19 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>wellby-wyvern</code> | high | <code>u0020:m1</code> | <code>{{while he}}</code> | <code>Wellby</code> | The opening contrasts Delwath telling stories with the companion training the wyvern; the later recap names that rider Wellby, as does the session record. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 121 (DuFr).md</code> | no |
| <code>chardonian-contacts</code> | supported | <code>u0135:m1</code> | <code>{{Draconian}}</code> | <code>Chardonian</code> | Riswynn is discussing her Crown-linked contacts after the news from Chardon. The Crown reference identifies its Chardonian subjects; Chardonian is strongly favored over Draconian or the historical Drankorian adjective. | <code>Things/Artifacts of Power/Crown of Purity.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 121 (DuFr).md</code> | no |
| <code>harrow-and-wend</code> | high | <code>u0223:m1</code> | <code>{{harrow and wind}}</code> | <code>Harrow and Wend</code> | The two threatening archfey are explicitly paired in their reference notes; the complete marked span contains their two names. | <code>People/Extraplanar Powers/Archfey/Harrow.md</code>, <code>People/Extraplanar Powers/Archfey/Wend.md</code> | no |
| <code>wend</code> | high | <code>u0329:m1</code> | <code>{{wend me}}</code> | <code>Wend</code> | The adjacent epithet Silence That Follows and rulership of Hollowdark uniquely identify Wend. | <code>People/Extraplanar Powers/Archfey/Wend.md</code> | no |
| <code>harrow-wend-question</code> | supported | <code>u0447:m1</code> | <code>{{hollow and wend}}</code> | <code>Harrow and Wend</code> | The question asks whether the paired entities are two people, and the answer is that nobody is sure. This closely matches the documented uncertainty about Harrow and Wend. Hollowdark is the nearby place name and a possible spoken confusion, so this less certain recognition is marked supported. | <code>People/Extraplanar Powers/Archfey/Harrow.md</code>, <code>People/Extraplanar Powers/Archfey/Wend.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>initiative-name-phrase</code> | <code>u1401:m1</code> | <code>{{Secretzone}}</code> | <code>Seeker</code>, <code>Riswynn</code> | Secretzone may contain Seeker and turn rather than a name alone. Seeker has just acted, while Riswynn answers and acts next; replacing it with Riswynn would impose the expected order over a possible spoken mistake. |
| <code>naval-referent</code> | <code>u0098:m1</code> | <code>{{darkness}}</code> | <code>Dunmar</code>, <code>Darba</code> | The discussion concerns the navy fighting at Darba and in Dunmar, followed immediately by an unmarked self-correction to Dunmar. The marked darkness could be a place-name recognition error or the start of a spoken stumble; no unique spoken form is established. |
| <code>prismwell-damaged-span</code> | <code>u0066:m1</code> | <code>{{prison well still}}</code> | <code>Prismwell</code> | Prismwell is the likely named destination, but the complete marked span also contains still. It could include ordinary words beyond the name; replacing it would silently reconstruct or drop wording. |
| <code>unclear-scholarship-referent</code> | <code>u0153:m1</code> | <code>{{an orphan kins}}</code> | — | The question occurs between discussion of chalyte and fey scholarship, but the marked phrase does not establish a recoverable name, people, or organization. No complete name replacement is supported by the inspected references or session record. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0158:m1</code>, <code>u0207:m1</code>, <code>u0224:m1</code>, <code>u0225:m1</code>, <code>u0544:m1</code>, <code>u0776:m1</code>, <code>u0796:m1</code>, <code>u1154:m1</code>, <code>u1306:m1</code>, <code>u1476:m1</code>, <code>u1854:m1</code>, <code>u1960:m1</code>, <code>u2287:m1</code>, <code>u2474:m1</code>, <code>u2521:m1</code> | Ordinary descriptive wording, conversational fragments, numbers, or combat rules. These spans do not supply a supported name or setting-term correction and remain unchanged outside this pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-121/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T044721274354Z-712d2c24/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-121/cleaned/dunmari-frontier-121-source-cleaned.md</code>
Before SHA-256: <code>e8853c9a407ca021fdcdd8b73f4303548f5e745d65690b04f65fbc2a9e21824e</code>
Planned after SHA-256: <code>8754805daa9dbc043f33b1b13f72fc86f25e8e4c652b33373ab6c275f72905d8</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

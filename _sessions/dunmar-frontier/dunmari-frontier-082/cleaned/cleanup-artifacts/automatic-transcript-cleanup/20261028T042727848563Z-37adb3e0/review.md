# Automatic transcript cleanup

Session: <code>dunmari-frontier-082</code>
Status: <code>reviewed_no_changes</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 23 | 0 | 0 | 0 | 15 | 8 | 23 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | No replacements. | — | — |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>barn-reference</code> | <code>u1618:m1</code> | <code>{{Barn}}</code> | <code>Arryn</code> | Arryn is the story subject, but this short interjection could be a name fragment or incidental speech; context does not recover it uniquely. |
| <code>chasa-phrase</code> | <code>u0144:m1</code> | <code>{{chaos of the Chaser River}}</code> | <code>Chasa</code> | Chasa is the relevant river, but the full span also contains unclear ordinary wording; retain it rather than reconstruct the source sentence. |
| <code>deva-phrase</code> | <code>u0135:m1</code> | <code>{{David messenger of the bars, out}}</code> | <code>Bahrazel</code> | The matching source identifies a deva of the Bahrazel, but correcting the entire damaged phrase would reconstruct ordinary source-reading wording around the name. |
| <code>imprisonment-reference</code> | <code>u0993:m1</code> | <code>{{the wall}}</code> | — | The nearby clarification says imprisonment on another plane, but the wall does not uniquely recover a setting name or its boundaries. |
| <code>iskra-story-phrase</code> | <code>u0829:m1</code> | <code>{{his Chris story}}</code> | <code>Iskra</code> | Iskra is a plausible prior story source, but his Chris story includes unclear pronoun or possessive boundaries and cannot be safely replaced by only the name. |
| <code>jade-hand-phrase</code> | <code>u0403:m1</code> | <code>{{jade&#x27;s hand at rise hand}}</code> | <code>Rai&#x27;s hand</code> | Rai&#x27;s hand is the referent, but the marker also contains a possible false start and repeated hand wording whose exact structure is uncertain. |
| <code>karnas-phrase</code> | <code>u0140:m1</code> | <code>{{Carnes North}}</code> | <code>Karnas</code> | The matching source has Karnas marching north; the marked span combines his name with damaged action wording and cannot safely be reduced to a name. |
| <code>oyster-shell-phrase</code> | <code>u0115:m1</code> | <code>{{ice of}}</code> | <code>Kaikkea</code> | Kaikkea may be intended, but the complete marked wording does not establish a recoverable name boundary before blessed oyster shell. |
| <code>portal-distance-reference</code> | <code>u0338:m1</code> | <code>{{cross}}</code> | — | The portal-distance discussion does not uniquely identify the intended name. The earlier Grash correction was rejected and selectively undone; keep the current marker unchanged. |
| <code>rodnya-repetition-boundaries</code> | <code>u1558:m1</code>, <code>u1558:m2</code>, <code>u1559:m1</code> | <code>{{Anya Rodney}}</code>, <code>{{rattan}}</code>, <code>{{Volknan volkn}}</code> | <code>Rodnya</code>, <code>Voknaz</code> | The discussion clearly concerns Rodnya Voknaz, but these marked fragments may include repetition, a false start, or ordinary clarification. Their complete replacements are not recoverable without reconstructing speech. |
| <code>uzgukhar-repetition</code> | <code>u0129:m1</code> | <code>{{who is Guitar? Who&#x27;s good car}}</code> | <code>Uzgukhar</code> | The besieged city is Uzgukhar, but this whole marker contains a question and a repeated pronunciation attempt; the exact words and repetition boundaries are uncertain. |
| <code>vetta-phrase</code> | <code>u0118:m1</code> | <code>{{in Fed Eye}}</code> | <code>Vetta</code> | Vetta is the relevant sacred island, but the marker includes a preposition and unclear trailing wording; a name-only replacement would discard or reconstruct speech. |
| <code>whisper-addressee</code> | <code>u1031:m1</code> | <code>{{Adela}}</code> | — | Adela could be a garbled name or ordinary aside; the dialogue does not uniquely establish the addressee. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0142:m1</code>, <code>u0334:m1</code>, <code>u0543:m1</code>, <code>u0843:m1</code>, <code>u1343:m1</code>, <code>u1344:m1</code>, <code>u1668:m1</code>, <code>u1745:m1</code> | Dates, chatter, party activity wording, and explanations are outside the name pass; no wording is reconstructed. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-082/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T042727848563Z-37adb3e0/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-082/cleaned/dunmari-frontier-082-source-cleaned.md</code>
Before SHA-256: <code>86cd052709a2cef3df29b7d82e1734f5dd63e29b3dbc1ca62db6c530699ea288</code>
Planned after SHA-256: <code>86cd052709a2cef3df29b7d82e1734f5dd63e29b3dbc1ca62db6c530699ea288</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

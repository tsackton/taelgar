# Automatic transcript cleanup

Session: <code>dunmari-frontier-075</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 36 | 2 | 2 | 0 | 7 | 25 | 32 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>wyvern</code> | high | <code>u1023:m1</code> | <code>{{liver}}</code> | <code>wyvern</code> | The recalled creature was turned into a turtle by Seeker; the recorded wyvern encounter establishes this exact referent and term. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 43 (DuFr).md</code> | no |
| <code>hralgar</code> | supported | <code>u1123:m1</code> | <code>{{You frog}}</code> | <code>Hralgar</code> | The named referent is explicitly the storm giant recently consulted by the party. Hralgar uniquely matches that role; Ulfgar is the separate dwarven research contact. | <code>People/Giants/Hralgar.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 74 (DuFr).md</code> | no |
| <code>alesh</code> | high | <code>u1342:m1</code> | <code>{{A lash}}</code> | <code>Alesh</code> | This complete marked name matches Alesh, the messenger discussed earlier in this conversation; preserve the spoken name without changing the addressee to Sura. | <code>People/Dunmari/Alesh.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 74 (DuFr).md</code> | no |
| <code>govir</code> | supported | <code>u1386:m1</code> | <code>{{go here}}</code> | <code>Govir</code> | The speaker lists sources of knowledge about Tokra; Govir is their contacted scholar in Tokra, strongly favoring his name over the literal ordinary phrase. | <code>People/Dunmari/Govir.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 74 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>augury-mirror-phrase</code> | <code>u1598:m1</code> | <code>{{Just kiss. I agree. Marilyn&#x27;s}}</code> | <code>augury mirror</code> | The previous words mention the augury mirror, but this marked span combines possible item wording with unrecoverable ordinary speech. |
| <code>darkness-referent</code> | <code>u0843:m1</code> | <code>{{melody}}</code> | <code>Wellby</code>, <code>Ladder</code> | The short corrupted combat reference does not uniquely identify a creature or companion; the lighting context does not securely distinguish Wellby, the Ladder, or ordinary wording. |
| <code>imperial-phrase</code> | <code>u1502:m1</code> | <code>{{imperial charges}}</code> | <code>Chardon</code> | The span may contain a reference to Chardon, but the complete replacement also requires reconstructing damaged ordinary wording. |
| <code>kenzo-phrase</code> | <code>u2015:m1</code> | <code>{{Ken was said}}</code> | <code>Kenzo</code> | Kenzo is plausible inside this span, but the full marked wording includes an uncertain verb or possessive; replacing it would reconstruct the surrounding phrase. |
| <code>news-informant</code> | <code>u1387:m1</code> | <code>{{Giles}}</code> | <code>Alesh</code>, <code>Gyles</code> | Alesh supplied the recent Dunmari news, but Giles also closely matches the established name Gyles. The context cannot distinguish ASR error from an actual spoken name or misremembering. |
| <code>riswynn-phrase</code> | <code>u2050:m1</code> | <code>{{He is up with me}}</code> | <code>Riswynn</code> | Riswynn may be describing her own concern, but neither the name nor the complete surrounding phrase is secure within this marked span. |
| <code>unfinished-alliance-reference</code> | <code>u1341:m1</code> | <code>{{C.}}</code> | <code>Karnas</code> | The single-letter span follows an unfinished alliance reference; Karnas is discussed nearby, but the intended full name or ordinary continuation cannot be recovered securely. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0346:m1</code>, <code>u0493:m1</code>, <code>u0734:m1</code>, <code>u0819:m1</code>, <code>u0876:m1</code>, <code>u1025:m1</code>, <code>u1078:m1</code>, <code>u1114:m1</code>, <code>u1376:m1</code>, <code>u1466:m1</code>, <code>u1467:m1</code>, <code>u1468:m1</code>, <code>u1549:m1</code>, <code>u1549:m2</code>, <code>u1644:m1</code>, <code>u1685:m1</code>, <code>u1771:m1</code>, <code>u1844:m1</code>, <code>u1878:m1</code>, <code>u1907:m1</code>, <code>u1941:m1</code>, <code>u1992:m1</code>, <code>u2000:m1</code>, <code>u2043:m1</code>, <code>u2065:m1</code> | Ordinary dialogue, rules, descriptions, damaged phrases, and directional words remain outside this name pass. The marked east and West may be spoken slips; do not correct them from geographical expectations. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-075/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T042124596115Z-52251522/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-075/cleaned/dunmari-frontier-075-source-cleaned.md</code>
Before SHA-256: <code>5b564eb6f890391a0ec491f877a2636a5a12dbc3123a7971d2aef18691b88ff0</code>
Planned after SHA-256: <code>8c6228b1f3c245232df2aaaded8bcaeab5ba45740a3655e5448aef0b0243674c</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

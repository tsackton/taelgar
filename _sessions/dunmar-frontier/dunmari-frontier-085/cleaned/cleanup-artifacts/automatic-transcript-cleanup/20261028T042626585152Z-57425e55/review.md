# Automatic transcript cleanup

Session: <code>dunmari-frontier-085</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 62 | 2 | 2 | 0 | 1 | 57 | 58 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>inkaye</code> | supported | <code>u0197:m1</code> | <code>{{entire}}</code> | <code>inkaye</code> | The discussion identifies the special elemental metal available for a ship enhancement, distinguishing it from the already magical glove. Inkaye is the party&#x27;s recovered metal that absorbs extraplanar energy; adamantine and Skaer steel do not fit this specific role as well. | <code>Things/Materials/Inkaye.md</code> | no |
| <code>highkeep</code> | high | <code>u0268:m1</code> | <code>{{hiking}}</code> | <code>Highkeep</code> | The letter addresses Seeker by his established clan name; Darakan identifies both Seeker and Frankar as Highkeep, and the campaign introduction uses Seeker of Highkeep. | <code>Gazetteer/Central Highlands/Dwarven Kingdoms/Darakan.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 1 (DuFr).md</code> | no |
| <code>faldrak-position</code> | high | <code>u0994:m1</code> | <code>{{contract}}</code> | <code>Faldrak</code> | The DM is positioning Faldrak on the encounter map, explicitly naming him before this span and confirming his position immediately afterward. The reference note establishes Faldrak as his short name. | <code>People/Dwarves/Faldrak Bronzehammer.md</code> | no |
| <code>dwarven-style</code> | supported | <code>u1501:m1</code> | <code>{{we&#x27;re then}}</code> | <code>Dwarven</code> | Seeker asks whether the carving style is dwarven; the preceding question and immediate response about rough-hewn rock strongly favor this one-word cultural term over ordinary wording. The session record identifies the dwarven explorers and their interest in worked stone. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 85 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>lisbon-identity</code> | <code>u1966:m1</code> | <code>{{Lisbon}}</code> | <code>Riswynn</code> | Riswynn is a plausible phonetic reading and an established dwarven companion, but this joking future-level aside does not identify its subject uniquely; ordinary wording such as this one is also possible. Retain the span rather than choose an identity. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0033:m1</code>, <code>u0034:m1</code>, <code>u0035:m1</code>, <code>u0161:m1</code>, <code>u0189:m1</code>, <code>u0281:m1</code>, <code>u0344:m1</code>, <code>u0387:m1</code>, <code>u0402:m1</code>, <code>u0456:m1</code>, <code>u0471:m1</code>, <code>u0553:m1</code>, <code>u0613:m1</code>, <code>u0702:m1</code>, <code>u0721:m1</code>, <code>u0732:m1</code>, <code>u0762:m1</code>, <code>u0772:m1</code>, <code>u0773:m1</code>, <code>u0813:m1</code>, <code>u0847:m1</code>, <code>u0857:m1</code>, <code>u0858:m1</code>, <code>u0885:m1</code>, <code>u0911:m1</code>, <code>u0916:m1</code>, <code>u0935:m1</code>, <code>u1074:m1</code>, <code>u1087:m1</code>, <code>u1089:m1</code>, <code>u1113:m1</code>, <code>u1142:m1</code>, <code>u1149:m1</code>, <code>u1227:m1</code>, <code>u1303:m1</code>, <code>u1374:m1</code>, <code>u1404:m1</code>, <code>u1413:m1</code>, <code>u1449:m1</code>, <code>u1465:m1</code>, <code>u1509:m1</code>, <code>u1634:m1</code>, <code>u1673:m1</code>, <code>u1684:m1</code>, <code>u1694:m1</code>, <code>u1708:m1</code>, <code>u1715:m1</code>, <code>u1730:m1</code>, <code>u1732:m1</code>, <code>u1831:m1</code>, <code>u1852:m1</code>, <code>u1879:m1</code>, <code>u1925:m1</code>, <code>u1961:m1</code>, <code>u1978:m1</code>, <code>u2256:m1</code>, <code>u2292:m1</code> | Ordinary chatter, damaged phrases, actions, object descriptions, geological descriptions, and rules or interface discussion outside the name-and-setting-term pass. Apparent names within longer damaged phrases do not support a complete name-only replacement. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-085/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T042626585152Z-57425e55/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-085/cleaned/dunmari-frontier-085-source-cleaned.md</code>
Before SHA-256: <code>bd467e71b9223f1dfe7c427717f7625fe915f9f241f9da91aab2bac2127bf6c2</code>
Planned after SHA-256: <code>c7e26dd06685b3cc88d47d31a5760cc47dd000689d4298d89dcba3a1675091cd</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

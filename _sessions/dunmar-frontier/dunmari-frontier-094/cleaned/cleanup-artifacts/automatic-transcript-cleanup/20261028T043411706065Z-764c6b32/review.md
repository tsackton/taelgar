# Automatic transcript cleanup

Session: <code>dunmari-frontier-094</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 54 | 1 | 3 | 0 | 4 | 46 | 50 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>aygul</code> | supported | <code>u0600:m1</code> | <code>{{I go}}</code> | <code>Aygul</code> | The frost giant is taking an interest in the two orc crew members. Aygul is Nuzkar’s twin and fellow traveler aboard the ship; the marked sound strongly favors her name in this list. | <code>People/Orcs/Aygul.md</code> | no |
| <code>sura-message-stone</code> | high | <code>u0645:m2</code> | <code>{{serf}}</code> | <code>Sura</code> | The party is distinguishing its two paired stones. The session record establishes that a stone was sent to Sura; the marked span is her name. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 74 (DuFr).md</code> | no |
| <code>riswynn-request</code> | supported | <code>u1530:m1</code> | <code>{{rather}}</code> | <code>Riswynn</code> | The DM is immediately summarizing Riswynn’s request for additional challenges at u1524–u1525. The speaker and request identify Riswynn; the reference note supplies her spelling. | <code>People/PCs/Dunmar Fellowship/Riswynn.md</code> | no |
| <code>seeker-goggles</code> | supported | <code>u1844:m1</code> | <code>{{Gospel is}}</code> | <code>goggles</code> | Seeker is listing the magical possessions removed from his body. His established carried goggles uniquely fit this marked item reference and its sound; retain the short reference without expanding the item name. | <code>Campaigns/Dunmari Frontier Campaign/Treasure/Goggles of Object Reading.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>armor-subject</code> | <code>u1676:m1</code> | <code>{{hit. Tim}}</code> | <code>Kenzo</code>, <code>Tim</code> | The following discussion concerns Kenzo’s armor and staff, but the marked span may include an address to Tim or other ordinary words. Its complete name-replacement boundary is unclear. |
| <code>crew-names-damaged</code> | <code>u0619:m1</code> | <code>{{Emma Chrissie}}</code> | <code>Amil</code>, <code>Kethra</code> | Amil and Kethra are plausible crew references, but the marked span does not clearly establish either complete name or a list boundary. Replacing it would require reconstructing the phrase. |
| <code>history-modifier</code> | <code>u0607:m1</code> | <code>{{august}}</code> | <code>Orcish</code>, <code>Algerd’s</code> | The context concerns histories of orcs, but the marked sound could be an ordinary modifier, Orcish, or a possessive reference to Algerd. The exact whole-span term is not established. |
| <code>rodnya-map-phrase</code> | <code>u2140:m1</code> | <code>{{rhinos like in these}}</code> | <code>Zoryana</code> | Zoryana is a plausible referent in the map discussion, but the marker includes additional damaged wording. A complete name-only replacement cannot preserve the phrase safely. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0074:m1</code>, <code>u0077:m1</code>, <code>u0108:m1</code>, <code>u0117:m1</code>, <code>u0118:m1</code>, <code>u0240:m1</code>, <code>u0505:m1</code>, <code>u0509:m1</code>, <code>u0512:m1</code>, <code>u0513:m1</code>, <code>u0514:m1</code>, <code>u0563:m1</code>, <code>u0619:m2</code>, <code>u0622:m1</code>, <code>u0630:m1</code>, <code>u0645:m1</code>, <code>u0716:m1</code>, <code>u0794:m1</code>, <code>u0801:m1</code>, <code>u0802:m1</code>, <code>u0803:m1</code>, <code>u0805:m1</code>, <code>u0833:m1</code>, <code>u0836:m1</code>, <code>u0900:m1</code>, <code>u0913:m1</code>, <code>u0934:m1</code>, <code>u1023:m1</code>, <code>u1219:m1</code>, <code>u1236:m1</code>, <code>u1381:m1</code>, <code>u1489:m1</code>, <code>u1554:m1</code>, <code>u1557:m1</code>, <code>u1570:m1</code>, <code>u1626:m1</code>, <code>u1680:m1</code>, <code>u1798:m1</code>, <code>u1855:m1</code>, <code>u1953:m1</code>, <code>u1954:m1</code>, <code>u1983:m1</code>, <code>u1989:m1</code>, <code>u2031:m1</code>, <code>u2040:m1</code>, <code>u2147:m1</code> | These spans concern descriptions, sentence fragments, social conversation, crafting, equipment discussion, or rules rather than recoverable names or setting terms. The marked Roman and Baxter phrases do not identify those characters in their local contexts; the descriptive boy-in-Chardon phrase and possible apprentice wording likewise require prose reconstruction, not name substitution. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-094/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T043411706065Z-764c6b32/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-094/cleaned/dunmari-frontier-094-source-cleaned.md</code>
Before SHA-256: <code>9e80ab82762ba7560f65178727dfc42e9a4432b0e1ebc85de4ccafc85f2df92e</code>
Planned after SHA-256: <code>729b71be4b5a6a86fa23ca14e15fe5ba579971bdae938ec7434aa6725f79b0d4</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

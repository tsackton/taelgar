# Automatic transcript cleanup

Session: <code>dunmari-frontier-089</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 22 | 2 | 3 | 0 | 4 | 13 | 17 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>orenlas</code> | supported | <code>u0357:m2</code> | <code>{{Orange}}</code> | <code>Orenlas</code> | The speaker is describing the reach of Alcarinque; Orenlas is an established surviving part of that realm and the closest supported name. The rough spoken direction is preserved and the recognition remains supported. | <code>History/Historical Realms/Alcarinque.md</code>, <code>Gazetteer/Upper Istaros/Orenlas/Orenlas.md</code> | no |
| <code>shadow-armband</code> | supported | <code>u0664:m1</code> | <code>{{1,000}}</code> | <code>armband</code> | The described object is the armband destroyed by the Deno&#x27;qai fire druid at the moment Delwath escaped. The session record explicitly connects that armband with his teleportation; the numeric ASR form is less certain phonetically. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 53 (DuFr).md</code> | no |
| <code>urgall</code> | high | <code>u0721:m1</code> | <code>{{ergo, the black}}</code> | <code>Urgall the Black</code> | The comparison explicitly concerns a ciphered record of private instructions; Urgall and his recovered scroll establish the unique referent and spelling. | <code>People/Skaer/Urgall the Black.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Treasure/Urgall&#x27;s scroll.md</code> | no |
| <code>havdar</code> | supported | <code>u1373:m1</code> | <code>{{hop there}}</code> | <code>Havdar</code> | The joke about finally giving an uncursed gift uniquely fits Havdar, whose curse came from a gifted sword. The phonetic recognition is imperfect, so this is supported rather than high. | <code>People/Dunmari/Havdar.md</code> | no |
| <code>tanshi</code> | high | <code>u1422:m1</code> | <code>{{tauntie}}</code> | <code>tanshi</code> | Delwath contrasts his divine companions with the party; the religious reference and his recorded journey establish the term. | <code>Gods and Religions/Gods/Tanshi/Tanshi.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 53 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>amil-origin-phrase</code> | <code>u1487:m1</code> | <code>{{parallel is from}}</code> | — | This may contain an origin place or simply ordinary wording about where Amil is from. His reference and the session record do not settle a unique place or complete replacement boundaries. |
| <code>giant-siege-phrase</code> | <code>u0425:m1</code> | <code>{{beseech the box}}</code> | — | A siege target may be embedded in this damaged phrase, but the inspected vision does not identify the complete wording or a unique place name. Replacing the whole marker would reconstruct a verb phrase. |
| <code>kenzo-phrase</code> | <code>u0544:m1</code> | <code>{{Kenza are much more talented than they look}}</code> | <code>Kenzo</code> | Kenzo is a possible embedded name, but the entire marker is a damaged sentence and cannot be replaced by a complete name without reconstructing or removing ordinary speech. |
| <code>sending-item-phrase</code> | <code>u1702:m1</code> | <code>{{sending one person}}</code> | <code>sending stone</code> | Context suggests the communication item paired with Sura, but the complete marked span may include additional ordinary words. A name-only replacement would guess those boundaries. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0081:m1</code>, <code>u0357:m1</code>, <code>u0361:m1</code>, <code>u0520:m1</code>, <code>u0823:m1</code>, <code>u0826:m1</code>, <code>u1538:m1</code>, <code>u1601:m1</code>, <code>u1602:m1</code>, <code>u1613:m1</code>, <code>u1638:m1</code>, <code>u1650:m1</code>, <code>u1660:m1</code> | Ordinary conversation, travel planning, saving-throw chatter, and damaged grammatical phrases; resolving them would require prose or rules reconstruction outside the marked name and setting-term pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-089/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T043017213295Z-5827a833/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-089/cleaned/dunmari-frontier-089-source-cleaned.md</code>
Before SHA-256: <code>50311dc2f7ca140aaeb44ca110a21c7e478c03418142606e2764fa9e3c6ed466</code>
Planned after SHA-256: <code>556f05ce861d266155e1c41bec5aa1c01fb86253c2c7dc322c67b9c313c19c2f</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

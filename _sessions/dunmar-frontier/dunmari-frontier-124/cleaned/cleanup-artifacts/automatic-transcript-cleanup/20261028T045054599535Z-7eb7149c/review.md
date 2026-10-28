# Automatic transcript cleanup

Session: <code>dunmari-frontier-124</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 23 | 2 | 3 | 0 | 3 | 15 | 18 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>tilly</code> | supported | <code>u0084:m1</code> | <code>{{Ellie}}</code> | <code>Tilly</code> | The speaker pairs this sailor with Milo Thistlefoot and identifies the Copperharps as their former crew. Tilly is Milo&#x27;s documented wife and sailing companion; no separate Ellie is established in this context. | <code>People/Halflings/Tilly Brineheart.md</code>, <code>People/Halflings/Mica Copperharp.md</code> | no |
| <code>chamutte</code> | high | <code>u0130:m1</code> | <code>{{Shabbat&#x27;s}}</code> | <code>Cha&#x27;mutte&#x27;s</code> | Delwath is describing his escape from the shadow realm connected to Cha&#x27;mutte&#x27;s armbands. The established name and pronunciation resolve the possessive marked form. | <code>People/Extraplanar Powers/Cha&#x27;mutte.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Treasure/Cha&#x27;mutte’s Shadow Armband.md</code> | no |
| <code>manifesto-title</code> | supported | <code>u0784:m1</code> | <code>{{raking the stone}}</code> | <code>Break the Stone</code> | The span names the manifesto being discussed. The contextual timeline documents its title; the phonetic recognition is less certain than the matching subject and role. | <code>_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Timeline.md</code> | no |
| <code>chasa</code> | supported | <code>u0822:m1</code> | <code>{{Chaucan}}</code> | <code>Chasa</code> | The conversation describes the river&#x27;s north bank in Chardon. The North Bank reference identifies that river uniquely as the Chasa, favoring it over an otherwise unattested Chaucan. | <code>Gazetteer/Major Rivers/Chasa-Nahadi Watershed/Chasa.md</code>, <code>Gazetteer/Greater Chardon/Chardonian Empire/Chardon/North Bank.md</code> | no |
| <code>kylos-market</code> | high | <code>u0873:m1</code> | <code>{{Kylos market}}</code> | <code>Kylos Market</code> | The marked market name is already recognizable; the reference confirms its capitalization and the matching Pandemonium incident. | <code>Gazetteer/Greater Chardon/Chardonian Empire/Chardon/Kylos Market.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>cleansed-fragments</code> | <code>u1881:m1</code>, <code>u1882:m1</code>, <code>u1884:m1</code> | <code>{{this client}}</code>, <code>{{not cleansed himself}}</code>, <code>{{Clan}}</code> | <code>Cleansed</code> | The surrounding exchange concerns the Cleansed, but the damaged phrases and final &#x27;Clan&#x27; do not establish exact spoken wording. Membership and magical possession are being distinguished; reconstructing a phrase or choosing Cleansed over an ordinary-word fragment would risk changing that distinction. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0204:m1</code>, <code>u0267:m1</code>, <code>u0284:m1</code>, <code>u0434:m1</code>, <code>u0481:m1</code>, <code>u0954:m1</code>, <code>u1010:m1</code>, <code>u1060:m1</code>, <code>u1075:m1</code>, <code>u1430:m1</code>, <code>u1627:m1</code>, <code>u1712:m1</code>, <code>u1760:m1</code>, <code>u1872:m1</code>, <code>u2014:m1</code> | Ordinary dialogue, jokes, incomplete wording, and spell or bastion discussion are outside this name pass. The longer &#x27;one of the cleansed&#x27; span includes surrounding prose rather than an isolated name; retain the whole span without reconstructing or partially unmarking it. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-124/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T045054599535Z-7eb7149c/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-124/cleaned/dunmari-frontier-124-source-cleaned.md</code>
Before SHA-256: <code>539a45810cec99c22beed9d01d3cd868aed960d87edd1c92e2f95fa48b4739f9</code>
Planned after SHA-256: <code>9fb77a12d86b76749d8e385e42b79fde3d9f652a9074edda8b7b8ec757855407</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

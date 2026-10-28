# Automatic transcript cleanup

Session: <code>dunmari-frontier-127</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 21 | 3 | 3 | 0 | 1 | 14 | 15 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>amil-hall-of-stories</code> | high | <code>u0267:m1</code> | <code>{{Omo}}</code> | <code>Amil</code> | The consecutive replies identify the Hall of Stories researcher; the bastion rules explicitly assign that role to Amil or Kenzo. | <code>People/Dunmari/Amil.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Vindristjarna Bastion Rules.md</code> | no |
| <code>amil-hall-of-stories</code> | high | <code>u0268:m1</code> | <code>{{Ammo}}</code> | <code>Amil</code> | The consecutive replies identify the Hall of Stories researcher; the bastion rules explicitly assign that role to Amil or Kenzo. | <code>People/Dunmari/Amil.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Vindristjarna Bastion Rules.md</code> | no |
| <code>amil-hall-of-stories</code> | high | <code>u0269:m1</code> | <code>{{Amel}}</code> | <code>Amil</code> | The consecutive replies identify the Hall of Stories researcher; the bastion rules explicitly assign that role to Amil or Kenzo. | <code>People/Dunmari/Amil.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Vindristjarna Bastion Rules.md</code> | no |
| <code>tanshi-contact</code> | supported | <code>u0634:m1</code> | <code>{{botanji}}</code> | <code>the tanshi</code> | The Contact Other Plane discussion and repeated phonetic variants strongly favor the tanshi as the consulted beings. The sources establish the term and Delwath&#x27;s tanshi shrine; no individual god is inferred. | <code>Gods and Religions/Gods/Tanshi/Tanshi.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Vindristjarna Bastion Rules.md</code> | no |
| <code>tanshi-contact</code> | supported | <code>u0650:m1</code> | <code>{{the time. She}}</code> | <code>the tanshi</code> | The Contact Other Plane discussion and repeated phonetic variants strongly favor the tanshi as the consulted beings. The sources establish the term and Delwath&#x27;s tanshi shrine; no individual god is inferred. | <code>Gods and Religions/Gods/Tanshi/Tanshi.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Vindristjarna Bastion Rules.md</code> | no |
| <code>vindristjarna-size-comparison</code> | supported | <code>u2078:m1</code> | <code>{{Peterson}}</code> | <code>Vindristjarna</code> | The immediately preceding comparison explicitly names Vindristjarna, and this continuation compares the same tower with that ship. The ship note establishes its spelling; no Peterson referent is established. | <code>Things/Ships/Vindristjarna.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>unclear-ice-experiment-name</code> | <code>u0149:m1</code> | <code>{{Baldrick Johnson}}</code> | <code>Faldrak</code> | The span may include Faldrak&#x27;s name and an action during the ice experiments, or may be damaged ordinary wording. Neither the complete replacement nor its boundaries are recoverable without reconstructing the phrase. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0029:m1</code>, <code>u0033:m1</code>, <code>u0068:m1</code>, <code>u0086:m1</code>, <code>u0150:m1</code>, <code>u0175:m1</code>, <code>u0663:m1</code>, <code>u1200:m1</code>, <code>u1301:m1</code>, <code>u1502:m1</code>, <code>u1956:m1</code>, <code>u2027:m1</code>, <code>u2064:m1</code> | These spans concern ordinary dialogue, an unfinished navy-transport phrase, descriptions, grammar, or spell and saving-throw discussion rather than recoverable names or setting terms. Preserve them without reconstructing wording. |
| <code>source-reading-geology</code> | <code>u0245:m1</code> | The matching survey shows this is an ordinary geological adjective in source-reading discussion, not an entity name or setting term. Repairing it belongs outside names-v1. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-127/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T045121252884Z-5fd0e078/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-127/cleaned/dunmari-frontier-127-source-cleaned.md</code>
Before SHA-256: <code>bf575416f5683fcd06a2b014df8267f3b7a60a364bd953776942ad035d48643a</code>
Planned after SHA-256: <code>dd81f60819b200fce891aff22b8b909d57d8043e9c7dc683ddc6dfb37de085da</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

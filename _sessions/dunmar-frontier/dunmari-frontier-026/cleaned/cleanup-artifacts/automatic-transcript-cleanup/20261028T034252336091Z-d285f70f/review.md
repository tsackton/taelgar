# Automatic transcript cleanup

Session: <code>dunmari-frontier-026</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 22 | 0 | 2 | 0 | 3 | 17 | 20 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>historical-ogres</code> | supported | <code>u0467:m1</code> | <code>{{owners}}</code> | <code>ogres</code> | The speaker recalls the old name used in the earlier campaign. The historical creation account uses ogre for the mountain people, and the old NPC list identifies Beryl&#x27;s ogre mentor; together with the adjacent recollection this strongly favors ogres over the ASR owners. This preserves the historical term rather than substituting the modern species name. | <code>Worldbuilding/Old Documents/Original Taelgar Documents/Human Creation Myth.md</code>, <code>Worldbuilding/Old Documents/Great War/NPC List.md</code> | no |
| <code>beryl-mentors</code> | supported | <code>u0468:m1</code> | <code>{{barrels mentors}}</code> | <code>Beryl&#x27;s mentors</code> | The speaker recalls the earlier campaign monk and his mentors. Beryl is the uniquely matching former player character, and the historical NPC list explicitly identifies his ogre mentor. Preserve the original plural mentors; only restore the possessive name within the complete marked reference. | <code>People/PCs/Great War/Beryl.md</code>, <code>Worldbuilding/Old Documents/Great War/NPC List.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>centaur-name-question</code> | <code>u1082:m1</code> | <code>{{turmeric}}</code> | <code>Tharandros</code> | The centaur leader is Tharandros, supplied by the DM on the next line. However the player is asking for the forgotten name, so turmeric may be an actual mistaken guess or joke rather than an ASR error. Retain the spoken uncertainty rather than overwrite it with the answer. |
| <code>drikod-or-chatter</code> | <code>u2709:m1</code> | <code>{{drinking}}</code> | <code>Drikod</code> | The speaker is Drikod and could be restating his name, but drinking may instead be an out-of-character aside; the following fragment mentions beer. The character spelling and mirror-carrying context do not resolve what was spoken. |
| <code>kenzo-introduction</code> | <code>u0575:m1</code> | <code>{{on Canada}}</code> | <code>Kenzo</code> | Kenzo is introducing himself, but the full marked span on Canada may include ordinary introduction wording or a different aside. The character note establishes Kenzo, not an unambiguous replacement for this entire span; do not reconstruct the phrase. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0047:m1</code>, <code>u0181:m1</code>, <code>u0189:m1</code>, <code>u0366:m1</code>, <code>u0408:m1</code>, <code>u0555:m1</code>, <code>u0563:m1</code>, <code>u0624:m1</code>, <code>u0783:m1</code>, <code>u0828:m1</code>, <code>u1319:m1</code>, <code>u1960:m1</code>, <code>u1972:m1</code>, <code>u2103:m1</code>, <code>u2245:m1</code>, <code>u2489:m1</code>, <code>u2735:m1</code> | These spans concern greetings, narration, physical descriptions, ordinary dialogue, combat mechanics, or descriptions of magical effects. None supplies a recoverable complete name or setting-term correction; repairing them would reconstruct ordinary wording outside names-v1. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-026/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T034252336091Z-d285f70f/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-026/cleaned/dunmari-frontier-026-source-cleaned.md</code>
Before SHA-256: <code>0afcd25714194eecd9e2b2b4afaa9b5803399b1c1a6f41d6105a40a94b962bdb</code>
Planned after SHA-256: <code>2c2c6e12111f10653cd651a4b12176ee179e032e106a88f54755257fa7583d4f</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

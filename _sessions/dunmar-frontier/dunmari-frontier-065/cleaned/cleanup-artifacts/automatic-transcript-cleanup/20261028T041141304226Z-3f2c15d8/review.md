# Automatic transcript cleanup

Session: <code>dunmari-frontier-065</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 76 | 1 | 2 | 0 | 3 | 70 | 73 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>illaran</code> | high | <code>u0014:m1</code> | <code>{{a Lauren}}</code> | <code>Illaran</code> | The recap identifies the donor of Seeker&#x27;s crystallized magic; the reference note and session record identify that donor as Illaran. | <code>People/Fey/Illaran.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 65 (DuFr).md</code> | no |
| <code>sylvan-legion</code> | supported | <code>u0175:m1</code> | <code>{{Celest}}</code> | <code>Sylvan</code> | Caulaus identifies his third legion. His collected story explicitly names the third Sylvan legion, strongly favoring Sylvan over the isolated Celest recognition. No surrounding wording is reconstructed. | <code>Campaigns/Dunmari Frontier Campaign/Collected Stories/Caulaus&#x27; Story.md</code> | no |
| <code>mote-of-fate</code> | supported | <code>u1466:m1</code> | <code>{{motivate}}</code> | <code>mote of fate</code> | The discussion concerns Seeker&#x27;s single-use means of rerolling a save. The campaign record establishes that he received a Mote of Fate; the compressed motivate recognition strongly favors that named gift over an ordinary verb. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 29 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>caves-referent</code> | <code>u2257:m1</code> | <code>{{a spoil}}</code> | <code>Lightdancer</code> | The Lightdancer is the likely referent because they retreat to caves, but a spoil does not establish whether a name, title, or ordinary wording was spoken. Retain the marked span rather than substitute the known role. |
| <code>delwath-mixed-phrase</code> | <code>u0556:m1</code> | <code>{{down with this}}</code> | <code>Delwath</code> | A possible Delwath reference is mixed with unclear ordinary wording; replacing the whole span with the name would discard words, while expanding it would reconstruct the phrase. |
| <code>spirala-mixed-phrase</code> | <code>u0533:m1</code> | <code>{{how to these, for all}}</code> | <code>Spirala</code> | The end of the marked phrase may address Spirala, but the preceding wording cannot be recovered by replacing the complete span with a name. Retain the entire phrase. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0073:m1</code>, <code>u0092:m1</code>, <code>u0104:m1</code>, <code>u0111:m1</code>, <code>u0152:m1</code>, <code>u0154:m1</code>, <code>u0169:m1</code>, <code>u0221:m1</code>, <code>u0375:m1</code>, <code>u0380:m1</code>, <code>u0384:m1</code>, <code>u0402:m1</code>, <code>u0412:m1</code>, <code>u0490:m1</code>, <code>u0536:m1</code>, <code>u0568:m1</code>, <code>u0586:m1</code>, <code>u0608:m1</code>, <code>u0630:m1</code>, <code>u0735:m1</code>, <code>u0839:m1</code>, <code>u0885:m1</code>, <code>u0919:m1</code>, <code>u0951:m1</code>, <code>u0979:m1</code>, <code>u0980:m1</code>, <code>u0982:m1</code>, <code>u1002:m1</code>, <code>u1003:m1</code>, <code>u1016:m1</code>, <code>u1018:m1</code>, <code>u1044:m1</code>, <code>u1071:m1</code>, <code>u1082:m1</code>, <code>u1082:m2</code>, <code>u1104:m1</code>, <code>u1106:m1</code>, <code>u1128:m1</code>, <code>u1227:m1</code>, <code>u1232:m1</code>, <code>u1332:m1</code>, <code>u1353:m1</code>, <code>u1384:m1</code>, <code>u1429:m1</code>, <code>u1461:m1</code>, <code>u1491:m1</code>, <code>u1524:m1</code>, <code>u1579:m1</code>, <code>u1595:m1</code>, <code>u1620:m1</code>, <code>u1621:m1</code>, <code>u1669:m1</code>, <code>u1799:m1</code>, <code>u1920:m1</code>, <code>u1957:m1</code>, <code>u2021:m1</code>, <code>u2049:m1</code>, <code>u2065:m1</code>, <code>u2080:m1</code>, <code>u2081:m1</code>, <code>u2083:m1</code>, <code>u2093:m1</code>, <code>u2112:m1</code>, <code>u2188:m1</code>, <code>u2208:m1</code>, <code>u2258:m1</code>, <code>u2265:m1</code>, <code>u2273:m1</code>, <code>u2308:m1</code>, <code>u2309:m1</code> | Ordinary descriptions, interrupted utterances, table chatter, numbers, dice, rules and spell-use wording are outside this name pass. This includes the alarm-like wording rendered Alan and the unclear channel-divinity utterance; neither establishes a proper-name correction. Preserve every span verbatim. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-065/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T041141304226Z-3f2c15d8/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-065/cleaned/dunmari-frontier-065-source-cleaned.md</code>
Before SHA-256: <code>262cdeb5339b844829b0d51751f69e6b89a9cda78f19d223287192d6ba1966f1</code>
Planned after SHA-256: <code>15e380fe3f256183170a024b55774c25765f6dee0f8c42996be77028b491542b</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

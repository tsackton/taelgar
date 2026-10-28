# Automatic transcript cleanup

Session: <code>dunmari-frontier-027</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 39 | 1 | 0 | 0 | 3 | 35 | 38 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>vision-automata</code> | high | <code>u0028:m1</code> | <code>{{atomic}}</code> | <code>automata</code> | The recap describes the same waterfall-powered small constructs as the initiation account, which explicitly calls them automata; the complete marked construct term can be corrected without reconstructing adjacent wording. | <code>Campaigns/Dunmari Frontier Campaign/Dreams and Visions/The Shakun Mystai Initiation.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>armory-owner</code> | <code>u0352:m1</code> | <code>{{shots}}</code> | — | The quip follows a question about Delwath summoning weapons. The inspected character and campaign sources do not establish a uniquely named armory or an owner matching shots; the possessive and identity remain uncertain. |
| <code>mesa-presence-reference</code> | <code>u0827:m1</code> | <code>{{chimeras bora}}</code> | <code>Shakun</code> | The following feminine pronoun and mesa context make a Shakun reference plausible, but the complete marked phrase is not recoverable as a unique name or setting term. Replacing it would require guessing additional wording. |
| <code>shadow-creature-term</code> | <code>u0030:m1</code> | <code>{{doctors}}</code> | <code>dogs</code>, <code>stalkers</code> | The recap refers to the preceding shadow attack, but the session record establishes shadowy forms rather than a unique creature term matching doctors. Dogs and stalkers are possible readings; neither is established for this marked occurrence. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0017:m1</code>, <code>u0026:m1</code>, <code>u0068:m1</code>, <code>u0216:m1</code>, <code>u0220:m1</code>, <code>u0313:m1</code>, <code>u0330:m1</code>, <code>u0373:m1</code>, <code>u0404:m1</code>, <code>u0537:m1</code>, <code>u0577:m1</code>, <code>u0595:m1</code>, <code>u0605:m1</code>, <code>u0700:m1</code>, <code>u0712:m1</code>, <code>u0774:m1</code>, <code>u0784:m1</code>, <code>u0814:m1</code>, <code>u0900:m1</code>, <code>u0902:m1</code>, <code>u1162:m1</code>, <code>u1210:m1</code>, <code>u1257:m1</code>, <code>u1442:m1</code>, <code>u1448:m1</code>, <code>u1449:m1</code>, <code>u1484:m1</code>, <code>u1637:m1</code>, <code>u1694:m1</code>, <code>u1714:m1</code>, <code>u1719:m1</code>, <code>u2219:m1</code>, <code>u2239:m1</code>, <code>u2321:m1</code>, <code>u2359:m1</code> | Ordinary narration, conversation, incomplete phrases, measurements, generic planar wording, or rules discussion. These spans do not present a supported complete name or setting-term replacement and remain unchanged under names-v1. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-027/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T034243588496Z-ebaa904f/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-027/cleaned/dunmari-frontier-027-source-cleaned.md</code>
Before SHA-256: <code>1ac51c78e47f9c0c71ec3d7bb04841207684535f61b3444774315bd4c55e65a0</code>
Planned after SHA-256: <code>0596b802a2e24262e75f825bac59ff4ed4aceead6c7a817a80679dddefebec66</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

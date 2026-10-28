# Automatic transcript cleanup

Session: <code>dunmari-frontier-116</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 63 | 1 | 1 | 0 | 4 | 57 | 61 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>delwath</code> | supported | <code>u1600:m1</code> | <code>{{Dylan}}</code> | <code>Delwath</code> | Wellby is proposing that the person who just suggested the crown test take it; Delwath replies that he meant Riswynn. The session roster establishes Delwath; Dylan is not a participant in this session. | <code>_sessions/dunmar-frontier/dunmari-frontier-116/cleaned/dunmari-frontier-116-session.yaml</code> | no |
| <code>bahrazel</code> | high | <code>u2850:m1</code> | <code>{{barzel}}</code> | <code>Bahrâzel</code> | Riswynn is driving away undead with dwarven divine power; the reference note establishes the collective name of the dwarven gods as Bahrâzel. | <code>Gods and Religions/Gods/Embodied Gods/Bahrazel/Bahrazel.md</code>, <code>Gods and Religions/Religions/Dwarven Religious Practice.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>dead-realm-fragment</code> | <code>u3178:m1</code> | <code>{{Dead tigers}}</code> | <code>Land of the Dead</code> | The preceding line says land of the, so Land of the Dead is plausible, but the extra word tigers is unexplained. Removing it would reconstruct a damaged phrase. |
| <code>initiative-name-phrase</code> | <code>u0312:m1</code> | <code>{{seekers are dealt with}}</code> | <code>Seeker</code>, <code>Delwath</code> | The initiative discussion may contain Seeker and Delwath, but the complete marked phrase includes unclear connective wording. A name-only replacement would reconstruct the phrase. |
| <code>jaguar-ability-fragment</code> | <code>u3477:m1</code> | <code>{{lang}}</code> | <code>Lengau</code>, <code>Lengau&#x27;s Claw</code> | The jaguar reference favors Lengau, and a prior session records Lengau&#x27;s Claw. The fragment does not establish whether the speaker started the spirit name, a possessive, or the full ability name before saying The Jaguar Fist; retain the uncertain boundary. |
| <code>prehuman-crown-question</code> | <code>u1893:m1</code> | <code>{{Kenzel’s}}</code> | <code>Kenzo</code> | The question follows the claim that the crown predates humans. Kenzo is a phonetic possibility, but the intended possessive referent and sense of the question are unclear; the roster alone does not resolve it. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0038:m1</code>, <code>u0229:m1</code>, <code>u0316:m1</code>, <code>u0575:m1</code>, <code>u0820:m1</code>, <code>u0852:m1</code>, <code>u0857:m1</code>, <code>u1400:m1</code>, <code>u1483:m1</code>, <code>u1521:m1</code>, <code>u1776:m1</code>, <code>u1802:m1</code>, <code>u1864:m1</code>, <code>u1964:m1</code>, <code>u2049:m1</code>, <code>u2123:m1</code>, <code>u2126:m1</code>, <code>u2197:m1</code>, <code>u2211:m1</code>, <code>u2238:m1</code>, <code>u2278:m1</code>, <code>u2318:m1</code>, <code>u2336:m1</code>, <code>u2338:m1</code>, <code>u2365:m1</code>, <code>u2592:m1</code>, <code>u2895:m1</code>, <code>u2915:m1</code>, <code>u3168:m1</code>, <code>u3188:m1</code>, <code>u3627:m1</code>, <code>u3675:m1</code> | Ordinary dialogue, damaged sentences, descriptions, and source-phrase reconstruction are outside this pass. No complete uniquely supported name or setting-term replacement is established for these spans. |
| <code>rules-and-numbers</code> | <code>u0237:m1</code>, <code>u0630:m1</code>, <code>u0678:m1</code>, <code>u0690:m1</code>, <code>u0715:m1</code>, <code>u0715:m2</code>, <code>u0758:m1</code>, <code>u0775:m1</code>, <code>u0871:m1</code>, <code>u0873:m1</code>, <code>u0925:m1</code>, <code>u0951:m1</code>, <code>u1038:m1</code>, <code>u1060:m1</code>, <code>u1136:m1</code>, <code>u1137:m1</code>, <code>u1493:m1</code>, <code>u1539:m1</code>, <code>u1812:m1</code>, <code>u2285:m1</code>, <code>u2398:m1</code>, <code>u2529:m1</code>, <code>u2942:m1</code>, <code>u3486:m1</code>, <code>u3646:m1</code> | Rules explanations, saves, inspiration, spell discussion, actions, and numerical wording are outside the name pass; retain without repairing mechanics or grammar. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-116/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T044413130066Z-0b12c3e1/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-116/cleaned/dunmari-frontier-116-source-cleaned.md</code>
Before SHA-256: <code>1626ff4d2d607f8d6e7b4cc87cdfdf185dfd05259442378868ac4fdbc7af6c7c</code>
Planned after SHA-256: <code>31b4ec3bae9df78de36af6fc53c5552914333064f946ed96a95387675da97b36</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

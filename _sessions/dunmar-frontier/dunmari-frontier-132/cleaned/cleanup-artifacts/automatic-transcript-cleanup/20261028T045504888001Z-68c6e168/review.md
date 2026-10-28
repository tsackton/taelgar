# Automatic transcript cleanup

Session: <code>dunmari-frontier-132</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 41 | 0 | 1 | 0 | 4 | 36 | 40 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>tanshi-sanctuary</code> | supported | <code>u1210:m1</code> | <code>{{Shetanshi}}</code> | <code>tanshi</code> | The discussion enumerates structures on Vindristjarna; the ship reference explicitly identifies its sanctuary of the tanshi. This uniquely favors tanshi despite the extra initial syllable in the marked ASR form. | <code>Things/Ships/Vindristjarna.md</code>, <code>Gods and Religions/Gods/Tanshi/Tanshi.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>evasion-name-conflict</code> | <code>u2314:m1</code> | <code>{{Kenzo and Seeker}}</code> | <code>Kenzo and Seeker</code>, <code>Kenzo and Wellby</code> | The marked names say Kenzo and Seeker, while the nearby dialogue excludes Seeker from the save and says Wellby takes nothing. This may be a spoken name slip; substituting Wellby would silently choose between ASR error and the recorded speaker wording. |
| <code>heartroot-self-correction</code> | <code>u2838:m1</code> | <code>{{Hearthstone}}</code> | <code>Hearthstone</code>, <code>Heartroot</code> | The marker is immediately followed by or the Heartroot. This can be the speaker correcting their own name slip; the setting source identifies Heartroot but does not establish what was spoken before that correction. |
| <code>icicle-shield-phrase</code> | <code>u0272:m1</code> | <code>{{Icicle Shield at the rabbit}}</code> | <code>Icicle Shield</code> | Icicle Shield is a recognizable ship feature, but the marked span also contains unclear ordinary words. Recovering the complete span would require reconstructing a phrase, so it remains unchanged. |
| <code>seeker-turn-order</code> | <code>u2714:m1</code> | <code>{{Seeker 5}}</code> | <code>Seeker 5</code>, <code>Seeker</code> | The speaker lists Seeker 5 twice in the same turn order. The surrounding dialogue distinguishes Seeker and Seeker 5, but cannot establish whether the final repetition was spoken or mistranscribed. Preserve the marker rather than correcting the turn order. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0090:m1</code>, <code>u0129:m1</code>, <code>u0150:m1</code>, <code>u0297:m1</code>, <code>u0424:m1</code>, <code>u0465:m1</code>, <code>u0647:m1</code>, <code>u0676:m1</code>, <code>u0728:m1</code>, <code>u0801:m1</code>, <code>u0816:m1</code>, <code>u0998:m1</code>, <code>u1292:m1</code>, <code>u1365:m1</code>, <code>u1482:m1</code>, <code>u1644:m1</code>, <code>u1738:m1</code>, <code>u1739:m1</code>, <code>u1777:m1</code>, <code>u1787:m1</code>, <code>u1873:m1</code>, <code>u1891:m1</code>, <code>u2098:m1</code>, <code>u2212:m1</code>, <code>u2271:m1</code>, <code>u2280:m1</code>, <code>u2281:m1</code>, <code>u2414:m1</code>, <code>u2652:m1</code>, <code>u2654:m1</code>, <code>u2739:m1</code>, <code>u2746:m1</code>, <code>u2770:m1</code>, <code>u2854:m1</code>, <code>u2857:m1</code>, <code>u2877:m1</code> | These spans concern ordinary conversation, tactical descriptions, distances, dice or damage, spell mechanics, gestures, and incomplete sentence wording. No complete name or setting-term replacement is justified without reconstructing surrounding phrasing. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-132/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T045504888001Z-68c6e168/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-132/cleaned/dunmari-frontier-132-source-cleaned.md</code>
Before SHA-256: <code>248e9f1d7ba7de5b1c8225d1929b26743d5256a50a24683efdba30a2908b4841</code>
Planned after SHA-256: <code>f1eb9d97444555e161f9af3cda87ced8b925e698c2f9126e5cb712557be945a3</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

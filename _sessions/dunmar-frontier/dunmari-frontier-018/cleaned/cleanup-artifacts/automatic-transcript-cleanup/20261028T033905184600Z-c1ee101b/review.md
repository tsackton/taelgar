# Automatic transcript cleanup

Session: <code>dunmari-frontier-018</code>
Status: <code>reviewed_no_changes</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 | 0 | 0 | 0 | 2 | 0 | 2 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| — | — | — | — | — | No replacements. | — | — |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>seer-name-or-title</code> | <code>u1746:m1</code> | <code>{{Our car}}</code> | — | The dialogue attributes the warning about Candrosa to a centaur seer, but Our car could conceal a personal name or part of a title. The inspected centaur and session sources do not establish the exact form; replacing the complete span would require guessing. |
| <code>seer-title</code> | <code>u2762:m1</code> | <code>{{omen car}}</code> | <code>omen caller</code> | The preceding omen seeker and following of our tribe establish a diviner role, but do not distinguish a damaged English title such as omen caller from a name or another title. The inspected sources establish centaur divination without attesting the complete marked term. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| — | — | No outside-scope markers. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-018/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T033905184600Z-c1ee101b/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-018/cleaned/dunmari-frontier-018-source-cleaned.md</code>
Before SHA-256: <code>dbf1ecdf6b95d71711ae85a4120a2f8ec290b39936c77d1ef792ee954fd31afd</code>
Planned after SHA-256: <code>dbf1ecdf6b95d71711ae85a4120a2f8ec290b39936c77d1ef792ee954fd31afd</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

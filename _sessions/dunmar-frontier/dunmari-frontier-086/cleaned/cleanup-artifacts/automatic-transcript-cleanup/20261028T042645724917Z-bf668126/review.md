# Automatic transcript cleanup

Session: <code>dunmari-frontier-086</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 0 | 2 | 0 | 2 | 12 | 14 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>blessing-of-perception</code> | supported | <code>u1232:m1</code> | <code>{{blasting up perception}}</code> | <code>Blessing of Perception</code> | Delwath names a preparation that lets him see invisible creatures. The shield reference identifies his item, and the preserved discussion explicitly names its existing Blessing of Perception and see-invisibility function; no proposed later upgrade is adopted. | <code>Campaigns/Dunmari Frontier Campaign/Treasure/Deno&#x27;qai Lynx Shield.md</code>, <code>Worldbuilding/Chats and Emails/Chats/2025-10-11 - Calendars and Holidays.md</code> | no |
| <code>raven-whistle</code> | supported | <code>u1520:m1</code> | <code>{{Brittany&#x27;s}}</code> | <code>Raven&#x27;s</code> | Kenzo blows his whistle to fly. The item note establishes his ownership of the Raven Whistle, and Session 38 independently records its flight use. The possessive is retained within the marked span; the unmarked word whistle is preserved. | <code>Campaigns/Dunmari Frontier Campaign/Treasure/Raven Whistle.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 38 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>handbook-in-damaged-phrase</code> | <code>u0486:m1</code> | <code>{{have security on that we found}}</code> | <code>Enchiridion of the Occulta Ludum</code> | The discussion concerns showing the newly found book to the mirror, making Enchiridion plausible, but the whole marked span contains additional damaged wording. Replacing it would require reconstructing an ordinary phrase. |
| <code>possible-drankor-in-damaged-phrase</code> | <code>u2296:m1</code> | <code>{{drink or look over}}</code> | <code>Drankor</code> | The speaker is comparing the ancient binding vision with Drusilia. A Drankor reference is possible in the marked phrase, but its identity and surrounding wording are not securely recoverable as a complete name-only span. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0410:m1</code>, <code>u0410:m2</code>, <code>u0487:m1</code>, <code>u0493:m1</code>, <code>u0648:m1</code>, <code>u0931:m1</code>, <code>u1198:m1</code>, <code>u1522:m1</code>, <code>u1609:m1</code>, <code>u1657:m1</code> | Damaged conversational wording, sentence fragments, and a quantity are outside the name and setting-term pass; retain them without reconstructing phrases. |
| <code>rules-wording</code> | <code>u1471:m1</code>, <code>u1864:m1</code> | Resistance wording and action-economy terminology are rules explanations rather than recoverable name spans. Do not correct mechanics or a possible spoken rules mistake. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-086/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T042645724917Z-bf668126/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-086/cleaned/dunmari-frontier-086-source-cleaned.md</code>
Before SHA-256: <code>3188764d22121c1e3d94eb97abc6bc317dc3c738857522b54c9aabf94b803094</code>
Planned after SHA-256: <code>d5e49739774ee9f19429d3965bdc68078e5c1159dbcb4fd3943bc02d55db3cbb</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

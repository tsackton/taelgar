# Automatic transcript cleanup

Session: <code>dunmari-frontier-105</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 20 | 1 | 1 | 0 | 1 | 17 | 18 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>psychic-rune</code> | supported | <code>u1800:m1</code> | <code>{{rune of psychic destruction}}</code> | <code>Rune of Psychic Disruption</code> | Seeker casts an incapacitating rune and later calls another use rune of psychic disruption at u2102. The campaign record establishes Rune of Psychic Disruption. Destruction could be a spoken variant, but the repeated caster, effect, and later name strongly favor Disruption. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 112 (DuFr).md</code>, <code>_sessions/dunmar-frontier/dunmari-frontier-105/cleaned/dunmari-frontier-105-source-cleaned.md</code> | no |
| <code>fire-clan</code> | high | <code>u2464:m1</code> | <code>{{fire}}</code> | <code>Fire</code> | The bat is listing the speaking jungle groups alongside Blaze and Slither; the reference note establishes Fire as the clan name. | <code>People/Other Nonhumans/Pip.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>elemental-strike-name</code> | <code>u1752:m1</code> | <code>{{earth buying}}</code> | <code>earthbinding</code> | This may be a named elemental attack or an ordinary descriptive phrase. The session notes and vault search do not establish its name; earthbinding is plausible, but its exact form cannot be supported. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>numbers-and-measurements</code> | <code>u2130:m1</code>, <code>u2895:m1</code> | Damage numbers and height measurements are outside the name and setting-term pass. |
| <code>ordinary-wording</code> | <code>u0100:m1</code>, <code>u0161:m1</code>, <code>u0214:m1</code>, <code>u0682:m1</code>, <code>u0990:m1</code>, <code>u1068:m1</code>, <code>u1251:m1</code>, <code>u1681:m1</code>, <code>u2265:m1</code>, <code>u2499:m1</code>, <code>u2579:m1</code>, <code>u2790:m1</code>, <code>u3205:m1</code>, <code>u3256:m1</code>, <code>u3301:m1</code> | Ordinary conversation, descriptions, hypotheses, and incomplete phrases outside the name and setting-term pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-105/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T044039244517Z-0228a2b7/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-105/cleaned/dunmari-frontier-105-source-cleaned.md</code>
Before SHA-256: <code>7e6562793600d94a9279fcdf0c051d5eb0cfbcbe8e65e4f02b8f3d3afa3ed9bb</code>
Planned after SHA-256: <code>2bd05fb445f0c09e6b0b5c3ff68af7a6d9d9fc37a5fb00c7b90488afcc05da1d</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

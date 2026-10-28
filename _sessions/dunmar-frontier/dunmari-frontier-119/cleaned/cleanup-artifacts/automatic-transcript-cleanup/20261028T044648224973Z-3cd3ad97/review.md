# Automatic transcript cleanup

Session: <code>dunmari-frontier-119</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 41 | 3 | 1 | 0 | 9 | 28 | 37 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>seeker-aura</code> | high | <code>u0031:m1</code> | <code>{{seekers}}</code> | <code>Seeker&#x27;s</code> | The preceding exchange identifies the aura as belonging to Seeker; normalize the marked possessive of his established name without repairing adjacent dialogue. | <code>_sessions/dunmar-frontier/dunmari-frontier-119/cleaned/dunmari-frontier-119-session.yaml</code> | no |
| <code>sembaran-language</code> | high | <code>u0180:m1</code> | <code>{{sambarin}}</code> | <code>Sembaran</code> | The DM is listing languages heard by the party. Sembaran is the established language matching this marked form; no surrounding assignments are changed. | <code>Background/Languages.md</code> | no |
| <code>thark-compulsion</code> | supported | <code>u1230:m1</code> | <code>{{stark}}</code> | <code>Thark</code> | The free orcs and the Cloudspinner cloak uniquely favor Thark, whose compulsion the People of the Rainbow escaped. Grash is the defeated commander in the preceding sentence; ordinary dark is less consistent with the named source of their bondage. | <code>Gods and Religions/Gods/Embodied Gods/Thark.md</code> | no |
| <code>everlights-bloom</code> | high | <code>u1440:m1</code> | <code>{{Everlight&#x27;s bloom}}</code> | <code>Everlight&#x27;s Bloom</code> | Normalize the capitalization of the already recognizable domain name. Preserve the speaker naming this realm, even though the context might suggest a mistaken place reference. | <code>Gazetteer/Extraplanar/Feywild/Everlight&#x27;s Bloom.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>cloak-phrase</code> | <code>u0108:m1</code> | <code>{{So I guess we&#x27;re the Cloak of Rainbows.}}</code> | <code>Cloak of Rainbows</code> | Cloak of Rainbows is recognizable, but the complete marked sentence contains uncertain ordinary wording; correcting only the item name would require reconstructing the phrase. |
| <code>colorado-location</code> | <code>u0953:m1</code> | <code>{{Colorado}}</code> | — | The dialogue recalls an earlier bird transformation, but the inspected campaign records do not uniquely identify the place represented by Colorado. Preserve the location rather than choose a phonetic guess. |
| <code>dancer-carlos</code> | <code>u0542:m1</code> | <code>{{Carlos.}}</code> | <code>Kenzo</code> | Kenzo volunteers immediately afterward and Riswynn says Kenzo, but Carlos could be actual spoken wording or a misstatement; do not substitute the contextually correct character without establishing the marked utterance. |
| <code>fina-ally</code> | <code>u0856:m1</code> | <code>{{Fina}}</code> | <code>Typhina</code> | Typhina is a possible phonetic candidate connected to Seeker and the Cloudspinner court, but the source distinguishes her from the impostor known to the party. Fina could be shorthand or another spoken reference; the present ally claim does not securely identify a complete replacement. |
| <code>golden-stag-title</code> | <code>u0756:m1</code> | <code>{{Enter Golden Stag}}</code> | — | The source establishes Lirien and a golden stag, but Enter Golden Stag is not an established title. It could be connective wording about her mount or a misremembered title; retain the complete span. |
| <code>lirien-demise-phrase</code> | <code>u0695:m1</code> | <code>{{Lirien’s demise of the agents of Harrow and Wend}}</code> | <code>Lirien</code>, <code>Harrow</code>, <code>Wend</code> | Lirien and Harrow and Wend are identifiable, but the complete marked span includes damaged wording about her demise. No whole-span name-only correction preserves its uncertain meaning. |
| <code>master-revels-spelling</code> | <code>u1518:m1</code>, <code>u1551:m1</code> | <code>{{Sovin}}</code>, <code>{{Sovin}}</code> | <code>Soven</code>, <code>Sorven</code> | The Master of the Revels is uniquely identified, but the ruler reference explicitly disputes Soven versus Sorven. Retain both Sovin markers until the preferred spelling is settled. |
| <code>temple-connective</code> | <code>u0205:m1</code> | <code>{{Shaolin}}</code> | — | The temple and artifact context is established, but no complete name replacement for Shaolin is established. This may instead be damaged connective wording; retain the span. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0093:m1</code>, <code>u0098:m1</code>, <code>u0156:m1</code>, <code>u0187:m1</code>, <code>u0225:m1</code>, <code>u0301:m1</code>, <code>u0391:m1</code>, <code>u0417:m1</code>, <code>u0512:m1</code>, <code>u0778:m1</code>, <code>u0794:m1</code>, <code>u0795:m1</code>, <code>u0908:m1</code>, <code>u0909:m1</code>, <code>u0917:m1</code>, <code>u0991:m1</code>, <code>u1057:m1</code>, <code>u1194:m1</code>, <code>u1224:m1</code>, <code>u1227:m1</code>, <code>u1344:m1</code>, <code>u1367:m1</code>, <code>u1466:m1</code>, <code>u1475:m1</code>, <code>u1498:m1</code>, <code>u1530:m1</code>, <code>u1550:m1</code>, <code>u1555:m1</code> | Ordinary dialogue, ad hoc ballad wording, numbers, descriptive prose, gestures, and rules discussion require wording reconstruction rather than established name or setting-term correction. Retain these spans unchanged; this category does not require human name review. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-119/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T044648224973Z-3cd3ad97/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-119/cleaned/dunmari-frontier-119-source-cleaned.md</code>
Before SHA-256: <code>ad654db00ded48523f49c5288ab034e4c7ca52e75750219d4c540bccca03a998</code>
Planned after SHA-256: <code>6e335eba32e2ce079115524a61e642e455bbbc380c471e8ba433783a26caa1d5</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

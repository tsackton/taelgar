# Automatic transcript cleanup

Session: <code>dunmari-frontier-128</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 61 | 1 | 0 | 0 | 2 | 58 | 60 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>dhrukmir-repeated-name</code> | high | <code>u0011:m1</code> | <code>{{Ruthmere}}</code> | <code>Dhrukmir</code> | The opening recap repeats the giant ruler’s name immediately before Skybreaker; the canonical person note and session account establish Dhrukmir. | <code>People/Giants/Dhrukmir.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 128 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>garbled-giant-name</code> | <code>u3346:m1</code> | <code>{{drigamga bugger}}</code> | <code>Dhrukmir</code> | Dhrukmir is the target of the named psychic attack, but the complete marked span may include a joking or deliberately mangled name and additional wording. Replacing it with the canonical name would erase uncertain spoken content. |
| <code>orc-recollection</code> | <code>u1843:m1</code> | <code>{{orc}}</code> | <code>ogre</code>, <code>orc</code> | The prior session identifies the interrogated creature as an ogre, and Delwath calls it an ogre moments later; Kenzo may actually have said orc while recalling it. Preserve the possible spoken mistake. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>names-within-damaged-wording</code> | <code>u0595:m1</code>, <code>u1087:m1</code>, <code>u2030:m1</code>, <code>u3820:m1</code>, <code>u3869:m1</code>, <code>u3920:m1</code> | These complete spans contain ordinary damaged phrasing, sometimes alongside a recognizable name or spell. Resolving them would require reconstructing wording rather than correcting a whole marked name or setting term. |
| <code>numbers-and-rolls</code> | <code>u0459:m1</code>, <code>u1007:m1</code>, <code>u1185:m1</code>, <code>u1968:m1</code>, <code>u2567:m1</code>, <code>u3329:m1</code>, <code>u3859:m1</code>, <code>u3860:m1</code> | Damage totals, spell levels, saving throw DCs, and dice narration are outside the name pass. |
| <code>ordinary-combat-and-conversation</code> | <code>u0026:m1</code>, <code>u0040:m1</code>, <code>u0041:m1</code>, <code>u0041:m2</code>, <code>u0083:m1</code>, <code>u0486:m1</code>, <code>u0574:m1</code>, <code>u0978:m1</code>, <code>u0992:m1</code>, <code>u1204:m1</code>, <code>u1246:m1</code>, <code>u1250:m1</code>, <code>u1280:m1</code>, <code>u1285:m1</code>, <code>u1566:m1</code>, <code>u1654:m1</code>, <code>u1667:m1</code>, <code>u1859:m1</code>, <code>u1959:m1</code>, <code>u2045:m1</code>, <code>u2075:m1</code>, <code>u2129:m1</code>, <code>u2205:m1</code>, <code>u2255:m1</code>, <code>u2477:m1</code>, <code>u2479:m1</code>, <code>u2639:m1</code>, <code>u2754:m1</code>, <code>u2773:m1</code>, <code>u2775:m1</code>, <code>u2818:m1</code>, <code>u2818:m2</code>, <code>u2996:m1</code>, <code>u3005:m1</code>, <code>u3005:m2</code>, <code>u3035:m1</code>, <code>u3059:m1</code>, <code>u3125:m1</code>, <code>u3378:m1</code>, <code>u3600:m1</code>, <code>u3713:m1</code>, <code>u3817:m1</code>, <code>u3890:m1</code>, <code>u3899:m1</code> | Ordinary conversation, tactical directions, mechanics, and damaged narrative wording; no complete marked proper name or setting term is supported for replacement. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-128/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T045137492739Z-cd1bc950/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-128/cleaned/dunmari-frontier-128-source-cleaned.md</code>
Before SHA-256: <code>8b183441a1ea1274bfb4f4934e5fb1a737e6ce02e2da0a18152d22ed63c143d1</code>
Planned after SHA-256: <code>7cdbb538fa5a566383035334ac02ca2d1a2ed10b4e311d5e5ffd1d207ed1218c</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

# Automatic transcript cleanup

Session: <code>dunmari-frontier-131</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 24 | 1 | 0 | 1 | 5 | 18 | 23 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>seeker-simulacrum</code> | high | <code>u2501:m1</code> | <code>{{Seeker}}</code> | <code>Seeker</code> | The preceding session explicitly establishes Seeker and his simulacrum together. The repeated name is therefore plausible as spoken; retain Seeker without inventing a numbered suffix. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 130 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>armor-referent</code> | <code>u0407:m1</code> | <code>{{Corps}}</code> | <code>Empress of Chaos</code> | The conversation distinguishes the centipede from the leader’s special armor. The source establishes the Empress of Chaos, but does not establish what complete name or term the marked Corps represents. |
| <code>chaos-title-or-wording</code> | <code>u0690:m1</code> | <code>{{chaos, of course}}</code> | <code>Chaos Empress</code> | The speakers joke that Revaka may become a worse successor. Chaos Empress is plausible, but chaos force or a longer phrase is also possible; the title source cannot determine the exact spoken marked span. |
| <code>isingue-damaged-phrase</code> | <code>u0060:m1</code> | <code>{{that is engaged}}</code> | <code>Isingue</code> | The discussion concerns control of Isingue and its magic, but the complete marked phrase cannot be recovered as a plain name without reconstructing surrounding wording. |
| <code>possible-player-address</code> | <code>u2577:m1</code> | <code>{{Debit}}</code> | <code>David</code>, <code>dammit</code> | Debit could be an address to David or ordinary dammit. Two participants are named David and there is no decisive addressee or lexical cue; preserve the marker. |
| <code>unidentified-general</code> | <code>u0269:m1</code> | <code>{{alamandas}}</code> | — | A female general is intended, but filename, name/alias, variant and campaign-source searches did not establish a matching identity or spelling. Do not substitute a different known general. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0483:m1</code>, <code>u0574:m1</code>, <code>u0796:m1</code>, <code>u0888:m1</code>, <code>u0971:m1</code>, <code>u1036:m1</code>, <code>u1068:m1</code>, <code>u1374:m1</code>, <code>u1381:m1</code>, <code>u1594:m1</code>, <code>u1621:m1</code>, <code>u1866:m1</code>, <code>u1870:m1</code>, <code>u1883:m1</code>, <code>u2675:m1</code>, <code>u2821:m1</code>, <code>u2848:m1</code>, <code>u2849:m1</code> | Ordinary chatter, damaged sentence wording, religious questions, spell discussion and combat mechanics. Correcting these complete spans would reconstruct speech rather than normalize a name or setting term. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-131/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T045548932732Z-cfd1aff4/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-131/cleaned/dunmari-frontier-131-source-cleaned.md</code>
Before SHA-256: <code>3930ded2de8fd2e54ec5eee2102c01d18f088a74169b70cb15a213e078f766b9</code>
Planned after SHA-256: <code>0b4f1de7313c54f0878c8ec30edc70076dd30db290d187bfd9b1ae401b4da23f</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

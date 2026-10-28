# Automatic transcript cleanup

Session: <code>dunmari-frontier-063</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 43 | 5 | 0 | 0 | 0 | 38 | 38 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>illaran</code> | high | <code>u1369:m1</code> | <code>{{a Lauren}}</code> | <code>Illaran</code> | The dwarf-like fey who lives in Crystal Peak, manipulates stone and hair, and guides the party to the Hall of Mirrors is uniquely identified as Illaran in the guardian note and this session&#x27;s record. | <code>People/Fey/Illaran.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 63 (DuFr).md</code> | no |
| <code>taelgar</code> | high | <code>u1445:m1</code> | <code>{{Tel Aviv}}</code> | <code>Taelgar</code> | Seeker distinguishes his home world from the elemental plane of earth. The world name is Taelgar; the Material Plane note confirms the cosmological context. | <code>Gazetteer/Geography of Taelgar.md</code>, <code>Cosmology/Material Plane.md</code> | no |
| <code>illaran</code> | high | <code>u1694:m1</code> | <code>{{Lauren}}</code> | <code>Illaran</code> | The dwarf-like fey who lives in Crystal Peak, manipulates stone and hair, and guides the party to the Hall of Mirrors is uniquely identified as Illaran in the guardian note and this session&#x27;s record. | <code>People/Fey/Illaran.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 63 (DuFr).md</code> | no |
| <code>illaran</code> | high | <code>u1695:m1</code> | <code>{{a Lauren}}</code> | <code>Illaran</code> | The dwarf-like fey who lives in Crystal Peak, manipulates stone and hair, and guides the party to the Hall of Mirrors is uniquely identified as Illaran in the guardian note and this session&#x27;s record. | <code>People/Fey/Illaran.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 63 (DuFr).md</code> | no |
| <code>illaran</code> | high | <code>u1696:m1</code> | <code>{{a Lauren}}</code> | <code>Illaran</code> | The dwarf-like fey who lives in Crystal Peak, manipulates stone and hair, and guides the party to the Hall of Mirrors is uniquely identified as Illaran in the guardian note and this session&#x27;s record. | <code>People/Fey/Illaran.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 63 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| — | — | — | — | No name decisions remain. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>combat-wording</code> | <code>u1812:m1</code>, <code>u1971:m2</code>, <code>u1976:m1</code> | These occur in tactical target selection and armor-class discussion, not references to a location or people named White House, Emily, or Obama. Their ordinary wording remains uncertain and outside the name pass. |
| <code>court-activity</code> | <code>u0025:m1</code> | This modifies the bustling court&#x27;s activity in a descriptive sentence; correcting it would reconstruct ordinary wording, not resolve a person or setting name. |
| <code>healing-wording</code> | <code>u1591:m1</code> | This occurs in a discussion of healing and hit points, not a reference to a person named Hamilton. Recovering the health-related wording is outside this pass. |
| <code>ordinary-wording</code> | <code>u0438:m1</code>, <code>u0476:m1</code>, <code>u0491:m1</code>, <code>u0492:m1</code>, <code>u0684:m1</code>, <code>u0684:m2</code>, <code>u0748:m1</code>, <code>u0748:m2</code>, <code>u0931:m1</code>, <code>u0938:m1</code>, <code>u0944:m1</code>, <code>u1018:m1</code>, <code>u1071:m1</code>, <code>u1103:m1</code>, <code>u1341:m1</code>, <code>u1342:m1</code>, <code>u1360:m1</code>, <code>u1427:m1</code>, <code>u1561:m1</code>, <code>u1569:m1</code>, <code>u1573:m1</code>, <code>u1595:m1</code>, <code>u1779:m1</code>, <code>u1857:m1</code>, <code>u1939:m1</code>, <code>u1957:m1</code>, <code>u1971:m1</code>, <code>u2202:m1</code>, <code>u2303:m1</code>, <code>u2367:m1</code>, <code>u2383:m1</code>, <code>u2398:m1</code> | Ordinary dialogue, movement and combat mechanics, numbers, general descriptions, and damaged phrases outside the name pass. No complete supported name or setting-term replacement is established for these spans. |
| <code>sword-modifier</code> | <code>u0767:m1</code> | The span is an unclear descriptive modifier before sword. The dialogue later calls the weapon a crystal sword, but that does not establish the word spoken here; rewriting this adjective is outside the name pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-063/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T041139615811Z-f51c8852/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-063/cleaned/dunmari-frontier-063-source-cleaned.md</code>
Before SHA-256: <code>5fc45c0e081512da0fe30baced24fd5f68bbf2680f697b575a98ad7af9c64204</code>
Planned after SHA-256: <code>a26ea64e8120ced8a6e8eedb6593b668a274c32dc7f7b5ce0c3c2c40613d3050</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

# Automatic transcript cleanup

Session: <code>dunmari-frontier-097</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 30 | 3 | 0 | 0 | 6 | 21 | 27 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>songara</code> | high | <code>u2742:m1</code> | <code>{{Slingara}}</code> | <code>Songara</code> | Sura is warning Havdar on the named plains; the reference note establishes Songara Plains. The unmarked word plains remains unchanged. | <code>Gazetteer/Greater Dunmar/Hara Basin/Songara Plains.md</code> | no |
| <code>frostfell</code> | high | <code>u3182:m1</code> | <code>{{frost now}}</code> | <code>Frostfell</code> | The speaker offers future use of the Voknaz portal; the manor reference identifies its destination as Frostfell. | <code>Cosmology/Energy Realms/Compound Realms/Frostfell.md</code>, <code>Gazetteer/Northern Green Sea/Ursk/Voknaz Manor.md</code> | no |
| <code>irrla</code> | high | <code>u3847:m1</code> | <code>{{Erla}}</code> | <code>Irrla</code> | Faldrak locates the ship over the Green Sea between Ursk and the island; Irrla is the matching island and its documented pronunciation is EAR-la. | <code>Gazetteer/Eastern Green Sea/Irrla.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>arrival-water-name</code> | <code>u3962:m1</code> | <code>{{Chargmen. See}}</code> | <code>Gulf of Chardon</code>, <code>Chardon sea</code> | The destination is near the Old Chardon Canal and the reference geography names the Gulf of Chardon. Chargmen. See could instead reflect a spoken Chardon sea description; substituting Gulf of Chardon would choose a factual label without establishing the spoken form. |
| <code>chardonian-phrase</code> | <code>u2587:m1</code> | <code>{{chart out of the}}</code> | — | The phrase may repeat Chardonian or modify the following anti-Chardonian description, but replacing the complete span would require reconstructing unclear surrounding words. |
| <code>dwarf-recipient</code> | <code>u3937:m1</code> | <code>{{Demos}}</code> | — | The preceding request is to warn the dwarves about duplicate Riswynn; Demos could be an unclear recipient or a garbled reference to the dwarves. The inspected sources do not establish a unique named recipient. |
| <code>execution-phrase</code> | <code>u2574:m2</code> | <code>{{they was voustillic}}</code> | <code>Fausto</code> | Fausto may be embedded in the marked phrase, but neither the whole phrase nor its name boundary is recoverable with confidence; retain the entire span. |
| <code>kenzo-contact</code> | <code>u3905:m1</code> | <code>{{Case already}}</code> | <code>Kaeso</code> | Kenzo names his contact in Mawar, strongly suggesting Kaeso, but the marker also contains already and the complete name-versus-discourse boundary is uncertain. Retain the full span. |
| <code>orc-stop-phrase</code> | <code>u3457:m1</code> | <code>{{You got with my loose card in your}}</code> | <code>Uzgukhar</code> | This occurs during the Uzgukhar discussion, but the entire marked sentence is unclear and may contain a place or person reference; no complete name-only replacement is established. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0161:m1</code>, <code>u0267:m1</code>, <code>u0469:m1</code>, <code>u0586:m1</code>, <code>u0781:m1</code>, <code>u1177:m1</code>, <code>u1584:m1</code>, <code>u1790:m1</code>, <code>u1941:m1</code>, <code>u2002:m1</code>, <code>u2235:m1</code>, <code>u2250:m1</code>, <code>u2574:m1</code>, <code>u2876:m1</code>, <code>u3362:m1</code>, <code>u3365:m1</code>, <code>u3577:m1</code>, <code>u3707:m1</code>, <code>u3717:m1</code>, <code>u3742:m1</code>, <code>u3784:m1</code> | Ordinary wording, sentence fragments, combat mechanics, equipment descriptions, or conversational repairs outside this name/setting-term pass. These spans require prose reconstruction rather than an evidence-backed complete name replacement. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-097/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T043504417990Z-dd052bfa/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-097/cleaned/dunmari-frontier-097-source-cleaned.md</code>
Before SHA-256: <code>58d0b4c2ac1c363c12a9aa63cbaa022c367ea19e0fd90c17315e547e7973abef</code>
Planned after SHA-256: <code>c4a4534e0bf47d3624a72fb2bc2605dbdf36d17ea9e412313d77455390f18af6</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

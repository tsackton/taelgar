# Automatic transcript cleanup

Session: <code>dunmari-frontier-126</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 39 | 1 | 1 | 0 | 8 | 29 | 37 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>sura</code> | high | <code>u1278:m1</code> | <code>{{Sarah}}</code> | <code>Sura</code> | The conversation names a ruler the party has met; Sura is the established Dunmari ruler and recent campaign contact. The reference establishes the spelling. | <code>People/Dunmari/Sura.md</code> | no |
| <code>circular-island</code> | supported | <code>u1691:m2</code> | <code>{{circular}}</code> | <code>Circular Island</code> | The immediately following discussion concerns flying across the ocean and withholding the location of Apollyon&#x27;s tower. This strongly favors Circular Island over a circlet or scepter; the island reference establishes the complete place name. | <code>Gazetteer/Drankorian Hinterland/Circular Island.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>allison-park</code> | <code>u1116:m1</code> | <code>{{Allison Park}}</code> | <code>Valius and Vargus</code> | The surrounding discussion concerns Valius and Vargus in Tokra, but the complete marked span and the unmarked words do not support a unique person or place replacement. Retain rather than reconstruct the sentence. |
| <code>auratan-self-correction</code> | <code>u0030:m1</code>, <code>u0031:m1</code> | <code>{{are a Torian}}</code>, <code>{{a Torian}}</code> | <code>Auratan</code> | The DM immediately corrects the spoken family name to Auratan and explicitly rejects the earlier form. Replacing the rejected form with Auratan would erase the self-correction; the exact earlier pronunciation or mistaken name is unresolved. |
| <code>bargallde-misremembering</code> | <code>u1309:m1</code> | <code>{{Bargallde}}</code> | <code>Veldari</code> | The player explicitly says this is the name they keep wanting to say and asks for the correct name, supplied next as Veldari. Preserve the spoken misremembering; the source confirms the intended family but not the rejected name. |
| <code>how-may</code> | <code>u1691:m1</code> | <code>{{how may}}</code> | <code>Cha&#x27;mutte</code> | This fragment follows an unfinished list of ancient history to mention. Cha&#x27;mutte is contextually possible, but ordinary hesitation is also plausible and the marked sounds do not establish a unique name. |
| <code>nebos-self-correction</code> | <code>u1286:m1</code> | <code>{{Nebo&#x27;s}}</code> | <code>Nera</code>, <code>Nevos</code> | The DM immediately restates the location as Nera Domains. Nebo&#x27;s may represent a spoken false start or a mistaken Nevos reference; substituting the correct destination would erase that distinction. |
| <code>never-geography</code> | <code>u1221:m1</code> | <code>{{Never}}</code> | <code>Nahadi</code>, <code>Nera</code>, <code>Nevos</code> | The grain-growing river corridor suggests the Nahadi, while Nera and Nevos are also nearby sounding geographic names. The marked form and sentence do not uniquely select one; preserve the uncertainty. |
| <code>orion-family</code> | <code>u1354:m1</code> | <code>{{Orion}}</code> | <code>Caloren</code>, <code>Auratan</code> | Both Caloren and Auratan have just been discussed, and the DM answers by naming both. The player is uncertain about names here, so the span could be a spoken mistake rather than an ASR variant with a unique correction. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>incidental-chatter</code> | <code>u1495:m1</code> | Incidental real-world chatter about a cat and a mouse; no setting identity is being resolved in this pass. |
| <code>ordinary-wording-and-mechanics</code> | <code>u0184:m1</code>, <code>u0221:m1</code>, <code>u0223:m1</code>, <code>u0252:m1</code>, <code>u0254:m1</code>, <code>u0275:m1</code>, <code>u0307:m1</code>, <code>u0595:m1</code>, <code>u0655:m1</code>, <code>u0814:m1</code>, <code>u0941:m1</code>, <code>u0953:m1</code>, <code>u0970:m1</code>, <code>u0971:m1</code>, <code>u1037:m1</code>, <code>u1229:m1</code>, <code>u1443:m1</code>, <code>u1482:m1</code>, <code>u1642:m1</code>, <code>u1683:m1</code>, <code>u1706:m1</code>, <code>u1908:m1</code>, <code>u1921:m1</code>, <code>u2087:m1</code>, <code>u2095:m1</code>, <code>u2157:m1</code> | Ordinary dialogue, incomplete phrases, numbers, rolls, rules explanations, and action wording outside this name and setting-term pass. Preserve the full marked spans without reconstructing surrounding language. |
| <code>spelled-letters</code> | <code>u1140:m1</code>, <code>u1141:m1</code> | Individual letters in a slowly spelled word are source-reading reconstruction, outside the name-only pass; the later complete spelling does not authorize rewriting these fragments. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-126/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T045138441096Z-75717260/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-126/cleaned/dunmari-frontier-126-source-cleaned.md</code>
Before SHA-256: <code>a9485ed44fa1b8e82543dcd1771b6dd80b7bb466be551066ce4fa47ea0abb298</code>
Planned after SHA-256: <code>de1ab5ef99e654b7c5fb0495b33bcc1c7a5a0a1bd0ca88a263aeb7dc1381905d</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.

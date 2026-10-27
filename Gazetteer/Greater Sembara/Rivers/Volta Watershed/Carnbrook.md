---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: brook
name: Carnbrook
whereabouts:
  - {type: primary, location: Tollen}
  - {type: secondary, location: Volta Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

A small brook that flows through [[Tollen]] in culverts. 

%% The name comes from the Skaer Kvernabok (Mill Brook); during the original settlement this brook was the original walls and was used as a mill stream %%

%%^Metadata:names:v1%%
- {"name": "Carnbrook", "language": "unknown", "pronunciation": "KARN-brook", "status": "proposed", "notes": "The Tollish English analogue in [[Languages]] favors initial stress, hard c, ar as in car, and brook with the vowel of book. The shared noncanonical comment proposes derivation from Skaer Kvernabok, meaning Mill Brook, and associates it with early milling and an ambiguously worded original boundary; these historical claims remain for human adoption. The accepted source language and pronunciation are not established."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: Volta, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern culverted urban brook; the date of culverting and the historical claims retained in the comment are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting without changing existing values.
- Recorded a broadly modern article POV and persistent temporal-coverage guidance.
- Added primary name metadata with a proposed pronunciation and its derivation.
- Recorded the filename-derived subject name explicitly in frontmatter.
- Added typed source/outlet map entries, leaving unestablished coordinates blank.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The source and outlet `locator` values remain blank in the required map block. The reviewed direct sources do not establish verified world-map coordinates. Fill each existing typed entry with its verified coordinate as a quoted string; retain its source/outlet role and do not infer a hex from the broader whereabouts.

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed complete pronunciation `KARN-brook` in the persistent name block. The Tollish English analogue in [[Languages]] favors initial stress, hard c, ar as in car, and brook with the vowel of book. The shared noncanonical comment proposes derivation from Skaer Kvernabok, meaning Mill Brook, and associates it with early milling and an ambiguously worded original boundary; these historical claims remain for human adoption. The accepted source language and pronunciation are not established. Accept or revise the proposal; if accepted, copy the complete value into frontmatter and mark the existing entry `documented`.

- [ ] **Suggestion — editorial.public_material_candidate:** The ordinary comment beginning “The name comes from the Skaer Kvernabok” supplies a developed etymology and early use absent from the visible entry. Consider adopting: “The Carnbrook was used as a mill stream during Tollen's early settlement. Its name comes from the Skaer Kvernabok, meaning ‘Mill Brook’.” These remain claims from a noncanonical comment pending human acceptance. Preserve the separate “this brook was the original walls” clause as an unresolved note until its intended boundary meaning is clarified; do not publish that ambiguous clause as history.
%%^End%%

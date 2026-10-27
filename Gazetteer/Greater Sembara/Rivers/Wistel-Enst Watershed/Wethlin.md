---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [status/check/name, place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Wethlin
whereabouts:
  - {type: primary, location: Ardlas}
  - {type: secondary, location: Wistel-Enst Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

%%  check/name -> consider whether one or more of the minor Ardlas rivers should retain Old Zimkovan names %%

The Wethlin is a tributary of the [[Bollin]], joining the river near its headwaters.

%%^Metadata:names:v1%%
- {name: "Wethlin", language: "unknown", pronunciation: "WETH-lin", status: "proposed", notes: "Regional northern Sembaran English analogue: initial stress, short e, voiceless th, and short i in the final syllable. No established name language or exact pronunciation is recorded."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: "Bollin", map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the article describes the drainage system in its current-era geographic reference role, with no narrower speaking position required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving parsed values and headerVersion.
- Added the explicit subject name already supplied by the filename and article.
- Recorded a broadly modern geographic POV and a persistent temporal-coverage note.
- Added persistent name metadata, preserving accepted pronunciations and documenting proposal provenance where needed.
- Added the required typed map entries; unsupported coordinates remain blank for human completion.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required map block now has typed entries, but its source and outlet locator values remain blank. Supply the two verified map coordinates in those entries; do not infer positions from the prose or assign arbitrary coordinates.

- [ ] **Warning — metadata.names_unresolved_status:** The northern Sembaran English analogue suggests initial stress, short e, voiceless th, and a short final i. The name language is unknown. Candidate if accepted: set frontmatter `pronunciation: WETH-lin` and the matching persistent entry pronunciation to `WETH-lin` with `status: documented`; otherwise correct the durable proposal and its derivation together.
%%^End%%

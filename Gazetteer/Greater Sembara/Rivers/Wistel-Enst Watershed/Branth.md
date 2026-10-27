---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Branth
whereabouts:
  - {type: primary, location: Addermarch}
  - {type: secondary, location: Wistel-Enst Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Branth is a short upland river flowing west from the ridge country between [[Addermarch]] and [[Tyrwingha]] to join the [[Aure]] north of [[Adderfell]]. Its narrow valley is dry in places with thin soils but supports significant pasture; the Branth runs swiftly in spring and dwindles to a manageable flow by late summer.

%%^Metadata:names:v1%%
- {name: "Branth", language: "unknown", pronunciation: "BRANTH", status: "proposed", notes: "Addermarch regional Sembaran English analogue: one syllable with short a and final voiceless th; the name language and exact in-world phonology remain unrecorded."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: "Aure", map: world, locator: }
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

- [ ] **Warning — metadata.names_unresolved_status:** The documented English analogue for Addermarch suggests one syllable, short a, and final voiceless th. The source language and exact in-world phonology remain unrecorded. Candidate if accepted: set frontmatter `pronunciation: BRANTH` and the matching persistent entry pronunciation to `BRANTH` with `status: documented`; otherwise correct the durable proposal and its derivation together.
%%^End%%

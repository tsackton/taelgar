---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Bollin
aliases: [Bollin River, River Bollin]
whereabouts:
  - {type: primary, location: Greater Sembara}
  - {type: secondary, location: Wistel-Enst Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

A major river in [[Ardlas]] and western [[Sembara]] that joins the [[Wistel]] near [[Ainwick]]. The Bollin is cold and rocky and shallow for much of its length, and is not navigable save for the 30 miles or so upriver of the confluence with the [[Wistel]]. It has three major tributaries:

* The [[Cambril]], which joins just north of the Aine Hills
* The [[Vardell]], which flows east from [[Khatridun]]
* The [[Wethlin]], which flows south near the headwaters of the Bollin

%%^Metadata:names:v1%%
- {name: "Bollin", language: "unknown", pronunciation: "BOLL-in", status: "proposed", notes: "Regional northern Sembaran English analogue: initial stress, short o, doubled l as a single consonant, and a reduced second syllable; exact name language and pronunciation are unrecorded."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: "Wistel", map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the article describes the drainage system in its current-era geographic reference role, with no narrower speaking position required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving parsed values and headerVersion.
- Recorded a broadly modern geographic POV and a persistent temporal-coverage note.
- Added persistent name metadata, preserving accepted pronunciations and documenting proposal provenance where needed.
- Added the required typed map entries; unsupported coordinates remain blank for human completion.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required map block now has typed entries, but its source and outlet locator values remain blank. Supply the two verified map coordinates in those entries; do not infer positions from the prose or assign arbitrary coordinates.

- [ ] **Warning — metadata.names_unresolved_status:** The northern Sembaran English analogue suggests initial stress, short o, a single l sound, and a reduced second syllable. This is an analogue-informed proposal; the name language is not established. Candidate if accepted: set frontmatter `pronunciation: BOLL-in` and the matching persistent entry pronunciation to `BOLL-in` with `status: documented`; otherwise correct the durable proposal and its derivation together.
%%^End%%

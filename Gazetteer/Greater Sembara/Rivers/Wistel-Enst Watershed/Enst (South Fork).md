---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Enst (South Fork)
aliases: [South Fork, South Fork of the Enst]
whereabouts:
  - {type: primary, location: Western Marches}
  - {type: secondary, location: Wistel-Enst Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
# The Enst (South Fork)
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

One of the three rivers (the others being the [[Enst (North Fork)|North Fork]] and [[Enst (Middle Fork)|Middle Fork]]) that join to form the [[Enst]].

%%^Metadata:names:v1%%
- {name: "Enst (South Fork)", language: "unknown", pronunciation: "ENST south fork", status: "proposed", notes: "ENST is inferred from the documented ENST-bayn pronunciation in [[Enstbain]]; South Fork uses ordinary English. This component evidence does not establish an accepted pronunciation for the complete river name."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: "Enst", map: world, locator: }
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

- [ ] **Warning — metadata.names_unresolved_status:** The documented ENST-bayn in [[Enstbain]] supports the Enst component as ENST; South Fork uses ordinary English. Acceptance of the complete river-name pronunciation remains a human decision. Candidate if accepted: set frontmatter `pronunciation: ENST south fork` and the matching persistent entry pronunciation to `ENST south fork` with `status: documented`; otherwise correct the durable proposal and its derivation together.
%%^End%%

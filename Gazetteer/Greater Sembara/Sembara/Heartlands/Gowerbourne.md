---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Gowerbourne
whereabouts: Duchy of Wisford
dm_owner: none
dm_notes: none
POV: modern
---
# Gowerbourne
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A large market town on the [[Wistel]], known as a center of the [[Duchy of Cheimen|Cheimen]] wool trade.

%% There is some light color in [[El's Story]] %%

%%^Metadata:names:v1%%
- {"name": "Gowerbourne", "language": "unknown", "pronunciation": "GOW-er-burn", "status": "proposed", "notes": "Proposed using the English side of the Sembaran French/English analogues in [[Languages]] and the English-looking place-name form: hard g, ow as in cow, first-syllable stress, and bourne as burn. The source language and a possible French-influenced reading remain unconfirmed."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river-town and wool-trade description; [[El's Story]] supplies selected earlier trading context rather than a continuous history.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added supported persistent name and temporal-viewpoint metadata.
- Added the explicit established name and the required settlement map skeleton, leaving its unknown locator blank.

### Validated judgments
- The one-sentence river-town and wool-trade description performs its bounded reference role. The shared comment points to [[El's Story]], whose economic detail supports an optional addition rather than a central coverage warning.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has its typed single-location entry, but its `locator` is blank. Supply the verified world-map coordinate in that existing entry; the reviewed text and prepared evidence do not establish a coordinate, so none has been guessed.

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `GOW-er-burn`. The English side of the Sembaran French/English analogues in [[Languages]] and the English-looking place-name form support hard g, ow as in cow, initial stress, and bourne as burn. A French-influenced reading and the name language remain unconfirmed. Confirm or replace the proposal; if accepted, copy the complete pronunciation to frontmatter and mark the existing entry `documented`.
%%^End%%

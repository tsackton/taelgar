---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Silverflood
whereabouts:
  - {type: primary, location: Alta Tonaro, startFilter: r}
  - {type: secondary, location: Yeraad Watershed, startFilter: "1"}
dm_owner: tim
dm_notes: none
POV: modern
---
# Silverflood
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Silverflood is the principal river of [[Alta Tonaro]], draining the mineral‑rich foothills north of the [[Chataan Mountains]]. 

In the late DR 1600s, traces of [[chalyte]] were [[Reports on Chalyte in Alta Tonaro|discovered]] by [[Chardonian Empire|Chardonian]] explorers along the upper Silverflood and its tributaries, igniting a rush that transformed the region, though within a generation the easy lodes and river pans were exhausted, and the area fell from prominence as deeper reserves in the [[Chataan Mountains]] proved too perilous to extract.

%%^Metadata:names:v1%%
- {"name":"Silverflood","language":"unknown"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: foothills north of the Chataan Mountains, map: world, locator: }
  - {role: outlet, feature: , map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography with a retrospective account of the first chalyte boom and decline; the article does not survey later mining.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting while preserving parsed values.
- Recorded the existing subject name explicitly in frontmatter.
- Added a persistent name entry, preserving recorded pronunciation and meaning and leaving unsupported language unknown.
- Added typed map entries with supported endpoint features and left unknown positions blank.
- Recorded POV: modern and concise persistent temporal interpretation.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The existing map block lacks verified world-map `locator` values for source and outlet. Fill those blank values with confirmed coordinates, preserving recorded features and roles.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Kayan
pronunciation: KAH-yan
whereabouts:
  - {type: primary, location: Elderwood}
  - {type: secondary, location: Chasa-Nahadi Watershed}
dm_owner: none
dm_notes: color
POV: modern
---
# Kayan
*(KAH-yan)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A tributary of the [[Chasa]] that flows north through the [[Elderwood]], joining the [[Chasa]] near [[Arendum]].

%%^Metadata:names:v1%%
- {"name":"Kayan","language":"unknown","status":"documented","pronunciation":"KAH-yan"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Elderwood, map: world, locator: }
  - {role: outlet, feature: Chasa, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography; no narrower speaking position is required by the visible account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Removed trailing horizontal whitespace on changed prose or the former end-of-file boundary.
- Normalized frontmatter and recorded explicit identity where previously supplied by the filename.
- Added persistent name metadata, preserving accepted pronunciations and keeping unaccepted readings proposed.
- Added required typed map entries, leaving unsupported locators blank.
- Recorded POV: modern and concise temporal coverage in persistent metadata.

### Validated judgments
- The positive dm_notes attestation has confirmed local source support; private contents remain outside this report.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required source and outlet map entries have blank locators. Supply verified world-map coordinates in the existing `Metadata:map:v1` entries; no endpoint coordinate for these positions was established, and none was inferred from regional geography.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
%%^End%%

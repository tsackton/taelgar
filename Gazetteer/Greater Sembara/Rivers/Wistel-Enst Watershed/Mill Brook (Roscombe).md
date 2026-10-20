---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: brook
name: Mill Brook
whereabouts:
  - {type: primary, location: Carlinshire}
  - {type: secondary, location: Wistel-Enst Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
# The Mill Brook
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Mill Brook is a rushing brook that flows past [[Roscombe]] from the northwest, turning south to pass under the road from [[Valcroix]] about a quarter‑mile from the town’s main gates, before eventually joining the [[Velan]].

%%^Metadata:names:v1%%
- {"name":"Mill Brook","language":"Common","status":"inferred","notes":"Transparent written-out place name under the Common naming convention in [[Languages]]."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: Velan, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography; no narrower speaking position is required by the visible account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and recorded explicit identity where previously supplied by the filename.
- Added persistent name metadata, preserving accepted pronunciations and keeping unaccepted readings proposed.
- Added required typed map entries, leaving unsupported locators blank.
- Recorded POV: modern and concise temporal coverage in persistent metadata.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required source and outlet map entries have blank locators. Supply verified world-map coordinates in the existing `Metadata:map:v1` entries; no endpoint coordinate for these positions was established, and none was inferred from regional geography.
%%^End%%

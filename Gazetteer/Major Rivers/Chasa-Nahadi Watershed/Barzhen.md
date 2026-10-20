---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Barzhen
pronunciation: bar-SHEN
whereabouts:
  - {type: primary, location: Blackwater Fens}
  - {type: secondary, location: Chasa-Nahadi Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
# Barzhen
*(bar-SHEN)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Barzhen is a slow, muddy river that flows through the [[Blackwater Fens]], and is the primary river that drains this region.

The name derives from the old Northros word for "heavy, slow".

%% NOTE
The hydrology of the [[Blackwater Fens]] is a bit complicated with several small lakes on the map. The Barzhen is intended to be the "major river" of the region, with a source in the mountains to the north and then joined by tributaries from the lakes before exiting the fens.
%%

%%^Metadata:names:v1%%
- {"name":"Barzhen","language":"Old Northros","status":"documented","pronunciation":"bar-SHEN","notes":"The article explicitly derives the name from the old Northros word meaning heavy, slow.","meaning":"heavy, slow"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: Zarnato, map: world, locator: }
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

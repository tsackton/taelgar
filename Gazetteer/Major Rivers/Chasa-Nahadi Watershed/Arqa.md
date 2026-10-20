---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Arqa
pronunciation: ar-KAH
whereabouts:
  - {type: primary, location: Central Highlands}
  - {type: secondary, location: Chasa-Nahadi Watershed}
dm_owner: none
dm_notes: none
POV: modern
---
# Arqa
*(ar-KAH)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Arqa is a swift-flowing, unnavigable river that cascades down from the [[Sentinel Range|Sentinels]] to join the [[Zarnato]], passing through forests and many ravines over its course.

The name derives from the old Northros word for "hidden". 

%% NOTE

This is the river that joins the [[Zarnato]] from the Sentinels, south of the confluence with the [[Barzhen]]. 

%%

%%^Metadata:names:v1%%
- {"name":"Arqa","language":"Old Northros","pronunciation":"ar-KAH","status":"documented","meaning":"hidden"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Sentinel Range, map: world, locator: }
  - {role: outlet, feature: Zarnato, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river course; the older name derivation has no established adoption date.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting while preserving parsed values.
- Added a persistent name entry, preserving recorded pronunciation and meaning and leaving unsupported language unknown.
- Added typed map entries with supported endpoint features and left unknown positions blank.
- Recorded POV: modern and concise persistent temporal interpretation.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The existing map block lacks verified world-map `locator` values for source and outlet. Fill those blank values with confirmed coordinates, preserving recorded features and roles.

- [ ] **Suggestion — editorial.shared_material_redundant:** The hidden NOTE repeats the visible origin in the Sentinels and confluence with the Zarnato, while adding one distinct positional detail. Remove the repeated wording and retain only the distinct map guidance, for example: “The Arqa joins the Zarnato south of its confluence with the Barzhen.” Keep that positional guidance nonpublic pending any separate adoption decision.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-24T09:25:51-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Sulqat
pronunciation: sul-KAHT
whereabouts: Mawakel Peninsula
dm_owner: none
dm_notes: color
POV: modern
---
# Sulqat
*(sul-KAHT)*
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Sulqat is a cold, rushing river, mostly unnavigable, that flows northeast from the [[Mawar Mountains]] to the [[Slate Sea]], past the city of [[Suhaya]]. The salmon runs on the Sulqat are a major source of food and income for the people of the [[Mawar Confederacy]].

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Mawar Mountains, map: world, locator: }
  - {role: outlet, feature: Slate Sea, map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Sulqat, role: primary, language: unknown, pronunciation: sul-KAHT, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography and subsistence; no narrower temporal constraint is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added a typed waterway map skeleton plus persistent name and temporal POV metadata.

### Validated judgments
- The two local-only evidence clusters genuinely concern the Sulqat and support the positive `dm_notes: color` attestation.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required waterway map block now identifies the [[Mawar Mountains]] as the source feature and the [[Slate Sea]] as the outlet feature, but both `locator` values remain blank. Supply the source and outlet map coordinates.

### DM evidence
- [[_DM_/_Mawar Confederacy/Ep 5 - Lost Legacy/Mawar Religion]]
- [[_DM_/_Mawar Confederacy/Jasper Thundertree]]
%%^End%%

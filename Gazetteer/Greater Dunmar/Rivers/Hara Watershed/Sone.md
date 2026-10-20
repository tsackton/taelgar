---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Sone
pronunciation: SO-nay
whereabouts: Hara Watershed
dm_owner: none
dm_notes: none
POV: modern
---
# Sone
*(SO-nay)*
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Sone is a broad, winding river that flows about 380 miles east from its source in the [[Chataan Mountains]], across the [[Songara Plains]], to its confluence with the [[Hara]]. During the drier months, from November to April, the Sone is a slow, sluggish river. Its outflow increases dramatically during the monsoon, fed by the rains that fall on the [[Songara Plains]].

%%^Metadata:names:v1%%
- {name: Sone, role: primary, language: unknown, pronunciation: SO-nay, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Chataan Mountains, map: world, locator: }
  - {role: outlet, feature: Hara, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the article describes the river's physical course and recurring seasonal flow.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order while preserving existing values and added the explicit subject name.
- Added persistent name metadata retaining the accepted pronunciation and leaving its unestablished language unknown.
- Added the required two-ended waterway map skeleton, naming the supported source and outlet features and leaving both unknown locators blank.
- Added `POV: modern` and temporal coverage metadata for the river's course and seasonal flow.

### Validated judgments
- The visible course and seasonal description are consistent with [[Hara Watershed]], [[Hara]], and [[Hara Basin]].

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required waterway map entries have blank `source.locator` and `outlet.locator`. The article establishes the source in the Chataan Mountains and the outlet at the Hara, but supplies no exact world-map coordinates. Enter confirmed locator strings in the existing source and outlet entries; retain their respective roles and features.
%%^End%%

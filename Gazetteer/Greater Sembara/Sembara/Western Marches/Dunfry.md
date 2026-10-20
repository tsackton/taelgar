---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: town
name: Dunfry
whereabouts: Barony of Dunfry
dm_owner: mike
dm_notes: color
POV: modern
---
# Dunfry
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A fortified settlement along the southern part of the [[Western Wall of Sembara]], it primarily exists to service the large [[Army of the West]]. It is a place of weaponsmiths, quartermasters, and commanders, and bustles with activity in service of the army.

%%^Metadata:names:v1%%
- {"name": "Dunfry", "language": "unknown", "pronunciation": "DUN-fry", "status": "proposed", "notes": "Preferred proposal using the English strand of the Sembaran analogue in [[Languages]]: Dun rhymes with done, final fry with sky, and initial stress. The French strand could favor a rounded u, final ee, and later prominence. Neither the name language nor exact in-world phonology is established."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the article describes the place in its current-era reference role, with no narrower speaking position required by the visible account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent name and temporal metadata.
- Added the required settlement map skeleton with its unknown locator left blank.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map entry has an unknown world-map locator. Supply the verified coordinate in `locations: [{map: world, locator: "<verified coordinate>"}]`; no position was inferred from regional prose.

- [ ] **Warning — metadata.names_unresolved_status:** Review the name-block pronunciation `DUN-fry`. Preferred proposal using the English strand of the Sembaran analogue in [[Languages]]: Dun rhymes with done, final fry with sky, and initial stress. The French strand could favor a rounded u, final ee, and later prominence. Neither the name language nor exact in-world phonology is established. Accept the complete form in frontmatter and mark the entry `documented`, or replace it with the intended pronunciation.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: market town
name: Ruthin
whereabouts: Tyrwingha
dm_owner: mike
dm_notes: none
POV: 1710s
---
# Ruthin
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A moderately sized market town about a half day's walk east of the [[Trellyn]]. There is a temple to the Wyrdling here.
### Notable Residents
* [[Eirian]], a trans woman and acolyte of the Wyrdling. She is known in the region for her gender-affirming herbalist care and is a skilled teacher

%% There is significant color in the "unlinked" backlinks %%

%%^Metadata:names:v1%%
- {"name": "Ruthin", "language": "unknown", "pronunciation": "RITH-in", "status": "proposed", "notes": "The Welsh analogue for Tyrwinghan in [[Languages]] supports initial stress, Welsh u approximated as short i, th as in thin, and a second short-i syllable. RITH-in approximates the Welsh rh without requiring a special phonetic alphabet. The actual in-world name language and phonology are not explicitly recorded, so this is an analogue-informed proposal."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the town and Eirian’s temple teaching as established during Celyn’s studies around DR 1715; her later tenure is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added primary name metadata and supported temporal POV metadata.
- Added the required typed map skeleton without inventing positions.
- Removed the stray “on” before the travel distance.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The typed map block has a blank world-map locator. Supply a verified locator from the map; the linter has not inferred a coordinate.

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry records proposed pronunciation `RITH-in`. The Welsh analogue for Tyrwinghan in [[Languages]] supports initial stress, Welsh u approximated as short i, th as in thin, and a second short-i syllable. RITH-in approximates the Welsh rh without requiring a special phonetic alphabet. The actual in-world name language and phonology are not explicitly recorded, so this is an analogue-informed proposal. Accept or revise it; if accepted, copy the pronunciation to frontmatter and mark the existing entry documented.
%%^End%%

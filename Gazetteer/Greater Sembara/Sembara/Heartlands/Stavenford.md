---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: river town
population: 652
name: Stavenford
pronunciation: Staven-ford
whereabouts: Duchy of Wisford
dm_owner: none
dm_notes: none
POV: modern
---
# Stavenford
*(Staven-ford)*
>[!info]+ Information
> pop. 652
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small river town in the Duchy of Wisford along the [[Enst]], it is about 20 miles downriver of [[Fellburn]]. There is a ferry here. Historically there was a significant fortification here, but the "new town" which was built in the 1670s after the [[Third Hobgoblin War (Sembara)|hobgoblin wars]] dismantled the fortifications to use as building material. 

%% No information really made up, this is basically just a place because I needed a town past Fellburn %%

%%^Metadata:names:v1%%
- {"name": "Stavenford", "language": "unknown", "pronunciation": "Staven-ford", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern, after the rebuilding of the town in the 1670s; the account does not yet incorporate the reported January DR 1720 undead attack.
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

- [ ] **Warning — coverage.established_fact_missing:** [[Letter from Rosalind (January 8th)]] reports a deadly undead attack at Stavenford in January DR 1720, with roughly three dozen deaths according to the residents she consulted. Against the town’s recorded population of 652, this is a significant local consequence. Candidate: “During the [[Undead Attacks in Sembara|undead rising of DR 1720]], Stavenford suffered a deadly attack. [[Rosalind Essford]] reported that residents counted about three dozen dead, many killed by a sword-wielding undead warrior.” Retain the report’s attribution rather than turning the casualty estimate into an omniscient count.
%%^End%%

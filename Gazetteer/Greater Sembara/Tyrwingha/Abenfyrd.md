---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
campaignInfo: null
population: 450
name: Abenfyrd
pronunciation: AY-ben-veered
whereabouts: Tyrwingha
dm_owner: mike
dm_notes: none
POV: modern
---
# Abenfyrd
*(AY-ben-veered)*
>[!info]+ Information  
> pop. 450  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Abenfyrd is a small wooded village along the banks of the [[Aben|Aben River]] known for its timber, and relatively prosperous because of it.

Not much happens in Abenfyrd save the yearly [[Festival of the Miracle of the Mist]], a commemoration of a time when [[The Wanderer]] (it is said) used dense mists to lead a pack of trolls from the [[Plaguelands]] into the Aben, to drown. 

This festival does attract some people from other nearby villages, and the fair held for several days on either side is a major event in Abenfyrd.

There is a large temple to the Wanderer here, which occasionally receives pilgrims, miracle workers, and others seeking the Wanderer's blessing.

%%^Metadata:names:v1%%
- {"name": "Abenfyrd", "language": "unknown", "pronunciation": "AY-ben-veered", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern village economy and recurring festival observance; the commemorated miracle is not assigned a historical year.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving parsed values.
- Added persistent primary name metadata, preserving existing accepted pronunciations and leaving newly composed pronunciations proposed.
- Recorded the supported article viewpoint and concise temporal-coverage metadata.
- Added the required typed settlement map block with its unsupported position left blank.
- Applied the declared objective spelling, punctuation, or grammar corrections; no lore was rewritten.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block has a blank `locator` because no supported world-map hex is established in the reviewed evidence. Supply the village's verified position in `- {map: world, locator: <verified hex>}`; the placeholder is a human task, not a coordinate proposal.
%%^End%%

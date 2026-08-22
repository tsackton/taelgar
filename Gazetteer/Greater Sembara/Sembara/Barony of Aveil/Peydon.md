---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T19:01:27-04:00"
lintVersion: "3.4"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
population: 498
name: Peydon
pronunciation: Pay-dun
whereabouts: Barony of Aveil
dm_owner: mike
dm_notes: important
POV: modern
---
# Peydon
*(Pay-dun)*
>[!info]+ Information  
> pop. 498  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A manorial village along the [[Auberonne]] in [[Barony of Aveil]], it is about 15 miles north of [[Rinburg]] over the fields, and 25 miles by road.

%% Note: It was controlled by a hag for a period in early 1720; some notes in [[Gareth's Story]] %%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: "Peydon", role: "primary", language: "unknown", pronunciation: "Pay-dun", status: "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geographic description; the visible article does not yet incorporate the village's early DR 1720 crisis and aftermath.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting and added the filename-supplied explicit name.
- Added the required settlement map block with its unknown locator left blank.
- Added the required persistent POV, povNotes:v1, and Metadata:names:v1 blocks after contextual review; the accepted frontmatter pronunciation was preserved as documented.
- Corrected the objective typo `manoral` to `manorial`.

### Validated judgments
- The shared comment is a source pointer to [[Gareth's Story]] and was retained unchanged.
- The dm_notes contextual evidence review is not applicable for this note under the current gate.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The map locator remains blank. Fill it from the authoritative world map; do not guess a coordinate.
- [x] **Error — content.internal_conflict:** Frontmatter records `population: 498`, while the visible information callout says `pop. 318`. No other vault source resolves the discrepancy. Confirm the intended population and make those two values agree.
- [ ] **Warning — coverage.established_fact_missing:** [[Gareth's Story]], [[Cleenseau - Session 23]], and [[Cleenseau - Session 24]] establish the village's defining early DR 1720 crisis and its resolution, which the visible article omits. Copy-ready addition: `In early DR 1720, Peydon came under the control of the hag called the [[Midnight Lady]] after the local lord bargained away authority over the village in return for protection from an undead attack. The [[Heroes of Cleenseau]] killed her in March, and the village began recovering from her bargains and curses.`

%%^End%%

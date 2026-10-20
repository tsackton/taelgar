---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
name: Nefyn
pronunciation: NEV-yin
whereabouts: Tyrwingha
dm_owner: mike
dm_notes: none
POV: modern
---
# Nefyn
*(NEV-yin)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small market town about two hours' walk north from [[Clawyn]], a quiet place just before the land starts to rise towards the [[Mostreve Hills]]. Nefyn is known for its wheat, and it is a little bigger than the surrounding villages, and often hosts the Earl on their circuit, and has two blacksmiths, an inn, and an apothecary, as well as a relatively well-attended market on the second and fourth Saturdays of every month.

Its grain and cattle help supply nearby villages, including Clawyn. A dyer also works in the town.

### Notable People
* Trefor, the administrator of the temple to the Father. Elderly, often called Grandfather Trefor.

%% Trefor is trans %%

%%^Metadata:names:v1%%
- {"name":"Nefyn","language":"unknown","pronunciation":"NEV-yin","status":"documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; describes the town’s markets, trades, and regional role, while the resident’s age is an undated detail rather than a history of his life.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting; recorded the explicit subject name and existing pronunciation in name metadata, and added a typed settlement map entry and modern temporal metadata.
- Corrected the hours’ possessive, malformed wheat clause, erroneous plural apostrophes, “well-attended,” and “administrator.”

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The settlement’s `Metadata:map:v1` entry has a blank `locator`; the consulted sources do not establish its world-map hex. Supply the verified coordinate as a string in `  - {map: world, locator: "<verified world hex>"}`. Do not infer the position from a nearby river, settlement, or regional map.
%%^End%%

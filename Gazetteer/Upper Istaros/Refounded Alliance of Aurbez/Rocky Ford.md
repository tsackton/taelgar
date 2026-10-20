---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/text, status/check/lint]
typeOf: settlement
typeOfAlias: trading spot
name: Rocky Ford
whereabouts: Refounded Alliance of Aurbez
dm_owner: none
dm_notes: none
POV: modern
---
# The Rocky Ford
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%%
Rocky Ford, movable town springs up around the ford of the Masance
see [[The Travelogue of Etienne of Cassons]] for a few details

general idea is that the village is recreated each spring where the best fording spot is on the masance, which moves each season; PCs came here in Ausson's game but the details are mostly lost to time as I didn't write them down

The vibe was frontier town/rough justice/slightly crooked place with a "river boss" who controlled the crossing and basically ran the town. could have changed some since the 1680s but should still be a moveable camp more than a real town
%%

%%^Metadata:names:v1%%
- {name: Rocky Ford, language: unknown}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern seasonal-settlement framing; the authored account remains in a shared comment, whose comparison with the 1680s does not establish a precise snapshot.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting; added the existing subject name explicitly.
- Added a minimal name entry; the plain-English name needs no pronunciation, and its source language remains unknown.
- Added a typed settlement map entry with the unsupported locator left blank and broadly modern temporal metadata.

### Validated judgments
- `status/cleanup/text`: **supported** by the absence of visible reference prose and the retained drafting comment; the tag is preserved.
- The comment's remembered “river boss” and rough-justice atmosphere remain unadopted. The travelogue's disputed year is not used to date the settlement.

### Editorial assessment
**Underdeveloped**. The visible note gives only a title and generated information callout. It lacks the central identification of the seasonal settlement, its location at the Masance crossing, and its purpose for travelers. The smallest useful scope is one short paragraph from the established road account and the travelogue, with no new lore or precise historical date required.

### Open findings
- [ ] **Warning — metadata.map_location_missing:** Supply a verified world-map locator in the existing `Metadata:map:v1` settlement entry. The sources establish a shifting Masance crossing but do not establish its map hex; do not infer a coordinate from travel distances or fix the town permanently to a single seasonal position without checking the map convention.
- [ ] **Warning — coverage.established_fact_missing:** All authored description remains hidden in the ordinary comment. [[The Travelogue of Etienne of Cassons]] identifies Rocky Ford as a seasonally shifting camp at the Masance crossing, with ferries, caravan traffic, and flooding hazards. [[Maseau - Dunmar Road]] independently describes a small warm-season town at the shifting Masance fords, disappearing in winter. Add a visible identification such as: “Rocky Ford is a seasonal trading settlement at the crossing of the [[Masance]] on the [[Maseau - Dunmar Road]]. Its site shifts with the river's fords. Guides, tinkers, traders, and other travelers gather here in the warmer months, and the town disperses into the countryside in winter.” The travelogue corroborates the identification, but its author's dating comment leaves its exact year unresolved; omit an exact date and keep the comment's uncorroborated river-boss detail for separate human adoption.
%%^End%%

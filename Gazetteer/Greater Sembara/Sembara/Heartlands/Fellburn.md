---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/text, status/check/lint]
typeOf: settlement
subTypeOf: null
typeOfAlias: fortified market town
population: 6000
name: Fellburn
pronunciation: Fell-burn
whereabouts: Duchy of Wisford
dm_owner: mike
dm_notes: color
POV: modern
---
# Fellburn
*(Fell-burn)*
>[!info]+ Information  
> pop. 6,000  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A populous and fortified town along the [[Enst]], it was historically the "second city" of the Enst, smaller than [[Rinburg]]. However, since the [[Third Hobgoblin War (Sembara)|hobgoblin wars]], Fellburn has grown substantially and has overtaken [[Rinburg]] to become the largest city along the Enst.

%%^Metadata:names:v1%%
- {"name":"Fellburn","language":"unknown","pronunciation":"Fell-burn","status":"documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern post-hobgoblin-war growth and regional prominence; the DR 1720 siege and succession are not yet incorporated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added persistent name metadata, retaining documented pronunciations and keeping derived readings proposed.
- Added the typed settlement map block with its unknown locator left blank.
- Added modern POV and persistent temporal-coverage metadata.

### Validated judgments
- The local dm_notes contextual review is not applicable for dm_owner: mike; the broad dossier match does not reopen it. The existing status/cleanup/text is not assessable without its author’s intended cleanup scope and is preserved.

### Editorial assessment
**Underdeveloped**. The visible note identifies growth and regional size, but omits its established military role and the consequential DR 1720 siege and succession. The smallest useful scope is a brief account of the garrison role plus a dated paragraph on the defeat of the undead siege and Elise Moreau’s appointment; no campaign travel log is needed.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — metadata.map_location_missing:** The required settlement map block is now present, but its `map: world` entry has a blank `locator`. Supply an established map coordinate for this settlement; the typed placeholder deliberately makes no location claim.

- [ ] **Warning — coverage.established_fact_missing:** [[Army of the South]] establishes Fellburn as a garrison base, a defining institutional role absent from the town’s current account. Bounded candidate: “Before the undead attacks of DR 1720, Fellburn housed a garrison of the [[Army of the South]].” Keep the pre-crisis framing because the army account also records its subsequent dispersal.

- [ ] **Warning — coverage.later_material_change:** [[Cleenseau - Interlude - After the Siege of Fellburn]] records the defeat of the undead siege and the settlement of Fellburn’s succession, with [[Elise Moreau]] appointed baroness. These are durable changes to the city’s account. Candidate: “In DR 1720, an undead army besieged Fellburn. After the siege was broken, [[Jacques Bellemont]], Duke of Wisford, appointed [[Elise Moreau]] as Baroness of Fellburn.” Choose whether to incorporate this history and review the temporal framing, defer it with a human game-update disposition, or intentionally retain the earlier account. The lint does not alter game-update tags.
%%^End%%

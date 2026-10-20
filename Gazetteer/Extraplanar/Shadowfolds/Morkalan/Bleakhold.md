---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
destroyed: 1748-08-26
name: Bleakhold
whereabouts: Morkalan
dm_owner: tim
dm_notes: none
POV: 1748
---
# Bleakhold
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A dismal Dwarven village along the [[Muddy River]], in the [[Shadowfolds]] domain of [[Morkalan]]. 

%%^Date:1748-08-26%%
It was described by the dwarves who were rescued from Morkalan as a large village, home to maybe 800 people. However, it usually felt much smaller, as few ever left their homes, except at need, to fetch water or harvest the wild grasses and rice that grew along the [[Muddy River]] and seemed to provide sufficient sustenance for what passed for life in [[Morkalan]]. It was tunneled into the cliffs, although a large number of buildings were also poorly constructed of mud and stone along the river's edge. 
%%^End%%


%%^Campaign:none%%
Raw DM notes
## Overview

Bleakhold is a dwarven village, home to about 800 people these days. About 2/3 of the buildings are built of stone and mud (poorly, for dwarves) or carved into the cliffs, while the rest is tunneled into several large caverns in the cliff face.

There is no real obvious source of food, although they seem to have enough to eat, or at least enough to survive. The village itself is a pale reflection of life - few sounds disturb the quiet of Morkalan.

## The Watch

Village is watched, and watchers are watched, so new arrivals will be reported.

## Scenes

Upon approaching the village, a few possible scenes.

1. The guards, in a monotonous ritual, pacing back and forth, seeming not to really notice anything, slow to react. At the end of each pace back and forth, pause staring off into the distance for a moment. Once the characters are noticed, one will leave, saying little and ignoring any conversation.
2. Rurik, a dwarf of indeterminant age but at least middle-aged, sobbing quietly, barely audible, trying to keep his despair from the other villagers. His son, Tak has not returned from a his wandering, usually he comes back by nightfall, or in a few days, but it has been nearly a week now. He has little to go on, other than that Tak traveled "upriver", and often likes to try to find the ghost of his mother.

Most of the village, such as it is, is shut tight, few dwarves ever leave their homes. Most houses have either specters, wights, or dust and ash using mephit stats, or people cowering.

The key should be that most cannot remember their past, and over time memories of the outside world fade particularly quickly.

Most dwarves should have forgotten their clan name by now.

Names: Kilvar, Gardain, Dworic, Baern, Caebrek, Sannl, Thodris, Urshar, Bardryn

Kilia - old woman
Dworic - smith
Rurik - father of Tak
Tak - kid

%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Bleakhold, language: Common, status: inferred, notes: descriptive Common name}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 historical description of Bleakhold before Morkalan's destruction; the dated paragraph reports the rescued inhabitants' retrospective account from August 26 onward.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting without changing existing values.
- Added a descriptive Common name entry and a DR 1748 historical POV with its retrospective temporal interpretation.
- Added the required typed settlement map skeleton with its locator left blank.

### Validated judgments
- The settlement's setting, approximate population, dwellings and subsistence provide a sufficient bounded historical description; the destruction date and rescued-inhabitant frame already identify it as a former community.
- Bleakhold is a transparent English compound and needs no pronunciation; [[Languages]] supports treating such descriptive written place names as Common.
- The shared DM block mixes duplicated overview prose with distinct encounter guidance; no private material was promoted automatically.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block contains `{map: world, locator: }`, but neither the article nor the consulted Morkalan description establishes a supported map position. Supply a verified map and locator for the historical settlement, using an appropriate planar map if one exists. Do not infer a Material Plane hex from the domain's shadowy correspondence to Dunmar.

- [ ] **Suggestion — editorial.shared_material_redundant:** The `Campaign:none` block's “Overview” repeats the visible population of about 800, the stone-and-mud or cliff dwellings, and the unusually quiet, withdrawn village. Remove those duplicate overview statements, or retain only distinct editorial qualifications that the author still needs. Keep “The Watch,” the encounter scenes, NPC roster, and memory/clan-name guidance together as DM material under the existing wrapper. The old observation that no food source is obvious should remain explicitly provisional or be removed in light of the visible subsistence description; it is not an independent factual contradiction. This bounded split leaves public history in the article and usable encounter guidance in the shared DM block.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/The Domain of Morkalan/The Domain of Morkalan]]
%%^End%%

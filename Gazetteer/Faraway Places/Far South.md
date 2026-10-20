---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/map, status/check/lint]
typeOf: region
name: Far South
whereabouts:
  - {type: home, location: Taelgar, linkText: in}
dm_owner: none
dm_notes: none
POV: modern
---
# The Far South
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

In the markets of [[Tollen]] or [[Chardon]], rumors are occasionally heard of great lands faraway to the south and east, where creatures as tall as castles roam and the air is sticky and wet. Others tell of an endless desert, where oases bloom with flowers the size of trees, but death awaits those who lose their way in the endless heat and sand. What truth there is to these rumors is not known.
## Map

{link to leaflet map of region}
## Topography and Major Features
This region is shrouded in mystery, and only a few features are rumored. Many reports of a [[Great Desert|endless desert]] stretching for thousands of miles have come west, but beyond that, few know what mysteries this region holds.

%%^Campaign:DuFr%%
[[Kenzo]] brought stories of a tropical jungle called [[Orekatu]] by the [[Lizardfolk|lizardfolk]] who dwell there.
%%^End%%
## Civilizations and Cultures
What civilizations live in this region, beyond -- or within -- the desert is not known.
## Climate
The climate of this region is varied, and not well known - but all the stories tell of hot and humid, or hot and dry places. 

%%^Campaign:None%%
There are no real canonical details about this region's climate although it is exclusively subtropical and tropical. The [[Great Desert]] is similar in size and climate to the Sahara; [[Orekatu]] has a tropical jungle feeling, perhaps similar to Panama.
%%^End%%

## Major Historical Eras
_See more: the [[Founding of Dunmar]]_

Nothing is known of the history of this region. Any people who live here are likely strange and foreign compared to the descendants of [[Drankor]]. The [[Dunmar|Dunmari]] claim to have come east from somewhere in this region soon after the fall of Drankor, but the exact location of the ancient Dunmari homeland has been lost.

%%^Campaign:None%%
## DM Notes and Meta
*Area:* This region is poorly defined as little geographic development exists, but functionally it is everything east of the [[~Eastern Mountains~]] and south of the Green Sea coastal realms. 

*Canonical Development and Constraints:* The swamps and jungles of [[Orekatu]] have some basic canonical development, primarily on geography and climate. There is canonically a great desert somewhere in this region. Dinosaurs canonically live in [[Orekatu]], at least, and are in some cases partially domesticated by [[Lizardfolk]]. Some halfling ships do occasionally trade to the south (or from the south?) to Chardon and exotic goods can be occasionally found in the markets there. Whether human ships also make these journeys is undetermined but relatively unlikely. 

*Brainstorming and Potential Canon:* Gnomes are generally thought to inhabit this region, but details are vague. Hints of an ancient trading civilization (Targu) exist, but details are vague / non-existent. The Dunmari homeland is likely in this region, although the exact location is unclear.

*Needs Development:* None. 

*Intentionally Blank:* This area is explicitly left blank and should not be developed without careful consideration. 

*Adventures:* The Kenzo solo arc from the Dunmar Frontier campaign was set in western Orekatu and the [[Azta Lekua|Footprint of the Gods]] immediately to the west of [[Orekatu]], but otherwise this region has seen no play time. 

*Important Places in Staging:* None are critical but the [[Great Desert]] could use a name (even if that is just "the Great Eastern Desert" or similar). 
%%^End%%

%%^Metadata:names:v1%%
- {name: Far South, language: Common, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern, rumor-led account of the poorly known southern and eastern lands, with Dunmari origin traditions as historical background; detailed regional chronology remains undeveloped.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting while preserving the existing map-cleanup status and all campaign markers.
- Corrected singular agreement in “What truth there is to these rumors”.
- Added minimal name metadata for the plain-English geographic title and broadly modern temporal coverage notes.

### Validated judgments
- The region’s intentional blankness is explicit in its DM planning and corroborated by [[Human Cultures of Taelgar]]. That deliberate limit does not require new regional invention.
- `status/cleanup/map` remains supported by the visible map placeholder. The ordinary-English title needs no pronunciation guide. Both legacy private blocks were reviewed as mixed development constraints, analogues, and unresolved planning; their visibility and speculative material are preserved.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** “What civilizations live in this region … is not known” and “Nothing is known of the history of this region” omit bounded established exceptions. [[Orekatu]] identifies an ancient lizardfolk kingdom, and [[Khemut of Targu]] records a Far South island port trading tea and spices with Drankor before her disappearance in DR 1043. Qualify the absolute claims while preserving the region’s largely unknown character and any intended campaign knowledge scope. Candidate summary: “The societies and history of the region remain poorly known. [[Orekatu]] is an ancient lizardfolk kingdom, while Targu was an island port that traded tea and spices with [[Drankor]] in the early eleventh century DR; its present condition is not established.” Do not infer modern trade or modern survival of Targu.

- [ ] **Warning — correctness.cross_note_conflict:** The Major Historical Eras passage says the Dunmari “come east from somewhere in this region,” whereas the Dunmari section of [[Human Cultures of Taelgar]] says they travelled west from an eastern homeland after the Fall of Drankor. Reconcile the direction without choosing an exact lost homeland. Candidate replacement for only that sentence: “The [[Dunmar|Dunmari]] trace their origins to an eastern homeland, but its exact location has been lost.” Preserve attribution and uncertainty; [[Founding of Dunmar]] is a mythic founding account and does not fix the homeland’s location.

- [ ] **Warning — correctness.shared_nonpublic_conflict:** The first legacy private block begins “There are no real canonical details about this region’s climate,” but K29–K30 of [[Climate and Weather Constraints]] retain broad Great Desert interior aridity and tropical warmth and moisture compatible with Orekatu’s forests. Replace that obsolete blanket claim while leaving detailed seasons and boundaries open. Candidate for that first sentence only: “Canonical climate constraints establish broad desert-interior aridity and tropical warmth and forest moisture in Orekatu; detailed rainfall seasons and regional boundaries remain open.” Retain the distinct real-world analogues inside their existing private wrapper.

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The note uses `%%^Campaign:DuFr%%` once and `%%^Campaign:None%%` twice. The canonical opening markers are `%%^Campaign:dufr%%` and `%%^Campaign:none%%` respectively. Confirm equivalent export visibility, then replace only these three opening markers; preserve their enclosed text, ordering, and closing markers.
%%^End%%

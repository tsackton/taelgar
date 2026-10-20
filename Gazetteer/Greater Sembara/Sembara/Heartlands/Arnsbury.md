---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
population: 4500
name: Arnsbury
whereabouts: Duchy of Arnsbury
dm_owner: none
dm_notes: none
POV: modern
---
# Arnsbury
>[!info]+ Information  
> pop. 4,500  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The largest city in the [[Duchy of Arnsbury]] and the seat of the Duke. Although smaller than [[Fellburn]], [[Telham]], and [[Embry]], it is larger than most other cities in Sembara and has ancient roots.

%% 

Old Plaguelands Campaign Note: Large market town in central Sembara; small village outside Arnsbury is where Evendur grew up

%%

%%^Metadata:names:v1%%
- {"name": "Arnsbury", "language": "unknown", "pronunciation": "ARNZ-buh-ree", "status": "proposed", "notes": "The northern Sembaran setting favors the English side of the Sembaran analogue in [[Languages]]: initial stress, Arnz with voiced z, and unstressed bury as buh-ree. This is an analogue-informed proposal; the source language and exact in-world reading are unrecorded."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern identification, relative size, and ducal-seat role of Arnsbury; no individual living duke or dated city state is asserted.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected “larger that most other cities” to “larger than most other cities.”
- Normalized frontmatter field order and collection formatting without changing existing values.
- Added primary name metadata with a proposed pronunciation and its derivation.
- Added the required single-location map skeleton with its unknown locator left blank.
- Recorded the article POV and a persistent temporal-coverage interpretation.

### Validated judgments
- The legacy comment was reviewed as campaign provenance rather than adopted city lore.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The settlement has no established world-map locator in the reviewed evidence. Supply the actual coordinate in the existing `locations` entry, keeping `map: world`; do not infer a hex from nearby places.

- [ ] **Warning — metadata.names_unresolved_status:** Review `ARNZ-buh-ree` in `Metadata:names:v1`. The northern Sembaran setting favors the English side of the Sembaran analogue in [[Languages]]: initial stress, Arnz with voiced z, and unstressed bury as buh-ree. This is an analogue-informed proposal; the source language and exact in-world reading are unrecorded. Accept or revise the complete reading; if accepted, copy it to frontmatter and mark the entry `documented`.

%%^End%%

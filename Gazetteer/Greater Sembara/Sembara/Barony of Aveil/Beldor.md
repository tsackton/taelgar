---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: mining village
name: Beldor
whereabouts: Barony of Aveil
dm_owner: none
dm_notes: none
POV: modern
---
# Beldor
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small village in the hills about a day and a half walk north of [[Veltor]], it is one of several small tin mining camps and villages in the [[Aveil Ridge]]. No road leads south to Veltor from here, but a rough track leads north towards the [[Wistel]] on which raw ores are transported.

%%^Metadata:names:v1%%
- {"name": "Beldor", "language": "unknown", "pronunciation": "bel-DOR", "notes": "Proposed from the French strand of the regional Sembaran analogue in [[Languages]]: e as in belle, audible l and d, rounded open o, final r, and final-syllable emphasis. The name-specific language and exact in-world phonology are unestablished.", "status": "proposed"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the subject in the current campaign era; the article does not require a narrower temporal reading position.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported name and/or map metadata where absent and a temporal viewpoint with coverage guidance; normalized frontmatter where needed.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or replace the proposed `bel-DOR`. The French strand of the regional Sembaran analogue in [[Languages]] motivates e as in belle, audible l and d, an open rounded o, final r, and final emphasis. This is a regional analogue-based proposal; no exact name-specific language or pronunciation is established. On acceptance, copy it to frontmatter and mark the name entry documented.
- [ ] **Warning — metadata.map_location_missing:** The settlement map skeleton has no confirmed locator. Supply its world-map position in `locations: [{map: world, locator: <confirmed locator>}]`; relative walking distance from Veltor does not establish a coordinate.
%%^End%%

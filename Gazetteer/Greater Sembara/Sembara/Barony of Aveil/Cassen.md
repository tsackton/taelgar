---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
population: 35
name: Cassen
whereabouts: Barony of Aveil
dm_owner: none
dm_notes: none
POV: 1720
---
# Cassen
>[!info]+ Information  
> pop. 35  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small village on the [[Great South Road]] between [[Dallet]] and [[Champimont]]. It was recently decimated by the [[Undead Attacks in Sembara]] and much of the population was killed, including most of the lord's guard.

The zombies apparently wandered north towards [[Cleenseau Wood]], and the village is terrified to leave their houses.

%%^Metadata:names:v1%%
- {"name": "Cassen", "language": "unknown", "pronunciation": "KASS-en", "status": "proposed", "notes": "[[Languages]] gives Sembaran French and English analogues. The preferred English adaptation uses hard c, short a, ss as s, and initial stress; a French-influenced alternative would be kah-SAHN with a nasal final vowel. No accepted village pronunciation or uniquely established name language was found, so this choice remains proposed."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 snapshot shortly after the January undead attacks; the surviving population and immediate fear are not a claim about later recovery.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added primary name metadata and supported temporal POV metadata.
- Added the required typed map skeleton without inventing positions.
- Corrected “popluation” and supplied the missing verb in “much of the population was killed”.

### Validated judgments
- [[Elizabeth of Cassen's Story]] corroborates the devastating undead attack and the loss of the village guard.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The typed map block has a blank world-map locator. Supply a verified locator from the map; the linter has not inferred a coordinate.

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry records proposed pronunciation `KASS-en`. [[Languages]] gives Sembaran French and English analogues. The preferred English adaptation uses hard c, short a, ss as s, and initial stress; a French-influenced alternative would be kah-SAHN with a nasal final vowel. No accepted village pronunciation or uniquely established name language was found, so this choice remains proposed. Accept or revise it; if accepted, copy the pronunciation to frontmatter and mark the existing entry documented.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: market town
name: Cienne
whereabouts: Duchy of Wisford
POV: modern
---
# Cienne
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Cienne is a market town on the [[Great South Road]], about twenty miles from [[Fellburn]].

%%^Metadata:names:v1%%
- {"name": "Cienne", "language": "unknown", "pronunciation": "SYENN", "status": "proposed", "notes": "The southern Sembaran setting favors the French side of the Sembaran analogue in [[Languages]]: soft c before i, ie as a y glide plus eh, sounded n from doubled nn, and silent final e. SYENN is one syllable; the source language and exact in-world reading are unrecorded."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern identification and location of the market town.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected “market town othe” to “market town on the.”
- Added primary name metadata with a proposed pronunciation and its derivation.
- Added the required single-location map skeleton with its unknown locator left blank.
- Recorded the article POV and a persistent temporal-coverage interpretation.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The settlement has no established world-map locator in the reviewed evidence. Supply the actual coordinate in the existing `locations` entry, keeping `map: world`; do not infer a hex from nearby places.

- [ ] **Warning — metadata.names_unresolved_status:** Review `SYENN` in `Metadata:names:v1`. The southern Sembaran setting favors the French side of the Sembaran analogue in [[Languages]]: soft c before i, ie as a y glide plus eh, sounded n from doubled nn, and silent final e. SYENN is one syllable; the source language and exact in-world reading are unrecorded. Accept or revise the complete reading; if accepted, copy it to frontmatter and mark the entry `documented`.

%%^End%%

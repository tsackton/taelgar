---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T19:36:26-04:00"
lintVersion: "3.2"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Argento
whereabouts:
  - {type: primary, location: Alta Tonaro}
dm_owner: tim
dm_notes: important
POV: modern
---
# Argento
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Argento is the largest city, and provincial capital, of [[Alta Tonaro]]. Founded during the boom years of chalyte mining in the northern [[Chataan Mountains]], its fortunes have declined significantly over the past two generations. Now, its economy depends largely on a few productive silver mines.

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: "Argento", role: "primary", language: "Chardonian", pronunciation: "ar-JEN-toh", notes: "Italian analogue: soft g before e, final o, and penultimate stress.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a post-boom view of Argento after surface chalyte production ended, when the city's economy rests on its remaining silver mines. Chalyte mining resumes in the region in DR 1749 and dramatically changes Alta Tonaro; the article does not describe Argento's resulting later state.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Completed the full linter 3.2 review and refreshed the atomic lint completion state.
- Reassessed the article viewpoint and replaced the legacy Metadata:article block with persistent POV and povNotes:v1 metadata.
- Added the applicable persistent Metadata:names:v1 entry after the independent name review.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Map position fields remain incomplete: locator. Fill only the blank locator values from the authoritative map; do not guess coordinates.
- [ ] **Warning — metadata.names_unresolved_status:** Persistent name review remains open for `Argento — ar-JEN-toh` (proposed). Review the recorded language, pronunciation, and derivation; then accept it in frontmatter where appropriate or correct the persistent entry.

%%^End%%

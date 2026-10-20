---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: town
name: Ainwick
whereabouts: Barony of Ainwick
dm_owner: none
dm_notes: none
POV: modern
---
# Ainwick
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A town in western Sembara, on the upper reaches of the River Wistel. This is an important communication and market hub for the upper reaches of the [[Wistel]] river. Although the [[Army of the West]] is based further west, along the [[Western Wall of Sembara]], Ainwick is in many ways the spiritual heart of the army.

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Ainwick", "language": "unknown", "pronunciation": "AYN-wik", "status": "proposed", "notes": "Preferred proposal from the English analogue available for Sembaran in [[Languages]]: ai as in rain, pronounced w in wick, short i, hard k, and initial stress. A French-influenced reading could instead nasalize Ain and use an ee-like final vowel; the name’s language and exact phonology are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern account of the town’s communication, market, and military roles; the article does not narrate the DR 1720 attacks.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added persistent name and temporal metadata; preserved header versions, human attestations, and non-lint statuses.
- Added the required single-location map skeleton, leaving its unknown locator blank.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the persistent proposed pronunciation `AYN-wik`. [[Languages]] supplies both English and French analogues for Sembaran, but the name’s source language is unestablished. The preferred English adaptation uses ai as in rain, pronounced w, short i, hard k, and initial stress; a French-influenced reading could instead nasalize Ain and use an ee-like final vowel. Accept it by copying `pronunciation: AYN-wik` to frontmatter and marking the entry documented, or revise the persistent proposal.
- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now contains `{map: world, locator: }`. A human must supply Ainwick’s verified world-map locator; leave it blank until established.
%%^End%%

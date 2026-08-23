---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T12:50:50-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
name: Luminatia
whereabouts: Chardonian Empire
dm_owner: none
dm_notes: color
POV: "1749"
---
# Luminatia
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small village near [[Lake Valandros]].

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: "Luminatia", role: "primary", language: "Chardonian", pronunciation: "loo-mee-NAH-tee-ah", notes: "Latin/Italian analogue: pure vowels and stress on na.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: DR 1749. Minimal settlement reference at the time of the Session 86 contact; broader history and later state are not established here.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected `POV` and `povNotes:v1` from DR 1748 to DR 1749, matching [[Session 86 (DuFr)]].

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map locator remains blank in `Metadata:map:v1`. Fill the `locator` from the authoritative map; do not guess coordinates.
- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry for `Luminatia — loo-mee-NAH-tee-ah` remains `status: proposed`. Review its Chardonian language basis and analogue-derived pronunciation, then either accept it by adding `pronunciation: loo-mee-NAH-tee-ah` to frontmatter and marking the entry documented, or correct the persistent entry.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No local-only `_DM_` notes were found for Luminatia. Verify that `dm_notes: color` still reflects remembered or off-vault material; if not, a human may change the attestation to `dm_notes: none`.
%%^End%%

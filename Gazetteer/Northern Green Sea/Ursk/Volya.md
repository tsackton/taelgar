---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: trading post
name: Volya
pronunciation: VOH-leeah
whereabouts: Ursk
dm_owner: none
dm_notes: color
POV: modern
---
# Volya
*(VOH-leeah)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small walled village and trading post at the confluence of the [[Leis]] and the [[Beyil]] rivers.

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name":"Volya","language":"unknown","pronunciation":"VOH-leeah","status":"documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern settlement geography and reference description; no narrower current-era viewpoint is required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added the explicit name, a documented name entry preserving the accepted `VOH-leeah` pronunciation, and broadly modern temporal metadata.
- Added the required settlement map block with a blank world-map locator.

### Validated judgments
- [[Leis]] and [[Session 95 (DuFr)]] corroborate the confluence location and trading-post role. The brief visible account performs its bounded connector role.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The world-map locator for Volya is blank. Supply a verified coordinate in the existing single-location map entry; the river confluence identifies the site without establishing a hex.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. The complete prepared local dossier has no candidates, while the shared Leis entry and Session 95 establish the public confluence/route context. The attestation may still represent remembered information or an off-vault source, so it has been preserved. Confirm the existing value or make the human-authored correction appropriate to the remaining private information.
%%^End%%

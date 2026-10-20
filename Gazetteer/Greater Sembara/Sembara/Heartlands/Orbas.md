---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
destroyed: 1720-01-10
name: Orbas
whereabouts: Duchy of Wisford
dm_owner: none
dm_notes: color
POV: modern
---
# Orbas
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small village near [[Fellburn]], it was deserted during the [[Undead Attacks in Sembara]].

%%^Metadata:names:v1%%
- {"name":"Orbas","language":"unknown","pronunciation":"or-BAH","status":"proposed","notes":"French-informed southern Sembaran proposal under [[Languages]]: open o before r, a as ah, silent final s, and final-group prominence. An English-like OR-buhs is also possible; the name-specific language and sound rules are not documented."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective description of the village deserted during the DR 1720 undead attacks; subsequent resettlement is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added the explicit display name from the existing title and filename.
- Added persistent name metadata, retaining documented pronunciations and keeping derived readings proposed.
- Added the typed settlement map block with its unknown locator left blank.
- Added modern POV and persistent temporal-coverage metadata.

### Validated judgments
- The planned family return recorded in [[Hugh Cosson]] does not establish completed resettlement; the village article does not assert later resettlement.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block is now present, but its `map: world` entry has a blank `locator`. Supply an established map coordinate for this settlement; the typed placeholder deliberately makes no location claim.

- [ ] **Warning — metadata.names_unresolved_status:** The persistent entry proposes `or-BAH`, using the southern French Sembaran analogue in [[Languages]]: open o before r, a as ah, silent final s, and final-group prominence. `OR-buhs` is a possible English alternative. Exact name language is unestablished; accept the reading in frontmatter and mark it documented, or correct the proposal.

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The existing `dm_notes: color` may refer to remembered or off-vault material; preserve the attestation until its human owner decides.
%%^End%%

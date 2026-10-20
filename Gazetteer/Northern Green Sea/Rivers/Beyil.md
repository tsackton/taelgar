---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Beyil
pronunciation: BEY-eel
whereabouts: Ursk
dm_owner: none
dm_notes: color
POV: modern
---
# Beyil
*(BEY-eel)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Beyil, from the Urskan word for "White", is a slow, winding river that flows from the [[Yengorza Mountains]] to the [[Green Sea]]. After quickly cascading from the mountains to the flat coastal plains, the Beyil becomes wide and slow, winding across the flat lowlands. In the summer months, it is navigable for much of its length by river boat, and in the winter months, once frozen, by sledge.

%%^Metadata:names:v1%%
- {"name":"Beyil","language":"Urskan","pronunciation":"BEY-eel","meaning":"White","status":"documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Yengorza Mountains, map: world, locator: }
  - {role: outlet, feature: Green Sea, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference geography; no narrower temporal anchor is established for the visible description.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added the explicit name.
- Recorded the article’s Urskan derivation, meaning “White,” and accepted frontmatter pronunciation in persistent name metadata.
- Added broadly modern temporal metadata and the required source/outlet map skeleton, using the river’s stated source and outlet features.

### Validated judgments
- The visible account sufficiently identifies this bounded river, its course, and its seasonal transport role.
- The accepted pronunciation is preserved; no pronunciation proposal is needed.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Both `Metadata:map:v1` locators remain blank: the source in the [[Yengorza Mountains]] and the outlet in the [[Green Sea]]. Supply each verified world-map coordinate as a quoted `locator` value; the geographic prose does not determine an exact hex.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. The direct-identity dossier has no matches. Keep the human attestation unless its owner confirms a change; remembered or off-vault material may support it.
%%^End%%

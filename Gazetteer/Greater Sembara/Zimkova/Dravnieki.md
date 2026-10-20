---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T06:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
name: Dravnieki
pronunciation: DRAHV-nyeh-kee
whereabouts: Breva
dm_owner: mike
dm_notes: none
POV: modern
---
# Dravnieki
*(DRAHV-nyeh-kee)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Dravnieki is a small village in [[Zimkova]], on the upper reaches of the [[Teft]]. 

%%^Campaign:none%%

In the Chasm intro context:

After an unexpected fall of hunting orcs, Justas and Finnan, you are wintering in the small village of Dravnieki (DRAHV-nyeh-kee) on the banks of the upper Teft. The village was attacked twice by orcs, and you are here in part as a favor to the village elders, as added protection in case more dangers come out of the winter. Other than the rumors around the Chasm, it has been a quiet winter, although you wonder about the omens, and think maybe a journey to the Chasm would be interesting, come spring.

%%^End%%

%%^Metadata:names:v1%%
- {"name":"Dravnieki","language":"unknown","pronunciation":"DRAHV-nyeh-kee","status":"documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern identification and river location; the separate shared DM block preserves an Into the Chasm opening scenario rather than dating the visible article.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized frontmatter and added a primary name entry using the accepted frontmatter pronunciation.
- Added the typed settlement map skeleton and modern temporal metadata.

### Validated judgments
- The village identity and upper-Teft location suffice for this minor place; the shared campaign-opening material remains separately hidden.
- The local DM-attestation review is not applicable for `dm_owner: mike`; this does not suppress the separate Campaign:none review.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The settlement row in `Metadata:map:v1` has a blank `locator`. Supply an established world-map coordinate for Dravnieki; the prose location on the upper [[Teft]] does not determine an exact hex, so do not guess one.
- [ ] **Suggestion — editorial.public_material_candidate:** The Campaign:none paragraph beginning "After an unexpected fall of hunting orcs" contains a developed village-security account. For human adoption, a bounded public sentence is: "Dravnieki has endured two orc attacks, and the village elders have sought outside help to guard against further danger." This gives the village a specific history without narrating a party visit. Confirm the opening-scenario account before adoption and retain the remaining campaign setup and omens as private guidance.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-24T09:25:51-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [place, status/gameupdate/gl, status/check/lint]
typeOf: inn
name: The Wandering Toad
whereabouts:
  - {type: primary, location: Voltara}
dm_owner: tim
dm_notes: important
POV: 1747
---
# The Wandering Toad
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small, welcoming inn just inside the city walls of [[Voltara]]. Known for wild game, mushrooms, and ale, and run by the unusually large halfling [[Finoc Small]]. 


%% Great Library

 Considered comfortable accommodations, 2 gp for food, drink, lodging.

Served as lodging for the party during planning for the [[Battle of Voltara]]. [[Brelith]] apprenticed with the chef here before opening [[The Hero's Feast]].

%%

%%^Metadata:names:v1%%
- {name: The Wandering Toad, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1747 snapshot of the inn under Finoc Small's proprietorship; its later status is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added a minimal name entry; the plain-English inn name does not require a pronunciation.
- Added `POV: 1747` and a persistent temporal-coverage note for Finoc Small's proprietorship.

### Validated judgments
- `status/gameupdate/gl` is not assessable because the reviewed sources establish the DR 1747 inn state but no later change to the inn.

### Open findings

- [ ] **Suggestion — dm.notes_no_local_evidence:** No local-only `_DM_` note was found for the positive `dm_notes: important` attestation. Verify whether the attestation refers to remembered or off-vault information; do not remove or change it automatically.
- [ ] **Suggestion — editorial.public_material_candidate:** The Git-shared Great Library comment mixes incidental party lodging with a durable fact corroborated by [[Finoc Small]]. Add only: “Before opening [[The Hero's Feast]], [[Brelith]] apprenticed with the chef at the Wandering Toad.” Retain the lodging note privately only if it remains useful campaign guidance.
%%^End%%

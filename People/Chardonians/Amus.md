---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T18:23:23-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Chardonian
born: 1726
campaignInfo:
  - {campaign: grli, type: ransomed, date: 1747-07-10}
name: Amus
pronunciation: AH-moos
whereabouts:
  - {type: home, location: Chardon}
  - {type: away, start: 1747-07-06, end: 1747-07-16, location: Greater Voltara}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1747
---
# Amus
*(AH-moos)*
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Ransomed grli on July 10th, 1747 in [[Greater Voltara]], the [[Northern Provinces]], the [[Chardonian Empire]] %%^End%%

Amus is a young, brash man, a swift rider who serves the Great Library as a messenger. %%^Date:1747-07-10%%In DR 1747, Amus was kidnapped by kobolds on the road to Voltara, and [[Great Library Session Notes - Arc 1#Session 16|eventually ransomed]] by the [[Silver Tempests]].%%^End%%

%%
Referenced: GL Arc 1 — ransomed by the party; left safely in a hidden camp during the operation.

The messenger, Amus, is a young, brash man, shaken by the experience of being a hostage. However he is dedicated to the library and once exchange is made and he is ungagged will tell them that they need to get the map.
%%

%%^Metadata:names:v1%%
- {name: Amus, role: primary, language: Chardonian, pronunciation: AH-moos,  status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1747 encounter portrait centered on Amus's service as a Great Library messenger and his ransom from kobolds; earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- None.

### Validated judgments
- The current Great Library session record confirms Amus's ransom and the kobolds' retention of the map; its later edit does not add a material post-ransom change.

### Open findings

- [ ] **Warning — content.internal_conflict:** The campaign header says `Ransomed grli`, while the article and [[Great Library Session Notes - Arc 1#Session 16|Session 16]] say the [[Silver Tempests]] ransomed Amus, and the live campaign registry identifies `grli` as the Great Library campaign code with the Silver Tempests as its party. Candidate: `>> %%^Campaign:grli%% Ransomed by the [[Silver Tempests]] on July 10th, 1747 in [[Greater Voltara]], the [[Northern Provinces]], the [[Chardonian Empire]] %%^End%%`
- [ ] **Suggestion — editorial.public_material_candidate:** The hidden comment partly repeats the visible ransom account but adds a coherent public-safe aftermath: Amus was shaken, remained dedicated to the Great Library, and immediately warned that the kobolds still had the map. Candidate: `Though shaken by his captivity, Amus remained dedicated to the Great Library and warned his rescuers that the kobolds still held the map he had been carrying.` After adoption or rejection, remove the repeated ransom summary from the hidden comment.
%%^End%%

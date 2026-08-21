---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T13:33:35-04:00"
lintVersion: "3.4"
tags: [person, status/check/lint]
species: human
ancestry: Chardonian
born: 1726
campaignInfo:
  - {campaign: grli, type: ransomed, date: 1747-07-10}
name: Amus
whereabouts:
  - {type: home, location: Chardon}
  - {type: away, start: 1747-07-06, end: 1747-07-16, location: Greater Voltara}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1747
---
# Amus
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Ransomed by the [[Silver Tempests]] on July 10th, 1747 in [[Greater Voltara]], the [[Chardonian Empire]] %%^End%%

Amus is a young, brash man, a swift rider who serves the Great Library as a messenger. 

%%
Referenced: GL Arc 1 — ransomed by the party; left safely in a hidden camp during the operation.

The messenger, Amus, is a young, brash man, shaken by the experience of being a hostage. However he is dedicated to the library and once exchange is made and he is ungagged will tell them that they need to get the map.
%%

%%^Metadata:names:v1%%
- {name: Amus, role: primary, language: Chardonian, pronunciation: AH-moos, notes: "Proposed from the Latin analogue documented for Chardonian; exact in-world phonology is not recorded.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1747 encounter portrait centered on Amus's service as a Great Library messenger and his ransom from kobolds; earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized the Great Library campaign code to `grli`, added `knownTo: [grli]`, and added persistent name and temporal metadata.

### Validated judgments
- The shared comment is a source pointer and encounter-planning note; public-safe facts are independently established by [[Great Library Session Notes - Arc 1]].

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The visible biography omits Amus's only established campaign episode. Copy-ready addition from [[Great Library Session Notes - Arc 1]]: `In DR 1747, the [[Silver Tempests]] ransomed Amus from kobolds while seeking the map to the last of the [[Elemental Scrolls of Airion]]. The kobolds had taken the map, so the party left him safely in a hidden camp while recovering it.`
- [ ] **Warning — metadata.names_unresolved_status:** Persistent name review remains open for `Amus — AH-moos` (proposed). The proposal follows the Latin analogue documented for Chardonian; review it, then accept it in frontmatter or correct the persistent entry.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: elf
ancestry: null
campaignInfo:
  - {campaign: dufr, type: heard about him, date: 1749-01-08, wParty: "<person:U> <met> on <target>"}
born: null
died: 1
ka: null
gender: male
name: Elandrial
pronunciation: eh-LAN-dree-ahl
affiliations: [Fides Lucaris]
whereabouts:
  - {type: away}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: modern
---
# Elandrial
*(eh-LAN-dree-ahl)*
>[!info]+ Biographical Info  
> An [[Elves|elf]] (he/him), ([[Elven Cycle of Generations|ka]] unknown)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% The [[Dunmar Fellowship]] heard about him on January 8th, 1749 %%^End%%

An elf who was active during the [[History of the Drankorian Empire|Drankorian Era]]. Participated in attempts to decipher the [[Enchiridion of the Occulta Ludum]].

%%^Metadata:names:v1%%
- {name: "Elandrial", language: "unknown", pronunciation: "eh-LAN-dree-ahl", status: "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective account of a deceased elf's Drankorian-era work; the dates of his life and research are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected “A elf” to “An elf”.
- Added `knownTo: [dufr]` from the existing encounter metadata and normalized campaign codes to `dufr`.
- Recorded the accepted pronunciation in a name block and added the article’s modern retrospective viewpoint.

### Validated judgments
- [[Session 86 (DuFr)]] corroborates Elandrial’s work on deciphering the handbook; the short account is proportionate to the established role.

### Open findings

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: important`. The attestation may describe remembered information or another off-vault source, so retain it unless a human determines otherwise.
%%^End%%

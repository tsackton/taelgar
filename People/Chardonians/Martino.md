---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, date: 1749-05-06, type: met}
gender: male
born: 1681
name: Martino
whereabouts:
  - {type: home, end: 1749-05-07, location: Artevus}
  - {type: away, start: 1749-05-07, end: 1749-05-11, location: "Summer's Breeze"}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1749
---
# Martino
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on May 6th, 1749 in [[Artevus]], [[Portalia]], the [[Chardonian Empire]] %%^End%%

![[martino-portrait.jpg|right|400]]Martino is a retired sailor, fisherman, and navigator. He once sailed widely along the coasts of [[Apporia]], seeking the best fishing grounds, until he was hurt in a storm and lost most of the use of his right hand. 

He is extremely knowledgeable about the waters and coasts of [[Apporia]], but now spends his days hanging around [[Artevus]], gazing out to sea. 

%%SECRET[v2:b5d785bf48c765a697e976bb7d0dff0b]%%

%%^Metadata:names:v1%%
- {name: Martino, language: Chardonian, pronunciation: mar-TEE-noh, notes: "Proposed from the Italian and Latin analogue for Chardonian, with articulated vowels and penultimate stress; exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 portrait of Martino after his injury and retirement, with earlier sailing experience described only broadly.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting and added the explicit name field.
- Added `knownTo: [dufr]`.
- Added persistent Chardonian name metadata with the proposed pronunciation `mar-TEE-noh`.
- Added `POV: 1749` and a persistent temporal-coverage note.

### Validated judgments
- Confirmed local-only evidence supports the positive `dm_notes` attestation.
- The `SECRET` block was reviewed without exposing its contents; its unresolved accuracy caveat prevents a safe recovery proposal.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry remains `status: proposed` because no accepted pronunciation is recorded. Review the Italian- and Latin-analogue proposal `mar-TEE-noh`; if accepted, mark the entry `documented` and copy the pronunciation to frontmatter, or revise it and record the chosen basis.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Adventure Arc Outline]]
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Peninsula NPC Notes]]
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Session 98 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Session 99 - DM Notes]]
%%^End%%

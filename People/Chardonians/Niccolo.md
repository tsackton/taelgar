---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Chardonian
gender: male
campaignInfo:
  - {campaign: grli, type: met, date: 1748-09-18}
name: Niccolo
whereabouts:
  - {type: home, location: Castrella}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1748
---
# Niccolo
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Met by the [[Silver Tempests]] on September 18th, 1748 in [[Castrella]], [[Cedrano]], the [[Chardonian Empire]] %%^End%%

Niccolo is a librarian in [[Castrella]].

%%^Metadata:names:v1%%
- {name: Niccolo, language: Chardonian, pronunciation: neek-koh-LOH, notes: "Proposed from the ordinary Italian name under the Chardonian analogue, with a hard doubled c before o and final stress as in Italian Niccolò; the note's ASCII spelling does not mark the stress accent, and exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 snapshot of Niccolo as a librarian in Castrella; earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added `knownTo: [grli]` and canonicalized the Great Library code in `campaignInfo` and the campaign block.
- Added persistent Chardonian name metadata with the proposed pronunciation `neek-koh-LOH`.
- Added `POV: 1748` and a persistent temporal-coverage note.

### Validated judgments
- The prepared local-only name match refers to a different person and offers no recoverable material for this note.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry remains `status: proposed` because no accepted pronunciation is recorded. Review the Italian-analogue proposal `neek-koh-LOH`, including the unmarked final stress in the ASCII spelling; if accepted, mark the entry `documented` and copy the pronunciation to frontmatter, or revise it and record the chosen basis.
%%^End%%

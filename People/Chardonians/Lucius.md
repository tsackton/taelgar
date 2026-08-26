---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, type: reached via sending stone, date: 1749-01-08}
born: 1743
gender: male
name: Lucius
whereabouts:
  - {type: home, location: Luminatia}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1749
---
# Lucius
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Reached via sending stone by the [[Dunmar Fellowship]] on January 8th, 1749 in [[Luminatia]], the [[Chardonian Empire]] %%^End%%

![[lucius-portrait.jpeg|right|420]]Lucius is a boy of about 5 who lives with his mother, [[Livia]], in the village of [[Luminatia]], near [[Lake Valandros]] in the [[Chardonian Empire]]. He found a stone, in which he believes his imaginary friend Benji lives, in his [[Claudio|father's]] study, after his father abandoned the family.

- (DR:: 1749-01-08) Lucius' imaginary friend Benji spoke to him from the stone he carries, and asked him about his life. 

%%^Metadata:names:v1%%
- {name: Lucius, language: Chardonian, pronunciation: LOO-kee-oos, notes: "Proposed from Chardon's more Latinate Chardonian analogue, using the classical Latin hard c, three articulated syllables, and first-syllable stress; an Italian-like reading could soften the c, and exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 portrait of Lucius as a young child living with his mother after his father left; earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added `knownTo: [dufr]`.
- Added persistent Chardonian name metadata with the proposed pronunciation `LOO-kee-oos`.
- Added `POV: 1749` and a persistent temporal-coverage note.
- Repaired the opening sentence fragment without changing its meaning.

### Validated judgments
- The prepared local-only matches were false positives for this subject and do not support the positive `dm_notes` attestation.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry remains `status: proposed` because no accepted pronunciation is recorded. Review the Latinate Chardonian proposal `LOO-kee-oos`, including the documented Italian-like alternative with a softened c; if accepted, mark the entry `documented` and copy the pronunciation to frontmatter, or revise it and record the chosen basis.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No confirmed local-only `_DM_` notes were found for this Lucius; verify `dm_notes: color`. The attestation may still represent remembered or off-vault information and must not be removed automatically.
%%^End%%

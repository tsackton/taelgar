---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, type: mentioned to, date: 1749-01-08, wParty: "<met:U> <person> on <target>"}
gender: female
name: Livia
whereabouts: Luminatia
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1749
---
# Livia
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (she/her)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Mentioned to the [[Dunmar Fellowship]] on January 8th, 1749 %%^End%%

%%another need to track rumors campaign info page%%

[[Lucius]]'s mother.

%%^Metadata:names:v1%%
- {name: Livia, language: Chardonian, pronunciation: LEE-vyah, notes: "Proposed from the Italian analogue for Chardonian, with first-syllable stress and a compressed final ia; a more classically Latinate reading could be LEE-wee-ah, and exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 snapshot identifying Livia as Lucius's mother; earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added `knownTo: [dufr]` and canonicalized the Dunmar Frontier campaign code in `campaignInfo` and the campaign block.
- Added persistent Chardonian name metadata with the proposed pronunciation `LEE-vyah`.
- Added `POV: 1749` and a persistent temporal-coverage note.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry remains `status: proposed` because no accepted pronunciation is recorded. Review the Italian-analogue proposal `LEE-vyah` and the more classically Latinate alternative `LEE-wee-ah`; if one is accepted, mark the entry `documented` and copy the pronunciation to frontmatter, or revise it and record the chosen basis.
%%^End%%

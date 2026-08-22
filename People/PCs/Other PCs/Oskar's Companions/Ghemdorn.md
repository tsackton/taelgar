---
subspecies: satyr
headerVersion: 2023.11.25
lintedAt: "2026-08-21T18:44:38-04:00"
lintVersion: "3.4"
tags: [person, status/check/lint]
species: fey
gender: male
campaignInfo:
  - {campaign: dufr, person: Riswynn, type: met, date: 1748-05-31}
player: Sasha Rosan
ddbLink: https://www.dndbeyond.com/characters/53344874
name: Ghemdorn
affiliations:
  - {org: "Oskar's Companions", title: One}
whereabouts:
  - {type: away, start: 1748-05-25, end: 1748-06-02, location: Yuvanti Mountains}
knownTo: [dufr]
dm_owner: player
dm_notes: none
POV: 1748
---
# Ghemdorn
>[!info]+ Biographical Info  
> A [[Fey|fey]] (satyr) (he/him)  
> [Character Sheet](https://www.dndbeyond.com/characters/53344874)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by [[Riswynn]] on May 31st, 1748 in the [[Yuvanti Mountains]] %%^End%%

Ghemdorn is a satyr paladin, known to travel with [[Eva]]. 

%%^Metadata:names:v1%%
- {name: Ghemdorn, role: primary, language: unknown, pronunciation: GEM-dorn, status: proposed, notes: Cautious spelling-based reading; no stronger language or pronunciation source was found.}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a narrow DR 1748 campaign portrait around Ghemdorn's encounter with Riswynn and Oskar in the Yuvanti Mountains; earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized frontmatter and campaign syntax, added `knownTo: [dufr]`, and corrected `31th` to `31st`.
- Added persistent name and temporal POV metadata.

### Validated judgments
- Editorial sufficiency: **Sufficient, worth expanding**. The optional campaign-role addition is recorded in the private handoff rather than as a finding.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry records `GEM-dorn` as a cautious spelling-based pronunciation proposal because no stronger source or language rule was found. Confirm it by copying `pronunciation: GEM-dorn` to frontmatter and changing the entry to `status: documented`, or replace it with the accepted pronunciation.
- [ ] **Suggestion — frontmatter.deprecated_field:** `subspecies: satyr` is obsolete. [[Satyrs]] exists and the article identifies Ghemdorn as a satyr; after confirming the classification, replace `species: fey` with `species: satyr` and remove `subspecies: satyr`.

%%^End%%

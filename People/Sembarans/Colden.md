---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:37:56-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: alien fungal entity
died: 1740-10-07
gender: male
name: Colden
whereabouts: Dandelion House
knownTo: [feywild]
dm_owner: none
dm_notes: none
POV: 1740
---
# Colden
>[!info]+ Biographical Info  
> A [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Colden is an alien fungal entity posing as [[Alden|Alden's]] cousin, and bears a resemblance: short and somewhat pudgy, dressed in rough homespun. He helps around [[Dandelion House]], working for [[Lord Hulda]]. He was killed by [[Lord Hulda]] when the [[Prisoner in the 27th Room]] was set free and [[Lost in the Feywild - Episode 07|disappeared to a strange alien realm]].

%%^Metadata:names:v1%%
- {"name": "Colden", "language": "unknown", "status": "proposed", "pronunciation": "KOHL-den", "notes": "Cautious spelling-based proposal because Colden's name-language is not established: initial stress, long o, and unstressed -den. The resemblance to Alden's name does not establish a pronunciation rule."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740 Dandelion House portrait: the appearance and service describe Colden before his death, with his fate stated retrospectively.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added supported name and temporal metadata.
- Added `knownTo: [feywild]` from the reviewed campaign evidence.
- Corrected an objective grammar error.

### Validated judgments
- The existing record identifies Colden as an alien in human guise; the added name and temporal metadata do not change audience visibility.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry proposes `KOHL-den`. Cautious spelling-based proposal because Colden's name-language is not established: initial stress, long o, and unstressed -den. The resemblance to Alden's name does not establish a pronunciation rule. If accepted, add `pronunciation: KOHL-den` to frontmatter and set the entry to `status: documented`; otherwise revise the proposal with its basis.

- [ ] **Warning — identity.header_species_conflict:** The static biographical line calls Colden a `[[Humans|human]]`, while `species: alien fungal entity` and the article identify an alien posing as a human. Regenerate the header from the existing species metadata, or replace only that line with `> An alien fungal entity (he/him)`; retain the human appearance in the article.
%%^End%%

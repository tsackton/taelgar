---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
gender: male
campaignInfo:
  - {campaign: grli, type: met, date: 1748-08-23}
name: Elian of Suwi
aliases: [Elian]
whereabouts:
  - {type: home, location: Suwi}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1748
---
# Priest Elian of Suwi
>[!info]+ Biographical Info  
> A [[Humans|human]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Met by the [[Silver Tempests]] on August 23rd, 1748 in [[Suwi]] %%^End%%

Elian of Suwi is a priest serving the coastal village of [[Suwi]]. 

%% nothing decided about Elian's ancestry, age, background, or activities beyond the one encounter with the Silver Tempests. %%

%%^Metadata:names:v1%%
- {"name": "Elian of Suwi", "language": "unknown", "pronunciation": "EH-lee-an of SOO-wee", "status": "proposed", "notes": "Suwi supplies the accepted SOO-wee; EH-lee-an is a cautious spelling-based proposal because Elian has no established naming language or pronunciation."}
- {"name": "Elian", "role": "alias", "language": "unknown", "pronunciation": "EH-lee-an", "status": "proposed", "notes": "Cautious spelling-based proposal; no established naming language or explicit pronunciation was found."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 snapshot of Elian serving as Suwi's village priest; the beginning and end of that service are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [grli]` from the existing campaign interaction and normalized its campaign code in metadata and the existing block.
- Corrected the ordinal `23th` to `23rd`.
- Added proposed full and short name pronunciations, a DR 1748 viewpoint, and persistent temporal guidance; normalized frontmatter.

### Validated judgments
- The brief priest identification is proportionate to the minor role established in [[Great Library Session Notes - Arc 4]]; the undecided background comment remains unchanged.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise `EH-lee-an of SOO-wee` (and the short form `EH-lee-an`). [[Suwi]] documents `SOO-wee`; Elian's ancestry and naming language remain undecided in this note, so `EH-lee-an` is only a cautious spelling-based reading with initial stress, e as eh, and i as ee. The proposals remain in `Metadata:names:v1`; on acceptance, mark the entries documented and copy the accepted full form to frontmatter `pronunciation`.
%%^End%%

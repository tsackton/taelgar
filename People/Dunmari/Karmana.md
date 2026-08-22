---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T18:44:38-04:00"
lintVersion: "3.4"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Dunmari
born: null
gender: male
campaignInfo:
  - {campaign: dufr, date: 1748-05-11, type: met}
name: Karmana
pronunciation: kar-MAH-nah
whereabouts: Monastery of Bhishma
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Karmana
*(kar-MAH-nah)*
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on May 11th, 1748 in the [[Monastery of Bhishma]], the [[Garamjala Desert]] %%^End%%

%%need to figure out how to properly deal with undead%%
%%need to add whereabouts and campaign info%%

The last master of the [[Order of the Awakened Soul]] at the [[Monastery of Bhishma]], now a ghost.

%%SECRET[v2:002b144fe04df3576c97d4fb851dfa88]%%

%%^Metadata:names:v1%%
- {name: Karmana, role: primary, language: Dunmari, pronunciation: kar-MAH-nah, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 encounter portrait of Karmana as the ghost guarding the Monastery of Bhishma; his earlier life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the established Dunmar Frontier interaction, current monastery whereabouts, `knownTo`, `POV`, `povNotes`, and a persistent pronunciation proposal; normalized frontmatter formatting.

### Validated judgments
- `status/cleanup/metadata` remains supported because the shared comment's undead-classification question is unresolved; no status was changed.
- Matching local-only sources support `dm_notes: important`; their contents are not reproduced here.

### Open findings
- [ ] **Warning — metadata.names_unresolved_status:** Persistent name review remains open for `Karmana — kar-MAH-nah` (proposed). The Dunmari Hindi and Indo-Iranian analogue supports this cautious reading, but exact in-world phonology is not established. Accept it by adding `pronunciation: kar-MAH-nah` to frontmatter and changing the name entry to `status: documented`, or correct the proposal.
%%^End%%

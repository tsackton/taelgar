---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T23:02:51-04:00"
lintVersion: "3.5"
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
- None.

### Validated judgments
- The local-only `SECRET` block was reviewed; useful material is routed only through the private lint handoff.
- `status/cleanup/metadata` remains supported by the unresolved undead-classification question.

### Open findings

- [ ] **Suggestion — editorial.shared_material_redundant:** The shared comment `%%need to add whereabouts and campaign info%%` is obsolete because both `whereabouts` and `campaignInfo` are now present in frontmatter. Candidate: remove that comment.
%%^End%%

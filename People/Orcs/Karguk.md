---
headerVersion: 2023.11.25
lintedAt: "2026-10-05T14:32:22-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: orc
gender: male
title: Chief
died: "0001"
name: Karguk
pronunciation: kar-GOOK
whereabouts: Uzgukhar
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: modern
---
# Karguk
*(kar-GOOK)*
>[!info]+ Biographical Info  
> An [[Orcs|orc]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Karguk was an [[Orcs|orc]] chief of [[Uzgukhar]] and the father of [[Lubash]].

%% figure out sensible death date and replace undated death %%

%% Sources:
- [[Murook]]
- [[Murook's Story]]
%%

%%^Metadata:names:v1%%
- {name: Karguk, language: Free Orcish, pronunciation: kar-GOOK, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: modern retrospective identification of Karguk; the dates of his chiefship and death are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Quoted the existing `0001` undated-death sentinel to preserve its spelling in canonical YAML; no death year was assigned.

### Validated judgments
- The `status/cleanup/metadata` tag remains supported by the unresolved death date and its existing reminder.
- The existing `POV: modern` and temporal note fit a retrospective identification whose chiefship and death dates remain unestablished.

### Open findings

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The note records `dm_notes: color`, but the local source search found no confirmed Karguk evidence. Keep `dm_notes: color` if useful information remains in memory or another private source; otherwise, after human confirmation, use `dm_notes: none`.
%%^End%%

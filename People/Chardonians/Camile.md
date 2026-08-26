---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T09:29:24-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/gl, status/check/lint]
species: human
ancestry: Chardonian
born: 1736
gender: female
campaignInfo:
  - {campaign: grli, type: met, date: 1748-09-18}
name: Camile
whereabouts:
  - {type: home, start: 1748-09-18, location: Castrella}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1748
---
# Camile
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (they/them)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Met by the [[Silver Tempests]] on September 18th, 1748 in [[Castrella]], [[Cedrano]], the [[Chardonian Empire]] %%^End%%

Camile is an orphan living in [[Castrella]]. After fleeing trouble along the upper [[Kedron]] with [[Arturo]], Camile found work and refuge at [[The Whale's Spout]], a tavern run by [[Old Leo]] and known for taking in orphans.

%% Game Update: 
After [[Great Library Session Notes - Arc 5|GL Session 63]], it is likely that she has been reunited with his parents in DR 1752. But undecided, possible her parents didn't survive. 
%%

%%^Metadata:names:v1%%
- {name: Camile, language: Chardonian, pronunciation: kah-MEE-leh, notes: "Proposed from the Italian analogue for Chardonian: hard c before a, i read as ee, and a pronounced final e; exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Camile as an orphan living in Castrella after fleeing trouble along the upper Kedron; her later fate remains unresolved.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added `knownTo: [grli]` and canonicalized the Great Library campaign code in `campaignInfo` and the campaign block.
- Added persistent Chardonian name metadata with the proposed pronunciation `kah-MEE-leh`.
- Added `POV: 1748` and a persistent temporal-coverage note.

### Validated judgments
- `status/gameupdate/gl` is not assessable: the shared comment preserves an unresolved possible DR 1752 fate rather than an established outcome, so the tag remains unchanged.

### Open findings

- [ ] **Warning — content.internal_conflict:** The header identifies Camile with `(they/them)`, while frontmatter has `gender: female` without a `pronouns` override and the article/comment use `she`, `her`, and once `his`. Confirm the intended pronouns. If they are she/her, change the header to `(she/her)` and `his parents` to `her parents`; if they are they/them, add `pronouns: they/them` and revise the gendered prose consistently.
- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry remains `status: proposed` because no accepted pronunciation is recorded. Review the Chardonian Italian-analogue proposal `kah-MEE-leh`; if accepted, mark the entry `documented` and copy the pronunciation to frontmatter, or revise it and record the chosen basis.
%%^End%%

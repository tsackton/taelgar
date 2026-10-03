---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:37:56-04:00"
lintVersion: "3.5"
tags: [person, status/check/ai, status/check/lint]
species: human
ancestry: Sembaran
gender: female
born: 1697
name: Betsy Thorne
affiliations:
  - {org: "Lord's Guard of Cleenseau", title: Guardswoman}
  - {org: Thornes of Cleenseau, type: primary}
whereabouts: Cleenseau
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1720
---
# Betsy Thorne
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her), of the [[Thornes of Cleenseau]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The daughter of [[Jon Thorne]], cousin of [[Beatrix Thorne]] and a member of the Cleenseau town watch.

In late April 1720, Betsy left [[Rosalind Essford|Rosalind's]] guard for [[Asineau]], where she joined the guard. She wanted a fresh start away from comparison with her cousin and felt that Ames, her former captain, was a poor teacher.

%% Sources:
- [[Asineau Hirelings (Email)]]
- [[Cleenseau - Session 29]]
%%

%%^Metadata:names:v1%%
- {name: "Betsy Thorne", language: "Sembaran"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: A DR 1720 portrait combining her earlier Cleenseau guard service with her late-April move to Asineau; the undated opening and relationship metadata still need reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported name, campaign-knowledge, and temporal metadata; normalized frontmatter formatting.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — temporal.inconsistent_frame:** The opening calls Betsy a current member of Cleenseau’s town watch and the header still gives `whereabouts: Cleenseau` with an open-ended Lord’s Guard affiliation, while the dated paragraph, [[Cleenseau - Session 29]], and [[Asineau Hirelings (Email)]] establish her late-April 1720 move and new guard service. For a post-move article, use `The daughter of [[Jon Thorne]], cousin of [[Beatrix Thorne]], and a former member of the Cleenseau town watch.` Reconcile whereabouts and guard affiliations to Asineau while retaining the Thorne family tie; supply or deliberately bound the transition dates instead of inventing an exact April day. Alternatively preserve an explicitly earlier snapshot and isolate the later paragraph in an approved Date block.
%%^End%%

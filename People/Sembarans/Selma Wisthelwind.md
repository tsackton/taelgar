---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T16:23:04-04:00"
lintVersion: "2.3"
tags: [person, status/check/mike]
species: human
ancestry: Zimka
born: 1644
gender: female
name: Selma Wisthelwind
pronunciation: SELL-mah VIS-tel-vind
affiliations:
  - {org: "The Fox's Flagon", type: leader, title: Proprietor, start: 1712}
whereabouts:
  - {type: home, location: Ardlas}
  - {type: home, start: 1709, end: 1711, location: Cleenseau}
  - {type: home, start: 1712, location: "The Fox's Flagon"}
knownTo: [clee]
dm_owner: mike
dm_notes: none
POV: 1720
---
# Selma Wisthelwind
*(SELL-mah VIS-tel-vind)*
>[!info]+ Biographical Info  
> A [[Zimka]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% validate pronunciation, which is based on ChatGPT Baltic-ish interpretation %%

![[selma-wisthelwind.png|right|320]]Selma bought [[The Fox's Flagon]] for cash in DR 1712 and appears to enjoy running the inn as a form of retirement. From what exactly is not clear. She has always been a bit of an outsider in town and is one of the few people who keeps the old [[Kestavo]] religion of [[Zimkova]].

%%^Metadata:article:v1%%
mode: character reference
povNotes: "Accuracy range: approximately the DR 1720 Cleenseau campaign era. The article assumes that Selma still owns the Fox's Flagon after buying it in DR 1712; it establishes no later endpoint for her proprietorship."
%%^End%%

%%^Metadata:names:v1%%
- {name: Selma Wisthelwind, role: primary, language: Zimkovan, pronunciation: SELL-mah VIS-tel-vind, status: proposed}
%%^End%%

%%^Lint%%
## Taelgar note lint

### Open findings

- [ ] **warning — `name.pronunciation_missing`:** `SELL-ma WISS-thel-wind` is a cautious spelling-based proposal. Zimkovan is inferred from Selma’s Zimka origin, while [[Languages]] gives analogues but no exact rules. If accepted, copy:
  ```yaml
  pronunciation: SELL-ma WISS-thel-wind
  ```
  and update the name entry’s status.

### Applied changes

- Added `POV: 1720`, current article metadata, and a proposed v1 name entry. Removed the stale explanation about “8 years ago,” because the prose now uses the explicit DR 1712 date.
%%^End%%

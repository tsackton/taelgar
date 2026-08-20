---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T21:07:45-04:00"
lintVersion: "2.5"
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

%% validate pronunciation, which is based on ChatGPT Baltic-ish interpretation. delete the lint block once you confirm  %%

![[selma-wisthelwind.png|right|320]]Selma bought [[The Fox's Flagon]] for cash in DR 1712 and appears to enjoy running the inn as a form of retirement. From what exactly is not clear. She has always been a bit of an outsider in town and is one of the few people who keeps the old [[Kestavo]] religion of [[Zimkova]].

%%^Metadata:article:v1%%
mode: character reference
povNotes: "Accuracy range: approximately the DR 1720 Cleenseau campaign era. The article assumes that Selma still owns the Fox's Flagon after buying it in DR 1712; it establishes no later endpoint for her proprietorship."
%%^End%%

%%^Metadata:names:v1%%
- {name: Selma Wisthelwind, role: primary, language: Zimkovan, pronunciation: SELL-mah VIS-tel-vind, status: proposed, notes: Baltic-informed reading; w is adapted as v and the nonnative th cluster as t. Latvian-style initial stress and Lithuanian stress variation make the compound stress the main uncertainty.}
%%^End%%

%%^Lint%%
## Taelgar note lint

### Open findings

- [ ] **warning — name.pronunciation_unconfirmed:** The current `SELL-mah VIS-tel-vind` value is a genuinely Baltic-informed proposal, not an English-default reading. [[Languages]] explicitly maps Zimkovan to Baltic languages: the proposal adapts nonnative `w` to `v`, adapts the nonnative `th` cluster to `t`, and uses short Baltic-style vowels. Latvian favors initial stress, while Lithuanian stress is variable, so the surname's stress remains the main uncertainty. If Mike accepts it, copy-ready name entry: `- {name: Selma Wisthelwind, role: primary, language: Zimkovan, pronunciation: SELL-mah VIS-tel-vind, status: documented}`; then the validation comment and `status/check/mike` can be cleared by a human.

### Applied changes

- Expanded the persistent name entry to record the concrete Baltic sound choices behind the proposal.

### Validated

- `POV: 1720` correctly anchors the DR 1712 inn purchase and current proprietorship to the Cleenseau campaign era.
%%^End%%

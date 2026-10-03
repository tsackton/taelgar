---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
ancestry: Sembaran
campaignInfo:
  - {campaign: clee, type: met, date: 1719-11-01}
born: 1693
gender: male
name: Mermin Stonebridge
affiliations:
  - {org: Stonebridges, type: primary}
whereabouts:
  - {type: home, location: Cleenseau}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1719
---
# Mermin Stonebridge
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Halflings|halfling]] (he/him), of the [[Stonebridges]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:clee%% Met by the [[Heroes of Cleenseau]] on November 1st, 1719 in [[Cleenseau]], the [[Manor of Cleenseau]], the [[Barony of Aveil]] %%^End%%

A young halfling trader based out of Cleanseau, although he travels between [[Rinburg]] and [[Cleenseau]] somewhat regularly.  Like most halflings, but unlike most Stonebridges, he is anxious to travel and is just looking for the opportunity which, as he says, "the ancestors want for him".

He was working with [[Gentza]] to potentially sell her remedy before she died and was shocked by her murder and the subsequent misuse of her medical investigations.

%%^Metadata:names:v1%%
- {name: "Mermin Stonebridge", language: "unknown", pronunciation: "MER-min STOHN-brij", status: "proposed", notes: "Proposed English-branch adaptation of the Sembaran analogue in Languages; a French reading would differ, and the name’s actual language is unestablished."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1719 portrait of Mermin as a young trader, after Gentza’s murder; earlier and later life stages are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent name and temporal-viewpoint metadata; unestablished name languages remain `unknown`.
- Added `knownTo: [clee]` from the existing campaign interaction.

### Validated judgments
- The trading role, desire to travel, and relationship with [[Gentza]] provide sufficient reference substance. The session source’s broad chronology does not establish a replacement for the existing exact meeting date.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise `MER-min STOHN-brij` in `Metadata:names:v1`. The preferred reading uses the English branch of the [[Languages]] Sembaran analogue: initial stress, short i in the second syllable, and the English compound surname with final /dʒ/. Southern French influence could instead favor a final-stressed, nasalized `mehr-MAN`. The provisional Halfling Igbo analogue does not establish this particular name’s language. The proposal is analogue-informed, not documented in-world phonology; on acceptance, mark it `documented` and copy the accepted primary pronunciation to frontmatter.
- [ ] **Suggestion — correctness.name_spelling:** The visible prose says “based out of Cleanseau,” while the frontmatter, the linked town in the same sentence, and [[Gentza]] consistently identify [[Cleenseau]]. Candidate: “based out of Cleenseau.” The name spelling has been left for human confirmation.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T18:44:38-04:00"
lintVersion: "3.4"
tags: [person, status/check/lint]
species: dwarf
campaignInfo:
  - {campaign: dufr, date: 1749-01-28, type: met}
gender: female
born: 1701
image: kethra-small.png
name: Kethra Silverspark
pronunciation: KETH-rah SIL-ver-spark
affiliations:
  - {org: Silversparks, type: primary}
whereabouts:
  - {type: home, location: Tharn Todor}
  - {type: away, start: 1749-01-11, end: 1749-01-29, location: "Pava and Avaras' House"}
  - {type: away, start: 1749-01-30, end: 1749-06-18, location: Vindristjarna}
  - {type: away, start: 1749-06-18, end: 9999, location: Uzgukhar}
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: 1749
---
# Kethra Silverspark
*(KETH-rah SIL-ver-spark)*
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (she/her), of the [[Silversparks|Silverspark Clan]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on January 28th, 1749 in [[Pava and Avaras' House]], the [[Garamjala Desert]] %%^End%%

![[kethra-final-option1.png|right|400]]Kethra Silverspark, great-grandaughter of [[Nora Silverspark]], is a proud dwarven smith and novice adventurer from [[Tharn Todor]]. 

Inspired by the tales of [[Riswynn]]'s heroic adventures in returning the [[Chalice of the Runepriest]] and putting to rest the ghosts of [[Nora Silverspark]] and [[Hagrim]], among others, she decided to leave home and put herself in Riswynn's service.

%%^Metadata:names:v1%%
- {name: Kethra Silverspark, role: primary, language: Dwarven, pronunciation: KETH-rah SIL-ver-spark, status: documented, notes: Dwarven family name translated into Common.}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 origin portrait of Kethra before and during her early service to Riswynn; her later campaign activities are not yet represented in the visible article.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Editorial assessment
**Underdeveloped**. The visible account stops at Kethra's decision to enter Riswynn's service and does not yet represent the central established later course of that service: joining Vindristjarna after seeking Riswynn as a mentor, accompanying her during the doppelganger crisis, and departing with her for Uzgukhar.

### Applied changes
- Added the established Dunmar Frontier interaction, `knownTo`, DR 1749 `POV` and `povNotes`, a persistent pronunciation proposal, and the June 1749 move from Vindristjarna to Uzgukhar; normalized frontmatter formatting.

### Validated judgments
- Matching local-only sources support `dm_notes: color`; their contents are not reproduced here.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** [[Session 89 (DuFr)]], [[Session 103 (DuFr)]], and [[Session 124 (DuFr)]] establish the central later role absent from the visible article: Kethra joined Vindristjarna after seeking Riswynn as a mentor, accompanied her during the doppelganger crisis, and later went with her to Uzgukhar. Copy-ready candidate: “By DR 1749, Kethra had joined the crew of Vindristjarna after seeking out Riswynn as a mentor. She accompanied Riswynn back to Tharn Todor to confront a doppelganger recruiting dwarves to their deaths and later went with her to Uzgukhar to support the campaign to free orcs from Thark.”
- [ ] **Warning — pronunciation.review_pending:** Persistent pronunciation review remains open for `Kethra Silverspark — KETH-rah SIL-ver-spark` (proposed). The Tolkien-style Dwarvish analogue and ordinary Common compound support this cautious reading, but the full form's exact in-world language and phonology are not established. Accept it by adding `pronunciation: KETH-rah SIL-ver-spark` to frontmatter and changing the entry to `status: documented`, or correct the proposal.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: fey
subspecies: korred
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-11-01, type: met}
born: null
gender: male
name: Illaran
affiliations:
  - {org: Crystal Peak, title: Guardian, type: ruler}
whereabouts: Crystal Peak
knownTo: [dufr]
dm_owner: none
dm_notes: important
POV: 1740s
---
# Illaran
>[!info]+ Biographical Info  
> A [[Fey|fey]] (korred) (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:DuFr%% Met by the [[Dunmar Fellowship]] on November 1st, 1748 in the [[Crystal Peak]], the [[Feywild]], [[Multiverse]] %%^End%%

Illaran, the guardian of Crystal Peak in the [[Feywild]], is a whimsical fey who wields power over the very stones of his domain.
## Overview

Illaran guards and protects Crystal Peak, a magical fey mountain made of solid crystal between the [[Feywild]] domains of [[Fortune's Rest]] and [[Shimmersong]]. He is known for his curious and innovative nature. He displays a strong connection to the stones of his home, manipulating them with ease.
## Description

Physically, Illaran is dwarf-like: short and stout. His most distinguishable feature is his untamed, vibrant hair that fans out in a frizzy, multi-colored spectacle.
## Events

- During DR 1748, Illaran inadvertently caused a wild magic storm in the [[Feywild]]. [[Seeker]], assisted by two guardians from [[Shimmersong]] and a wandering fey samurai, managed to quell the tempest. Recognizing their efforts, Illaran bestowed upon [[Seeker]] shards of crystallized magic as a token of appreciation.

%%SECRET[v2:1bf4d8bd3e9f61263799270c669a8d1a]%%

%%^Metadata:names:v1%%
- {"name": "Illaran", "language": "unknown", "pronunciation": "ee-LAH-rahn", "notes": "Proposed using the Classical Greek tendency noted for Fey names in Languages: i as ee, a as ah, ll as l, and a provisional penultimate stress. Sylvan’s analogue is explicitly undetermined, so this is a naming-pattern proposal rather than an adopted phonological rule; the name’s language is not established.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740s portrait of the guardian of Crystal Peak, including the storm incident in DR 1748; earlier and later states of his guardianship are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and the campaignInfo code; added knownTo: [dufr].
- Added a proposed pronunciation and a DR 1740s temporal interpretation.

### Validated judgments
- The visible note identifies the guardian, his appearance, and a defining incident. Positive dm_notes evidence is confirmed; the SECRET block was reviewed without sharing its contents.

### Open findings

- [ ] **Warning — correctness.source_conflict:** The Events sentence says Illaran “caused a wild magic storm”, but [[Session 63 (DuFr)]] describes a geode crash leaking uncontrolled magic before he summoned a gem-eating creature, and states that the geode caused the storm. Preserve his contribution without making him its original cause. Copy-ready replacement for the opening sentence: “During DR 1748, Illaran’s attempt to deal with a crashed magical geode at [[Crystal Peak]] worsened a wild magic disturbance: a creature he summoned swallowed the geode’s shards, and spells cast within the mountain came alive.” Keep the later account of the storm’s resolution and his gift.

- [ ] **Warning — temporal.campaign_date_conflict:** campaignInfo and the generated meeting line date the encounter to 1748-11-01, while [[Session 63 (DuFr)]] places the Crystal Peak encounter in the 1748-10-03 to 1748-10-12 session range. Confirm the intended chronology before changing either representation. If the session chronology is authoritative, date: 1748-10 is a copy-ready month-level value; do not invent an exact day.

- [ ] **Warning — metadata.affiliation_type:** The Crystal Peak affiliation uses type: ruler, outside the member/primary/leader vocabulary in [[Metadata Specification]]. The visible note calls Illaran its guardian, and [[Session 63 (DuFr)]] calls him master of the mountain. If this denotes authority over Crystal Peak, use {org: Crystal Peak, title: Guardian, type: leader}; otherwise retain the Guardian title with type: member. Confirm the intended relationship before changing the value.

- [ ] **Warning — metadata.names_unresolved_status:** Review ee-LAH-rahn in the name block. [[Languages]] notes a Classical Greek tendency among Fey names while explicitly leaving the Sylvan analogue undetermined. The proposal uses i as ee, a as ah, ll as l, and provisional penultimate stress; neither the source language nor exact in-world sound rules are established. Accept by copying pronunciation: ee-LAH-rahn to frontmatter and marking the entry documented, or supply the intended reading.

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated meeting line uses Campaign:DuFr. Replace only DuFr with the canonical dufr from [[Campaign Registry]], preserving the block’s other content until the separate date question is resolved.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Seeker Solo Arc/Session 1 - Seeker]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Seeker Solo Arc/Session 2 - Seeker]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Raw Notes - Seeker Solo]]
%%^End%%

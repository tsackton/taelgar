---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Skaer
campaignInfo:
  - {campaign: dufr, person: Kenzo, date: 1748-12-30, type: courted, format: "<met:U> by <person> on <target>"}
  - {campaign: dufr, date: 1749-01-05, type: last seen}
born: 1724
gender: female
title: Laivan
name: Iskra
whereabouts:
  - {type: home, location: Pikkua}
  - {type: home, start: 1743, location: Tollen}
knownTo: [dufr]
dm_owner: tim
dm_notes: none
POV: 1748
---
# Laivan Iskra
>[!info]+ Biographical Info  
> A [[Skaer]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Courted by [[Kenzo]] on December 30th, 1748 %%^End%%  
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on January 5th, 1749 in the [[Tollen|Free City of Tollen]], the Western Green Sea Region %%^End%%

![[laivan-iskra.png|right|500]]A young woman and priestess of [[Kaikkea]] in [[Tollen]]. She speaks with the power of the ocean, and has a deep connection to [[Kaikkea]].

%%^Campaign:dufr%%
She told her story and history to Kenzo while they wandered [[Tollen]] together in the moments of quiet after the destruction of the [[Scepter of Command]] and before the [[Battle for Uzgukhar]]. 



![[Iskra's Story]]

%%^End%%

%%^Metadata:names:v1%%
- {name: Iskra, language: unknown, pronunciation: EES-krah, status: proposed, notes: 'Proposal informed by the Finnish option in the Skaegish analogues in [[Languages]]: initial stress, ee-like i, hard sk, and open final a. The name language and exact in-world phonology are not established.'}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-DR 1748 portrait of Iskra as a young priestess in Tollen, with earlier personal history and campaign interactions extending into early DR 1749; the dates of her residence and priestly appointment are not equated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added knownTo from the existing campaign interaction record and normalized frontmatter ordering and collection formatting.
- Normalized the existing campaign aliases to canonical registry codes in campaignInfo and the matching header block.
- Added persistent name and temporal-viewpoint metadata; existing names, accepted pronunciations, and human attestations were preserved.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The pronunciation `EES-krah` is recorded as `status: proposed` in Metadata:names:v1. The Skaegish guidance in [[Languages]] permits Finnish or Norwegian with Swedish influences. The proposal uses the Finnish option: initial stress, ee-like i, hard sk, and open final a. No adopted in-world phonology or exact name-language attribution settles the choice. Confirm or revise it; if accepted, copy `pronunciation: EES-krah` to frontmatter and change the entry to `status: documented`.
- [ ] **Warning — consistency.cross_note_conflict:** The campaign paragraph says Iskra told Kenzo her story “after the destruction of the [[Scepter of Command]],” but [[Session 81 (DuFr)]] dates collecting [[Iskra's Story]] to December 17, DR 1748 and the destruction to December 25. [[Session 83 (DuFr)]] separately records their later December 31 walk. Decide whether the paragraph refers to the first collection or a later retelling. For the documented collection, use: “She told [[Kenzo]] her story and history in [[Tollen]] on December 17, DR 1748, before the destruction of the [[Scepter of Command]].”

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
gender: female
campaignInfo:
  - {campaign: grli, type: met, date: 1747-12-05}
name: Diesa Shockstone
affiliations:
  - {org: Shockstones, type: primary}
whereabouts:
  - {type: home, location: Zarkandur}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Diesa Shockstone
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (she/her), of the [[Shockstones]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:GL%% Met by the [[Silver Tempests]] on December 5th, 1747 in [[Zarkandur]], [[Am'khazar]], [[Sentinel Range|Labkhan]] %%^End%%

Diesa is a prominent and wealthy dwarf, one of the elite of [[Zarkandur]]. She is also [[Brelith]]'s mother and [[Osrik]]'s wife. 

%%^Metadata:names:v1%%
- {name: Diesa Shockstone, language: unknown, pronunciation: DEE-eh-sah SHOK-stohn, notes: "Analogue-informed proposal using the Tolkien Dwarvish guidance in [[Languages]]: distinct i/e/a vowels, plain d and s consonants, and tentative first-syllable stress; the family-name reading follows [[Brelith]]. The source language and vowel grouping are not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of her wealth, family relationships, and home in Zarkandur, anchored by the December DR 1747 visit; earlier and later circumstances are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added persistent name metadata and a supported temporal viewpoint.
- Normalized campaignInfo to grli and added knownTo: [grli].

### Validated judgments
- The family relationships and Zarkandur identity agree with [[Brelith]], [[Osrik]], and [[Great Library Session Notes - Arc 3]]. Other people named Diesa and a generic name-list occurrence do not establish facts about this person.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `DEE-eh-sah SHOK-stohn`. This uses the Tolkien Dwarvish analogue in [[Languages]] as guidance: separate i/e/a vowel sounds, plain d and s consonants, and tentative first-syllable stress; `SHOK-stohn` follows the family name in [[Brelith]]. The analogue does not establish this name’s source language or vowel grouping. Confirm or replace the proposal, then set `status: documented` and copy the accepted complete pronunciation to frontmatter.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The existing generated encounter line uses `%%^Campaign:GL%%`; its canonical registry code is `grli`. Regenerate the line from campaignInfo or replace only the opening marker with `%%^Campaign:grli%%`, preserving the line and its boundaries. The generated header and visibility marker were retained for human review.
%%^End%%

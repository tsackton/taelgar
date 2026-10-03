---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
gender: male
campaignInfo:
  - {campaign: grli, type: met, date: 1747-12-05}
name: Osrik Shockstone
affiliations:
  - {org: Shockstones, type: primary}
whereabouts:
  - {type: home, location: Zarkandur}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Osrik Shockstone
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him), of the [[Shockstones|Shockstone Clan]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Met by the [[Silver Tempests]] on December 5th, 1747 in [[Zarkandur]], [[Am'khazar]], [[Sentinel Range|Labkhan]] %%^End%%

Osrik is a prominent and wealthy dwarf, one of the elite of [[Zarkandur]]. He is also [[Brelith]]'s father and [[Diesa]]'s husband.

%%^Metadata:names:v1%%
- {"name": "Osrik Shockstone", "language": "unknown", "pronunciation": "OS-rik SHOK-stohn", "status": "proposed", "notes": "The [[Languages]] guidance uses Tolkien Dwarvish for dwarven naming. Proposal uses short o and i vowels, an audible r and hard k, with tentative initial stress; the clan surname follows its transparent trade-tongue form. No name-specific pronunciation is recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of Osrik’s status and family in Zarkandur, anchored by the December 1747 visit; later life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Recorded supported campaign knowledge in `knownTo`, the article’s temporal viewpoint in `POV`, and its coverage limits in `povNotes`.
- Added a primary name entry with a proposed pronunciation; retained `language: unknown` because the complete name’s language is not expressly attested.
- Normalized the exact campaign aliases `GL` to `grli` in campaign metadata and the existing header block, preserving the campaign identity and audience.
- Capitalized “He” at the beginning of the second sentence.

### Validated judgments
- The family relationships and Zarkandur setting agree with [[Diesa]], [[Brelith]], and [[Great Library Session Notes - Arc 3]]. The short note adequately identifies this minor family connector.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `OS-rik SHOK-stohn` for Osrik Shockstone. The [[Languages]] guidance uses Tolkien Dwarvish for dwarven naming. Proposal uses short o and i vowels, an audible r and hard k, with tentative initial stress; the clan surname follows its transparent trade-tongue form. No name-specific pronunciation is recorded. Accept or revise this proposal in `Metadata:names:v1`; on acceptance, change its status to `documented` and copy the accepted primary pronunciation to frontmatter.
%%^End%%

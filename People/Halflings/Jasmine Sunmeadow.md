---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-08-09, type: met}
  - {campaign: dufr, date: 1748-08-21, type: last seen}
born: null
gender: female
name: Jasmine Sunmeadow
affiliations:
  - {org: Sunmeadows, type: primary}
whereabouts:
  - {type: home, end: 1748-08-08, location: The Green Leaf}
  - {type: away, start: 1748-08-09, end: 1748-08-21, location: Emerald Song}
  - {type: away, start: 1748-08-22, location: Chardon}
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: 1748
---
# Jasmine Sunmeadow
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her), of the [[Sunmeadows]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on August 9th, 1748 in the [[Emerald Song]], [[Darba]], [[Dunmar]] %%^End%%  
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on August 21st, 1748 in the [[Emerald Song]], [[Chardon]], the [[Chardonian Empire]] %%^End%%

Jasmine Sunmeadow is a halfling adventurer with a strong connection to the natural world. She grew up in Darba, the daughter of the innkeepers of [[The Green Leaf]], but always longed for adventure, and even as a child she could sense the weather and make flowers bloom.
%%^Campaign:DuFr%%
Recently, she married [[Oswalt Tealeaf]], and they booked passage on the [[Emerald Song]] together, to travel north and explore the world. Jasmine has always felt a close connection to [[Jemghari]], and a stewardship over the natural places where she feels the presence of the ancestors most strongly, so now, with her new husband, she is journeying to go out in the world and find these places and tell their stories.
## Relationships
- [[Oswalt Tealeaf]], husband
## Events
- (DR:: 1747): Jasmine meets and falls in love with [[Oswalt Tealeaf]] in [[Darba]]
- (DR:: 1748): Jasmine and Oswalt are married
- (DR:: 1748-08-09): Jasmine and Oswalt leave Darba together on the Emerald Song, heading for adventure

%%^End%%

%% notes
As of DR 1748, assumed to be a level 1 druid
%%

%%^Metadata:names:v1%%
- {"name": "Jasmine Sunmeadow", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Jasmine as a newly married adventurer beginning her travels, with selected childhood backstory; later adventures are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added knownTo: [dufr], persistent name metadata, and the supported DR 1748 viewpoint.
- Repaired the missing subject and closing comma in “with her new husband, she is journeying.”

### Validated judgments
- Confirmed local evidence supports the existing positive dm_notes attestation; its contents remain outside this report.
- [[Session 47 (DuFr)]] supports the marriage and beginning of the shared journey; incidental shipboard conversation does not require additional reference prose.

### Open findings

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The authored campaign section begins with `%%^Campaign:DuFr%%`; the canonical registry code is `dufr`. Replace that opening marker with `%%^Campaign:dufr%%`, retaining the existing boundaries and contents. This is proposed for human review because campaign markers control filtered visibility.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Emerald Song (OneNote)]]
%%^End%%

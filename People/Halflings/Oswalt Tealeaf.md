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
gender: male
name: Oswalt Tealeaf
affiliations:
  - {org: Tealeafs, type: primary}
whereabouts:
  - {type: home, end: 1747, prefix: roads of, location: Dunmar}
  - {type: away, start: 1748, end: 1748-08-08, location: The Green Leaf}
  - {type: away, start: 1748-08-09, end: 1748-08-21, location: Emerald Song}
  - {type: away, start: 1748-08-22, location: Chardon}
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: 1748
---
# Oswalt Tealeaf
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (he/him), of the [[Tealeafs]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on August 9th, 1748 in the [[Emerald Song]], [[Darba]], [[Dunmar]] %%^End%%  
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on August 21th, 1748 in the [[Emerald Song]], [[Chardon]], the [[Chardonian Empire]] %%^End%%

Oswalt Tealeaf is a halfling adventurer, archer, and scout. He grew up traveling the roads of Dunmar with the Tealeaf clan. 
%%^Campaign:DuFr%%
After the Tealeaf clan encountered trouble with Agata Dustmother, and lost Garret Tealeaf, Oswalt decided to learn to defend himself, and picked up the shortbow. After spending several years traveling with his family on safe roads far from the frontier, he met and fell in love with Jasmine Sunmeadow in Darba, who also wanted to adventure, and they left together for the north on the [[Emerald Song]]. 
## Relationships
- [[Garret Tealeaf]], cousin
- [[Jasmine Sunmeadow]], wife
## Events
- (DR:: 1737): Tealeaf clan fights off [[Dustthorn Horde]] orcs, but are then ambushed by [[Agata]]. [[Garret Tealeaf]] is captured.
- (DR:: 1747): Oswalt meets and falls in love with [[Jasmine Sunmeadow]] in [[Darba]]
- (DR:: 1748): Jasmine and Oswalt are married
- (DR:: 1748-08-09): Jasmine and Oswalt leave Darba together on the Emerald Song, heading for adventure

%%^End%%

%% notes
As of DR 1748, assumed to be a level 1 ranger
%%

%% old from onenote
Oswalt Tealeaf grew up on the road, traveling with the Tealeaf clan around Dunmar. After the experiences with Agata and losing Garrett (a cousin twice removed), he picked up the bow and started developing skills, but just traveling around with his family in their new, safer route didn't get him very far. Until he met and fell in love with Jasmine. Now he is committed to traveling with her and exploring the world together.
%%

%%^Metadata:names:v1%%
- {"name": "Oswalt Tealeaf", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Oswalt as a newly married adventurer, with selected childhood and DR 1737 backstory; later adventures are not described. For the whereabouts entry at The Green Leaf beginning in 1748, the original qualification is preserved: #start is approx.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added knownTo: [dufr], persistent name metadata, and the supported DR 1748 viewpoint.
- Preserved the exact “#start is approx” qualification, explicitly tied to the 1748 The Green Leaf whereabouts entry, in the persistent temporal comment so the frontmatter can be safely formatted.

### Validated judgments
- Confirmed local evidence supports the existing positive dm_notes attestation; its contents remain outside this report.
- [[Session 47 (DuFr)]] supports the marriage and beginning of the shared journey; incidental shipboard conversation does not require additional reference prose.

### Open findings

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The authored campaign section begins with `%%^Campaign:DuFr%%`; the canonical registry code is `dufr`. Replace that opening marker with `%%^Campaign:dufr%%`, retaining the existing boundaries and contents. This is proposed for human review because campaign markers control filtered visibility.

- [ ] **Suggestion — editorial.shared_material_redundant:** The “old from onenote” comment substantially repeats the visible childhood, Agata attack, archery, and Jasmine account. Remove the duplicated prose while retaining its distinct kinship qualification for review. Copy-ready replacement comment: `%% Old notes describe Garret Tealeaf as Oswalt’s cousin twice removed. %%` This keeps the additional relationship detail noncanonical and nonpublic without retaining a second biography.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Emerald Song (OneNote)]]
%%^End%%

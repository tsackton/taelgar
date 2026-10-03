---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
ancestry: null
campaignInfo:
  - {campaign: dufr, person: Wellby, date: 1738, type: met}
  - {campaign: dufr, date: 1748-12-16, type: met}
  - {campaign: dufr, date: 1748-12-28, type: last seen}
born: 1671
gender: male
name: Wendel Quickstep
affiliations:
  - {org: Quicksteps, type: primary}
  - {place: The Windward Sail, title: Proprietor, start: 1718, type: leader}
whereabouts:
  - {type: home, start: 1718, location: The Windward Sail}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Wendel Quickstep
>[!info]+ Biographical Info
> A [[Halflings|halfling]] (he/him), of the [[Quicksteps]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:DuFr%% Met by [[Wellby]] on DR 1738 at [[The Windward Sail]], in [[Fiskurth]], the [[Tollen|Free City of Tollen]] %%^End%%
>> %%^Campaign:DuFr%% Met by the [[Dunmar Fellowship]] on December 16th, 1748 at [[The Windward Sail]], in [[Fiskurth]], the [[Tollen|Free City of Tollen]] %%^End%%
>> %%^Campaign:DuFr%% Last seen by the [[Dunmar Fellowship]] on December 28th, 1748 at [[The Windward Sail]], in [[Fiskurth]], the [[Tollen|Free City of Tollen]] %%^End%%

Wendel is the long-time proprietor of *The Windward Sail*, a busy sailor's tavern in [[Fiskurth]]. Known as a place for tales and stories - some true, many not - and a place for gossip, as well as a place to find a crew. Has a few dirty, cramped rooms stacked with "human sized" bunks, and some slightly more comfortable halfling rooms. 
## Relationships
Wendel knows several regulars of [[The Windward Sail]] well, including:
- [[Wellby]], an old acquaintance who frequented The Windward Sail in his youth
- [[Nika Hyne|Nika]], a collector of tales and legends, with connections to the [[University of Tollen]]

%%SECRET[v2:284222bcc889df56acc82e5a3df5e98e]%%

![[wendel-quickstep.png]]

%%^Metadata:names:v1%%
- {name: Wendel Quickstep, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of his ongoing tavern ownership and acquaintances, with ownership beginning in DR 1718. The first campaignInfo meeting with Wellby, DR 1738, retains its original qualification: "# date is approx".
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added persistent name metadata and a supported temporal viewpoint.
- Normalized campaignInfo to dufr and added knownTo: [dufr].
- Preserved the exact inline YAML comment “# date is approx,” with its DR 1738 Wellby-meeting context, in persistent temporal metadata so frontmatter can be safely formatted.

### Validated judgments
- [[Session 80 (DuFr)]] corroborates Wendel’s tavern ownership and existing relationship with [[Nika Hyne]].
- The positive dm_notes attestation has a confirmed local source match; the SECRET block was reviewed separately and retained.

### Open findings

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** Three generated encounter lines use `%%^Campaign:DuFr%%`; the canonical code is `dufr`. Regenerate the lines from campaignInfo or replace each opening marker with `%%^Campaign:dufr%%`, preserving the encounter text and boundaries. The generated header and visibility markers were retained for human review.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Tollen DM Notes]]
%%^End%%

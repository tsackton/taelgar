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
born: 1649
gender: male
name: Ewen Silversong
affiliations:
  - {org: Silversongs, type: primary}
  - {org: Emerald Song, title: Songmaster}
whereabouts: Emerald Song
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Ewen Silversong
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (he/him), of the [[Silversongs]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on August 9th, 1748 in the [[Emerald Song]], [[Darba]], [[Dunmar]] %%^End%%  
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on August 21th, 1748 in the [[Emerald Song]], [[Chardon]], the [[Chardonian Empire]] %%^End%%

Songmaster and storyteller on the [[Emerald Song]].
## Relationships
- [[Harol Silversong]], his nephew
- [[Dani Silversong]], his granddaughter
%%^Campaign:None%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", choice(contains(file.tags,"person"),"Person", "Thing")) as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization OR #item
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%

%%^Metadata:names:v1%%
- {name: Ewen Silversong, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of his shipboard role and family relationships, anchored by the August DR 1748 voyage; the beginning and end of that role are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added persistent name metadata and a supported temporal viewpoint.
- Added knownTo: [dufr] from the existing campaignInfo.

### Validated judgments
- The songkeeper role and family relationships are supported by [[Session 47 (DuFr)]], [[Harol Silversong]], and [[Dani Silversong]]. His ordinary personal name and transparent surname need no separate pronunciation.

### Open findings

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. Retain it if it represents useful remembered or off-vault information; otherwise a human may set `dm_notes: none`. The attestation was preserved.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated relationship-query block uses `%%^Campaign:None%%`; the canonical private-block sentinel is `%%^Campaign:none%%`. Replace only that opening marker or regenerate the block, preserving the query and closing boundary.
- [ ] **Suggestion — editorial.header_typo:** The generated encounter header reads “August 21th, 1748.” Regenerate that header, or change only `21th` to `21st`; the event date and campaign boundary should remain unchanged. The generated header was preserved.
%%^End%%

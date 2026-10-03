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
born: 1712
gender: female
name: Dani Silversong
affiliations:
  - {org: Silversongs, type: primary}
  - {org: Emerald Song, title: Quartermaster}
whereabouts: Emerald Song
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Dani Silversong
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her), of the [[Silversongs]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on August 9th, 1748 in the [[Emerald Song]], [[Darba]], [[Dunmar]] %%^End%%  
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on August 21st, 1748 in the [[Emerald Song]], [[Chardon]], the [[Chardonian Empire]] %%^End%%

Quartermaster and chief trader on the [[Emerald Song]]. Dani Silversong serves as the main spokesperson for the family and is the face of the Emerald Song.
## Relationships
- [[Ewen Silversong]], her grandfather
- [[Harol Silversong]], her uncle
%%^Campaign:none%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", choice(contains(file.tags,"person"),"Person", "Thing")) as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization OR #item
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Dani Silversong", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740s portrait of Dani as quartermaster and chief trader aboard the Emerald Song, confirmed in August 1748; the beginning and end of that role are unknown.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and recorded supported `knownTo`, a primary name entry, and `POV`/`povNotes`.
- Normalized the equivalent `Campaign:None` sentinel to `Campaign:none` and corrected the ordinal `August 21th` to `August 21st`.

### Validated judgments
- The occupation and kinship account is sufficient; [[Emerald Song]] and [[Session 47 (DuFr)]] corroborate the quartermaster and chief-trader role.
- Dani Silversong is an ordinary readable given name with a transparent English compound surname; pronunciation is omitted, while the complete name language remains unknown.
- The relationship query is an operational index, not hidden narrative material.

### Open findings

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. This human attestation may refer to remembered information or another off-vault source. Retain it if that information remains; only a human should change it to `dm_notes: none` after confirming that no useful private remainder exists.
%%^End%%

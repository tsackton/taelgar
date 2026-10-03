---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person]
species: halfling
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-06-30, type: met}
born: 1731
gender: male
name: Tye Strongbones
affiliations:
  - {org: Strongbones, type: primary}
  - {org: The Red Lily Inn, title: Cook}
whereabouts:
  - {type: home, location: The Red Lily Inn}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Tye Strongbones
>[!info]+ Biographical Info
> A [[Halflings|halfling]] (he/him), of the [[Strongbones]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on June 30th, 1748 at [[The Red Lily Inn]], in [[Tokra]], [[Dunmar]] %%^End%%

## Relationships
- [[Wes Strongbones]], father
- [[Cade Strongbones]], twin brother
%%^Campaign:none%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%

%%^Metadata:names:v1%%
- {name: Tye Strongbones, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a Dunmar Frontier-era portrait of Tye as a cook living at The Red Lily Inn, anchored in DR 1748; the note does not establish when his work there began or ended.
%%^End%%

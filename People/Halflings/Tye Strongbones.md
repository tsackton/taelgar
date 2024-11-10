---
headerVersion: 2023.11.25
tags: [person]
campaignInfo: 
- {campaign: dufr, date: 1748-06-30, type: met}
name: Tye Strongbones
born: 1731
species: halfling
ancestry:
gender: male
affiliations: 
- {org: Strongbones, type: primary}
- {org: The Red Lily Inn, title: Cook }
whereabouts: 
- {type: home, location: The Red Lily Inn }
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
%%^Campaign:None%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%

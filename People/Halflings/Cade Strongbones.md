---
headerVersion: 2023.11.20
tags: [dufr/background, person, dufr/met]
campaignInfo: 
- {campaign: dufr, date: 1748-06-30, type: met}
name: Cade Strongbones
born: 1731
species: halfling
ancestry:
gender: male
leaderOf: [ { place: The Red Lily Inn, title: Barkeep, start: 0001} ]
affiliations: [Strongbones]
whereabouts: The Red Lily Inn
---
# Cade Strongbones
>[!info]+ Biographical Info
> [[Halflings|halfling]], he/him of the [[Strongbones]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_RegnalValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on June 30th, 1748 in [[The Red Lily Inn]], [[Tokra]], [[Central Dunmar]] %%^End%%
## Relationships
- [[Wes Strongbones]], father
- [[Tye Strongbones]], twin brother
%%^Campaign:None%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%

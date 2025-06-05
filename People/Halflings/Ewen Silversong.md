---
headerVersion: 2023.11.25
tags: [person]
campaignInfo: 
- {campaign: dufr, date: 1748-08-09, type: met}
- {campaign: dufr, date: 1748-08-21, type: last seen}
name: Ewen Silversong
born: 1649
species: halfling
ancestry:
gender: male
affiliations: 
- {org: Silversongs, type: primary}
- {org: Emerald Song, title: Songmaster }
whereabouts: Emerald Song
dm_owner: none
dm_notes: color
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

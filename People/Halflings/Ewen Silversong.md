---
headerVersion: 2023.11.20
tags: [person, dufr/met, dufr/minor]
displayDefaults: {startStatus: born, startPrefix: b., endPrefix: d., endStatus: died}
campaignInfo: 
- {campaign: dufr, date: 1748-08-09, type: met}
- {campaign: dufr, date: 1748-08-21, type: last seen}
name: Ewen Silversong
born: 1649
species: halfling
ancestry:
gender: male
affiliations: [Silversongs]
leaderOf: [ { place: Emerald Song, title: Songmaster, start: 0001} ]
whereabouts: Emerald Song
---
# Ewen Silversong
>[!info]+ Biographical Info
> [[Halflings|halfling]], he/him of the [[Silversongs]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_RegnalValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on August 9th, 1748 in the [[Emerald Song]], [[Darba]], [[Western Dunmar]] %%^End%%
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on August 21st, 1748 in the [[Emerald Song]], [[Chardon]], the [[Chardonian Empire]] %%^End%%

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

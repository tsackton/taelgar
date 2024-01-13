---
headerVersion: 2023.11.25
tags: [person, dufr/minor]
campaignInfo: 
- {campaign: dufr, date: 1748-08-09, type: met}
- {campaign: dufr, date: 1748-08-21, type: last seen}
name: Dani Silversong
born: 1712
species: halfling
ancestry:
gender: female
leaderOf: [ { place: Emerald Song, title: Quartermaster, start: 0001} ]
affiliations: [ Silversongs ]
whereabouts: Emerald Song
---
# Dani Silversong
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on August 9th, 1748 in the [[Emerald Song]], [[Darba]], [[Dunmar]] %%^End%%  
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on August 21st, 1748 in the [[Emerald Song]], [[Chardon]], the [[Chardonian Empire]] %%^End%%

Quartermaster and chief trader on the [[Emerald Song]]. Dani Silversong serves as the main spokesperson for the family and is the face of the Emerald Song.
## Relationships
- [[Ewen Silversong]], her grandfather
- [[Harol Silversong]], her uncle
%%^Campaign:None%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", choice(contains(file.tags,"person"),"Person", "Thing")) as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization OR #item
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%
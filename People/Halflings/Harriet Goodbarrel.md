---
headerVersion: 2023.11.25
tags: [person]
campaignInfo:
  - { campaign: dufr, person: Wellby, date: 1730, type: met}
  - { campaign: DuFr, date: 1748-12-30, type: met}
name: Harriet Goodbarrel
born: 1685
species: halfling
ancestry: 
gender: female
aliases: [Harriet]
affiliations: 
- {org: Goodbarrels, type: primary }
- {org: The Singing Fox, title: Proprietor, type: leader}
whereabouts:
  - {type: home, end: 1722, location: Western Gulf}
  - {type: home, location: The Singing Fox}
  - {type: away, start: 1748-12-30, end: 1748-12-30, location: Vindristjarna}
dm_owner: tim
dm_notes: color
---
# Harriet Goodbarrel
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her), of the [[Goodbarrels]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by [[Wellby]] on DR 1730 at [[The Singing Fox]], in [[Fairgate Outer]], the [[Tollen|Free City of Tollen]] %%^End%%  
>> %%^Campaign:DuFr%% Met by the [[Dunmar Fellowship]] on December 30th, 1748 on [[Vindristjarna]], in the [[Tollen|Free City of Tollen]] %%^End%%

![[harriet-goodbarrel.png|right|300]]%% notes
Secret mostly contains roleplaying notes; ask if they'd be useful
tagged dm_owner only because of connection to Wellby backstory
%%

Harriet's melodious voice graces *[[The Singing Fox]]* on performance nights, drawing an enthusiastic crowd of locals and passing halflings. Though initially reserved, she truly shines when on stage, and alongside her wife, [[Chenna Goodbarrel|Chenna]], she's made the tavern a warm haven for many.

Harriet married into the [[Goodbarrels|Goodbarrel clan]]; while she never had her own children, she feels a matronly duty to all the scattered Goodbarrel youth. 
## Relationships
- [[Chenna Goodbarrel]], wife
- [[Wellby]], a distant relation, something like a third cousin once removed by marriage
%%^Campaign:None%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%



%%SECRET[1]%%




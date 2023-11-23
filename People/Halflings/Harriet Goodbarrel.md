---
headerVersion: 2023.11.20
tags: [dufr/background, person]
campaignInfo:
  - { campaign: dufr, person: Wellby, date: 1730, type: met}
  - { campaign: DuFr, date: 1748-12-30, type: met}
name: Harriet Goodbarrel
born: 1685
species: halfling
ancestry: 
gender: female
aliases: [Harriet]
affiliations: [Goodbarrels]
leaderOf:
  - {place: The Singing Fox, title: Proprietor, start: 1}
whereabouts:
  - {type: home, end: 1722, location: Western Gulf}
  - {type: home, location: The Singing Fox}
  - {type: away, start: 1748-12-30, end: 1748-12-30, location: Vindristjarna}
---
# Harriet Goodbarrel
>[!info]+ Biographical Info
> [[Halflings|halfling]], she/her of the [[Goodbarrels]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_RegnalValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by [[Wellby]] around 1730 in [[The Singing Fox]], [[Fairgate Outer]], the [[Tollen|Free City of Tollen]] %%^End%%
>> %%^Campaign:DuFr%% Met by the [[Dunmar Fellowship]] on December 30th, 1748 in [[Vindristjarna]], the [[Tollen|Free City of Tollen]], the [[Western Green Sea Region]] %%^End%%

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

%% notes
Secret mostly contains roleplaying notes; ask if they'd be useful
%%

%%SECRET[1]%%

![[harriet-goodbarrel.png]]


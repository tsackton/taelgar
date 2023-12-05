---
headerVersion: 2023.11.25
tags: [dufr/background, person, testcase]
name: Chenna Goodbarrel
born: 1688
species: halfling
ancestry:
gender: female
campaignInfo:
- {campaign: dufr, person: Wellby, date: 1730, type: met, wParty: "<met:u> <person:q> around <target> <current:2rq>"} #date is approx
- {campaign: DuFr, date: 1748-12-30, type: met}
affiliations: 
- {org: Goodbarrels, type: primary}
- {org: The Singing Fox, title: Proprietor, type: leader}
whereabouts:
- {type: home, end: 1725, location: Sembara} # settled in Tollen in 1725 or earlier
- {type: home, start: 1725, location: The Singing Fox}
- {type: away, start: 1748-12-30, end: 1748-12-30, location: Vindristjarna}
---
# Chenna Goodbarrel
>[!info]+ Biographical Info
> A [[Halflings|halfling]] (she/her), of the [[Goodbarrels]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by [[Wellby]] around DR 1730 at [[The Singing Fox]], [[Fairgate Outer]] %%^End%%
>> %%^Campaign:DuFr%% Met by the [[Dunmar Fellowship]] on December 30th, 1748 on [[Vindristjarna]], in the [[Tollen|Free City of Tollen]] %%^End%%

Chenna Goodbarrel owns a small and charming halfling tavern in [[Fairgate Outer]] called *[[The Singing Fox]]*, with her wife [[Harriet Goodbarrel|Harriet]]. Chenna runs the bar and kitchen; warm, welcoming, and charming, she's the heart of the establishment.
## Relationships
- [[Harriet Goodbarrel]], wife
- [[Wellby]], a distant relation, something like a third cousin once removed
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

![[chenna-goodbarrel-portrait.png]]

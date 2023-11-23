---
headerVersion: 2023.11.20
tags: [dufr/met_one, person, dufr/minor]
campaignInfo: 
- {campaign: dufr, person: Kenzo, date: 1748-09-30, type: met}
- {campaign: dufr, person: Kenzo, date: 1748-11-04, type: last seen}
name: Elazar
born: 1665
species: lizardfolk
ancestry:
gender: male
whereabouts: Bedez
---
# Elazar
>[!info]+ Biographical Info
> [[Lizardfolk|lizardfolk]], he/him
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by [[Kenzo]] on September 30th, 1748 in [[Bedez]], [[Orekatu]], the [[South Region]] %%^End%%
>> %%^Campaign:dufr%% Last seen by [[Kenzo]] on November 4th, 1748 in [[Bedez]], [[Orekatu]], the [[South Region]] %%^End%%

A lizardfolk man in the prime of his life, a prophet, seer, and spirit guide who has deeply felt visions and exceptional perception into the spirit realms. A bit of an outcast in his village, seen as someone who sees trouble in everything.

![[elazar-portrait.png|500]]
%%^Campaign:DuFr%%
- (DR:: 1748). Elazar began to acquire a reputation as far-sighted and wise, after he warned of the troubles of the [[Azta Lekua]]. 
- (DR:: 1748-09-30). Elazar met [[Kenzo]] when [[Kenzo]] appeared in [[Orekatu]]. Taught [[Kenzo]] the lizardfolk language and introduced him to lizardfolk spiritual practices over the next month.
%%^End%%
%%^Campaign:None%%
## Relationships
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link FROM #person OR #organization  
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link) 
SORT choice(contains(file.tags,"organization"), "Organization", "Person"), choice(species, species, typeof)
```
%%^End%%
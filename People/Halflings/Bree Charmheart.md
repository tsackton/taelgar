---
headerVersion: 2023.11.25
tags: [person, dufr/minor]
campaignInfo: 
- {campaign: dufr, date: 1748-03-29, type: met }
- {campaign: dufr, date: 1748-07-09, type: last seen}
name: Bree Charmheart
born: 1644
species: halfling
ancestry:
gender: female
affiliations: [Charmhearts]
whereabouts:
- { type: away, start: 1748-03-19, end: 1748-03-19, location: Raven's Hold }
- { type: away, start: 1748-03-28, end: 1748-04-07, location: Karawa }
- { type: away, start: 1748-04-07, end: 1748-04-13, location: traveling to Tokra }
- { type: away, start: 1748-04-13, end: 1748-07-18, location: Tokra }
- { type: away, start: 1748-07-18, end: 1748-08-13, location: Tokra-Darba Road }
- { type: away, start: 1748-08-13, location: Darba }
---
# Bree Charmheart
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on March 29th, 1748 in [[Karawa]], [[Eastern Dunmar]], [[Dunmar]] %%^End%%  
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on July 9th, 1748 in [[Tokra]], [[Dunmar]] %%^End%%

The matriarch of the Charmheart trading clan of halflings.

## Relationships
- [[Callie Charmheart]], granddaughter
- [[Ander Charmheart]], grandson
%%^Date:1748%%
- [[Garret Tealeaf]], occasional traveling companion
%%^End%%
%%^Campaign:None%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%


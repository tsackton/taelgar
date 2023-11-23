---
headerVersion: 2023.11.20
tags: [dufr/background, person, dufr/met]
campaignInfo: 
- {campaign: dufr, date: 1748-08-09, type: met}
- {campaign: dufr, date: 1748-08-21, type: last seen}
name: Harol Silversong
born:
species: halfling
ancestry:
gender: male
leaderOf: [ { place: Emerald Song, title: Captain, start: 0001} ]
affiliations: [ Silversongs ]
whereabouts: Emerald Song
---
# Harol Silversong
>[!info]+ Biographical Info
> [[Halflings|halfling]], he/him of the [[Silversongs]]
> `$=dv.view("_scripts/view/get_RegnalValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on August 9th, 1748 in the [[Emerald Song]], [[Darba]], [[Western Dunmar]] %%^End%%
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on August 21st, 1748 in the [[Emerald Song]], [[Chardon]], the [[Chardonian Empire]] %%^End%%

Captain of the [[Emerald Song]]. He is tough and wiry, tall for a halfling, with olive-brown skin and curly white hair, with bright silver eyes. Although not very talkative for a halfling, he has a good singing voice and often takes up the bass viol in the evenings.
## Relationships
- [[Ewen Silversong]], his uncle
- [[Dani Silversong]], his niece

%%^Campaign:None%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", choice(contains(file.tags,"person"),"Person", "Thing")) as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization OR #item
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%


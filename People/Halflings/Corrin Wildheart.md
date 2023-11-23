---
headerVersion: 2023.11.20
tags: [dufr/background, dufr/met_one, person]
campaignInfo: 
- { campaign: dufr, person: Wellby, date: 1748-09-30, type: met}
- { campaign: dufr, person: Wellby, date: 1748-10-12, type: last seen}
name: Corrin Wildheart
born:
species: halfling
ancestry:
gender: male
leaderOf: [ { place: Wave Dancer, title: Navigator, start: 0001} ]
affiliations: [ Wildhearts]
whereabouts: Wave Dancer
---
# Corrin Wildheart
>[!info]+ Biographical Info
> [[Halflings|halfling]], he/him of the [[Wildhearts]]
> `$=dv.view("_scripts/view/get_RegnalValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by [[Wellby]] on September 30th, 1748 on the [[Wave Dancer]], the [[Eastern Green Sea]] %%^End%%
>> %%^Campaign:dufr%% Last seen by [[Wellby]] on October 12th, 1748 on the [[Wave Dancer]], [[Wahacha]], the [[Vermillion Isles]] %%^End%%

Corrin Wildheart is a navigator with a touch of weather magic, part of the crew of the halfling trading ship the [[Wave Dancer]].
## Relationships
Corrin married into the [[Brightmoons|Brightmoon trading family]], and now sails with them, along with his younger brother [[Lerry Wildheart]].
%%^Campaign:None%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%
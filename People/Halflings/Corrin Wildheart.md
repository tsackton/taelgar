---
headerVersion: 2023.11.25
tags: [dufr/background, person]
campaignInfo: 
- { campaign: dufr, person: Wellby, date: 1748-09-30, type: met}
- { campaign: dufr, person: Wellby, date: 1748-10-12, type: last seen}
name: Corrin Wildheart
born:
species: halfling
ancestry:
gender: male
affiliations:
- {org: Wildhearts, type: primary}
- {org: Wave Dancer, title: Navigator}
whereabouts: 
- {type: home, location: Wave Dancer, wHome: "Based <home:q>", wHomePast: "Was based <home:q>"}
---
# Corrin Wildheart
>[!info]+ Biographical Info
> a [[Halflings|halfling]] (he/him), of the [[Wildhearts]]
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by [[Wellby]] on September 30th, 1748 in the [[Wave Dancer]], sailing to [[Wahacha]], the [[Vermillion Isles]] %%^End%%
>> %%^Campaign:dufr%% Last seen by [[Wellby]] on October 12th, 1748 in the [[Wave Dancer]], [[Wahacha]], the [[Vermillion Isles]] %%^End%%

Corrin Wildheart is a navigator with a touch of weather magic, part of the crew of the halfling trading ship the [[Wave Dancer]]. He has bright blond unkempt hair, and tends towards yellow and red clothes.
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
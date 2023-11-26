---
headerVersion: 2023.11.25
tags: [person, dufr/minor]    
campaignInfo: 
- {campaign: dufr, date: 1748-08-22, type: met}
- {campaign: dufr, person: Delwath, date: 1748-10-21, type: scryed}
- {campaign: dufr, person: letter from Dee Wildcloak, date: 1748-11-15, type: last heard from }
name: Dee Wildcloak
born:
species: halfling
ancestry:
gender: female
affiliations: [Society of the Open Scroll, {org: Wildcloaks, type: primary}]
whereabouts:
- {type: home, location: ""}
- {type: home, end: 1748-09-12, location: Chardon}
- {type: away, start: 1747-12-23, end: 1748-02-01, location: traveling in the Yeraad watershed}
- {type: away, start: 1748-02-02, end: 1748-03-12, location: traveling in Dunmar}
- {type: away, start: 1748-03-13, end: 1748-03-19, location: Stormcaller Tower}
- {type: away, start: 1748-08-22, end: 1748-08-22, location: The Thirsty Scholar}
- {type: away, start: 1748-03-20, end: 1748-04-22, location: traveling to Chardon}
- {type: away, start: 1748-10-18, end: 1748-10-21, location: Darba}
---
# Dee Wildcloak
>[!info]+ Biographical Info
> a [[Halflings|halfling]], she/her of the [[Wildcloaks]]
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on August 22nd, 1748 in [[The Thirsty Scholar]], [[Chardon]], the [[Chardonian Empire]], the [[West Coast Region]] %%^End%%
>> %%^Campaign:dufr%% Scryed by [[Delwath]] on October 21st, 1748 in [[Darba]], [[Western Dunmar]], [[Dunmar]], the [[Central Lowlands Region]] %%^End%%
>> %%^Campaign:dufr%% Last heard from by [[Letter from Dee WIldcloak]] on November 15th, 1748 in Unknown %%^End%%

Dee Wildcloak is an adventurer and treasure-hunter, based for a time in Chardon. 
## Relationships
- Dee has traveled and adventured with the dwarf [[Dain Goldhammer]] and the Chardonian [[Alban]]. 
- Dee's adventures have largely been funded by the Chardonian wizard [[Fausto]]
- Dee knows other adventurers associated with the [[Society of the Open Scroll]], including [[Arcus]] and  [[Vola]]. She is particularly friendly with Vola. 
%%^Date:1748-08-22%%
- (DR:: 1748-08-22): Dee Wildcloak has a short romantic encounter with [[Wellby]]
%%^End%%
%%^Campaign:None%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(contains(file.tags,"organization"), "Organization", "Person"), choice(species, species, typeof)
```
%%^End%%

%%^Campaign:DuFr%%
## Events
Dee was part of a party of adventurers (herself, [[Dain Goldhammer]], and [[Alban]]) who traveled to [[Stormcaller Tower]] and returned to Chardon with several treasures, including [[Hralgar's Eyes]] and the [[Binding Stones]]. 

- (DR:: 1747-12-23): Arcus, Servius, Dee Wildcloak, Dain Goldhammer, and Alban leave Chardon together, on a mission to find treasure for the Society of the Open Scroll, funded by [[Fausto]].
- (DR:: 1748-02-02): Arcus, Servius, Dee Wildcloak, Dain Goldhammer, and Alban arrive in Songara.
- (DR:: 1748-02-03): Dee Wildcloak, Dain Goldhammer, and Alban leave across plains to the north, parting ways with Arcus and Servius. 
- (DR:: 1748-03-13): Dee Wildcloak, Dain Goldhammer, and Alban find the [[Stormcaller Tower]], and make plans to explore. 
- (DR:: 1748-03-18): Alban, Dee Wildcloak, and Dain Goldhammer loot [[Stormcaller Tower]], taking [[Hralgar's Eyes]] and the [[Binding Stones]], which awakens [[Hralgar]] in a confused, disturbed state. In the chaos of fleeing, Alban is killed.
- (DR:: 1748-03-19): Dee Wildcloak and Dain Goldhammer bury Alban outside Stormcaller Tower, and depart for Chardon
- (DR:: 1748-04-22): Dee Wildcloak and Dain Goldhammer arrive in Chardon with [[Hralgar's Eyes]] and the [[Binding Stones]], and give them to [[Fausto]]. 

After the [[Dunmar Fellowship]] acquired [[Hralgar's Eyes]] from [[Fausto]] and caused a stir in [[Chardon]], Dee decided to flee south and get out of [[Fausto]]'s control, first traveling to [[Darba]] and then booking passage south, past the [[Sea of Storms]]. 
- (DR:: 1748-09-12): Dee Wildcloak leaves Chardon quietly, heading for Darba, hoping to escape Fausto's influence
- (DR:: 1748-10-19): Dee Wildcloak writes to the Dunmar Fellowship and Wellby from the Green Leaf Inn, Darba. 
- (DR:: 1748-10-21): Dee Wildcloak boards a ship heading south across the Sea of Storms in Darba

```dataview
TABLE events.text as Event from -"_MoC" flatten file.lists as events where contains(events.text, this.file.name) sort events.DR
````
%%^End%%
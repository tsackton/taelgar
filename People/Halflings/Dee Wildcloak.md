---
headerVersion: 2023.11.25
tags: [person]
displayDefaults: {wOriginU: ""}
campaignInfo: 
- {campaign: dufr, date: 1748-08-22, type: met, format: "<met:U> by <person> on <target> <current:2>"}
- {campaign: dufr, person: Delwath, date: 1748-10-21, type: scryed}
- {campaign: dufr, person: letter from Dee Wildcloak, date: 1748-11-15, format: "Received a <person> on <target>"}
name: Dee Wildcloak
born:
species: halfling
ancestry:
gender: female
affiliations: 
- {org: Society of the Open Scroll, end: 1748-09-12}
- {org: Wildcloaks, type: primary}
whereabouts:
- {type: home, location: ""}
- {type: home, end: 1748-09-12, location: Chardon}
- {type: away, start: 1747-12-23, end: 1748-02-01, prefix: traveling through, location: Yeraad River Basin}
- {type: away, start: 1748-02-02, end: 1748-03-12, prefix: traveling in, location: Dunmar}
- {type: away, start: 1748-03-13, end: 1748-03-19, location: Stormcaller Tower}
- {type: away, start: 1748-03-20, end: 1748-04-22, location: traveling to Chardon}
- {type: away, start: 1748-08-22, end: 1748-08-22, location: The Thirsty Scholar}
- {type: away, start: 1748-10-18, end: 1748-10-21, location: Darba, wLastKnown: ""}
dm_owner: tim
dm_notes: important
---
# Dee Wildcloak
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her), of the [[Wildcloaks]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on August 22th, 1748 [[The Thirsty Scholar]], [[Chardon]] %%^End%%  
>> %%^Campaign:dufr%% Scryed by [[Delwath]] on October 21th, 1748 in [[Darba]], [[Dunmar]] %%^End%%  
>> %%^Campaign:dufr%% Received a [[Letter from Dee WIldcloak]] on November 15th, 1748 %%^End%%

Dee Wildcloak is an adventurer and treasure-hunter, based for a time in Chardon. 
## Relationships
- Dee has traveled and adventured with the dwarf [[Dain Goldhammer]] and the Chardonian [[Alban]]. 
- Dee's adventures have largely been funded by the Chardonian wizard [[Fausto]]
- Dee knows other adventurers associated with the [[Society of the Open Scroll]], including [[Arcus]] and  [[Vola]]. She is particularly friendly with Vola. 
%%^Date:1748-08-22%%
- (DR:: 1748-08-22): Dee Wildcloak has a short romantic encounter with [[Wellby]]
%%^End%%


%%^Campaign:None%%
### Relationships
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Alive"], 
			dv.pages("#person or #organization or #item")
				.where(f => util.isLinkedToPerson(f.file, dv.current().file))
				.sort(f => util.s("<maintype:n>", f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.isAlive(b.file.frontmatter, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Campaign:DuFr%%
## Event
Dee was part of a party of adventurers (herself, [[Dain Goldhammer]], and [[Alban]]) who traveled to [[Stormcaller Tower]] and returned to Chardon with several treasures, including [[Hralgar's Eyes]] and the [[Binding Stones]]. 

- (DR:: 1747-12-23): Arcus, Servius, Dee Wildcloak, Dain Goldhammer, and Alban leave Chardon together, on a mission to find treasure for the Society of the Open Scroll, funded by [[Fausto]].
- (DR:: 1748-02-02): Arcus, Servius, Dee Wildcloak, Dain Goldhammer, and Alban arrive in [[Songara]].
- (DR:: 1748-02-03): Dee Wildcloak, Dain Goldhammer, and Alban leave across plains to the north, parting ways with Arcus and Servius. 
- (DR:: 1748-03-13): Dee Wildcloak, Dain Goldhammer, and Alban find the [[Stormcaller Tower]], and make plans to explore. 
- (DR:: 1748-03-18): Alban, Dee Wildcloak, and Dain Goldhammer loot [[Stormcaller Tower]], taking [[Hralgar's Eyes]] and the [[Binding Stones]], which awakens [[Hralgar]] in a confused, disturbed state. In the chaos of fleeing, Alban is killed.
- (DR:: 1748-03-19): Dee Wildcloak and Dain Goldhammer bury Alban outside Stormcaller Tower, and depart for Chardon
- (DR:: 1748-04-22): Dee Wildcloak and Dain Goldhammer arrive in Chardon with [[Hralgar's Eyes]] and the [[Binding Stones]], and give them to [[Fausto]]. 

After the [[Dunmar Fellowship]] acquired [[Hralgar's Eyes]] from [[Fausto]] and caused a stir in [[Chardon]], Dee decided to flee south and get out of [[Fausto]]'s control, first traveling to [[Darba]] and then booking passage south, past the [[Sea of Storms]]. 

- (DR:: 1748-09-12): Dee Wildcloak leaves Chardon quietly, heading for Darba, hoping to escape Fausto's influence
- (DR:: 1748-10-19): Dee Wildcloak writes to the Dunmar Fellowship and Wellby from [[The Green Leaf]] Inn, Darba. 
- (DR:: 1748-10-21): Dee Wildcloak boards a ship heading south across the Sea of Storms in Darba

```dataview
TABLE events.text as Event from -"_MoC" AND -"People/Halflings/Dee Wildcloak" flatten file.lists as events where contains(events.text, this.file.name) sort events.DR
````
%%^End%%

%% One Note

**Trait (Aspiration):** as discussed below
 
Halfling adventurer (fighter, ranged battlemaster) who explored Eudomis' tower with her companions, Dain Goldhammer (dwarven paladin, oath of glory), and Alban (deceased, human sorcerer).
 
She can usually be found at one of the better-class student inns, and keeps a small apartment in the academic quarter.
 
## Appearance
 
Young halfling woman. Wiry, quick. Short even for a halfling, her main weapon is a vicious little crossbow that she wields with deadly accuracy. Tanned and freckled, with curly brown hair and a cheerful smile.
 
## Mannerisms
 
Cheerful, good natured. She has a clear goal and a clear plan - earn enough money to buy a nice crossroads inn somewhere with lots of travelers, find a man, and start a family.
 
May look Wellby up and down appraisingly.
 
## Motivation
 
She is clearly in it for the money and adventure. The pay is good, she gets to explore, and is well supported. Family is mostly sailors plying the Chardon coastal trade, often trsveling as far north as Mawar or beyond - but unusually for a halfling she hates boats and the ocean. So set off on her own to make her way in the world.
 
Would like someday to settle down, run an inn at some crossroads with lots of travelers coming and going, with a nice man and have lots of little halfling babies - but needs a nice big chunk of money to do this.
 
Susceptible to flirting, also generally just friendly. But reluctant to do anything that would jeopardize her status with the Open Scroll and get in the way of her nest egg.
 
She figures she needs about 5000-7000 gp to buy or build an inn of the sort she wants and have enough to get it up and running. She currently has 3000 gp.

%%
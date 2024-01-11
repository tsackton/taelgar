---
headerVersion: 2023.11.25
excludeRooted: ["Clee"]
tags: [person, dufr/major]
campaignInfo:
- {campaign: DuFr, date: 1748-06-02, type: freed}
- {campaign: dufr, date: 1748-07-09, type: last seen}
name: Garret Tealeaf
born: 1656
species: halfling
gender: male
aliases: [Garret]
affiliations: [{org: Tealeafs, type: primary}]
whereabouts:
- {type: home, end: 1737, prefix: roads of, location: Dunmar} # date of capture is approx
- {type: away, start: 1737, end: 1748-06-07, location: Agata's lair}
- {type: away, start: 1748-06-08, end: 1748-06-19, location: Karawa}
- {type: away, start: 1748-06-20, end: 1748-06-29, location: traveling to Tokra}
- {type: away, start: 1748-06-30, end: 1748-07-17, location: The Red Lily Inn}
- { type: away, start: 1748-07-18, end: 1748-08-12, location: Tokra-Darba Road }
- { type: away, start: 1748-08-13, location: Darba }
---
# Garret Tealeaf
>[!info]+ Biographical Info
> a [[Halflings|halfling]], he/him of the [[Tealeafs]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:DuFr%% Freed by the [[Dunmar Fellowship]] on June 2nd, 1748 in [[Agata's lair|Agata's Lair]], [[Garamjala Desert|Garamjala]], [[Nashtkar]], the [[Desolation of Cha'mutte]] %%^End%%
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on July 9th, 1748 in [[The Red Lily Inn]], [[Tokra]], [[Central Dunmar]], [[Dunmar]], the [[Greater Dunmar]] %%^End%%

Garret Tealeaf grew up traveling the roads of Dunmar with the Tealeaf trading family, eventually becoming the patriarch of a group of 5 well-armed and defended caravans that regularly made the circuit from Chardon, east to Songara, Tokra, and Karawa, before turning south across the Yuvanti Mountains to Nayahar, and then north along the coast to Darba, and back to Chardon. 
%%^Campaign:DuFr%%
## Relationships
- [[Charmhearts]], occasional traveling companions after being freed from imprisonment in [[Agata's lair]]. 
- [[Agata]], his captor and tormentor
- [[Seeker]], who freed him from his wooden puppet form
- [[Wellby]], who introduced him to the Charmhearts
- [[Oswalt Tealeaf]], a cousin
## Events
In DR 1737, the Tealeaf family fought of an orc attack from the [[Dustthorn Horde]], associated with [[Agata]]. In revenge, [[Agata]] herself attacked, killing a number of Tealeafs, and then capturing Garret, and using her magic to turn him into a wooden puppet, forced to serve her. She promised the surviving Tealeafs, including [[Oswalt Tealeaf]], that if they did not come east of the Hara River for 15 years, she would return Garret to them. 

The [[Dunmar Fellowship]] saw a vision of this attack in the [[Soul Lantern Vision]]. 

Garret spent the next 11 years in servitude, as a wooden scarecrow, until he was rescued by the [[Dunmar Fellowship]]. Since then, he has slowly come back to himself, although he reminds extremely nervous around magic, and especially any treasure claimed from Agata herself. 

 - (DR:: 1737): Tealeaf clan fights off [[Dustthorn Horde]] orcs, but are then ambushed by [[Agata]]. [[Garret Tealeaf]] is captured.
  - (DR:: 1748-06-02):  [[Garret Tealeaf]] is freed from his imprisonment as a wooden scarecrow by [[Seeker]] and the [[Dunmar Fellowship]]. 
%%^End%%
%%^Campaign:None%%
```dataview
TABLE events.text as Event from -"_MoC" flatten file.lists as events where contains(events.text, this.file.name) sort events.DR
```
%%^End%%
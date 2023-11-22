---
headerVersion: 2023.11.20
tags: [person, dufr/met, dufr/minor, status/needswork/internal]
displayDefaults: {startStatus: born, startPrefix: b., endPrefix: d., endStatus: died}
campaignInfo:
- {campaign: dufr, date: 1748-03-29, type: met }
- {campaign: dufr, date: 1748-07-09, type: last seen}
name: Ander Charmheart
born: 1721
species: halfling
ancestry:
gender: male
affiliations: [Charmhearts]
whereabouts:
- { type: away, start: 1748-03-19, end: 1748-03-19, location: Raven's Hold }
- { type: away, start: 1748-03-28, end: 1748-04-07, location: Karawa }
- { type: away, start: 1748-04-07, end: 1748-04-13, location: traveling to Tokra }
- { type: away, start: 1748-04-13, end: 1748-07-18, location: Tokra }
- { type: away, start: 1748-07-18, end: 1748-08-13, location: Tokra-Darba Road }
- { type: away, start: 1748-08-13, location: Darba }
---
# Ander Charmheart
>[!info]+ Biographical Info
> [[Halflings|halfling]], he/him of [[Charmhearts]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on March 29th, 1748 in [[Karawa]], [[Eastern Dunmar]], [[Dunmar]] %%^End%%
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on July 9th, 1748 in [[Tokra]], [[Central Dunmar]], [[Dunmar]] %%^End%%

%%  Ander's illness notes. 
A halfling trader from Sembara, grandson of Bree and brother to Callie. Curious. Explored Raven's Hold, got caught in a wave of Abyssal energy, and when mad. Was at Raven's Hold at the same time the demon was summoned, but fled as strange abyssal plants started to grow. Callie kept some of the weird vines, showed to party in Karawa. 

In Karawa - the madness drove him to endless hunger, to and to wish to be devoured by the maw demons that attacked Karawa. This intense form of the madness lasted while the demon remained, but faded when the demon was killed. 

In Tokra - July 1748: Anders is not exactly better, but is mostly conscious and functional. Can describe more clearly what happened -- felt like a wave of something, washing over him, this chaotic dark energy, almost like a bomb and then the shrapnel embedded in his mind. Now the shrapnel has faded but the wounds remain. Speaks slowly, cautiously, struggles for words.
%%

A young, rambunctious and excessively curious [[Halflings|halfling]], traveling with the [[Charmhearts|Charmheart]] trading caravan as a scout and general hand. 

Ander is brother to [[Callie Charmheart]] and the grandson of [[Bree Charmheart]]. 
%%^Campaign:DuFr%%
In March 1748, was taken with madness by contact with Abyssal energy during a demon summoning at [[Raven's Hold]], on the northern border of [[Dunmar]]. While partially cured by the defeat of the demon by [[Dunmar Fellowship]], as of the summer of 1748 he still struggles with speech, and nightmares. 
%%^End%%
%%^Campaign:None%%
## Relationships
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%
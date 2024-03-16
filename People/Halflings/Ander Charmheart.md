---
headerVersion: 2023.11.25
tags: [person]
timelineDescriptor: Charmhearts
campaignInfo:
- {campaign: dufr, date: 1748-03-29, type: met }
- {campaign: dufr, date: 1748-07-09, type: last seen}
name: Ander Charmheart
born: 1728
species: halfling
ancestry:
gender: male
affiliations: 
- {org: Charmhearts, type: primary}
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
> A [[Halflings|halfling]] (he/him), of the [[Charmhearts]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on March 29th, 1748 in [[Karawa]], [[Eastern Dunmar]], [[Dunmar]] %%^End%%
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on July 9th, 1748 in [[Tokra]], [[Dunmar]] %%^End%%

A young, rambunctious and excessively curious halfling, traveling with the Charmheart trading caravan as a scout and general hand. 

## Relationships
- [[Callie Charmheart]], older sister and traveling companion
- [[Bree Charmheart]], grandmother and traveling companion
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
%%^Campaign:DuFr%%
## Events
In March 1748, Ander was taken with a demonic curse as a result of accidental contact with Abyssal energy during the demon summoning at [[Raven's Hold]]. The curse caused him to suffer from an overwhelming hunger for raw flesh. When the demon [[Oduk]] was killed by the [[Dunmar Fellowship]], Ander was released from the worst of the curse. As of the summer of 1748, he still suffered from occasional confusion and difficulty speaking and finding the right word, describing the feeling as the wounds left by the shrapnel from a chaotic bomb that exploded in his mind. 

### Chronology
- (DR:: 1748-03-19): While exploring the ruined Dunmari fort of [[Raven's Hold]], Ander Charmheart heard a strange chanting, and was grabbed by a thorny vine while trying to flee. He later described this as like a wave of chaotic dark energy washing over him, and then exploding in his mind like a bomb. 
- (DR:: 1748-03-22): Ander Charmheart begins to display signs of madness, feeling either consumed by a ravenous hunger for raw flesh, or raving about the coming master who would consume the world. 
- (DR:: 1748-04-12): Ander Charmheart is released from the demonic curse possessing him, when the demon [[Oduk]] is killed by the [[Dunmar Fellowship]] in [[Raven's Hold]]
%%^End%%
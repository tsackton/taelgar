---
headerVersion: 2023.11.25
tags: [person]
campaignInfo:
- {campaign: dufr, date: 1748-03-29, type: met }
- {campaign: dufr, date: 1748-07-09, type: last seen}
name: Callie Charmheart
born: 1722
species: halfling
ancestry:
gender: female
affiliations: 
- {org: Charmhearts, type: primary }
whereabouts: 
- { type: away, start: 1748-03-19, end: 1748-03-19, location: Raven's Hold }
- { type: away, start: 1748-03-28, end: 1748-04-07, location: Karawa }
- { type: away, start: 1748-04-07, end: 1748-04-13, location: traveling to Tokra }
- { type: away, start: 1748-04-13, end: 1748-07-18, location: Tokra }
- { type: away, start: 1748-07-18, end: 1748-08-13, location: Tokra-Darba Road }
- { type: away, start: 1748-08-13, location: Darba }
---
# Callie Charmheart
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her), of the [[Charmhearts]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on March 29th, 1748 in [[Karawa]], [[Eastern Dunmar]], [[Dunmar]] %%^End%%  
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on July 9th, 1748 in [[Tokra]], [[Dunmar]] %%^End%%

One of the Charmhearts, a halfling family of long-distance merchants and traders, who make a living trading between [[Dunmar]] and [[Sembara]]. 

## Relationships
- [[Ander Charmheart]], younger brother and traveling companion
- [[Bree Charmheart]], grandmother and traveling companion
%%^Date:1748%%
- [[Garret Tealeaf]], occasional traveling companion 
%%^End%%

%%^Campaign:None%%
### Relationships
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person or #organization or #item")
				.where(f => util.isLinkedToPerson(f.file, dv.current().file))		
				.sort(f => util.s("<maintype:n>", f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```

%%^End%%
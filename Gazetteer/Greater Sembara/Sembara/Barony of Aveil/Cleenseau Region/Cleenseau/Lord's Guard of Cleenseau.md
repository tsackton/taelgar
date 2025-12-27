---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {boxInfo: ""}
name: Lord's Guard of Cleenseau
typeOf: army
subTypeOf: warband
whereabouts: Cleenseau
dm_owner: mike
dm_notes: color
---
# The Lord's Guard of Cleenseau
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Lord's Guard of Cleenseau is a troop of 18 people-at-arms who are responsible for protecting the [[Essford Manor]], watching the [[River Gate of Cleenseau|River Gate]] and [[North Gate of Cleenseau|North Gate]] and maintaining peace within the walls. These are not well trained, professional soldiers, but most of them can ride and shoot relatively well and have some practice with spears and wearing armor.

The guard is divided up into a household guard of 10, under the command of [[Ames Benthey]] and a town watch of 8, under the command of the sheriff [[Ysabel]]. The town watch is primarily responsible for guarding the [[River Gate of Cleenseau|River Gate]] and the [[North Gate of Cleenseau|North Gate]], and aides [[Nicholas Wysson|the magistrate]] when needed.

The household guard is responsible for the defense of the [[Essford Manor]], the personal safety of [[Wymar Essford]] and his family, and assists the town watch when needed.

The town watch is led by [[Beatrix Thorne]], and the current members are:
* [[Colin]], a guardsman
* [[Sarabeth]], a guardswoman
* [[Betsy Thorne]], a guardswoman
* [[Jon]], a guardsman
* Clarissa, a guardswoman, recently killed by zombies
* Jacques, a guardsman, recently killed by zombies

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {defArt: the}
name: Shockstone Clan
typeOf: clan
ancestry: dwarven
whereabouts: Zarkandur
dm_notes: none
dm_owner: none
---
# The Shockstone Clan
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Shockstones are one of the most prominent dwarven clans in [[Am'khazar]], and the de facto rulers of [[Zarkandur]]. 

The clan is best known, at least outside dwarven circles, through [[Brelith|Brelith Shockstone]], a priest of the [[Bahrazel]] and hero of the [[Battle of Voltara]]. 

###  Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"],
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```


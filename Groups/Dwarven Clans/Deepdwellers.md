---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {defArt: the}
name: Deepdweller Clan
typeOf: clan
ancestry: dwarven
dm_owner: none
dm_notes: none
---
# The Deepdweller Clan
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Deepdwellers are a dwarven clan originally from the lost kingdom of [[Enderra]], now mostly living around [[Apporia]]. 

### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"],
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```

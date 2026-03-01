---
headerVersion: 2023.11.25
tags: [group, status/gameupdate/dufr]
ancestry: Urskan
displayDefaults: {defArt: ""}
typeOf: magical bloodline
partOf: Rodnya
dm_notes: important
dm_owner: tim
---
# Rodnya Voknaz
>[!info]+ Information  
> An [[Ursk|Urskan]] magical bloodline  
> `$=dv.view("_scripts/view/get_Affiliations")`  
> Parent Organization: the [[Rodnya|Rodnye]]

The Rodnya Voknaz is one of the eight [[Rodnya|rodnye]] that rule [[Ursk]]. Voknaz is based in the western reaches of the country and is known for war magic: shaping elemental forces into destructive spells, and arguing that offensive power is the best defense against the threats of the far north.

The Rodnya’s headquarters is the [[Voknaz Manor]], a heavily warded estate that includes at least one extraplanar portal to the [[Frostfell]].


%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
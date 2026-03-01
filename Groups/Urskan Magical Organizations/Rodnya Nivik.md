---
headerVersion: 2023.11.25
tags: [group]
ancestry: Urskan
displayDefaults: {defArt: ""}
typeOf: magical bloodline
partOf: Rodnya
dm_notes: important
dm_owner: tim
---
# Rodnya Nivik
>[!info]+ Information  
> An [[Ursk|Urskan]] magical bloodline  
> `$=dv.view("_scripts/view/get_Affiliations")`  
> Parent Organization: the [[Rodnya|Rodnye]]

The Rodnya Nivik is one of the eight [[Rodnya|rodnye]] that rule [[Ursk]]. Nivik is most closely associated with conjuration magic, and especially with teleportation.


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
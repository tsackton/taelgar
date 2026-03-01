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
# The Rodnya Kinzal
>[!info]+ Information  
> An [[Ursk|Urskan]] magical bloodline  
> `$=dv.view("_scripts/view/get_Affiliations")`  
> Parent Organization: the [[Rodnya]]

The Rodnya Kinzal is one of the eight [[Rodnya|rodnye]] that rule [[Ursk]]. Kinzal is most closely associated with enchantment and illusion magic, and in modern Urskan politics is known for its hostility toward the [[Ursk#The People of Ursk|novja]].

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
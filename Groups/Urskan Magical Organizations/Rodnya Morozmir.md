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
# The Rodnya Morozmir
>[!info]+ Information  
> An organization  
> `$=dv.view("_scripts/view/get_Affiliations")`


The Rodnya Morozmir is one of the eight [[Rodnya|rodnye]] that rule [[Ursk]]. Morozmir is based in the southeast of the country and is best known for defensive magic; it is often credited with involvement in the vast arcane wards that protect much of Ursk.


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
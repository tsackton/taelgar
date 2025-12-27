---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {partOf: "", boxInfo: "<ancestry:UA> <typeof:UA> of <deity:UA>"}
typeOf: mystery cult
ancestry: Dunmari
deity: Laka
dm_notes: important
dm_owner: tim
---
# The Lakan Mystai
>[!info]+ Information  
> A [[Dunmar|Dunmari]] mystery cult of [[Laka]]  
> `$=dv.view("_scripts/view/get_Affiliations")`

The mystery cult of the Dunmari god [[Laka]]. Guardians of secret knowledge, especially concerning the lore of other planes, and the secrets of manipulating planar energy to create magic.

%%SECRET[1]%%

%%^Campaign:None%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
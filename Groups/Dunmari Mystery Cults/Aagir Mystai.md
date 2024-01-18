---
headerVersion: 2023.11.25
tags: [organization, status/unknown]
displayDefaults: {partOf: "", boxInfo: "<ancestry:UA> <typeof:UA> of <deity:UA>"}
name: Aagiri
typeOf: mystery cult
ancestry: Dunmari
deity: Aagir
---
# Aagiri
>[!info]+ Information  
> A [[Dunmar|Dunmari]] mystery cult of [[Aagir]]  
> `$=dv.view("_scripts/view/get_Affiliations")`

The mystery cult dedicated to the Dunmari god [[Aagir]], a traveling order of warriors who protect the roads of [[Dunmar]]. 

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
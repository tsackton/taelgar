---
headerVersion: 2023.11.25
tags: [organization]
displayDefaults: {defArt: "the" }
typeOfAlias: noble house
typeOf: family
whereabouts: Barony of Aveil
dm_plans: yes
dm_notes: important
---
# The D'Aslains
>[!info]+ Information  
> A noble house  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A longstanding noble family in the [[Barony of Aveil]] with an ancient history. One of the wealthiest families in the [[Auberonne]] river valley.

%%^Campaign:None%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2Fr> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
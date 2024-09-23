---
headerVersion: 2023.11.25
tags: [status/needswork/internal, organization]
dm_notes: color
dm_plans: no
typeOf: clan
ancestry: dwarven
whereabouts: Barony of Aveil
---
# Ferrystones
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% dwarven clan in Rinburg and Aslain, known for their work building with recovered stones from  ruins %%

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
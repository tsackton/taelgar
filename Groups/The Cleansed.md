---
headerVersion: 2023.11.25
tags: [organization, status/check/tim]
displayDefaults: {defArt: ''}
name: The Cleansed
typeOf: cult
ancestry: mysterious
---
# The Cleansed
>[!info]+ Information  
> A mysterious cult  
> `$=dv.view("_scripts/view/get_Affiliations")`

A mysterious secret society in [[Chardon]] of which [[People/Chardonians/Fausto]] is a member and seem to be dedicated in some way to Drankorian purity. 

%% Tim: Does this need more? %%

%%SECRET[1]%%

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
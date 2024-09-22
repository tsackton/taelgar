---
headerVersion: 2023.11.25
tags: [organization/family]
typeOf: family
typeOfAlias: merchant family
ancestory: Sembaran
whereabouts: Embry
---
# The Garay Family
>[!info]+ Information  
> A merchant family  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A wealthy merchant family based in Embry, specializing in cloth.

%% Free to be used for other purposes, but note some of the details on Susanne's page %%

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
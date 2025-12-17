---
headerVersion: 2023.11.25
tags: [organization]
displayDefaults: {defArt: the}
name: Sunmeadows
typeOf: family
ancestry: halfling
dm_notes: none
dm_owner: none
---
# The Sunmeadows
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

%% Jasmine's parents own [[The Green Leaf]] in [[Darba]], but what the rest of the family does, and whether they travel or are largely based in Darba,  is not invented. %%

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
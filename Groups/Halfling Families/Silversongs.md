---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {defArt: the}
typeOf: family
ancestry: halfling
name: Silversongs
affiliations:
- {place: Emerald Song, type: leader, title: Owners}
dm_owner: none
dm_notes: none
---
# The Silversongs
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

A halfling family of traders and sailors based in the [[Nevos Sea]]. 

%% From OneNote
The Silversongs have been sailing the trade routes between Chardon and the Nevos Sea for the past three generations, about 120 years. The clan itself is large and scattered, with at least four Silversong ships plying the Chardon->Dunmar trade, and two more sailing the coastal routes north of Chardon. This particular branch of the family has focused on fast coastal trade.
%%

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
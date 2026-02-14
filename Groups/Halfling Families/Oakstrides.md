---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {defArt: the}
name: Oakstrides
typeOf: family
ancestry: halfling
dm_notes: none
dm_owner: tim
---
# The Oakstrides
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Oakstrides are a halfling family of moderate prominence, based along the [[Volta Watershed]]. Though not a major trading family, they are a large, well-connected clan of performers, innkeepers, storytellers, and wanderers. The most famous Oakstride is likely [[Finnan Oakstride]], a storyteller and collector of songs with a particular connection to the [[Zimkova Highlands]]. 

%%^Campaign:None%%
### Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
The vibe is: if there is a small crossroads inn, incongruously homely in a backwoods part of the upper Volta, it would not be surprising at all to find it run by an Oakstride. But unlike many halfling families they are not organized into a major family corporation, and Finnan grew up in a relatively small, for halflings, caravan of artists, probably with his parents, siblings, and a few cousins, aunts, uncles, etc. 

%%^End%%

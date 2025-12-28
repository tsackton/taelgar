---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {defArt: the, partOf: ""}
campaignInfo:
name: Honeyhills
ancestry: halfling
typeOf: family
dm_notes: none
dm_owner: none
---
# Honeyhills
>[!info]+ Information
> A [[Halflings|halfling]] family
> `$=dv.view("_scripts/view/get_Affiliations")`

A family of halfling traders and sailors based in the Nevos Sea, the Gulf of Chardon, and areas north. 

%%^Date:1743%%
The Honeyhills' two major trading ships, the Twilight Breeze and the Starlight Bough, which plied the coasts from [[Darba]] to [[Suhaya]], were lost in a tragic storm north of [[Chardon]] in the winter of DR 1743, with few survivors. Many of the Honeyhills who escaped tragedy were subsequently taken in by other halfling ships. 
%%^End%%

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
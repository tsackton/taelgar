---
headerVersion: 2023.11.25
tags: [organization]
displayDefaults: {defArt: the}
name: Hardstones
typeOf: clan
ancestry: dwarven
dm_notes: none
dm_owner: none
---
# The Hardstones
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Hardstones are a prominent dwarven clan in Tokra, primarily known for their long-standing association with the [[Archives|Tokra Archives]]. The clan has traditionally worked at the archives, primarily as architects and generally managing the physical infrastructure of the building, settling in [[Tokra]] in the years after the [[Fire War]]. But they are also known, at times, to work some minor runic magic to protect scrolls and mend damage.

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
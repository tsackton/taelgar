---
tags: [organization, status/stub, status/check/ai]
displayDefaults: {defArt: the}
name: Brightmoons
typeOf: family
ancestry: halfling
dm_notes: none
dm_owner: none
---

# The Brightmoons
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Brightmoons are a seafaring halfling clan, closely associated with the ship [[Wave Dancer]]. The clan’s matriarch, [[Wella Brightmoon]], serves as the Wave Dancer’s captain; among her kin are [[Pearl Brightmoon]] (first mate) and [[Rose Brightmoon]] (musician).

## Sources

- [[Pearl Brightmoon]]
- [[Rose Brightmoon]]
- [[Wella Brightmoon]]

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

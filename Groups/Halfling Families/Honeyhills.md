---
headerVersion: 2023.11.25
tags: [organization/family, status/notes, status/unknown]
displayDefaults: {defArt: the, partOf: ""}
campaignInfo:
name: Honeyhills
ancestry: halfling
typeOf: family
---
# Honeyhills
>[!info]+ Information
> A [[Halflings|halfling]] family
> `$=dv.view("_scripts/view/get_Affiliations")`

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file.frontmatter))
				.map(b => [util.getName(b.file.name), util.getLoc(b.file.frontmatter)]))
```
%%^End%%
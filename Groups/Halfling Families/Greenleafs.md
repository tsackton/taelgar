---
headerVersion: 2023.11.25
tags: [organization/family]
displayDefaults: {definitiveArticle: the, partOf: ""}
campaignInfo: []
name: Greenleafs
typeOf: family
ancestry: halfling
---
# The Greenleafs
>[!info]+ Information
> A [[Halflings|halfling]] family

%% no information exists about this family; only created members were two brothers traveling for unknown reasons%%
## Members
- [[Lyle Greenleaf]] and [[Alton Greenleaf]], brothers
%%^Campaign:None%%
```dataviewjs
const { util } = customJS
dv.table(["Person", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file.frontmatter))
				.map(b => [util.getName(b.file.name), util.getLoc(b.file.frontmatter)]))
```
%%^End%%
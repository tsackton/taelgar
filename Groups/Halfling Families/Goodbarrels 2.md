---
tags: [organization/family, status/unknown]
displayDefaults: {definitiveArticle: the}
campaignInfo: []
name: Goodbarrels
typeOf: family
---


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
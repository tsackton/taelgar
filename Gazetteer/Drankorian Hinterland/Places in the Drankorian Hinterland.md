---
tags: [background]
excludePublish: ["all"]
dm_owner: none
dm_notes: none
---
### Places in the Drankorian Hinterland
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inRegion("Drankorian Hinterland", f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```


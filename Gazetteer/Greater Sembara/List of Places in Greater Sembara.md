---
tags: [background]
excludePublish: ["all"]
dm_owner: none
dm_notes: none
---
### Places in Greater Sembara
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.homeLocation("Greater Sembara", f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```


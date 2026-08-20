---
lintedAt: "2026-08-20T14:57:54-04:00"
lintVersion: "3.0"
tags: [background]
name: Places in Greater Chardon
excludePublish: [all]
dm_owner: none
dm_notes: none
POV: undated
---
### Places in Greater Chardon
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation("Greater Chardon", f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

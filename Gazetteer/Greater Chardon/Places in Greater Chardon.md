---
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
tags: [background]
name: Places in Greater Chardon
excludePublish: [all]
dm_owner: none
dm_notes: none
POV: timeless
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

%%^Metadata:article:v1%%
mode: generated index
povNotes: "Accuracy range: timeless. Generated structural index whose results depend on current vault metadata rather than an in-world speaking date."
%%^End%%

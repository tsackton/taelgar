```
All the things in a place

```dataviewjs
const { util } = customJS
dv.table(["File", "TypeOf", "Part Of"], 
			dv.pages("#religion or #place")
				.where(f => util.inLocation("Spiritual Realms", f.file.frontmatter))
				.map(b => [util.getName(b.file.name), b.typeOf, b.partOf]))
```
```
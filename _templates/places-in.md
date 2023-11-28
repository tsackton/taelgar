%%^Campaign:None%%
### Places in <% tp.file.title %>
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter))
				.map(b => [util.s("<name>", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%
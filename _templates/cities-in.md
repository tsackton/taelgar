%%^Campaign:None%%
### Cities in <% tp.file.title %>
```dataviewjs
const { util } = customJS
dv.table(["Place", "Region", "Type Of", "Population"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter) && (f.file.frontmatter.typeOf == "city" || f.file.frontmatter.typeOf == "village" || f.file.frontmatter.typeOf == "town" || f.file.frontmatter.typeOf == "hamlet"))
				.sort(f => util.s("<home:1>", f.file))
				.map(b => [util.s("<name>", b.file), util.s("<home:1>", b.file), util.s("<maintype>", b.file), util.s("<population>", b.file)]))
```

%%^End%%
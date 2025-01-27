%%^Campaign:None%%
### Cities in <% tp.file.title %>
```dataviewjs
const { util } = customJS
dv.table(["Place", "Region", "Type Of", "Population"], 
			dv.pages("#place")
				.where(f => util.inPolity(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.file.frontmatter.typeOf == "settlement"))
				.sort(f => util.s("<home:1>", f.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<home:1>", b.file, dv.current().pageTargetDate), util.s("<maintype>", b.file, dv.current().pageTargetDate), util.s("<population>", b.file, dv.current().pageTargetDate)]))
```

%%^End%%
---
headerVersion: 2023.11.25
tags: [place]
name: Volta Watershed
typeOf: watershed
whereabouts:
- { type: home, location: Greater Sembara, linkText: in }
dm_owner: none
dm_notes: none
---
# The Volta Watershed
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Volta Watershed is the drainage basin of the [[Volta]] and its tributaries, including the waterways that pass through [[Tollen]] and the upper lake country around [[Lake Kamchak]]. 

%%^Campaign:none%%

## Places in the Volta Watershed

```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.typeOf == "river" || f.typeOf == "waterway" || f.typeOf == "lake"))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%

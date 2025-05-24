---
tags: [place]
typeOf: region
dm_notes: none
dm_owner: tim
---

The Chasa-Nahadi watershed is a vast river system that drains the interior basin of the western [[Sentinel Range|Sentinels]]. Geographically, this watershed is composed of three distinct areas:

- The [[Chasa River Valley]], consisting of the [[Chasa]] and its tributaries. The [[Chasa]] flows west from the southern reaches of the [[Central Highlands]], passing through vast forests before it is joined by the [[Nahadi]] just east of [[Chardon]]. Numerous tributaries join the [[Chasa]], largely small forest rivers (exemplified by the [[Kayan]]). %%NOTE: most tributaries are unnamed so far, and exactly which branch of the upper reaches of the [[Chasa]] is the [[Chasa]] vs tributaries is not determined. Canonically, the [[Chasa]] retains is name after the [[Nahadi]] joins, so the river that flows past [[Chardon]] is the [[Chasa]]. %%

- The [[Nahadi]] and [[Lake Valandros]] form a distinct region of the watershed, dominated by the vast size of [[Lake Valandros]]. The [[Nahadi]] is the only outflow from [[Lake Valandros]], and is a wide, broad river for its entire length. Numerous smaller tributaries flow into [[Lake Valandros]]. %%NOTE: no tributaries are mapped or named, really, but presumably there are rivers that flow into the lake from the west and east. [[Lake Valandros]] is roughly the size of Lake Michigan for context. %%

- The [[Zarnato]] watershed, north of [[Lake Valandros]], drains the interior of the [[Northern Provinces]] and the western [[Sentinel Range|Sentinels]]. The [[Zarnato]] is the largest river in this system; just north of [[Lake Valandros]], it is joined by the meandering [[Snake River]], which flows east of [[Voltara]] and forms the second of the two major parts of the watershed. The major tributaries of the [[Zarnato]] include the [[Barzhen]], draining [[Blackwater Fens]], and the [[Arqa]], from the [[Sentinel Range|Sentinels]]; the major tributaries of the [[Snake River]] include the [[Wild River]], which cuts across the plains northeast of [[Voltara]], and [[Kelvaros]], which joins the [[Snake River]] close to its confluence with the [[Zarnato]]. %%NOTE: a lot of names still uncertain; look for status/namecheck as needed. The Erbalta Plains is pretty arid and likely only minor additional unmapped rivers; however there are likely numerous unmapped rivers flowing out of the Sentinels and joining the [[Zarnato]]. %%

%%^Campaign:None%%
### Places in Chasa-Nahadi Watershed
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.typeOf == "river" || f.typeOf == "waterway" || f.typeOf == "lake"))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%
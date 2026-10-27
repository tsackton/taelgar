---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: watershed
name: Chasa-Nahadi Watershed
whereabouts: Taelgar
dm_owner: tim
dm_notes: none
POV: modern
---
```taelgar-header
```

The Chasa-Nahadi watershed is a vast river system that drains the interior basin of the western [[Sentinel Range|Sentinels]]. Geographically, this watershed is composed of three distinct areas:

- The [[Chasa River Valley]], consisting of the [[Chasa]] and its tributaries. The [[Chasa]] flows west from the southern reaches of the [[Central Highlands]], passing through vast forests before it is joined by the [[Nahadi]] just east of [[Chardon]]. Numerous tributaries join the [[Chasa]], largely small forest rivers (exemplified by the [[Kayan]]). %%NOTE: most tributaries are unnamed so far; the Chasa arises from the confluence of two of these unnamed rivers northeast of [[Arendum]]. Canonically, the [[Chasa]] retains its name after the [[Nahadi]] joins, so the river that flows past [[Chardon]] is the [[Chasa]]. %%

- The [[Nahadi]] and [[Lake Valandros]] form a distinct region of the watershed, dominated by the vast size of [[Lake Valandros]]. The [[Nahadi]] is the only outflow from [[Lake Valandros]], and is a wide, broad river for its entire length. Numerous smaller tributaries flow into [[Lake Valandros]]. %%NOTE: no tributaries are mapped or named, really, but presumably there are rivers that flow into the lake from the west and east. [[Lake Valandros]] is roughly the size of Lake Michigan for context. %%

- The [[Zarnato]] watershed, north of [[Lake Valandros]], drains the interior of the [[Northern Provinces]] and the western [[Sentinel Range|Sentinels]]. The [[Zarnato]] is the largest river in this system; just north of [[Lake Valandros]], it is joined by the meandering [[Snake River]], which flows east of [[Voltara]] and forms the second of the two major parts of the watershed. The major tributaries of the [[Zarnato]] include the [[Barzhen]], draining [[Blackwater Fens]], and the [[Arqa]], from the [[Sentinel Range|Sentinels]]; the major tributaries of the [[Snake River]] include the [[Wild River]], which cuts across the plains northeast of [[Voltara]], and [[Kelvaros]], which joins the [[Snake River]] close to its confluence with the [[Zarnato]]. %%NOTE: a lot of names still uncertain; look for status/namecheck as needed. The Erbalta Plains is pretty arid and likely only minor additional unmapped rivers; however there are likely numerous unmapped rivers flowing out of the Sentinels and joining the [[Zarnato]]. %%

%%^Campaign:none%%
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

%%^Metadata:names:v1%%
- {name: "Chasa-Nahadi Watershed", language: "unknown", pronunciation: "CHA-sa nah-HAH-dee WAW-ter-shed", status: "proposed", notes: "The Chasa and Nahadi components follow the accepted pronunciations in [[Chasa]] and [[Nahadi]]; Watershed uses ordinary English. The complete compound pronunciation is proposed; its single source language is not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the article describes the drainage system in its current-era geographic reference role, with no narrower speaking position required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving parsed values and headerVersion.
- Added the explicit subject name already supplied by the filename and article.
- Recorded a broadly modern geographic POV and a persistent temporal-coverage note.
- Corrected "retains is name" to "retains its name" without changing meaning.
- Converted the legacy Campaign:None sentinel to the equivalent canonical Campaign:none form.
- Added persistent name metadata, preserving accepted pronunciations and documenting proposal provenance where needed.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** [[Chasa]] documents CHA-sa and [[Nahadi]] documents nah-HAH-dee; the proposal combines those recorded components with ordinary English Watershed. Confirm the complete compound before adding it to frontmatter. Candidate if accepted: set frontmatter `pronunciation: CHA-sa nah-HAH-dee WAW-ter-shed` and the matching persistent entry pronunciation to `CHA-sa nah-HAH-dee WAW-ter-shed` with `status: documented`; otherwise correct the durable proposal and its derivation together.
%%^End%%

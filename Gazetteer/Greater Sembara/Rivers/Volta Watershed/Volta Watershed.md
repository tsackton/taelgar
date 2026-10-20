---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: watershed
name: Volta Watershed
whereabouts:
  - {type: home, location: Greater Sembara, linkText: in}
dm_owner: none
dm_notes: none
POV: modern
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

%%^Metadata:names:v1%%
- {name: "Volta Watershed", language: "unknown", pronunciation: "VOHL-tah WAW-ter-shed", status: "proposed", notes: "Northern regional Sembaran naming guidance uses an English analogue: initial stress and long o in Volta, ordinary English Watershed. The name language and exact in-world pronunciation are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the article describes the drainage system in its current-era geographic reference role, with no narrower speaking position required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving parsed values and headerVersion.
- Recorded a broadly modern geographic POV and a persistent temporal-coverage note.
- Added persistent name metadata, preserving accepted pronunciations and documenting proposal provenance where needed.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The northern Sembaran English analogue supports initial stress and long o in Volta; Watershed uses ordinary English. The source language and exact in-world phonology remain unknown. Candidate if accepted: set frontmatter `pronunciation: VOHL-tah WAW-ter-shed` and the matching persistent entry pronunciation to `VOHL-tah WAW-ter-shed` with `status: documented`; otherwise correct the durable proposal and its derivation together.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T23:55:52-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: topographical feature
typeOfAlias: peninsula
name: Mawakel Peninsula
whereabouts: Northwest Coast
dm_owner: none
dm_notes: color
POV: modern
---
# The Mawakel Peninsula
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`


The Mawakel Peninsula is a land of contrasts and challenge. The peninsula is cut off from the mainland by steep, rocky mountains, making coastal travel the primary means of access. The center of the peninsula is dominated by the swift-flowing [[Sulqat]] river. Little of the river is navigable by ship, but the salmon run on the [[Sulqat]] is a major source of food and wealth for the Mawar and most of the inland settlements on the peninsula are on this river. 

The [[Sulqat]] river valley in the center of the peninsula is separated from the coasts by steep hills dominated by dense, old growth pine forests. The coasts themselves are rocky and dominated by steep cliffs and narrow inlets. 

The western and northern sides of the peninsula tend towards milder climates, with less snow in the winter, while the interior and eastern sides are colder and often receive heavy snowfall, especially towards the higher elevations near the mountains.

%%^Campaign:none%%
### Cities in Mawakel Peninsula
```dataviewjs
const { util } = customJS
dv.table(["Place", "Region", "Type Of", "Population"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter) && (f.file.frontmatter.typeOf == "city" || f.file.frontmatter.typeOf == "village" || f.file.frontmatter.typeOf == "town" || f.file.frontmatter.typeOf == "hamlet"))
				.sort(f => util.s("<home:1>", f.file))
				.map(b => [util.s("<name>", b.file), util.s("<home:1>", b.file), util.s("<maintype>", b.file), util.s("<population>", b.file)]))
```

%%^End%%

%%^Metadata:names:v1%%
- {name: Mawakel Peninsula, language: Mawaran, pronunciation: mah-WAH-kehl, notes: Proposed from Mawaran's Arabic analogue with consonantal w and middle-syllable stress; exact in-world phonology is not documented, status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the article describes durable geography and climate without a narrower historical state.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, corrected an objective grammar error, canonicalized the `Campaign:none` sentinel, and added supported name and temporal POV metadata.

### Validated judgments
- Confirmed local-only matches support the existing positive `dm_notes` attestation; private contents are not reproduced here.
- The `Campaign:none` block is an internal Dataview utility and contains no public lore to adopt.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The Mawaran entry retains the proposed pronunciation `mah-WAH-kehl`, derived from Mawaran's documented Arabic analogue with consonantal `w` and middle-syllable stress; exact in-world phonology is not documented. Accept it by copying `pronunciation: mah-WAH-kehl` to frontmatter and changing the entry to `status: documented`, or replace it with a sourced pronunciation.

### DM evidence
- [[_DM_/_Mawar Confederacy/Ep 3/Mawar Ep 3 - DM Notes]]
- [[_DM_/_Mawar Confederacy/Ep 5 - Lost Legacy/Mawar Religion]]
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T16:50:31-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [place, status/check/name, status/check/lint]
typeOf: region
name: Coastlands
whereabouts:
  - {type: home, location: Chardonian Empire}
dm_owner: none
dm_notes: none
POV: modern
---
# The Coastlands
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Coastlands is the colloquial name for the coastal region of the Chardonian Empire, stretching from the borders of [[Portalia]] in the south to the [[Mawar Mountains]] in the north, and bounded inland by the [[Beacon Hills]] and the [[Chardon Hills]]. 

The Low Coast, the portion of coastlands south of [[Chardon]], is hot and dry in the summer, with mild winters and extensive coastal wetlands. 

The Upper Coast, the portion of the coastlands north of [[Chardon]], is rich agricultural land, with many rivers and mild weather, sandy beaches and small stands of ancestral forests among fields of wheat. The land here slopes gently up to the [[Beacon Hills]]. 

Much of the Upper Coast was occupied by [[Hobgoblins|hobgoblins]] during the [[Blood Years]]. 

Five major rivers, and several smaller ones, flow through the coastlands. From south to north, they are:
- [[Dashun]]
- [[Zar]]
- [[Corvessa]]
- [[Sevros]]
- [[Breakrock]]

## Places in the Coastlands
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```


%%^Campaign:none%%

See: [[Hobgoblin Movements After Cha'Mutte]] and [[West Coast History Framework]] for historical context. 

Sandy beaches, leading to land of rivers and farms and pastures, breadbasket of Chardon (Upper Coast)
Geography of Low Coast less developed. 

Relatively few big cities? perhaps one or two in the north? Not sure yet about urbanization in this area. Open to develop. 

Generally part of the "core" of the Chardonian Empire and generally Chardonian rule is popular here. 

%%^End%%

%%^Metadata:names:v1%%
- {name: "Coastlands", role: "primary", language: "Common", notes: "The existing status/check/name indicates that the name remains under human review.", status: "unresolved"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern regional geography, climate, and settlement; the Blood Years occupation is historical background rather than a boundary on the current landscape.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- None.

### Validated judgments
- Newer source candidates corroborate the boundaries, agriculture, drainage, and imperial framing already represented in the article; no later material change was identified.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent `Coastlands` name entry remains `status: unresolved`, matching the existing `status/check/name`. Review its recorded Common-language classification and naming status, then accept the entry or correct it.
- [ ] **Suggestion — editorial.public_material_candidate:** The `Campaign:none` block contains a coherent public-safe claim about the region's place in the empire alongside source pointers, duplicated geography, and unresolved planning. Candidate: `The Coastlands are part of the core of the Chardonian Empire, where Chardonian rule is generally popular.` If adopted, retain the source pointers and unsettled Low Coast and urbanization questions privately, and remove only hidden text that duplicates the visible article.
%%^End%%

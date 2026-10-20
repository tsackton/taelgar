---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
ancestry: lizardfolk
population: 62
name: Ganboa
pronunciation: Gan-bo-a
whereabouts: Barony of Aveil
dm_owner: none
dm_notes: none
POV: modern
---
# Ganboa
*(Gan-bo-a)*
>[!info]+ Information  
> pop. 62  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small lizardfolk village a few miles downstream on the Enst, known in [[Cleenseau Region]] as a good source of healing herbs. Several lizardfolk from Ganboa are regulars at the markets in [[Cleenseau]] and [[Beury]].  Ganboa is built on a cul-de-sac in the [[Enst]] where the banks become very marshy and the river splits and a northerly channel meanders through several large marshy flats. It is a small village of only about two dozen huts, about half scattered across the semi-permanent marsh islands, and the other half along the banks of the river.

A small community of fisherfolk in [[Asineau]] has been known to grumble about lizardfolk getting preferential fishing rights when times are lean, but relationships with the humans in the region are usually quite good. Despite good relationships, the lizardfolk of Ganboa tend to mostly keep to themselves.
### Notable Residents

* [[Erdu]], the spokesperson
* [[Unai]], a noted herbalist and healer, chiefly responsible for Ganboa's reputation

%%^Campaign:None%%
### People in, or based in Ganboa
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name":"Ganboa","language":"unknown","pronunciation":"Gan-bo-a","status":"documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; describes the village and its usual regional relations, without dating individual residents or claiming continuous coverage of their lives.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting; recorded the existing pronunciation in primary name metadata, and added a typed settlement map entry and modern temporal metadata.
- Corrected “about a two dozen,” “relationships … as usually,” and the missing “for” after “responsible.”

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The settlement’s `Metadata:map:v1` entry has a blank `locator`; the consulted sources do not establish its world-map hex. Supply the verified coordinate as a string in `  - {map: world, locator: "<verified world hex>"}`. Do not infer the position from a nearby river, settlement, or regional map.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated People section opens with the legacy `%%^Campaign:None%%`. [[Campaign Registry]] specifies `%%^Campaign:none%%`. Review the existing block’s intended filtering and replace only the opener with that canonical sentinel; preserve its query and closing marker. The block has been left unchanged for this visibility-sensitive decision.
%%^End%%

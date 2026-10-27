---
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: fishing village
population: 102
name: Auloutte
pronunciation: OO-loot
whereabouts: Manor of Cleenseau
dm_owner: mike
dm_notes: none
POV: modern
---
```taelgar-header
```

A poor fishing village on the banks of the [[Enst]], a short walk from [[Cleenseau]]. It is nestled on reclaimed marsh between the [[Great South Road]], [[Amance Brook]], and the [[Enst]]. About a mile downriver from Cleenseau, just before the road crosses the Amance, it is part of the [[Manor of Cleenseau]]. About a dozen boats fish for river trout in the spring and summer, from a makeshift dock rebuilt each April. The twenty houses here flood at times, save for the sturdy mill, built on the banks of the [[Amance Brook]], and the small temple of the Warlord built next to the mill. 

### Notable Residents
* [[Gideon Thorne]], a prominent fisherman and part-time steward of the small temple
* Lucien, a skilled fisherman, quite knowledgeable about the river currents
* Marguerite, the toll collector and miller

%%^Campaign:None%%
### People in, or based in Auloutte
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name":"Auloutte","language":"unknown","pronunciation":"OO-loot","status":"documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; describes the village, seasonal fishing, and recurring floods rather than a dated snapshot.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting; recorded the existing pronunciation in primary name metadata, and added a typed settlement map entry and modern temporal metadata.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The settlement’s `Metadata:map:v1` entry has a blank `locator`; the consulted sources do not establish its world-map hex. Supply the verified coordinate as a string in `  - {map: world, locator: "<verified world hex>"}`. Do not infer the position from a nearby river, settlement, or regional map.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated People section opens with the legacy `%%^Campaign:None%%`. [[Campaign Registry]] specifies `%%^Campaign:none%%`. Review the existing block’s intended filtering and replace only the opener with that canonical sentinel; preserve its query and closing marker. The block has been left unchanged for this visibility-sensitive decision.
%%^End%%

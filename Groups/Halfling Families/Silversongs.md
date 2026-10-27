---
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group, status/check/lint]
typeOf: family
ancestry: halfling
name: Silversongs
affiliations:
  - {place: Emerald Song, type: leader, title: Owners}
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

A halfling family of traders and sailors based in the [[Nevos Sea]]. 

%% From OneNote
The Silversongs have been sailing the trade routes between Chardon and the Nevos Sea for the past three generations, about 120 years. The clan itself is large and scattered, with at least four Silversong ships plying the Chardon->Dunmar trade, and two more sailing the coastal routes north of Chardon. This particular branch of the family has focused on fast coastal trade.
%%

%%^Campaign:none%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Silversongs", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern family identity and Nevos Sea trade; the older hidden fleet history has no precise in-world date.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Recorded the primary name and supported temporal viewpoint with persistent name and temporal metadata.
- Normalized frontmatter field order and collection formatting.
- Canonicalized Campaign:None to the equivalent Campaign:none sentinel.

### Validated judgments
- The compact family entry and ship affiliation already perform a bounded reference role; the hidden paragraph is an adoption decision, not an automatic source of canon.

### Open findings

- [ ] **Suggestion — editorial.public_material_candidate:** The “From OneNote” comment contains a coherent fleet and trade-history account beyond the visible Nevos Sea label. Confirm its undated quantities and adopt a concise version if still intended. Candidate: “The Silversongs have sailed the routes between [[Chardon]] and the [[Nevos Sea]] for three generations, about 120 years. Their scattered fleet includes at least four ships trading between Chardon and [[Dunmar]], and two on the coastal routes north of Chardon. The branch aboard the [[Emerald Song]] specializes in fast coastal trade.” The ownership and fast-trade specialization are independently supported by [[Emerald Song]]; the fleet counts and duration remain proposed from the shared comment. Retain the OneNote provenance as a short source comment after adoption.
%%^End%%

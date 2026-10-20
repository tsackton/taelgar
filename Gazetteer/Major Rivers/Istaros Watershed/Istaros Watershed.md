---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: watershed
name: Istaros Watershed
whereabouts:
  - {type: home, location: Taelgar, linkText: in}
dm_owner: none
dm_notes: none
POV: modern
---
# The Istaros Watershed
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Istaros watershed is the vast river basin that gathers into the [[Istaros]] and its many tributaries, stretching from the [[Mostreve Hills]] to the [[Sea of Storms]]. For much of recorded history it has been a fertile crossroads, central first to the vast elven realm of [[Alcarinque|Alcarinquë]], then to the [[Drankorian Empire]]; even after the [[Fall of Drankor]] the upper Istaros served as a crucial connection between [[Cymea]] and the [[Green Sea]], the [[Istabor Alliance]], and the [[Dunmar|Dunmari]].

Since the [[Great War]], much of the watershed has been defined by the scars and magical curses of [[Cha'mutte]]. The upper Istaros flows through the [[Plaguelands]], where the ruined city of [[Isingue]] lies near one of the watershed’s most storied confluences; beyond, it passes into the [[Desolation of Cha'mutte]] around the ruined city of [[Drankor]]. 


%%^Campaign:none%%
### Places in the Istaros Watershed
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
- {"name":"Istaros Watershed","language":"unknown","status":"proposed","pronunciation":"ISS-tah-rohs WAW-ter-shed","notes":"Complete-form proposal combining the accepted Istaros pronunciation in [[Istaros]] with the ordinary English word watershed. Exact pronunciation of the complete name is not independently recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern, after the Great War; selected older realms provide historical context without narrowing the present geographic frame.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Removed trailing horizontal whitespace on changed prose or the former end-of-file boundary.
- Normalized frontmatter and recorded explicit identity where previously supplied by the filename.
- Corrected the objective grammar error in “central first to vast elven realm”.
- Normalized the legacy capitalization of the reserved Campaign:none sentinel.
- Added persistent name metadata, preserving accepted pronunciations and keeping unaccepted readings proposed.
- Recorded POV: modern and concise temporal coverage in persistent metadata.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or correct `ISS-tah-rohs WAW-ter-shed` for Istaros Watershed. Complete-form proposal combining the accepted Istaros pronunciation in [[Istaros]] with the ordinary English word watershed. Exact pronunciation of the complete name is not independently recorded. If accepted, mark this name entry `documented` and copy the accepted primary pronunciation into frontmatter; otherwise replace it with the intended pronunciation while preserving established name context.
%%^End%%

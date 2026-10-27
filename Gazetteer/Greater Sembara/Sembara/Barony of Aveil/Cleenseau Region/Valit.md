---
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
population: 249
name: Valit
pronunciation: Val-le
whereabouts: Manor of Valit
dm_owner: mike
dm_notes: important
POV: 1720
---
```taelgar-header
```

A small village overseen by the castellan of the [[Manor of Valit]] of about 50 houses scattered a little more widely than most of the other villages in the region. There are no walls, although the manor complex is walled and fortified and can shelter the population of the village in times of need. The most notable features of the village are the wooden bridge over the [[Amance Brook]], and the three mills built along the brook, as well as the large two-story wooden manor with several outbuildings, rebuilt about 30 years ago after a fire. The manor complex includes a land registry, a temple to the Wildling, a stable, and a blacksmith. Just under the eaves of the [[Cleenseau Wood]], is another small ancient shrine to the Wildling, said to date back
### Notable People
* [[Alix Degwyn]], installed as castellan of the [[Manor of Valit]] on June 12, 1720
* [[Sabine de Brune]], the former castellan and magistrate, who vanished in early 1720
* [[Warin the Woodsman|Warin]], her master of the guard and woodsman
* [[Giselle]], Sabine's secretary and keeper of the baronial land registry
* Henri, Odette, and Reynard, the three millers
* Julien Leclair, the steward to the temples, and his wife, a skilled carpenter

%%^Campaign:None%%
### People in, or based in Valit
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Valit", "language": "unknown", "pronunciation": "Val-le", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 village snapshot after Alix Degwyn’s June 12 installation; the current offices and the manor’s relative rebuilding age are read from that point, while earlier history is selective.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported name and/or map metadata where absent and a temporal viewpoint with coverage guidance; normalized frontmatter where needed.
- Corrected “There is no walls” to “There are no walls” (objective grammar).
- Corrected “a stable, and blacksmith.” to “a stable, and a blacksmith.” (objective grammar).

### Validated judgments
- The DR 1720 POV follows Alix Degwyn’s recorded installation; the existing DM owner and attestation are preserved, with local attestation review not applicable to this owner.

### Open findings

- [ ] **Warning — editorial.prose_clarity:** The first paragraph ends “Just under the eaves of the [[Cleenseau Wood]], is another small ancient shrine to the Wildling, said to date back” with no date or completed claim. Complete it from established evidence, or use the bounded candidate “Just under the eaves of the [[Cleenseau Wood]] is another small ancient shrine to the Wildling.” This preserves the shrine without inventing an age.
- [ ] **Warning — correctness.cross_note_conflict:** The village describes “the three mills” beside the brook, whereas [[Manor of Valit#Economy]] names a small papermill and “three other mills” grinding grain; that same source’s opening also says three mills. Confirm whether the papermill is included in the three or is a fourth mill before changing either account. Nearby review-comment candidate: `%% Mill count unresolved: [[Valit]] and the opening of [[Manor of Valit]] say three mills; [[Manor of Valit#Economy]] describes a papermill plus three other grain mills. Confirm whether these describe the same set. %%`
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The existing `%%^Campaign:None%%` marker is a noncanonical spelling. Proposed marker: `%%^Campaign:none%%`, with its existing body and end marker preserved exactly. Apply only after human approval or proof of equivalent filtered visibility; this lint preserves the original sentinel.
- [ ] **Warning — metadata.map_location_missing:** The settlement map entry has a blank locator. Supply `locations: [{map: world, locator: <confirmed locator>}]` from an established map position.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: realm
typeOfAlias: manor
created: 1490
name: Manor of Valit
whereabouts: Barony of Aveil
dm_owner: mike
dm_notes: none
POV: modern
---

# The Manor of Valit
>[!info]+ Information
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Manor of Valit is part of the demesne of the Baron of Aveil and has been in baronial hands for many years.  It is mostly known for two things: its three mills, and as the main place for baronial land records in the [[Cleenseau Region]]. Although the manor itself is relatively large, [[Amance Brook]] runs through the middle of the manor, and much of the land to the east of the brook is hilly and hard to farm (and hard to get to from the village over the one small wooden bridge in [[Valit]]).

There is a small farmstead on the east side of the brook, near the woodlot that separates [[Valit]] from [[Asineau]], which is home to a dozen people, and has recently grown to two sturdy wooden farmhouses and a couple of barns. The rest of the population of the manor lives in the village of [[Valit]]. The manor is relatively poor, as much of the land is held freehold, especially on the eastern side of the brook. There are three mills along the [[Amance Brook]], all of which are controlled by the manor, which provide the majority of the manorial income.
### Economy
Valit has a small section of good soils (on the west side of [[Amance Brook]]) and substantial farmland that is a bit rocky or hilly and is farmed more in scraps and pieces, intermixed with berry bushes and small stands of fruit and nut trees. There is more millet grown here than in [[Beury]], but wheat and barley are also grown. There are few cattle and sheep, but a substantial number of pigs who forage in the eaves of the woods. There is a significant charcoal industry here, and wood is plentiful. There are bees kept here, although mostly for local consumption. Fruit and nut trees are plentiful, and in the fall game is fairly easy to find. Valit derives income from the baronial land registry in town, which draws travelers and supports the work of a scribe and a small papermill along the brook, from which paper is exported to the local region. There are also three other mills along the river that grind grain for Cleenseau and Tavoise. 

Valit does not have a proper market, although buyers often come to the paper mill. Charcoal, paper, pork, fruit, nuts, timber, and game are often sold in Beury or Cleenseau, and the millers take many clients from Cleenseau, as does the scribe. 


%%^Metadata:names:v1%%
- {"name": "Manor of Valit", "language": "unknown", "pronunciation": "MAN-er uhv VAL-lee", "status": "proposed", "notes": "[[Valit]] explicitly records Val-le for the place-name component. MAN-er uhv VAL-lee is an assembled full-form proposal: ordinary English Manor of plus that recorded component, rendered VAL-lee. No reviewed source explicitly records or accepts the complete form. The name’s source language is not established; human acceptance is required before marking the complete entry documented or adding its pronunciation to frontmatter."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern landholding, settlement, and economy; the relative phrase recently grown does not establish an exact expansion date.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing parsed values.
- Added an explicit `name` matching the existing subject and filename.
- Recorded `POV` and a persistent temporal-coverage note.
- Corrected objective spelling, punctuation, duplication, or grammar in the declared passages; lore and visibility are preserved.
- Added a proposed full-name pronunciation using the recorded Valit component and ordinary English words; recorded its derivation and need for human acceptance.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry proposes `MAN-er uhv VAL-lee`. [[Valit]] records only the component `Val-le`; `Manor of` uses ordinary English pronunciation, and the assembled complete form is not explicitly recorded in the reviewed evidence. Confirm or revise this full-form proposal. If accepted, copy it to frontmatter `pronunciation` and set the entry to `status: documented`; retain `language: unknown` until the name’s source language is established.
- [ ] **Warning — content.internal_conflict:** The overview twice gives three mills, but Economy describes a paper mill and then “three other mills,” implying four. [[Valit]] also describes three mills. Confirm whether the paper mill is included in the three. If it is, use: `One of the manor’s three mills makes paper; the others grind grain for Cleenseau and Taviose.` If there are four, revise both overview counts instead; do not silently change the economy.
- [ ] **Suggestion — identity.name_mismatch:** Economy names `Tavoise`, while the nearby settlement’s canonical filename, name, and article are [[Taviose]]. Confirm the intended client settlement, then replace `Tavoise` with `[[Taviose]]` if that is the intended referent. Name corrections are preserved as human choices rather than applied as light prose edits.
%%^End%%

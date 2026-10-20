---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [status/cleanup/text, place, status/check/lint]
typeOf: settlement
typeOfAlias: logging village
population: 237
name: Ashcombe
whereabouts: Barony of Aveil
dm_owner: mike
dm_notes: important
POV: 1720s
---
# Ashcombe
>[!info]+ Information  
> pop. 237  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% 
The small village of Ashcombe is up in the Maudor Hills and is the heart of fey hunter plot line:
[[The Hunter]]:
* he's been hunting messengers with his packs of harpies
* created a base of sorts in the hills somewhere
* people in Ashcombe have gone missing, in particular William Forester's husband, who is the steward of the forest and the chief lumber-guy
%%

%%^Metadata:names:v1%%
- {"name": "Ashcombe", "language": "unknown", "pronunciation": "ASH-kuhm", "status": "proposed", "notes": "The English component ash and the English place-name ending combe support ASH-kuhm, with sh, a reduced final vowel, and silent final e, under the Sembaran English analogue in [[Languages]]. The source language is not explicitly recorded. Exact in-world pronunciation remains unconfirmed."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the hidden working account belongs to the Cleenseau campaign around DR 1720; the visible page has no authored reference account, and later village history is not represented.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing parsed values.
- Added an explicit `name` matching the existing subject and filename.
- Recorded `POV` and a persistent temporal-coverage note.
- Added a persistent primary name entry with a proposed pronunciation and its derivation; accepted frontmatter pronunciation is unchanged.
- Added the required typed map block, leaving its unsupported locator blank for human completion.

### Validated judgments
- `status/cleanup/text` is supported: the note consists of hidden working preparation and lacks a visible settlement account.

### Editorial assessment
**Underdeveloped** — The page has no visible reference account of the logging village, its local leadership, or the displacement and rebuilding that define its established DR 1720 history. A short sourced settlement paragraph is the smallest useful repair; its hidden encounter preparation cannot substitute for that account.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** All substantive authored text is hidden. [[cleenseau-016-session-recap]] identifies the logging village and its evacuation, [[Ameline Evynwood]] identifies its lady and the villagers’ later return, and [[Alban of Ashcombe]] establishes its temple. Proposed visible account: `Ashcombe is a logging village in the [[Barony of Aveil]], ruled by Lady [[Ameline Evynwood]], with a temple to [[The Wildling]]. Fey attacks drove its people to [[Aslain]] in February DR 1720. After the [[Crisis of Malach]], the villagers returned and began rebuilding.` Keep the detailed hunting plot and uncertain disappearances in private guidance; do not turn the entry into a party itinerary.
- [ ] **Warning — metadata.names_unresolved_status:** The persistent primary entry proposes `ASH-kuhm`. The English component ash and the English place-name ending combe support ASH-kuhm, with sh, a reduced final vowel, and silent final e, under the Sembaran English analogue in [[Languages]]. The source language is not explicitly recorded. This is an analogue-informed proposal, not established in-world phonology. Accept or revise it; if accepted, copy the complete pronunciation to frontmatter and set the entry to `status: documented`.
- [ ] **Warning — metadata.map_location_missing:** The required `Metadata:map:v1` block has a blank `locator`. No supported position was found in the reviewed sources. Supply the settlement’s world-map locator in `locations: [{map: world, locator: <verified locator>}]`; do not infer a coordinate from prose distances.
%%^End%%

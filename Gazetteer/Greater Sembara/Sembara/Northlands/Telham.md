---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
campaignInfo: null
population: 12000
name: Telham
whereabouts: Duchy of Telham
dm_owner: none
dm_notes: none
POV: modern
---
# Telham
>[!info]+ Information  
> pop. 12,000  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A large coastal trading city and the most important maritime city in Sembara.

%% No specific details exist in my head; but the vibe is probably something like Rotterdam to Tollen-as-Amsterdam or similar; a similar in some ways but less important %%

%%^Metadata:names:v1%%
- {"name": "Telham", "language": "unknown", "pronunciation": "TEL-um", "status": "proposed", "notes": "Proposed from the northern English analogue for Sembaran in [[Languages]]: first-syllable stress, short e, and a reduced English place-name ending ham with an unsounded h. A literal TEL-ham remains possible; the name language and local reading are unconfirmed."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern coastal-city description, with no narrower date established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added supported persistent name and temporal-viewpoint metadata.
- Added the required settlement map skeleton, leaving its unknown locator blank.

### Validated judgments
- The Rotterdam/Amsterdam analogy is explicitly a speculative vibe and supplies no adopted city facts. It remains private.

### Editorial assessment
**Underdeveloped**. The article calls Telham Sembara’s most important maritime city but gives no setting-specific account of that maritime role. The central missing dimension is its port geography and shipbuilding function, described in [[Northlands]] but absent here. The smallest useful scope is one short sourced port paragraph, with the source’s review caveats resolved; no generic city checklist or invented political history is required.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has its typed single-location entry, but its `locator` is blank. Supply the verified world-map coordinate in that existing entry; the reviewed text and prepared evidence do not establish a coordinate, so none has been guessed.

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `TEL-um`. The northern English analogue for Sembaran in [[Languages]] supports first-syllable stress, short e, and a reduced place-name ending ham with an unsounded h. A literal TEL-ham remains possible; the name language is unconfirmed. Confirm or replace the proposal; if accepted, copy the complete pronunciation to frontmatter and mark the existing entry `documented`.

- [ ] **Warning — coverage.established_fact_missing:** [[Northlands]] places Telham at the head of a small bay and describes shipyards supplying halfling traders and the small Sembaran navy. These concrete facts would explain the central maritime importance that this article currently only asserts. Candidate: “Telham lies at the head of a small bay. Its shipyards build vessels for [[Halflings|halfling]] traders crossing the [[Green Sea]] and for Sembara’s small navy.” Northlands carries `status/gameupdate/clee` and `status/check/mike`, so confirm that its port description remains current before adoption. This is the identified central coverage gap; no duplicate invention-based underdevelopment finding is added.
%%^End%%

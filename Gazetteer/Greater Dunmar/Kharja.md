---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
subTypeOf: null
typeOfAlias: intermittent river
campaignInfo: []
name: Kharja
pronunciation: KHAAr-jaa
whereabouts: Istaros Watershed
dm_owner: tim
dm_notes: important
POV: modern
---
# Kharja
*(KHAAr-jaa)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The now mostly dry riverbed that flows past [[Kharsan]], eventually joining with the [[Hara]] river. 

%%SECRET[v2:e1bc298ce4b40c43c3ae18a559d59fe4]%%

%%^Metadata:names:v1%%
- {name: Kharja, language: unknown, pronunciation: KHAAr-jaa, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: , map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the largely dry Kharja riverbed; its present connection with the Hara remains unresolved.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting without changing existing values.
- Added a documented primary name entry preserving the accepted pronunciation; the name's language remains unknown.
- Added the required two-ended waterway map skeleton with unknown source and outlet locators blank.
- Added `POV: modern` and temporal guidance for the present-day riverbed description.

### Validated judgments
- Confirmed local DM evidence supports retaining the existing positive `dm_notes` attestation.
- Reviewed the local-only `SECRET` block; any recovery proposal remains in the private handoff.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** The visible description says the Kharja is “eventually joining with the [[Hara]] river,” but [[Hara#In Dunmari Culture]] says its route has not been traced through the Garamjala and that it is presumed no longer to meet the Hara; [[Garamjala Desert#River Systems]] likewise treats its stopping before the confluence as a suspicion. The historical confluence in [[Report of the Aagiri to Samraat Dasa]] does not establish the current course. Reconcile the present-day claim without turning uncertainty into certainty. Copy-ready candidate reflecting the public sources: “The Kharja is a mostly dry riverbed that passes [[Kharsan]]. It flows fitfully after rare storms and is presumed to stop before reaching the [[Hara]], though its route through the [[Garamjala Desert]] has not been fully traced.”
- [ ] **Warning — metadata.map_location_missing:** The required `Metadata:map:v1` block now has `source` and `outlet` entries, but both `locator` values remain blank. Supply verified positions for `source.locator` and `outlet.locator` on `map: world`; resolve the current-course question above before assigning an outlet from a historical confluence.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan History]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 20]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 24]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 25]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 42]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 118 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Desolation of Cha'mutte Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
campaignInfo: null
name: Yeraad
whereabouts: Chardonian Empire
dm_owner: tim
dm_notes: none
POV: 1740s
---
# Yeraad
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Yeraad is a wide, winding river that flows from its source in the [[Sentinel Range|Sentinels]], through the southern parts of the [[Elderwood]], and across the lowlands to the [[Emerald Bay]]. Its name derives from the old Northos name, meaning Green River. 

%% notes -
Yeraad is the name given it the river from the northern branch in the sentinels to the sea. Major tributaries includes the southern branch in the sentinels, the elderwood hills river, and several rivers that flow north or south into the lowlands from the north hills or south mountains
Generally a slow, winding river but carries a ton of water. Yeraad river valley is a flat, low basin surrounded by higher ground and there are plenty of small swamps and wet riparan forests
name from ancient Northros for "Green"
%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Sentinel Range, map: world, locator: }
  - {role: outlet, feature: Emerald Bay, map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: geographic reference
povNotes: "Accuracy range: approximately the DR 1740s. Geographic Reference for Yeraad; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.

### Open findings
- [ ] **Warning — pronunciation.missing_or_exception:** Semitic analogue documented for Northros: clear vowel sequence and stress on the long middle syllable. Copy-ready candidate for a Metadata:names:v1 block: `- {name: Yeraad, language: Northros, pronunciation: yeh-RAH-ahd, status: proposed}`. Accept it in frontmatter only after human review.
- [ ] **Warning — dm.notes_private_evidence_suspect:** Local-only evidence in [[Session 49]], [[Session 121 - DM Notes]], [[Chalyte Giants Brainstorming]], [[Chardon Brainstorming]], [[Chardon Timeline]], [[Session 124 - DM Notes]], [[Session 126 - Brainstorming]], [[Session 126 - DM Notes]], [[Session 98 - DM Notes]] is not accounted for by an in-note SECRET link. Review whether `dm_notes: none` remains accurate; do not remove or change the field automatically.
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks source.locator, outlet.locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
%%^End%%

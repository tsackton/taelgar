---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Zurrua
pronunciation: TSOO-roo-ah
whereabouts: Portalia
dm_owner: none
dm_notes: none
POV: 1740s
---
# Zurrua
*(TSOO-roo-ah)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% west of canal, unmapped, minor %%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: , map: world, locator: }
%%^End%%

%%^Metadata:article:v1%%
mode: geographic reference
povNotes: "Accuracy range: approximately the DR 1740s. Geographic Reference for Zurrua; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.
- Added or populated the required Metadata:map:v1 block.

### Open findings
- [ ] **Warning — metadata.map_location_missing:** The required map block still lacks source.locator, outlet.locator. Candidate: fill only the blank `locator` values in the existing Metadata:map:v1 block from the authoritative map; do not guess coordinates.
- [ ] **Warning — coverage.established_fact_missing:** Great Library Arc 5 establishes that the river passes Urkabi and was traveled downriver by the Silver Tempests in DR 1748, but the note has no visible article text. Candidate: add one sentence identifying the Zurrua as the river through Urkabi and noting the DR 1748 downstream journey only if campaign context is useful.
%%^End%%

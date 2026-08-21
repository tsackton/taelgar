---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T13:33:35-04:00"
lintVersion: "3.4"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Zar
pronunciation: ZAR
whereabouts: Coastlands
dm_owner: none
dm_notes: none
POV: modern
---
# Zar
*(ZAR)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

One of the major rivers of the [[Coastlands]], rising from the [[Beacon Hills]] and flowing west to the [[Endless Ocean]].

%%^Metadata:names:v1%%
- {name: Zar, role: primary, language: Northros, pronunciation: ZAR, meaning: boundary, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Beacon Hills, map: world, locator: "12.07.A23"}
  - {role: outlet, feature: Gulf of Chardon, map: world, locator: "12.06.I11"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the river's course from the Beacon Hills to the Endless Ocean is stable.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the accepted frontmatter pronunciation ZAR to the existing documented primary name entry without changing any populated documented value.

### Open findings

- [ ] **Warning — metadata.names_documented_conflict:** The documented name entry records language: Northros, while [[Languages]] defines Northros as a language family rather than a specific language. The linter must preserve the documented value. Candidate: identify the specific established Northros language for Zar and replace the family label by human decision; if no specific language is established, use language: unknown and separately verify whether the documented meaning boundary remains supported.

%%^End%%

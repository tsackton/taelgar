---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/ai, status/check/lint]
typeOf: road
typeOfAlias: street
name: Market Road
whereabouts: Cleenseau
POV: modern
---
# Market Road
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Market Road is a paved street in [[Cleenseau]], connecting the [[Market Gate (Cleenseau)|Market Gate]] to the [[North Gate of Cleenseau|North Gate]]. It separates the North Close from the [[Garrison Quarter]] and [[Underhill]].

%%^Metadata:names:v1%%
- {name: Market Road, language: Common, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {feature: Market Gate (Cleenseau), map: world, locator: }
  - {feature: North Gate of Cleenseau, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the subject in the current campaign era; the article does not require a narrower temporal reading position.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported name and/or map metadata where absent and a temporal viewpoint with coverage guidance; normalized frontmatter where needed.

### Validated judgments
- The complete name is plain English and needs no separate pronunciation guide; the pronunciation warning is contextually exempt.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Both road endpoint locators are blank. The text establishes [[Market Gate (Cleenseau)|Market Gate]] and [[North Gate of Cleenseau|North Gate]] as endpoints, which are recorded as features; supply their confirmed world-map locators rather than inferring positions from the town description.
%%^End%%

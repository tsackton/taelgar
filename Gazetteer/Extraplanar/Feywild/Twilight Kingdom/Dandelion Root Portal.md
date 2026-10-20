---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
displayDefaults: {wSecondary: "<typeof:Ua> <secondary:q>", wHome: "<typeof:Ua> <home:q>"}
tags: [place, status/check/lint]
typeOf: planar link
typeOfAlias: fey portal
name: Dandelion Root Portal
whereabouts:
  - {type: secondary, location: Dandelion House}
  - {type: home, location: Twilight Kingdom}
dm_owner: none
dm_notes: none
POV: 1740
---
# The Dandelion Root Portal
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[the-door-in-the-floor.jpg|right|400]]The Dandelion Root Portal is a fey crossing between the [[Material Plane]] and the [[Feywild]]. 

In the [[Twilight Kingdom]], a portal in a ruined manor leads to the ruins of [[Dandelion House]] in [[Varrow Forest]].

On the Material Plane, the crossing begins behind a hidden door in a root-covered subcellar beneath [[Dandelion House]]. Beyond the door, a narrow tunnel runs through the hollow center of a massive dry root, becoming bone-like before emerging through the ruined manor in the Twilight Kingdom.

%%^Metadata:names:v1%%
- {"name":"Dandelion Root Portal","language":"Common","status":"inferred","notes":"Plain Common descriptive place name, following the ordinary English place-name convention in [[Languages]]."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the passage is directly attested in DR 1740; its condition after Dandelion House's destruction is not established by the sources reviewed.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter; added a Common descriptive-name entry and a DR 1740 viewpoint with explicit uncertainty about later operation.

### Validated judgments
- [[Lost in the Feywild - Episode 01]] and [[Lost in the Feywild - Episode 02]] establish the subcellar, hollow root, and ruined Feywild counterpart in DR 1740. The descriptive English name needs no pronunciation.

### Open findings

- [ ] **Warning — coverage.later_material_change:** The article currently presents a usable crossing through the “ruins of Dandelion House.” [[Lost in the Feywild - Episode 01]] and [[Lost in the Feywild - Episode 02]] directly establish this route on October 5, DR 1740, while the Material Plane manor still stood. [[Dandelion House]] records its later destruction, dated October 7 in metadata, with an open distinction from the October 6 collapse of the [[27th House]] in [[Lost in the Feywild - Episode 07]]. None of these sources establishes that the root crossing remained passable afterward. Decide whether to update its later condition, defer that update with the appropriate game-update status, or intentionally retain a DR 1740 snapshot; do not infer either survival or closure. A bounded historical candidate is to add `## The crossing in DR 1740` before the two route paragraphs and replace the first of them with “In DR 1740, a portal in a ruined manor in the [[Twilight Kingdom]] led to [[Dandelion House]] in [[Varrow Forest]].” Add a nearby comment: `%% The route is directly observed in Episodes 01–02 before Dandelion House's destruction; its condition afterward is unestablished. %%` If a later destruction paragraph is adopted, isolate only that paragraph in a `Date:<confirmed destruction date>` block after resolving the date and counterpart distinction; no visibility change is applied here.
%%^End%%

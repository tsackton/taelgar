---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: ruined city
name: Drankor
pronunciation: DRAN-kor
whereabouts: "Desolation of Cha'mutte"
dm_owner: tim
dm_notes: important
POV: modern
---
# Drankor
*(DRAN-kor)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Drankor is a ruined city near the mouth of the [[Istaros]], once the heart of the [[Drankorian Empire]] and a great center of magic and learning. Devastated by the [[First Plague]] in DR 1059, its jungle-covered ruins lie within the [[Desolation of Cha'mutte]], haunted by undead and dangerous remnants of imperial magic.

%%^Metadata:names:v1%%
- {name: Drankor, role: primary, language: Drankorian, pronunciation: DRAN-kor, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of Drankor as a ruined city after the First Plague; it does not yet describe the outcome of the DR 1749 confrontation with Apollyon.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting and recorded `POV: modern` with persistent temporal coverage.
- Added the required single-location map skeleton; its world-map locator remains unknown.

### Validated judgments
- The documented Drankor name entry and accepted pronunciation are preserved.
- Confirmed matching local sources supporting the positive `dm_notes` attestation; no private contents were adopted.

### Editorial assessment
**Underdeveloped**. The city's location and destruction are clear, but the reference account lacks its surviving urban landmarks and the defining change to its principal long-lived threat in DR 1749. A short account linking the preserved sanctuary, university ruins and dock district, followed by the established outcome at Apollyon's prison, would fill these central gaps. These dimensions are already established; a full city gazetteer or invented reconstruction is unnecessary.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — metadata.map_location_missing:** Supply a verified world-map locator for the settlement in `Metadata:map:v1`; the reviewed prose and annotated city map do not establish a world hex. Keep `map: world` and replace the blank `locator` only with a verified coordinate.

- [ ] **Warning — coverage.established_fact_missing:** The visible paragraph gives no usable account of the surviving city beyond generic ruin and danger. [[Temple of the Eight Divines]], [[Imperial University]], [[Valtrius University]], [[University of the Blessed Waters]], and [[Session 114 (DuFr)]] establish its principal surviving landmarks. Add one bounded paragraph, for example: “The [[Temple of the Eight Divines]] remains a preserved sanctuary among the ruins. The city's three great universities—the [[Imperial University]], [[Valtrius University]], and the [[University of the Blessed Waters]]—survive as ruins, while the old dock district includes the ruined tavern [[The Laughing Wave]] and the Custom House.” This supplies setting-specific orientation without adopting the private encounter plans or treating historical map annotations as current observation.

- [ ] **Warning — coverage.later_material_change:** [[Session 117 (DuFr)]] records Apollyon's defeat in DR 1749 and the subsequent failure of his prison, a defining durable change absent from this city account. Choose whether to update the article, defer the update with the appropriate `status/gameupdate/dufr` disposition, or intentionally retain the earlier account. Candidate: “In DR 1749, the [[Dunmar Fellowship]] defeated [[Apollyon]] in [[Apollyon's Temple]]; his inner sanctum collapsed, and the prison around the temple failed several days later.” This does not imply that all undead, plague echoes or other hazards vanished. If earlier-date filtering is desired, the smallest proposed date layer is `%%^Date:1749-05-30%%` around that paragraph, followed by `%%^End%%`; it has not been applied.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Desolation of Cha'mutte Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Stormcaller Tower - DM Version]]
%%^End%%

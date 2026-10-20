---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
subTypeOf: null
typeOfAlias: trading city
ancestry: Urskan
campaignInfo: null
name: Zakat
pronunciation: zuh-KAHT
whereabouts:
  - {type: home, location: Ursk, startFilter: f}
dm_owner: tim
dm_notes: important
POV: modern
---
# Zakat
*(zuh-KAHT)*
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Zakat is a mysterious city on the north coast of the [[Green Sea]], and the westernmost of the handful of open ports where foreigners are allowed to trade in the country of [[Ursk]]. 

Zakat is a sprawling city with high walls and extensive coastal fortifications, including several massive stone wave breaks. The foreign trading port and related buildings are set on a protected spit of land, but exit from the docks and storehouses of the foreign city is forbidden and the whole area is patrolled by masked wizards. A great gate stands at the end of the peninsula, guarded constantly. 

The city is known for strange goods from the north, including furs, hide, and monster parts. Most prized of all is dragon hide, which is sold for exorbitant prices to foreign traders. It is a common stop for Tollender ships seeking magical ingredients for the famous Tollen dyes. 

%%SECRET[v2:ab7df98e62e50d5881146c2a6a3d9761]%%

%%^Metadata:names:v1%%
- {"name": "Zakat", "language": "unknown", "pronunciation": "zuh-KAHT", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the restricted foreign trading port and its trade; no narrower change in access or city state is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and retained its existing null fields.
- Added the accepted name entry, broadly modern temporal metadata, and the required settlement map skeleton.

### Validated judgments
- The visible article identifies the port’s location, controlled foreign access, fortifications, and defining trade; [[Ursk]] and [[Philosopher's Information Concerning Ursk]] corroborate its restricted-port role.
- Confirmed local source matches support the existing positive `dm_notes` attestation. The SECRET placeholder was reviewed and preserved.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The settlement map block has an empty `locator`. Supply Zakat’s confirmed world-map grid coordinate in `- {map: world, locator: <confirmed coordinate>}`; the reviewed sources do not establish that grid value, and illustrative trade-map reference points are not adopted harbor coordinates.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 93 - DM Notes]]
%%^End%%

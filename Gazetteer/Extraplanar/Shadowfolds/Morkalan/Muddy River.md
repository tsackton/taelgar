---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Muddy River
whereabouts: Morkalan
dm_owner: none
dm_notes: none
POV: modern
---
# The Muddy River
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A bleak, slow-flowing river in [[Morkalan]], a shadowy echo of the northern part of the [[Hara]].

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: , map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Muddy River", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern before the destruction of Morkalan in DR 1748; the brief river description preserves that earlier setting and does not establish a surviving river afterward.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added the explicit primary name.
- Added primary-name metadata with unknown language; the ordinary English name needs no pronunciation guide.
- Added a broadly modern pre-destruction temporal interpretation and the required waterway map skeleton, with unknown locators left blank.

### Validated judgments
- The short physical description performs the role of a minor landmark entry. The separate [[Muddy River (Tollen)]] is a different river; bare [[Muddy River]] links resolve the unique filename of this subject.
- [[Morkalan]], [[Bleakhold]], [[Session 56 (DuFr)]] and [[Session 58 (DuFr)]] distinguish the earlier landscape from the domain’s later destruction; no surviving post-destruction river is established.

### Open findings

- [ ] **Warning — coverage.later_material_change:** [[Morkalan]] records the domain's destruction in August DR 1748, and [[Session 58 (DuFr)]] records its shadows dissolving and its inhabitants returning to Dunmar. The current river entry gives only an unqualified description within that domain. Choose to update its temporal account, defer with an appropriate game-update tag, or explicitly preserve the pre-destruction snapshot. A bounded retrospective candidate is: ‘The Muddy River was a bleak, slow-flowing river in [[Morkalan]]. The domain was destroyed in August DR 1748.’ Do not infer that the river independently survived or assign it a separate exact destruction date. The viewpoint note preserves the earlier frame while this human choice remains open.

- [ ] **Warning — correctness.source_uncertainty:** The final phrase calls the river ‘a shadowy echo of the northern part of the Hara’ as a fact, while [[Morkalan]] explicitly says the connection is presumed; [[Session 56 (DuFr)]] likewise describes only a seemingly distorted echo of the landscape. Restore that uncertainty rather than deciding the metaphysics: replace the final apposition with ‘presumed to be a shadowy echo of the northern part of the [[Hara]]’. Preserve this qualification in any retrospective rewrite.

- [ ] **Warning — metadata.map_location_missing:** Both required endpoint `locator` values remain blank. The consulted Morkalan, Bleakhold and session sources provide landscape context but no supported mapped source/outlet positions. Supply map/locator values only from a human-selected map or established coordinates; retain the typed skeleton meanwhile.
%%^End%%

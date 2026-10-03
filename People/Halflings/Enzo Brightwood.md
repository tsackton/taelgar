---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: halfling
ancestry: null
born: null
gender: male
name: Enzo Brightwood
affiliations:
  - {org: Brightwoods, type: primary}
  - {org: Rangers}
whereabouts:
  - {type: away, start: 1720-01-14, location: Eftly}
  - {type: away, start: 1720-01-15, location: Champimont}
  - {type: away, start: 1720-01-18, location: Champimont}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1720
---
# Enzo Brightwood
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (he/him), of Brightwoods  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[enzo-brightwood.png|right|400]]A skirmisher and scout. Young, to be on the road. Cousin of [[Adra Brightwood]].

%% Meta 3rd  level rogue scout %%

%% need to fix whereabouts; he is with Adra and Damien %%

%%^Metadata:names:v1%%
- {name: "Enzo Brightwood", language: "unknown", status: "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 portrait of Enzo as a young scout; the whereabouts retain the January itinerary and do not yet represent the later February report near Veltor.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Recorded supported campaign knowledge in `knownTo`, the article viewpoint in `POV`, and its temporal limits in `povNotes`.
- Added a primary name entry; the ordinary name Enzo and transparent surname do not need a pronunciation guide.
- Resolved the unambiguous Rangers affiliation by changing its target from `The Rangers` to `Rangers`.

### Validated judgments
- Status disposition: `status/cleanup/metadata` remains supported by the unresolved family affiliation and outdated whereabouts.
- The January scout portrait is proportionate to Enzo’s minor reference role.

### Open findings

- [ ] **Warning — relationship.unresolved:** `affiliations.org: Brightwoods` has no resolvable family note. The source [[Rangers in Champimont]] establishes that Enzo and [[Adra Brightwood]] are cousins, but does not supply an existing family-page target. Create a human-approved Brightwoods family note or remove only the unresolved family affiliation while retaining the cousin relationship; keep `{org: Rangers}`.
- [ ] **Warning — coverage.later_material_change:** The whereabouts still end with an open-ended January 18 stay in Champimont. [[Viepuck and Tal - Authored Turns]] identifies the group as Damien, Adra, and Enzo, and Damien’s reply places them near Veltor; its session source config dates the exchange to February DR 1720 without an exact day. Choose whether to update the itinerary, defer it with a human-applied game-update tag, or intentionally retain the January snapshot. Copy-ready later entry, once its temporal handling is accepted: `{type: away, start: 1720-02, location: near Veltor}`. Do not invent a precise departure day or extend a January stay indefinitely.
%%^End%%

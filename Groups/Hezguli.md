---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T16:23:04-04:00"
lintVersion: "2.3"
tags: [group, status/check/lint]
typeOf: communal society
ancestry: orc
name: Hezguli
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Hezguli
>[!info]+ Information  
> An [[Orcs|orc]] communal society  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Hezguli are a community of [[Orcs|orcs]] who were born under the sway of [[Thark]]’s curse, but freed from it as children or young adults. They have learned—often with difficulty—to live as free orcs. They are most closely associated with General [[Murook]], widely regarded as their unofficial leader.

%% this is supposed to have vibes kind of like a support group for orcs rescued from Thark in childhood or young adulthood, a kind of mix something like AA and a fraternity and a mutual aid society %%

%%^Metadata:names:v1%%
- {name: Hezguli, role: primary, language: Orcish, pronunciation: HEZ-goo-lee, status: proposed, notes: language inferred from the group's Orcish context; pronunciation is spelling-only}
%%^End%%

%%^Metadata:article:v1%%
mode: group reference
povNotes: "Accuracy range: the DR 1740s campaign era. The article describes the modern Hezguli community and its association with Murook; the shared comment records a support-group and mutual-aid emphasis not yet present in visible prose."
%%^End%%

%%^Lint%%
## Taelgar note lint

### Open findings

- [ ] **warning — `name.pronunciation_missing`:** `HEZ-goo-lee` is a spelling-only proposal. Orcish is inferred from the group’s context; [[Languages]] supplies no exact Orcish phonology. If accepted, copy:
  ```yaml
  pronunciation: HEZ-goo-lee
  ```
  and update the name entry’s status.
- [ ] **suggestion — `coverage.shared_material_candidate`:** The visible article omits the support-group and mutual-aid function described in this note’s shared comment and in [[Nuzkar]]’s shared history. This is a promotion decision, not a claim that the canonical prose is false. Copy-ready candidate: “The Hezguli also serve as a mutual-aid community for freed orcs learning to live outside Thark’s control, offering practical support and fellowship to people carrying the effects of enslavement.”
- [ ] **suggestion — `dm.notes_no_local_evidence`:** No linking `_DM_` note was found to support `dm_notes: important`. Confirm it if it reflects information in someone’s head or elsewhere; otherwise a human may change it to `none`. The linter will not remove it automatically.

### Applied changes

- Added the explicit name, `POV: 1740s`, current article metadata, and migrated the proposed naming data to v1.
%%^End%%

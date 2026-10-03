---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/ai, status/check/lint]
species: dwarf
gender: male
name: Vondal Ferrystone
affiliations:
  - {org: Ferrystones, type: primary}
whereabouts: Aslain
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720s
---
# Vondal Ferrystone
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him), of the [[Ferrystones]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[vondal-ferrystone.png|left|200]]

Vondal Ferrystone is a dwarf of the [[Ferrystones]] living in [[Aslain]]. He and [[Kazak Ferrystone]] helped the [[Heroes of Cleenseau]] investigate the ruined [[Night Queen Temple (Aslain)|Night Queen temple]], identifying the supposed necromantic chamber as recent, poorly built stonework inconsistent with the older temple.

%%^Metadata:names:v1%%
- {name: Vondal Ferrystone, language: unknown, pronunciation: VON-dahl FEH-ree-stohn, notes: "Proposed adaptation using the Tolkien Dwarvish analogue in [[Languages]], with full o/ah vowels in Vondal and a plain-English reading of Ferrystone. The name's in-world language and accepted pronunciation are unrecorded.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early-1720s portrait of Vondal in Aslain, anchored by the February 1720 temple investigation; earlier and later residence are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, added the explicit name and Cleenseau `knownTo` code, and added persistent name and temporal-viewpoint metadata.

### Validated judgments
- The clan, Aslain residence, and temple stonework assessment provide a sufficient minor-person reference. [[Kazak Ferrystone]] and the preserved recap for [[Cleenseau - Session 17]] corroborate the investigation; the refreshed visible paragraph has been preserved.
- `dm_owner: mike` is outside the local `_DM_` attestation-review scope, so the existing `dm_notes: color` is preserved without a no-local-evidence finding.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise `VON-dahl FEH-ree-stohn` in `Metadata:names:v1`. The Tolkien Dwarvish analogue in [[Languages]] motivates a cautious adaptation with initial stress, a full rounded o and final ah, and sounded v/n/d/l; the transparent English surname is read as written. These are proposed reading choices, not established in-world phonology. On acceptance, set `status: documented` and copy the accepted primary pronunciation to frontmatter. The name's in-world language remains `unknown`.
%%^End%%

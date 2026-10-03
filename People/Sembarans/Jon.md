---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
born: 1700
gender: male
name: Jon
affiliations:
  - {org: "Lord's Guard of Cleenseau", type: Gateguard}
whereabouts: Cleenseau
knownTo: []
dm_owner: none
dm_notes: none
POV: 1720
---
# Jon
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A deputy of [[Ysabel]] and gateguard; strong and quick with a spear. He was on the bridge during the [[Undead Attacks in Sembara]] and distinguished himself. A strong supporter of [[Beatrix Thorne|Béatrix Thorne]].

%%^Metadata:names:v1%%
- {"name": "Jon", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 guard portrait after the bridge fighting whose undated deputy relationship still assumes Ysabel is alive; that mismatch requires human reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added required knownTo, minimal name metadata, and supported POV/povNotes.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — coverage.later_material_change:** The opening calls Jon a deputy of [[Ysabel]], while [[Ysabel]] records her death on January 6, 1720 and [[Beatrix Thorne]] records her appointment as sheriff on January 11. The note already looks back on the undead bridge fighting. A post-attack candidate is `A gateguard and former deputy of [[Ysabel]], strong and quick with a spear.` Confirm his later position without assuming he became Béatrix's deputy; choose an updated snapshot, an intentionally earlier one, or deferral with the appropriate game-update status.

- [ ] **Warning — metadata.affiliation_role:** The affiliation uses `type: Gateguard`, although [[Metadata Specification]] restricts affiliation type to member, primary or leader and uses `title` for the role. The body unambiguously describes a gateguard. Proposed entry: `{org: Lord's Guard of Cleenseau, type: member, title: Gateguard}`.
%%^End%%

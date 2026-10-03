---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
born: 1690
gender: male
name: "Jean-Luc d'Aslain"
affiliations:
  - {org: "d'Aslains", type: primary}
whereabouts:
  - {type: home, location: Aslain}
  - {type: home, location: Beury}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Jean-Luc D'Aslain
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[d'Aslains]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[jean-luc d'aslain.png|right|320]]A disciple of the Father, splitting time between [[Dallet]] and [[Beury]]. A cousin of the current baron, [[Isabeau d'Aslain]].

%%^Metadata:names:v1%%
- {"name": "Jean-Luc d'Aslain", "language": "unknown", "pronunciation": "zhahn-lük dahz-LANE", "status": "proposed", "notes": "French-shaped Jean-Luc follows the southern Sembaran analogue in [[Languages]]: j as zh, Jean with an approximately nasal ah, and Luc with a rounded ee vowel (ü); d'Aslain uses the recorded Ahz-lane in [[Aslain]] with the prefixed d. This is a proposed full-name combination, not an attested pronunciation."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early-DR 1720 portrait of the disciple while Isabeau is the current Baroness; the later change of baron remains a human update decision.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added required knownTo, minimal name metadata, and supported POV/povNotes.
- Recorded the existing filename identity explicitly as name.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes `zhahn-lük dahz-LANE`. French-shaped Jean-Luc follows the southern Sembaran analogue in [[Languages]]: j as zh, Jean with an approximately nasal ah, and Luc with a rounded ee vowel (ü); d'Aslain uses the recorded Ahz-lane in [[Aslain]] with the prefixed d. This is a proposed full-name combination, not an attested pronunciation. Confirm or revise this reading; if accepted, copy it to frontmatter `pronunciation` and mark the entry documented.

- [ ] **Warning — coverage.later_material_change:** The visible description calls [[Isabeau D'Aslain]] the current baron, but [[Asineau in May (Email)]] reports a new Baron by May DR 1720. For a later snapshot, replace the second sentence with `A cousin of [[Isabeau D'Aslain]], the former Baroness of Aveil.` Alternatively preserve this early-1720 snapshot intentionally, or defer the update with the appropriate game-update status; the human must choose the article framing and any status change.
%%^End%%

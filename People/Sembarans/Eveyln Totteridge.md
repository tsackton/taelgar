---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:37:56-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/clee, status/check/lint]
species: human
ancestry: Sembaran
title: Sergeant
born: 1689
gender: female
name: Eveyln Totteridge
affiliations:
  - {org: Army Garrison of Cleenseau, title: Sergeant}
whereabouts:
  - {type: home, location: Cleenseau}
  - {type: away, start: 1719-10-15, end: 1719-10-29, location: "Bandit's Way"}
  - {type: away, start: 1719-11-27, end: 1720-01-10, location: Dunfry}
knownTo: [clee]
dm_owner: mike
dm_notes: important
POV: 1720
---
# Sergeant Eveyln Totteridge
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% status/update -> status/check/mike %%

![[eveyln-totteridge.png|right|320]]The sergeant of the [[Army Garrison of Cleenseau|River Patrol]], Evelyn is a talented soldier and particularly strong and brutal with her favored weapon, a two-handed waraxe.

%%^Metadata:names:v1%%
- {"name": "Eveyln Totteridge", "language": "Sembaran", "status": "disputed", "notes": "The frontmatter and heading read Eveyln, while the article, [[Army Garrison of Cleenseau]], and [[Into Aslain (Email)]] use Evelyn. Preserve the recorded name pending human choice; the intended spelling and its pronunciation are unresolved."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 portrait centered on her River Patrol command, with whereabouts recorded through her January return from Dunfry; the entry does not attempt a complete campaign travel history.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added supported name and temporal metadata.
- Added `knownTo: [clee]` from the reviewed campaign evidence.
- Corrected an objective typo.

### Validated judgments
- `status/gameupdate/clee` is preserved and not assessable: the legacy reminder does not identify the intended update, and the later northern deployment does not itself establish a durable change to her River Patrol role.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The exact primary name is `Eveyln Totteridge` in metadata and the heading, but `Evelyn` in the article, [[Army Garrison of Cleenseau]], and [[Into Aslain (Email)]]. Confirm the spelling. If Evelyn is intended, set `name: Evelyn Totteridge`, change the displayed heading to `# Sergeant Evelyn Totteridge`, and amend the persistent primary entry without renaming the file. If Eveyln is intentional, supply its pronunciation. The name entry remains disputed.
%%^End%%

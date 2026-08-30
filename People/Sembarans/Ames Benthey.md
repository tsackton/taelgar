---
headerVersion: 2023.11.25
lintedAt: "2026-08-28T16:53:46-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo:
  - {campaign: clee, date: 1720-01-03}
born: 1675
gender: male
name: Ames Benthey
affiliations:
  - {org: "Lord's Guard of Cleenseau", title: Captain, type: leader}
  - {org: Essfords, title: Guard Captain}
  - {org: "Lord's Council of Cleenseau"}
whereabouts:
  - {type: home, location: Cleenseau}
  - {type: away, start: 1720-01-04, end: 1720-01-19, location: travelling to Embry}
  - {type: away, start: 1720-01-20, end: 9999, location: Embry}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Ames Benthey
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:clee%% Seen by the [[Heroes of Cleenseau]] on January 3rd, 1720 in [[Cleenseau]], the [[Manor of Cleenseau]], the [[Barony of Aveil]] %%^End%%

![[ames-benthey.png|right|320]]The captain of the household guard of [[Essford Manor]], part of the [[Lord's Guard of Cleenseau|Lord's Guard]] in [[Cleenseau]]. Likes to play dice with [[Celyn]]. Better at delegating than doing any actual work and enjoys his food. However, when push comes to shove, he is a competent fighter and captain. 






%%^Campaign:none%%
### Relationships
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Alive"], 
			dv.pages("#person or #organization or #item")
				.where(f => util.isLinkedToPerson(f.file, dv.current().file))
				.sort(f => util.s("<maintype:n>", f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.isAlive(b.file.frontmatter, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {name: Ames Benthey, role: primary, language: Sembaran, pronunciation: AYMZ BEN-thee, status: proposed, notes: "English-side Sembaran analogue: Ames uses a long a and Benthey takes initial stress; exact in-world phonology is not documented."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 portrait of Ames around his departure from Cleenseau for Embry; earlier and later career are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added `knownTo: [clee]`, a DR 1720 `POV`, and persistent name and temporal metadata.
- Normalized the legacy `Campaign:None` marker to `Campaign:none`.

### Validated judgments
- The `Campaign:none` block is an operational relationship index rather than narrative material.
- The DR 1720 campaign timeline supports Ames's departure for Embry, already represented by his whereabouts metadata.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name block retains the proposed Sembaran pronunciation `AYMZ BEN-thee`, using the English side of the Sembaran analogue in [[Languages]]. If accepted, add `pronunciation: AYMZ BEN-thee` to frontmatter and change the name entry to `status: documented`; otherwise revise the proposal while preserving its derivation.
%%^End%%

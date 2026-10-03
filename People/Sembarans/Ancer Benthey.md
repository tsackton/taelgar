---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:37:56-04:00"
lintVersion: "3.5"
tags: [person, testcase, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo: []
born: 1689
gender: male
name: Ancer Benthey
affiliations:
  - {org: Bridge Patrol, title: Sergeant, start: 1719-11-20, type: leader}
  - {org: Army Garrison of Cleenseau, title: Sergeant, start: 1719-11-20}
whereabouts:
  - {type: home, location: Cleenseau}
  - {type: away, location: Army Garrison of Cleenseau}
knownTo: [clee]
dm_owner: mike
dm_notes: none
POV: 1719
---
# Ancer Benthey
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[ancer-benthey-portrait.png|right|320]]The nephew of [[Ames Benthey]], recently appointed sergeant of the [[Army Garrison of Cleenseau|Bridge Patrol]] after [[Odo Cordwaner]] was dismissed. He is untested and rumored to be somewhat stern, and not very close to his uncle.

%%^Metadata:names:v1%%
- {name: "Ancer Benthey", language: "Sembaran", pronunciation: "AN-ser BEN-thee", notes: "Benthey follows the accepted BEN-thee in [[Ames Benthey]]. Ancer is proposed with short a and soft c before e, following the English component of Sembaran guidance in [[Languages]] and the family’s recorded English-style form. The French alternative would nasalize the opening and stress the final syllable; the given-name reading remains unconfirmed.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: A late DR 1719 portrait shortly after his appointment as sergeant on November 20; later deployment and promotion prospects do not establish a later appointment.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported name, campaign-knowledge, and temporal metadata; normalized frontmatter formatting.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — relationship.unresolved:** The first affiliation names `Bridge Patrol`, which has no resolving note, while [[Army Garrison of Cleenseau]] establishes that patrol as part of the garrison. Choose a separate patrol record or consolidate the two sergeant entries to `{org: Army Garrison of Cleenseau, title: Sergeant of the Bridge Patrol, start: 1719-11-20}`. Keep patrol command distinct from command of the whole garrison.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `AN-ser BEN-thee` in `Metadata:names:v1`. Benthey follows the accepted BEN-thee in [[Ames Benthey]]. Ancer is proposed with short a and soft c before e, following the English component of Sembaran guidance in [[Languages]] and the family’s recorded English-style form. The French alternative would nasalize the opening and stress the final syllable; the given-name reading remains unconfirmed. If accepted, copy it to frontmatter and mark the entry documented; otherwise supply the preferred reading.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:37:56-04:00"
lintVersion: "3.5"
displayDefaults: {endStatus: killed himself in remorse}
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
born: 1681
gender: male
died: 1719-11-05
name: François the Bandit
aliases: [François the Bandit]
whereabouts: Cleenseau Region
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1719
---
# François the Bandit
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A ruffian and ne'er do well, he was a key figure in the [[Attempted Poisoning of Cleenseau]].

%%^Metadata:names:v1%%
- {"name": "François the Bandit", "language": "Sembaran", "status": "proposed", "pronunciation": "frahn-SWAH thuh BAN-dit", "notes": "Proposed from the southern French analogue for Sembaran in [[Languages]]: François has a nasal first vowel, ç as s, oi as wah, and silent final s. The descriptive title is read as ordinary English. Exact in-world pronunciation remains unrecorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a retrospective DR 1719 entry covering François's role in the November poisoning attempt and his death; earlier life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added supported name and temporal metadata.
- Added `knownTo: [clee]` from the reviewed campaign evidence.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry proposes `frahn-SWAH thuh BAN-dit`. Proposed from the southern French analogue for Sembaran in [[Languages]]: François has a nasal first vowel, ç as s, oi as wah, and silent final s. The descriptive title is read as ordinary English. Exact in-world pronunciation remains unrecorded. If accepted, add `pronunciation: frahn-SWAH thuh BAN-dit` to frontmatter and set the entry to `status: documented`; otherwise revise the proposal with its basis.

- [ ] **Warning — correctness.unsupported_certainty:** `displayDefaults.endStatus: killed himself in remorse` presents the manner and motive as certain. [[Cleenseau - Session 04]] says he died in custody apparently by suicide, and [[Cleenseau Campaign - Timeline]] qualifies remorse as apparent. Preserve that uncertainty with `displayDefaults: {endStatus: "died in custody, apparently by suicide"}`, or confirm stronger evidence before retaining the present wording.
%%^End%%

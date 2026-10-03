---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
born: 1730
gender: female
name: Scordith
affiliations:
  - {org: Silver Tempests, end: 1747-06-09}
whereabouts:
  - {type: home, end: 1736, location: Paisa}
  - {type: away, start: 1747-03-01, end: 1747-06-09, location: Voltara}
knownTo: [grli]
dm_owner: tim
dm_notes: none
POV: 1747
---
# Scordith
>[!info]+ Biographical Info  
> A [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Scordith was born in [[Paisa]], a small village on the northwestern shore of [[Lake Valandros]]. Her early life was uneventful, until her parents died in a tragic accident when she was only six years old. The village elders, not sure what to do, sent her to live in a secretive monastery in the hills that was willing to take her in. Scordith was raised in the monastery for the next twelve years. 

When she turned 16, she tried to flee the monastery, but the monks had other ideas, and tried to stop her. At this moment, a divine spark awoke in Scordith, and she barely escaped through her new-found connection to [[The Sibyl]]. Fleeing north, she found herself in [[Voltara]], where she met [[Lyra]] and started working for the [[Great Library]]. 

After traveling to help some centaurs deal with a curse with [[Adrik]], [[Samso]], [[Brelith]], and [[Aglath]], she returned to [[Voltara]] alone, and was never seen again.

%%SECRET[v2:4a7de520e8a49b5aaf42ce08c8b4027f]%%

%%^Metadata:names:v1%%
- {"name":"Scordith","language":"unknown","pronunciation":"SKOR-dith","notes":"Cautious spelling-based proposal because no name-specific pronunciation or source language is established: initial sc as sk, or as in horn, short i, final unvoiced th as in thin, and first-syllable stress.","status":"proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a retrospective account through Scordith's disappearance in DR 1747, with selected childhood backstory; the monastery duration and escape age conflict and her later fate is not publicly established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added explicit name: Scordith, knownTo: [grli], and the persistent pronunciation proposal.
- Recorded POV: 1747 with temporal coverage and normalized frontmatter.
- Corrected “was never seen from again” to “was never seen again.”

### Validated judgments
- [[Great Library Session Notes - Arc 1]] corroborates Scordith’s sorcerer role, early Library missions, and departure on June 9, DR 1747. Her origin, escape, role, and disappearance form a sufficient bounded account.
- Reviewed the local-only evidence and SECRET block; preserved the existing privacy boundaries and dm_notes attestation.

### Open findings

- [ ] **Warning — correctness.internal_conflict:** The first paragraph places Scordith in the monastery at age six “for the next twelve years,” implying departure at eighteen, but the next paragraph says she fled at sixteen. With born: 1730, eighteen would also fall after the DR 1747 adventures recorded in [[Great Library Session Notes - Arc 1]]. Resolve the intended chronology. If the stated escape age and birth year are retained, the copy-ready correction is: “Scordith was raised in the monastery for the next ten years.” Otherwise reconcile the age, duration, and birth year together; no chronology has been silently changed.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm the spelling-based pronunciation proposal `SKOR-dith` in the persistent name block. No explicit pronunciation or established name-language was found: the proposal reads initial sc as sk, or as in “horn,” short i, and unvoiced th as in “thin,” with first-syllable stress. If accepted, add `pronunciation: SKOR-dith` to frontmatter and mark the entry documented; otherwise provide the intended pronunciation.
%%^End%%

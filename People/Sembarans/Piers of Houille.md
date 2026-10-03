---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/stub, status/check/lint]
species: human
died: 1720-02-16
name: Piers of Houille
whereabouts:
  - {location: Houille, type: home}
  - {location: Cranford, type: away, start: 1720-02-11, end: 1720-02-16}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: modern
---
# Piers of Houille
>[!info]+ Biographical Info  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% dead suitor #2. see [[Lambert Talwrey]] for details on the source of the murders. literally no information made up %%

%%^Metadata:names:v1%%
- {"name": "Piers of Houille", "language": "unknown", "pronunciation": "PEERZ ov oo-yee", "status": "proposed", "notes": "Combines the ordinary English name Piers and connective of with the accepted oo-yee in [[Houille]]. The full personal-name pronunciation is a proposal because only the place component is explicitly attested."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a retrospective reference to a suitor who died in February DR 1720; the authored identity currently appears only in a comment.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added required knownTo, minimal name metadata, and supported POV/povNotes.
- Recorded the existing filename identity explicitly as name.

### Validated judgments
- status/stub is supported: the note has no visible authored reference prose.

### Editorial assessment
**Underdeveloped**. The note has no visible identifying account: its only authored statement is a hidden dead-suitor/source reminder. One sentence identifying Piers as Juliana Westby's murdered suitor would fill the central gap.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes `PEERZ ov oo-yee`. Combines the ordinary English name Piers and connective of with the accepted oo-yee in [[Houille]]. The full personal-name pronunciation is a proposal because only the place component is explicitly attested. Confirm or revise this reading; if accepted, copy it to frontmatter `pronunciation` and mark the entry documented.

- [ ] **Warning — coverage.established_fact_missing:** The visible note consists only of its generated header. [[Cleenseau - Session 17]] identifies Piers as one of [[Juliana Westby]]'s murdered suitors, which supplies the minimum useful reference account. Candidate: `Piers of [[Houille]] was a suitor of [[Juliana Westby]] who was murdered in [[Cranford]] in February DR 1720.` The existing death field supplies the month; keep details about the murderer subject to the source record.
%%^End%%

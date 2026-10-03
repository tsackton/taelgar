---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Skaer
born: 1716
gender: male
died: 1748
name: Jorma
whereabouts:
  - {type: home, location: Skaerhem}
  - {type: home, start: 1737, location: Vetta}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Jorma
>[!info]+ Biographical Info  
> A [[Skaer]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% setting metadata/jheader as ideally want a way to tag campaign info for people that the party didn't meet, but only heard about, but not clear the best way to do this as the location ends up wrong if you use the date the party heard about the person. %%

Jorma, a Skaer priest in his early 30s, served as the Priest of the Waters in [[Vetta]]. He was killed by [[Urgall the Black]] in May 1748.

%%^Metadata:names:v1%%
- {name: Jorma, language: unknown, pronunciation: YOHR-mah, status: proposed, notes: "Proposal using the Finnish side of the Skaegish analogue in [[Languages]]; the name's source language is unconfirmed."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a retrospective DR 1748 portrait of Jorma as a priest in his early thirties, ending with his death in May; earlier residence is recorded only in the whereabouts metadata.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added `knownTo: [dufr]` to record campaign knowledge without an invented meeting date.
- Added a primary name entry with a pronunciation proposal; the source language remains unknown.
- Recorded a supported temporal viewpoint and persistent temporal notes.

### Validated judgments
- The minimal priest-and-fate account is sufficient for this minor figure. [[Urgall the Black]] and [[Vetta]] corroborate the fatal attack and its aftermath.
- Confirmed local DM sources support the positive attestation; their contents are not reproduced here.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `YOHR-mah`. The proposal uses the Finnish side of the Skaegish analogue in [[Languages]]: initial stress, j read as English y, a pure o vowel, a lightly tapped r, and final ah. The documented analogue also allows Norwegian and Swedish influences; the actual source language and intended pronunciation remain unconfirmed. Accept into frontmatter and mark the entry documented, or supply the intended reading.
- [ ] **Warning — status.questioned:** `status/cleanup/metadata` is tied to the comment about how to record a person the party only heard about. [[Metadata Specification]] now supports `knownTo: [dufr]` without a date or meeting header, and that field has been added. If this resolves the intended cleanup, remove the obsolete comment and `status/cleanup/metadata`; otherwise identify the remaining metadata task. Both are preserved for human disposition.

### DM evidence
- [[_DM_/_Dunmari Frontier/NPCs/Ankka]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Vetta/Encounters]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Vetta/Temple Key]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Vetta/Vetta DM Notes]]
%%^End%%

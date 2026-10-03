---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
born: 1538
gender: male
died: 1552
title: King
name: Bertram I
affiliations:
  - {place: Vostok, title: High King, end: 1551, start: 1549}
  - {place: Sembara, title: High King, start: 1549}
  - {place: Ardlas, title: High King, start: 1549}
  - {place: Lavnoch, title: High King, start: 1549}
  - {place: Breva, title: High King, start: 1549}
  - {org: House of Sewick, type: primary}
knownTo: []
dm_owner: none
dm_notes: none
POV: modern
---
# King Bertram I
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[House of Sewick]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`

Bertram I, [[Derik III|Derik III’s]] youngest son, came to the throne in December of 1549, a boy of 11. His mother, [[Jane of Tollen]], was appointed regent, and Bertram’s entire kingship is dominated by her, a shrewd woman who disliked waste.

He did not live long enough to have children. He is believed to have died of the effects of the [[Blood Plague]].

%%^Metadata:names:v1%%
- {"name": "Bertram I", "language": "Sembaran", "notes": "Ordinary personal name with a regnal number; no separate pronunciation guide is needed.", "status": "inferred"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: A modern retrospective of Bertram I's short reign and presumed death from the Blood Plague; the accession season remains disputed across sources.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: []`; no campaign knowledge was established in the reviewed sources.
- Normalized frontmatter without changing existing parsed values.
- Added a persistent name entry, `POV: modern`, and temporal coverage metadata.
- Corrected `Bertam I,` to `Bertram I,` (objective typo).

### Validated judgments
- Bertram is an ordinary personal name and the regnal number needs no separate pronunciation guide.
- The short account supplies parentage, regency, and fate; the unresolved chronology does not require broader biography development.

### Open findings

- [ ] **Warning — content.cross_note_conflict:** The body places accession in December DR 1549, while [[Timeline of Sembaran History]] places the coronation in summer DR 1549. The Vostok affiliation ends in DR 1551, whereas the timeline drops that title in fall DR 1550. The timeline is itself marked for review, so neither version is silently preferred. Confirm the accession and title-end chronology. A bounded body option that retains their shared certainty is: “Bertram I, [[Derik III|Derik III’s]] youngest son, came to the throne in DR 1549, a boy of 11.” If the timeline’s Vostok event is confirmed, use `end: 1550` on that affiliation; otherwise retain `end: 1551` and reconcile the timeline separately.
%%^End%%

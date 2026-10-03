---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, testcase, status/check/lint]
species: human
ancestry: Sembaran
born: 1539
gender: female
title: Queen
died: 1592
name: Elaine I
affiliations:
  - {org: House of Sewick, type: primary}
  - {place: Tyrwingha, start: 1567, end: 1571, title: Princess Consort}
  - {place: Tyrwingha, start: 1571, title: Queen Consort}
  - {place: Sembara, start: 1582}
  - {place: Tyrwingha, start: 1589, title: Queen}
knownTo: [clee]
dm_owner: mike
dm_notes: none
POV: modern
---
# Queen Elaine I
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her), of the [[House of Sewick]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`

The twin sister of [[Anne]], her disputes with her sister over the throne dominated the 1560s and 1580s.

Elaine spent much of the 1570s in Tyrwingha, and married the King of Tyrwingha, [[Cynan]], thus reuniting the crowns that had been sundered on [[Derik III|Derik III's]] death at the end of the Great War. 

Her three children were: [[Arryn I]], [[Blanche II]], and [[Derik of Lils|Derik]]. 

%% No specific canonical details exist except in the various Sembaran documents scattered about Worldbuilding. %%

%%^Metadata:names:v1%%
- {"name": "Elaine I", "language": "Sembaran", "role": "regnal", "notes": "Sembaran regnal form; the ordinary personal name and regnal number do not need a separate pronunciation guide.", "status": "inferred"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern retrospective account of Elaine’s dynastic disputes, marriage, and children; dated affiliations distinguish her changing royal roles.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported campaign-knowledge metadata, a persistent name entry, and a broadly modern retrospective POV with temporal-coverage guidance; normalized frontmatter.

### Validated judgments
- Elaine I is an ordinary regnal form and needs no separate pronunciation guide.
- The shared comment remains a source/provenance reminder. The local-DM attestation gate does not apply to `dm_owner: mike`.

### Editorial assessment
**Underdeveloped**. The visible biography names the dynastic dispute but does not explain the compromise succession, the later attempt to coerce Elaine, or the accession that resolved her claim to Sembara. The smallest useful scope is one paragraph linking the two succession crises to her coronation.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The sentence about disputes dominating the 1560s and 1580s omits their central resolution and leaves her accession unexplained. [[Interregnum of 1568]] identifies Wisym as the compromise ruler, while [[Attempted Geas of Elaine I]] and [[Timeline of Sembaran History]] establish the failed coercion and Elaine’s coronation in DR 1582. Add: “After [[Blanche I]] died, Elaine and [[Anne]] disputed the succession, and [[Wisym I]] was chosen as a compromise king in the [[Interregnum of 1568]]. When Wisym died in DR 1582, Anne [[Attempted Geas of Elaine I|attempted to compel Elaine by magic]] to abandon her claim. The attempt failed, and Elaine became queen of [[Sembara]]; Anne was subsequently executed for treason.” Do not give Anne’s execution a new exact date here: her person note dates it to DR 1583, while the timeline groups it under DR 1582.
%%^End%%

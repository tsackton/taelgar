---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, testcase, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo: []
born: 1702
gender: male
title: King
name: Arryn III
affiliations:
  - {org: House of Lils, type: primary}
  - {place: Sembara, start: 1745}
  - {place: Tyrwingha, start: 1745}
whereabouts:
  - {type: home, location: Tafolwern, end: "1721-08"}
  - {type: home, location: Embry, start: "1721-09"}
knownTo: []
dm_owner: none
dm_notes: none
POV: 1740s
---
# King Arryn III
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[House of Lils]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%%^Date:1721b%%
A young princeling of [[Tyrwingha]], he is a quiet and mild-mannered child who is said to particularly love stories about his namesake, [[Arryn I]].
%%^End%%

%%^Date:1740%%
The king of Sembara in the 1740s, he is a quiet ruler and has largely maintained the peace and prosperity of his mother, [[Elaine II]]. He came to the throne in DR 1745 on her death, and continues to be interested in tales of his namesake, [[Arryn I]], and his supposed second life in [[Twilight's Grace]].
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Arryn III", "role": "regnal", "language": "unknown", "pronunciation": "AR-in the Third", "notes": "The article says he was named after [[Arryn I]]. Proposed reading uses the Welsh analogue for their Tyrwinghan context in [[Languages]]: a as in father, final y as short i, and initial stress. Sembaran English AIR-in is an alternative; the exact name language is unrecorded.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s kingship portrait whose prose and affiliations place accession in DR 1745, plus a separate childhood passage before DR 1721; the intervening years are not described and the kingship block’s earlier opening date requires correction.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected “a quite and mild-mannered child” to “a quiet and mild-mannered child.”
- Added required `knownTo: []`, primary name metadata with the documented namesake relationship and a proposed pronunciation, and 1740s POV metadata.
- Normalized frontmatter; preserved both existing date markers for review.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes `AR-in the Third`, preserving the explicitly stated naming after [[Arryn I]]. [[Languages]]’ Welsh analogue for their Tyrwinghan context supports open `a`, final `y` as short /i/, and first-syllable stress; the Sembaran English alternative is `AIR-in`. Confirm or replace the reading; if accepted, copy it to frontmatter `pronunciation` and mark the entry `documented`.
- [ ] **Warning — temporal.date_block_conflict:** The kingship paragraph opens at `%%^Date:1740%%` but says he acceded in DR 1745, agreeing with both leader affiliations and [[Elaine II]]. A view dated DR 1740–1744 therefore exposes his later kingship. Copy-ready correction: replace only `%%^Date:1740%%` with `%%^Date:1745%%`. Preserve the paragraph and its end marker; human approval is required because this changes filtered visibility.
%%^End%%

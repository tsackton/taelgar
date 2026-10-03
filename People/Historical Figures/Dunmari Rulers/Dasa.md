---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
born: null
died: 1395
gender: male
title: Samraat
name: Aatmaj Dasa
aliases: [Samraat Dasa, Samraat Aatmaj Dasa, Aatmaj Dasa]
affiliations:
  - {org: Aatmaji Dynasty, type: primary}
  - {org: Dunmar, start: 1385, type: leader}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: modern
---
# Samraat Aatmaj Dasa
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him), of the [[Aatmaji Dynasty|Aatmaji dynasty]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`

The last Samraat of the [[Aatmaji Dynasty]]. 

His tomb is among the monuments in Kharsan. 

%%SECRET[v2:f655efefe17c2c59b53dd2d7fe0c1241]%%

%%^Metadata:names:v1%%
- {"name": "Aatmaj Dasa", "language": "Dunmari", "pronunciation": "AAT-muj DAA-suh", "notes": "Proposed using the Hindi side of the Dunmari analogue in [[Languages]]: initial aa is long, t and d are dental, j is the sound in judge, and unstressed a is reduced. The Dasa vowel lengths and whether its final a is retained are uncertain; a Hindi-style final-vowel loss would give DAAS.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern retrospective identification of the last Aatmaji Samraat and his tomb; the reign and earlier scouting-report chronology require reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` and persistent name and temporal metadata; normalized frontmatter.

### Validated judgments
- [[Aatmaji Dynasty]], [[Dunmar]], and [[Report of the Aagiri to Samraat Dasa]] establish the defining expedition and its dynastic consequence.
- Local sources support the positive `dm_notes` attestation. The `SECRET` block was reviewed and preserved; its recovery candidate remains in the private handoff.

### Editorial assessment
**Underdeveloped** — The visible entry identifies the last Samraat and his tomb but omits the disastrous expedition and death that ended the Aatmaji dynasty. A short account of that established consequence is the smallest useful completion; the earlier scouting report and reign dates also need reconciliation.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The defining end of Dasa’s reign is absent from the visible article. [[Aatmaji Dynasty]], [[Dunmar]], and [[Report of the Aagiri to Samraat Dasa]] establish that he led an expedition against Drankor, died in the attempt, and ended the dynasty. Copy-ready addition: “Dasa led a disastrous expedition into [[Gazetteer/Drankorian Hinterland/Drankor/Drankor|Drankor]] and died in the attempt, bringing the [[Aatmaji Dynasty]] to an end and leaving [[Dunmar]] in turmoil.” This adds his defining fate without inventing motives or a new date.

- [ ] **Warning — correctness.cross_note_conflict:** The Dunmar affiliation starts Dasa’s rule in DR 1385, while [[Report of the Aagiri to Samraat Dasa]] addresses him as Samraat in a document Nuzkar tentatively dates to DR 1378. The report’s calculation is explicitly uncertain. Decide whether to retain `start: 1385` and clarify the report’s retrospective dating, or revise the accession date from an adopted chronology. Do not treat the primary source itself as factually wrong or silently choose a date.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation of Aatmaj Dasa: `AAT-muj DAA-suh`. The Hindi side of the Dunmari analogue in [[Languages]] supplies long initial aa, dental t/d, j as in judge, and reduced unstressed a. Dasa’s vowel lengths and final-vowel treatment are not established; Hindi-style final-vowel loss would give DAAS. The proposal is preserved in `Metadata:names:v1`; if accepted, copy it to frontmatter and mark the entry `documented`, or revise it with its derivation.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Samraat Tombs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 41]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Desolation of Cha'mutte Brainstorming]]
%%^End%%

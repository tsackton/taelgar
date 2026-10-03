---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
born: 1579
gender: nonbinary
name: Brot Starsearcher
aliases: [Brot]
whereabouts:
  - {type: home, location: "Am'khazar"}
  - {type: home, start: 1670, end: 1720-04-30, location: Taviose}
  - {type: away, start: 1719-11-21, end: 1719-12-23, location: Dunfry}
  - {type: home, start: 1720-05-01, location: Asineau}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Brot Starsearcher
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (they/them)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[brot-portrait.png|right|320]]A dwarven astronomer and tinkerer known for their clever telescope designs who lives in [[Taviose]], a small village on the outskirts of [[Cleenseau]]. 

In spring 1720, Brot and [[Diesla Starsearcher|Diesla]] moved their workshop to [[Asineau]] and became its workshop masters.

%%^Metadata:names:v1%%
- {"name": "Brot Starsearcher", "language": "unknown", "pronunciation": "BROHT STAR-ser-cher", "status": "proposed", "notes": "The [[Dwarves]] name list supplies Brot as a dwarven form, and the [[Languages]] guidance uses Tolkien Dwarvish. Proposal uses a single pure o vowel, pronounced br and final t; the transparent surname keeps its ordinary trade-tongue reading. Exact in-world phonology and the language of the complete name are unrecorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the DR 1719–1720 Cleenseau portrait, including the spring 1720 move to Asineau; the undated Taviose residence remains inconsistent with that move and requires human correction.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Recorded supported campaign knowledge in `knownTo`, the article’s temporal viewpoint in `POV`, and its coverage limits in `povNotes`.
- Added a primary name entry with a proposed pronunciation; retained `language: unknown` because the complete name’s language is not expressly attested.

### Validated judgments
- The craft and workshop account is proportionate to Brot’s reference role; the unresolved residence wording is a continuity defect, not a missing biography.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `BROHT STAR-ser-cher` for Brot Starsearcher. The [[Dwarves]] name list supplies Brot as a dwarven form, and the [[Languages]] guidance uses Tolkien Dwarvish. Proposal uses a single pure o vowel, pronounced br and final t; the transparent surname keeps its ordinary trade-tongue reading. Exact in-world phonology and the language of the complete name are unrecorded. Accept or revise this proposal in `Metadata:names:v1`; on acceptance, change its status to `documented` and copy the accepted primary pronunciation to frontmatter.

- [ ] **Warning — temporal.internal_conflict:** The lead says Brot currently lives in [[Taviose]], but the next paragraph, `whereabouts`, and [[Cleenseau - Session 29]] record the spring 1720 move to [[Asineau]]. Resolve the residence framing without removing the older Taviose connection. Copy-ready replacement for the lead: “A dwarven astronomer and tinkerer known for their clever telescope designs, formerly based in [[Taviose]], a small village on the outskirts of [[Cleenseau]].” The following move paragraph can then supply the current Asineau role. If earlier-date publication is needed, retain the old residence only in a `Date:1720-05-01b` block and place the existing relocation paragraph in `Date:1720-05-01`; these visibility changes need human approval.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/clee, status/check/lint]
species: human
ancestry: Sembaran
born: 1660
gender: male
died: 1720-06-15
title: King
name: Robert I
affiliations:
  - {org: House of Sewick, type: primary}
  - {place: Sembara, start: 1713-09-12}
knownTo: [clee]
dm_owner: mike
dm_notes: none
POV: modern
---
# King Robert I
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[House of Sewick]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`

A ruler of Sembara, son of [[Cece I]].  He was never crowned king of Tyrwingha when his mother died, that honor going to his cousin [[Elaine II]]. 

%% 
Important in Sembaran history because for much of his reign he was actually a lich, Malach. This page should be updated to reflect that,
%%

%%^Metadata:names:v1%%
- {"name": "Robert I", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern retrospective account of Robert’s royal identity; the visible narrative omits his replacement by Malach and its chronology remains unresolved.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [clee]` and persistent name and temporal metadata; normalized frontmatter.

### Validated judgments
- Robert I is an ordinary personal name with a regnal numeral; no pronunciation is needed.
- `status/gameupdate/clee` remains unchanged and is not assessable until the human chooses how to incorporate the campaign revelation and resolve the chronology.

### Editorial assessment
**Underdeveloped** — The visible royal entry omits Robert’s defining fate: his death and replacement by Malach, along with the resulting succession context. A short account of the established impersonation and Elaine’s designation as heir would supply the central missing history; the death and reign-end dates require a human decision.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.later_material_change:** [[Cleenseau - Session 25]] establishes that Robert had been replaced by [[Malach]], and [[Timeline of Sembaran History]] records the Royal Council’s DR 1718 designation of [[Elaine II]] as heir. These facts materially change the two-sentence royal biography. Copy-ready account: “Robert was killed and replaced by the lich [[Malach]], who ruled [[Sembara]] under his identity. In DR 1718, the Royal Council designated [[Elaine II]] as heir to the throne.” Resolve the dates below before assigning acts during the impersonation to Robert personally. Choose to update the article and POV, defer with the existing game-update status, or intentionally preserve the earlier account; no visibility or status change was applied.

- [ ] **Warning — correctness.cross_note_conflict:** The metadata gives `died: 1720-06-15`, but [[Cleenseau - Session 25]] places the revelation that Robert was already dead on DR 1720-03-05. [[Cleenseau - Session 28]] also records Malach’s defeat in March 1720. Distinguish Robert’s actual death, the impostor’s defeat, and the legal end of the reign, then supply the correct `died` value and any explicit affiliation end. Do not infer that June 15 represents any one of these events. The chronology remains unchanged pending that decision.
%%^End%%

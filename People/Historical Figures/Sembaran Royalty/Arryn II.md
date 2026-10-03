---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
born: 1601
gender: male
died: "1648-10"
title: King
name: Arryn II
affiliations:
  - {org: House of Sewick, type: primary}
  - {place: Sembara, start: 1602}
  - {place: Tyrwingha, start: 1602}
knownTo: []
dm_owner: none
dm_notes: none
POV: modern
---
# King Arryn II
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[House of Sewick]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`

The only child of [[Blanche II]]. His two daughters, [[Charlotte II]] and [[Cece I]] both rule the united realm of Sembara and Tyrwingha.

%% killed by hobgoblins, daughter died of injuries from same attack; some small set of facts in the Sembaran  timeline %%

%%^Metadata:names:v1%%
- {"name": "Arryn II", "language": "Sembaran", "pronunciation": "AIR-in thuh SEK-und", "notes": "Proposed from the English branch of Sembaran's French-and-English analogue in [[Languages]]: preferred initial AIR, unstressed y as short i, first-syllable stress, and the ordinary spoken regnal number. French-influenced vowel and stress choices remain possible; no accepted subject-specific pronunciation is recorded.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: A modern retrospective genealogy of Arryn II and his successors; the succession wording is read as historical present, not a claim of simultaneous current rule.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: []`; no campaign knowledge was established in the reviewed sources.
- Normalized frontmatter without changing existing parsed values.
- Added a persistent name entry, `POV: modern`, and temporal coverage metadata.

### Validated judgments
- The shared comment is a source pointer to [[Timeline of Sembaran History]]; the death account is independently recorded there.
- The timeline contains unresolved seasonal chronology, so no exact day or new death date is inferred.

### Editorial assessment
**Underdeveloped** — The visible entry records family connections but omits Arryn II's defining role in the Third Hobgoblin War and the fatal attack that caused the succession. The smallest useful addition is a short account of his DR 1644 intervention and DR 1648 death, preserving unresolved seasonal chronology.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed complete pronunciation `AIR-in thuh SEK-und`. Proposed from the English branch of Sembaran's French-and-English analogue in [[Languages]]: preferred initial AIR, unstressed y as short i, first-syllable stress, and the ordinary spoken regnal number. French-influenced vowel and stress choices remain possible; no accepted subject-specific pronunciation is recorded. If accepted, copy it to frontmatter `pronunciation` and mark the primary name entry `documented`; otherwise revise the proposal.
- [ ] **Warning — coverage.established_fact_missing:** [[Timeline of Sembaran History]] records Arryn launching the DR 1644 attack on the [[Shattered Ice Clan]] at Charlotte’s urging and dying in a DR 1648 hobgoblin attack while inspecting the army near Wisford. [[Charlotte II]] and [[Cece I]] establish the successive queens. Add: “At the urging of [[Charlotte II]], Arryn led Sembara into the [[Third Hobgoblin War (Sembara)|Third Hobgoblin War]] in DR 1644. He was killed in a hobgoblin attack near [[Wisford]] in DR 1648; Charlotte was injured in the same attack and succeeded him briefly before [[Cece I]] took the united crowns.” The timeline remains marked for review and has inconsistent seasonal ordering, so retain year-level chronology pending human confirmation.
%%^End%%

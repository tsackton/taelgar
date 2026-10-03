---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Tollish
gender: female
died: 1659
born: 1571
name: Nicole Ardouin
affiliations:
  - {org: University of Tollen, type: member, title: Faculty}
whereabouts: Tollen
knownTo: []
dm_owner: none
dm_notes: none
POV: modern
---
# Nicole Ardouin
>[!info]+ Biographical Info  
> A [[Tollen|Tollish]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Nicole Ardouin was a Tollish cosmological and theological philosopher, most famous for her work on difficult or marginal planes, including the [[Far Realms]], the [[Nightmare Realm]], and [[Pandemonium]].

%%^Metadata:names:v1%%
- {name: Nicole Ardouin, language: unknown, pronunciation: "nih-KOHL ar-DOO-in", status: proposed, notes: "Proposed from the Tollish cultural context and its English analogue in [[Languages]]: ordinary Nicole, sounded r, ou as oo, and final in; the surname's syllabification and stress remain uncertain, and its source language is not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern retrospective reference to Nicole Ardouin's scholarship in the DR 1600s; the article does not currently describe the expedition from which she failed to return.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, made the filename-supplied name explicit, added `knownTo: []`, and recorded a retrospective modern viewpoint and proposed name pronunciation.

- Represented the existing Faculty affiliation as a `member` relationship with `title: Faculty`, preserving its recorded role.

### Validated judgments
- The note adequately identifies a historical scholar and her fields; a bounded account of her named works is an optional expansion.
- No local DM candidates were found; `dm_notes: none` is supported by the completed discovery gate.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Proposed pronunciation: `nih-KOHL ar-DOO-in`. [[Languages]] gives Tollish an English analogue with Germanic or Slavic loan words. The proposal uses ordinary Nicole, sounded `r`, `ou` as `oo`, and final `in`; surname syllabification and stress are uncertain. The Tollish cultural context does not establish the name’s language. Confirm a pronunciation before accepting it or copying it to frontmatter.
- [ ] **Warning — coverage.established_fact_missing:** [[Far Realms]] states that Ardouin never returned from a research expedition to the [[Marches of Enford]], and that this kept her work marginal. The biographical article omits this defining final event. Proposed addition: “Ardouin never returned from a research expedition to the [[Marches of Enford]], a disappearance that helped keep her work on the [[Far Realms]] marginal.” The source does not date the expedition or establish a cause of death; retain those uncertainties and do not silently equate disappearance with the recorded `died: 1659`.
%%^End%%

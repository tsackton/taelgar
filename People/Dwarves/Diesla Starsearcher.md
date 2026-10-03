---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
ancestry: null
campaignInfo:
  - {campaign: clee, type: met}
born: 1512
gender: female
name: Diesla Starsearcher
whereabouts:
  - {type: home, location: Ardith}
  - {type: home, start: 1670, location: Taviose}
  - {type: home, start: 1720-05-01, location: Asineau}
knownTo: [clee]
dm_owner: none
dm_notes: color
POV: 1720
---
# Diesla Starsearcher
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

[[Brot Starsearcher]]'s wife, a respected metalsmith in [[Taviose]]. A patient and loving companion to her somewhat scatterbrained spouse.

In spring 1720, she and Brot moved their workshop to [[Asineau]] and became its workshop masters.

%%^Metadata:names:v1%%
- {name: Diesla Starsearcher, language: unknown, pronunciation: DEE-ehs-lah STAR-sur-cher, notes: "Proposed adaptation using the Tolkien Dwarvish analogue in [[Languages]]; separate ee/eh vowels in Diesla and a plain-English reading of Starsearcher. The name's in-world language and accepted pronunciation are unrecorded.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1719–1720 account with earlier home metadata; the opening retains the Taviose description while the dated paragraph records the spring 1720 move to Asineau.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, canonicalized `campaignInfo` to `clee`, and added the matching `knownTo` code.
- Added a proposed name entry and a DR 1720 temporal viewpoint, preserving the visible prose and dated whereabouts.

### Validated judgments
- The marriage, metalsmith role, and move to become a workshop master provide a sufficient minor-person reference. The move is corroborated by [[Cleenseau - Session 29]] and [[Asineau Hirelings - Authored Turns]]; incidental craft commissions and conversations do not require a campaign log here.
- The multiple home entries validly retain origin and later residences; no date defect follows merely from their multiplicity.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise `DEE-ehs-lah STAR-sur-cher` in `Metadata:names:v1`. The Tolkien Dwarvish analogue in [[Languages]] motivates a cautious adaptation with separately sounded ee/eh vowels for `ie`, a full final ah, sounded s/l, and initial stress; the transparent English surname is read as written. These are proposed reading choices, not established in-world phonology. On acceptance, set `status: documented` and copy the accepted primary pronunciation to frontmatter. The name's in-world language remains `unknown`.
- [ ] **Warning — temporal.mixed_viewpoint:** The opening calls Diesla “a respected metalsmith in [[Taviose]]” without a historical qualifier, while the final paragraph and current whereabouts record her spring 1720 move to [[Asineau]], corroborated by [[Asineau Hirelings - Authored Turns]]. Clarify the opening without losing her former association: “[[Brot Starsearcher]]'s wife, a respected metalsmith formerly based in [[Taviose]]. A patient and loving companion to her somewhat scatterbrained spouse.” Retain the dated final paragraph. If date-filtered historical views are needed, the smallest later layer is a `%%^Date:1720-05-01%%` block around that final paragraph, using the move date already in this note's metadata; confirm the precise cutoff before adoption because the narrative source establishes spring rather than that exact day. No visibility block has been applied.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The existing `dm_notes: color` may reflect remembered or other off-vault information and has been preserved; retain it if useful private material remains, or explicitly authorize `dm_notes: none` if the shared record is complete.
%%^End%%

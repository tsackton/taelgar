---
headerVersion: 2023.11.25
lintedAt: "2026-08-28T16:53:46-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: null
campaignInfo:
  - {campaign: dufr, person: Wellby, type: "rescued from imprisonment in an aboleth's lair", date: 1748-10-14}
born: 1724
gender: female
name: Resenna
whereabouts:
  - {type: home, location: Medju}
  - {type: away, start: 1748-10-01, end: 1748-10-14, location: Outer Ocean}
  - {type: away, start: 1748-10-16, prefix: sea elf village in, location: Quanyi}
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: 1748
---
# Resenna
>[!info]+ Biographical Info  
> A [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Rescued from imprisonment in an aboleth's lair by [[Wellby]] on October 14th, 1748 in the [[Outer Ocean]] %%^End%%

![[resenna.png|right|320]]Young woman, from Medju. Apprentice to [[Arryn]]. Fled when he vanished into [[Mirror Realm]]; was trapped and enslaved by aboleth. Now dwelling with sea elves until aboleth curse can be removed. 

%%^Metadata:names:v1%%
- {name: Resenna, language: unknown, pronunciation: reh-SEN-ah, status: proposed, notes: "Proposed from spelling; no recorded pronunciation or established source-language rule was found."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 post-rescue portrait of Resenna, with her apprenticeship and enslavement summarized; her later recovery and whereabouts are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added `knownTo: [dufr]` from the existing campaign interaction.
- Added persistent name metadata with a proposed pronunciation and recorded the article's DR 1748 viewpoint and temporal coverage.

### Validated judgments
- The private evidence dossier supports the positive `dm_notes` attestation.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** `Resenna` has no accepted pronunciation in the note or searched sources. The persistent name entry proposes `reh-SEN-ah` from the spelling alone because no source-language rule is established. If accepted, copy `reh-SEN-ah` to frontmatter and change the entry to `status: documented`; otherwise replace it with the chosen pronunciation and derivation.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Session 1 - Wellby]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Session 2 - Wellby]]
%%^End%%

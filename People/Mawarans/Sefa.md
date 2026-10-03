---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Mawaran
gender: female
died: 1747-08-05
name: Sefa
whereabouts: Hamri
knownTo: [mawar]
dm_owner: none
dm_notes: none
POV: 1747
---
# Sefa
>[!info]+ Biographical Info  
> A Mawaran [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Sefa is an older woman, poor and addicted to [[Gatza]], who lives alone in the Drowned Flats, in Hamri. 

%%^Date:1747-08-05%%
She was killed by [[Azar the Lost]], in a misguided quest to restore his dead wife using the waters of the [[Sentient Ocean]].
%%^End%%

%%^Metadata:names:v1%%
- {name: Sefa, language: Mawaran, pronunciation: SEH-fah, status: proposed, notes: "Proposal from the Mawaran Arabic analogue in Languages: two syllables with plain s and f and unstressed final ah. Initial eh preserves the written e as an adapted vowel; the spelling does not establish an exact Arabic vowel or an in-world stress rule, so first-syllable stress remains provisional."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1747 portrait of Sefa living alone in Hamri before her recorded August death; the dated paragraph records her fate, while her earlier life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting and changed the campaign alias to `knownTo: [mawar]`.
- Added the missing article in “in a misguided quest.”
- Added a proposed name pronunciation and recorded `POV: 1747` with temporal coverage guidance.

### Validated judgments
- The note identifies this minor subject's circumstances and fate. [[Mawar Adventures Episode 02]] corroborates her death in Azar's lair; the place of discovery and restitution do not require a separate campaign recap here.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed `SEH-fah` in `Metadata:names:v1`. [[Languages]] gives Mawaran an Arabic analogue: plain s and f and an unstressed final ah support this two-syllable adaptation. Initial eh follows the written e, which does not establish an exact Arabic vowel, and first-syllable stress is provisional. If accepted, set `pronunciation: SEH-fah` in frontmatter and change the entry to `status: documented`; otherwise record the accepted reading.
- [ ] **Warning — temporal.date_scope:** The opening says Sefa “lives alone” without a cutoff, so that living state remains visible beside the paragraph recording her death. The note's `died: 1747-08-05` and existing death block provide a matching boundary. A minimal proposal is to wrap only the opening sentence in `%%^Date:1747-08-05b%%` and `%%^End%%`, leaving the existing death block unchanged. This visibility change requires human approval.

### DM evidence
- [[_DM_/_Mawar Confederacy/Ep 2/Mawar Ep 2 - DM Notes]]
%%^End%%

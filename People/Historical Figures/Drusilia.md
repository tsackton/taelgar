---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Drankorian
gender: female
died: 1
name: Drusilia
affiliations:
  - {org: Occulta Ludum}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: modern
---
# Drusilia
>[!info]+ Biographical Info  
> A [[Drankorian Empire|Drankorian]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`

%% lots of backstory around Fides Lucaris and Occulta Ludum that is not well incorporated into notes %% 

A Drankorian woman, presumably long dead, who at one point lived at the [[Edge of Echoes]].

%%^Metadata:names:v1%%
- {"name": "Drusilia", "language": "Drankorian", "pronunciation": "droo-SIH-lee-ah", "status": "proposed", "notes": "Classical-Latin-informed proposal from the Drankorian analogue in [[Languages]]: u is oo, s remains s, and i-a are separate vowels; the proposed short penultimate i gives antepenultimate stress. No source records the vowel lengths or exact in-world stress."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern retrospective identification of a Drankorian woman associated with the Edge of Echoes; her lifetime is undated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]`, persistent name metadata with a proposed pronunciation, and `POV: modern` with temporal guidance; normalized frontmatter.
- Added the explicit name already used by the title.

### Validated judgments
- Campaign knowledge is established by [[Session 86 (DuFr)]], while the author’s hidden backstory reminder remains unresolved.

### Editorial assessment
**Underdeveloped**. The visible biography identifies only a former resident of the Edge of Echoes. It omits the established account of her opposition to the Fides Lucaris agent and her presumed caretaking role for the Occulta Ludum, which explain why she has a reference entry. A brief attributed addition from Session 86 is the smallest useful addition.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `droo-SIH-lee-ah` in `Metadata:names:v1`. Classical-Latin-informed proposal from the Drankorian analogue in [[Languages]]: u is oo, s remains s, and i-a are separate vowels; the proposed short penultimate i gives antepenultimate stress. No source records the vowel lengths or exact in-world stress. If accepted, copy it to frontmatter and mark the entry `documented`.
- [ ] **Warning — coverage.established_fact_missing:** [[Session 86 (DuFr)]] records a dead Fides Lucaris agent’s testimony that Drusilia bound and killed her when she tried to free the captive elemental, and identifies Drusilia as the presumed caretaker for the Occulta Ludum. Candidate: `According to a [[Fides Lucaris spy|Fides Lucaris agent]] questioned after death, Drusilia bound and killed her when she tried to free the elemental at the [[Edge of Echoes]]. Drusilia was presumably the [[Occulta Ludum]]’s caretaker there.` Preserve both the testimonial attribution and the uncertainty about her office; no invented wider biography is needed.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: important`. The field may refer to remembered backstory or another off-vault source. Retain it unless the human confirms a different attestation.
%%^End%%

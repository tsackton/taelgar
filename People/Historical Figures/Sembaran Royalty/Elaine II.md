---
headerVersion: 2023.11.25
lintedAt: "2026-08-20T18:24:04-04:00"
lintVersion: "3.1"
tags: [person, status/check/mike, status/check/lint]
species: human
ancestry: Sembaran
born: 1673
gender: female
died: 1745
name: Elaine II
affiliations:
  - {org: House of Lils, type: primary}
  - {org: Tyrwingha, type: leader, title: Queen, start: 1713-09-12}
  - {org: Sembara, type: leader, title: Queen, start: 1720-06-15}
knownTo: [clee]
dm_owner: mike
dm_notes: none
POV: modern
---
# Elaine II
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her), of the [[House of Lils]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`

%% tagging check/mike just to confirm putting the gloss on her reign as a time of peace and prosperity should be commented out; Sembara 1720 - 1750 needs a little more thought before we should commit to that, IMO. I agree the vibe of Sembara is clearly fairly stable in the 1720-1749 timeframe, and I think it is sensible to commit to the House of Lis as it stands, but maybe soften the "her reign was a time of peace and prosperity" and the connection to Cece %%

The first monarch of the [[House of Lils]], descended from, Derik, the youngest son of [[Elaine I]], and [[Morgaine]], a Tyrwinghan [[Oracle of the Riven|oracle]]. She was succeeded by her son [[Arryn III]] in DR 1745.

%%

Her reign was a time of peace and prospertity, and an intentional throwback to the glorious years of [[Cece I]]. 

%%

%%
There are some notes for Cleenseau Campaign that I have not incorporated here, but nothing canonical yet
%%

%%^Metadata:names:v1%%
- {name: Elaine II, role: primary, language: Sembaran, status: inferred, notes: Sembaran regnal name inferred from the subject's dynasty and realms}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective summary of Elaine II's reigns through her death in DR 1745; the exact start of her Sembaran reign remains unresolved across sources.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Open findings

- [ ] **Error — consistency.cross_note:** The affiliations date Elaine II's Tyrwinghan reign from DR 1713-09-12 and her Sembaran reign from DR 1720-06-15. [[The Election of Elaine II]] records her election in Tyrwingha on DR 1713-06-03, while [[Cleenseau - Session 28]] records a Sembaran regnal shift on DR 1720-03-26 and [[Robert I]] records his death on DR 1720-06-15. Determine whether these are election, proclamation, coronation, or effective-reign dates, then align the affiliations and visible explanation without treating the session record as factually wrong.
- [ ] **Warning — coverage.established_fact_missing:** The visible biography omits the central succession history established by [[The Election of Elaine II]] and [[Timeline of Sembaran History]]: election as queen of Tyrwingha in DR 1713, designation as Robert I's Sembaran heir in DR 1718, and accession in DR 1720. After resolving the exact dates, add a concise paragraph covering those three transitions.
- [ ] **Suggestion — editorial.public_material_candidate:** The shared comment proposes describing her reign as peaceful and prosperous, and [[Arryn III]] independently supports that characterization while not supporting the stronger claim of an intentional return to Cece I's era. Copy-ready bounded candidate: `Her reign in Sembara is remembered as a period of peace and prosperity.`

### Applied changes

- Added `knownTo: [clee]`, persistent name metadata, and a modern retrospective temporal frame; `status/check/mike` remains unassessed.
%%^End%%

---
headerVersion: 2023.11.25
tags: [person, status/check/ai]
campaignInfo:
- {campaign: DuFr, date: 1748-12-30, type: met}
name: Thomas Hawke
born: 1716
species: human
ancestry: Tollender
gender: male
affiliations: [University of Tollen]
whereabouts: Tollen
lintedAt: "2026-08-19T01:07:33-04:00"
lintVersion: 2
dm_owner: tim
dm_notes: color
---
# Thomas Hawke
>[!info]+ Biographical Info  
> A [[Tollen|Tollender]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:DuFr%% Met by the [[Dunmar Fellowship]] on December 30th, 1748 in the [[Tollen|Free City of Tollen]] %%^End%%

![[thomas-hawke.png|right|400]]Thomas Hawke is Professor of Rhetoric, a playwright, and a rising star at the [[University of Tollen]], recognized more for his dramatic flair than his academic pursuits. He is a handsome man in his mid-30s, well-dressed and exuding confidence. 
## Overview
Born and raised in [[Tollen]], Thomas Hawke is an ambitious scholar at the [[University of Tollen]]. While he holds a lectureship in rhetoric, his true passion leans more towards drama than academia. He is captivated by the allure of legends and tales, and has a passion for stories he can borrow from in his plays. His work, notably the locally famous play "[[Luminastra's Gift]]," has showcased his potential and marked him as an influential figure in the theatrical world.
## Relationships
- **[[University of Tollen]]:** As a scholar and lecturer, he has forged deep connections within the University, making him a person of influence and significance.
## Rumors and Information
- Hawke's fascination with legends and tales is well-known; he is always seeking the most exotic tales and stories as fodder for his plays. 

%%SECRET[v2:5f8aec0976e7cbfc68fd9955a9cde47f]%%

%%^Metadata:names%%
version: 1
names:
  - {form: Thomas Hawke, role: primary, language: Tollish, languageStatus: inferred, pronunciationStatus: exception-obvious, derivation: unknown}
%%^End%%

%%^Lint%%
## Taelgar note lint
- Linted: 2026-08-19T01:07:33-04:00
- Linter version: 2
- Profile: person
- Article mode: current character-facing reference
- Temporal POV: apparently DR 1748, inferred from the dated DuFr meeting rather than declared by the article
- Inference confidence: medium
- POV suitability: needs human confirmation; the article's relative age wording depends on this choice
- Review signal: yes — `status/check/ai` is the live-trial stand-in; clear it after human review

### Open findings
- [ ] **Knowledge metadata:** `knownTo` is required for people but is absent. Session 82 establishes that the Dunmar Fellowship met Hawke; decide the exact supported value and whether later campaign knowledge changes it.
- [ ] **Temporal POV:** born in DR 1716, Hawke is 32 at the DR 1748 meeting, while the visible article calls him “in his mid-30s.” Either anchor a later POV or revise the relative age wording.
- [ ] **Name evidence:** Tollish is inferred from ancestry and residence, not documented as the source language of the name. Confirm or replace the inference.
- [ ] **Private attestation:** `dm_notes: color` asserts substantial off-page knowledge. A linter cannot verify the material in a person's head or outside Git.

### Applied changes
- Added the trial lint state and `status/check/ai`.
- Added a provisional naming block. No pronunciation was added: “Thomas Hawke” qualifies as an obvious ordinary-name exception.

### Evidence reviewed
- [[Session 82 (DuFr)]]; [[Session 98 (DuFr)]]; [[Luminastra's Gift]]; current note and private block
%%^End%%

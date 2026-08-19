---
headerVersion: 2023.11.25
tags: [event, status/check/ai]
name: Treaty of Valarin
DR: 1430
dm_owner: none
dm_notes: none
typeOf: treaty
tentativeReason: "unclear if this exists"
lintedAt: "2026-08-19T01:07:33-04:00"
lintVersion: 2
---
# The Treaty of Valarin
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_PageDatedValue")`

A treaty between the [[Istabor Alliance]] and [[Sembara]] establishing boundaries.

%% This does not have to be canonical, esp if say Istabor is rethought as something less "alliance-like"; there needs to be a reason why Sembara didn't expand further southward, but "well-established other people" could be the reason without a specific treaty %%

%%^Metadata:names%%
version: 1
names:
  - {form: Treaty of Valarin, role: primary, language: Common, languageStatus: inferred, pronunciationStatus: unresolved, derivation: descriptive}
  - {form: Valarin, role: name-component, language: unknown, languageStatus: unresolved, pronunciationStatus: unresolved, derivation: unknown}
%%^End%%

%%^Lint%%
## Taelgar note lint
- Linted: 2026-08-19T01:07:33-04:00
- Linter version: 2
- Profile: Worldbuilding / Tentative event
- Article mode: development proposal, not canonical event reference
- Temporal POV: proposes a DR 1430 event from an out-of-world design perspective
- Inference confidence: high
- POV suitability: suitable for Worldbuilding
- Review signal: yes — `status/check/ai` is the live-trial stand-in; clear it after human review

### Open findings
- [ ] **Adoption state:** the canonical Sembaran timeline links this treaty, while this note says its existence is unclear and the timeline's surrounding comment keeps parts of the chronology provisional. Decide whether the concept has been adopted, remains tentative, or should be replaced by a different explanation for Sembara's southern boundary.
- [ ] **Pronunciation and name language:** “Valarin” requires a pronunciation if retained, but its source language is unresolved. The English treaty-title frame does not supply that evidence.

### Applied changes
- Added the trial lint state, `status/check/ai`, and a naming block that separates the Common descriptive title from the unresolved “Valarin” component.

### Validated
- This note was not labeled incorrect, stale, or in cross-note conflict. Worldbuilding is allowed to be provisional or divergent; the finding is about human adoption state only.
- The existing `tentativeReason` and shared comment were preserved.

### Evidence reviewed
- [[Timeline of Sembaran History]]; current Worldbuilding note and comment
%%^End%%

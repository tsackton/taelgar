---
headerVersion: 2023.11.25
tags: [object]
name: Thunderbrand
typeOf: warhammer
subTypeOf: magical
ancestry: dwarven
lintedAt: "2026-08-19T01:07:33-04:00"
lintVersion: 2
dm_owner: none
dm_notes: none
---
# Thunderbrand
>[!info]+ Information  
> ([[Dwarves|dwarven]] magical warhammer)  
> `$=dv.view("_scripts/view/get_Affiliations")`

A powerful magical warhammer, of dwarven make, currently wielded by [[Adrik]]. It was lost in the [[Goldpeak Mines]] under [[Goldpeak Mountain]] for many years, with the magical shield [[Coldguard]], until both were recovered by the [[Silver Tempests]].

%%^Metadata:names%%
version: 1
names:
  - {form: Thunderbrand, role: primary, language: Common, languageStatus: inferred, pronunciationStatus: exception-obvious, derivation: compound}
%%^End%%

%%^Lint%%
## Taelgar note lint
- Linted: 2026-08-19T01:07:33-04:00
- Linter version: 2
- Profile: campaign object
- Article mode: current campaign reference
- Temporal POV: unstated; “currently wielded” is only securely evidenced through the recorded Great Library material
- Inference confidence: high
- POV suitability: needs an anchor because ownership is time-sensitive
- Review signal: yes — `status/check/ai` is the live-trial stand-in; clear it after human review

### Open findings
- [ ] **Temporal POV:** replace or date “currently wielded by Adrik,” or declare the Great Library article POV. The problem is not an edit timestamp; it is that later campaign invention could change ownership.
- [ ] **Classification:** `subTypeOf` is deprecated by current metadata rules. Decide the supported `typeOf`/tag representation rather than mechanically translating it.
- [ ] **Name evidence:** Common compound formation and the plain-English pronunciation exception are inferred, not documented as an in-world etymology.

### Applied changes
- Added the trial lint state, `status/check/ai`, and a provisional naming block.
- Corrected “Goldpeak Mines mines” to “Goldpeak Mines.”

### Validated
- `knownTo` is not required for objects in this phase.
- Great Library Arc 1 establishes recovery and empowerment; Arc 4 still places Thunderbrand with Adrik, but that does not make “currently” permanently safe.

### Evidence reviewed
- [[Great Library Session Notes - Arc 1]]; [[Great Library Session Notes - Arc 4]]; [[Coldguard]]; current note
%%^End%%

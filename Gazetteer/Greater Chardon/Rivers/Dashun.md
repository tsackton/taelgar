---
headerVersion: 2023.11.25
tags: [place, status/check/name, status/check/ai]
typeOf: waterway
whereabouts: Chardonian Empire
dm_owner: none
dm_notes: none
typeOfAlias: river
pronunciation: DAH-shoon
lintedAt: "2026-08-19T01:07:33-04:00"
lintVersion: 2
---
# Dashun
*(DAH-shoon)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A minor river in the [[Coastlands]], south of the [[Chasa]], flowing from the [[Chardon Hills]] to the [[Gulf of Chardon]].

%%^Metadata:names%%
version: 1
names:
  - {form: Dashun, role: primary, language: Old Northros, languageStatus: documented, pronunciationStatus: documented, pronunciation: DAH-shoon, derivation: borrowing, sourceForm: dāšûn, sourceLanguage: Old Northros, meaning: warm spring, certainty: documented}
%%^End%%

%%^Metadata:map%%
version: 1
locations:
  - {role: source, feature: Chardon Hills, map: unregistered, geometry: point, locator: 13.07.F16}
  - {role: outlet, feature: Gulf of Chardon, map: unregistered, geometry: point, locator: 13.07.C18}
%%^End%%

%%^Lint%%
## Taelgar note lint
- Linted: 2026-08-19T01:07:33-04:00
- Linter version: 2
- Profile: minor river
- Article mode: current encyclopedic geography
- Temporal POV: stable modern geography; no time-sensitive claim detected
- Inference confidence: high
- POV suitability: suitable
- Review signal: yes — `status/check/ai` is the live-trial stand-in; clear it after human review

### Open findings
- [ ] **Map registry:** the source and outlet hexes are preserved, but their map is not identified. Register the coordinate system before treating them as machine-actionable.
- [ ] **Existing name review:** `status/check/name` remains unresolved. The note now records the evidence clearly, but only a human should decide whether that older review tag can be cleared.

### Applied changes
- Added the trial lint state and `status/check/ai`.
- Migrated the existing etymology and endpoint comment into provisional structured naming and map blocks without changing its meaning.
- Removed trailing whitespace from the one-sentence description.

### Evidence reviewed
- Current note and its pre-existing shared comment; [[Chardon Hills]]; [[Gulf of Chardon]]; [[Background/Languages]]
%%^End%%

---
headerVersion: 2023.11.25
tags: [place, status/check/ai]
displayDefaults: {defArt: ""}
dm_notes: important
dm_owner: tim
typeOf: building
typeOfAlias: tower
whereabouts:
- {type: home, location: Circular Island, startFilter: "1", linkText: "on"}
lintedAt: "2026-08-19T01:07:33-04:00"
lintVersion: 2
---
# Apollyon's Tower
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Apollyon's Tower is a black marble spire on the coast of the [[Circular Island]], once a stronghold and retreat of the Drankorian emperor [[Apollyon]], a place of dark study and craft. The tower itself is almost 250 feet tall, with a main section that rises 140 feet from the ground, and battlements and a tower extension that rise another 100 feet, capped with a platform open to the sky. After the [[Fall of Drankor]], the tower stood abandoned and warded, looming over the island’s storm‑lashed shore. 

%%^Campaign:DuFr%%
In DR 1749 the [[Dunmar Fellowship]] assaulted the ruin, uncovering its forge, libraries, and throne room, and carrying away the treasures now catalogued as [[Apollyon's Tower Treasure]].
%%^End%%

%%SECRET[v2:336d2b6a742073ad1667272cfcf6ff5e]%%

%%^Metadata:names%%
version: 1
names:
  - {form: "Apollyon's Tower", role: primary, language: Common, languageStatus: inferred, pronunciationStatus: unresolved, pronunciationSource: Apollyon, derivation: descriptive}
  - {form: Apollyon, role: name-component, language: unknown, languageStatus: unresolved, pronunciationStatus: unresolved, derivation: unknown}
%%^End%%

%%^Lint%%
## Taelgar note lint
- Linted: 2026-08-19T01:07:33-04:00
- Linter version: 2
- Profile: canonical place with campaign and SECRET material
- Article mode: post-Fall encyclopedic reference plus a DuFr event block and private pre-session design
- Temporal POV: the public ruin description spans DR 1059 to the DR 1749 assault; the campaign block is explicitly dated
- Inference confidence: high
- POV suitability: suitable, but later established discoveries have overtaken the visible article's level of detail
- Review signal: yes — `status/check/ai` is the live-trial stand-in; clear it after human review

### Open findings
- [ ] **Coverage:** Sessions 109–110 and 113 establish defensive constructs, the forge and ritual spaces, and evidence used to understand and destroy Apollyon's phylactery. The visible note mentions only the forge, libraries, throne room, and removed treasure.
- [ ] **Internal reconciliation:** the SECRET block mixes pre-session possibilities, encounter planning, and details that later became established. Reconcile it against the sessions, but do not expose private material merely because it is supported.
- [ ] **Pronunciation inheritance:** “Tower” needs none, but the title depends on the pronunciation of “Apollyon,” which is absent from the base person note.
- [ ] **Name evidence:** the Common descriptive title is inferred; the source language and etymology of “Apollyon” are unresolved.
- [ ] **Private attestation:** `dm_notes: important` cannot be verified from tracked files alone.

### Applied changes
- Added the trial lint state, `status/check/ai`, and a naming block separating the descriptive title from its unresolved name component.
- Normalized the campaign marker from `dufr` to `DuFr` and harmless frontmatter spacing.
- Made no changes inside the SECRET block.

### Validated
- The SECRET block is current private syntax, not legacy comment material.
- No universal `campaign` or `knownTo` field was required for this place note.

### Evidence reviewed
- [[Session 109 (DuFr)]]; [[Session 110 (DuFr)]]; [[Session 113 (DuFr)]]; [[Circular Island]]; current visible note, campaign block, and SECRET block
%%^End%%

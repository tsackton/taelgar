---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/gl, status/check/lint]
species: halfling
gender: male
name: Finoc Small
affiliations:
  - {org: The Wandering Toad, title: Proprietor}
whereabouts:
  - {type: home, location: Voltara}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1748
---
# Finoc Small
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> 

![[finoc-small.png|right|300]]An unusually tall and cheerful halfling, and the owner of [[The Wandering Toad]], an inn in [[Voltara]] known for wild game, mushrooms, and ale. [[Brelith]] apprenticed with the chef there before opening [[The Hero's Feast]].

%%^Metadata:names:v1%%
- {"name": "Finoc Small", "language": "unknown", "pronunciation": "FEE-nohk SMAWL", "notes": "Tentative adaptation using the qualified Halfling analogue in [[Languages]] (Igbo, but may change or be diverse): clear ee for i and oh for o inform the proposal. The final c as k and first-syllable English guide stress remain spelling-based choices, not established Igbo or Halfling rules; Small is the ordinary English surname. The name language is not established.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Finoc as proprietor of the Wandering Toad, after Brelith's apprenticeship and restaurant opening; later proprietorship is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized frontmatter ordering and collection formatting.
- Added the primary name entry and persistent temporal coverage metadata.
- Normalized `knownTo: [gl]` to `knownTo: [grli]` and added `POV: 1748`.

### Validated judgments
- The note sufficiently identifies the proprietor and his inn; [[Great Library Session Notes - Arc 4]] already supports the included Brelith apprenticeship and restaurant connection.
- `status/gameupdate/gl`: not assessable as a remaining task. The visible apprenticeship information is already captured, but the tag’s intended outstanding update is not specified; preserve the tag for human disposition.
- No local-only candidate evidence was found for the negative `dm_notes` attestation.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name entry proposes **FEE-nohk SMAWL**. [[Languages]] gives the qualified Halfling analogue “Igbo, but may change or be diverse”: clear ee for i and oh for o inform this tentative adaptation. Reading final c as k and supplying first-syllable English guide stress are unresolved spelling-based choices, not established Igbo or Halfling rules; Small is the ordinary English surname. The proposal therefore needs explicit name-specific confirmation. If accepted, copy the proposed pronunciation to frontmatter and change the name entry to `status: documented`; otherwise revise the proposal and its derivation. The name language remains `unknown` pending evidence.
%%^End%%

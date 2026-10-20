---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/text, status/check/lint]
typeOf: realm
typeOfAlias: duchy
campaignInfo: null
name: Duchy of Wisford
whereabouts: Sembara
dm_owner: mike
dm_notes: important
POV: modern
---
# The Duchy of Wisford
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

One of the original ancient duchies that formed Sembara. Still a powerful and rich land, with significant agricultural wealth including cattle, wheat, and cheese production.

As of 1720, the duke is [[Jacques Bellemont]]. Like the dukes of other ancient duchies, he has considerable authority within his duchy, while the army follows a separate royal command structure.

%%
Needs a vibes-based update based on in-game info from Cleenseau. Minimal canonical details though; also see [[Heartlands]] and [[Timeline of Sembaran History]] 
%%

%%^Metadata:names:v1%%
- {"name": "Duchy of Wisford", "language": "unknown", "pronunciation": "DUH-chee of Wis-ford", "status": "documented", "notes": "Uses the accepted Wis-ford pronunciation in [[Wisford]] with the ordinary English title Duchy of; the source does not establish the name’s language."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern origins and agricultural wealth, with Jacques Bellemont’s leadership explicitly anchored to DR 1720; the later crisis and its consequences await coverage disposition.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added persistent name and temporal metadata; preserved header versions, human attestations, and non-lint statuses.

### Validated judgments
- `status/cleanup/text` is supported by the existing update reminder and the concrete coverage gaps and is preserved.
- The shared comment is an editorial research reminder rather than a developed public account; the local DM-attestation gate does not apply to `dm_owner: mike`.

### Editorial assessment
**Underdeveloped** — The powerful duchy is identified by wealth and an ancient origin, but its core geography and ducal seat are missing, and the DR 1720 military and political rupture is absent. The smallest useful scope is a short geographical identification and a dated account of the crisis, preserving reported news as reported and leaving later outcomes unresolved.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The article does not locate the duchy within Sembara or identify its seat. [[Heartlands]] places it around the Wistel and south to the Enst, while [[Wisford]] identifies the traditional ducal seat. Candidate: “The duchy lies around the [[Wistel]] and extends south to the [[Enst]]. Its largest city and traditional ducal seat is [[Wisford]].”
- [ ] **Warning — coverage.later_material_change:** The generic distinction between ducal authority and royal army command does not capture the DR 1720 rupture. [[Army of the South]] records its dispersal and surviving soldiers serving an informal army under Jacques; [[Cleenseau - Session 24 - Original]] reports his treason sentence and withdrawal toward Fellburn with troops. Candidate: “During the undead crisis of DR 1720, surviving soldiers of the [[Army of the South]] served in an informal force under [[Jacques Bellemont]]. By early March, reports said that the duke had been sentenced to death for treason and was withdrawing from [[Embry]] toward [[Fellburn]] with his troops.” Add the dated account and review temporal framing, defer it for a human game-update disposition, or explicitly preserve the earlier account. Do not infer a settled civil-war outcome.
%%^End%%

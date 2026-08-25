---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T23:55:52-04:00"
lintVersion: "3.5"
tags: [place, status/stub, status/check/name, status/check/lint]
typeOf: topographical feature
typeOfAlias: mountain range
name: Mawar Mountains
aliases: [Dahrat]
whereabouts: Mawakel Peninsula
dm_owner: tim
dm_notes: important
POV: modern
---
# The Mawar Mountains
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`


%% 
the mountains between the [[Mawakel Peninsula]] and the [[Tawir Forest]]
%%

%% naming gloss:

Drankorian imperial surveys identified the Mawar Mountains, but did not explore/survey the peninsula extensively

Mawaran local name is:
Dahrat (DAH-raht) 

other options:
Dahraz (dah-RAHZ) Qahrat (KAH-raht)
%%

%%^Metadata:names:v1%%
- {name: Mawar Mountains, role: primary, language: Common, pronunciation: mah-WAHR MOUN-tinz, notes: "Proposed from the Mawaran Arabic analogue for the Mawar name component; the English generic follows ordinary Common pronunciation.", status: proposed}
- {name: Dahrat, role: local, language: Mawaran, pronunciation: DAH-raht, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography; the timing and extent of the Drankorian surveys mentioned in the naming notes are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized frontmatter field order and collection formatting and added the explicit subject name.
- Added persistent name metadata for Mawar Mountains and the documented local form Dahrat.
- Added persistent temporal POV metadata.

### Validated judgments
- The existing `status/stub` tag remains supported because the note has no visible reference prose.
- The independent `status/check/name` state was preserved without using it as name evidence.

### Editorial assessment
**Underdeveloped**. The visible article has no public account of the range's established geography or regional role; all authored subject matter remains inside shared nonpublic comments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent primary-name entry proposes `mah-WAHR MOUN-tinz`. The Mawaran analogue in [[Languages]] is Arabic, supporting `mah-WAHR` for the Mawar component, while “Mountains” follows ordinary Common pronunciation. Accept, revise, or reject the proposal and copy an accepted primary pronunciation to frontmatter.
- [ ] **Warning — coverage.established_fact_missing:** The note's hidden geography fragment, [[Timeline of the Mawar]], and [[Sulqat]] establish a central public account that the visible article omits: the range lies between the [[Mawakel Peninsula]] and [[Tawir Forest]], isolates the peninsula from the continental interior, and forms the Sulqat's headwaters. Candidate: `The Mawar Mountains rise between the [[Mawakel Peninsula]] and the [[Tawir Forest]], cutting the peninsula off from the continental interior. The [[Sulqat]] flows from the range toward the [[Slate Sea]].`
- [ ] **Suggestion — editorial.public_material_candidate:** The shared hidden passage `the mountains between the [[Mawakel Peninsula]] and the [[Tawir Forest]]` is a coherent public-safe geographic description rather than DM-only material. Candidate: `The Mawar Mountains lie between the [[Mawakel Peninsula]] and the [[Tawir Forest]].`
- [ ] **Suggestion — dm.notes_no_local_evidence:** No local-only `_DM_` notes were found for the positive `dm_notes: important` attestation. Verify whether the attestation refers to off-vault or remembered material; do not remove it automatically.
%%^End%%

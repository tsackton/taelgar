---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {linkText: "on", ltPlace: "on"}
tags: [place, status/check/name, status/check/lint]
typeOf: grassland
aliases: [plains south of Tokra, Sukal Lands, Sukalan]
whereabouts: Central Dunmar
dm_owner: tim
dm_notes: color
POV: modern
---
# The Sukal Plains
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

South of the city of [[Tokra]], the land grows increasingly arid, with little rain even during the monsoon season. The [[Hara]] is the lifeblood of this land. 

To the west, the intermittent streams that flow from the [[Copper Hills]], and the [[Sukal]], support a variety of drought-resistant plants, and provide grazing habitat in wide riparian valleys. To the east, the land turns to arid scrublands as it rises to meet the [[Garamjala Plateau]]. 

%% names
Standard cartographic name in Chardon is the Sukal Plains. In Dunmar would often be referred to as the Sukalan, translated as the Sukal Lands or Sukal Country
%%

%%^Metadata:names:v1%%
- {"name": "Sukal Plains", "role": "primary", "language": "unknown", "pronunciation": "su-KAHL PLAYNZ", "notes": "The river [[Sukal]] records su-KAHL; the proposal retains that component and gives Plains its ordinary English reading. The complete regional name has no recorded pronunciation. The authored naming comment identifies this as the standard cartographic name in Chardon without establishing its source language.", "status": "proposed"}
- {"name": "Sukalan", "role": "local", "language": "unknown", "pronunciation": "su-KAHL-uhn", "meaning": "Sukal Lands or Sukal Country", "notes": "The authored naming comment describes this form as Dunmari usage and gives the translations, but it has not been adopted into visible prose. The proposal retains the accepted su-KAHL component in [[Sukal]] and treats the final an as an unstressed uhn, preferring a Hindi-like schwa under the Dunmari Hindi-or-other-Indo-Iranian guidance in [[Languages]]. A more open Persian-like ahn is possible; exact vowel quality and the language of this name remain unestablished.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern description of the arid plains south of Tokra; earlier geography before the upheavals of the Great War is outside the article.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting, preserving `headerVersion` and explicitly quoting the existing `on` display prepositions. [[Display Control]] defines `linkText` and `ltPlace` as prepositions; quoting prevents YAML 1.1 from converting the intended text to booleans.
- Added persistent name metadata, preserving the authored naming account as unadopted context and recording proposed pronunciations.
- Added `POV: modern` and persistent temporal coverage notes.
- Corrected “refered” to “referred” in the naming comment.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The complete names have no accepted pronunciation. Review the persistent proposals `Sukal Plains: su-KAHL PLAYNZ` and `Sukalan: su-KAHL-uhn`. [[Sukal]] supplies the accepted component `su-KAHL`; the first proposal adds ordinary English “Plains.” The local form preserves that component and prefers an unstressed Hindi-like final schwa under the Dunmari analogue in [[Languages]], while a Persian-like final “ahn” is also possible. Exact local vowel quality is unestablished. Accept or revise each proposed entry; an accepted primary pronunciation can be copied to frontmatter as `pronunciation: su-KAHL PLAYNZ`.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The scan and bounded variant search covered Sukal Plains, Sukal Lands, Sukalan, and plains south of Tokra. Retain or revise the human attestation after checking off-vault or unrecorded information.
- [ ] **Suggestion — editorial.public_material_candidate:** The authored `%% names` comment preserves a coherent naming account absent from the visible article, but ordinary comments are noncanonical. Human adoption would explain the region's existing aliases and local usage. Proposed public addition: “In Chardon, this region is known as the Sukal Plains. In Dunmar, it is often called Sukalan, translated as ‘Sukal Lands’ or ‘Sukal Country’.” Approve or revise that account before adding it; afterward, remove only duplicated naming explanation from the comment while retaining distinct editorial guidance.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: lizardfolk
born: 1517
gender: male
name: Erdu
whereabouts: Ganboa
knownTo: [clee]
dm_owner: none
dm_notes: color
POV: 1719
---
# Erdu
>[!info]+ Biographical Info  
> A [[Lizardfolk|lizardfolk]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[lizardfolk-erdu.png|right|320]]The spokesperson for the village of [[Ganboa]] when dealing with humans. Older, with graying scales. Has a relatively low opinion of humans, all things considered. His family has lived along the Enst for hundreds of years (he says), and he is skeptical of [[Sembara|Sembaran]] claims to the land. 

%%^Date:1719%%
The death of his brother [[Edur]] by giant spiders has further soured his opinion of humans. 
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Erdu", "language": "unknown", "pronunciation": "EHR-doo", "status": "proposed", "notes": "Basque-informed proposal using the Lizardling cultural analogue in Languages: e as eh, u as oo, and r before d as a pronounced rhotic. Initial stress is provisional; the exact personal-name language is not recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1719 portrait of Ganboa’s older spokesperson, including his response to his brother’s death; the later DR 1720 defense agreement is not yet represented.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added knownTo: ["clee"].
- Added persistent name and temporal-viewpoint metadata.

### Validated judgments
- [[Ganboa]], [[Edur]], and the Cleenseau records support the existing spokesperson, family and campaign identity.
- The note already performs its concise reference role; the later defense agreement is a separate coverage decision.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm `EHR-doo` for Erdu. The proposal follows [[Languages]]’ Basque analogue for the Lizardling cultural context: eh for e, oo for u, and a pronounced r before d, with provisional initial stress. The personal-name language and in-world stress are not explicitly recorded. After acceptance, copy the value to frontmatter and mark the entry documented.

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. It may reflect remembered information or another off-vault source, so the attestation is unchanged.

- [ ] **Warning — coverage.later_material_change:** [[Cleenseau - Session 29]] establishes that in DR 1720 Erdu agreed to coordinate Ganboa’s defense with Asineau. That durable responsibility materially qualifies a portrait framed only by distrust of humans. Decide whether to update the article and POV, defer with the appropriate status/gameupdate/clee tag, or intentionally retain the DR 1719 snapshot; the linter has not changed any game-update tag. Copy-ready addition if adopted: “In DR 1720, Erdu agreed to coordinate [[Ganboa]]’s defense with [[Asineau]].” Keep that dated change distinct from the earlier response to Edur’s death.
%%^End%%

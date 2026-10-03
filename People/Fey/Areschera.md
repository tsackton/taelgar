---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/clee, status/check/lint]
species: fey
gender: female
died: 1720-02-21
name: Areschera
whereabouts:
  - {type: home, location: Duskmire}
  - {type: away, location: Veltor, start: 1720-01-04, end: 9999}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Areschera
>[!info]+ Biographical Info  
> A [[Fey|fey]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[areschera.jpg|right|400]]A servant of [[Lord Umbraeth]], and a shapeshifter. Mischievous and cruel, she especially enjoys using her disguises and shapeshifting to bring ruin to mortals.

%%
She was a major villain for two sessions in the Cleenseau campaign, so some color and game mechanics information was developed for that.

She was a key participant in a more complex plot of Umbraeth's which is not captured in Obsidian outside my DM notes, but is not very relevant to her life prior to coming to Veltor (whereabouts dates are accurate)

%%

%%^Metadata:names:v1%%
- {"name": "Areschera", "language": "unknown", "pronunciation": "ah-res-KEH-rah", "status": "proposed", "notes": "Greek-informed proposal using the qualified Sylvan guidance in [[Languages]]: open ah vowels, short e vowels, s followed by a hard k for sch, and provisional penultimate stress. The guidance supplies no fixed Sylvan phonology or stress rule; the name language itself is not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 portrait of Areschera as an active shapeshifting servant of Umbraeth, before her death on February 21; her Veltor infiltration and death are not yet narrated in the visible body.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, added the explicit subject name and Cleenseau knowledge, and recorded name and temporal metadata.

### Validated judgments
- Preserved the shared comment as DM planning/provenance. Local dm_notes evidence review does not apply to dm_owner: mike.
- The status/gameupdate/clee tag remains pending the human choice to update, defer, or preserve the pre-death portrait; no status tag was changed.

### Editorial assessment
**Underdeveloped** — The visible sentence identifies a cruel shapeshifting servant but omits her defining Veltor impersonations, the resulting murder and false accusation, and her exposure and death. A brief sourced account of those consequences would make the reference usable without reproducing the sessions.

### Open findings

- [ ] **Warning — coverage.later_material_change:** [[Juliana Westby]] establishes that Areschera killed Lambert while impersonating Tobias; [[Cleenseau - Session 19]] establishes her murder and replacement of Marguerite, exposure, and death on February 21, DR 1720. These are defining consequences of her use of shapeshifting, currently absent from the body even though death is recorded in metadata. Choose an updated account, defer with the existing game-update tag, or intentionally preserve the earlier portrait and disposition that tag. Copy-ready proposal, with a date boundary requiring human approval:

  ```markdown
  %%^Date:1720-02-21%%
  In early DR 1720, Areschera murdered and replaced [[Marguerite Deschamps]] in [[Veltor]]. She also impersonated [[Tobias of Cranford]] while murdering [[Lambert Talwrey]], nearly causing Tobias to be executed for the crime. The [[Heroes of Cleenseau]] exposed her, and she was killed on February 21.
  %%^End%%
  ```

- [ ] **Warning — metadata.names_unresolved_status:** Review the persistent pronunciation proposal `ah-res-KEH-rah`. [[Languages]] gives Sylvan no fixed analogue, while noting that many existing fey names use Classical Greek and that Polynesian or Hawaiian inspiration is possible. This proposal uses the Greek option: open ah vowels, short e vowels, `sch` as s plus a hard k, and provisional penultimate stress. These are suggested adaptations rather than an adopted Sylvan rule; the source language and stress are not established. Accept and copy the primary pronunciation to frontmatter, or replace the proposal.
%%^End%%

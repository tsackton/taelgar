---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
displayDefaults: {endStatus: killed in battle, dPast: "<endstatus:U> by [[Heroes of Cleenseau|The Heroes of Cleenseau]] on <enddate>"}
tags: [person, status/check/lint]
species: ogre
gender: male
died: 1719-12-06
name: Wakog
whereabouts: "Wakog's Camp"
knownTo: [clee]
dm_owner: none
dm_notes: color
POV: modern
---
# Wakog
>[!info]+ Biographical Info  
> An ogre (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[wakog.jpg|right|320]]An ogre of unclear origin. 
%%^Date:1719-10-30%%
Managed to organize a small horde of orcs in the northern parts of the [[Duchy of Maseau]], and attempted to overrun [[Cleenseau]], but was stopped by the [[Heroes of Cleenseau]].
%%^End%%

%% Most of the color is in [[Guy de Varan's Story]] %%

%%^Metadata:names:v1%%
- {name: Wakog, language: unknown, pronunciation: WAH-kog, status: proposed, notes: "Cautious spelling-based proposal with first-syllable stress; no name-specific pronunciation or established name language was found in the consulted sources."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern retrospective identification of Wakog, with his DR 1719 warband and defeat confined to the dated passage and death metadata.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, recorded the explicit name, and added `knownTo: [clee]`.
- Added a primary name entry with a spelling-based pronunciation proposal.
- Recorded a supported temporal viewpoint and persistent temporal notes.

### Validated judgments
- [[Cleenseau - Session 05]] and [[Battle Against Wakog]] corroborate the recorded death and defeat on December 6, DR 1719.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `WAH-kog`. This is a cautious spelling-based proposal with first-syllable stress, ah in the first syllable, and a short o in the second; no established name language or stronger pronunciation guide was found. Accept into frontmatter and mark the name entry documented, or provide the intended reading.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. [[Guy de Varan's Story]] is already a shared source, so it does not by itself establish information remaining only in private material. Retain `color` if other useful private information exists; otherwise a human can set `dm_notes: none`.
- [ ] **Suggestion — temporal.date_block_scope:** The `Date:1719-10-30` block already includes Wakog being stopped by the Heroes, but [[Cleenseau - Session 05]] dates that victory to December 6. It currently reveals the outcome too early. The smallest safe proposal is to change the enclosing marker to `%%^Date:1719-12-06%%`, retaining the existing paragraph and end marker. This visibility change is proposal-only.
%%^End%%

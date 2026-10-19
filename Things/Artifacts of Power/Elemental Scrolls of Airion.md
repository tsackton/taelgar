---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:07:38-04:00"
lintVersion: "3.5"
tags: [object, status/check/lint]
typeOf: scroll
name: Elemental Scrolls of Airion
knownTo: [grli]
dm_owner: tim
dm_notes: important
POV: modern
---
# The Elemental Scrolls of Airion
>[!info]+ Information  
> (scroll)  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Elemental Scrolls of Airion are four legendary scrolls of elemental power crafted by the wizard [[Airion |Airion Mistspeaker]] before the [[Great War]], but lost amid the upheavals of the [[Blood Years]]. The four scrolls are known as the [[Flamekeeper Scroll]], the [[Stonemaster Scroll]], the [[Skyborn Scroll]], and the [[Deepwater Scroll]]. 

%%^Date:1747%%
In DR 1747, they became the subject of a long search by the [[Great Library]]. A group of treasure seekers, who would later become known as the [[Silver Tempests]], were hired by [[Lyra|Archivist Lyra]] of the [[Great Library]] to recover these scrolls, from various locations associated with [[Airion]] in [[Greater Voltara]] and environs. They succeeded, and all four scrolls were returned to [[Chardon]] in the summer of DR 1747. 
%%^End%%

%% Exactly what they do or why they are important was never decided. %%

%%^Metadata:names:v1%%
- {"name": "Elemental Scrolls of Airion", "language": "unknown", "pronunciation": "el-uh-MEN-tul SKROHLZ uhv AIR-ee-on", "status": "proposed", "notes": "The Airion component follows the documented AIR-ee-on in [[Airion]]; the remaining words use ordinary English readings. The complete compound pronunciation remains proposed."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern retrospective reference prose; the existing DR 1747 date block records the scrolls' recovery separately.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the explicit name, knownTo: [grli], a proposed complete-name pronunciation, and broadly modern temporal metadata.

### Validated judgments
- The existing DR 1747 date block is preserved; [[Great Library Session Notes - Arc 1]] corroborates the recovery sequence.

### Editorial assessment
**Underdeveloped** — The collection has a documented creator, membership, and recovery history, but no central account of what its elemental powers do or why those powers matter. Define the shared purpose and the four elemental distinctions in a short artifact description; the existing comment explicitly leaves these decisions uninvented.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `el-uh-MEN-tul SKROHLZ uhv AIR-ee-on` in the name block. The component `AIR-ee-on` is documented in [[Airion]]; the remaining words use ordinary English readings. This is a proposed complete compound, not a newly established language rule. If accepted, set the entry to `status: documented` and copy the complete pronunciation to frontmatter.

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The current `important` attestation may refer to remembered or off-vault material and remains unchanged.

- [ ] **Suggestion — editorial.note_underdeveloped:** The authored comment says that what the scrolls do and why they matter was never decided. [[Great Library Session Notes - Arc 1]] makes their recovery the central quest and calls the Skyborn Scroll a powerful artifact, but does not establish usable powers. Decide a short shared function and the elemental distinctions before adding reference prose; do not infer spell effects from the scroll names.
%%^End%%

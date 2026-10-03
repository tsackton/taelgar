---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: giant
subspecies: cursed
campaignInfo: []
born: null
gender: male
name: Vondar
whereabouts:
  - {type: home, location: null}
  - {type: home, start: 1700, location: Amberglow}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Vondar
>[!info]+ Biographical Info  
> A [[Giants|giant]] (cursed) (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% Amberglow home whereabouts, start: 1700 — date uncertain %%

A cursed giant who guards the passes from [[Shimmersong]] into [[Amberglow]], asking for a toll of a memory in order to pass. Killed, but presumably not permanently, by [[Seeker]] and friends.

%%^Metadata:names:v1%%
- {name: "Vondar", language: "unknown", pronunciation: "VON-dahr", notes: "Proposed using the Old Norse analogue in Languages for Giant: initial stress, short rounded o, open a, and a tapped or rolled final r. The name language and exact in-world phonology are not recorded.", status: "proposed"}
- {name: "Vondar One-Eye", role: "epithet", language: "unknown", pronunciation: "VON-dahr WUN-eye", notes: "The complete form is recorded in Session 65 (DuFr); the Vondar component uses the proposed Old Norse-informed reading above, followed by the ordinary English epithet.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the DR 1748 encounter with Vondar in Amberglow and its immediate aftermath; his possible return after being killed remains explicitly uncertain.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added knownTo: [dufr], supported name forms, and the DR 1748 encounter viewpoint.
- With explicit user approval, moved the existing date-uncertainty annotation below the complete header, retaining its association with the Amberglow home whereabouts start: 1700, and normalized frontmatter without changing its values.

### Validated judgments
- The short reference captures Vondar's defining toll and uncertain fate; Session 65 corroborates the encounter.
- The uncertainty comment attached to the Amberglow start date is preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise `VON-dahr` and the full epithet form `VON-dahr WUN-eye`. [[Languages]] gives Giant an Old Norse analogue; this proposal uses initial stress, short rounded o, open a, and a tapped or rolled final r. The epithet is recorded in [[Session 65 (DuFr)]] and is read as ordinary English. Exact name language and in-world phonology are not recorded. If accepted, set `pronunciation: VON-dahr` in frontmatter and mark the corresponding name entries documented.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: important`. Preserve it if useful information remains in memory or another off-vault source; change it only by human decision.
%%^End%%

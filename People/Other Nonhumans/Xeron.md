---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: aboleth
campaignInfo:
  - {campaign: dufr, person: Riswynn, type: discovered, date: 1748-05-10}
name: Xeron
whereabouts:
  - {type: home, location: Yuvanti Mountains}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: modern
---
# Xeron
>[!info]+ Biographical Info  
> An aboleth  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Discovered by [[Riswynn]] on May 10th, 1748 in the [[Yuvanti Mountains]] %%^End%%

Xeron is an ancient aboleth entombed within the rock beneath the Yuvanti Mountains, near Tharn Todor. The being is believed to have mineralized, and is now more stone than flesh. Reports from explorers indicate it shows no evident interest in meddling with affairs beyond its cavern.

%% DM

An ancient aboleth, now more stone than anything else, that no longer cares to meddle in the world. Trapped in rock that was once under the sea beneath the Yuvanti mountains.
 
Introduced in: [[Ep 1 Chuul]]: 

- The vibe was that when the Yuvanti was uplifted, some things that were in the ocean got trapped. 
- Vibe: a crystallized aboleth that no longer cares to meddle in the world. 
- Mining under Tharn Todor uncovered ancient runes and a lost temple to an aboleth god; “Ancient aboleth now nearly a statue … still exists beneath Tharn Todor.”
- Relics mentioned in notes: a golden idol of Xeron; very old coins from Hkar found with it (Agnor’s possession in DM notes).

%%

%%^Metadata:names:v1%%
- {name: Xeron, language: unknown, pronunciation: "ZEHR-on", notes: "Cautious spelling-based proposal: initial x as z, short eh, and first-syllable stress; no name-specific pronunciation or language is established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern reference to the ancient aboleth beneath the Yuvanti Mountains; the DR 1748 discovery records the observed condition without dating its beginning.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added knownTo: [dufr] from the recorded campaign interaction.
- Normalized campaignInfo to the canonical lowercase campaign code.
- Normalized the existing campaign marker to its equivalent canonical code.
- Added persistent name metadata and POV modern with temporal coverage notes.
- Normalized frontmatter ordering and collection formatting.

### Validated judgments
- [[Oskar in Tharn Todor]] supports the ancient remains beneath Tharn Todor and the observed lack of interest in disturbance. The mineralized condition is a longstanding reference state, so the discovery date does not require a year-specific POV.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise the proposed `ZEHR-on`. Neither [[Oskar in Tharn Todor]] nor [[Ep 1 Chuul]] records a pronunciation or name language; this is a cautious spelling-based reading with initial x as z, short eh, and first-syllable stress. If accepted, set frontmatter `pronunciation: ZEHR-on` and the name entry to `status: documented`.
- [ ] **Suggestion — editorial.shared_material_redundant:** The opening DM-comment sentence “An ancient aboleth, now more stone than anything else, that no longer cares to meddle in the world” and the later “Vibe: a crystallized aboleth that no longer cares to meddle in the world” repeat the visible description. Remove those two duplicate sentences/lines while retaining the source pointer, the separate geological hypothesis, and the remaining DM/source notes in the hidden comment. This bounded split preserves distinct private guidance without maintaining two copies of the public description.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T13:33:35-04:00"
lintVersion: "3.4"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: brook
name: Mournebrook
whereabouts:
  - {type: primary, location: Addermarch, startFilter: r}
  - {type: secondary, location: Wistel-Enst Watershed, startFilter: "1"}
dm_owner: none
dm_notes: none
POV: modern
---

# Mournebrook
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% not mapped, but something like 13.11.A24 to 13.11.D07 is approx %%

The Mournebrook flows northeast out of the [[Shadowmere]]—a haunted swamp on the western edge of the [[Darkwood]]—to join the [[Aure]] a little north of where that river exits the forest. In the southern [[Addermarch|Addermarian]] frontier it is treated as a boundary as much as a watercourse, and few willingly cross it.

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Shadowmere, map: world, locator: }
  - {role: outlet, feature: Aure, map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Mournebrook, role: primary, language: unknown, pronunciation: MORN-brook, notes: "Cautious spelling-based proposal; no source establishing the name's language or exact in-world phonology was found.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography of the Mournebrook from the Shadowmere to the Aure; its exact map coordinates remain unresolved.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the required waterway map skeleton with the established source at [[Shadowmere]] and outlet at [[Aure]].
- Added persistent name and temporal metadata.

### Validated judgments
- The shared comment records approximate, explicitly unresolved mapping guidance and remains hidden for later verification.

### Open findings
- [ ] **Warning — metadata.map_location_missing:** Map position fields remain incomplete: `source.locator` and `outlet.locator`. The shared comment suggests only an approximate range (`13.11.A24` to `13.11.D07`); verify the authoritative map and fill the two blank locator values without guessing.
- [ ] **Warning — metadata.names_unresolved_status:** Persistent name review remains open for `Mournebrook — MORN-brook` (proposed). This is a cautious spelling-based reading because no source establishes the name's language or exact in-world phonology; accept it in frontmatter or correct the persistent entry.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Vorongrad
whereabouts: Ursk
dm_owner: tim
dm_notes: important
POV: modern
---
# Vorongrad
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A fortified city built on rocky cliffs in the eastern part of [[Ursk]]; the primary port of call for the Urskan Navy.
%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Vorongrad", "language": "unknown", "pronunciation": "vah-ruhn-GRAHT", "status": "proposed", "notes": "The Urskan context supplies the Russian analogue in [[Languages]]. Proposed reduced unstressed o vowels, a hard gr cluster, a full ah in the stressed final syllable, and final d devoiced to t. Final-syllable stress and the exact in-world name language remain unconfirmed."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern fortified naval-port description; no narrower current-era snapshot is required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, made the filename-supplied name explicit, and added the required typed map skeleton with a blank locator.
- Added proposed primary name metadata and broadly modern temporal metadata.

### Validated judgments
- [[Philosopher's Information Concerning Ursk]] supports the fortified eastern cliff city and its naval role.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required `Metadata:map:v1` single-location entry has an empty locator. Supply the settlement's verified world-map position as `- {map: world, locator: "<verified coordinate>"}`; the available prose does not establish a hex, so no coordinate was guessed.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm or revise `vah-ruhn-GRAHT` in the persistent name entry. The Urskan context supplies the Russian analogue in [[Languages]]: reduce the unstressed o vowels, retain hard gr, use ah in the stressed final syllable, and devoice final d to t. Final-syllable stress and the exact name language are unconfirmed. If accepted, set `pronunciation: vah-ruhn-GRAHT` and mark the entry `documented`.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The existing `important` attestation may refer to remembered or off-vault information. Confirm whether it remains accurate; do not remove or change it solely because the local search found no match.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T23:55:52-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: town
name: Mendin
whereabouts:
  - {type: primary, location: Mawar Confederacy, startFilter: "1"}
  - {type: secondary, location: Mawakel Peninsula, startFilter: "2", linkText: "on"}
dm_owner: none
dm_notes: none
POV: modern
---
# Mendin
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Mendin is a small town and port on the western coast of the [[Mawakel Peninsula]], near the [[Chardonian Empire]], used as a stopping place by travelers and traders. 

%%
Source links:
- [[The Ciphered Scroll]]
- [[Mawar Adventures Episode 02]]
%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Mendin, language: unknown, pronunciation: MEN-din, notes: cautious spelling-based reading; no language or name-specific pronunciation source was found, status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the town's port and travel role are not tied to a narrower date.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added the required single-location map block, leaving its unknown locator blank.
- Added persistent name metadata with a spelling-based pronunciation proposal.
- Recorded a broadly modern POV and its temporal interpretation.

### Validated judgments
- Preserved the hidden source list as a source pointer.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Mendin's required world-map locator remains blank. Supply the established coordinate in `- {map: world, locator: <hex>}`.
- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `MEN-din` only as a cautious spelling-based reading because no language or name-specific pronunciation source was found. Review the proposal; if accepted, add `pronunciation: MEN-din` to frontmatter and change the entry to `status: documented`, or replace it with the accepted form and derivation.
%%^End%%

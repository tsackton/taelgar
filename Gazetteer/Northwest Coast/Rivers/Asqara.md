---
headerVersion: 2023.11.25
lintedAt: "2026-08-24T09:25:51-04:00"
lintVersion: "3.5"
tags: [place, status/stub, status/check/name, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Asqara River
whereabouts: Mawakel Peninsula
dm_owner: none
dm_notes: none
POV: modern
---
# The Asqara River
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% the small river that runs from the [[Mawar Mountains]] to the [[Slate Sea]] %%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: , map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Asqara River, role: primary, language: unknown, pronunciation: ahs-KAH-rah RIV-er, notes: "Proposed from a cautious spelling-based reading because no language or pronunciation source is established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography; the available evidence establishes the river's endpoints but no narrower temporal constraint.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added a typed waterway map skeleton plus persistent name and temporal POV metadata.

### Validated judgments
- `status/stub` is supported because the note has no visible reader-facing description.
- `status/check/name` was preserved as independent human-review state.

### Editorial assessment
- **Underdeveloped**: the visible article contains no reader-facing geographic definition of the river. The smallest useful scope is one sentence identifying it as a small river from the Mawar Mountains to the Slate Sea; no broader cultural or historical development is required.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required waterway map block now has source and outlet entries, but both `locator` values remain blank. Supply the source and outlet map coordinates; the optional feature names remain blank until the hidden geographic statement is adopted or otherwise confirmed for public metadata.
- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry proposes `ahs-KAH-rah RIV-er` from a cautious spelling-based reading because no language or pronunciation source is established. Accept, revise, or reject it, and copy an accepted primary pronunciation to frontmatter.
- [ ] **Suggestion — editorial.public_material_candidate:** The shared hidden sentence is a coherent public-safe geographic description. Candidate: `The Asqara is a small river that flows from the [[Mawar Mountains]] to the [[Slate Sea]].`
- [ ] **Suggestion — editorial.note_underdeveloped:** The reference note has no visible article text and therefore does not currently perform even its bounded river-reference role. Resolve this by adopting or revising the one-sentence public candidate above; additional expansion is optional.
%%^End%%

---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Naithalë
aliases: [Naithalë, Nimrata, Arianrith]
pronunciation: NY-thah-lay
whereabouts: Istaros Watershed
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Naithalë flows south from the [[Mostreve Hills]] to [[Lathirion Lake]] through largely uninhabited and desolate land. It is a border of sorts for the elves, and the elves of [[Orenlas]] rarely cross the Naithalë, or if they do, only with strength of arms and magic. 

%%^Campaign:none%%
For many years after the Great War, the red dragon [[Vraedhul]] had a lair in the southern reaches of the Naithalë and smoke and steam would rise from the waters. The lair was destroyed in 1720 during the [[War of the Ashen Horde]] by unknown forces. 
%%^End%%
### Names
This river is well-known in Tyrwingha, where it is called the Arianrith and often spoken of with fear. Few who see its waters are said to return. Isinguese sources refer to it as the Nimrata, although today the elves speak of it more often than any others.

%%^Metadata:names:v1%%
- {name: "Naithalë", language: "unknown", pronunciation: "NY-thah-lay", status: "documented"}
- {name: "Arianrith", role: "alias", language: "unknown", status: "documented", notes: "The name used in Tyrwingha, where the river is spoken of with fear."}
- {name: "Nimrata", role: "alias", language: "unknown", status: "documented", notes: "The name used in Isinguese sources."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: "Mostreve Hills", map: world, locator: }
  - {role: outlet, feature: "Lathirion Lake", map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the article describes the drainage system in its current-era geographic reference role, with no narrower speaking position required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving parsed values and headerVersion.
- Recorded a broadly modern geographic POV and a persistent temporal-coverage note.
- Converted the legacy Campaign:None sentinel to the equivalent canonical Campaign:none form.
- Corrected "often spoke of with fear" to "often spoken of with fear" without changing meaning.
- Added persistent name metadata, preserving accepted pronunciations and documenting proposal provenance where needed.
- Added the required typed map entries; unsupported coordinates remain blank for human completion.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required map block now has typed entries, but its source and outlet locator values remain blank. Supply the two verified map coordinates in those entries; do not infer positions from the prose or assign arbitrary coordinates.

- [ ] **Suggestion — editorial.public_material_candidate:** The Campaign:none paragraph beginning “For many years after the Great War” preserves a coherent account of the river’s dragon lair that would explain the danger associated with its southern reaches. Confirm this shared hidden history for public adoption; the Vraedhul staging stub does not independently establish its chronology. Candidate: “For many years after the [[Great War]], the red dragon [[Vraedhul]] maintained a lair along the southern reaches of the Naithalë, where smoke and steam rose from the waters. Unknown forces destroyed the lair in DR 1720 during the [[War of the Ashen Horde]].” If adopted, replace only this hidden paragraph with the approved public prose and retain the uncertainty about who destroyed the lair.
%%^End%%

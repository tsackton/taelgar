---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
mapLocation: { x: 10388.5, y: 7089, hex: 15.17.F.22/3406, importance: local, symbol: square }
name: Medju
whereabouts: Eastern Green Sea
dm_owner: tim
dm_notes: important
POV: modern
---
# Medju
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The great spice city in the south, the terminus of trade routes from strange lands across the desert, where you can buy and sell almost anything in the markets of the obscenely wealthy spice lords.

![[medju-1.jpg|500]]

%%^Metadata:names:v1%%
- {name: Medju, language: unknown, pronunciation: MEJ-oo, status: proposed, notes: "Cautious spelling-based proposal: first-syllable stress, e as in bed, dj as j in judge, and final u as oo; no source language or recorded pronunciation is established."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the spice city and its trade role, as reported by Green Sea sailors; no narrower speaking position is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter; added persistent name, map, and POV metadata.
- Removed the duplicated spacing in “markets of the obscenely wealthy spice lords.”

### Validated judgments
- The short trade-city account matches the sailors’ report in [[Session 60 (DuFr)]].
- Confirmed local sources support the positive `dm_notes` attestation; the field is preserved.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The settlement map entry has no position. Supply the world-map `locator` in `Metadata:map:v1`; no supported hex was found in the reviewed material.
- [ ] **Warning — metadata.names_unresolved_status:** The primary name has no recorded pronunciation or established source language. Review `MEJ-oo`: this cautious spelling reading uses e as in bed, dj as j in judge, final u as oo, and tentative first-syllable stress. Accept it by copying `pronunciation: MEJ-oo` to frontmatter and changing the name entry to `status: documented`, or revise the persistent proposal.

### DM evidence
- [[_DM_/Brainstorming/Campaign Pitches]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Prequel - Wellby]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Session 1 - Wellby]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Session 2 - Wellby]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Wave Dancer's Information]]
- [[_DM_/_Dunmari Frontier/NPCs/Bernie Tidewater]]
%%^End%%

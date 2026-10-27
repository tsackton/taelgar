---
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Nayan
whereabouts: Nayan Floodplains
dm_owner: none
dm_notes: color
POV: modern
---
```taelgar-header
```

The northernmost of the three great rivers of the [[Nayan Floodplains]].

%%^Metadata:names:v1%%
- {name: Nayan, language: unknown, pronunciation: NYE-ann, notes: "Proposed transfer of the Nayan component from the accepted pronunciation in [[Marathu]] (NYE-ann muh-RAH-too); the river-specific pronunciation and name language are not documented.", status: proposed}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: , map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geographic identification of the river within the Nayan Floodplains.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and tag-list formatting while preserving existing values.
- Added persistent name metadata with a source-based proposed pronunciation; the specific name language remains unknown.
- Added the required waterway map skeleton with source and outlet entries; neither endpoint locator was guessed.
- Added `POV: modern` and a temporal coverage note for the existing geographic description.

### Validated judgments
- Confirmed river references support the positive `dm_notes` attestation. Its value is preserved; private source contents are excluded from this report.
- The existing sentence performs a bounded geographic reference role. It has no demonstrated factual contradiction or material later change.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Both `locator` fields in `Metadata:map:v1` remain blank. Supply the river's source and outlet coordinates on `map: world` in the corresponding typed entries. The reviewed evidence does not establish exact endpoint hexes; retain the blank locators until those positions are supplied.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `NYE-ann` in `Metadata:names:v1`. [[Marathu]] explicitly records `NYE-ann muh-RAH-too`; the proposal transfers that accepted name component, with first-syllable emphasis and an eye-like vowel followed by ann, rather than deriving a new reading from the Dunmari language analogue. This remains a proposal because the river's own pronunciation is not recorded, and the river name's language remains unknown. If accepted, add `pronunciation: NYE-ann` to frontmatter and mark the entry `documented`, or supply the intended river pronunciation and language.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 42]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Dunmari Magic - Old Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
%%^End%%

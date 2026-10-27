---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/name, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Little Valmont
whereabouts: Istaros Watershed
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Little Valmont is a small tributary of the [[Valmont]], joining it north of its confluence with the [[Andonne]].

%% The river is not labeled on the map. %%

%% Naming discussion: [[2026-08-04 - Northern Forest Hills and River Names]] proposed Brenne (BREN), Orvane (or-VAHN), and Little Valmont. A preference was expressed for Little Valmont or Orvane. %%

%%^Metadata:names:v1%%
- {name: "Little Valmont", role: "primary", language: "Common", status: "documented", notes: "Pronunciation proposal pending human acceptance: LIT-ul VAL-mont. Common uses Modern English; Little is ordinary English and Valmont is adapted with initial stress, short a/o, and pronounced final t. The existing documented name, language, role, and status are preserved."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: "Valmont", map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the article describes the drainage system in its current-era geographic reference role, with no narrower speaking position required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Recorded a broadly modern geographic POV and a persistent temporal-coverage note.
- Retained the accepted name entry and stored a durable pronunciation proposal in its notes without changing documented values.
- Added the required typed map entries; unsupported coordinates remain blank for human completion.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required map block now has typed entries, but its source and outlet locator values remain blank. Supply the two verified map coordinates in those entries; do not infer positions from the prose or assign arbitrary coordinates.

- [ ] **Warning — pronunciation.missing_or_exception:** The preserved documented name entry identifies Common, whose analogue is Modern English. The proposal uses ordinary Little, initial stress and short a/o in Valmont, and a pronounced final t. No accepted proper-name pronunciation is recorded; the proposal is retained in the entry notes without changing its documented status. Candidate if accepted: set frontmatter `pronunciation: LIT-ul VAL-mont` and the matching persistent entry pronunciation to `LIT-ul VAL-mont` with `status: documented`; otherwise correct the durable proposal and its derivation together.
%%^End%%

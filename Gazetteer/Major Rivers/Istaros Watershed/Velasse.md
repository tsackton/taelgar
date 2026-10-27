---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Velassë
aliases: [Velassë, Velonere]
pronunciation: veh-LAH-sseh
whereabouts: Istaros Watershed
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

Flowing south from [[Orenlas]], this is known as the "river of the elves" and few reliable reports exist as to its character. It flows into [[Lathirion Lake]] and emerges from the lake as the [[Thalurien|Thalúrien]].

It is said to mean "veiled river" in Elvish and legend says that no mortal can cross it. The Isinguese called it the Velonere and said its dark waters brought forgetfulness, although these stories have mostly been lost since the Great War.

%%^Metadata:names:v1%%
- {"name": "Velassë", "language": "Elvish", "pronunciation": "veh-LAH-sseh", "status": "documented", "notes": "The article reports the Elvish meaning veiled river and preserves its legendary attribution.", "meaning": "veiled river"}
- {"name": "Velonere", "language": "Isinguese", "pronunciation": "vuh-loh-NEHR", "status": "proposed", "notes": "The article explicitly identifies this as the Isinguese form. Proposal uses the northern French option of the Isinguese analogue in [[Languages]]: initial e reduced, o as oh, final ere as ehr with silent final e, and final emphasis. The Spanish option would instead suggest veh-loh-NEH-reh; exact in-world phonology is unestablished.", "role": "historical"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {"role": "source", "feature": "Orenlas", "map": "world", "locator": ""}
  - {"role": "outlet", "feature": "Lathirion Lake", "map": "world", "locator": ""}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography, with attributed Elvish and Isinguese legends as retrospective background.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing values.
- Added persistent name metadata and a broadly modern POV with temporal-coverage notes.
- Added the required typed map entries; unsupported locator values remain blank.
- Corrected the declared objective grammar or typo without changing the factual account.
- Stored the unresolved pronunciation proposal persistently in the name block; accepted frontmatter pronunciations were preserved.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required river source and outlet entries in Metadata:map:v1 still have blank locator values. The reviewed sources establish identifying features but no verified world-map hexes for these positions. Supply each verified coordinate in its existing `locator` field, for example `locator: "<verified world hex>"`; retain the typed entries and do not infer a hex from a nearby place.

- [ ] **Warning — metadata.names_unresolved_status:** Review the persistent proposed pronunciation `vuh-loh-NEHR` in Metadata:names:v1. The target identifies Velonere as Isinguese. The northern French option of the Isinguese analogue in [[Languages]] supports reduced initial e, oh for o, final ere as ehr with silent final e, and final emphasis. The Spanish option suggests veh-loh-NEH-reh; exact phonology is unknown. The accepted primary veh-LAH-sseh remains unchanged. Accept or revise the proposal, then mark the historical entry documented after acceptance; keep the accepted primary pronunciation in frontmatter.
%%^End%%

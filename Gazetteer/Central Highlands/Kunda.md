---
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
ancestry: stoneborn
mapLocation: { x: 5787, y: 6520, hex: 14.10.B.24/6045, importance: local, symbol: square }
name: Kunda
whereabouts:
  - {type: primary, location: Indalas}
  - {type: secondary, location: Central Highlands}
dm_owner: tim
dm_notes: color
POV: modern
---
```taelgar-header
```

%% Drikod village %%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Kunda, language: unknown, pronunciation: KOON-dah, status: proposed, notes: "Proposal informed by the Stoneborn analogue to Xhosan in Languages: pure u as oo and a as ah, retained n and d, and penultimate stress. The name's language and exact in-world phonology are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern village identification; the Drikod connection is established for DR 1748, while the note gives no developed account of earlier or later village life.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added the required settlement map skeleton with the unknown locator left blank.
- Added persistent name metadata with a proposed pronunciation, plus `POV: modern` and temporal coverage.

### Validated judgments
- The authored `Drikod village` comment makes the note eligible, but it functions as a brief editorial pointer rather than a visible reference account.
- [[Drikod]] and [[Session 32 (DuFr)]] establish the village's defining home connection. Confirmed local source matches support the positive `dm_notes` attestation, which is preserved.

### Editorial assessment
**Underdeveloped**: the visible article lacks its central identifying account as the stoneborn village associated with Drikod. One sourced sentence identifying the village, its mountain setting, and that home connection is sufficient; a general village history or invented civic detail is not required.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has one `map: world` entry, but its `locator` remains blank. Supply the verified world-map hex in that existing entry; the reviewed sources do not establish a coordinate. Preserve the typed entry rather than substituting an empty locations list.
- [ ] **Warning — metadata.names_unresolved_status:** The persistent entry proposes `KOON-dah`, informed by the Stoneborn/Xhosan analogue in [[Languages]]: pure u as oo and a as ah, retained n and d, and penultimate stress. The name's own language and exact in-world phonology remain unestablished. Accept or revise the stored proposal; if accepted, copy the primary pronunciation to frontmatter and set the entry to `status: documented`.
- [ ] **Warning — coverage.established_fact_missing:** The visible body contains no reference prose and omits Kunda's defining connection to [[Drikod]]. His note identifies it as his village, and [[Session 32 (DuFr)]] records his departure north toward his home village on DR 1748-06-20. The existing metadata identifies a stoneborn village in Indalas. The smallest useful addition is: “Kunda is a [[Stoneborn|stoneborn]] village in the [[Sentinel Range|Indalas]], the home village of [[Drikod]].” This records the place's identity without importing a campaign itinerary or inventing settlement details.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 26-0]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Drikod (OneNote)]]
%%^End%%

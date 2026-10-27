---
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
displayDefaults: {wOriginU: "<ancestry:Ua> <typeof>, location unknown", wCurrent: ""}
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: mythical city
ancestry: null
name: "Pu'aatar"
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

Pu’aatar is a mythical desert city, reputed to shelter a vast library of legendary scale, hidden somewhere in the vast deserts to the east.  

%%
DM notes / sources
- Session 115 (DuFr): crew charmed to seek Pu’aatar, described as a hidden city famed for its library.
%%

%%^Metadata:names:v1%%
- {name: "Pu'aatar", language: unknown, pronunciation: poo-AH-tar, status: proposed, notes: "Cautious spelling-based proposal: u as oo, aa as a sustained ah, the apostrophe as a syllable break, and stress on the middle syllable. No source language, adopted rule, analogue, or accepted pronunciation is established."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern account of a reputed city whose location and existence remain unconfirmed; the DR 1749 report of a search does not establish that the city was reached or found.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized frontmatter order and collection formatting while preserving its values, and added the explicit subject name.
- Added a typed settlement map skeleton with its unknown locator left blank, persistent name metadata with an unaccepted pronunciation proposal, and broadly modern POV and temporal coverage.

### Validated judgments
- [[Session 115 (DuFr)]] supports a mythical desert city reputed for a great library. The charmed search does not prove that the city exists or was found; the article preserves that uncertainty and is sufficient for its bounded reference role.
- The ordinary comment is a source pointer. No local DM evidence matches were supplied, and `dm_notes: none` is retained.

### Open findings
- [ ] **Warning — metadata.map_location_missing:** The city's location is unknown in the article. Retain the blank locator until a human can supply a verified world coordinate in `{map: world, locator: }`; do not turn a legend or travel direction into a mapped fact.
- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise `poo-AH-tar` in the name block, then put an accepted pronunciation in frontmatter and mark the entry documented. This is only a cautious spelling-based reading: `u` as `oo`, `aa` as a sustained `ah`, the apostrophe as a syllable break, and middle stress. No source language, adopted pronunciation rule, cultural analogue, or accepted pronunciation is established.
%%^End%%

---
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Aquilona
whereabouts: Drankorian Empire
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

Aquilona was a small city in the [[Drankorian Empire]]. Though known from names and sources, its location has been lost.

%%^Metadata:names:v1%%
- {"name": "Aquilona", "language": "unknown", "pronunciation": "ah-KWEE-loh-nah", "notes": "Proposed from the Drankorian cultural context and the Classical Latin analogue in [[Languages]]: qu is kw, vowels are kept separate, and stress is antepenultimate assuming short penultimate o. A long o would yield ah-kwee-LOH-nah; name-specific language and vowel quantities are not established.", "status": "proposed"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern retrospective identification of an ancient Drankorian city whose location is lost.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the explicit filename-derived name, a persistent proposed pronunciation entry, temporal metadata, and the required map skeleton.

### Validated judgments
- No local-only DM evidence was found for the negative attestation. The city’s lost-location statement is preserved; neither the scholar’s name nor her work establishes a rediscovered site.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has its typed skeleton, but `locations[0].locator` is blank. Supply a verified world-map locator in `{map: world, locator: <verified locator>}`; no coordinate is established by the consulted text sources.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm `ah-KWEE-loh-nah`, retained as proposed in `Metadata:names:v1`. The Drankorian cultural context and Classical Latin analogue in [[Languages]] support qu = kw and separate vowels; antepenultimate stress assumes a short penultimate o. A long o would instead give `ah-kwee-LOH-nah`. Exact source language and vowel quantities are unrecorded. Accept or revise the proposal; copy an accepted primary pronunciation to frontmatter and mark its entry documented.
%%^End%%

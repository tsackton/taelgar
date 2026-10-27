---
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
name: Laicon
whereabouts: Refounded Alliance of Aurbez
dm_owner: mike
dm_notes: none
POV: modern
---
```taelgar-header
```

A small village that grew up around [[Ausson's Crossing]], a large inn, in the late 1690s. [[Ausson's Crossing]] is still the dominant building and still the heart and soul of the village. It is set across the [[Maseau - Dunmar Road]] and has become an important trading point for [[Aurbez Plateau]] scavengers who reclaim dwarven mining goods and ore from the ruins and dangers of [[Ardith]] and sell it to the outside world.

%% See [[Ardith Mining]] for some background on this. Also note the details in the [[Ausson's Crossing]] page.  %%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Laicon, role: primary, language: unknown, pronunciation: LAY-kon, status: proposed, notes: "Cautious spelling proposal: ai as in rain, hard c before o, short final o, and first-syllable stress. No established in-world language or name-specific pronunciation was found."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern village description, with its emergence around the inn placed in the late DR 1690s.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added the explicit name, a proposed name pronunciation, modern temporal metadata, and the required single-location map skeleton.
- Corrected “has grew up” to “grew up” and “the dominate building” to “the dominant building”; both are objective word-form errors.

### Validated judgments
- The visible paragraph adequately identifies the village, its inn, location, origin, and trading function. [[Ausson's Crossing]] and [[Refounded Alliance of Aurbez]] corroborate that role. The travelogue’s questioned chronology is not used to revise the village’s founding date.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required map block is now present, but Laicon’s world-map locator is unknown. Supply a verified hex in `locations: [{map: world, locator: VERIFIED_HEX}]`; the placeholder is a request for human map placement, not a proposed coordinate.

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed pronunciation `LAY-kon`: cautious spelling-based `ai` as in rain, hard `c` before `o`, short final `o`, and first-syllable stress. No subject-specific source establishes a language or accepted pronunciation, so no real-world language analogue is inferred from regional culture. Accept or revise the proposal, mark the entry documented on acceptance, and copy the accepted pronunciation to frontmatter; retain `language: unknown` until supported.
%%^End%%

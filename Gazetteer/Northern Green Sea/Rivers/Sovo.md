---
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Sovo
whereabouts: Ursk
dm_owner: none
dm_notes: color
POV: modern
---
```taelgar-header
```

%%the river that flows into the Green Sea near the 2nd easternmost trade city%%

%%^Metadata:names:v1%%
- {"name":"Sovo","language":"unknown","pronunciation":"SOH-vuh","status":"proposed","notes":"Proposal uses the regional Urksan/Russian analogue in [[Languages]]: hard s and v, stressed first o as oh, and reduced unstressed final o as uh. Initial stress is tentative; neither the name language nor exact in-world pronunciation is established."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: Marinsk, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography, currently recorded only in an authored comment; no narrower temporal boundary is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added the explicit subject name.
- Added persistent name metadata and a broadly modern article viewpoint.
- Added the two-ended waterway map skeleton; unknown locators remain blank.

### Validated judgments
- The article is reviewed as a geographic reference; routine campaign travel and transactions do not require a campaign log.

### Editorial assessment
**Underdeveloped**: the note has no visible defining account of the river. Its central missing dimension is the established route through Marinsk to the Green Sea; one factual sentence is sufficient development scope.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Supply the source and outlet `locator` values in `Metadata:map:v1` from an established map reference. The typed entries are present, but no exact world hexes were established; retain the descriptive features and do not infer coordinates.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. This may represent remembered information or another off-vault source; confirm the attestation or supply its source. The linter preserved the human value.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm or replace proposed **SOH-vuh** for Sovo. The regional Urksan/Russian analogue in [[Languages]] suggests hard `s` and `v`, `oh` in the stressed first syllable, and a reduced final unstressed `o` as `uh`; the stress and name language are unconfirmed. If accepted, copy `pronunciation: SOH-vuh` into frontmatter and mark the name entry `documented`, or supply the intended reading.
- [ ] **Warning — coverage.established_fact_missing:** The only authored geography is hidden in the comment “the river that flows into the Green Sea near the 2nd easternmost trade city.” [[Marinsk]] and [[Philosopher's Information Concerning Ursk]] identify that city and establish the river through it. Add the minimal visible definition: “The Sovo is a river in [[Ursk]] that flows through [[Marinsk]] into the [[Green Sea]].” Then reconcile the provisional locator comment; do not invent headwaters or a longer course.
%%^End%%

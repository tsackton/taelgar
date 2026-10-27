---
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Leis
pronunciation: LEE-is
whereabouts: Ursk
dm_owner: none
dm_notes: color
POV: modern
---
```taelgar-header
```

A swift-flowing river that runs from the mountains near [[Vedmakov]] until it joins the [[Beyil]] near the village of [[Volya]]. A road runs parallel to the Leis for much of its length, but the river itself is unnavigable, except when frozen in the depths of winter.

%%^Metadata:names:v1%%
- {"name":"Leis","language":"unknown","pronunciation":"LEE-is","status":"documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: mountains near Vedmakov, map: world, locator: }
  - {role: outlet, feature: Beyil near Volya, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography and travel conditions; no narrower temporal boundary is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, added the explicit subject name, and removed pre-existing trailing space exposed by adding end metadata.
- Added persistent name metadata and a broadly modern article viewpoint.
- Added the two-ended waterway map skeleton; unknown locators remain blank.

### Validated judgments
- The article is reviewed as a geographic reference; routine campaign travel and transactions do not require a campaign log.
- [[Volya]] and [[Session 95 (DuFr)]] corroborate the confluence and the road toward [[Vedmakov]]. The compact course and travel account performs this river note’s role.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Supply the source and outlet `locator` values in `Metadata:map:v1` from an established map reference. The typed entries are present, but no exact world hexes were established; retain the descriptive features and do not infer coordinates.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: color`. This may represent remembered information or another off-vault source; confirm the attestation or supply its source. The linter preserved the human value.
%%^End%%

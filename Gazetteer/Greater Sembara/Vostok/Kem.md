---
lintedAt: "2026-10-20T06:59:58-04:00"
lintVersion: "3.5"
displayDefaults: {prep: "on", defArt: the}
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Kem
pronunciation: KEM
whereabouts: Vostok
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Kem is a river in [[Vostok]] that receives the [[Niva]] and flows into the [[Green Sea]]. Its lower valley is one of the principal inhabited areas of southern Vostok.

%%
Geographic clarification:

- The Kem and [[Niva]] are established names within the same complex river system. Written sources describe the Kem as the more eastern river, refer to its lower valley in southern [[Vostok]], and say that the Niva joins it.
- The map does not label individual channels, however, so it does not establish which upper branch is the Kem, which is the Niva, or precisely where the named rivers meet.
- [[Lake Pekul]] and [[Lake Sova]] are distinct lakes in this drainage system, but the available evidence does not establish that either lies directly on the reach properly called the Kem rather than on a tributary with another local name.
- Do not assume that “Kem” names the entire mapped network or that one river name continues unchanged through all of its upper branches.
%%

%%^Metadata:names:v1%%
- {name: Kem, language: Vosic, pronunciation: KEM, status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: , map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference geography and physical character; no narrower speaking position is required by the visible account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized frontmatter and added the typed waterway map skeleton.
- Quoted the authored `prep: on` preposition as a string, following [[Display Control]], to preserve its meaning across YAML parsers rather than convert it to a boolean.
- Added modern POV and persistent temporal guidance; preserved the existing documented name entry.

### Validated judgments
- The confluence and inhabited lower-valley account performs the river's present reference role.
- The clarifications in this note, [[Niva]], [[Lake Pekul]], and [[Lake Sova]] preserve the unresolved assignment of upper channels and lakes; no whole-network identity is inferred.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The `source` and `outlet` rows in `Metadata:map:v1` both have blank `locator` values. Supply established world-map coordinates for those two endpoints. Preserve the existing geographic clarification: the unlabeled upper branches do not establish the Kem's named source or the precise Niva confluence, and neither lake can be assumed to lie on the named Kem reach. Leave unsupported coordinates blank pending human map review.
%%^End%%

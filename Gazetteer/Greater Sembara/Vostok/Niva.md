---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T06:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Niva
aliases: [River Niva, Niva River]
pronunciation: NEE-vah
whereabouts: Vostok
dm_owner: none
dm_notes: none
POV: modern
---
# Niva
*(NEE-vah)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Niva is a river in [[Vostok]] that joins the [[Kem]], and forms part of the large Kem watershed that flows into the [[Green Sea]].

%%
Geographic clarification:

- The Niva and [[Kem]] are established names within the same complex river system. Written sources say that the Niva joins the Kem, but the map does not label either river or identify their precise confluence.
- It is therefore unclear which of the mapped upper branches is the Niva, how far upstream that name applies, or whether individual tributaries have separate local names.
- [[Lake Pekul]] and [[Lake Sova]] belong to the wider Kem–Niva drainage system, but neither can currently be assigned specifically to the Niva.
%%

%%^Metadata:names:v1%%
- {name: Niva, language: Vosic, pronunciation: NEE-vah, status: documented}
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
- Added the typed waterway map skeleton and modern temporal metadata.
- Preserved the existing documented name entry.

### Validated judgments
- The confluence account performs the river's present reference role; [[Kem]], [[Lake Pekul]], and [[Lake Sova]] support retaining the distinction between the named rivers and their wider drainage system.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The `source` and `outlet` rows in `Metadata:map:v1` both have blank `locator` values. Supply established world-map coordinates for the Niva's named source and its confluence with the Kem. The notes explicitly leave the upper channels and precise confluence unresolved; do not infer coordinates or assign either lake to the Niva from an unlabeled network. Leave unsupported values blank pending human map review.
%%^End%%

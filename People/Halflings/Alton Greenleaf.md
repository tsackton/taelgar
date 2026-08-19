---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T14:40:45-04:00"
lintVersion: "2.2"
tags: [person, testcase]
species: halfling
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-07-18, type: met}
born: null
gender: male
name: Alton Greenleaf
affiliations:
  - {org: Greenleafs, type: primary}
whereabouts:
  - {type: away, start: 1748-07-18, end: 1748-07-18, location: Melavan Caravanserai}
  - {type: away, start: 1748-07-19, location: traveling east to Tokra}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1748
---
# Alton Greenleaf
>[!info]+ Biographical Info
> A [[Halflings|halfling]] (he/him), of the [[Greenleafs]]
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on July 18th, 1748 at the [[Melavan Caravanserai]], on the [[Stoneway]], [[Dunmar]] %%^End%%

A halfling wanderer, traveling with only his brother. 
## Relationships
- [[Lyle Greenleaf]], brother and traveling companion.

%%^Metadata:article:v1%%
mode: encounter snapshot
povNotes: "Accuracy range: minimal. This is a snapshot of Alton Greenleaf at the DR 1748-07-18 encounter and his immediate eastward journey. Nothing is established about his earlier or later life."
%%^End%%

%%^Metadata:names:v1%%
- {name: Alton Greenleaf, role: primary, language: Common, pronunciation: obvious, status: documented}
%%^End%%

%%^Lint%%
## Open findings

- [ ] `relationship.unresolved_location` (warning): the ongoing `whereabouts` entry uses `traveling east to Tokra` as a location target, but no such note or alias exists. [[Session 42 (DuFr)]] establishes only that Alton and Lyle were at the [[Melavan Caravanserai]] on DR 1748-07-18 and intended to travel east toward [[Tokra]]; it does not establish a later arrival.
- [ ] `name.language_inferred` (suggestion): the name block treats the English-readable “Alton Greenleaf” as Common because [[Languages]] maps written-out English names to Common. No source explicitly identifies the in-world language of his name; confirm or revise that inference.

## Copy-ready candidate

If the unresolvable journey entry is not intended as a special testcase, the source-bounded whereabouts are:

```yaml
whereabouts:
- {type: away, start: 1748-07-18, end: 1748-07-18, location: Melavan Caravanserai}
```

## Applied changes

- Added experimental `POV: 1748` and a minimal-range `povNotes` explanation; this deliberately records only the encounter and immediate stated journey.
- Added `knownTo: [dufr]`, supported by the direct encounter in [[Session 42 (DuFr)]].
- Added persistent name metadata and the obvious-pronunciation exception.
- Canonicalized frontmatter layout, including explicit nulls for the existing empty `born` and `ancestry` fields, and wrote the 2.2 lint state.

## Evidence reviewed

- [[Session 42 (DuFr)]] for the DR 1748-07-18 encounter, Alton's brother, and their stated direction of travel.
- [[Greenleafs]] for the same family relationship and travel plan; it adds no established earlier or later life.
- [[Languages]] for the provisional Common name-language inference.

## Validated judgments

- `Accuracy range: minimal` is useful here: the note is an accurate encounter snapshot, not an incomplete biography.
- “Alton Greenleaf” qualifies for the obvious ordinary-name pronunciation exception.
- No local-only `_DM_` note was found that makes `dm_notes: none` suspect.
- The campaign annotation is embedded in the information callout below the title; the deterministic comment-placement suggestion is not applicable.
- The current 2.2 validator still requires the pre-proposal free-text `pov` key in article metadata. This experiment intentionally uses searchable frontmatter `POV` plus `povNotes` instead, so that validator error is a proposal/tooling mismatch rather than an article deficiency.
%%^End%%

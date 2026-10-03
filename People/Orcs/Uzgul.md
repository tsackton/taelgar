---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: orc
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-12-10, type: met}
born: 1734
gender: male
title: Chiefling
name: Uzgul
affiliations: [The People of the Rainbow]
whereabouts:
  - {type: home, start: "", end: "", location: Uzgukhar}
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: 1748
---
# Chiefling Uzgul
>[!info]+ Biographical Info
> an [[Orcs|orc]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on December 10th, 1748 in [[Uzgukhar]], [[Xurkhaz]], the [[Garamjala Desert]] %%^End%%

A young man of 14, current heir to the kingdom. The family resemblance to [[Lubash]] is apparent, but Uzgul is full of the vigor of youth, with a mohawk of wiry black hair, a dangling silver earring on a chain in one ear, and vibrant green skin. He has a nervous excitement to him, and has a hard time sitting still.

%%SECRET[v2:3dc08695bd6f965a905c406e251e300b]%%

%%^Metadata:names:v1%%
- {"name":"Uzgul","language":"unknown","pronunciation":"ooz-GOOL","status":"proposed","notes":"The Turkic analogue for Orcish in [[Languages]] supports both written u vowels as oo, z as voiced z, and hard g; final stress is a cautious Turkic-informed choice. The broad analogue does not establish exact in-world phonology or the language of this name."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait, when Uzgul is fourteen and heir to Xurkhaz; the age is not a continuing present-day claim.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter; added `knownTo: [dufr]`, name-review metadata, and a DR 1748 viewpoint with the age-specific temporal interpretation.
- Canonicalized the existing campaignInfo code and campaign-block code to `dufr`, preserving the audience and contents.

### Validated judgments
- The fourteen-year-old heir’s portrait is read from DR 1748, matching the birth year and recorded meeting; no continuing age claim is inferred.
- The positive `dm_notes` attestation has confirmed local source support. The local-only secret was reviewed and preserved, with its recovery candidate reserved for the private handoff.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes `ooz-GOOL`. The Orcish cultural guidance in [[Languages]] gives a broad Turkic analogue: both written u vowels are read as “oo,” z is voiced, and g remains hard; final stress is a cautious Turkic-informed choice. This is an analogue-derived proposal, not attested in-world phonology or proof of the name’s language. Confirm or replace it before copying the accepted pronunciation to frontmatter and marking the entry documented.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
%%^End%%

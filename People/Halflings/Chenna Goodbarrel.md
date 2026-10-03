---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, testcase, status/check/lint]
species: halfling
ancestry: null
born: 1688
gender: female
campaignInfo:
  - {campaign: dufr, person: Wellby, date: 1730, type: met, wParty: "<met:u> <person:q> around <target> <current:2rq>"}
  - {campaign: dufr, date: 1748-12-30, type: met}
name: Chenna Goodbarrel
affiliations:
  - {org: Goodbarrels, type: primary}
  - {org: The Singing Fox, title: Proprietor, type: leader}
whereabouts:
  - {type: home, end: 1725, location: Sembara}
  - {type: home, start: 1725, location: The Singing Fox}
  - {type: away, start: 1748-12-30, end: 1748-12-30, location: Vindristjarna}
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: 1740s
---
# Chenna Goodbarrel
>[!info]+ Biographical Info
> A [[Halflings|halfling]] (she/her), of the [[Goodbarrels]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by [[Wellby]] around DR 1730 at [[The Singing Fox]], [[Fairgate Outer]] %%^End%%
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on December 30th, 1748 on [[Vindristjarna]], in the [[Tollen|Free City of Tollen]] %%^End%%

![[chenna-goodbarrel-portrait.png|right|400]]Chenna Goodbarrel owns a small and charming halfling tavern in [[Fairgate Outer]] called *[[The Singing Fox]]*, with her wife [[Harriet Goodbarrel|Harriet]]. Chenna runs the bar and kitchen; warm, welcoming, and charming, she's the heart of the establishment.
## Relationships
- [[Harriet Goodbarrel]], wife
- [[Wellby]], a distant relation, something like a third cousin once removed






%%^Campaign:none%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%

%% notes
Secret mostly contains roleplaying notes; ask if they'd be useful
%%

%%SECRET[v2:e5240229d5ad35fe54e169c1ca837ae5]%%

%%^Metadata:names:v1%%
- {"name": "Chenna Goodbarrel", "language": "unknown", "pronunciation": "CHEN-nah GOOD-bar-uhl", "notes": "Proposed using the tentative Halfling/Igbo analogue in [[Languages]] for Chenna: ch as in church, e as in bed, and final a as ah; the doubled n is retained as one clear consonant. Goodbarrel follows the transparent English compound naming pattern documented in [[Playing a Halfling]]. Stress is a reading aid; no lexical tones or exact in-world pronunciation are established.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of Chenna as an established tavern owner with Harriet; the earlier Wellby encounter and settlement dates remain qualified. The campaignInfo entry for meeting Wellby in 1730 retains its exact qualifier "#date is approx"; the Sembara whereabouts entry ending in 1725 retains its exact qualifier "# settled in Tollen in 1725 or earlier".
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added knownTo from recorded campaign interactions, a minimal name block, and temporal metadata.
- Canonicalized the campaignInfo alias DuFr to dufr and normalized frontmatter while preserving parsed values and the explicitly retained date qualifiers.
- Canonicalized campaign-marker spelling without changing the resolved audience.
- Preserved both exact YAML date qualifiers in povNotes, attached explicitly to the same campaignInfo and whereabouts entries, before normalizing frontmatter.

### Validated judgments
- Reviewed the SECRET block separately; its contents remain outside shared lint prose. Confirmed local DM matches support the existing positive attestation.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed pronunciation `CHEN-nah GOOD-bar-uhl` in `Metadata:names:v1`. Proposed using the tentative Halfling/Igbo analogue in [[Languages]] for Chenna: ch as in church, e as in bed, and final a as ah; the doubled n is retained as one clear consonant. Goodbarrel follows the transparent English compound naming pattern documented in [[Playing a Halfling]]. Stress is a reading aid; no lexical tones or exact in-world pronunciation are established. If accepted, copy it to frontmatter `pronunciation` and mark the entry `documented`; otherwise revise the proposal. The name’s source language remains `unknown`.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Tollen DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
%%^End%%

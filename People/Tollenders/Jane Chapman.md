---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Tollender
campaignInfo:
  - {campaign: dufr, date: 1748-12-30, type: met}
born: 1715
activeYear: 1740
gender: female
title: Captain
name: Jane Chapman
affiliations:
  - "Dyer's Guild"
  - {org: the Chapmans, type: primary, format: "<org:T>"}
whereabouts:
  - {type: home, location: Tollen}
  - {type: away, start: "1748-12-30", end: "1748-12-30", location: "Dyer's Guildhall"}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Captain Jane Chapman
>[!info]+ Biographical Info  
> A [[Tollen|Tollender]] [[Humans|human]] (she/her), of the Chapmans  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on December 30th, 1748 in the [[Dyer's Guildhall]], the [[Tollen|Free City of Tollen]] %%^End%%

![[jane-chapman-portrait.png|right|320]]A Tollender-born woman in her early 30s, from the well-off and well-established Chapman merchant family, Jane became a Dyer's Guild captain known for her skill and her luck at sea.  

%%SECRET[v2:6d3335abbd9e17db160768a6d2d210b1]%%

%%^Metadata:names:v1%%
- {"name":"Jane Chapman","language":"unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-DR 1748 portrait of Jane as a guild captain in her early thirties, with brief family and career background; her later career is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added knownTo: [dufr], ordinary-name metadata, and POV: 1748 with a late-1748 age and career snapshot.
- Normalized frontmatter and canonicalized the equivalent campaignInfo and Campaign block codes to dufr.

### Validated judgments
- The compact family and seafaring-career portrait is sufficient. Jane Chapman is an ordinary familiar name requiring no pronunciation proposal.
- Reviewed the local DM evidence and the SECRET block, retained the existing positive dm_notes attestation, and preserved the block’s local-only contents.

### Open findings

- [ ] **Warning — relationship.unresolved:** The primary affiliation `{org: the Chapmans, type: primary, format: "<org:T>"}` does not resolve to a family note. The visible biography establishes the merchant family, but no matching filename, metadata name, or alias was found. Either intentionally retain the free-text affiliation, or create a supported `Chapmans` family note and then use `{org: Chapmans, type: primary, format: "<org:T>"}`; the family should not be conflated with Jane herself.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
%%^End%%

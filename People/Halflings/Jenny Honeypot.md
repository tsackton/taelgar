---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
gender: female
campaignInfo:
  - {campaign: dufr, person: Riswynn, type: met, date: 1748-05-31}
name: Jenny Honeypot
whereabouts:
  - {type: home, location: Yuvanti Mountains, linkText: on the roads of, format: "<name:q>", startFilter: "1"}
  - {type: away, start: 1748-05-31, end: 1748-05-31, location: Yuvanti Mountains, alias: road between Tharn Todor and Nayahar, linkText: "on", format: "<name:q>", startFilter: "1"}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Jenny Honeypot
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:DuFr%% Met by [[Riswynn]] on May 31th, 1748 on the [[Yuvanti Mountains|road between Tharn Todor and Nayahar]] %%^End%%

Jenny Honeypot is a halfling merchant, wife of [[Mica Honeypot]], who operates a small caravan through the [[Yuvanti Mountains]], carrying trade between the dwarves and [[Nayahar]]. Jenny is the leader of the operation.

%%^Metadata:names:v1%%
- {"name": "Jenny Honeypot", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of Jenny as leader of a Yuvanti trading caravan and wife of Mica; earlier and later circumstances are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Quoted the existing “on” location prefix so YAML preserves it as text rather than interpreting it as a boolean.
- Normalized the existing campaignInfo code from DuFr to dufr and added knownTo: [dufr].
- Added persistent name metadata and the supported late-1740s viewpoint.

### Validated judgments
- [[Oskar in Tharn Todor]] records the attack and rescue of her caravan companions; no lasting change to the trade operation is established that requires adding a campaign recap.

### Open findings

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The existing generated encounter line uses `%%^Campaign:DuFr%%`; the canonical registry code is `dufr`. Regenerate that header from the now-canonical campaignInfo entry, or replace only the opening marker with `%%^Campaign:dufr%%`, retaining the line and its boundaries. The generated header and visibility marker were preserved for human review.
%%^End%%

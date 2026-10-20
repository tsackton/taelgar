---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Marinsk
whereabouts: Ursk
dm_owner: none
dm_notes: none
POV: modern
---
# Marinsk
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Marinsk is a coastal city of [[Ursk]] and one of its three principal trading ports, alongside [[Zakat]] and [[Praznitsky]]. The [[Sovo]] River runs through the city, dividing harbors and districts before reaching the [[Green Sea]]. Despite foreign docks maintained for commerce, Marinsk is cautious toward outsiders; visitors remain confined to the walled port district unless they possess proper papers. 

Like all of the coastal ports in Ursk open to trade, the port district is watched by the [[Eyes of Vedmakov|Okolov]]. But compared with the larger ports, Marinsk’s foreign quarter is smaller and—by reputation—less vigilantly guarded, and some traders speak of discreet opportunities to move goods upriver. Within the city, Urskan culture and law prevail: magic is strictly controlled, and unfamiliar customs can draw unwelcome attention.

%%
Meta/DM notes and campaign interactions:
- Source: [[Philosopher's Information Concerning Ursk|Philosopher’s memorandum on Urskan cities]] (foreign docks, Sovo approach, Okolov caution); see also [[Ursk]].
- Practical: smallest foreign port among the three; Sovo bisects the city; Okolov surveillance concentrated at docks and gates.
- 2nd easternmost of the trading cities
- DM notes indicate this is the "cultural" city but don't add anything about what that might mean.
%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name":"Marinsk","language":"unknown","pronunciation":"muh-REENSK","status":"proposed","notes":"Proposed using the Russian analogue for Urskan in [[Languages]] as a cultural guide: reduce unstressed a toward uh, read stressed i as ee, and retain the final nsk cluster. The name's specific language and stress are unrecorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern settlement geography and reference description; no narrower current-era viewpoint is required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, added the explicit name and broadly modern temporal metadata, and added the required settlement map block with its locator blank.
- Added an analogue-informed pronunciation proposal and corrected the objective spelling error “vigiliantly” to “vigilantly”.

### Validated judgments
- [[Philosopher's Information Concerning Ursk]] supports the foreign port, Sovo approach, and comparative number of Eyes; the source remains an attributed in-world warning rather than omniscient proof of every practical inference.
- The hidden block chiefly preserves provenance and unresolved cultural/geographic shorthand; it is not a developed public account awaiting adoption.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The settlement’s world-map locator is blank. Supply a verified Marinsk coordinate in the existing `Metadata:map:v1` entry; the Sovo/coastal description does not provide a hex.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm `muh-REENSK`, stored in `Metadata:names:v1`. The Russian analogue for Urskan in [[Languages]] supplies the cultural basis: unstressed a reduces toward uh, stressed i is ee, and the final nsk cluster is retained. The specific name language and stress are unrecorded, so this remains proposed. If accepted, add `pronunciation: muh-REENSK` to frontmatter and set the name entry to `status: documented`; otherwise provide the intended pronunciation.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Yamgov
whereabouts: Ursk
dm_owner: none
dm_notes: none
POV: modern
---
# Yamgov
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Yamgov is an interior city of [[Ursk]], the commercial center of the fertile [[Dalinka]] River valley. Grain fields and pastures stretch for miles around the walls, dotted with windmills and riverland hamlets. The River Market, a sprawling series of stalls along the riverbanks, serves caravans and barges alike, moving produce east toward [[Vedmakov]] and west toward outlying estates.

Unlike the fortified frontier further west at the border, the farmlands around Yamgov are less intensively patrolled by the [[Eyes of Vedmakov|Okolov]].  Even so, transit papers are wise to carry, and the main crossings of the Dalinka are watched.

In winter, when fields are quiet, gossip and small ventures fill the time in the hinterlands; in planting and harvest, the roads are crowded with carts and hired hands.

%%
Meta/DM notes and campaign interactions:
- Travel planning and passage noted in [[Session 95 (DuFr)|DuFr 95]] (Dalinka crossing; caravan logistics; overland route to Voknaz lands).
- Source note: [[Dalinka|Dalinka River]] entry; Philosopher’s memorandum on Ursk’s cities (hinterland attitudes, Okolov focus elsewhere).
%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name":"Yamgov","language":"unknown","pronunciation":"YAHM-guhf","status":"proposed","notes":"Proposed using the Russian analogue for Urskan in [[Languages]] as a cultural guide: initial y is consonantal, a is ah, g is hard, unstressed o reduces toward uh, and final v devoices to f. First-syllable stress is provisional; the name's specific language and pronunciation are unrecorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern settlement geography and reference description; no narrower current-era viewpoint is required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, added the explicit name and broadly modern temporal metadata, and added the required settlement map block with its locator blank.
- Added an analogue-informed name pronunciation proposal for human review.

### Validated judgments
- [[Dalinka]] and [[Philosopher's Information Concerning Ursk]] support the fertile-valley setting and inland/hinterland context. [[Session 95 (DuFr)]] corroborates the Dalinka crossing and overland route without requiring a campaign log in the article.
- The hidden source pointers were reviewed separately from the external DM attestation. No private source contents were included in this report.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The world-map locator is blank. Supply a verified Yamgov coordinate in the existing settlement entry; the Dalinka valley and road description do not determine a hex.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed `YAHM-guhf` in `Metadata:names:v1`. Its cultural basis is the Russian analogue for Urskan in [[Languages]]: initial y is consonantal, a is ah, g stays hard, unstressed o reduces toward uh, and final v devoices to f. First-syllable stress and exact in-world pronunciation are unrecorded. If accepted, add `pronunciation: YAHM-guhf` to frontmatter and set the entry to `status: documented`; otherwise provide the intended form.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 95 - DM Notes]]
%%^End%%

---
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/ai, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Ket
whereabouts: Northern Green Sea
dm_owner: none
dm_notes: color
POV: modern
---
```taelgar-header
```

The Ket is the most significant river of the [[Great Northern Forest]], flowing over 1500 miles from its source on the eastern slopes of the [[Svinjo Mountains]], east to the [[Green Sea]]. For most of its length, the Ket cuts through vast, uncharted stretches of taiga, dominated by dense pine and spruce forests, interspersed with birch groves. The river’s valley is home to countless species of boreal wildlife, including elk, wolves, and bears. In the summer, migratory birds flock to its banks, feeding on the abundant fish and insects, while the winter brings stark stillness, with thick snow blanketing the region.

![[ket-landscape.jpg|right|400]]The river's climate is harsh and highly seasonal. For much of its length, the Ket freezes solid from late October to early April, with the ice reaching up to four feet thick during the coldest months. Spring is dramatic, as melting ice from the river and nearby mountains causes the river to swell, flooding nearby lowlands and creating temporary marshes teeming with life. By early June, the ice has cleared, and the river runs swift and cold, carrying meltwater and sediment toward the Green Sea.

%% Climate conflict: This paragraph's late-October/early-April freeze calendar, four-foot ice depth, and early-June clearance are not retained by [[Climate and Weather Constraints#Green Sea, Skaerhem and Ursk]] (K27 and supporting limits), which leaves exact freeze/thaw dates and ice thickness open. Reconcile this precision; see the Lint proposal. %%

The most significant settlement on the Ket is the [[Ursk|Urskan]] city of [[Zvervinka]], near the river mouth, less than 100 miles inland from the coast. The Ket is also the lifeblood of the [[Vargaldi]] who call the [[Great Northern Forest]] their home. 

%% 
A dangerous place - white dragons often lair on the northern shore, and in the winter ice worms use it as a road. 
%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Svinjo Mountains, map: world, locator: }
  - {role: outlet, feature: Green Sea, map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name":"Ket","language":"unknown","pronunciation":"KET","status":"proposed","notes":"Cautious spelling-based proposal: one syllable, hard k, short e as in set, final t. No source establishes the name's language or pronunciation."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography and seasonal conditions; precise recurring freeze and thaw dates remain a documented source conflict, not a narrower temporal viewpoint.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Repaired the comma-joined tag entry as `tags: [place, status/check/ai]`, preserving its intended classification and human-review marker, and normalized frontmatter.
- Added the explicit name, a proposed name pronunciation, broadly modern temporal metadata, and a typed river map block with verified source/outlet feature names and blank locators.
- Added a nearby comment identifying the climate-precision conflict; preserved the disputed visible passage for human resolution.

### Validated judgments
- The river course, boreal setting, Zvervinka relationship, and Vargaldi context provide a sufficient regional waterway account.
- Confirmed local source matches support the positive dm_notes attestation; unrelated substring matches in a separate names pool were excluded. Private source contents have not been incorporated into this report.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** Both world-map locators in `Metadata:map:v1` are blank. Supply verified source and outlet coordinates for the Svinjo Mountains and Green Sea endpoints; retain the two directional roles and do not infer coordinates from the river description.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `KET` in the persistent name entry. It is a cautious one-syllable spelling reading, with hard k, short e as in set, and final t; the name’s language and an explicit pronunciation are unrecorded. If accepted, copy `pronunciation: KET` to frontmatter and set the entry to `status: documented`; otherwise supply the preferred form.
- [ ] **Warning — correctness.cross_note_conflict:** The climate paragraph fixes freezing to late October–early April, ice depth to four feet, and clearance to early June. [[Climate and Weather Constraints#Green Sea, Skaerhem and Ursk|K27 and its supporting limits]] explicitly leave exact freeze/thaw dates and ice thickness open and reject the old Ket precision. The dated local conditions summarized there and in [[Session 94 (DuFr)]] do not establish a recurring calendar. Reconcile the later adopted constraints with this paragraph. A bounded replacement, retaining the image embed, is: “The river's climate is harsh and highly seasonal. The Ket freezes during the long winter, and the late spring thaw brings weakening ice and flooding. Melting ice and mountain runoff swell the river, flooding nearby lowlands and creating temporary marshes teeming with life. During the warmer months, it runs swift and cold, carrying meltwater and sediment toward the Green Sea.” No exact annual schedule or ice depth is supplied.
- [ ] **Suggestion — editorial.public_material_candidate:** The ordinary comment beginning “A dangerous place” contains a coherent public-safe hazard description, while the visible account omits these distinctive dangers. [[Great Northern Forest]] publicly corroborates winter dragon raids and ice worms, but the comment’s more specific lairs and river-road details remain an adoption candidate. Decide whether to add: “White dragons often lair on the Ket’s northern shore, and ice worms use the frozen river as a road in winter.” If adopted, remove the now-duplicated comment; otherwise retain it as unadopted guidance. No encounter mechanics or private local source content is included in this candidate.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 94 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 95 - DM Notes]]
%%^End%%

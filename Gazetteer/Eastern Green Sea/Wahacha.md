---
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
subTypeOf: null
typeOfAlias: port town
ancestry: kenku
name: Wahacha
whereabouts: Vermillion Isles
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

Wahacha is one of several notable ports in the [[Vermillion Isles]], inhabited primarily by [[Kenku]]. The low port, including the harbor, docks, trading houses, and a few taverns and sailor's inns, is set along the water, below towering cliffs of red stone. The main part of town is built in and among the red stone pillars that dot the landscape, with many buildings clinging impossibly to the sides of cliffs, inaccessible except by flight.

![[kenku-village-1.png]]
*The red pillars of Wahacha are home to many [[Kenku]]*

While nominally welcoming of outsiders, the [[Kenku]] of Wahacha do little to make their homes and villages accessible to those without wings, and most of the grounders, as they call the flightless people -- [[Humans]], mostly, but some [[Halflings]] and others -- live in a few small clusters of buildings around the main harbor.

Wahacha is primarily known for the chiles that grow in the sheltered valleys outside of town, which are dried and powdered to produce a spice highly valued across the [[Green Sea]]. 

%% OneNote

Low town - bottom, docks, port
 
Main town scattered on cliffs and red stone pillars
   

Kenku names:
 
(female): Skoda, Waji, Zontay  
(male): Nahto, Makha, Choto, Kayawa
 
Halflings have good relationships with kenku, can introduce
   

**Makha** - town council type, port master, warns the ship about coastal raids
 
several kenku have vanished, including **Nahto** and **Skoda**, who have

%%
%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Wahacha", "language": "unknown", "pronunciation": "wah-HAH-chah", "status": "proposed", "notes": "The islander Kenku context supplies the Sioux analogue in [[Languages]], qualified by [[Kenku]] as islander naming inspiration rather than established general phonology. Proposed open ah vowels, w and h as written, ch as the affricate in church, and tentative middle-syllable stress. No exact dialect, stress rule, or name language is established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern settlement layout, inhabitants, and chile trade; the shared campaign-planning comment does not establish an ongoing present-day raid or disappearance.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, added the required typed map skeleton, and left its unestablished locator blank.
- Added a proposed primary name entry and broadly modern temporal metadata.

### Validated judgments
- [[Session 60 (DuFr)]], [[Session 62 (DuFr)]], and [[Vermillion Isles]] support the port, inhabitants, and cliff/harbor layout; the old raid planning does not describe a continuing present-day crisis.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required `Metadata:map:v1` single-location entry has an empty locator. Supply the settlement's verified world-map position as `- {map: world, locator: "<verified coordinate>"}`; the available prose does not establish a hex, so no coordinate was guessed.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm or revise `wah-HAH-chah` in the persistent name entry. [[Languages]] supplies Sioux as the Kenku analogue, qualified in [[Kenku]] as islander naming inspiration rather than general established phonology. The proposal uses open ah vowels, w and h as written, ch as in church, and tentative middle-syllable stress. Neither an exact dialect nor a stress rule or name language is recorded. If accepted, set `pronunciation: wah-HAH-chah` and mark the entry `documented`.
- [ ] **Suggestion — editorial.shared_material_redundant:** The `OneNote` comment's lines “Low town - bottom, docks, port” and “Main town scattered on cliffs and red stone pillars” substantially duplicate the first visible paragraph. Delete only those two source-summary lines, retaining the Kenku-name list, relationship reminder, and unresolved campaign-planning entries for separate DM review. This bounded split removes duplicate geography without promoting the remaining notes.
%%^End%%

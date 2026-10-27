---
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
subTypeOf: null
typeOfAlias: fortified town
name: Evis
whereabouts: Duchy of Maseau
dm_owner: none
dm_notes: none
POV: 1710s
---
```taelgar-header
```

The northernmost settlement in [[Duchy of Maseau|Maseau]] along the Great South Road. Evis is a fortified frontier town on the border of the March of Evis, ruled by the aging Marcher Lord, [[Peyre Vayler]], and his two daughters.  South of Evis, the land turns more fertile, and more populated, before eventually reaching the rolling valleys near [[Valarin]], where most of the people of the Duchy of Maseau live.

%%

From old background notes for family Cleenseau game; does not have to be canonical

The town of Evis, in the Duchy of Maseau, is a bustling trade town and the last stop on the Great South Road before Clenseau, 100 miles to the north (the land between Clenseau and Evis is largely deserted and known as Bandit's Way).
 
For the last few years you have been working for Lilibet, the younger daughter of the March of Evis, as her bodyguard and confidant. Her father is older, Lilibet and her older sister being children of a late-in-life second marriage, and your character was never very close to the March, but had a cordial relationship with him (he ultimately paid your wages, after all).
  
Living on the northern border, a bodyguard is important and your life had its exciting moments, like the time you fled back to Evis just behind a tribe of twenty goblins who had caught you and Lilibet out riding, or when you cracked the case of the missing caravan: an innkeeper, charmed by a darkling fey, and misdirected the caravan so it could be plundered by the darklings and the bodies devoured by redcaps.
  
When Lilibet married, and went south to the more settled parts of Maseau, you rejected offers to either stay in the March's employ or head south with Lilibet to what seemed destined to be more of a maid in waiting position than bodyguard.
 
Armed with letters of recommendation from the March and Lilibet, and a broad familiarity with the caravaners and the Bandit's Way, you decided to head north to Sembara and see what fate had in store for you.
%%

%%^Metadata:names:v1%%
- {"name": "Evis", "language": "unknown", "pronunciation": "ay-VEE", "status": "proposed", "notes": "Proposed from the French analogues for southern Sembaran and northern Isinguese in [[Languages]], appropriate regional guidance for Maseau: initial e as ay, v retained, i as ee, silent final s, and final-syllable stress. The name language and whether the final s is sounded are unconfirmed."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1710s description of Evis under the aging Peyre Vayler, whose lordship is attested in DR 1719 in [[Guy de Varan's Story]]; the older character-background alternatives remain unadopted.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added supported persistent name and temporal-viewpoint metadata.
- Added the required settlement map skeleton, leaving its unknown locator blank.

### Validated judgments
- Selected `POV: 1710s` for the aging lord and his daughters; [[Guy de Varan's Story]] attests Peyre Vayler’s lordship in DR 1719.
- The old character-background comment explicitly disclaims canonical status; its alternative personal history and encounters remain unadopted.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has its typed single-location entry, but its `locator` is blank. Supply the verified world-map coordinate in that existing entry; the reviewed text and prepared evidence do not establish a coordinate, so none has been guessed.

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `ay-VEE`. The French analogues for southern Sembaran and northern Isinguese in [[Languages]] supply the strongest regional guidance for Maseau: initial e as ay, v retained, i as ee, silent final s, and final-syllable stress. A sounded final s remains possible; the name language is not established. Confirm or replace the proposal; if accepted, copy the complete pronunciation to frontmatter and mark the existing entry `documented`.
%%^End%%

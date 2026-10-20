---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
displayDefaults: {dPast: "<ancestry:UA> <subtypeof:UA> <typeof:UA> <current:3Frq>, <end:U> by [[Grash]] on <enddate>", wPastHome: ""}
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: town
ancestry: orc
campaignInfo: []
destroyed: 1748-12-11
name: Khumarz
whereabouts: Xurkhaz
dm_owner: tim
dm_notes: color
POV: 1748
---
# Khumarz
>[!info]+ Information
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Khumarz is a fortified border town that serves as a vital outpost for the kingdom of [[Xurkhaz]]. Situated on the banks of the [[Kulthul]] River, it guards the western border of the kingdom against the dangers of the [[Nashtkar]]. The town is enclosed by high walls made of thick stone, with watchtowers strategically placed along the ramparts to provide a clear view of the surrounding wilderness. The gates of Khumarz are guarded by heavily armed [[Orcs]], ever-vigilant against any threat that might arise from the cursed land beyond. The town's buildings are simple and functional, designed for defense and survival rather than aesthetic appeal.
## History
- (DR:: 1748-12-11): Khumarz is destroyed by [[Grash's Horde|Grash's army of undead]] in  [[Battle of the Kulthul]] during the [[War of the Cloak]]

%%^Metadata:names:v1%%
- {"name": "Khumarz", "language": "unknown", "pronunciation": "khoo-MARZ", "notes": "Proposed from the Orcish cultural context and Turkic analogue in [[Languages]]: kh is approximated as a back-of-throat fricative, u as oo, a as open ah, r and voiced z are retained, and stress is final. Turkic does not define one exact spelling system, and the name-specific source language is not established.", "status": "proposed"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the visible description portrays the fortified town before its destruction on DR 1748-12-11, followed by a dated notice of that destruction; the continuing present-tense wording still requires human reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent proposed pronunciation, temporal metadata, and the required map skeleton.

### Validated judgments
- The positive `dm_notes` attestation is supported by the reviewed local-source dossier; no attestation change or private-content promotion was applied.
- [[War of the Cloak]] corroborates the DR 1748-12-11 defeat; [[Session 78 (DuFr)]] separately establishes the preceding western-front crisis. The role and dated destruction are enough for a bounded town entry, subject to the open temporal framing.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has its typed skeleton, but `locations[0].locator` is blank. Supply a verified world-map locator in `{map: world, locator: <verified locator>}`; no coordinate is established by the consulted text sources.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm `khoo-MARZ`, stored as proposed. The Orcish cultural setting and Turkic analogue in [[Languages]] motivate a back-of-throat fricative for kh (reader-facing kh), oo for u, open ah for a, retained r and voiced z, and final stress. Turkic supplies no single exact spelling system; the name-specific source language and phonology remain unknown. Accept or revise, mark an accepted entry documented, and copy the primary pronunciation to frontmatter.

- [ ] **Warning — temporal.mixed_viewpoints:** The description still says Khumarz “is a fortified border town” and that its gates “are guarded,” while frontmatter and History record its destruction on DR 1748-12-11. Choose a coherent historical account or a dated pre-destruction layer. For a historical account, a copy-ready paragraph is: “Before its destruction in DR 1748, Khumarz was a fortified border town that served as a vital outpost for the kingdom of [[Xurkhaz]]. Situated on the banks of the [[Kulthul]] River, it guarded the western border of the kingdom against the dangers of the [[Nashtkar]]. The town was enclosed by high walls made of thick stone, with watchtowers strategically placed along the ramparts to provide a clear view of the surrounding wilderness. The gates of Khumarz were guarded by heavily armed [[Orcs]], ever-vigilant against any threat that might arise from the cursed land beyond. The town's buildings were simple and functional, designed for defense and survival rather than aesthetic appeal.” Alternatively, preserve the existing descriptive paragraph verbatim inside a `Date:1748-12-11b` block and the existing destruction item inside a `Date:1748-12-11` block, using the adopted opening and End markers. These are human proposals because either choice changes temporal framing or filtered visibility; the staged POV records the supported DR 1748 snapshot without claiming a surviving garrison.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 70 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 71 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 72 - DM Notes]]
%%^End%%

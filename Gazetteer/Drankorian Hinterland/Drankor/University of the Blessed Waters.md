---
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [place, status/check/lint]
typeOf: building
typeOfAlias: ruined university
name: University of the Blessed Waters
aliases: [Thalorian]
whereabouts:
  - {type: home, location: Drankor, startFilter: "1"}
dm_owner: tim
dm_notes: important
POV: 1749
---
```taelgar-header
```

The University of the Blessed Waters, also called the Thalorian, was one of the three great universities of [[Drankor]] in the last centuries of the Drankorian Empire. It stood southeast of the [[Temple of the Eight Divines]], amid gardens and lecture halls that once housed a Faculty of Natural History and other schools.

In the present ruins, the university is overgrown and unstable. Its approach leads through jungle‑choked streets to a walled garden marked by two guardian statues, still animated by lingering magic.

%%^Campaign:none%%
### DM notes

- Scrolls recovered from the Custom House in DR 1749 named Minarith as a faculty member here, and the [[Dunmar Fellowship]] later searched his former office while gathering mementos for [[Apollyon's Phylactery]]’s destruction.
- Known as the University of the Blessed Waters, with its elvish roots reflected in its serene, naturalistic design.
- Open courtyards, lush gardens, and elegant stone buildings seamlessly integrated with nature, emphasizing harmony with the world.
- Associated with natural philosophy, astronomy, arts, and literature; its most renowned college, Thalorian, was dedicated to understanding the natural world and the cosmos.
- Water features, such as reflecting pools and flowing channels, crisscross the campus, lending an ethereal tranquility.

%%^End%%

%%^Metadata:names:v1%%
- {"name": "University of the Blessed Waters", "role": "primary", "language": "Common", "status": "inferred", "notes": "Plain-English institutional title; no pronunciation guide is needed."}
- {"name": "Thalorian", "role": "alias", "language": "unknown", "pronunciation": "THAL-or-ee-an", "status": "proposed", "notes": "The alternate name is recorded in [[Session 114 (DuFr)]]. No source-language attribution or explicit pronunciation was found; cautious spelling-based proposal with unvoiced th, short a, initial stress, and separate ee-an ending."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 pre-exploration view of the ruins; the animated guardians belong before the events of May 23, while the university’s institutional history is much older. The later guardian destruction is an open update decision.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added supported persistent name and temporal-viewpoint metadata.

### Validated judgments
- The public university identity and surviving Faculty of Natural History are supported by [[Session 114 (DuFr)]] and [[Session 115 (DuFr)]].
- Confirmed local source matches support the existing positive `dm_notes` attestation; no private contents were promoted.

### Open findings

- [ ] **Warning — coverage.later_material_change:** The present-tense approach describes two guardian statues as “still animated,” but [[Session 115 (DuFr)#Entering the Garden of Statues]] records both statues being destroyed on DR 1749-05-23. This durable change requires a human choice: update the approach, defer with the applicable game-update status, or intentionally retain an earlier snapshot. Copy-ready update: `Its approach leads through jungle-choked streets to a walled garden. Two animated statues guarded the entrance until they were destroyed on DR 1749-05-23.` If retaining both states, propose `%%^Date:1749-05-23b%%` around the existing guardian sentence and `%%^Date:1749-05-23%%` around the destruction sentence; apply those visibility changes only after approval.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or replace `THAL-or-ee-an` for the alternate name Thalorian. [[Session 114 (DuFr)]] records the spelling but no pronunciation or name language; this is a cautious spelling-based reading with unvoiced th, short a, initial stress, and a separate ee-an ending, rather than an established in-world pronunciation. If accepted, mark the existing alias entry `documented`; the primary English title needs no guide.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 114 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 115 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Seven Souls]]
%%^End%%

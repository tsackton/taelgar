---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: hobgoblin
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1749-08-06, type: met}
born: null
gender: female
name: Empress of Chaos
aliases: null
whereabouts:
  - {type: away, start: 1749-08-06, end: 1749-08-06, location: Plaguelands}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1749
---
# Empress of Chaos
>[!info]+ Biographical Info  
> A [[Hobgoblins|hobgoblin]] (she/her)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:DuFr%% Met by the [[Dunmar Fellowship]] on August 6th, 1749 in the [[Plaguelands]] %%^End%%

![[emrpess-of-chaos.png|right|400]]The Empress of Chaos is the leader of the [[Iron Fang]] hobgoblin clan. 

%%SECRET[v2:fbc3e1fc0ae11de672549fdd4f686b00]%%

%%^Metadata:names:v1%%
- {"name": "Empress of Chaos", "language": "Common", "status": "inferred", "notes": "Plain-English descriptive title; the underlying personal name and original language are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early-August DR 1749 leadership snapshot before the Battle of Heartroot Vale; the visible article does not yet incorporate the later outcome.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, including the unambiguous `campaignInfo` alias to `dufr`; added `knownTo: [dufr]`, the descriptive title’s name entry, and a DR 1749 viewpoint with temporal notes.

### Validated judgments
- The plain-English title needs no pronunciation guide.
- Matching local DM sources support `dm_notes: important`. The separate SECRET placeholder has no recoverable content.

### Editorial assessment
**Underdeveloped**: the one-sentence leadership description omits the central purpose of her chaos-metal campaign and her established defeat and death. The smallest useful revision is a short account of that purpose and outcome, with a deliberate temporal treatment of the later event.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** [[Session 129 (DuFr)]] establishes the purpose of the Empress’s campaign through Szoltár’s account, while [[Session 133 (DuFr)]] confirms the attack on the Heartroot. This defining purpose is absent. Candidate addition: “In DR 1749, the Empress led an Iron Fang army toward the [[Aurbez Plateau]]. According to [[Szoltar|Szoltár]], she intended to pierce the [[Heartroot]] with a chaos-metal spear, take control of [[Isingue]]’s magic and its ooze titan, and conquer the lands to the north and west.” Preserve the attribution for the reported wider plan.
- [ ] **Warning — coverage.later_material_change:** [[Session 133 (DuFr)]] and [[Battle of Heartroot Vale]] record her death on DR 1749-08-12 and the defeat of her army. Choose whether to update the article and temporal framing, defer with the applicable game-update tag, or intentionally retain the early-August snapshot. For an update, candidate prose is: “On August 12, DR 1749, the [[Dunmar Fellowship]] killed the Empress at the [[Battle of Heartroot Vale]]. Her armor erupted into an elemental cataclysm, which was destroyed before it could corrupt the Heartroot; the Iron Fang army was routed.” Gate only this later sentence group with `Date:1749-08-12` if preserving the earlier leadership frame, or revise the opening to past tense and record `died: 1749-08-12` in an explicitly retrospective article. No visibility or lifecycle change has been applied.
- [ ] **Warning — consistency.external:** The current `campaignInfo`, whereabouts entry, and generated header put the first encounter on August 6. [[Session 129 (DuFr)]] dates the scouting sighting of the silver-clad commander to dawn on August 7, after the party reached the marshes on August 6. Reconcile these records before changing dates. Candidate if the session chronology is retained: `campaignInfo: [{campaign: dufr, date: 1749-08-07, type: seen}]` and `whereabouts: [{type: away, start: 1749-08-07, end: 1749-08-07, location: Plaguelands}]`; regenerate the matching header.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated header uses `Campaign:DuFr`; [[Campaign Registry]] specifies `Campaign:dufr`. Replace the existing marker’s code with `dufr` when regenerating the header; preserve the block’s boundaries.

### DM evidence
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Leveling]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Empress of Chaos Adventure]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Planning Update - Plaguelands]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 130 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 131 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 132 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 133 - DM Notes]]
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: building
typeOfAlias: manor
ancestry: Drankorian
destroyed: 1740-10-07
name: 27th House
aliases: [Twenty-Seventh House, 27th Room]
whereabouts: Twilight Kingdom
dm_owner: none
dm_notes: none
POV: 1740
---
# The 27th House
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A strange house, north of [[Lord Endless Ending's Manor]] in the [[Twilight Kingdom]]. It is reached by a westward footpath branching from the north road, which runs along a narrowing promontory above cliffs that drop into deep darkness, ending not at a visible building but at a single freestanding door.

The house is a vast magical and mechanical prison built by the [[Arithrimos Lamperum]] around a central prison chamber of cold-iron holding the [[Prisoner in the 27th Room]]. Its chambers rotate around the central prison as beings move through the rooms and passages of the building; each rotation, driven by the unpredictable choices of mortals, shifts the prison's position in space or time. This keeps the captive from anticipating where or when it would be and growing through the walls to freedom. 

The surrounding house also functions as a [[Arithrimos Lamperum]] workshop and outpost, with laboratories, archives, map collections, a chapel, and living quarters.

%%^Date:1740-10-07%%
In DR 1740, the 27th House was destroyed when the prisoner [[Lost in the Feywild - Episode 07|released the souls that powered the complex]]. It burst through the central chamber, causing the surrounding structure to collapse and slide over the cliffs into the ravine. All that still remains of the complex on the [[Twilight Promontory]] is a strange bottomless well.
%%^End%%

%%^Metadata:names:v1%%
- {"name":"27th House","language":"unknown"}
- {"name":"Twenty-Seventh House","role":"alias","language":"unknown"}
- {"name":"27th Room","role":"alias","language":"unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the undated description presents the intact prison and outpost before its destruction in DR 1740; the existing dated passage presents the later collapse, with its one-day chronology difference unresolved.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent name entries for the primary name and its two existing aliases.
- Added a DR 1740 viewpoint and temporal interpretation distinguishing the intact-house description from the dated destruction.

### Validated judgments
- The prison mechanism, workshop role, and destruction provide a sufficient reference account; [[Lost in the Feywild - Episode 07]] corroborates the collapse and the prisoner's departure.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** `destroyed: 1740-10-07` and the existing destruction block use October 7, but [[Lost in the Feywild - Episode 07]] dates the release and collapse to DR 1740-10-06. [[Twilight Promontory]] also uses October 7. Reconcile the one-day difference across those references rather than choosing a date automatically. If the played date is adopted, the copy-ready metadata is `destroyed: 1740-10-06` and the block opener is `%%^Date:1740-10-06%%`; otherwise correct the session chronology through its owning workflow. Changes to date-block visibility remain a human decision.
- [ ] **Warning — temporal.mixed_viewpoints:** The unscoped descriptions beginning “A strange house,” “The house is a vast magical and mechanical prison,” and “The surrounding house also functions” present an intact, operating complex, while the dated final paragraph says it collapsed. The new POV records the pre-collapse view but does not control filtered visibility. After resolving the date above, consider wrapping the three intact-house paragraphs in a before-date block. Copy-ready structure using the currently recorded boundary: `%%^Date:1740-10-07b%%`, followed by those three paragraphs unchanged, then the standard closing End sentinel. If October 6 is adopted, use `%%^Date:1740-10-06b%%` instead. Preserve the existing destruction passage and use matching old/new cutoffs.
%%^End%%

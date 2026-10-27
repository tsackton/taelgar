---
lintedAt: "2026-10-20T07:49:48-04:00"
lintVersion: "3.5"
tags: [object, status/check/lint]
typeOf: shield
subTypeOf: magical
ancestry: dwarven
image: "[[brawnanvil-shield.png]]"
name: Shield of the Brawnanvil Clan
aliases: [Brawnanvil Shield]
whereabouts:
  - {type: home, location: Brawnanvils, linkText: by, format: "<name:q>"}
  - {type: away, start: 1547-01-01, end: 1748-04-12, location: "Dwarven Outpost (Raven's Hold)"}
  - {type: away, start: 1748-04-12, end: 1748-05-09, location: Riswynn}
knownTo: [dufr]
dm_owner: tim
dm_notes: none
POV: modern
---
```taelgar-header
```

![[brawnanvil-shield.png|right|350]]The Shield of the Brawnanvil Clan is an elaborate decorative shield of polished steel, worked with scenes from dwarven life. It is a Brawnanvil family heirloom, not a practical battle shield, whose magic draws a dwarf holding it into a recreation of a story from the Brawnanvil past; a Brawnanvil can guide the vision toward a particular memory or place.

The shield was lost in the [[Dwarven Outpost (Raven's Hold)|dwarven outpost near Raven's hold]] when the Brawnanvils and other dwarves fled during the [[Great War]]. [[Riswynn]] recovered it in DR 1748 and returned it to the Brawnanvils in [[Tharn Todor]].

## Chronology of the Shield

- (DR:: 1544): The Brawnanvils flee the [[Dwarven Outpost (Raven's Hold)]] during the upheavals around the [[Great War]], leaving the shield sealed in the Brawnanvil vault. %% Date follows [[Eberk Brawnanvil]]'s recorded departure from Raven's Hold, but might be imprecise; assumption is dwarves fled under attack from mind flayers and others and could not get to the vault. %%
- (DR:: 1748-04-05): [[Riswynn]] meets the [[Dunmar Fellowship]] in [[Karawa]] while seeking companions to help recover the shield from [[Raven's Hold]].
- (DR:: 1748-04-12): [[Riswynn]] recovers the [[Shield of the Brawnanvil Clan]] from the sealed Brawnanvil vault in the [[Dwarven Outpost (Raven's Hold)]].
- (DR:: 1748-04-13): [[Riswynn]] shows the shield to a damaged dwarven stone construct guarding the outpost forge and mines; the construct recognizes or accepts its authority and lets the party pass.
- (DR:: 1748-04-16): [[Riswynn]] parts ways with the [[Dunmar Fellowship]] after [[Stormcaller Tower]] and heads home to [[Tharn Todor]] with the Brawnanvil clan artifacts.
- (DR:: 1748-05-05): [[Riswynn]] arrives in [[Tharn Todor]] with the shield, and returns it to the clan elders.

%%^Metadata:names:v1%%
- {name: "Shield of the Brawnanvil Clan", language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern description of the shield after its return to the Brawnanvils in DR 1748, with selected earlier history; the precise loss and return boundaries in the whereabouts metadata need reconciliation with the chronology.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added `knownTo: [dufr]`, primary name metadata, and the broadly modern article viewpoint with its temporal coverage limits.
- Removed the duplicated outer parentheses around the 1544 chronology date, preserving the `(DR:: 1544)` annotation and its value.

### Validated judgments
- The reviewed external DM accounts duplicate recovery and return information already captured in the shared record; `dm_notes: none` is preserved.

### Open findings

- [ ] **Warning — correctness.internal_conflict:** The outpost whereabouts starts at `1547-01-01`, but the first chronology entry places the shield’s loss in 1544, explicitly using [[Eberk Brawnanvil]]’s departure as an uncertain proxy. Eberk’s note distinguishes his 1544 departure from his 1547 arrival in Tharn Todor; neither event independently dates the shield’s loss. The Riswynn whereabouts also ends at `1748-05-09`, while the final chronology entry says she returned the shield on `1748-05-05`, the arrival date recorded in [[Riswynn]]. [[Oskar in Tharn Todor]] dates a later tavern meeting to May 9, rather than establishing the return on that date. Confirm the intended boundaries and reconcile metadata and chronology together. If adopting the chronology’s existing interpretation, copy-ready field replacements are `start: 1544` for the outpost entry and `end: 1748-05-05` for the Riswynn entry; preserve the comment that 1544 is an uncertain proxy. Otherwise revise the chronology to match the chosen history without treating either precise metadata date as independently established.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: dwarf
ancestry: null
born: 1589
gender: female
name: Vistra Fireforge
affiliations:
  - {org: The Iron Swan, title: Proprietor, type: leader, start: 1700}
whereabouts:
  - {type: home, start: "", end: "", location: Nardith}
  - {type: home, start: 1620-01-01, end: "", location: "Ausson's Crossing"}
  - {type: home, start: 1730-01-01, end: "", location: Tokra}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Vistra Fireforge
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% needs dunmar campaign info in header; tim has some color notes from her later years in Tokra to add  %%

![[vistra-fireforge-innkeeper.png|right|250]]A dwarven blacksmith, trader, innkeep, and adventurer. She is of the Traveler thuhr and originally from [[Nardith]]. She was born after the [[Great War]] and has always been eager to work with humans. She is charming and pleasant enough, but perhaps not that bright and she sometimes makes mistakes in her trades, although she rarely wants to believe it.



![[vistra-fireforge-smith.png|left|300]]
In her youth she was a blacksmith and trader in [[Ausson's Crossing]], a crossroads inn south of [[Sembara]]. She is now settled in [[Tokra]] where she runs the dwarven inn, [[The Iron Swan]].



%% One Note

The innkeeper and owner of the Iron Swan, a dwarven tavern and inn in Tokra, in the dwarvish quarter behind the archives.
 
Originally from the Yuvanti mountains, but was an adventurer for many years, now retired.
 
Fairly old, late middle aged, maybe around 200. Born in the unsettled time after the Great War, one of the first generations born in the Yuvanti mountains and the Kingdom of Nardith.

%%

%%^Metadata:names:v1%%
- {name: "Vistra Fireforge", language: "unknown", pronunciation: "VIHS-trah FY-er-forj", notes: "Proposed using the Dwarvish analogue in Languages and the attested Vistra naming form in Dwarves; short i, sounded v and str, full final a, and tentative initial stress, with an ordinary English reading of Fireforge. The complete name language is not expressly attested.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of Vistra as the settled innkeeper in Tokra, with selected earlier blacksmithing and trading history; the intervening adventuring years are not comprehensively described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Recorded supported campaign knowledge in `knownTo`, the article viewpoint in `POV`, and its temporal limits in `povNotes`.
- Added a primary name entry with a proposed pronunciation; retained `language: unknown` because the complete name’s language is not expressly attested.
- Inserted the missing comma before the appositive describing Ausson’s Crossing.

### Validated judgments
- The Tokra innkeeper role and retired adventurer identity are corroborated in [[The Iron Swan]] and [[Session 38 (DuFr)]].
- Status disposition: `status/cleanup/metadata` is not assessable after the mechanical fixes; the authored reminder may include further intended campaign-header work, so the tag is preserved.
- The matched local sources support the positive `dm_notes` attestation; the field is preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed `VIHS-trah FY-er-forj` in `Metadata:names:v1`. Vistra appears in the [[Dwarves]] female-name list; the [[Languages]] analogue is Tolkien Dwarvish. The proposal uses short i, pronounced v and str, a full final a, and tentative first-syllable stress; the transparent surname uses its ordinary English reading. The analogue guides the proposal without establishing exact in-world phonology. Accept it by changing the entry to `status: documented` and copying the pronunciation to frontmatter, or revise it.
- [ ] **Suggestion — editorial.shared_material_redundant:** The final shared `One Note` comment repeats the visible account of owning the Iron Swan, origin in Nardith/Yuvanti, earlier adventuring, and birth after the Great War. Remove the repeated statements while retaining the distinct tentative age and early-generation guidance: `Old notes describe Vistra as late middle-aged, perhaps around 200, and among the early generations born in Nardith after the Great War. Reconcile the rough age estimate with born: 1589, which implies about 159 in DR 1748, before adopting it.` Keep this as editorial guidance until resolved; do not silently adopt the rough age estimate.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
%%^End%%

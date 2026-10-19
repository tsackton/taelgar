---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:07:38-04:00"
lintVersion: "3.5"
displayDefaults: {wOrigin: "Home area: <origin>", ruledBy: "<affiliationtitle:t>: <name> <(of )primary>", wHome: "", wCurrent: "Current location: <current:3Frq>"}
tags: [object, testcase, status/check/lint]
typeOf: vehicle
typeOfAlias: boat
ancestry: halfling
name: Wave Dancer
whereabouts:
  - {type: home, end: 1, location: Eastern Green Sea}
  - {type: away, start: 1748-09-30, end: 1748-10-11, location: sailing to Wahacha, startFilter: "2"}
  - {type: away, start: 1748-10-12, end: 1748-10-14, alias: main port of Wacahca, location: Wahacha, linkText: moored in, format: "<name:q>", startFilter: "2"}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# The Wave Dancer
>[!info]+ Information  
> ([[Halflings|halfling]] boat)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A halfling ship plying the trade routes of the eastern Green Sea, regularly visiting [[Praznitsky]], [[Wahacha]], [[Quanyi]], and [[Medju]].  
## Crew
[[Wella Brightmoon]], captain and matriarch of the family
[[Rose Brightmoon]], musician and Wella's wife
[[Pearl Brightmoon]], first mate and captain of the guard
[[Corrin Wildheart]], navigator
[[Lerry Wildheart]], quartermaster

![[wave-dancer-1.png|500]]

%% old notes from OneNote
Main people:

Captain - Wella Brightmoon, matriarch of the Brightmoon clan, sailing all her life, old and stiff and getting slow but her weather sense is deeply respected by the crew

Musician - Wella's wife Rose Brightmoon, brilliant guitarist

First mate and captain of the guard - Pearl Brightmoon, a cousin, buff, good with a rapier

Navigator - Corrin Wildheart, married into Brightmoon clan 15 years ago, his wife and young son are on board as well. Smart, has a touch of weather magic.

Quartermaster - Lerry Wildheart, Corrin's younger brother, taken on as apprentice and now thrust into role after the former quartermaster, Poppy Brightmoon, left to seek adventure two years ago.

%%

%%^Metadata:names:v1%%
- {"name": "Wave Dancer", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the late-1740s trading ship and crew, corroborated by the September–October DR 1748 voyage; earlier and later crew arrangements are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added supported `knownTo`, primary name metadata, `POV`, and `povNotes`.
- Added the explicit subject name and corrected `matriach` to `matriarch` in the visible crew list and ordinary comment.

### Validated judgments
- The route and crew are corroborated by [[Session 60 (DuFr)]] and the linked crew biographies. The late-1740s viewpoint describes the crew in that voyage period; no later service is inferred. Confirmed local source matches support the positive `dm_notes` attestation.

### Open findings

- [ ] **Suggestion — editorial.shared_material_redundant:** The ordinary comment beginning “old notes from OneNote / Main people” repeats all five names and roles in the visible Crew section; much of its biographical color is also in the linked crew notes. Remove the repeated roster after review, retaining the distinct family and apprenticeship context. A bounded replacement comment is: `%% Crew context, DR 1748: Corrin married into the Brightmoon clan about fifteen years earlier; his wife and young son also sail aboard the Wave Dancer. Lerry was apprenticed to Poppy Brightmoon before she left to seek adventure about two years earlier. %%` This retains the original context without promoting it to public prose.
- [ ] **Suggestion — metadata.whereabouts_name_spelling:** The 1748-10-12 whereabouts entry uses `alias: main port of Wacahca` for `location: Wahacha`. [[Session 60 (DuFr)]] and the article’s route use Wahacha. Confirm the display spelling; the copy-ready correction is `alias: main port of Wahacha`, leaving the location, dates, filters and format unchanged.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Timelines - Solo Arcs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Prequel - Wellby]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Wave Dancer's Information]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Wellby Solo Arc]]
%%^End%%

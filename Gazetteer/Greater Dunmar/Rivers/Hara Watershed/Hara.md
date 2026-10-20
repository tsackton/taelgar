---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Hara
pronunciation: HAH-rah
whereabouts: Hara Watershed
dm_owner: tim
dm_notes: color
POV: modern
---
# Hara
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Hara flows 750 miles through the [[Hara Basin]], from its source in the foothills of the [[Sentinel Range]] to the [[Hara Gorge]]. Once, it flowed more than twice that length in total, joining the [[Istaros]] north of [[Drankor]]. Whether it still does after the cataclysms and upheavals following the [[Great War]], no one knows.

At its source, the Hara is a swift flowing mountain river, descending to the flat plains of the [[Hara Basin]]. As the Hara enters the [[Hara Basin]], it slows and widens as it meanders south towards [[Tokra]], joined first by the [[Sone]] and then by the [[Thandar]], along with several minor tributaries.

South of the confluence with the [[Thandar]], the Hara turns broad and sluggish as it flows through the [[Varashan]]. Here, the Hara frequently floods during the monsoon season. 

The region in the immediate vicinity of [[Tokra]] is rocky and hard, especially just south of the city, where the rocky land of the [[Darba Highlands]] protrudes into the [[Hara Basin]]. Here, the river widens again as it passes beneath the Tokra Bridge. 

South of [[Tokra]], the river passes through a series of small canyons on the rugged [[Sukal Plains]]. The [[Sukal]] joins between [[Tokra]] and [[Askandi]], and a number of dry washes and seasonal rivers flow into the Hara in this stretch during the monsoon. 

Just north of [[Askandi]], the terrain levels, and the Hara pursues a slow, twisting path southeast. [[Askandi]] sits on the floodplains of the [[Lower Hara Valley]], a wide flat basin between the [[Yuvanti Mountains]] and the [[Garamjala Plateau]]. Here, virtually no rain falls, even during the monsoon, but the flood of the Hara, swollen from monsoon rains to the north, sustains a rich riparian ecosystem and the city of [[Askandi]] itself.

Beyond [[Askandi]], the land begins to rise again as the [[Garamjala Plateau]] joins the [[Yuvanti Mountains]]. This is a land of dry desert canyons, as the Hara narrows again as it cuts through the [[highlands]] via the [[Hara Gorge]].

Beyond the [[Hara Gorge]], no one knows the fate of the river. Does it feed a seasonal lake in the depths of the [[Garamjala Desert|Garamjala]]? Does it flow all the way through the plateau to join the [[Istaros]], as it once did? Or does something stranger happen?
## In Dunmari Culture

The Hara is a central river of Dunmari myth and culture. Before the [[Great War]], when the Dunmari settled in this land, the two great rivers of the Hara and the [[Kharja]], collectively known as Jeevali's Tears, provided water and sustenance to much of the people of the [[Hara Basin]]. Before the [[Yuvanti Mountains]] and the [[Garamjala Plateau]] were raised, these rivers were separated only by the high land around [[Karawa]], and the monsoons swept across the entire plains, supporting a rich grassland ecosystem.

Since the [[Great War]], the [[Kharja]] has nearly or completely dried up. None have traced its route into the [[Garamjala Desert|Garamjala]], but even near [[Kharsan]] it flows only fitfully, in sudden floods after rare storms, and it is presumed it no longer meets the Hara. 

The Hara has thus taken on greater significance for the Dunmari. Without it, life would not be possible in the [[Hara Basin]]. 

%% notes

Starts in the [[Sentinel Range|Sentinels]], where its main tributaries join north of [[Tokra]] ([[Sone]] and [[Thandar]])
Flows past [[Tokra]]; from [[Tokra]] south to [[Askandi]] most tributaries are seasonal, except for a few small rivers with sources in the [[Copper Hills]]
Past [[Askandi]], enters the Hara River Gorge between the Yuvanti and the [[Garamjala Plateau]]
Once, it flowed south to join the [[Istaros]] north of [[Drankor]], but whether it still does is anyone's guess

Real world: Indus River Valley, Brahmaputra River Basin, general area of the [Indo-Gangetic Plain](https://en.wikipedia.org/wiki/Indo-Gangetic_Plain)

%%

%%^Metadata:names:v1%%
- {name: Hara, language: Dunmari, pronunciation: HAH-rah, notes: "Documented in [[Hara Watershed]] for the river-name form.", status: documented}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: , map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern, describing the post-Great-War river and its seasonal flow; earlier courses are historical, and the present course beyond the Hara Gorge remains uncertain.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order while preserving its existing values and `headerVersion`.
- Added the documented pronunciation `HAH-rah` and a persistent Dunmari name entry from [[Hara Watershed]].
- Added the required two-ended waterway map skeleton, leaving unestablished coordinates blank.
- Added `POV: modern` and a temporal note distinguishing the present river from its historical course and unresolved downstream geography.
- Removed the duplicated space in “the  flat plains” and trailing whitespace on that changed line.

### Validated judgments
- The geographic and cultural account performs the river's reference role; [[Hara Basin]], [[Hara Watershed]], [[Istaros]], and [[Garamjala Desert]] corroborate its regional setting and the uncertainty of its modern downstream course.
- The historical account in [[Report of the Aagiri to Samraat Dasa]] and its later editorial observations do not establish a complete modern route or outlet. The uncertainty is preserved rather than resolved by inference.
- Confirmed local DM evidence supports the existing positive `dm_notes: color` attestation; the attestation and `dm_owner` are preserved.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The source and outlet `locator` values in `Metadata:map:v1` remain blank. The article locates the source in the [[Sentinel Range]] foothills but does not establish an exact world-map position, and the modern outlet remains uncertain. Supply verified positions for the existing `role: source` and `role: outlet` entries when known; retain `map: world`. No coordinate can safely be supplied from the consulted text, and the former confluence with the [[Istaros]] must not be substituted for an unverified modern outlet.

- [ ] **Warning — link.incorrect_target:** In the paragraph beginning “Beyond [[Askandi]],” the phrase “cuts through the [[highlands]]” resolves to [[Highlands]], a region of [[Sembara]] north and west of Cheimen. This paragraph instead describes the meeting of the [[Garamjala Plateau]] and [[Yuvanti Mountains]]. Remove that misleading link without changing the geography: replace `the [[highlands]] via the [[Hara Gorge]]` with `the highlands via the [[Hara Gorge]]`.

- [ ] **Warning — correctness.cross_note_conflict:** The final cultural paragraph says that the [[Kharja]] is “presumed” no longer to meet the Hara, consistent with the suspected lost confluence in [[Garamjala Desert]]. The visible sentence in [[Kharja]] instead describes its now-mostly-dry riverbed as “eventually joining with the [[Hara]] river.” Decide whether that sentence describes the former course or an established present connection. If it describes the former course, a bounded candidate for [[Kharja]] is: “The Kharja is a now mostly dry riverbed that flows past [[Kharsan]]. Its former course joined the [[Hara]], but it is suspected to peter out before reaching that confluence.” Preserve Hara's stated uncertainty unless an appropriate source establishes a present connection; this proposal does not adopt a new outlet.

- [ ] **Suggestion — editorial.shared_material_redundant:** The closing notes comment repeats the visible source, north-of-Tokra tributaries, Tokra–Askandi route, gorge, and former Istaros connection. Retain its distinct Copper Hills detail and real-world editorial references rather than maintaining a second route summary. Keep the existing comment wrapper and replace only its contents with:

  ```text
  notes

  From [[Tokra]] south to [[Askandi]], most tributaries are seasonal, except for a few small rivers with sources in the [[Copper Hills]].

  Real world: Indus River Valley, Brahmaputra River Basin, general area of the [Indo-Gangetic Plain](https://en.wikipedia.org/wiki/Indo-Gangetic_Plain)
  ```

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Nayan Sura]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Festival Visitors and NPCs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 17]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Session 9]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Copper Hills (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 42]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 26-1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 29]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Lakan Monastery/Lakan Monastery (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 33]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 34]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Dunmari Magic - Old Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 104 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Desolation of Cha'mutte Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
%%^End%%

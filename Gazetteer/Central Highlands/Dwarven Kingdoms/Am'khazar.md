---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: realm
ancestry: dwarven
name: "Am'khazar"
whereabouts:
  - {type: primary, location: Labkhan}
  - {type: secondary, location: Central Highlands}
dm_owner: tim
dm_notes: important
POV: modern
---
# Am'khazar
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% copy over notes from OneNote from Great Library dwarf kingdom arc, Brelith backstory %%

The Kingdom of Am’khazar has always been a quiet but wealthy kingdom. During the height of the five kingdoms before the [[Great War]], it was never as powerful as [[Khatridun]], and in the years since it has not risen to the heights of [[Nidzahar]]. But the Am’khun have always been quietly prosperous off their rich mineral wealth, which they trade primarily with other [[Dwarven Kingdoms]]. The kingdom of Am’khazar is in many ways the most Dwarvish of all the five kingdoms, seeming untouched by time or the world shaking events around it, always content to continue their traditional ways and live life as they always have lived.

%%^Metadata:names:v1%%
- {name: "Am'khazar", language: unknown, pronunciation: ahm-KAH-zahr, meaning: rich-iron-mountains, status: proposed, notes: "The meaning is approximate, as recorded in [[Dwarven Kingdoms]]. Pronunciation proposed from the Dwarvish cultural context and the Tolkien Dwarvish analogue in [[Languages]]: open ah vowels, kh read as an aspirated k, voiced z, and tentative stress on the first syllable of khazar. The name's language and exact in-world phonology are not explicitly recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern account of the kingdom's mineral wealth and traditional character, with comparisons before and after the Great War; the DR 1747 cold crisis is not yet incorporated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter while preserving its parsed values and header version.
- Added a primary name entry with the documented approximate meaning and a proposed pronunciation, and recorded the broadly modern viewpoint and temporal coverage.

### Validated judgments
- The existing source-transfer comment remains an editorial pointer rather than public article text.
- The modern economic and cultural overview is supported by [[Dwarven Kingdoms]]; the recent cold crisis is established by [[Great Library Session Notes - Arc 3]].

### Editorial assessment
**Underdeveloped**: The realm's account lacks its defining geographic and settlement context and omits the established DR 1747 cold crisis that forced the abandonment of a southern city. The smallest useful scope is one short paragraph locating the kingdom and its City of Gems, followed by a concise historical paragraph recording the crisis and its resolution.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The article describes mineral wealth and tradition but does not identify the kingdom's position or any settlement through which that wealth is understood. [[Dwarven Kingdoms]] places Am'khazar west of [[Khatridun]] and names the deep mines and gemstone trade of [[Zarkandur]]; [[Zarkandur]] describes the underground City of Gems. Add this geographic anchor: “Am'khazar lies west of [[Khatridun]] in the [[Sentinel Range|Sentinels]]. Its deep mines and the gemstone trade of [[Zarkandur]], the City of Gems, are central to its mineral wealth.”
- [ ] **Warning — coverage.established_fact_missing:** The phrase “seeming untouched by time or the world shaking events around it” is left as the whole recent account, omitting the cold crisis that displaced a settlement. [[Great Library Session Notes - Arc 3]], especially sessions 42–51 and the December DR 1747 timeline, establishes the frozen, abandoned [[Tumukhar]], the cause of the cold, and the ending of the curse. Add a bounded account of that durable regional consequence: “In DR 1747, unnatural cold spread into Am'khazar from the mountains to the south, forcing the abandonment of [[Tumukhar]]. [[Morgana Stoneclaw|Morgana Frostclaw]] was directing the ice magic behind the cold from beneath [[Vangebekkr]]. The curse ended after the [[Silver Tempests]] killed her in December DR 1747.” Do not imply that ending the curse immediately restored the abandoned city; [[Tumukhar]] still describes plans for resettlement in DR 1748.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm or revise the proposed pronunciation `ahm-KAH-zahr` in the primary name entry. It uses the Tolkien Dwarvish analogue in [[Languages]] for the dwarven naming context: open ah vowels, `kh` read as an aspirated k, voiced z, and tentative stress on the first syllable of `khazar`. The analogue does not establish the name's exact language or in-world phonology. If accepted, add `pronunciation: ahm-KAH-zahr` to frontmatter and mark the primary entry documented; retain the approximate meaning recorded in [[Dwarven Kingdoms]].
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: important`. The human attestation may represent remembered information or an off-vault source. Keep it unless a human confirms a different value; the existing OneNote-transfer reminder identifies work to investigate.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr}
born: 1702
activeYear: 1722
gender: male
name: Kirian
affiliations:
  - {place: "Kirian's", title: Proprietor, start: 1}
whereabouts: Tokra
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Kirian
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A retired Dunmari soldier who spent his early twenties riding in the warband of [[Shandan]], a charismatic soldier, traveling in the [[Myraeni Gap]] and elsewhere. Wounded in a skirmish with [[Kobolds]] in DR 1728, and returned to [[Tokra]].

Now runs an inn, [[Kirian's]], near the Trader's Market in [[Tokra]]. 

%%^Campaign:dufr%%
[[Kenzo]] listened to his story and collected it for the [[Order of the Awakened Soul]]: [[Kirian's Story]]
%%^End%%


%% story

[[Kirian]], the innkeeper of the eponymously named [[Kirian's]] in [[Tokra]], grew up in [[Tokra]], and rode off in his youth with a war band, raiding [[Kobolds]] along the [[Myraeni Gap]] to the west, around [[Songara]], until he was wounded in an ambush. After that he returned to [[Tokra]] with his gold and treasure, and opened the inn. That was maybe 15 years ago, and now he is proud of what he built, and enjoys reminiscing about the time in camp with his companions, talking and laughing about what they would do with all the gold they would find. 

%%

%%^Metadata:names:v1%%
- {name: Kirian, language: unknown, pronunciation: kee-ree-AHN, status: proposed, notes: "Proposed from the Dunmari cultural context and the Persian analogue in [[Languages]]; the name's language is not independently documented."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740s portrait of Kirian as a retired soldier running his inn in Tokra, with selected earlier military history; the source’s approximate inn-opening recollection is not an exact date for his injury.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected the typo “solider” to “soldier.”
- Normalized the campaign opener from `Campaign:DuFr` to `Campaign:dufr`; case-insensitive filtering preserves the block’s visibility and contents.
- Added `knownTo: [dufr]`, normalized the existing campaignInfo code and frontmatter formatting, and recorded proposed name pronunciation and a DR 1740s article viewpoint.

### Validated judgments
- The soldier-to-innkeeper account is sufficient for this minor reference subject; [[Kirian's Story]] and [[Kirian's]] corroborate his role.
- `status/cleanup/metadata`: supported while name review remains open; retained unchanged.
- Confirmed local source matches support the positive `dm_notes` attestation; private contents remain outside this report.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or correct the proposed pronunciation `kee-ree-AHN`, then record the accepted primary form in frontmatter and mark the name entry documented. The Dunmari guidance in [[Languages]] permits Hindi or other Indo-Iranian (Persian) models; this proposal favors a Persian reading with hard k, separate ee vowels, an open ah final vowel and final stress. A Hindi-influenced reading could reduce the final vowel or move the prominence, so this is a proposal rather than recorded in-world phonology. The language of this particular name remains unknown.
- [ ] **Suggestion — editorial.shared_material_redundant:** The ordinary comment labeled “story,” beginning “[[Kirian]], the innkeeper,” repeats the soldier, injury, return and inn history already visible and duplicates the linked [[Kirian's Story]] verbatim. Remove that duplicate comment and keep the existing source link. Its distinct reminiscence and approximate inn-opening date remain available in that source.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 41]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Kenzo (OneNote)]]
%%^End%%

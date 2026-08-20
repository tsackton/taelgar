---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T19:08:29-04:00"
lintVersion: "2.4"
tags: [person, status/cleanup/metadata, status/cleanup/text, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, person: Delwath, date: 1748-10-12, type: scryed}
born: 1691
gender: male
name: Kaeso
pronunciation: KAI-soh
affiliations: [Shakun Mystai]
whereabouts:
  - {type: home, end: 1712, location: Chardon}
  - {type: away, start: 1713, prefix: traveling in, location: Dunmar}
  - {type: away, start: 1717, location: Karawa}
  - {type: away, start: 1719, location: Taelgar, prefix: traveling widely across, format: ""}
  - {type: home, start: 1723, end: 1748-09-09, location: Chardon}
  - {type: away, start: 1748-09-10, location: fleeing the Chardonian Empire}
  - {type: away, start: 1748-10-12, location: Hamri, wLastKnown: ""}
knownTo: [mawar, dufr]
dm_owner: tim
dm_notes: important
POV: 1749
---
# Kaeso
>[!info]+ Biographical Info
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%%^Campaign:dufr%%
Scryed with [[Delwath]] on October 12th, 1748 in [[Hamri]], the [[Mawar Confederacy]]
%%^End%%

%% clean up campaign info and text, add image, copy various notes from Kenzo brainstorming in DM folder %%
![[kaeso.png|right|400]]
[[Kenzo]]'s mentor and friend. A Chardonian, but widely traveled. Former student of [[Roscelia]] and member of the [[Society of the Open Scroll]], but expelled for keeping secrets, specifically about Dunmari magic. 

Secretly a member of the [[Shakun Mystai]]. 

%% One Note

## Two-Note Summary
 
**Purpose:** ally to Kenzo, information-giver and supporter  
**Trait (Value):** The exploitation and commercialization of magic in Chardon is a mistake. This manifests both in his doubts about the Society of the Open Scroll and its mission to learn everything about everything; and in his concern about the influence of chalyte on the imperial side of things.
 
Kenzo's mentor/patron/protector in Chardon. Lives in the Panemsgate neighborhood, south of the [[Kylos Market]].
 
Trained at the university, including higher learning from the faculty of Magic, but never a great caster [he is probably something like a level 3-5 melee bard], more an adventurer type, "practical magician". After his training, left to seek knowledge elsewhere, eventually ending up in Karawa and joining the Shakun Mystai.
 
When he returned, he refused to speak of his travels, holding is oath to the Mystai sacred. Was expelled from the Society of the Open Scroll for this, and left the academy, although retains some old contacts, especially his master from his university days, Roscelia.
 
## Appearance
 
In his late 50s - some wrinkles but still a lively face, scraggly black hair, and a few day's stubble. Olive skin, plain dress.
 
## Mannerisms
 
Uses his hands a lot - for emphasis, also to pull people close, create space.
 
## Motives
 
He is fully on Kenzo's side, just wants him to thrive. Has already burned most of his bridges in the academy so not concerned about burning more.
 
He still respects some people in the Society and especially at the University, but can't agree with the combination of arrogance and passivity - wishes the Hetaeri Magica and others would take a more active role against the chalyte trade, instead of just looking down on it. Even maybe helping those who burn themselves out using it, doing something to stop overdoses and deaths.
 
But these days his focus and concern is really on the political side of things -- control of the chalyte trade consolidated under the Auratan family has given them too much power.

%%

%%
AI NPC proposal - Mawar review, 2026-05-07

Proposed whereabouts/metadata updates:
- Existing whereabouts already places Kaeso in [[Hamri]] starting DR 1748-10-12. Consider confirming this line through at least DR 1749-05-26, since Mawar Episode 05 lists him as a Chardonian scholar recently staying in Hamri.
- Add campaignInfo for Delwath's later February DR 1749 scrying: Kaeso is seen with [[Yaz]] on a tower overlooking stormy ocean, and later in a cozy rented room or lodging.
- Add campaignInfo or a note for Mawar Episode 05 if you want Mawar visibility distinct from DuFr scrying.

Proposed text updates:
- Add Mawar-side text from the Ep05 intro draft: Kaeso arrived in Hamri at the start of October DR 1748, brought warnings about Chardon's greed for magic and chalyte overuse, and spent long evenings talking with [[Wazir]].
- Add that he was distressed by news from Dunmar during the winter of DR 1748-1749, but later said Dunmar held.
- Keep deeper Kenzo/Shakun Mystai material in DM notes or carefully player-facing sections, depending on what Kaeso has revealed in play.

Source links:
- [[Mawar Adventures Episode 05]]
- [[Mawar Ep 5 - Intro Draft]]
- [[Scrying Delwath Oct 21]]
- [[Scrying Delwath Tollen Downtime]]
- [[Yaz]]
- [[Wazir]]
%%

%%^Metadata:names:v1%%
- {name: Kaeso, role: primary, language: Chardonian, pronunciation: KAI-soh, status: proposed, notes: Chardonian uses Latin and Italian analogues; ae is read as a diphthong and the opening consonant remains hard. An Italianized KAY-zoh is a plausible alternative if intervocalic s is voiced.}
%%^End%%

%%^Metadata:article:v1%%
mode: campaign-aware character reference
povNotes: The visible biography is a late-1748 to 1749 snapshot. Kaeso's whereabouts in Hamri and later scrying appearances need consolidation before the note can reliably answer where he is within that interval.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Open findings

- [ ] **warning — name.pronunciation_missing:** KAI-soh is the preferred analogue-informed proposal. [[Languages]] maps Chardonian to Latin and Italian; the proposal gives ae its Latinate diphthong, keeps the opening consonant hard, and uses two syllables. KAY-zoh is a plausible more Italianized alternative if intervocalic s is voiced. If the preferred form is accepted, copy pronunciation: KAI-soh and change the name entry to status: documented.
- [ ] **suggestion — coverage.campaign_update:** The visible biography and campaign metadata do not yet consolidate the later Mawar stay and DuFr scrying material already listed in the shared review comment. Copy-ready visible candidate from [[Mawar Adventures Episode 05]]: By DR 1749, Kaeso was staying in [[Hamri]], where he had warned local leaders about Chardon's exploitation of magic and the dangers of chalyte. The exact date for the later February scrying remains unresolved, so no additional campaignInfo row should be copied until it is confirmed.

### Applied changes

- Canonicalized frontmatter; normalized knownTo and campaignInfo to registered mawar and dufr codes; moved the Campaign:dufr block below the complete header callout; and added POV: 1749 plus persistent proposed-name/article metadata.

### Validated

- The existing positive dm_notes value is supported by [[_DM_/Timelines/NPC Travels|NPC Travels]], [[_DM_/Timelines/Old Timeline (Table)|Old Timeline]], [[_DM_/Timelines/Unified Timeline From OneNote|Unified Timeline From OneNote]], [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Chardon NPC Flowchart|Chardon NPC Flowchart]], [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 48|Session 48 DM source]], [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 49|Session 49 DM source]], [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Hralgar (Session 62- )/Session 62/Session 62 1|Session 62 DM source]], [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime|Session 32 Downtime]], [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part III Saving the Te'kula/Arrival|Elderwood Arrival]], [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Calendar Eras - DuFr Player Background|Calendar Eras]], [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Dates - Dunmar Campaign Player Background|Dunmar Campaign Dates]], [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Kenzo (OneNote)|Kenzo OneNote]], [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon|Events Since Chardon]], [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes|Session 124 DM Notes]], [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 125 - DM Notes|Session 125 DM Notes]], and [[_DM_/_Mawar Confederacy/Ep 5 - Lost Legacy/Time Skip - Bullet Points|Time Skip - Bullet Points]]. The existing cleanup status tags remain justified by the unintegrated material.
%%^End%%

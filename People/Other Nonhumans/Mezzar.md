---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: dragon
subspecies: green dragon
campaignInfo:
  - {campaign: dufr, date: 1748-09-15, type: killed}
born: null
gender: male
died: 1748-09-15
name: Grimbaskal
aliases: [Grimbaskal]
whereabouts:
  - {type: home, location: Elderwood}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: modern
---
# Grimbaskal
>[!info]+ Biographical Info  
> A [[Dragons|dragon]] ([[Dragons|green dragon]]) (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Killed by the [[Dunmar Fellowship]] on September 15th, 1748 in the [[Elderwood]], [[Ainumarya]] %%^End%%

%% fix campaign info, whereabouts; many historical notes missing, in DM notes %%

Also known as Mezzar. A green dragon who made his lair in the Elderwood, and traveled widely in the guise of an elf, using the name Mezzar and poisoning the minds of the Deno'qai of the Elderwood.

%%^Metadata:names:v1%%
- {name: Grimbaskal, role: primary, language: unknown, pronunciation: GRIM-bass-kahl, status: proposed, notes: "Cautious spelling-based proposal: hard g, short i as in grim, short a as in bass (the fish), final ah vowel, and first-syllable stress. No name-specific pronunciation or source language is established."}
- {name: Mezzar, role: alias, language: unknown, pronunciation: MEZ-ar, status: proposed, notes: "The article identifies this as his assumed elven identity. Cautious spelling-based proposal: short e, voiced z for zz, ar as in far, and first-syllable stress; the disguise does not establish the name's language."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern retrospective account of Grimbaskal's Elderwood identity and influence; the dated header records his death in DR 1748, while the earlier duration of his activities is not specified.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting; added `knownTo: [dufr]` from the existing campaign interaction and [[Session 52 (DuFr)]].
- Converted the campaign code in `campaignInfo` and the existing header marker from `DuFr` to canonical `dufr` without changing its scope.
- Added proposed name pronunciations and a broadly modern retrospective POV with temporal coverage notes.

### Validated judgments
- The existing species, assumed elven identity, Elderwood home, and September 15, 1748 death are supported by [[Session 52 (DuFr)]].
- Confirmed local DM sources support the existing positive `dm_notes` attestation; its value is unchanged. The ordinary comment remains an editorial reminder, not adopted lore.
- `status/cleanup/metadata`: not assessable after the mechanical corrections because the author's intended further whereabouts and historical cleanup is not fully specified; preserved for human review.

### Editorial assessment
**Underdeveloped**: the visible account omits the established substance and lasting consequences of Grimbaskal's rule over the Elderwood tribes, his attack on the Te'kula, and the reported origin connecting him to Cha'mutte. A short account of his rule and its aftermath, plus one attributed origin sentence, would address these central gaps without a campaign itinerary or invented connective history.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new name block proposes `GRIM-bass-kahl` for Grimbaskal and `MEZ-ar` for Mezzar. No established name language or accepted pronunciation was found. These are cautious spelling-based readings: Grimbaskal uses hard g, short i, short a as in the fish bass, final ah, and initial stress; Mezzar uses short e, voiced z, ar as in far, and initial stress. Confirm or correct both proposals. If accepted, set `pronunciation: GRIM-bass-kahl` in frontmatter and change both name entries to `status: documented`; the elven disguise alone does not establish an Elvish name language.
- [ ] **Warning — coverage.established_fact_missing:** “Poisoning the minds of the Deno'qai” does not give the central substance or lasting consequences of his rule. [[Bek'eni]] and [[Baz'aku]] establish the tribes' isolation, tribute, and raiding; [[Te'kula]] and [[Session 52 (DuFr)]] establish his attack for Rai's jade, the village's refuge, transformed Deno'qai, and the aftermath. Add a bounded account, preserving the already recorded death date. Candidate: “As Mezzar, Grimbaskal drew the [[Bek'eni]] into isolation and extracted heavy tribute, while his influence encouraged [[Baz'aku]] raids against Chardonian interests. He attacked the [[Te'kula]] after [[Jordo]] refused to surrender a [[Jade Piece of Rai's Hand]]; [[Aasimti]], acting through the jade, sheltered their village in a pocket dimension. After Grimbaskal's death, the corruption around his lair began to recede, and the bodies of Deno'qai he had transformed into snake people were recovered and buried. [[Theba]] began working to repair relations among the tribes, while the Te'kula eventually returned to the Material Plane.” These are defining effects on his subjects and territory, rather than incidental party encounters.
- [ ] **Warning — coverage.established_fact_missing:** The article lacks the reported origin that connects Grimbaskal to [[Cha'mutte]]. In [[Session 83 (DuFr)]], [[Delios the Sage]] identifies him as one of seven dragons hatched from eggs that grew from Cha'mutte's destroyed body, apparently consulting a scroll. Preserve this as an attributed account, not omniscient certainty. Candidate: “According to [[Delios the Sage]], Grimbaskal was one of seven dragons hatched from eggs that grew from [[Cha'mutte]]'s destroyed body.”

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Elderwood Arc NPCs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Grimbaskal - DM Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part II Finding the Te'kula/Baz'aku (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part II Finding the Te'kula/Bek'eni (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part II Finding the Te'kula/Flowchart - Elderwood Part 2]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part III Saving the Te'kula/Aftermath and Resolution]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part III Saving the Te'kula/Flowchart - Elderwood Part 3]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part III Saving the Te'kula/Grimbaskal's Home]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part III Saving the Te'kula/Journey to the Lair]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part III Saving the Te'kula/Te'kula - DM Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part III Saving the Te'kula/The Final Confrontation]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/SESSION III]]
- [[_DM_/_Dunmari Frontier/Leveling]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/NOTES/Friday Morning]]
%%^End%%

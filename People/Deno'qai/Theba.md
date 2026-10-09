---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: "Deno'qai"
campaignInfo:
  - {campaign: dufr, person: Delwath, date: 1748-10-22, type: scryed}
born: 1717
gender: female
name: Theba
affiliations:
  - {org: "Bek'eni", type: primary}
whereabouts:
  - {type: home, end: 1748-09-06, location: Talem}
  - {type: away, start: 1748-09-07, end: 1748-09-09, location: Dunmar Fellowship}
  - {type: away, start: 1748-09-10, end: 1748-09-30, location: Neshet}
  - {type: home, start: 1748-10-01, location: Talem}
knownTo: [dufr]
dm_owner: none
dm_notes: important
POV: 1748
---
# Theba
>[!info]+ Biographical Info  
> A [[Deno'qai]] [[Humans|human]] (she/her), of the [[Bek'eni]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Scryed by [[Delwath]] on October 22th, 1748 in [[Talem|Bek'eni village]], the [[Elderwood]], [[Ainumarya]] %%^End%%

%% some information from DM notes; need to link character sheet; clean up whereabouts and campaign info%%

The formerly disgraced Godcaller of the [[Bek'eni]], out of favor due to [[Mezzar]]'s influence. Aided the party in their travels and fights in the [[Elderwood]], and agreed to take charge of rebuilding the relations among the Deno'qai after [[Mezzar]]'s meddling. This seems to be going well, in Oct 1748 at least.

%%^Metadata:names:v1%%
- {name: Theba, language: "Deno'qai", pronunciation: teh-BAH, status: proposed, notes: "Inferred Deno'qai name context; Hebrew-informed proposal using the analogue in [[Languages]]: th as t, e as eh, b as b, final a as ah with final stress. The Arabic analogue could instead retain th as in thin (theh-BAH); no accepted name-specific pronunciation is recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a post-Mezzar portrait in autumn DR 1748, with her rebuilding efforts tentatively assessed in October; the note does not establish her later position.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting; added `knownTo: [dufr]` from the existing campaign interaction and [[Session 51 (DuFr)]].
- Added a proposed name pronunciation and an autumn DR 1748 temporal interpretation.
- Corrected the objective typo “formely” to “formerly”.

### Validated judgments
- Matching local DM sources support the existing positive `dm_notes` attestation; its value is unchanged.
- `status/cleanup/metadata` remains supported by the whereabouts conflict below. The October assessment is consistent with the qualified observations in [[Scrying Delwath Oct 21]]; the broader tribal recovery described in [[Bek'eni]] does not establish a later change in Theba's own position.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new name entry proposes `teh-BAH`. [[Languages]] gives Deno'qai Hebrew or Arabic analogues; the preferred Hebrew-informed reading uses t for the written th, eh for e, b for b, and final stressed ah. An Arabic-informed reading could retain th as in thin (`theh-BAH`). These are analogue-based proposals, not documented in-world phonology. Accept or correct the pronunciation; if accepted, set `pronunciation: teh-BAH` in frontmatter and change the matching name entry to `status: documented`.
- [ ] **Warning — metadata.whereabouts_conflict:** The `Te'kula village` whereabouts entry spans September 10–30, 1748, but [[Session 52 (DuFr)]] records Theba leaving on September 12, fighting at Grimbaskal's lair on September 15, and returning with the group on September 20. Split that one entry so dated headers do not place her in the village throughout the expedition. Candidate replacement, preserving the other whereabouts entries:

  ```yaml
  - {type: away, start: 1748-09-10, end: 1748-09-11, location: "Te'kula village"}
  - {type: away, start: 1748-09-12, end: 1748-09-19, location: Elderwood}
  - {type: away, start: 1748-09-20, end: 1748-09-30, location: "Te'kula village"}
  ```

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Delwath Solo Arc/Prequel - Delwath]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Kenzo Solo Arc/Prequel - Kenzo]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Seeker Solo Arc/Prequel - Seeker]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Prequel - Wellby]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Elderwood Arc NPCs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/SESSION III]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Raw Notes - Seeker Solo]]
%%^End%%

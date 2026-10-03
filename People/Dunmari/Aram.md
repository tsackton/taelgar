---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo: []
born: 1717
gender: male
name: Aram
affiliations: ["Havdar's Warband"]
whereabouts:
  - {type: home, location: "Havdar's Warband"}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Aram
>[!info]+ Biographical Info
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% add campaign info, fix whereabouts %%

A holy warrior of [[Aagir]] in [[Havdar]]'s service, and unofficial spiritual leader of [[Havdar's Warband]].

%%^Metadata:names:v1%%
- {"name": "Aram", "language": "Dunmari", "pronunciation": "ah-RAHM", "notes": "Persian-informed proposal from the Dunmari analogue in [[Languages]]: two open a vowels, a light r, and final stress; vowel length and stress remain unconfirmed.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of Aram serving Havdar and his warband; the sources establish this role in 1748 but do not date its beginning or end.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the established campaign interaction.
- Added a persistent name entry with a proposed pronunciation and its derivation.
- Recorded the article's temporal viewpoint in `POV` and `povNotes`.

### Validated judgments
- The visible account is proportionate to this person's reference role.
- Confirmed local source matches support the positive `dm_notes` attestation; its value is preserved.
- `status/cleanup/metadata`: not assessable; the authored reminder requests whereabouts work without specifying a correction. The current warband location is valid relationship metadata, so the tag and reminder are preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed pronunciation `ah-RAHM` in `Metadata:names:v1`. Persian-informed proposal from the Dunmari analogue in [[Languages]]: two open a vowels, a light r, and final stress; vowel length and stress remain unconfirmed. The documented Dunmari guidance allows Hindi or Persian analogues, so this is a preferred analogue-informed reading, not adopted in-world phonology. A Hindi-oriented reading could reduce or shorten the unmarked vowels; the spelling does not settle their length. Accept or revise the proposal; if accepted, copy `ah-RAHM` to frontmatter `pronunciation` and mark the entry `documented`.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Grash (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 21]]
%%^End%%

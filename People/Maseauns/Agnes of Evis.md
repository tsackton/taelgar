---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Mazeanne
campaignInfo:
  - {campaign: clee, date: 1719-12-07, type: met}
born: 1690-04-03
gender: female
name: Agnés of Evis
aliases: [Agnés of Evis]
whereabouts:
  - {type: home, location: Evis}
  - {type: away, start: 1719-12-05, end: 1719-12-07, location: "Wakog's Camp"}
  - {type: away, start: 1719-12-07, end: 1719-12-12, location: Cleenseau}
  - {type: away, start: 1719-12-12, end: 1719-12-22, location: traveling home to Evis}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1719
---
# Agnés of Evis
>[!info]+ Biographical Info  
> A [[Duchy of Maseau|Maseanne]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:Clee%% Met by the [[Heroes of Cleenseau]] on December 7th, 1719 in [[Cleenseau]], the [[Manor of Cleenseau]], the [[Barony of Aveil]] %%^End%%

Agnés is a tough-as-nails but somewhat lazy caravan guard, who has struggled to find work recently. She distinguished herself in the recent [[Battle Against Wakog]].

%%^Metadata:names:v1%%
- {"name": "Agnés of Evis", "language": "unknown", "pronunciation": "ah-NYEHS uhv ay-VEE", "notes": "Proposal using the French analogues for northern Isinguese and southern Sembaran in [[Languages]], consistent with the Maseau context: gn as ny, accented e as a close e, the given-name final s retained by the Agnès naming pattern, and Evis with initial e as ay and silent final s. The exact local language and Evis reading are unconfirmed; English of is retained as displayed.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-DR 1719 portrait of her work and recent battle service, anchored by the December 6 Battle Against Wakog and the dated December movements; later employment is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the missing sentence-final period.
- Normalized the `campaignInfo` code to `clee` and added matching `knownTo: [clee]`.
- Added a proposed full-name pronunciation, DR 1719 POV metadata, and canonical frontmatter formatting.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes `ah-NYEHS uhv ay-VEE`, using the French analogues for northern Isinguese and southern Sembaran in [[Languages]] as the strongest regional guidance. This reads `gn` as /ny/, the accented vowel as close /e/, and retains the given-name final /s/ by the Agnès pattern; `Evis` is provisionally read with initial /e/ and silent final `s`. The exact local name language and place-name reading remain unconfirmed. Preserve the authored spelling `Agnés`; confirm or replace the pronunciation before copying it to frontmatter and marking the entry `documented`.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated meeting line uses `%%^Campaign:Clee%%`; the registry’s canonical code is `clee`. Copy-ready replacement opener: `%%^Campaign:clee%%`. Preserve the existing meeting text and end marker when regenerating or correcting the header.
%%^End%%

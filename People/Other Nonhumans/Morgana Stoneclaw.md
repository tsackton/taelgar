---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: fey
subspecies: hag
gender: female
died: 1747-12-16
campaignInfo:
  - {campaign: grli, type: killed, date: 1747-12-16}
name: Morgana Stoneclaw
aliases: [Morgana Frostclaw]
whereabouts:
  - {type: home, location: Yuvanti Mountains, end: 1745}
  - {type: home, start: 1744, location: Vangebekkr, alias: ice caves below Vangebekkr}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: modern
---
# Morgana Stoneclaw
>[!info]+ Biographical Info  
> A [[Fey|fey]] (hag) (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Killed by the [[Silver Tempests]] on December 16th, 1747 in the [[Vangebekkr|ice caves below Vangebekkr]], the [[Sentinel Range]] %%^End%%

Morgana Stoneclaw, later known as Morgana Frostclaw, was a hag of the mountains. For many years, she made a home in the [[Yuvanti Mountains]], where she tricked, corrupted, and manipulated the [[Dwarves|dwarves]] of the small mountain villages, seeking to cause strife wherever possible. Rarely making herself known, she preferred to work through disguise and subtle manipulation. It was here, in the dwarven village of [[Narazara]], that she encountered [[Adrik]], who would later become her destroyer.

She fled the [[Yuvanti Mountains]] in DR 1744, after refusing to swear fealty to [[Agata|Agata Dustmother]]. She eventually found her way to the [[Sentinel Range|Sentinels]], where she sought power to create a world-shaking event that would make people fear her again. She transformed herself into a hag of ice and frost, and discovered a fragment of elemental power at the heart of a massive glacier. She built a lair beneath the frost giant castle of [[Vangebekkr]], after turning the frost giants against each other and establishing dominion over them. 

Morgana, now calling herself Morgana Frostclaw, channeled this power to change the land itself. She willed cold to grow, freezing the peaks and even pressing into the dwarven cities below the mountains, eventually threatening [[Am'khazar]]. This brought her to the attention of [[Adrik]] and the [[Silver Tempests]], who killed her beneath [[Vangebekkr]], thus ending [[Adrik]]'s childhood quest for revenge and saving [[Am'khazar]]. 

%% DM Sources

[[Cursed Cold DM Background]]
[[Cursed Cold Adventure Outline]]
[[Vangebekkr - DM Notes]]
[[Glacier Caves- DM Notes]]

%%

%%^Metadata:names:v1%%
- {name: Morgana Stoneclaw, language: unknown, notes: "The name used during her life in the Yuvanti Mountains, before her transformation into a hag of ice and frost.", status: documented}
- {name: Morgana Frostclaw, role: later name, language: unknown, notes: "She adopted this name after transforming herself into a hag of ice and frost in the Sentinels.", status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective biography ending with her death in DR 1747; it includes earlier life in the Yuvanti Mountains and her later rule beneath Vangebekkr, with a conflicting departure date preserved for review.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added knownTo: [grli] from the recorded campaign interaction.
- Normalized campaignInfo to the canonical lowercase campaign code.
- Normalized the existing campaign marker to its equivalent canonical code.
- Added persistent name metadata and POV modern with temporal coverage notes.
- Normalized frontmatter ordering and collection formatting.

### Validated judgments
- Morgana is an ordinary familiar personal name, and Stoneclaw/Frostclaw are plain-English compounds; separate pronunciation is unnecessary. The two documented name forms and their transformation context are preserved.
- The existing narrative covers her defining role, transformation, regional threat, and fate.

### Open findings

- [ ] **Warning — temporal.conflicting_dates:** The biography says Morgana fled the Yuvanti Mountains in DR 1744, while her Yuvanti home entry ends in 1745. Confirm the intended departure/home boundary; do not infer it from the overlapping home entries alone. If the visible biography is authoritative, the corresponding candidate is `{type: home, location: Yuvanti Mountains, end: 1744}`. Otherwise reconcile the biography and the dated home records together.
- [ ] **Warning — content.cross_note_conflict:** “Thus ending [[Adrik]]'s childhood quest for revenge” places his revenge quest in childhood. [[Adrik]] dates the childhood encounter to DR 1673–1675 but says he vowed vengeance after the pestilence of DR 1746, as an adult. Replace that clause with “thus ending [[Adrik]]'s quest for revenge and saving [[Am'khazar]].” Keep his childhood trauma distinct from the later vow; the source records his belief about the pestilence, not proof that Morgana caused it.
%%^End%%

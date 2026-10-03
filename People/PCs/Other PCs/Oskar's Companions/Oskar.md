---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
ancestry: Nardith
gender: male
player: Nathaniel Sackton
campaignInfo:
  - {campaign: grli, type: met, date: 1747-06-02}
  - {campaign: dufr, person: Riswynn, type: met, date: 1748-05-09}
name: Oskar
affiliations:
  - {org: "Oskar's Companions", title: One}
whereabouts:
  - {type: home, location: Tharn Todor}
  - {type: away, start: 1747-06-02, end: 1747-06-02, location: Goldpeak Mines}
  - {type: away, start: 1747-06-10, end: 1747-06-14, location: Greater Voltara}
  - {type: away, start: 1747-06-14, end: 1747-06-14, location: Voltara}
  - {type: away, start: 1747-07-16, end: 1747-07-19, location: Erbalta Plains}
knownTo: [grli, dufr]
dm_owner: player
dm_notes: important
POV: 1740s
---
# Oskar
>[!info]+ Biographical Info  
> A [[Nardith]] [[Dwarves|dwarf]] (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:GL%% Met by the [[Silver Tempests]] on June 2nd, 1747 in [[Goldpeak Mines]], [[Goldpeak Mountain]], the [[Fiatara Mountains]] %%^End%%  
>> %%^Campaign:DuFr%% Met by [[Riswynn]] on May 9th, 1748 in [[Tharn Todor]], [[Nardith]], the [[Yuvanti Mountains]] %%^End%%

Oskar grew up in [[Nardith]], in [[Tharn Todor]]. His parents were retired travelers and explorers, who now owned an inn, [[The Red Shield]]. He grew up around weapons, training with scimitars and crossbows from a young age, encouraged by his two older sisters.

After he came of age, he wanted badly to travel, and left for a time to explore, reaching as far north as [[Voltara]], but eventually returned to Tharn Todor. 

He travels with his hyena companion, [[Stoneclaw]].

%%
Old backstory, written by Nathaniel age 6 or 7
Grew up in Dwarven kingdom, parents were retired travelers and explorers who now own an inn called The Fighting Scimitar. This inn is where I started training with crossbows and Dwarven scimitars. 

My older sisters wanted to be something else and they didn't like scimitars because they were going to be in class called archery, so I kept that I fought with scimitars from them so they wouldn't think that I was bad. I also learned archery but still I wanted to keep a secret that I had scimitars. 

I spent most of my childhood playing and practicing archery with my sisters. Then when I was a teenager I thought I was ready to explore and travel on my own, and I really wanted to start adventuring.
%%

%%^Metadata:names:v1%%
- {name: Oskar, language: Dwarvish, status: inferred, notes: "Listed among traditional dwarven personal names in [[Dwarves#Dwarven Names]]; pronunciation omitted as an obvious ordinary name."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s adventurer's portrait with childhood backstory and a return to Tharn Todor established by spring DR 1748; the intervening life is not comprehensively described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected the objective typo “explorerers” to “explorers.”
- Normalized frontmatter order and collection formatting, canonicalized the campaignInfo codes to grli and dufr, and added knownTo: [grli, dufr] from those existing interactions.
- Added persistent name metadata and a 1740s temporal viewpoint with its coverage explanation.

### Validated judgments
- The family inn and northern journey agree with [[The Red Shield]] and [[Oskar in Tharn Todor]]. The concise origin, travels, and companion account is sufficient for this episodic adventurer; individual combats need not become a campaign log.
- Oskar is an obvious ordinary name and needs no pronunciation field. [[Dwarves#Dwarven Names]] lists the form among traditional dwarven personal names, supporting inferred Dwarvish language metadata.
- Preserved the player-owned DM attestation; the local-DM review gate is not applicable.

### Open findings

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated biographical header still uses the recognized aliases `Campaign:GL` and `Campaign:DuFr`. [[Campaign Registry]] requires canonical codes. On the next header refresh, replace only the opening markers with `%%^Campaign:grli%%` and `%%^Campaign:dufr%%`, respectively, keeping the existing text, closing markers, and line-break formatting.
- [ ] **Suggestion — editorial.shared_material_redundant:** The ordinary comment introduced “Old backstory, written by Nathaniel age 6 or 7” repeats the visible family, weapons training, and desire to travel, while retaining distinct old-draft details about the inn name and sisters. Decide whether to preserve the complete attributed draft as a separate source and replace this comment with a source link, or retain only the distinct editorial guidance here. A copy-ready reduced comment body is: “Original backstory written by Nathaniel at age 6 or 7. Earlier-draft differences: the family inn was called The Fighting Scimitar, and Oskar concealed his scimitar training from his sisters, who preferred archery. These variants belong to the old draft and are not adopted by this note.” Keep the full original unchanged until that preservation choice is made.
%%^End%%

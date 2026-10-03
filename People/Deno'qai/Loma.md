---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: "Deno'qai"
campaignInfo:
  - {campaign: grli, type: met, date: 1747-11-23}
born: 1733
gender: female
name: Loma
whereabouts: Raha
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1747
---
# Loma
>[!info]+ Biographical Info  
> A [[Deno'qai]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:GL%% Met by the [[Silver Tempests]] on November 23rd, 1747 in [[Raha]], the [[Highveil Forest]] %%^End%%

%% Raha does not yet have a tribal connection, but probably should %%

Loma is a young Deno’qai scout from the village of [[Raha]], quick and quiet in the woods and familiar with paths along the Sentinel foothills. Locals say she is favored by [[Wenba]], and leaves small offerings before dangerous journeys. 

She is slim, quick on her feet, and wears her red hair long, in tight braids. 
## Events
- (DR:: 1747-11-24) - (DR_end:: 1747-12-03): Guided the [[Silver Tempests]] south from [[Raha]] toward the [[Thordun|western gates]] of [[Am'khazar]]. En route the company investigated nearby [[Tirnessa|elven ruins]] and narrowly escaped banshees before continuing on.

%%
GL Arc 3 notes (sources and constraints)
- Description and age: “youngish girl, maybe 13/14, skinny and quick, braided red hair; incredibly good at hiding; knows the woods; blessed by Wenba; leaves small offerings (often burned; occasionally small animal when hunting)” — see [[GL - Session 40 - DM Notes]] and [[GL - Session 41 - DM Notes]].
- Travel role: escorted the party from Raha toward the dwarven gates; see Campaigns/Great Library Campaign/Session Notes/Great Library Session Notes - Arc 3.md (travel with Loma; banshees at [[Tirnessa]]; arrival near [[Thordun]]).
- Gazetteer tie-in: Gazetteer/Central Highlands/Tirnessa.md notes the party “almost killed by banshees … while traveling to [[Am'khazar]] with [[Loma]].”
- Keep details within these sources; no additional inventions added.
%%

%%^Metadata:names:v1%%
- {name: Loma, language: unknown, pronunciation: loh-MAH, notes: "Proposed loh-MAH uses the Hebrew option in the Deno'qai guidance in [[Languages]], provisionally suggested by her background, with final stress and pure oh/ah vowels. Her name's language and exact in-world reading are unrecorded.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1747 portrait of Loma as a young scout, with a dated account of her journey in November and December of that year; her later life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [grli]`, normalized the Great Library code in `campaignInfo` to `grli`, and formatted the frontmatter.
- Recorded a DR 1747 viewpoint and persistent name metadata with a proposed pronunciation.
- Corrected “November 23th” to “November 23rd” and replaced the obsolete combined source pointer with the two existing session-preparation note links.

### Validated judgments
- [[Great Library Session Notes - Arc 3]] supports the scout's journey and its dates; no material later change was found in the consulted references.
- `status/cleanup/metadata` remains supported while the name metadata requires human review; the tag was preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new name entry proposes `loh-MAH`. This uses the Hebrew option in [[Languages]] for Deno'qai names provisionally from Loma's cultural background: ordinary l/m consonants, a pure oh vowel, ah for a, and final stress. The name's source language is unrecorded, and the alternative Arabic analogue does not uniquely resolve the vowels or stress; no exact in-world rule was found. Confirm or correct the reading. If accepted, add `pronunciation: loh-MAH` to frontmatter and change the entry to `status: documented`, retaining its derivation and `language: unknown` until the language is established.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated header uses `Campaign:GL`, which resolves to `grli` in the campaign registry. The current site exporter compares casefolded literal identifiers without expanding aliases, so changing this marker would switch which campaign exports show the header. After confirming the intended export audience and aligning its configuration, replace only the opening marker `%%^Campaign:GL%%` with `%%^Campaign:grli%%`; preserve the header text and closing marker. This remains a proposal so the existing filtering is preserved.
%%^End%%

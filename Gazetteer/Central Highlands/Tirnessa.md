---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: building
subTypeOf: ruined
typeOfAlias: fort
ancestry: elven
campaignInfo:
  - {campaign: GL, type: explored, date: 1747-11-19, wParty: "<met:u> by <person> on <target>"}
name: Tirnessa
pronunciation: TEER-ness-ah
whereabouts: Highveil Forest
dm_owner: none
dm_notes: none
POV: modern
---
# Tirnessa
*(TEER-ness-ah)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:GL%% Explored by the [[Silver Tempests]] on November 19th, 1747 %%^End%%

Tirnessa is an ancient elven fort within the [[Highveil Forest]], now ruined. 

%%^Campaign:GL%%
The [[Silver Tempests]] briefly explored this ruin, and were almost killed by banshees, while traveling to [[Am'khazar]] with [[Loma]]. 
%%^End%%

%% DM
GL Arc 3: side site during Deno’qai-guided travel, see [[Great Library Session Notes - Arc 3]]

See also: [[Haunted Elven Ruins - DM Notes]]

%%

%%^Metadata:names:v1%%
- {name: Tirnessa, language: unknown, pronunciation: TEER-ness-ah, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the ruined elven fort; the campaign passage records a DR 1747 exploration, while the fort's construction and ruin dates are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added a primary name entry matching the accepted frontmatter pronunciation, with unknown name language, and broadly modern temporal metadata.

### Validated judgments
- The ruined-fort identity and banshee encounter are corroborated by [[Great Library Session Notes - Arc 3]]. The short article performs a bounded location-reference role; the ordinary DM comment is a source pointer.

- Retained the existing GL campaignInfo value and both GL content markers: current header generation reuses the metadata code, while export membership treats GL and grli as distinct identifiers. Their migration requires a coordinated visibility decision.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** The campaignInfo date and displayed exploration header say November 19, DR 1747, but the Events chronology in [[Great Library Session Notes - Arc 3#Events|Arc 3]] places the Tirnessa encounter on November 30, after departure from Raha on November 24. Reconcile these dates without changing the source record. If the Arc 3 chronology is intended, set the existing campaignInfo date to `1747-11-30` and replace only “November 19th, 1747” in the header with “November 30th, 1747”. The conflicting values remain unchanged pending that decision.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The exploration header and encounter paragraph both use the legacy opening marker `%%^Campaign:GL%%`; the registry resolves this to Great Library, whose authored code is `grli`. The canonical marker proposal is `%%^Campaign:grli%%` for both openings. Apply it only as part of the same approved consumer/configuration migration as the campaignInfo code: current export membership does not resolve GL and grli as aliases, so replacing the markers can change which campaign sees the passage. Preserve the enclosed text and closing markers; the existing markers remain unchanged.
- [ ] **Suggestion — campaign.noncanonical_code:** The campaignInfo entry retains `campaign: GL`. [[Campaign Registry]] recognizes GL as an alias of Great Library and requires the authored code `grli`. The bounded metadata proposal is to replace `campaign: GL` with `campaign: grli` in that existing dictionary, preserving the date pending its separate conflict. Do so only after coordinating the generated header markers and export campaign configuration: header generation copies this code into Campaign markers, and the current exporter tests exact case-folded membership without GL/grli alias resolution. The metadata value has therefore been preserved for a human visibility decision.
%%^End%%

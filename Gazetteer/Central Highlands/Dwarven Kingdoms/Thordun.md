---
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: infrastructure
typeOfAlias: gate
campaignInfo:
  - {campaign: GL, type: passed through, date: 1747-12-03, wParty: "<person:u> <met:x> on <target>"}
name: Thordûn
pronunciation: THOR-doon
whereabouts: "Am'khazar"
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

Thordûn (the Western Door) is the largest and most elaborate of the western gates to the dwarven kingdom of [[Am'khazar]], though not the most frequently used. It is located on the edge of the [[Sentinel Range|Sentinels]], north of the [[Crimson Forest]], in the [[Highveil Forest]].

%%
GL Arc 3: [[Great Library Session Notes - Arc 3]]

This is a little too far north to be a major trading point in the modern day, but pre-Great-War this would have been a center of elvish/dwarven exchange. 

The vibe is kind of ancient grandeur slightly falling into decay, as traffic shifts south to connect to [[Arendum]].  
%%


%%^Metadata:names:v1%%
- {name: Thordûn, language: unknown, pronunciation: THOR-doon, meaning: the Western Door, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geographical description of the gate, with a separately campaign-filtered visit in DR 1747; the hidden historical trade and atmosphere notes remain provisional.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter while preserving the existing campaign code.
- Removed the comma between the subject and verb and the duplicated “to.”
- Added the documented pronunciation and translation to a persistent name block and added temporal metadata.

### Validated judgments
- [[Great Library Session Notes - Arc 3]] corroborates the dated arrival at the gate; the existing metadata code and campaign marker are preserved together.
- Header generation uses the campaignInfo code directly, and the exporter compares campaign codes by casefolded equality without registry alias resolution. Migrating GL to grli therefore requires coordinated visibility review.
- The hidden trade-history and atmosphere passage remains provisional and was not promoted.

### Open findings

- [ ] **Suggestion — campaign.noncanonical_code:** `campaignInfo` retains `campaign: GL`, which [[Campaign Registry]] resolves to canonical `grli`. This code also controls generated campaign markers, so changing it can change filtered visibility. Proposed metadata entry: `{campaign: grli, type: passed through, date: 1747-12-03, wParty: "<person:u> <met:x> on <target>"}`. Adopt it only with a coordinated decision about export campaign configuration and regenerated header visibility; the legacy code remains unchanged pending that decision.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated header retains `Campaign:GL`; [[Campaign Registry]] defines `grli` for Great Library. Proposed replacement for the existing header line: `>> %%^Campaign:grli%% The [[Silver Tempests]] passed through on December 3rd, 1747 %%^End%%`. Apply only with the campaignInfo/export-configuration migration above, since the exporter does not resolve GL and grli as aliases. The marker remains unchanged pending human review.
%%^End%%

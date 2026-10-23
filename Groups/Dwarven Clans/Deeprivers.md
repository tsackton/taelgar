---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
tags: [group, status/check/lint]
typeOf: clan
ancestry: Dwarven
name: Deepriver Clan
aliases: [Deeprivers]
whereabouts: Goldpeak Mountain
dm_owner: none
dm_notes: none
POV: modern
---
# The Deepriver Clan
>[!info]+ Information  
> A [[Dwarves|Dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Deepriver Clan was a [[Dwarves|Dwarven]] clan that was prominent in the [[Fiatara Mountains]] before the [[Great War]]. They were associated with the ancient mine workings under [[Goldpeak Mountain]], in particular.

%%^Campaign:GL%%
During explorations of the upper mines in DR 1747, the [[Silver Tempests]] recovered two Deepriver clan treasures: [[Thunderbrand]] and [[Coldguard]].
%%^End%%

%%^Metadata:names:v1%%
- {name: Deepriver Clan, role: primary, language: Common, status: inferred, notes: Plain-English descriptive name; no pronunciation guide is needed.}
- {name: Deeprivers, role: alias, language: Common, status: inferred, notes: Plural form recorded in frontmatter.}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern retrospective account of the pre-Great-War clan; the Great Library campaign passage separately dates the recovery of its treasures to DR 1747.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added persistent metadata for the plain-English primary name and recorded alias, plus modern POV and temporal coverage metadata.

### Validated judgments
- The compact retrospective identifies the clan's pre-war regional role, mine association, and surviving treasures; the DR 1747 expedition is corroborated by [[Great Library Session Notes - Arc 1]].

### Open findings

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The treasure-recovery paragraph opens with legacy `%%^Campaign:GL%%`; [[Campaign Registry]] assigns the canonical Great Library code `grli`. Copy-ready replacement opener: `%%^Campaign:grli%%`. Apply it together with a check that the Great Library export selects `grli`: the current exporter compares literal campaign identifiers, so changing this alias could otherwise change visibility. Preserve the paragraph and its closing `%%^End%%`.
%%^End%%

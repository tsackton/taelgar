---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: lizardfolk
ancestry: null
campaignInfo:
  - {campaign: clee, type: met, date: 1719-10-28}
born: 1688
gender: male
name: Izoko
whereabouts:
  - {type: home, location: Ganboa}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1719
---
# Izoko
>[!info]+ Biographical Info
> A [[Lizardfolk|lizardfolk]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:clee%% Met by the [[Heroes of Cleenseau]] on October 28th, 1719 in [[Ganboa]], the [[Barony of Aveil]], [[Sembara]] %%^End%%

![[lizardfolk-Izoko.png|right|320]]A young lizardfolk, sweet on [[Gentza]]. He is a skilled fisherman but not so skilled at keeping secrets.

%%^Metadata:names:v1%%
- {name: "Izoko", language: "unknown", pronunciation: "ee-SOH-koh", notes: "Proposal using the Basque analogue for Lizardling in [[Languages]]: i is ee, each o is a pure o, z is a voiceless s rather than English z, and k stays hard; penultimate stress is provisional because no precise in-world stress rule or accepted pronunciation is recorded.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1719 initial portrait of Izoko as a young fisherman sweet on Gentza; it does not yet account for her death in October 1719 or his recorded public role in spring 1720.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [clee]`, consistent with the existing campaign interaction.
- Added a proposed name entry and temporal metadata describing the existing DR 1719 portrait; normalized frontmatter formatting.

### Validated judgments
- The local DM dossier has no matches, consistent with `dm_notes: none`; the later relationship and role updates come from shared campaign evidence.

### Editorial assessment
- **Underdeveloped**. The visible initial portrait omits the fate of Izoko's defining relationship and his later established community role. The smallest useful scope is a short update acknowledging Gentza's death and his spring-1720 work organizing sand gathering; the available sources establish both facts, so no additional invented backstory is required.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed `ee-SOH-koh` in `Metadata:names:v1`. The Basque analogue for Lizardling in [[Languages]] motivates i as ee, pure o vowels, z as a voiceless s, and hard k. Penultimate stress is provisional because no exact in-world stress rule is recorded; the specific name language remains unestablished. Accept it by setting `pronunciation: ee-SOH-koh` in frontmatter and changing the entry to `status: documented`, or supply the intended reading.
- [ ] **Warning — coverage.later_material_change:** The present-tense phrase “sweet on [[Gentza]]” does not acknowledge her murder on DR 1719-10-27, recorded in [[Gentza]] and [[Cleenseau - Session 03]]. [[Cleenseau - Session 29]] additionally establishes Izoko's role organizing lizardfolk sand gathering for Asineau's glassworks in spring 1720. Update the article and `POV` to 1720, defer with an appropriate `status/gameupdate/clee` disposition, or deliberately preserve the initial 1719 portrait. The finalized [[cleenseau-003-session-recap]] identifies Izoko as her boyfriend. A concise updated body is: `Izoko is a young lizardfolk fisherman from [[Ganboa]], skilled at fishing but not at keeping secrets. He was [[Gentza]]'s boyfriend before she was murdered in October DR 1719. In spring DR 1720, he organized younger lizardfolk to gather sand for [[Asineau]]'s glassworks.` If maintaining a layered earlier portrait, place the old relationship wording in a `Date:1719-10-27b` block, its retrospective wording in `Date:1719-10-27`, and the later role in a separate `Date:1720` block. These visibility changes and any game-update tag remain human decisions.
%%^End%%

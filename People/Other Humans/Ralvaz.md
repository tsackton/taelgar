---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/gl, status/check/lint]
species: human
gender: male
campaignInfo:
  - {campaign: grli, type: rescued, date: 1747-06-11}
name: Ralvaz
whereabouts:
  - {type: home, location: Voltara}
  - {type: away, end: 1747-06-11, location: Lonely Watchtower}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Ralvaz
>[!info]+ Biographical Info  
> A [[Humans|human]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:GL%% Rescued by the [[Silver Tempests]] on June 11th, 1747 in the [[Lonely Watchtower]], the [[Chalyte Hills|North Voltara Hills]], the [[Erbalta Plains]] %%^End%%

Ralvaz is a mine captain from the chalyte mines near [[Voltara]]. He was caught up in the early raids by [[Grumella's Horde]] on [[Voltara]] trade, and was kept as a prisoner at the [[Lonely Watchtower]] by [[Raluhk]] until he was rescued by the [[Silver Tempests]].

%%^Metadata:names:v1%%
- {"name": "Ralvaz", "language": "unknown", "pronunciation": "RAL-vaz", "notes": "Cautious spelling-based proposal: short a in both syllables, pronounced v and final z, with initial stress; no name-specific language or accepted pronunciation is recorded.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740s portrait of a Voltara mine captain after his rescue in June 1747; later career and residence are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the persistent name entry and temporal viewpoint metadata.
- Added knownTo: [grli] and normalized the campaignInfo code to grli.
- Removed one duplicated space before the Lonely Watchtower link.

### Validated judgments
- The mine-captain role and rescue are corroborated by [[Great Library Session Notes - Arc 1]].
- `status/gameupdate/gl`: not assessable. The recorded rescue is already represented; the tag does not identify the intended later update. It remains unchanged.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed pronunciation `RAL-vaz` in the name block. No established language or accepted pronunciation was found; this cautious spelling reading uses short a in both syllables, pronounced v and final z, and initial stress. Accept or replace it before copying it to frontmatter.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The existing header uses `%%^Campaign:GL%%`; [[Campaign Registry]] identifies `grli` as the canonical Great Library code. Replace only that opening marker with `%%^Campaign:grli%%`, retaining its text, position, and closing marker. This visibility-sensitive marker has been left for human approval.
%%^End%%

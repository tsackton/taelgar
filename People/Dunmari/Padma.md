---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T18:44:38-04:00"
lintVersion: "3.4"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
born: 1720
gender: female
campaignInfo:
  - {campaign: dufr, type: met, date: 1748-07-26}
name: Padma
whereabouts: "an unnamed caravanserai, Tokra-Darba Road"
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Padma
>[!info]+ Biographical Info
> A [[Dunmar|Dunmari]] [[Humans|human]] (she/her)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by [[Dunmar Fellowship]] on July 26th, 1748 in an unnamed caravanserai, the [[Tokra-Darba Road]], [[Dunmar]] %%^End%%

An innkeeper and master of a caravanserai waystation on the [[Tokra-Darba Road]], running one of the first waystations on the west side of the [[Copper Hills]].  Generally well positioned to receive and pass along news. 

%%^Date:1748-07%%
In late July 1748, was briefly cut off from [[Tokra]] by wyverns who had made a nest in the ruined mining town of [[Vandar]]. Pleased to receive news that [[Dunmar Fellowship]] had killed the wyverns and the road was clear on 26 July 1748.
%%^End%%

%%SECRET[v2:e47d54c2b97a4f7120ffdaf96f3ebd1a]%%

%%^Metadata:names:v1%%
- {name: Padma, role: primary, language: Dunmari, pronunciation: PUD-mah, status: proposed, notes: The Dunmari Hindi and Indo-Iranian analogue supports this cautious reading; exact in-world phonology is not recorded.}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait centered on the Dunmar Fellowship's July visit to Padma's caravanserai.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo`, `POV`, `povNotes`, and a persistent pronunciation proposal; normalized the Dunmar Frontier code in `campaignInfo` and the campaign block; normalized frontmatter formatting.

### Validated judgments
- Matching local-only sources support `dm_notes: color`; their contents are not reproduced here.

### Open findings
- [ ] **Warning — metadata.names_unresolved_status:** Persistent name review remains open for `Padma — PUD-mah` (proposed). The documented Hindi and Indo-Iranian analogue for this culture supports the cautious reading, but exact in-world phonology is not established. Accept it by adding `pronunciation: PUD-mah` to frontmatter and changing the name entry to `status: documented`, or correct the proposal.
%%^End%%

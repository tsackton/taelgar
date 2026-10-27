---
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
tags: [group, status/gameupdate/dufr, status/check/lint]
typeOf: scholarly society
ancestry: Chardonian
name: Society of the Open Scroll
dm_owner: tim
dm_notes: important
POV: 1740s
---
```taelgar-header
```

A scholarly society founded in the aftermath of the [[Great War]], to preserve and protect knowledge against future disaster, and to learn the secrets of the past to better protect [[Chardon]] and the world from existential magical threats.

They have meetings, sometimes public lectures or demonstrations, sponsorship of individual scholars and research projects, including expeditions, and the like. The membership is largely made up of academics already associated with the [[Great Library]] or the [[University of Chardon]], but formally neither is a requirement to join - sponsorship and approval by a vote of the members is enough. In the past 20-30 years they have been recruiting more "practical historians" and now have kind of an "explorer's wing" for adventurers and the like. This is funded primarily by the [[Great Library]], but occasionally by individual patrons.

Generally speaking in favor of preserving knowledge, against chalyte magic, and in favor of sharing within the group but secrecy outside the group for fear of passing along dangerous magic.

## History

- (DR::1561): The Society of the Open Scroll is founded in [[Chardon]], in the aftermath of the [[Great War]], with a mission to preserve and protect knowledge of magic against future disaster, and to learn the secrets of the past to better protect Chardon and the world from existential magical threats.

%%SECRET[v2:c7885752c7e2df12a31ae1df3eae9e69]%%

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {name: Society of the Open Scroll, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s institutional overview, with the recent expansion of its explorer membership read relative to that period and a separate DR 1561 founding entry; the aftermath of Fausto's fall in DR 1749 is not yet incorporated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected `scholary` in the classification and information callout, `chalyte` in the visible prose, and `Scroll` in the founding entry.
- Added the missing subject in the recruitment sentence and corrected `funded primary` to `funded primarily` in visible prose.
- Normalized frontmatter order and added a minimal primary-name block with unknown source language.
- Added `POV: 1740s` and a temporal note distinguishing the institutional overview from the unincorporated DR 1749 aftermath.

### Validated judgments
- The plain-English institutional name does not require pronunciation; the name's in-world source language is not established by its members' ancestry.
- Matching local evidence supports the existing positive `dm_notes` attestation. The local-only `SECRET` block was reviewed without copying its contents into this report.
- `status/gameupdate/dufr` is not assessable until the human chooses whether to update or preserve the earlier institutional account; the tag is retained unchanged.

### Editorial assessment
**Underdeveloped**. The institutional outline is useful, but it omits two central dimensions of the Society's demonstrated campaign role: Fausto's patronage and exploitation of its recruits, and its political standing after his DR 1749 downfall. The smallest useful scope is a short sourced account of that patronage and coercion plus a dated aftermath paragraph; the sources do not justify treating every member as a willing participant or inventing a settled post-crisis organization.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The funding paragraph mentions the Great Library and unnamed individual patrons but omits [[Fausto]], whose reference note establishes extensive patronage of Society expeditions across Dunmar and the southern Sentinels. [[Session 79 (DuFr)]] records Valius's account of Fausto recruiting and coercing former Society treasure hunters. This is a defining institutional relationship, not an incidental party encounter. Add the public patronage account and decide the visibility of the coercion history separately. Copy-ready patronage candidate: "In the 1740s, [[Fausto]] was a prominent patron of the Society's expeditions across [[Dunmar]] and the southern [[Sentinel Range|Sentinels]], funding searches for Drankorian ruins and artifacts." Copy-ready historical candidate: "According to [[Valius]]'s account, Fausto recruited him and [[Vargus]] after their work as Society treasure hunters, then used the [[Crown of Purity]] against Vargus when he tried to leave." Preserve the attribution and do not identify the entire Society with [[The Cleansed]].
- [ ] **Warning — coverage.later_material_change:** [[Session 125 (DuFr)]] records that, by DR 1749-06-27, Tiberius reported the Magistros's anger at the Society and University for failing to recognize Fausto's rise and the infiltration of the Hetaeri Magica. This changes the Society's political standing and is absent from the current institutional account. Human choice: update the article and reassess `POV`; defer the update and retain `status/gameupdate/dufr`; or deliberately preserve the earlier account and then decide whether to remove that tag. A minimal dated addition, proposed only, is `%%^Date:1749-06-27%%` followed by "By late June DR 1749, [[Tiberius]] reported that [[Mitus Verina Auratan]] was angry with the Society and the [[University of Chardon]] for failing to recognize [[Fausto]]'s rise and the infiltration of the [[Hetaeri Magica]] by [[The Cleansed]]." and `%%^End%%`. This does not establish the Society's later governance or survival; leave those questions unresolved unless further played evidence settles them.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The member-query block opens with `%%^Campaign:None%%`; the documented private sentinel is `%%^Campaign:none%%`. Approve that exact marker replacement after confirming the intended filtered visibility. The block and its Dataview code have been preserved.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Agata Dustmother (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Apollyon (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Hralgar (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Vola Forena (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Chardon NPC Flowchart]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Power Structures]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 49]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 18]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Raven’s Hold Text]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Session 11]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Stormcaller Tower/Session 16]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Darba/Darba (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra Arc Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/History of Blasted Plains]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Major Players]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Arcs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Summary]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Faction Action]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Player Questions]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/The Relics of Apollyon]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Kenzo (OneNote)]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Politics - ChatGPT Summary]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Politics]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 125 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 126 - Brainstorming]]
%%^End%%

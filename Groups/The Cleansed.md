---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [group, status/gameupdate/dufr, status/check/lint]
typeOf: cult
ancestry: mysterious
name: The Cleansed
dm_owner: tim
dm_notes: important
POV: 1740s
---
# The Cleansed
>[!info]+ Information  
> A mysterious cult  
> `$=dv.view("_scripts/view/get_Affiliations")`

%% needs major updates post Apollyon arc %%

A mysterious secret society in [[Chardon]] of which [[Fausto]] is a member and which seems to be dedicated in some way to Drankorian purity.

%%SECRET[v2:9e786cf68113f784dc52d70fac42890d]%%

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {name: The Cleansed, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s account of the Cleansed while Fausto was alive; the DR 1749 loss of its leadership and exposure in Chardon are not yet incorporated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected the relative-clause grammar in the visible sentence from “and seem” to “and which seems”, preserving its uncertainty.
- Normalized frontmatter order and added a minimal primary-name block with unknown source language.
- Added `POV: 1740s` and temporal guidance for the existing account before Fausto's death.

### Validated judgments
- The plain-English name needs no pronunciation; its in-world source language is not established.
- Confirmed local evidence supports the existing positive `dm_notes` attestation. The local-only `SECRET` block was separately reviewed and preserved without copying its contents into this report.
- `status/gameupdate/dufr` is not assessable until the human chooses whether to update the article or retain its earlier viewpoint; it remains unchanged.

### Editorial assessment
**Underdeveloped**. The visible sentence omits the cult's defining leadership, purpose, coercion and institutional influence, and the collapse of its Chardonian power and release of its victims in DR 1749. A short sourced description plus a separately scoped aftermath paragraph would address these central gaps. The shared sources establish these dimensions; no speculative successor organization or new founding history is required.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The visible sentence calls [[Fausto]] a member and leaves the cult's purpose vague. The public, dated account in [[Fausto]] establishes his leadership, service to [[Apollyon]], control of the [[Crown of Purity]], and manipulation of the [[Hetaeri Magica]], [[Chamber of Stamps]], and chalyte trade to fund artifact recovery. The `Campaign:dufr` account in [[Crown of Purity]] establishes coercion and infiltration; [[Session 124 (DuFr)]] distinguishes magically controlled victims such as [[Vola]] and [[Vargus]] from the blackmailed [[Valius]]. These are defining features, not incidental campaign appearances. Copy-ready proposed account: “Under [[Fausto]], the Cleansed worked to restore [[Apollyon]] to power and pursue his vision of Hkaran purity. Fausto used the [[Crown of Purity]] to control key members of the [[Hetaeri Magica]] and [[Chamber of Stamps]], exploiting the [[chalyte]] trade to finance the search for Apollyon's artifacts. Those serving the Cleansed included magically coerced victims and people compelled by threats, as well as willing adherents.” Choose its campaign or date visibility before adoption; it must not silently replace the earlier public frame or equate all affiliated people with willing supremacists.
- [ ] **Warning — coverage.later_material_change:** [[Fausto]] records his death on DR 1749-05-24 and the exposure of the cult's chalyte network. [[Session 124 (DuFr)]] separately establishes that Riswynn's rededication of the Crown freed its victims, and [[Session 126 (DuFr)]] records lasting trauma and disruption among formerly controlled officials. These durable consequences are absent here. Human choice: update the account and reassess `POV`; defer and retain `status/gameupdate/dufr`; or deliberately retain this earlier account and decide whether to remove that tag. For a public aftermath layer, the smallest proposed block can follow [[Fausto]]'s existing revelation boundary: `%%^Date:1749-08-10%%`, then “Fausto died in DR 1749, and the exposure of the Cleansed's control over Chardon's chalyte trade left the [[Hetaeri Magica]] in disarray. The Crown's old bonds of domination were subsequently broken by [[Riswynn]]'s rededication of its power; some freed victims continued to suffer lasting harm.”, then `%%^End%%`. The date marker is a proposed visibility boundary, not the date of all these events. Keep the distinction between Fausto's death and the later breaking of the Crown's bonds; neither source establishes that every adherent was destroyed or every victim fully recovered.
- [ ] **Suggestion — metadata.ancestry_semantics:** `ancestry: mysterious` stores a description of uncertainty in a cultural classification field. [[Metadata Specification]] defines `ancestry` as a cultural or ancestry descriptor. Preserve the description without treating it as a culture: remove `ancestry: mysterious` and add `typeOfAlias: mysterious cult`, retaining `typeOf: cult`. This is a proposal because the intended classification and generated-header presentation need human disposition.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The member-query block uses `%%^Campaign:None%%`; the documented shared-private sentinel is `%%^Campaign:none%%`. Confirm the intended filtered visibility, then replace only that opening marker. The block and its Dataview code were preserved, and no visibility-changing conversion was applied.

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/_Campaign 3/Campaign 3 - Early Brainstorming - Overview]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Apollyon (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Vola Forena (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Chalice of the Runepriest (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Chardon NPC Flowchart]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Finding Artifacts in Chardon]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Hralgar's Eyes (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Power Structures]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 49]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 20]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 21]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Riswynn Solo Arc]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Elderwood Arc NPCs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part I To Arendum/Flowchart - Elderwood Part 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part I To Arendum/Part I To Arendum]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part I To Arendum/The Shadow Hunter]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part II Finding the Te'kula/Part II Finding the Te'kula]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Events in Tokra]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra Arc Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/History of Blasted Plains]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Major Players]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Summary]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/The Relics of Apollyon]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Apollyon Dopplegangers]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 115 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 116 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 120 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Politics - ChatGPT Summary]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Politics]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Timeline]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 125 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 126 - Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 128 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 129 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 73 - DM Notes]]
%%^End%%

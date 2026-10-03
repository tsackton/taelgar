---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:37:56-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/clee, status/check/lint]
species: human
ancestry: null
born: null
gender: male
name: Damien Montrichard
pronunciation: Dah-mee-en Mon-tree-shar
affiliations:
  - {org: Rangers}
whereabouts:
  - {type: away, start: 1720-01-14, location: Eftly}
  - {type: away, start: 1720-01-15, end: 1720-01-16, location: Champimont}
knownTo: [clee]
dm_owner: mike
dm_notes: important
POV: 1720s
---
# Damien Montrichard
*(Dah-mee-en Mon-tree-shar)*
>[!info]+ Biographical Info  
> A [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% needs to incorporate his false imprisonment and almost execution at the hands of [[Areschera]] %%

![[damien-montrichard.jpg|right|400]]A storyteller and musician, with a keen eye for lore.

%% Meta: 2nd or 3rd level bard 
 a musician and storyteller. He is charming and full of tales about his companions (mostly Adra and Enzo, it seems, who he clearly cares for and has spent some time with) but questions about his past or background just slide off him. You learn that Adra's ghostly birds are able to become quite real and peck her enemies, at need. But Adra prefers them as companions, and Damien tells (jokingly/lovingly) about some times when it seems like she is more motivated by finding a new bird than anything else. As the night wears on, and he gets a bit drunk, and leaves the stage, you do notice him and Adra and Enzo being served by an invisible servant of some sort.
%%

%%^Metadata:names:v1%%
- {"name":"Damien Montrichard","language":"unknown","pronunciation":"Dah-mee-en Mon-tree-shar","status":"documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a Cleenseau-era portrait of a Ranger musician; the January DR 1720 itinerary is dated, while the consequential February imprisonment and rescue remain absent from the visible account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and recorded the explicit name, campaign knowledge, name metadata, and temporal viewpoint where missing.
- Corrected the affiliations target from The Rangers to Rangers, matching [[Rangers]].

### Validated judgments
- status/gameupdate/clee is not assessable until the human chooses whether to update, defer, or preserve the earlier account.

### Editorial assessment
**Underdeveloped** — The visible musician description omits the defining accusation, captivity in Veltor Keep, and rescue that the played record and the note’s own update reminder identify. A brief dated account of that outcome is the smallest useful completion.

### Open findings

- [ ] **Warning — coverage.later_material_change:** [[Cleenseau - Session 18]] records Damien being blamed for an ambush and imprisoned; [[Cleenseau - Session 19]] records his rescue from Veltor Keep on February 21, DR 1720 and the exposure of Areschera. The target expressly asks to incorporate this history. Choose an update, deferral with the existing game-update tag, or preservation of the earlier portrait. Copy-ready dated addition:
```markdown
%%^Date:1720-02-21%%
In February DR 1720, Damien was falsely accused of arranging an ambush and imprisoned in [[Veltor Keep]]. The [[Heroes of Cleenseau]] freed him on February 21 and exposed [[Areschera]], the fey infiltrator behind his captivity.
%%^End%%
```

- [ ] **Suggestion — editorial.public_material_candidate:** The shared comment containing “a musician and storyteller” and [[Rangers in Champimont]] establish a recurring companionship with Adra and Enzo. A concise addition would connect this otherwise isolated reference entry: **Damien travels with [[Adra Brightwood]] and [[Enzo Brightwood]], whose exploits feature in his stories.** Keep class level, spell observations, and details about Adra’s abilities in the existing private guidance or her own note.
%%^End%%

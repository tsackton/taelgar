---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo: []
born: 1680
gender: male
name: Jonathon Henwyn
affiliations:
  - {org: Essfords, title: Steward}
  - {org: "Lord's Council of Cleenseau"}
whereabouts:
  - {type: home, location: Cleenseau}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Jonathon Henwyn
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[jonathon-henwyn.png|right|320]]The steward of the [[Essford Manor]] in [[Cleenseau]], Jonathon is responsible for its bookkeeping and upkeep, as well as collecting the rents from farmers and other manorial administration. 

He has a keen interest in history, and is a competent clerk and accountant. He took over as steward from his father-in-law in 1715. His wife is a childhood friend of [[Rosalind Essford|Rosalind]] and assists him. They and their three children live at [[Essford Manor]]. 

 %%^Campaign:Clee%%
### Jonathon's History Lesson
Before [[Cleenseau - Session 08]] Jonathon shared several facts and stories about Cleenseau:
- The hobgoblins occupied Cleenseau during the 3rd Hobgoblin War and built a motte and bailey castle / fortification here, but it was destroyed except for the actual hill of the motte by Cece's troops but a lot of rubble was left behind 
- Cleenseau was an army camp for a couple of years in the 1649 - 1651 period while Cece was still fighting the hobgoblins to the south.
- There are probably some records or information about this war hidden away in the garrison
- Essford Manor was built by [[Reginald Essford]] shortly after he became lord in the early 1650s on top of the hobgoblin-built motte  
- Underhill (the poor neighborhood where Tumbledown Manor is) was mostly built on top of the ruins of the hobgoblin fort in the 1660s and 1670s as the town grew. 

%%^End%%

%%^Metadata:names:v1%%
- {"name": "Jonathon Henwyn", "language": "unknown", "pronunciation": "JON-uh-thun HEN-win", "status": "proposed", "notes": "The English Sembaran analogue in [[Languages]] supports ordinary Jonathon and a provisional Henwyn reading with initial stress, short e, and wyn as win. The French alternative would alter the given-name consonants; the English-shaped spelling is the stronger cue, but the full pronunciation remains unconfirmed."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a portrait of his stewardship and family around DR 1719–1720; the campaign history lesson recounts older town history rather than widening the speaking position.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added required knownTo, minimal name metadata, and supported POV/povNotes.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes `JON-uh-thun HEN-win`. The English Sembaran analogue in [[Languages]] supports ordinary Jonathon and a provisional Henwyn reading with initial stress, short e, and wyn as win. The French alternative would alter the given-name consonants; the English-shaped spelling is the stronger cue, but the full pronunciation remains unconfirmed. Confirm or revise this reading; if accepted, copy it to frontmatter `pronunciation` and mark the entry documented.

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The history-lesson opener uses `%%^Campaign:Clee%%`. The campaign registry gives `clee`; replace only that opener with `%%^Campaign:clee%%`, preserving the existing content and end marker.
%%^End%%

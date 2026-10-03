---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/clee, status/check/lint]
species: human
ancestry: Sembaran
born: 1688
gender: male
title: Lord
name: Rinault Essford
aliases: [Lord Rinault, Lord Rinault Essford, Rinault]
affiliations:
  - {org: Essfords, title: Heir, type: primary}
whereabouts: Cleenseau
knownTo: [clee]
dm_owner: mike
dm_notes: important
POV: 1720s
---
# Lord Rinault Essford
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[Essfords]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[Lord-Rinault-Essford.png|right|320]]The younger brother of [[Rosalind Essford|Rosalind]], he is considered rash and impulsive. He openly dreams of bigger adventures and grander scales for his ambitions, but few trust him.

%%^Campaign:clee%%
### Rinault's Childhood Stories
Before [[Cleenseau - Session 08]] Rinault shares some stories of his childhood:
- When Renault was a bored teenager he sometimes took some buddies and went to smash stuff in the old ruins on the south side of the Enst. One night, he says, he swore he saw a skeleton arm move in the dirt. 
- He was fiercely forbidden from climbing around the hill or the basements of Essford Manor. He was always a rambunctious kid and often didn't follow the rules, but the one time he and two friends were "digging for buried treasure" in the side of the hill his father was apoplectic and he was confined to his room for a month afterwards. 
%%^End%%

%%^Campaign:none%%
### Relationships
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Alive"], 
			dv.pages("#person or #organization or #item")
				.where(f => util.isLinkedToPerson(f.file, dv.current().file))
				.sort(f => util.s("<maintype:n>", f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.isAlive(b.file.frontmatter, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Rinault Essford", "language": "Sembaran", "pronunciation": "ree-NOH ESS-ford", "status": "proposed", "notes": "The French strand of the Sembaran analogue in [[Languages]] gives Rinault an ee vowel and au as oh, with final lt silent; Essford is treated as an English-strand compound with short e and an audible ford. This mixed Sembaran adaptation remains proposed because no adopted pronunciation was found."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early-1720s portrait of Rinault with childhood recollections; his temporary authority during Rosalind’s absence is not yet described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting; added supported name and temporal review blocks, `POV`, and `knownTo`.
- Corrected “[[Rosalind Essford|Rosalind]] he is considered rash and impulse.” to “[[Rosalind Essford|Rosalind]], he is considered rash and impulsive.”.
- Normalized the existing campaign-block code from `%%^Campaign:Clee%%` to `%%^Campaign:clee%%` without adding or moving content.
- Normalized the existing campaign-block code from `%%^Campaign:None%%` to `%%^Campaign:none%%` without adding or moving content.

### Validated judgments
- `status/gameupdate/clee`: supported by the missing early-1720 acting-lord role; retained for human disposition after the article/POV choice.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The recaps for [[Cleenseau - Session 12]] and [[Cleenseau - Session 17]] identify Rinault as acting lord, while the article gives his family position and childhood stories without this substantive public responsibility. Add the bounded state without inventing permanent succession: “Rinault acted as lord of Cleenseau during Rosalind’s absence in early 1720.” Confirm the appointment’s bounds before adding a dated leader affiliation; the later return of Rosalind in [[The Situation in Asineau (Email)]] prevents treating the role as indefinite.

- [ ] **Suggestion — identity.inconsistent_spelling:** The first childhood-story bullet switches the subject’s name to “Renault,” while the title, metadata and surrounding text use Rinault. Proposed correction: “When Rinault was a bored teenager”. The linter leaves name decisions for human review.

- [ ] **Warning — metadata.names_unresolved_status:** The name-block pronunciation `ree-NOH ESS-ford` is proposed. The French strand of the Sembaran analogue in [[Languages]] gives Rinault an ee vowel and au as oh, with final lt silent; Essford is treated as an English-strand compound with short e and an audible ford. This mixed Sembaran adaptation remains proposed because no adopted pronunciation was found. Confirm it or supply the accepted full pronunciation before copying it to frontmatter and marking the entry documented.
%%^End%%

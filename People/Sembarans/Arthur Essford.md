---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:37:56-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo:
  - {campaign: clee, date: 1720-01-03}
born: 1682
gender: male
name: Arthur Essford
affiliations:
  - {org: Bybets, type: primary}
  - {org: Essfords, title: Lord Consort, start: 1706}
whereabouts:
  - {type: home, end: 1705, location: Ainwick}
  - {type: home, start: 1706, location: Cleenseau}
  - {type: away, start: 1720-01-04, end: 1720-01-19, location: travelling to Embry}
  - {type: away, start: 1720-01-20, end: 9999, location: Embry}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720s
---
# Arthur Essford
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[Bybets]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:clee%% Seen by the [[Heroes of Cleenseau]] on January 3rd, 1720 in [[Cleenseau]], the [[Manor of Cleenseau]], the [[Barony of Aveil]] %%^End%%

![[arthur-bybet-portrait.png|right|320]]The husband of [[Rosalind Essford|Rosalind]] (whom he married in 1706), he wisely takes a back seat in local affairs. He hails from a prominent family in [[Ainwick]]. He is an aficionado of stories and songs and often frequents [[The Crossroads Inn]] to hear the latest news.

In the fall of 1719, he lost his three children during the [[Tragic Flood of the River Enst]] and his and [[Rosalind Essford|Rosalind's]] sadness over this has been profound. 

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
- {name: "Arthur Essford", language: "Sembaran", pronunciation: "AR-thur ESS-ford", notes: "Proposed from the English component of Sembaran guidance in [[Languages]] and the English-form Arthur and -ford surname: th as in thin, doubled ss as s, and initial stress in each name. The French analogue would give Arthur a t sound and different vowels; the English-form surname supports this preferred proposal, not exact in-world phonology.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: A portrait around the beginning of the DR 1720s, after the loss of his children in autumn 1719; dated whereabouts separately track his journey to Embry.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported name, campaign-knowledge, and temporal metadata; normalized frontmatter formatting.
- Corrected “a aficionado” to “an aficionado”; normalized the private campaign sentinel to none without changing its scope.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `AR-thur ESS-ford` in `Metadata:names:v1`. Proposed from the English component of Sembaran guidance in [[Languages]] and the English-form Arthur and -ford surname: th as in thin, doubled ss as s, and initial stress in each name. The French analogue would give Arthur a t sound and different vowels; the English-form surname supports this preferred proposal, not exact in-world phonology. If accepted, copy it to frontmatter and mark the entry documented; otherwise supply the preferred reading.
%%^End%%

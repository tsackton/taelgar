---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/clee, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo:
  - {campaign: clee, date: 1720-01-03}
born: 1677
gender: female
title: Lady
name: Rosalind Essford
aliases: [Lady Essford, Lady Rosalind Essford, Rosalind]
affiliations:
  - {org: "Lord's Council of Cleenseau", type: leader, title: Leader}
  - {org: Cleenseau, type: leader, title: Regent, start: 1719-03-15, end: 1720-02-11}
  - {org: Cleenseau, type: leader, title: Lady, start: 1720-02-12}
whereabouts:
  - {type: home, location: Cleenseau}
  - {type: away, start: 1720-01-03, end: 1720-01-05, location: travelling to Rinburg}
  - {type: away, start: 1720-01-06, location: Rinburg}
  - {type: away, start: 1720-01-08, location: Fellburn}
  - {type: away, start: 1720-01-09, end: 1720-01-11, location: travelling to Wisford}
  - {type: away, start: 1720-01-12, end: 1720-01-13, location: Wisford}
  - {type: away, start: 1720-01-13, end: 1720-01-16, location: travelling to Embry}
  - {type: away, start: 1720-01-17, end: 9999, location: Embry}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Lady Rosalind Essford
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:clee%% Seen by the [[Heroes of Cleenseau]] on January 3rd, 1720 travelling to [[Rinburg]], in the [[Barony of Aveil]], [[Sembara]] %%^End%%

![[lady-rosalind-essford.png|right|320]]The daughter of [[Wymar Essford|Wymar]], short, and with hair just beginning to grey, but forceful out of proportion to her size, and with a sharp intelligence to her eyes. Popular with the townspeople and said to be wise and fair. She married [[Arthur Essford]] in 1706, and their match has been a good and popular one. 

%%^Date:1719%%
In the late fall of 1719, she lost her three children and their nursemaid to a [[Tragic Flood of the River Enst|unseasonable flood of the Enst]].  She enjoys quiet music, especially [[Robin of Abenfyrd|Robin's]] playing, which has been a comfort to her since her children died.
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

%% I have more information about her in some emails and DM notes that could be added here, mostly personality notes %%

%%^Metadata:names:v1%%
- {"name": "Rosalind Essford", "language": "Sembaran", "pronunciation": "ROZ-uh-lind ESS-ford", "notes": "Proposed from the English analogue in [[Languages]]: voiced s in Rosalind and first stress in both names; alternate Rosalind vowels remain possible.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 portrait of her household and rule, with a dated account of the autumn 1719 loss of her children; the open-ended Embry stay is outdated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Recorded Cleenseau campaign knowledge from existing campaign metadata or the reviewed session sources.
- Added the supported article viewpoint and persistent name and temporal metadata.
- Corrected “She enjoys quite music” to “She enjoys quiet music”.
- Normalized the existing campaign marker to its canonical lowercase value without changing its scope.

### Validated judgments
- Status disposition: `status/gameupdate/clee` is not assessable until the human chooses whether to update, defer, or preserve the earlier account; the tag is preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed full-name pronunciation `ROZ-uh-lind ESS-ford` in `Metadata:names:v1`. The English analogue for Sembaran in [[Languages]] supports voiced s in Rosalind, first-syllable stress, and the transparent Ess + ford surname. Rosalind also has other ordinary vowel readings, so this full-name proposal requires acceptance. If accepted, copy it to frontmatter and mark the entry documented; otherwise revise the persistent proposal.

- [ ] **Warning — coverage.later_material_change:** The last whereabouts entry places Rosalind in Embry through 9999, while [[Cleenseau - Session 24 - Original]] reports her withdrawing with her forces toward Fellburn beside the condemned Duke of Wisford by early March DR 1720. A bounded replacement for the ongoing state is `{type: away, location: travelling to Fellburn, start: 1720-03-04}` after ending the Embry entry; the source establishes a report by that date, not her exact departure. Confirm the date semantics before adoption, defer for game-update review, or intentionally preserve the earlier snapshot. This public military alignment is also a consequential addition: “By early March DR 1720, Rosalind and her forces were reported to be withdrawing toward Fellburn with the Duke of Wisford after his treason sentence.”
%%^End%%

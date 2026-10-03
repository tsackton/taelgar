---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo:
  - {campaign: clee, date: 1720-01-03, type: roused}
born: 1652
died: 1720-02-11
gender: male
title: Lord
name: Wymar Essford
affiliations:
  - {place: Cleenseau, start: 1689}
  - {org: Essords, type: primary}
whereabouts: Cleenseau
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Lord Wymar Essford
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of Essords
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:clee%% Roused by the [[Heroes of Cleenseau]] on January 3rd, 1720 in [[Cleenseau]], the [[Barony of Aveil]], [[Sembara]] %%^End%%

![[WymarOfClenseau.jpeg|right|320]]The aging and senile lord of the manor in [[Cleenseau]]. The son of [[Reginald Essford]] and [[Celine Essford]]. He is rarely involved in the day to day events of the town. His children are [[Rosalind Essford]] and [[Rinault Essford]]. Since March 1719, he has been suffering from increasingly significant dementia and his daughter has largely taken over the management of [[Cleenseau]]. 

### Wymar's Story of Childhood

>[!info] Childhood Story, as told to [[Viepuck]] under the influence of his patron's mind-probe
In his childhood, he recalled overhearing his parents (Reginald and Celine). Reginald was very drunk, and was weeping. Wymar recalls hearing his father sobbing to Celine: "I can't forget it. That day, the bodies just kept walking up out of the tower, just below us, and he was grinning even as we struck him down. Mother help me, I want to forget. Sometimes in my dreams I still see it. Was it wrong to build here? Is this place cursed?".


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
- {"name": "Wymar Essford", "language": "Sembaran", "pronunciation": "WYE-mar ESS-ford", "status": "proposed", "notes": "Prefer the English Sembaran analogue in [[Languages]] for Wymar and the English-shaped Essford: initial w, y as in why, retained r, doubled ss as s, and initial surname stress. A French-style vee-MAR is possible; the preferred local reading remains proposed."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early DR 1720 portrait of the ill lord before his February 11 death, with a separate childhood recollection; the undated living-state prose has not been updated to the recorded death.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [clee]` from campaign evidence, persistent name metadata, and a supported article POV with temporal notes.
- Normalized frontmatter order and collection formatting where needed.
- Canonicalized legacy campaign codes without changing the represented campaign or block visibility.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary name remains `proposed`. Preferred pronunciation: `WYE-mar ESS-ford`. Prefer the English Sembaran analogue in [[Languages]] for Wymar and the English-shaped Essford: initial w, y as in why, retained r, doubled ss as s, and initial surname stress. A French-style vee-MAR is possible; the preferred local reading remains proposed. Accept the intended pronunciation and record it in frontmatter, or revise the name-block proposal before clearing this task.
- [ ] **Warning — relationship.unresolved:** The affiliation `org: Essords` does not resolve. [[Essfords]], founded by his father [[Reginald Essford]], establishes the family target. Candidate: `{org: Essfords, type: primary}`. Confirm that correction and regenerate the corresponding header phrase ‘of Essords’; the current result leaves the authored relationship untouched.
- [ ] **Warning — coverage.later_material_change:** Frontmatter records his death on DR 1720-02-11, [[Cleenseau Campaign - Index of NPCs]] calls him recently deceased, and [[Rosalind Essford]] records her succession, but the visible paragraph still describes a living current lord. Candidate addition: `Wymar died on February 11, DR 1720, and [[Rosalind Essford]] succeeded him as lady of Cleenseau.` Decide whether to update the paragraph and POV, retain an explicitly early-1720 portrait with a separately dated death passage, or defer with a game-update tag. A proposed `%%^Date:1720-02-11%%` block should enclose only the new death/succession sentence, followed by `%%^End%%`; no visibility block was added automatically.
%%^End%%

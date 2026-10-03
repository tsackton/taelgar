---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
born: 1688
died: 1720-01-06
gender: female
name: Ysabel
affiliations:
  - {org: "Lord's Guard of Cleenseau", title: Sheriff}
whereabouts:
  - {type: home, location: Cleenseau}
knownTo: [clee]
dm_owner: mike
dm_notes: none
POV: 1719
---
# Ysabel
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[ysabel.png|right|420]] A striking and comely woman with a rough scar running from her eye to her neck. She is the sheriff of [[Cleenseau]] and leads a part of the [[Lord's Guard of Cleenseau|Lord's Guard]]. She has many opinions about her employers, in particular [[Rinault Essford]], and does not always successfully keep them to herself.

She grew in skill of arms and bravery during an unsettled period in late 1719, but died fighting zombies during the [[Undead Attacks in Sembara]].

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
- {"name": "Ysabel", "language": "Sembaran", "pronunciation": "ee-zah-BEL", "status": "proposed", "notes": "French-influenced Sembaran reading from [[Languages]]: initial y as ee, s voiced as z between vowels, and final syllable emphasis with pronounced l. An English IZ-uh-bel is possible; no pronunciation for this particular sheriff is recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late DR 1719 living portrait of the sheriff, followed by a DR 1720 death account; the two visible temporal layers still require human separation.
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

- [ ] **Warning — metadata.names_unresolved_status:** The primary name remains `proposed`. Preferred pronunciation: `ee-zah-BEL`. French-influenced Sembaran reading from [[Languages]]: initial y as ee, s voiced as z between vowels, and final syllable emphasis with pronounced l. An English IZ-uh-bel is possible; no pronunciation for this particular sheriff is recorded. Accept the intended pronunciation and record it in frontmatter, or revise the name-block proposal before clearing this task.
- [ ] **Warning — temporal.inconsistent_viewpoint:** The first paragraph says ‘She is the sheriff’ and ‘leads’, while the next paragraph and `died: 1720-01-06` establish her death. Preserve a living DR 1719 portrait by proposing `%%^Date:1720-01-06%%` around the complete second paragraph, followed by `%%^End%%`, or make the first paragraph retrospective: `She was the sheriff of [[Cleenseau]] and led a part of the [[Lord's Guard of Cleenseau|Lord's Guard]]. She had many opinions about her employers, in particular [[Rinault Essford]], and did not always successfully keep them to herself.` Choose one temporal treatment; the lint did not change visibility or silently replace the living account.
%%^End%%

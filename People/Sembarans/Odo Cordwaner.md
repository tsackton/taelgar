---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/clee, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo:
  - {campaign: clee}
born: 1700
gender: male
name: Odo Cordwaner
affiliations:
  - {org: Army Garrison of Cleenseau, end: 1719-11-05, title: Sergeant}
  - {org: "Lord's Guard of Cleenseau", start: 1719-11-16, title: Guardsman}
whereabouts:
  - {type: home, location: Eftly}
  - {type: home, location: Cleenseau, start: 1718}
  - {type: away, start: 1719-10-21, end: 1719-10-23, location: Taviose}
  - {type: home, start: 1719-11-16, location: Taviose}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Odo Cordwaner
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[odo-cordwaner.png|right|320]] Until recently a sergeant of the [[Army Garrison of Cleenseau|Bridge Patrol]], he was discharged after failing to heed orders during the [[Festival of the Bridge]]. He allowed [[Francois the Bandit|François the Bandit]] access to the food area, despite specific warnings to be on the lookout.

Investigation determined that he was not malicious, but just careless. In the excitement of the festival, he failed to pay attention as he should have. He was discharged from the [[Army of the West]], but at the intervention of [[Robin of Abenfyrd|Robin]], was hired by the [[Essfords]] to provide a steady presence in [[Taviose]].

He has since developed a romantic attachment to [[Abigail Moss]], and has come to believe that his mistake was the hand of [[The Warlord]], setting him on a path to find his true calling (and setting the [[Heroes of Cleenseau]] on the path to become heroes).

His family is based in [[Eftly]], but he left home at 18 to join the army, being one of five children and with no interest in farming.

In late April 1720, Odo came to [[Asineau]] with his younger brother [[Samuel Cordwaner|Samuel]] and [[Abigail Moss]] to serve as captain of the manor's guard.

%% See [[The Destruction of Eftly]] for some background information %%

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
- {"name": "Odo Cordwaner", "language": "Sembaran", "pronunciation": "OH-doh KORD-way-ner", "notes": "Proposed from the English analogue in [[Languages]]: OH-doh and hard-c, first-stressed KORD-way-ner; surname vowels are uncertain.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 portrait with earlier army history and a dated move to Asineau in late April; the Taviose metadata and family statement need reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Recorded Cleenseau campaign knowledge from existing campaign metadata or the reviewed session sources.
- Added the supported article viewpoint and persistent name and temporal metadata.
- Corrected “on the lookup.” to “on the lookout.”.
- Normalized the existing campaign marker to its canonical lowercase value without changing its scope.

### Validated judgments
- Status disposition: `status/gameupdate/clee` is not assessable until the human chooses whether to update, defer, or preserve the earlier account; the tag is preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed full-name pronunciation `OH-doh KORD-way-ner` in `Metadata:names:v1`. This uses the English side of the Sembaran analogues in [[Languages]]: long o in Odo, hard c and first-syllable stress in Cordwaner, with -waner read way-ner. The unstated surname vowels are uncertain; a French-influenced reading is also possible, so this remains a proposal. If accepted, copy it to frontmatter and mark the entry documented; otherwise revise the persistent proposal.

- [ ] **Warning — coverage.later_material_change:** The final paragraph and [[Cleenseau - Session 29]] place Odo in Asineau as guard captain in late April DR 1720, but the active home and guard affiliation still point to Taviose and Cleenseau. Update those fields with the supported move after deciding the appropriate date precision, defer for game-update review, or preserve an explicitly earlier metadata snapshot. A bounded proposed entry is `{type: home, location: Asineau, start: 1720-04}` with affiliation `{org: Manor of Asineau, title: Captain of the guard, start: 1720-04}`; confirm the month’s boundary semantics before adoption.

- [ ] **Warning — coverage.later_material_change:** “His family is based in Eftly” no longer fits [[The Destruction of Eftly]], in which Odo grieves his brothers and believes Samuel may also have died. [[Cleenseau - Session 16]] and [[Samuel Cordwaner]] establish Samuel’s survival. Candidate: “Odo came from [[Eftly]]. After its destruction in January DR 1720, he believed himself the only surviving brother; his younger brother [[Samuel Cordwaner|Samuel]] was later found alive.” Revise the undated family sentence or intentionally date it to the earlier state; preserve the distinction between Odo’s belief and confirmed fate.

- [ ] **Warning — coverage.established_fact_missing:** [[Cleenseau - Session 15]] records Robin’s formal induction of Odo into the [[Order of the Charitable Wanderer]]. This lasting religious affiliation is absent from both his affiliations and the account of his new calling. Candidate: “During the undead crisis of DR 1720, [[Robin of Abenfyrd]] inducted Odo into the [[Order of the Charitable Wanderer]].” Add the affiliation or a brief sourced sentence after confirming its temporal framing.
%%^End%%

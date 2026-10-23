---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {partOf: ""}
tags: [group, status/check/lint]
typeOf: clan
ancestry: orc
created: 843
name: People of the Rainbow
whereabouts:
  - {type: home, end: 940, location: Amberglow}
  - {type: home, start: 940, end: 1050, location: unknown}
  - {type: home, start: 1051, end: 1582, location: wandering and hiding}
  - {type: home, start: 1583, location: Xurkhaz}
dm_owner: tim
dm_notes: important
POV: modern
---
# The People of the Rainbow
>[!info]+ Information  
> An [[Orcs|orc]] clan  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% Whereabouts date qualifications preserved from frontmatter:
- Entry {type: home, end: 940, location: Amberglow}: #end is +/- 10 years
- Entry {type: home, start: 940, end: 1050, location: unknown}: #start +/- 10 years
%%

The name for the [[Orcs]] of [[Xurkhaz]] who have lived free from [[Thark]]'s curse for many generations.
## History

The People of the Rainbow trace their origins to the Golden Age of the [[Drankorian Empire]], when their ancestors were freed from [[Thark]]'s chains by the gift of an archfey known as the [[Cloudspinner]]. In those days, the People of the Rainbow grew and prospered in the [[Feywild]] domain of [[Amberglow]], under the [[Cloudspinner]]'s protection, and safe from [[Thark]]'s reach. 

As they grew, the People of the Rainbow wished to free their brethren from [[Thark]]'s chains, so with the [[Cloudspinner]]'s blessing and the gift of the [[Cloak of Rainbows|Cloak of Rainbows]] to protect them, they ventured back to the material plane. 

However, rumors of the unchained [[Orcs]] and the [[Cloak of Rainbows|Cloak of Rainbows]] and its power grew in [[Drankorian Empire|Drankor]], and eventually attracted the attention of [[Apollyon|Apollyon]], the emperor, who attacked the People of the Rainbow, and stole the [[Cloak of Rainbows|Cloak of Rainbows]] for himself. 

For the next five hundred years, the People of the Rainbow lived a hunted existence, scattered in small groups trying to avoid the ever-watchful eyes of [[Thark]] and the violence of his servants, until after the [[Great War]], when [[Uzgash]], the leader of a small tribe of orcs hiding in the [[Nashtkar]], discovered the long-lost [[Cloak of Rainbows|Cloak of Rainbows]] in a ruined Dunmari fort. Using the power of the cloak, he founded the kingdom of [[Xurkhaz]]. The People of the Rainbow have lived in [[Xurkhaz]] ever since, under the protection of the [[Cloak of Rainbows|Cloak of Rainbows]]. Over the years, as rumors of [[Xurkhaz]] spread, lost tribes of the People of the Rainbow hiding in distant places have begun to return when they can.

Now, the People of the Rainbow are thriving in [[Xurkhaz]], and perhaps in other hidden pockets of the world. 
### Events
- (DR:: 917): [[Cloak of Rainbows]] is gifted to the People of the Rainbow by [[Cloudspinner]]
- (DR:: 930)-(DR_end:: 950): People of the Rainbow begin to drift out of the feywild, seeking to free their chained brethren
- (DR:: 1050): [[Apollyon]] attacked the People of the Rainbow and the [[Cloak of Rainbows|Cloak of Rainbows]] was lost.
- (DR:: 1582): [[Uzgash]] finds the [[Cloak of Rainbows|Cloak of Rainbows]] in a Dunmari fort in the [[Nashtkar]]
- (DR:: 1583): [[Xurkhaz]] is founded as the new homeland of the People of the Rainbow. 

%%SECRET[v2:9129629b3cc26a5dd89b20c6e9a208fc]%%

%%^Campaign:none%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "People of the Rainbow", "language": "Common", "status": "inferred", "notes": "The transparent English display form follows the Common-name convention in [[Languages]]."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern account of the free orcs of Xurkhaz, with selected history from Amberglow through the founding of Xurkhaz; the visible history does not yet recount the later War of the Cloak.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and recorded the Common display name and modern POV/povNotes.
- Moved the two inline whereabouts comments into an ordinary comment below the complete header, retaining their exact text and their original entry context; all date values and their uncertainty are unchanged.
- Standardized Campaign:none after verifying identical filtering behavior, and joined the unambiguous “Until after” sentence fragment to its preceding sentence.

### Validated judgments
- The historical outline is consistent with [[Tale of the Cloak of Rainbows]] and [[Story of Xurkhaz]]; their attributed accounts remain distinct from omniscient history.
- Confirmed local source matches support the positive dm_notes attestation. The SECRET block was separately reviewed; its contents are not copied into this report.

### Open findings

- [ ] **Warning — coverage.later_material_change:** The visible history ends with the refounding of Xurkhaz and a statement that the people are thriving, while [[War of the Cloak]] records a later invasion aimed at taking their protective cloak and the siege of their capital. This was a defining threat to the people and their homeland. A bounded addition is: “In the [[War of the Cloak]], Grash’s armies invaded [[Xurkhaz]] to seize the [[Cloak of Rainbows]]. The [[Siege of Uzgukhar]] ended when the [[Dunmar Fellowship]] defeated Grash, preserving the people’s homeland and the cloak.” Choose whether to update the article, defer with the appropriate game-update status, or intentionally preserve its earlier historical scope. If filtered chronology is desired, place only this addition in a `Date:1749-01-20` block; that visibility change remains a proposal.

### DM evidence
- [[_DM_/Timelines/Cloak of Rainbows Timeline]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Timeline for the End of Drankor]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/The Story of Apollyon and Cha'mutte]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 70 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 83 - DM Notes]]
%%^End%%

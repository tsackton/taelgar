---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T22:19:46-04:00"
lintVersion: "2.5"
displayDefaults: {defArt: the}
tags: [place, status/check/name, status/check/lint]
typeOf: region
name: Coastlands
whereabouts:
  - {type: home, location: Chardonian Empire}
dm_owner: none
dm_notes: none
POV: 1740s
---
# The Coastlands
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Coastlands is the colloquial name for the coastal region of the Chardonian Empire, stretching from the borders of [[Portalia]] in the south to the [[Mawar Mountains]] in the north, and bounded inland by the [[Beacon Hills]] and the [[Chardon Hills]]. 

The Low Coast, the portion of coastlands south of [[Chardon]], is hot and dry in the summer, with mild winters and extensive coastal wetlands. 

The Upper Coast, the portion of the coastlands north of [[Chardon]], is rich agricultural land, with many rivers and mild weather, sandy beaches and small stands of ancestral forests among fields of wheat. The land here slopes gently up to the [[Beacon Hills]]. 

Much of the Upper Coast was occupied by [[Hobgoblins|hobgoblins]] during the [[Blood Years]]. 

Five major rivers, and several smaller ones, flow through the coastlands. From south to north, they are:
- [[Dashun]]
- [[Zar]]
- [[Corvessa]]
- [[Sevros]]
- [[Breakrock]]

## Places in the Coastlands
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```


%%^Campaign:none%%

See: [[Hobgoblin Movements After Cha'Mutte]] and [[West Coast History Framework]] for historical context. 

Sandy beaches, leading to land of rivers and farms and pastures, breadbasket of Chardon (Upper Coast)
Geography of Low Coast less developed. 

Relatively few big cities? perhaps one or two in the north? Not sure yet about urbanization in this area. Open to develop. 

Generally part of the "core" of the Chardonian Empire and generally Chardonian rule is popular here. 

%%^End%%

%%^Metadata:article:v1%%
mode: geographic reference
povNotes: "Accuracy range: approximately the DR 1740s. Geographic Reference for Coastlands; the visible description is a current-era reference, while established history and later developments may remain incomplete."
%%^End%%

%%^Lint%%
### Applied changes
- Canonicalized frontmatter, added an explicit `name`, and recorded the note's reviewed `POV`.
- Added persistent Metadata:article:v1 interpretation.

### Validated judgments
- The missing-pronunciation check was dispositioned as not applicable because this is a plain-English descriptive title or an otherwise obvious ordinary label.

### Open findings
- [ ] **Warning — status.disposition:** Existing status `status/check/name` remains in force. Its underlying name, cleanup, review, game-update, stub, or work-in-progress question requires human disposition; the lint did not alter it.
%%^End%%

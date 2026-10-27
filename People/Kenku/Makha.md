---
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person]
species: kenku
ancestry: Islander
campaignInfo:
  - {campaign: dufr, person: Wellby, date: 1748-10-12, type: met}
born: 1712
activeYear: 1740
gender: male
name: Makha
pronunciation: MAH-kah
whereabouts: Wahacha
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
```taelgar-header
```

![[makha.png|right|320]]The port master and unofficial town spokesperson for the kenku settlement of [[Wahacha]].  
## Relationships:
Makha knows the people of Wahacha well, including:
- [[Nahto]] and [[Skoda]], a married couple, travelers and wanderers based out of Wahacha
- [[Rufus]], a monster hunter, who hunts down threats to the island in exchange for food and shelter from the islanders

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
- {"name": "Makha", "language": "unknown", "pronunciation": "MAH-kah", "status": "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Makha's office and local relationships as described around Wellby's October DR 1748 visit; no wider tenure is established.
%%^End%%

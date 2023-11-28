---
headerVersion: 2023.11.25
tags: [clee/unsorted, person, dufr/unaware, status/unknown]
displayDefaults: {startStatus: born, startPrefix: b., endPrefix: d., endStatus: died}
campaignInfo: []
name: Rosalind Essford
born: 1677
species: human
ancestry: Sembaran
gender: female
aliases: [Lady Essford, Lady Rosalind Essford]
title: Lady
affiliations:
- {org: Lord's Council of Cleenseau, type: leader }
- {org: Cleenseau, type: leader, start: 1719-03-15}
whereabouts:
- {type: home, start: !!null '', end: '', location: 'Cleenseau, Sembara'}
---
# Lady Rosalind Essford
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The daughter of [[Wymar Essford|Wymar]], short, and with hair just beginning to grey, but forceful out of propotion to her size, and with a sharp intelligence to her eyes. Popular with the townspeople and said to be wise and fair. In the late fall of 1719, she lost her three children and their nursemaid to a [[Tragic Flood of the River Enst|unseasonable flood of the Enst]]. 

![[lady-rosalind-essford.png]]


%%^Campaign:None%%
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
---
headerVersion: 2023.11.25
tags: [dufr/background, person]
campaignInfo: 
- {campaign: dufr, person: Wellby, date: 1748-10-12, type: met}
name: Makha
born: 1712
species: kenku
ancestry: Islander
gender: male
whereabouts: Wahacha
pronunciation: MAH-kah
---
# Makha
*(MAH-kah)*
>[!info]+ Biographical Info
> An Islander [[Kenku|kenku]], he/him
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by [[Wellby]] on October 12th, 1748 in [[Wahacha]], the [[Vermillion Isles]], [[~Eastern Islands~]] %%^End%%

The port master and unofficial town spokesperson for the kenku settlement of [[Wahacha]].  

![[makha.png|500]]

## Relationships:
Makha knows the people of Wahacha well, including:
- [[Nahto]] and [[Skoda]], a married couple, travelers and wanderers based out of Wahacha
- [[Rufus]], a monster hunter, who hunts down threats to the island in exchange for food and shelter from the islanders


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
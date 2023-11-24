---
headerVersion: 2023.11.20
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
> Islander [[Kenku|kenku]], he/him
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by [[Wellby]] on October 12th, 1748 in [[Wahacha]], the [[Vermillion Isles]], [[~Eastern Islands~]] %%^End%%

The port master and unofficial town spokesperson for the kenku settlement of [[Wahacha]].  

![[makha.png|500]]

## Relationships:
Makha knows the people of Wahacha well, including:
- [[Nahto]] and [[Skoda]], a married couple, travelers and wanderers based out of Wahacha
- [[Rufus]], a monster hunter, who hunts down threats to the island in exchange for food and shelter from the islanders

%%^Campaign;None%%

```dataviewjs
const { util } = customJS
dv.table(["Person", "Current", "Known to Clee"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation("Wahacha", f.file.frontmatter, false))
				.map(b => [util.getName(b.file.name), util.getLoc(b.file.frontmatter), util.isKnownToParty(b.file.name, b.file.frontmatter, "clee", true, true)]))
```

```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```

%%^End%%
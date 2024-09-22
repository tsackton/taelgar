---
headerVersion: 2023.11.25
tags: [person]
ancestry: Isinguer
species: human
gender: male
born: 1674
whereabouts: 
- {type: home, location: Laicon, end: 1698 }
- {type: home, location: Cleenseau, start: 1699 }
dm_notes: none
dm_plans: no
---
# Arnaud Ausson
>[!info]+ Biographical Info  
> An [[Istabor Alliance|Isinguer]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[arnaud-ausson.png|right|320]]A prominent merchant in [[Cleenseau]], his grandmother, [[Lizette Ausson]], traces her family to [[Isingue]] and he and his wife Alessia are the heart of a small community of Isinguen transplants in [[Cleenseau]]. He is well connected with the [[Refounded Alliance of Aurbez]] and well known to the merchant caravans that come from places like [[Laicon]] with recovered dwarven metals. 

He remains close to his aunt, [[Giselle Ausson]], who runs [[Ausson's Crossing]], and important inn in [[Laicon]].


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
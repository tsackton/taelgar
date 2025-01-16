---
headerVersion: 2023.11.25
tags: [person, status/cleanup/gameupdate]
campaignInfo: [ {campaign: clee, date: 1720-01-03 }]
name: Rosalind Essford
born: 1677
species: human
ancestry: Sembaran
gender: female
aliases: [Lady Essford, Lady Rosalind Essford, Rosalind ]
title: Lady
affiliations:
- {org: Lord's Council of Cleenseau, type: leader, title: Leader }
- {org: Cleenseau, type: leader, title: Regent, start: 1719-03-15, end: 1720-02-11 }
- {org: Cleenseau, type: leader, title: Lady, start:  1720-02-12 }
whereabouts:
- {type: home, location: Cleenseau }
- {type: away, start: 1720-01-03, end: 1720-01-05, location: travelling to Rinburg }
- {type: away, start: 1720-01-06, location: Rinburg }
- {type: away, start: 1720-01-08, location: Fellburn }
- {type: away, start: 1720-01-09, end: 1720-01-11, location: travelling to Wisford }
- {type: away, start: 1720-01-12, end: 1720-01-13, location: Wisford }
- {type: away, start: 1720-01-13, end: 1720-01-16, location: travelling to Embry }
- {type: away, start: 1720-01-17, end: 9999, location: Embry }
dm_notes: color
dm_owner: mike
---
# Lady Rosalind Essford
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:clee%% Seen by the [[Heroes of Cleenseau]] on January 3rd, 1720 travelling to [[Rinburg]], in the [[Barony of Aveil]], [[Sembara]] %%^End%%

![[lady-rosalind-essford.png|right|320]]The daughter of [[Wymar Essford|Wymar]], short, and with hair just beginning to grey, but forceful out of proportion to her size, and with a sharp intelligence to her eyes. Popular with the townspeople and said to be wise and fair. She married [[Arthur Essford]] in 1706, and their match has been a good and popular one. 

%%^Date:1719%%
In the late fall of 1719, she lost her three children and their nursemaid to a [[Tragic Flood of the River Enst|unseasonable flood of the Enst]].  She enjoys quite music, especially [[Robin of Abenfyrd|Robin's]] playing, which has been a comfort to her since her children died. 
%%^End%%

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

%% I have more information about her in some emails and DM notes that could be added here, mostly personality notes %%
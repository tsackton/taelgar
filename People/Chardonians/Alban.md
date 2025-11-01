---
headerVersion: 2023.11.25
tags: [person, status/cleanup/metadata]
campaignInfo:
- {campaign: dufr, date: 1748-04-15, type: grave discovered}
name: Alban
born: 1719
species: human
ancestry: Chardonian
gender: male
died: 1748-03-18
affiliations: [Society of the Open Scroll]
whereabouts:
- {type: home, location: Chardon}
- {type: away, start: 1747-12-23, end: 1748-02-02, prefix: traveling in, location: Yeraad River Basin}
- {type: away, start: 1748-02-02, end: 1748-03-13, prefix: traveling in, location: Dunmar}
- {type: away, start: 1748-03-13, end: 9999, location: Stormcaller Tower}
dm_notes: color
dm_owner: none
---
# Alban
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Grave discovered by the [[Dunmar Fellowship]] on April 15th, 1748 in [[Gazetteer/Greater Dunmar/Hara Basin/Stormcaller Tower]], [[Eastern Dunmar]], [[Dunmar]] %%^End%%

%% some minor canonical locations in late 1747 - mid 1748 not captured completely in whereabouts %%

An adventurer associated with the [[Society of the Open Scroll]]. 

%%^Campaign:dufr%%
Traveled with [[Dee Wildcloak]] and [[Dain Goldhammer]] to [[Gazetteer/Greater Dunmar/Hara Basin/Stormcaller Tower]], where he was killed. 
## Chronology

```dataview
LIST WITHOUT ID events.text flatten file.lists as events where contains(events.text, this.file.name) and contains(events.text, "DR") sort events.DR
```
%%^End%%

%%SECRET[1]%%
---
headerVersion: 2023.11.25
tags: [person, status/cleanup/metadata]
displayDefaults: {endStatus: petrified}
campaignInfo:
- {campaign: dufr, date: 1748-03-25, type: discovered as a statue}
name: Arcus
born: 1723
species: human
ancestry: Chardonian
gender: male
died: 1748-03-15
affiliations: [Society of the Open Scroll]
whereabouts:
- {type: home, location: Chardon}
- {type: away, start: 1747-12-23, end: 1748-02-02, prefix: traveling in, location: Yeraad River Basin}
- {type: away, start: 1748-02-02, end: 1748-03-03, prefix: traveling in, location: Dunmar}
- {type: away, start: 1748-03-03, end: 1748-03-05, location: Karawa}
- {type: away, start: 1748-03-14, end: 9999, location: Dunmari Fort (Gomat)}
dm_notes: none
dm_owner: none
---
# Arcus
>[!info]+ Biographical Info
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Discovered as a statue with the [[Dunmar Fellowship]] on March 25th, 1748 in the [[Dunmari Fort (Gomat)]] %%^End%%

%% some canonical travel not captured in whereabouts yet %%

An adventurer and treasure hunter from the [[Society of the Open Scroll]], now petrified in the fort east of [[Gomat]]. 

%%^Campaign:dufr%%
Left [[Chardon]] with [[Servius]], [[Dee Wildcloak]], [[Dain Goldhammer]], and [[Alban]]. Argued constantly with [[Servius]], acording to [[Dee Wildcloak]]. Parted ways with other travelers in [[Songara]], presumably to press ahead. 

Passed through [[Karawa]] alone in late February or early March, according to [[Jasu]] and [[Ikram]].

## Chronology

```dataview
LIST WITHOUT ID events.text flatten file.lists as events where contains(events.text, this.file.name) and contains(events.text, "DR") sort events.DR
```
%%^End%%
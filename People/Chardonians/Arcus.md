---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T18:23:23-04:00"
lintVersion: "3.5"
displayDefaults: {endStatus: petrified}
tags: [person, status/cleanup/metadata]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, date: 1748-03-25, type: discovered as a statue}
born: 1723
gender: male
died: 1748-03-15
name: Arcus
pronunciation: AR-koos
affiliations: [Society of the Open Scroll]
whereabouts:
  - {type: home, location: Chardon}
  - {type: away, start: 1747-12-23, end: 1748-02-02, prefix: traveling in, location: Yeraad River Basin}
  - {type: away, start: 1748-02-02, end: 1748-03-03, prefix: traveling in, location: Dunmar}
  - {type: away, start: 1748-03-03, end: 1748-03-05, location: Karawa}
  - {type: away, start: 1748-03-14, end: 9999, location: Dunmari Fort (Gomat)}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1748
---
# Arcus
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Discovered as a statue by the [[Dunmar Fellowship]] on March 25th, 1748 in the [[Dunmari Fort (Gomat)]] %%^End%%

%% some canonical travel not captured in whereabouts yet %%

An adventurer and treasure hunter from the [[Society of the Open Scroll]], now petrified in the fort east of [[Gomat]]. 

%%^Campaign:dufr%%
Left [[Chardon]] with [[Servius]], [[Dee Wildcloak]], [[Dain Goldhammer]], and [[Alban]]. Argued constantly with [[Servius]], acording to [[Dee Wildcloak]]. Parted ways with other travelers in [[Songara]], presumably to press ahead. 

Passed through [[Karawa]] alone in late February or early March, according to [[Jasu]] and [[Ikram]].

## Chronology

```dataview
LIST WITHOUT ID events.text
FROM [[Arcus]] AND -"_sessions" AND -"Worldbuilding"
FLATTEN file.lists AS events
WHERE contains(events.text, this.file.name) AND contains(events.text, "DR")
SORT events.DR
```
%%^End%%


%%SECRET[v2:68301e3aaee1fb07af463b7a11db1511]%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 account of Arcus's final expedition and petrified state; his earlier life is not described beyond his departure from Chardon.
%%^End%%

%%^Metadata:names:v1%%
- {name: Arcus, language: Chardonian, pronunciation: AR-koos, status: documented}
%%^End%%

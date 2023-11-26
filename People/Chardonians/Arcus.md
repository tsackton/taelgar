---
headerVersion: 2023.11.25
tags: [dufr/aware, person, dufr/minor, status/unknown]
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
- {type: away, start: 1747-12-23, end: 1748-02-02, location: traveling in the Yeraad watershed}
- {type: away, start: 1748-02-02, end: 1748-03-03, location: traveling in Dunmar}
- {type: away, start: 1748-03-03, end: 1748-03-05, location: Karawa}
- {type: away, start: 1748-03-14, end: 9999, location: Dunmari Fort (Gomat)}
---
# Arcus
>[!info]+ Biographical Info
> A [[Chardonian Empire|Chardonian]] [[Humans|human]], he/him
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Discovered as a statue by the [[Dunmar Fellowship]] on March 25th, 1748 in the [[Dunmari Fort (Gomat)]], [[Nashtkar]], the [[Desolation of Cha'mutte]] %%^End%%

An adventurer and treasure hunter from the [[Society of the Open Scroll]], found petrified in the fort east of [[Gomat]]. 

Left [[Chardon]] with [[Servius]], [[Dee Wildcloak]], [[Dain Goldhammer]], and [[Alban]]. Argued constantly with [[Servius]], acording to [[Dee Wildcloak]]. Parted ways with other travelers in [[Songara]], presumably to press ahead. 

Passed through [[Karawa]] alone in late February or early March, according to [[Jasu]] and [[Ikram]].

```dataview
LIST WITHOUT ID events.text from #timeline flatten file.lists as events where contains(events.text, this.file.name) sort events.DR
```
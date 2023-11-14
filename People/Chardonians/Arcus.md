---
tags: [dufr/aware, person, dufr/minor]
displayDefaults: {startStatus: born, startPrefix: b., endPrefix: d., endStatus: died}
campaignInfo: []
name: Arcus
born: 1723
species: human
ancestry: Chardonian
gender: male
died: 1748
affiliations: [Society of the Open Scroll]
whereabouts:
- {type: home, start: !!null '', end: '', location: 'Chardon, Chardonian Empire'}
- {type: away, start: 1748-11-23, end: '', location: 'petrified in a fort east of Gomat, Nashtkar'}
---
# Arcus
>[!info]+ Biographical Summary
>[[Humans|human]] (Chardonian), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Chardon]], [[Chardonian Empire]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An adventurer and treasure hunter from the [[Society of the Open Scroll]], found petrified in the fort east of [[Gomat]]. 

Left [[Chardon]] with [[Servius]], [[Dee Wildcloak]], [[Dain Goldhammer]], and [[Alban]]. Argued constantly with [[Servius]], acording to [[Dee Wildcloak]]. Parted ways with other travelers in [[Songara]], presumably to press ahead. 

Passed through [[Karawa]] alone in late February or early March, according to [[Jasu]] and [[Ikram]].

```dataview
LIST WITHOUT ID events.text from #timeline flatten file.lists as events where contains(events.text, this.file.name) sort events.DR
```
---
type: NPC
name: Arcus
pronouciation:
aliases: []
tags:
- NPC/DuFr/minor
- NPC/DuFr/aware
pageTargetDate:
endStatus: petrified
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1723
died: 1748
gender: male
pronouns:
ancestry: Chardonian
species: human
affiliations:
- Society of the Open Scroll
family:
whereabouts:
- type: home
  start: null
  end: ''
  location: Chardon, Chardonian Empire
- type: away
  start: 1748-11-23
  end: ''
  location: petrified in a fort east of Gomat, Nashtkar
lastSeenByParty: []
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
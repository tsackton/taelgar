---
type: NPC
name: Enari
pronouciation:
aliases: []
tags:
- NPC/DuFr/minor
- NPC/DuFr/met_one
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born:
died:
gender: male
pronouns:
ancestry:
species: lizardfolk
affiliations: []
family:
whereabouts:
- type: home
  start: 0001-01-02
  end: ''
  location: unknown, Orekatu
- type: away
  start: 1748-11-23
  end: ''
  location: Bedez, Orekatu
lastSeenByParty: []
---
# Enari
>[!info]+ Biographical Summary
>lizardfolk, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: unknown, [[Orekatu]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A well-muscled lizardfolk hunter and wanderer, who earned a reputation and honor traveling among the villages of the kingdom of [[Orekatu]]. Guided [[Kenzo]] and [[Izzarak]] to the [[Azta Lekua]], the [[Azta Lekua|Footprint of the Gods]], and returned to [[Bedez]] after they succeeded in their quest, to report to the elders of the kingdom. 

![[enari-portrait.png|400]]
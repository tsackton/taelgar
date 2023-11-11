---
type: NPC
name: Typhina
pronouciation:
aliases: []
tags:
- NPC/DuFr/background
- NPC/DuFr/aware
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born:
died:
gender: female
pronouns:
ancestry:
species: fey
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Amberglow, Feywild
lastSeenByParty: []
---
# Typhina
>[!info]+ Biographical Summary
>fey, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Amberglow]], [[Feywild]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`
### Typhina

A member of the court of the [[Cloudspinner]] and guardian of the Heartwood Grove. She was killed by [[Agata]], who later stole her identity while hiding in the [[Ring of the Warded Mind]].
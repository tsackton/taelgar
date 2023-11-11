---
type: NPC
name: Ila
pronouciation:
aliases: []
tags:
- NPC/historical
- NPC/DuFr/aware
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title: Commander
born:
died:
gender: male
pronouns:
ancestry: Dunmari
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: 0001-01-02
  end: ''
  location: unknown, Central Dunmar
lastSeenByParty: []
---
# Commander Ila
>[!info]+ Biographical Summary
>human (Dunmari), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: unknown, [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The commander of the eastern Dunmari army in Tokra during and after the [[Second Hobgoblin War]]. Involved in [[The Exile of Fraternity of the Empty Moon]]. 


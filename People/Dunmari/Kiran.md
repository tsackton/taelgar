---
type: NPC
name: Kiran
pronouciation:
aliases: []
tags:
- NPC/DuFr/background
- NPC/DuFr/met
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
ancestry: Dunmari
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: plains north of Tokra, Central Dunmar
lastSeenByParty: []
---
# Kiran
>[!info]+ Biographical Summary
>human (Dunmari), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: plains north of Tokra, [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A member of a family of goat herders that wander across the upper reaches of the Hara river, north of Tokra. 

In 1748, met [[The Dunmar Fellowship]], and his family was gifted a mechanical goat of a strange clockwork design by the dwarf [[Seeker]]. 
---
type: NPC
name: Kisa
pronouciation:
aliases: []
tags:
- NPC/DuFr/minor
- NPC/DuFr/met
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1680
died:
gender: female
pronouns:
ancestry: Dunmari
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: 1680-01-02
  end: ''
  location: Karawa, Eastern Dunmar
lastSeenByParty: []
---
# Kisa
>[!info]+ Biographical Summary
>human (Dunmari), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Karawa]], [[Eastern Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A short elderly woman with graying hair and a limp, Kisa, known affectionately as Elder Kisa, is a member of the village council and the unofficial leader of Karawa. She is a slow and deliberate speaker, always thinking first of the safety of the village and its people. 
%%SECRET[1]%%
---
type: NPC
name: Padma
species: human
ancestry: Dunmari
gender: female
born: 1720
died: 
affiliations: 
aliases: []
title:
tags: [NPC/DuFr/background, NPC/DuFr/met]
yearOverride: 
family:
whereabouts:
     - { date: 1720-01-02, place: "caravanserai, Tokra-Darba Road", region: Central Dunmar, type: home  }
---
# Padma
>[!info]+ Biographical Summary
>human (Dunmari), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: caravanserai, [[Tokra-Darba Road]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`


An innkeeper and master of a caravanserai waystation on the [[Tokra-Darba Road]], running one of the first waystations on the west side of the [[Copper Hills]].  Generally well positioned to receive and pass along news. 

In late July 1748, was briefly cut off from Tokra by wyverns who had made a nest in the ruined mining town of [[Vandar]]. Pleased to receive news that [[The Dunmar Fellowship]] had killed the wyverns and the road was clear on 26 July 1748. 

%%SECRET[1]%%
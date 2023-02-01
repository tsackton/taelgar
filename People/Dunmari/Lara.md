---
type: NPC
## bio ##
name: Lara
species: human
ancestry: Dunmari
gender: female
## age ##
born: 1707
died: 
## groups ##
affiliations: ["Lakan Mystai"]
family:
## other ##
yearOverride: 
title:
aliases: []
tags: [NPC/DuFr/minor, NPC/DuFr/met]
whereabouts:
     - { date: 1707-01-02, place: "Lakan Monastery, Tokra", region: Central Dunmar, type: home }
---
# Lara
>[!info]+ Biographical Summary
>human (Dunmari), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Lakan Monastery]], [[Tokra]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The leader of the [[Lakan Mystai]] in Tokra.

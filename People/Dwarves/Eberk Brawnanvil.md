---
type: NPC
name: Eberk Brawnanvil
species: dwarf
ancestry: 
gender: male
born: 1502
died: 
affiliations: ["Brawnanvils"]
title:
family:
aliases: []
tags: [NPC/DuFr/background, NPC/DuFr/met_one]
yearOverride: 
whereabouts:
     - { date: 1502-01-01, place: "Raven's Hold, Ardith", region: "Sentinel Range", type: origin }
     - { date: 1502-01-02, place: "Tharn Todor, Nardith", region: Yuvanti Mountains, type: home }
---
# Eberk Brawnanvil
>[!info]+ Biographical Summary
>dwarf, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Raven's Hold]], [[Ardith]], [[Sentinel Range]]
>> Based in: [[Tharn Todor]], [[Nardith]], [[Yuvanti Mountains]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An elder [[Dwarves|dwarf]], a respected member of the Brawnanvil clan and priest of the [[Bahrazel]]. He was born in the [[Sentinel Range]] before the [[Great War]], and grew up in the [[Dwarven Outpost (Raven's Hold)|dwarven outpost]] near [[Raven's Hold]], but fled south during the [[Great War]]. He now lives with many other Brawnanvils in [[Tharn Todor]]. 
%%^Campaign:DuFr%%
Eberk is [[Riswynn]]'s great uncle, who helped her develop her divine magic, and passed along a map of the [[Dwarven Outpost (Raven's Hold)|dwarven outpost near Raven's Hold]] to aid her in the quest to recover the [[Shield of the Brawnanvil Clan]]. 
%%^End%%
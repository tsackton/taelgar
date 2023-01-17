---
type: Ruler
name: Tester
species: human
ancestry:
gender: male
born: 1711
reignStart: 1717
died: 1718
endStatus: petrified
location: 
locationRegion:
home: Whitsun District, Chardon
homeRegion: Chardonian Empire
origin: Arendum, Chasa River Valley
originRegion: Chardonian Empire
affiliations: ["Great Library"]
aliases: []
tags: [NPC/testing]
yearOverride: 
reignEnd:
title:
family:
lastSeenByParty_clee: 1718-04-05
whereabouts:
     - { date: 1711-01-01, place: "Whitsun District, Chardon", region: Chardonian Empire}
     - { date: 1717-01-01, place: "XX, A", region: x}
---
# Tester
>[!info]+ Biographical Summary
>human, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_RegnalValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

sad asdlk
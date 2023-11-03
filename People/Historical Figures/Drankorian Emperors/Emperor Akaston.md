---
type: NPC
name: Akaston
title: Emperor
species: human
ancestry: Hkaran
gender: male
born: 
died: 911
affiliations: 
tags: [NPC/historical, NPC/DuFr/aware, NPC/DuFr/background]
family:
yearOverride: 
aliases:
whereabouts:
     - { date: 0001-01-01, place: "Drankor", region: Drankorian Empire, type: home}
---
# Emperor Akaston
>[!info]+ Biographical Summary
>human (Hkaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Drankor]], [[Drankorian Empire]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An Emperor of Drankor. Ruled during Hralgar's time. 
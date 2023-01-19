---
type: NPC
name: Pearl Brightmoon
species: halfling
ancestry: 
gender: female
born: 
died: 
affiliations: Sea
aliases: []
tags: [NPC/DuFr/met_one, NPC/DuFr/background]
yearOverride: 
title:
family:
whereabouts:
     - { date: 1748-11-23, place: "unknown", region: Eastern Green, excursion: true }
---
# Pearl Brightmoon
>[!info]+ Biographical Summary
>halfling, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

Halfing woman in her prime. Captain of the guard and first mate. Buff, good with a rapier. Cousin to [[Wella Brightmoon|Wella]] by blood and [[Rose Brightmoon|Rose]] by marriage. 
---
type: NPC
name: Enari
species: lizardfolk
ancestry: 
gender: male
born: 
died: 
affiliations: 
title:
family:
aliases: []
tags: [NPC/DuFr/minor, NPC/DuFr/met_one]
yearOverride: 
whereabouts:
     - { date: 0001-01-02, place: "unknown", region: Orekatu}
     - { date: 1748-11-23, place: "Bedez", region: Orekatu, excursion: true }
---
# Enari
>[!info]+ Biographical Summary
>lizardfolk, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A well-muscled lizardfolk hunter and wanderer, who earned a reputation and honor traveling among the villages of the kingdom of [[Orekatu]]. Guided [[Kenzo]] and [[Izzarak]] to the [[Azta Lekua]], the [[Azta Lekua|Footprint of the Gods]], and returned to [[Bedez]] after they succeeded in their quest, to report to the elders of the kingdom. 

![[enari.png|400]]
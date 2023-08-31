---
type: NPC
name: Eleuha
species: dryad
ancestry: 
gender: female
born: 
died: 
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/background, NPC/DuFr/met_one, status/uptodate]
yearOverride: 
whereabouts:
     - { date: 0001-01-02 , place: "Azta Lekua", region: Orekatu, type: home }
---
# Eleuha
>[!info]+ Biographical Summary
>dryad, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Azta Lekua]], [[Orekatu]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A dryad of the jungle, daughter of a great tree, friend to [[Lengau]]. 
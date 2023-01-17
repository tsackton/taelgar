---
type: NPC
name: Ames Benthey
species: human
ancestry: Sembaran
gender: male
born: 1675
died: 
affiliations: ["Lord's Guard (Cleenseau)"]
aliases: []
tags: [NPC/Clee/unsorted, NPC/DuFr/unaware]
title:
family:
whereabouts:
     - { date: 1675-01-01, place: "Cleenseau", region: Sembara}
     - { date: 1719-10-18, place: "somewhere upriver from Cleenseau", region: Sembara, excursion: true}
---
# Ames Benthey
>[!info]+ Biographical Summary
>human (Sembaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

The captain of the household guard of [[Essford Manor]], part of the [[Lord's Guard of Cleenseau|Lord's Guard]] in [[Cleenseau]]. 
---
type: NPC
name: Melusine
species: fey
ancestry: nymph
gender: female
born: 
died: 
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/met_one, NPC/DuFr/background, status/uptodate]
yearOverride: 
whereabouts:
     - { date: 0001-01-02, place: "Amberglow", region: Feywild, type: home }
---
# Melusine
>[!info]+ Biographical Summary
>fey (nymph), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Amberglow]], [[Feywild]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A water nymph in [[Amberglow]]. She resides in a small, secluded grotto near a river, overgrown with vines and foliage. 

%%SECRET[1]%%
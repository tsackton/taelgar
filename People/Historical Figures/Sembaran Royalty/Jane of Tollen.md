---
type: Ruler
species: human
born:
ancestry: Vostok
gender: female
died:
family:
title:
affiliations:
reignStart:
reignEnd:
name: Jane
tags: [NPC/Clee/unsorted, NPC/DuFr/unaware, NPC/historical]
whereabouts:
- {date: 0001-01-01, place: Tollen, region: Tollen}
- {date: 0001-01-02, place: Embry, region: Sembara}
---
# Jane
>[!info]+ Biographical Summary
>human (Vostok), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_RegnalValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

The second wife of [[Derik III]], from a powerful and rich merchant family in Tollen.

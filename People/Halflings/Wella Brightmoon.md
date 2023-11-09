---
type: NPC
name: Wella Brightmoon
species: halfling
ancestry: 
gender: female
born: 1639
died: 
affiliations: ["Brightmoons"]
aliases: [Wella]
title:
family:
tags: [NPC/DuFr/background, NPC/DuFr/met_one]
yearOverride: 
whereabouts:
     - { date: 1639-01-02, place: "unknown", region: Eastern Green Sea, type: home }
---
# Wella Brightmoon
>[!info]+ Biographical Summary
>halfling, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: unknown, [[Eastern Green Sea]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Wella is an elderly [[Halflings|halfling]] woman, and the captain of the [[Wave Dancer]]. She is married to [[Rose Brightmoon]], and is the matriarch of the Brightmoon clan. 
%%^Date:1748%%
Although now getting old and stiff and sometimes slow on her feet, she has been sailing all her life, and her weather sense is deeply respected by the crew of the [[Wave Dancer]]. 
%%^End%%
---
type: NPC
name: Valius
species: human
ancestry: Chardonian
gender: male
born: 1722
died:
family:
affiliations:
  - "Chardonian Legion"
  - "Society of the Open Scroll"
aliases: []
tags: 
  - NPC/DuFr/met
  - NPC/DuFr/major
lastSeenByParty: 
     - { date: 1748-12-09, prefix: DuFr }
whereabouts:
     - { date: 1722-01-01, place: "Chardon", region: "Chardonian Empire", type: origin}
     - { date: 1722-01-02, place: "Chardon", region: "Chardonian Empire", type: home}
     - { date: 1748-12-09, place: "Trapped in the Mirror of Soul Trapping", region: "", type: excursion}
---
# Valius
>[!info]+ Biographical Summary
>human (Chardonian), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Chardon]], [[Chardonian Empire]]
>> Based in: [[Chardon]], [[Chardonian Empire]]
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 9th, 1748: Trapped in the Mirror of Soul Trapping %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A former mercenary and adventurer, Valius now finds himself ensnared by the machinations of [[Fausto]] and trapped in the [[Mirror of Soul Trapping]]. Alongside his twin, [[Vargus]], he once sought treasures and wealth, but now seeks only to free his brother from [[Fausto]]'s curse.

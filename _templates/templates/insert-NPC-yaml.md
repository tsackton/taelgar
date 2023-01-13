---
<%* const configFilePath = app.vault.getRoot().path  + ".obsidian/taelgarConfig.json";
let configFile = await app.vault.adapter.read(configFilePath);
let parsed = JSON.parse(configFile);       
const campaignValue = parsed.campaignPrefix
%>type: NPC
name: <% tp.file.title %>
species: 
ancestry: 
gender: 
born: 
died: 
location: 
locationRegion:
home: 
homeRegion:
origin:
originRegion:
affiliations: 
aliases: []
lastSeenByParty_<%_ campaignValue _%>: 
whereabouts: 
- {dateAr: 0001-01-01, place: "", region: }

yearOverride: 
tags: [NPC/unsorted]
---
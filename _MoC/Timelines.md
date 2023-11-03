Timelines can be generated from tagged list items with dataview, or from a combination of tagged list items and tagged files with dataviewjs. 

Some examples:

## All events where text contains NPC

Won't currently find things that are linked via alias but don't mention NPC, but should be fixable using events.outlinks, this.file.alias, and other stuff
```dataview
LIST WITHOUT ID events.text from #event-source flatten file.lists as events where contains(events.text, this.file.name) sort events.DR
```

Javascript 
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", { yearStart: 1600, yearEnd: 1749, pageFilter: "#event-source or #timeline"} )
```
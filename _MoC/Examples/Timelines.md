Timelines can be generated from tagged list items with dataview, or from a combination of tagged list items and tagged files with dataviewjs. 

Some examples:

## All events where text contains NPC

Won't currently find things that are linked via alias but don't mention NPC, but should be fixable using events.outlinks, this.file.alias, and other stuff

```
```dataview
LIST WITHOUT ID events.text from #event-source flatten file.lists as events where contains(events.text, this.file.name) sort events.DR
```

Some other examples:

This will get all of the timeline events between 1 and 2000 that are linked from the Timeline of Sembaran History.
```
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", { yearStart: 1, yearEnd: 2000, pageFilter: "outgoing([[Timeline of Sembaran History]])"} )
```

This will get all of the timeline events with tag #`event-source` in the Campaigns folder


`````
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", { yearStart: 1, yearEnd: 2000, pageFilter: "#event-source and \"Campaigns\"} )

Note the \" around Campaigns, that is critical, Dataview requires folder names to be wrapped in quotes.
````

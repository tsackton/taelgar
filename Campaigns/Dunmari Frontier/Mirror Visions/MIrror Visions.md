```dataview
LIST WITHOUT ID events.text FROM "Campaigns" flatten file.lists as events where contains(events.recharge, "mirror") sort events.DR
```


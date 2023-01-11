---
name: Charmhearts
---
# The Charmhearts

The Charmhearts are a prominent family of [[halfling]] overland traders. They trace their history to the [[Greater Sembara]] region, but for the past several generations they have made their living on long distance trade, bringing spices, furs, and dyed cloth from [[Sembara]] to [[Dunmar]], as well as sometimes apple brandy from Adderfell. 

Their traditional route brings them across the lower elevation eastern passes across the [[~CentralMountains~]] on the road to [[Karawa]], often crossing as early as the middle of March, aiming to arrive in [[Karawa]] in time to trade at the [[Festival of Rebirth]], usually in early April. After a year circuiting [[Dunmar]], they return to [[Sembara]] via the high passes from [[Tokra]] in late spring when the snows melt. 

They are a serious trading family, and always travel prepared for danger, especially across the passes and the open frontier north of [[Karawa]]. 

```dataviewjs
let currentYear = window.FantasyCalendarAPI.getCalendars()[0].current.year 
let currentFolder = "\"" + dv.current().file.folder + "\"" 
for (let group of dv.pages(currentFolder).sort(f => f.eventEndDate)) { 
  if (group.name == dv.current().name && group.type == "NPC_Event") { 
    if (group.eventEndDate <= currentYear) { 
      var link = group.file.link
      link.embed = true
      link.display = "natural"
      dv.span(link) 
      } 
  }
}
```


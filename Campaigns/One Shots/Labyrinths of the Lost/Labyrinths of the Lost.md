---
tags: [meta]
hide: [toc]
---

The Labyrinths of the Lost was a short adventure set in [[Western Cymea]], telling the story of [[Labyrinth Prisoners|four prisoners]] who escaped an abandoned manor. 

Sessions:
```dataview
TABLE WITHOUT ID
  link(file.path, default(descTitle, file.name)) AS "Session",sessionNumber as Episode,
  realWorldDate AS "On Earth"
FROM #session-note AND !"_templates" AND !"_sessions"
WHERE campaign = "Labyrinths of the Lost"
SORT realWorldDate ASC
```


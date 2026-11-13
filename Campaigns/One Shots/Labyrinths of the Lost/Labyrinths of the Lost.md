---
lintedAt: "2026-11-12T19:02:10-05:00"
lintVersion: "3.5"
tags: [meta]
hide: [toc]
campaign: Labyrinths of the Lost
name: Labyrinths of the Lost
POV: 1748
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

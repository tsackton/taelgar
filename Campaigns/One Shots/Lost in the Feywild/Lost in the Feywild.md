---
headerVersion: 2023.11.25
tags: [meta]
hide: [toc]
dm_owner: tim
dm_notes: none
---
# Lost in the Feywild

Lost in the Feywild is a short adventure that begins near [[Tollen]], where the [[Tollen Misfits]] follow a strange guide to Dandelion House and into a bargain older than it first appears.

The player characters: [[Tollen Misfits]]

Sessions:
```dataview
TABLE WITHOUT ID
  link(file.path, default(descTitle, file.name)) AS "Session",sessionNumber as Episode,
  realWorldDate AS "On Earth"
FROM #session-note AND !"_templates" AND !"_sessions"
WHERE campaign = "Lost in the Feywild"
SORT realWorldDate ASC
```


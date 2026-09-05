---
headerVersion: 2023.11.25
lintedAt: "2026-09-05T16:06:33-04:00"
lintVersion: "3.5"
tags: [meta]
hide: [toc]
campaign: Into the Chasm
name: Into the Chasm
dm_owner: mike
dm_notes: none
POV: 1730
---
# Into the Chasm

Into the Chasm is a short adventure in and around the [[Great Chasm]], where five strangers are drawn into [[Zeyfa's Labyrinth]] by impossible omens and a supernatural storm.

The player characters: [[Chasm Explorers]]

Sessions:

```dataview
TABLE WITHOUT ID
  link(file.path, default(descTitle, file.name)) AS "Session", sessionNumber as Episode,
  realWorldDate AS "On Earth"
FROM #session-note AND !"_templates" AND !"_sessions"
WHERE campaign = "Into the Chasm"
SORT realWorldDate ASC
```

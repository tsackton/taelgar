---
lintedAt: "2026-10-19T10:39:23-04:00"
lintVersion: "3.5"
tags: [background, religion/mosnumena, status/check/lint]
typeOf: holiday
fc-date: {day: 7, month: 1}
name: Miracle of the Hopeful Heat
dm_owner: mike
dm_notes: none
POV: modern
---
```taelgar-header
```

This miracle is celebrated locally in [[Asineau]]. The details were lost during the hobgoblin wars, but remembered by the [[Stonebridges]] who shared the following story with the inhabitants of [[Asineau]] after it was resettled after the hobgoblin wars:

> Once, many many years ago, the winter was extraordinarily cold, and when Pyravella came, a blizzard struck. It snowed for seven days, and the wood started to run out, and the people were freezing. As the hearths went cold, the people gathered in the manor hall. As the blizzard continued into the second week, desperation set in, and the village grew worried, and cold. Some suggested striking out through the snow for Cleenseau (it was not called Cleenseau in those days, but there has always been a town by the bridge). But a young girl stood up and started preaching hope and as she spoke the wall behind her grew colors and streaks, and these radiated heat. The Wyrdling had granted a miracle of hope, and the heat of the colors kept the people alive through the next two nights, until the storm broke. This same wall is now part of the temple here.


![[asineau-wrydling-painting.jpg|eft|500]] 
  
The painting on the wall of the temple still feels warm, sometimes, if you bring your hand close to it on a cold day. 

Recently, on this very feast day, [[El]] protected a group of villagers from zombies who were sheltering in the temple.

%%^Metadata:names:v1%%
- {"name": "Miracle of the Hopeful Heat", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern remembrance of the miracle and the surviving warm temple painting; the final undated “Recently” sentence is a narrower January 1720 campaign-era layer.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and added minimal name and temporal metadata.
- Corrected the obvious spelling error “heaths” to “hearths” in the story.

### Validated judgments
- The attributed miracle story and surviving warm painting provide a sufficient local-festival reference. The repeated “many many” is deliberate storytelling emphasis, not an accidental duplicated word.
- The annual January 7 date agrees with [[Mos Numena Feast Days]] and the preserved play-by-email account “Celyn Learns the Miracles of Asineau.”

### Open findings

- [ ] **Warning — temporal.unanchored_relative_time:** The final sentence begins “Recently, on this very feast day” and makes “who were sheltering in the temple” appear to modify the zombies. The preserved play-by-email account [[_sessions/cleenseau/cleenseau-016.2/sources/Celyn Learns the Miracles of Asineau - Authored Turns]] places the attack on the January 7 anniversary; [[Cleenseau - Session 11.1]] records El recalling their protection of the temple on January 11, 1720. Keep the broad festival viewpoint and consider replacing only the final sentence with the dated passage below. The new date block is proposal-only because it changes filtered visibility.

  ```markdown
  %%^Date:1720-01-07%%
  On January 7, 1720, during the feast day, [[El]] protected villagers sheltering in the temple from zombies.
  %%^End%%
  ```
%%^End%%

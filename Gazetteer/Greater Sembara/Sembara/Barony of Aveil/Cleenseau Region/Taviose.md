---
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, testcase, status/check/lint]
typeOf: settlement
typeOfAlias: village
population: 30
name: Taviose
pronunciation: Ta-vi-ose
whereabouts: Manor of Cleenseau
dm_owner: mike
dm_notes: color
POV: 1720
---
```taelgar-header
```

A small hamlet in the [[Cleenseau Region]] on the edge of the [[Cleenseau Wood]], a mile and a half north of [[Cleenseau]] along a dirt track. The small hamlet is mostly woodcutters, charcoal makers, and pig farmers and is part of the manor of the Lord of Cleenseau. It consists of about ten buildings, only one of which is notable: a large, two-story stone building with three large oak trees carved on the lintel, the home of [[Perrin Voclain]].  It is said this was once holy to a *[[Kestavo]]* of the wood, who has long since departed.

There is a small shrine to the Wildling attached to Perrin's house, with several ancient oak trees, which mostly serves as a burial plot for the hamlet. Perrin tends to this shrine. There is no regular market here. Taviose imports grain, tools, and wool from Cleenseau and sells pigs, tree nuts, apples, and plums.


%%^Date:1720%%
In the late fall of 1719, Taviose was the site of [[Cleenseau Spider Attacks|several]] [[Cleenseau Spider Attacks|spider attacks]] from giant spiders that came from the [[Cleenseau Wood]]. [[Perrin Voclain]] and the [[Heroes of Cleenseau]] were instrumental in saving the hamlet, which was abandoned for about a week in late 1719. Despite this, the town lost about a third of its population.

The ongoing corruption from these spiders later caused several orchards and timber groves to become corrupted and die, until healed by [[Robin of Abenfyrd|Robin]].
%%^End%%
### Notable Residents
* [[Perrin Voclain]], an acolyte of the Wildling and druid
* [[Brot Starsearcher]], an eccentric dwarf, and their wife [[Diesla Starsearcher]]
* [[Abigail Moss]] and her two uncles, pig and chestnut farmers, the sole survivors amongst the Moss family from the spider attacks
* [[Hugh Darrow]] and his father [[Remy Darrow]], charcoal makers
* [[Phillipa Northwood]], a woodcutter in the large Northwood family, the poorest of the inhabitants
* [[Odo Cordwaner]], recently appointed guardsman for the hamlet

%%^Campaign:None%%
### People in, or based in Taviose
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Alive", "Age"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, true, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file),  util.isAlive(b), util.s("<age> (<startdate>)", b.file)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Taviose", "language": "unknown", "pronunciation": "Ta-vi-ose", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early DR 1720 village portrait with the late-1719 attacks and their aftermath in a dated block; the resident list precedes the established spring-1720 moves to Asineau.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving parsed values.
- Added persistent primary name metadata, preserving existing accepted pronunciations and leaving newly composed pronunciations proposed.
- Recorded the supported article viewpoint and concise temporal-coverage metadata.
- Added the required typed settlement map block with its unsupported position left blank.
- Applied the declared objective spelling, punctuation, or grammar corrections; no lore was rewritten.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block has a blank `locator` because no supported world-map hex is established in the reviewed evidence. Supply the village's verified position in `- {map: world, locator: <verified hex>}`; the placeholder is a human task, not a coordinate proposal.

- [ ] **Warning — coverage.later_material_change:** The undated Notable Residents list still places [[Brot Starsearcher]], [[Diesla Starsearcher]], [[Odo Cordwaner]], and [[Abigail Moss]] in Taviose. [[Cleenseau - Session 29]] and [[Asineau Hirelings - Authored Turns]] establish that all four moved to [[Asineau]] in spring DR 1720, with Odo and Abigail arriving in late April. Candidate consequence: `In spring DR 1720, Brot and Diesla Starsearcher moved their workshop to [[Asineau]], and Odo Cordwaner and Abigail Moss also settled there.` Recast those roster entries as former residents if updating the article, defer with the appropriate game-update disposition, or intentionally preserve the earlier roster and POV. For filtered historical views, propose paired before/after Date blocks only after choosing a supported cutoff; the sources do not date all four moves to one exact day.

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The existing block before “People in, or based in Taviose” opens with `%%^Campaign:None%%`; the current validator and [[Campaign Registry]] specify lowercase `Campaign:none`. Proposed replacement opener: `%%^Campaign:none%%`, retaining the existing payload and matching closing marker. Equivalent filtered visibility has not been verified, so this normalization remains proposal-only; confirm visibility and approve the change before applying it.
%%^End%%

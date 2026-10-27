---
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
tags: [group, status/check/lint]
typeOf: mystery cult
ancestry: Dunmari
name: Order of the Awakened Soul
affiliations:
  - {type: primary, org: Bhishma}
dm_owner: tim
dm_notes: important
POV: modern
---
```taelgar-header
```

The mystery cult dedicated to the Dunmari god [[Bhishma]]. Dedicated to collecting the stories of the Dunmari, preserving the memories of the people of Dunmar, and making sure the souls of the dead are not forgotten and lost.

%%^Campaign:dufr%%
After the [[Great War]], the Order was one of the few who remained as much as they could in the [[Nashtkar]], as most Dunmari fled west. They made it their mission to find the many souls lost and wandering, unable to reach the [[Land of the Dead]], and help them find peace.

In the early 1700s, explorers and travelers from the Order reached as far as Drankor, and discovered [[Rai]], who spoke of the evil spreading from the wounds [[Cha'mutte]] left in the world. 

In DR 1718, the Order and Rai traveled together to [[Isingue]], and attempted to cleanse the land of the [[Seeds of Chaos]] left by [[Cha'mutte]]'s death, but [[Awakened Soul Disaster|failed]]. The few members of the Order that survived fled west, and scattered across [[Eastern Dunmar]] and [[Central Dunmar]], doing what they still could to tend the stories of the people. 

> [!warning]- Kenzo's conversation with Pava 
> 
> ### [[Kenzo]] and [[Pava]], [[Session 20 (DuFr)]]
> 
> [[Kenzo]] spoke with [[Pava]] to ask him what he knew of the Order of the Awakened Soul. During this conversation, he learned the following:
> 
> - The Order of the Awakened Soul was the pre-[[Great War]] name of the Mystai of [[Bhishma]]. When the order was founded in the years after [[Bhishma]] passed on from the mortal world and took up residence in the land of the gods, their mission was to tend to the soul of [[Dunmar]], and especially to see that the stories of the people of [[Dunmar]] were remembered, as [[Bhishma]] saw the people of the land as the heart and soul of the country. 
> - Since the [[Great War]], that name has fallen out of use, as the Mystai turned their focus to the dead, and from “awakening the soul of the country” to putting lost spirits to peaceful sleep.
> - The order is now all but dead, and few remember the time before the events 30 years ago during which many of the strongest of the Mystai died in an attempt at something, some ritual to cleanse the land. [[Pava]] and [[Avaras]] were still wanderers then, not yet promoted to masters.
> - The only master that [[Pava]] can think of who may still remember the times before is [[Saka]], an old woman who was a master before the attempted ritual but chose not to participate. He has not seen her in five years or more, but she always said that when she got too old to travel she was going to settle in the lands north and west of [[Tokra]], among the horse herders on the plains. So perhaps she is still there.
> - The Mystai of [[Bhishma]] are now few and far between. They do gather every few years for the Feast of [[Bhishma]], but [[Pava]] and [[Avaras]] did not attend the last gathering and don’t expect to make long journeys from their home anymore.

%%^End%%


%%SECRET[v2:4e5d0871895b4b3b332865f5ce1a038d]%%


%%^Campaign:none%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {name: Order of the Awakened Soul, language: unknown, status: documented, notes: "In the Session 20 conversation, Pava describes this as the pre-Great-War name of Bhishma's mystai and says it fell out of use after the Great War."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern account of the order's mission and history, with a separately attributed DR 1748 conversation; the fate and return of the lost monks established in DR 1749 are not yet incorporated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting and added the explicit subject name.
- Added a minimal documented name entry, with unknown name-language provenance and the existing account of the name's historical use; the plain-English title needs no pronunciation.
- Added `POV: modern` and temporal notes distinguishing the historical account and attributed DR 1748 conversation from later developments.
- Corrected one repeated space and two spelling errors.
- Normalized the existing `SECRETS` comment label to `SECRET` and `Campaign:None` to `Campaign:none`, preserving their content and verified Git/public visibility.

### Validated judgments
- Confirmed local source matches support the existing positive `dm_notes` attestation; its value is unchanged.
- The local-only SECRET block and the shared private member-query block were reviewed independently and retained in their existing privacy categories.
- The DR 1718 disaster date agrees with [[Awakened Soul Disaster]]. Pava's account remains attributed to its DR 1748 conversation rather than being treated as omniscient knowledge of later events.

### Editorial assessment
**Underdeveloped**: the account lacks the established fate of the monks lost in the disaster and their DR 1749 rescue and return. A short later-history paragraph is sufficient; it need not invent a renewed hierarchy, membership total, or institutional recovery.

### Open findings

- [ ] **Warning — coverage.later_material_change:** The disaster paragraph ends with a few survivors fleeing west, and the account closes with Pava's DR 1748 belief that the order is all but dead. [[dunmari-frontier-135-session-recap]] (recaps 005–006) and [[dunmari-frontier-136-session-recap]] (recaps 001 and 010) establish that monks survived with Rai in Limbo and were brought back; [[dunmar-frontier-139-session-recap]] (recap 002) records their later delivery to Karawa. This is a defining change in the order's fate. Decide whether to incorporate it into the existing `Campaign:dufr` history and update the temporal interpretation, defer it with the appropriate `status/gameupdate/dufr` tag, or intentionally preserve the earlier account. Copy-ready addition: `Some of the monks lost in the [[Awakened Soul Disaster]] survived in [[Limbo]], sustained by [[Rai]]. In DR 1749, the [[Dunmar Fellowship]] restored fading monks through stories and shared routines and brought the survivors back to the [[Material Plane]] after the wound at [[Isingue]] was closed. The rescued monks were later taken to [[Karawa]].` Preserve Pava's dated testimony as what he knew then; do not infer that all participants survived or that the order has already recovered its former strength. The return to Karawa should remain dated only to DR 1749 because the farewell's exact date is provisional.

### DM evidence
- [[_DM_/Dunmar Epilogues]]
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Campaign 3/Dunmar Epliogue - Campaign 3 Timing]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan History]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Awakened Soul Monks]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 20]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 21]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 24]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Individual Scenes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 18]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/The Situation in the South]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Travel to Raven's Hold/Journey North]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part III Saving the Te'kula/Te'kula - DM Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/History of Blasted Plains]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Major Players]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Arcs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Faction Action]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Kenzo (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Seeker (OneNote)]]
- [[_DM_/_Dunmari Frontier/Final Arc Planning - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Desolation of Cha'mutte Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 63 - DM notes]]
%%^End%%

---
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/text, status/check/lint]
typeOf: realm
typeOfAlias: secretive magocracy
campaignInfo: []
name: Ursk
aliases: [Urskan]
whereabouts: Northern Green Sea
dm_owner: tim
dm_notes: important
POV: modern
---
```taelgar-header
```

Ursk is a secretive civilization on the north coast of the [[Green Sea]]. Rumors are that it is a land of wizards and magic, of ice and snow, of monsters and secret treasure. While outsiders are allowed to trade at a handful of port cities, including [[Zakat]] and [[Praznitsky]], the warehouses and docks of these cities are kept isolated from the city proper, and foreigners are not allowed to pass the borders. Trade with Ursk, however, is worth the hassle, for the valuable hides, furs, and other monster parts, especially the most prized of all, dragonhide from the northern wastes.

Ursk itself lies largely on the lowland coastal plains, south of the highlands and plateaus that extend all the way west to northern Vostok and the Sembara Highlands. The winters are long and cold, and the westerly winds off the [[Green Sea]] bring snow from October to May. But the short summers are pleasant and the long days of June and July make some agriculture possible. Much like the central plateaus of Vostok, this is a land of many small, cold rivers, and with the maritime influence wetlands are common, especially along the coast. To the north, the vast taiga of the northern wastes extends as far as one can travel, until it is replaced by tundra in the higher elevations and the far north.

The people of Ursk speak their own tongue. Common is rarely spoken, although the trade tongue of the far east, Eastros, is more common. None speak Sembaran or any tongue of the western isles. 
## Rumors

The northern coasts between Skaegenland and Ursk are inhospitable, with few or no safe harbors, generally sheer cliffs and rocky coasts, and no ports. Who or what lives there is anyone's guess, and no one has ventured into the interior and returned. But many rumors fly:
- The Last Kingdom of the Giants
- Fierce snow elves
- Shapeshifters and changelings
- A hidden kingdom of wizards who fled the destruction of Drankor
- A kingdom of wild folk led by a queen who can turn into a massive winter wolf at will
- The kingdom of giant eagles
- A dense cold forest of talking trees who attack and kill any wooden ship that attempts to anchor
- The secret kingdom of a vampire who snacks on unwary sailors

%%^Campaign:None%%
### Places in Ursk
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%

%%SECRET[v2:ef64908ff0e18230c3cd94ae640280f8]%%

%% NOTES, FROM GOOGLE DRIVE

On the northern shores of the [[Green Sea]], stretching a few hundred miles along the coast and extending inland, lies a civilization ruled by wizards. A closed culture, foreigners are restricted to a few offshore islands on the outskirts of coastal trading cities, where they trade for prized furs and hides, especially dragonhide, of the northern wastes.
### Climate

Ursk  lies largely on the lowland coastal plains, south of the highlands and plateaus that extend all the way west to northern Vostok and the highlands of  [[Zimkova]]. The winters are long and cold, and the westerly winds off the [[Green Sea]] bring snow from October to May. But the short summers are pleasant and the long days of June and July make some agriculture possible. 

The land rises gradually to the north, and the northern edge of Ursk  is defined by the rough, rugged mountains of the [[Yengorza Mountains]]. Much like the central plateaus of Vostok, this is a land of many small, cold rivers, and with the maritime influence wetlands are common, especially along the coast. To the north, the vast taiga of the northern wastes extends are far as one can travel, until it is replaced by tundra in the higher elevations and the far north.

(the basic idea is roughly the northern parts of Atlantic Canada, perhaps with a bit more snow; or maybe the southern/coastal parts of Siberia - long winters, cold but modulated by the ocean, a fair bit of snow, warm short summers, and mostly forest/boreal swamp ecosystems)
### Geography

Ursk is dominated by its coastal cities. The vast majority of the population lives within 50 miles of the coast, and the only major population centers are here, including the four “trade cities” with ports at which foreigners are allowed to dock. Among the most prominent of these is [[Praznitsky]], in the western part of the country. The interior of Ursk is sparsely populated, and contains no large cities and few towns.
### Culture and Politics

#### The Krev rites and the Rodnya

The people of the Ursk are intimately connected with magic, through the krev and the rodnye system. 

The krev is a ritual that is required of everyone when they reach adulthood, which binds each citizen of Ursk together as a wellspring of magical energy. Undergoing this ritual enhances innate magical ability, and innate arcane ability in particular – there are many more wizards, and especially sorcerers, in Ursk than one would expect based on its size. The magical wellspring of the populace of Ursk, bound together, also allows the mages and wizards of the country, when connected to this energy, to enhance their magic, a crucial factor in the defense of the country against the dangers of the wild north. But the krev is not without cost. Those bound to it occasionally lose chunks of time, a few hours usually, that they cannot later recall. 

Ruling over the krev system and Ursk are the eight rodnye (bloodlines, loosely; singular rodnya), each one a loose confederacy headed by a powerful mage. Each rodnya is individualistic, not familial, and membership is not by inheritance. Instead, it is by nomination/invitation. While the focus of the rodnye is often on magical training and knowledge, and all magic users are eventually expected to join a rodnya, other prominent people (and sometimes random people of no particular prominence, perhaps when a rodnya has a magical intuition or foretelling about someone) can be invited to join as well. 

Joining a rodnya involves three rituals. First, one takes the zakava (pledge), marking one as a member of a rodnya, but not compelling further advancement, and at this stage some people can (and do) shift alliances. Some members are eventually invited to take the laj (oath), which marks you as a significant person in the ranks of your rodnya, and finally the zvia (binding), which magically binds you to compel loyalty to your rodnya. An invitation to advance in in your rodyna is the same as a command - it isn't like if you are invited to the zakava ritual you can say no. 

For those who truly do not wish to join, the rodnye are merciful  -- exile is an option, as long as you are willing to suffer the rasaka first. The details of the ceremony are mysterious - for none who undergo it are allowed to remain in Ursk. But it is known that is severs the part of you bound by the krev, leaving it behind in Ursk while you depart. For magic users, this destroys their ability to cast spells; for others, rumors claim it makes you sick, although to what extent, and how quickly ones recovers, is never clear. 

(What if the metaphysics is that it isn't just a seal but a redirection of some sort? So the rasaka actually allows the rodnye to continue to draw whatever magical power they previously would have from the person. Perhaps it is actually draws more power, in some way, at the expense of the victim's health (mitigated, if they have spellcasting ability, for that is what 'fills up' the bond) -- but for those without magic ability, the ritual is still used before exile, and it leaves the exiled lethargic, weak, tired, sickly, etc. Some people take the bargain (and perhaps, to some extent, it isn't always clear exactly what the bargain is). But the cost is real.)

Through these rituals – the krev system, the rodnya rites, and the rasaka – the rodnye maintain a monopoly on magical use in Ursk. And there are rumors that the heads of the rodnye bind themselves to each other with even more powerful rituals than the zvia. Although there is always disagreement and jockeying amongst the lower ranks, the leadership of each rodnya appear to always reach consensus with each other without conflict. 
#### The People of Ursk

Most people in the Ursk have been here for many generations, dating back hundreds of years before the Great War. The rodnya trace their origin to the great coastal cities of Ursk today, many of which have an ancient history. Outsiders are neither welcomed nor usually tolerated, and immigration and emigration are mostly unheard of. This is largely because of the krev. Those who are bound to it are not allowed to  leave without suffering the rasaka, and the krev ritual fails if attempted after a certain age, so only those who immigrate as children can be fully incorporated into the Ursk 

However, during the disruptions and upheavals of the Great War, in the course of wars against the terrors of the northern wastes, Ursk conquered the inland region, incorporating the people living there into the krev and society. 

These people, called the novja (loosely, new people), still have not, for the most part, fully integrated into society, and they often live in a separate ghetto or on the 'wrong side of town'. Prominence and advancement is rare, and as they have been connected to the krev for only a few generations, magic use seems particularly uncommon amongst them. Thus, few of the novja pledge rodnye, and none advance to the laj or zvia. This leaves them somewhat marginal, and there are occasional debates within the Ursk, even now, as to whether they should be truly citizens or if perhaps they should be formally segregated. The novja are often accused (sometimes correctly) of being not fully committed to the krev and the rodnya, and are sometimes suspected of avoiding their obligations to the krev, hiding their children from the rite. This leads to mistrust, especially when the dangers of the north increase in salience. 

### Recent Events

Over the past decade, the question of the novja has divided the eight rodnya. One of the rodnye, the [[Rodnya Kinzal]], is particularly known for their dislike of the novja. Another, [[Rodnya Voknaz]], is known for their pragmatism and is particularly concerned with Various Dangers Up North, rather than squabbling over who is or isn't a citizen. Voknaz has been the most open to novja, especially those who show strength of arms.

The winter of 1748 was a particularly dark and dangerous one. A dragon of ice and snow arose far in the north, stronger and more dangerous than many such beasts, and the early forays against this creature failed to stop it. The winter stretched long into spring, unnaturally so, and armies of walking ice were spotted moving south. A novja, Artem Novolozek, ended up as the leader of an elite squad sent to kill this creature. Success would likely have been a major coup for the factions that want to more closely integrate the novja... but he fails. He flees south ahead of disaster, the only survivor of the battle, and the dragon is only defeated by several of the very powerful mages - heads of the rodnye - band together. In the wake of this disaster, questions are raised: Why was Artem, who has not been through the zvia, even sent? Is anyone even sure he participated in the krev as a child? 

In the fallout of this near-disaster, Artem vanishes.

Notes from GDrive, might not be accurate:
- East of Skaegenland
    
- Land of long, hard winters, short summers, Russian in climate, but slightly modulated by Green Sea
    
- Possible mageocracy with ancient roots, maybe associated with dragons or giants
    
- Possible closed cities - trade missions outside, no outsiders in, but also considering same for western islands west of Chardon
    
- Remnants of old ‘east northlander’ people, relatively uninfluenced by Drankor
    
- Different language, religion? (or maybe Eight Divines still?) If different religion, use the “old gods” of highlands? 
    


%%

%%^Metadata:names:v1%%
- {name: Ursk, language: unknown, pronunciation: OORSK, status: proposed, notes: "Proposal informed by the Urskan cultural context and the Russian analogue in [[Languages]]: u is read as oo in food, r may be lightly rolled, and the final sk cluster is retained, producing one syllable. The name's language and exact in-world pronunciation are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography and trade, with attributed regional rumors; the visible overview does not yet incorporate the political developments of spring DR 1749.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting while preserving parsed values and `headerVersion`.
- Added persistent primary-name metadata with a proposed pronunciation, and recorded the broadly modern viewpoint and its limits.
- Corrected the visible typo “extends are far” to “extends as far.”

### Validated judgments
- `typeOf: realm` fits the subject; realm map metadata and `knownTo` are optional here.
- `status/cleanup/text` remains supported by the retained draft material and duplicate climate prose; the status is preserved.
- Confirmed local-source matches support the existing positive `dm_notes: important` attestation. The SECRET block was reviewed independently and preserved; its contents are excluded from this report.
- Current climate working notes retain substantial cold winters and a productive short summer without assigning a coastwide ice calendar; no new marine-ice claim is inferred here.

### Editorial assessment
**Underdeveloped** — The visible article offers geography and trade but lacks the established eight-rodnya government, magical guard, and relationship with the Vargaldi/novja. It also omits the documented spring DR 1749 political and western-border changes. Add a short sourced institutions/people section and choose a dated treatment of the later changes; no general origin story or religion needs to be invented for this bounded repair.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — metadata.names_unresolved_status:** Confirm or revise the persistent proposal `OORSK`, one syllable, with `oo` as in “food,” an optionally lightly rolled `r`, and the final `sk` cluster retained. The strongest available basis is the Urskan cultural context and the Russian analogue supplied by [[Languages]]; neither the name's source language nor an exact in-world pronunciation is established. If accepted, add `pronunciation: OORSK` to frontmatter and mark the primary name entry `documented`, or replace the proposal with the intended reading.

- [ ] **Warning — coverage.established_fact_missing:** The opening presents wizard rule only as rumor and the visible article does not identify its central institutions or constituent peoples. [[Rodnya]] establishes the eight ruling magical bloodlines, their invitation-based membership and collective defense; [[Eyes of Vedmakov]] identifies the magical guard; [[Vargaldi]] establishes settlement in Ursk and acceptance of the krev for protection. Copy-ready bounded addition: “Ursk is ruled by eight secretive magical bloodlines, the [[Rodnya|rodnye]], whose leaders cooperate to govern and defend the country. Membership is by invitation. The [[Eyes of Vedmakov]], also called the Watchers or Okolov, serve as Ursk's secret magical guard. Many [[Vargaldi]] have settled in Ursk, accepting the limitations of the krev rite in exchange for safety; others trade monster parts at [[Zvervinka]].” For the historical term, [[Philosopher's Information Concerning Rodnya Voknaz|the Forgotten Chronicler]] reports that Ursk expanded after the Great War and calls the incorporated Vargaldi the novja, or “new people.” Keep that history attributed if added; do not promote the detailed ritual drafts as established canon.

- [ ] **Warning — coverage.later_material_change:** [[Session 95 (DuFr)]] records Voknaz's diminished standing after the preceding winter's dragon attacks and Kinzal's negotiations with the western vampire lord; [[Session 97 (DuFr)]] records the vampire's death and Shadowkeep's collapse. These affect a ruling bloodline and Ursk's western neighbor, beyond an incidental party visit. Candidate dated addition: “In spring DR 1749, [[Rodnya Voknaz]] had lost standing after disastrous dragon attacks, while [[Rodnya Kinzal]] sought peace with [[Rhodar von Glauer]], the vampire lord west of Ursk. On May 3, the [[Dunmar Fellowship]] killed Rhodar and [[Shadowkeep]] collapsed.” The sources do not establish the eventual leadership or wider political settlement. Choose to incorporate this dated account with suitable visibility and temporal framing, defer the update with the appropriate human-selected game-update status, or intentionally preserve the earlier account and its viewpoint. Do not infer that every regional danger or political dispute ended.

- [ ] **Warning — correctness.cross_note_conflict:** The unqualified Rumors introduction says “no one has ventured into the interior and returned,” but [[Vargaldi]] describes inhabitants and guides of the northern forests, while [[Session 94 (DuFr)]], [[Session 95 (DuFr)]] and [[Session 97 (DuFr)]] record travel through the interior and return. Preserve the rumor list and its uncertainty, but decide whether the introduction is an explicitly earlier outsider view or a modern summary. Copy-ready modern replacement for that absolute sentence: “Outsider accounts of the interior are sparse, and many stories circulate about its inhabitants.” This bounds the perspective without declaring the listed rumors true or inventing outcomes for them.

- [ ] **Suggestion — editorial.shared_material_redundant:** In the shared `NOTES, FROM GOOGLE DRIVE` comment, the `Climate` paragraphs beginning “Ursk lies largely…” and “The land rises gradually…” repeat most of the visible coastal-plains, winter, rivers and taiga account. Propose a bounded split: remove the repeated climate sentences while retaining distinct northern-boundary and analogue guidance. Copy-ready retained boundary sentence: “The land rises gradually to the north, and the northern edge of Ursk is defined by the rough, rugged mountains of the [[Yengorza Mountains]].” Keep the existing real-world climate-analogue paragraph as editorial guidance, and retain a concise unresolved pointer to the hidden Zimkova-highlands wording versus the visible Sembara Highlands wording until a human reconciles that distinction. Preserve the other unique draft material and its uncertainties; this is a cleanup proposal, not permission to adopt the whole comment.

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated Places in Ursk block begins `%%^Campaign:None%%`; [[Campaign Registry]] reserves the lowercase sentinel. Candidate: change only that opening marker to `%%^Campaign:none%%`, preserving the dataview code and closing marker exactly, after confirming the same private export behavior. No visibility-sensitive conversion was applied during this review.

### DM evidence
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Pieces of Rai]]
- [[_DM_/_Dunmari Frontier/Final Arc Planning - DM Notes]]
- [[_DM_/_Dunmari Frontier/Leveling]]
- [[_DM_/_Dunmari Frontier/NPCs/Bernie Tidewater]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Adventure Part 0]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 112 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Brainstorming - Scepter Arc]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Prep Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 82 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/North Coast Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Northern Green Sea - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 83 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 85 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 92 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 93 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 94 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 95 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 96 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 97 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Session 98 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Session 99 - DM Notes]]
- [[_DM_/_Dunmari Frontier/assets/north-green-sea-coast.excalidraw]]
%%^End%%

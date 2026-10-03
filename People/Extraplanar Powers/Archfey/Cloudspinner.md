---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [power, status/gameupdate/dufr, status/check/lint]
typeOf: archfey
gender: female
name: Cloudspinner
aliases: [Queen of Sunset]
whereabouts:
  - {type: home, end: 1001, location: Amberglow}
  - {type: home, start: 1749-06-15, location: Amberglow}
  - {type: away, start: 1002, location: imprisoned}
  - {type: away, start: 1749-05-21, end: 1749-05-31, location: Vindristjarna}
  - {type: away, start: 1749-06-01, end: 1749-06-14, location: Portable Hole}
dm_owner: tim
dm_notes: important
POV: modern
---
# Cloudspinner
>[!info]+ Information  
> An archfey (she/her)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% fix whereabouts, campaign info; update page with lore about cloak of rainbows and people of the rainbow and conflict with Cha'mutte  %%

The Queen of Sunset was once the ruler of [[Amberglow]], known for spinning beautiful, magical thread from the clouds and sky. But long ago she vanished, and her realm has fallen into decay since that day.  

%%^Campaign:DuFr%%

Her memories opened [[Session 67 (DuFr)]]:

*As a group of travelers gathers here, some reunited after a long separation, others newly met, the Cloudspinner feels their presence even from her prison, far away, and she drifts in thought.*

*She remembers the days of plenty in [[Amberglow]], when she ruled as the Queen of Sunsets, when the glorious colors of the evening sun turned the sky and the grass and the water and the rocks to ever-changing paintings, when she spun threads of magic and color from the colors of the sky, when her court dazzled any who came with their beauty and elegance.*

*She remembers the fateful day she was tricked, bound and captive, her tools stolen, her life constrained, [[Amberglow]] slowly falling into ruin. She remembers how she could feel the footsteps of decay, a constant reminder of her fate as the color ran out of [[Amberglow]], her magnificent cloud palace fell into disarray, her court and servants fled, or lost, save the few who hung on, in desperation or fear or confusion, slowly turning as pale and colorless as the land itself.*

*She remembers the darkness that crept over her realm then, the cursed ones, the [[Story about Hags|hags]] and tricksters and malicious spirits of the Unseelie Court, who came after she was gone, who conquered and claimed [[Amberglow]] as their own, who filled the realm with darkness and despair. She remembers how they hunted down her remaining subjects, and how they desecrated the places that once held such beauty and light.*

*But she also remembers the resistance, the brave Fey and other creatures who fought back against the invaders, who formed secret alliances and underground networks, who kept the spark of hope alive in [[Amberglow]], even in its darkest days. [[Typhina]], the protector of the [[Heartwood Grove]]; <>, the Lady of the Lake, who drained the river of time; Bellator, the changeling king who sacrificed himself to hide the ruins of the Cloud Palace from those who would mean harm.*

*So she watches, and she waits, and she hopes, for the day when she will be free, and when [[Amberglow]] will once again be a realm of beauty and wonder. Until then, she will continue to fight, and to dream, and to hold onto the memory of what once was, and what could be again.*

*And our story fades from the Cloudspinner, and turns now to the travelers at [[Lastlight Falls]], who may yet have a small role to play in the story of [[Amberglow]].*

%%^End%%

%%^Metadata:names:v1%%
- {name: Cloudspinner, language: unknown}
- {name: Queen of Sunset, role: alias, language: unknown}
- {name: Queen of Sunsets, role: alias, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern before Cloudspinner's restoration in DR 1749, with a recollection explicitly set in DR 1748. The later whereabouts entries extend beyond the article's captivity-era account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and spacing without changing existing values.
- Added name metadata for the documented primary name and both recorded sunset titles; omitted pronunciation for these transparent English forms and left their in-world language unknown.
- Added a broadly modern POV and temporal coverage statement for the captivity-era article.
- Closed the missing italic delimiters in all seven paragraphs of the Session 67 recollection; its wording is unchanged.

### Validated judgments
- The recollection is explicitly presented as session narration; its lyrical voice is appropriate to that source role.
- Local evidence confirms support for the existing positive `dm_notes` attestation; the field is unchanged.
- `status/gameupdate/dufr`: not assessable pending the human choice to update, defer, or preserve the earlier article; retained unchanged.
- The shared comment is an editorial reminder, not an adopted account or a public-material candidate.

### Editorial assessment
**Underdeveloped**: the reference account omits Cloudspinner's defining protection of the People of the Rainbow and creation of the Cloak of Rainbows, the established account of her betrayal and imprisonment, and her restoration in DR 1749. These are established central gaps, not a request to invent an origin story or expand every campaign appearance. A short historical account and a bounded restoration update are sufficient.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The opening describes only her former rule and spinning, while [[People of the Rainbow]], [[Cloak of Rainbows]], and [[Tale of the Cloak of Rainbows]] establish her defining patronage and artifact. [[Session 120 (DuFr)]] also identifies the betrayal behind the disappearance that the recollection describes only as being tricked. Add a short account: "Cloudspinner sheltered the [[People of the Rainbow]] in [[Amberglow]], beyond [[Thark]]'s reach. She wove the [[Cloak of Rainbows]] from sunset threads and gave it to them so they could return to the material plane under its protection. [[Tale of the Cloak of Rainbows|Their tradition]] remembers the gift as thanks for Ilios the Bright's sacrifice in defending Amberglow." Within the existing Dunmar campaign section, add the separately established account: "[[Count Vashan]], once a trusted member of her court, betrayed her by bringing [[Cha'mutte]] to the [[Cloud Palace]] while she was vulnerable; he could no longer recall whether his betrayal was deliberate. She was subsequently held in a crystal prison on the [[Circular Island]]." Sources: [[Session 120 (DuFr)]] and [[Session 110 (DuFr)]]. Preserve the uncertainty about Vashan's intent and the campaign restriction.

- [ ] **Warning — coverage.later_material_change:** [[Session 123 (DuFr)]] records Cloudspinner's release at the [[Prismwell]] on DR 1749-06-13 and her return to power in Amberglow. This materially changes the article's captive/former-ruler account even though the recollection remains valid as a DR 1748 source. Choose to update the article and its temporal metadata, defer with the existing game-update tag, or intentionally retain the earlier snapshot. For an update, the smallest useful addition within the existing campaign section, in a proposed Date:1749-06-13 block, is: "On DR 1749-06-13, the [[Dunmar Fellowship]] freed Cloudspinner from her crystal prison at the [[Prismwell]]. Restored to power in [[Amberglow]], she drove back the shadows threatening the sanctuary and remained to face the damage to her realm." Make the opening retrospective about her absence rather than leaving it to imply that she is still missing, and keep the Session 67 recollection explicitly historical. Any new date block and game-update-tag disposition require human approval.

- [ ] **Warning — metadata.whereabouts_conflict:** The current entries keep Cloudspinner in the Portable Hole through DR 1749-06-14 and begin her renewed Amberglow home on DR 1749-06-15. [[Session 123 (DuFr)]] instead places her release at the Prismwell on DR 1749-06-13, with the party leaving her in Amberglow on June 14. Reconcile those entries with the session chronology; a day-granularity candidate is `{type: home, start: 1749-06-13, location: Amberglow}` and `{type: away, start: 1749-06-01, end: 1749-06-13, location: Portable Hole}`. The same-day transition can be recorded in prose if needed. Preserve the earlier location history until separately checked; no date values were changed automatically.

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The existing campaign opener uses `DuFr`. [[Campaign Registry]] requires the lowercase canonical code `dufr`; replace the opener with `%%^Campaign:dufr%%` while keeping the same content and campaign restriction.

- [ ] **Suggestion — editorial.prose_clarity:** The recollection contains the visible empty-name placeholder `<>, the Lady of the Lake`. It interrupts the list of defenders without supplying an identity. Either supply a supported name or retain the established title alone; the bounded replacement is `the Lady of the Lake, who drained the river of time`. Do not invent a personal name.

### DM evidence
- [[_DM_/Timelines/Cloak of Rainbows Timeline]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Feywild (Session 61)/Session 61/Session 61]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Meeting Place]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Seeker Solo Arc/Session 2 - Seeker]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Final Arc Planning - DM Notes]]
- [[_DM_/_Dunmari Frontier/Leveling]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Raw Notes - Agata Feywild]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Raw Notes - Seeker Solo]]
- [[_DM_/_Dunmari Frontier/Session 0.75 Planning Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Adventure Part 0]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Adventure Part 2]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Adventure Part 3]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Circular Island Overview - DM notes v2]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Cloudspinner's Prison]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Dragonet Info]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Ruins Secrets and Clues]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/NOTES/Friday Morning]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/NOTES/Thursday Night]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/OLD/Circular Island Overview - DM notes v1]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/OLD/Circular Island Rewritten]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/OLD/Sessions Overview]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/OLD/adventure_overview]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Outline v2]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 111 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Amberglow - Combat Ideas]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Brainstorming - Cloudspinner]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 118 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 119 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 119 - In Game Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 120 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 123 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/chatGPT - Cloudspinner Arc]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/The Story of Apollyon and Cha'mutte]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 83 - DM Notes]]
%%^End%%

---
tags: [meta]
hide: [toc]
---

The Dunmari Frontier Campaign tells the story of the adventures of [[Delwath]], [[Kenzo]], [[Seeker]], and [[Wellby]], along with their frequent companion [[Riswynn]], sometimes known as the [[Dunmar Fellowship]]. 

The events begin in the 191st year of the Nayan Dynasty in Dunmar, or DR 1748 as the Chardonians reckon, in the village of [[Karawa]] in [[Eastern Dunmar]]. Since their humble beginnings fighting gnolls, the [[Dunmar Fellowship]] has grown to a powerful force. 

You might start with:
- The index of session notes: [[Sessions]]
- A timeline of campaign events: [[Dunmari Frontier Timeline]]
- A list of treasure gained: [[Party Treasure]]
- The index of visions seen in the [[Mirror of the Past]]: [[Mirror Visions]]
- Information about [[Vindristjarna]], its [[Vindristjarna Mechanics|control mechanics]] and its [[Vindristjarna Bastion Rules|special facilities]].
- Information about [[Dunmar Fellowship Associates|companions, followers, and hirelings]]. 

The most recent session with published notes is [[Session 124 (DuFr)]]. For background, notes linked from that session are below:

```dataview
TABLE WITHOUT ID Link, join(split(meta(Link).path,"/",1),"/") as Folder
FROM "Campaigns/Dunmari Frontier Campaign/Session Notes/Session 124 (DuFr)"
FLATTEN file.outlinks as Link
GROUP BY Link
WHERE !contains(join(split(meta(Link).path,"/",2),"/"), "assets")
WHERE !contains(join(split(meta(Link).path,"/",2),"/"), "PCs")
WHERE !contains(join(split(meta(Link).path,"/",2),"/"), "Campaigns")
WHERE !contains(join(split(meta(Link).path,"/",2),"/"), "Worldbuilding")
WHERE !contains(join(split(meta(Link).path,"/",2),"/"), "_DM_")
SORT Folder
```

%%^Campaign:none%%

Dunmar Campaign cleanup / to do list

- [ ] Clean up main PC pages
- [ ] Clean up guest pages
- [ ] Clean up companion pages
- [ ] Clean up follower pages and figure out how to organize (probably should be via the Dunmar Fellowship page, not this page)
- [ ] Clean up Vindristjarna details and figure out how to organize (bastion rules, other mechanics, and in-world history as three separate notes is main idea)

%%^End%%
---
tags: [meta]
hide:
 - toc
---

This is the main page for the Dunmari Frontier campaign, covering the adventures of [[Delwath]], [[Kenzo]], [[Seeker]], and [[Wellby]], along with their frequent companion [[Riswynn]], sometimes known as the [[Dunmar Fellowship]]. 

The events begin in the 191st year of the Nayan Dynasty in Dunmar, or DR 1748 as the Chardonians reckon, in the village of [[Karawa]] in [[Eastern Dunmar]]. Since their humble beginnings fighting gnolls, the [[Dunmar Fellowship]] has grown to a powerful force. 

You might start with:
- The index of session notes: [[Sessions]]
- A timeline of campaign events: [[Dunmari Frontier Timeline]]
- A list of treasure gained: [[Party Treasure]]
- The index of visions seen in the [[Mirror of the Past]]: [[Mirror Visions]]

You can also explore the skyship [[Vindristjarna]] and the [[Vindristjarna Room Planning|special facilities]] constructed on it.

You can also explore the [[Session 107 (DuFr)|most]] [[Session 108 (DuFr)|recent]] [[Session 109 (DuFr)|several]] [[Session 110 (DuFr)|sessions]], or browse pages mentioned in the sessions in the current adventure (the quest for the last jade):

```dataview
TABLE WITHOUT ID Link, join(split(meta(Link).path,"/",2),"/") as Folder
FROM "Campaigns/Dunmari Frontier/Session Notes/Session 107 (DuFr)" OR "Campaigns/Dunmari Frontier/Session Notes/Session 108 (DuFr)" OR "Campaigns/Dunmari Frontier/Session Notes/Session 109 (DuFr)" OR "Campaigns/Dunmari Frontier/Session Notes/Session 110 (DuFr)"
FLATTEN file.outlinks as Link
GROUP BY Link
WHERE !contains(join(split(meta(Link).path,"/",2),"/"), "assets")
WHERE !contains(join(split(meta(Link).path,"/",2),"/"), "PCs")
WHERE !contains(join(split(meta(Link).path,"/",2),"/"), "Campaigns")
SORT Folder
```



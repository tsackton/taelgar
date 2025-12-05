---
headerVersion: 2023.11.25
tags: [background, status/incomplete]
dm_owner: none
dm_notes: none
---
# Divine Realms

%% status/incomplete -> could, as some point, use some brief descriptions of other Firstborn realms, once sufficient details are invented to be worth summarizing here.%%

Theological cosmologists, dating back to the influential Drankorian work [[On the Classification of Divinity]], have distinguished between [[Embodied Gods]], powerful celestial beings with an embodied physical manifestation, and [[Incorporeal Gods]], spiritual essences spun out of the divine power of creation itself. Current theological understanding, as represented in the [[Standard Multiversal Model]], suggests that these distinctions are critical for probing the nature of the divine realms. 

The [[Embodied Gods]], as even a cursory knowledge of the theology of any of the [[Elder Folk]] reveals, must have some extraplanar locus of their power, independent from the [[Divine Presence]]. All have heard the stories of [[Dwarves|dwarves]] traveling to the divine locus of the [[Bahrazel]], which they call the [[Heart of the Mountain]]; or the tales of the strange powers of ancestral memory the [[Halflings|halflings]] possess from being able to access the divine locus of the [[First Ones]]. These extraplanar places, the homes of the [[Embodied Gods]], are referred to as the Divine Realms in the [[Standard Multiversal Model]]. 

The nature of the [[Incorporeal Gods]], however, has long been a puzzle and matter of contention about theologians and philosophers. The current theological consensus, at least among scholars of the [[Mos Numena|Eight Divines]], suggests that [[Incorporeal Gods]] are best though of as manifestations of the [[Divine Presence]] itself, with memory and an independent mind and power, but located within the nexus of the [[Plane of Creation]] itself. Indeed, the famous first stanza of the ancient [[Mos Numena|Mos Numenan]] lyrical poem, "[[Blossom of the Eightfold Light]]," hints at the connected nature of the Divine Realm with the Plane of Creation:

*Not sundered, nor a realm apart, but rising,*  
*Rooted in light, yet swayed by unseen currents,*  
*A bloom upon Creation’s heart unfolding,*  
*Ever in flower.*

Whether theologians of the most prominent other human religion, the [[Five Siblings]] of the [[Dunmar|Dunmari]], agree, is unknown, as the [[Dunmari Mystery Cults|Dunmari Mystai]] do not share their secret knowledge with outsides. 

%%^Campaign:none%%

This note generally presumes that incorporeal gods, being incorporeal, do not have true "home realms". However, this may be incorrect. It is possible that the realms of the gods are simply inaccessible to anyone but the dead souls of believers, and basically function like some kind of mythological heaven. 

In practice, this explanation seems valuable as it solves several problems in Taelgarian religion. In particular, it simplifies the question of "what happens to the souls of creatures that don't worship gods with defined home realms (e.g., tanshi)", among other things. It also doesn't really seem interesting or necessary to have the "divine realm of Mos Numena" or whatever available as an adventure location. 

At the moment, there are really only two prominent human religions (Mos Numena and Five Siblings), with the various northern folk religions and the Skaer religion distinctly minor in comparison, and conveniently if the Dunmari have some alternate metaphysical truth it is likely locked behind the secret knowledge of the mystery cults. Upon the invention of additional religions - in the east, or wherever - it might be worth updating this note. 

A fair bit of discussion:
- [[Discord Chat - Divine Power in Taelgar]]
- [[Discord Chat - Homes of Incorporeal Gods]]
- [[Discord Chat - Multiverse]]

## List of Divine Realms

```dataviewjs
const { util } = customJS
dv.table(["Place"], 
			dv.pages("#place")
				.where(f => util.inLocation("Divine Realms", f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name:x>", b.file)]))
```

%%^End%%
---
headerVersion: 2023.11.25
tags: [place]
name: Wistel–Enst Watershed
typeOf: watershed
whereabouts:
- { type: home, location: Greater Sembara, linkText: in }
dm_owner: none
dm_notes: none
---
# The Wistel–Enst Watershed
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Wistel–Enst watershed drains much of southern and central [[Sembara]], carrying upland waters from the [[Sentinel Range|Sentinels]] and the [[Mostreve Hills]] to the [[Western Gulf]]. It consists of three closely linked systems:

- Wistel system: The [[Wistel]] rises in the foothills of the Sentinels and flows east to the marshlands of [[Ozabal|Ozabal Swamp]] on the coast. A major tributary is the [[Bollin]] from the north (joining near [[Ainwick]]). The Wistel meets and mingles with the lower [[Enst]] through the Ozabal wetlands before the combined waters reach the sea.

- Enst system: The [[Enst]] is a cold, rocky river forming much of Sembara’s southern frontier. Above [[Cleenseau]] it splits into the “Three Fingers”: [[Enst (North Fork)]], [[Enst (Middle Fork)]], and [[Enst (South Fork)]], which rejoin near [[Lysandale]]. Key Enst tributaries include the [[Auberonne]] (forming [[Lake Rin]] at its confluence and fed by the [[Leandre]] and the [[Cranmere|Cranmère]]) and the [[Clavert]] flowing north off [[Westcliff]].

- Aure system: The [[Aure]] rises in the [[Darkwood]] and runs north through [[Addermarch]] to join the Enst near the Ozabal lowlands. North of [[Adderfell]] it gathers the [[Velan]] from the west—which itself receives the [[Umber]] near [[Valcroix]]—and the short upland [[Branth]] from the east. [[Adderfell]] sits at the height of navigation on the Aure, on a small lake. 

## Character and Use 
The [[Wistel]] supports heavy barge and river traffic on its lower reaches, particularly along the stretch between [[Ainwick]] and [[Wisford]].  There are several bridges, including major ones at [[Ainwick]], [[Gowerbourne]], and [[Wisford]] as well as some smaller ones between [[Gowerbourne]] and [[Wisford]].

The [[Enst]], by contrast, is difficult to cross and forms a major barrier to movement: flooding, cold currents, and limited towpaths restrict navigation. Ferries (most notably at [[Rinburg]]) and a small number of bridges—most notably at [[Cleenseau]] and [[Eskbridge]]—manage crossings where the banks allow.

The Aure supports regular riverboat traffic between [[Adderfell]] and the [[Enst]].


%%^Campaign:None%%
### Places in the Wistel–Enst Watershed
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.typeOf == "river" || f.typeOf == "waterway" || f.typeOf == "lake"))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```
%%^End%%

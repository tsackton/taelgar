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
The [[Wistel]] supports heavy barge and river traffic on its lower reaches, primarily along the stretch between [[Ainwick]] and [[Wisford]].  There are several bridges, including major ones at [[Ainwick]], [[Gowerbourne]], and [[Wisford]] as well as some smaller ones between [[Gowerbourne]] and [[Wisford]].

The [[Enst]], by contrast, is difficult to cross and forms a major barrier to movement: flooding, cold currents, and limited towpaths restrict navigation. Ferries (most notably at [[Rinburg]]) and a small number of bridges—most notably at [[Cleenseau]] and [[Eskbridge]]—manage crossings where the banks allow.

The Aure supports regular riverboat traffic between [[Adderfell]] and the [[Enst]].

Once the Enst and the Wistel join, the river becomes a marshy delta with many meandering paths as it moves through [[Ozabal|Ozabal Swamp]], and it is not generally navigated further east of Wisford (on the Wistel) and Eskbridge (on the Enst).


%%^Campaign:None%%

## Rivers in the Wistel-Enst watershed

[[Wistel]]
source (Sentinels): 12.10.A02
end (ocean): 12.11.G..10

[[Bollin]]
source (Sentinels): 11.10.A.14
end (Wistel): 12.10.G.12

[[Cambril]]
source (Sentinels): 11.10.C.18
end (Bollin): 11.10.F.22

[[Wethlin]]
source (Sentinels): 11.10.D.02
end (Bollin): 11.10.B.21

[[Vardell]]
source (Sentinels): 11.10.B.16
end (Bollin): 11.10.E.03

Unnamed River 1
source (Aine Hills): 12.10.D.13
end (Cambril): 11.10.F.08

Unnamed River 2:
source (Aine Hills): 11.10.I.15
end (Wistel): 12.10.G.22 

[[Rindle]] **unmapped but might be one of the unnamed rivers**

[[Brunebeck]] **unmapped**

[[Lanting]] **unmapped but might be one of the unnamed rivers**

---

[[Enst]]
source: 13.10.D.09
end (Wistel): 12.11.G.03

[[Enst (Middle Fork)]]
source (Sentinels): 13.10.A.01
end (Enst): 13.10.D.09

[[Enst (South Fork)]]
source (Sentinels): 13.10.A.16
end (Enst): 13.10.D.09

[[Enst (North Fork)]]
source (Sentinels): 12.10.C.07
end (Enst): 13.10.D.13

[[Cranmere|Cranmère]] **unmapped**

[[Amance Brook]] **unmapped**

[[Leandre]]
source (Aveil Ridge): 12.10.H.07
end (Aurberonne): 12.10.H.19

[[Auberonne]]
source (Aveil Ridge): 12.10.H.14
end (Lake Rin): 12.10.I.21

[[Clavert]]
source (Westcliff): 12.11.C.15
end (Enst): 12.11.E.07

---

[[Aure]]
source (Darkwood): 13.11.D.08
end (Enst):12.11.E.18

[[Branth]]
source (Mostreve): 13.11.G.10
end (Aure): 12.11.F.12

Unnamed River 1
source (Mostreve): 13.11.G.07
end (Branth): 13.11.G.06

Unnamed River 2
source (Mostreve): 13.11.D.15
end (Branth): 13.11.D.14

[[Velan]]
source (Mostreve): 13.11.A.17
end (Aure): 12.11.F.16

[[Umber]]
source (Mostreve): 12.11.C.23
end (Velan): 12.11.F.03

[[Mill Brook (Roscombe)]] **unmapped**

Unnamed River 3
source (Mostreve): 12.11.F.10
end (Velan): 12.11.F.11

---

Mapped lakes in the Wistel-Enst watershed:

[[Lake Rin]]: 12.10.I.21

Unnamed Adderfell Lake **unmapped**

## Places in the Wistel–Enst Watershed
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.typeOf == "river" || f.typeOf == "waterway" || f.typeOf == "lake"))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%

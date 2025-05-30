---
headerVersion: 2023.11.25
tags: [organization]
name: Shakun Mystai
displayDefaults: {partOf: "", boxInfo: "<ancestry:UA> <typeof:UA> of <deity:UA>"}
name: Shakun Mystai
typeOf: mystery cult
deity: Shakun
ancestry: Dunmari
dm_notes: important
dm_owner: tim
---
# The Shakun Mystai
>[!info]+ Information  
> A [[Dunmar|Dunmari]] mystery cult of [[Shakun]]  
> `$=dv.view("_scripts/view/get_Affiliations")`

One of the [[Dunmari Mystery Cults]], mystical organizations devoted to the [[Five Siblings|Dunmari gods]]. The [[Shakun]] Mystai, devoted to the goddess [[Shakun]], are based in the [[Temple of Shakun]] in the small village of [[Karawa]] in [[Eastern Dunmar]]. The temple in [[Karawa]] supports a community of somewhat over 100 initiates, along with a few dozen initiates-in-training and 40 or more lay associates of the mystai. The mystai are known for creating healing powders from the stone of the [[Red Mesa]], and for somehow misleading and waylaying those who attempt to cross the eastern borders of [[Dunmar]] with evil intent. 
%%^Campaign:DuFr%%
The Shakun Mystai are primarily responsible for maintaining, in secret, the webs of protection and illusion that defend the eastern borders of [[Dunmar]], known as Shakun's Protection, as well as tending the living rock of the [[Red Mesa]], which is the embodied form of Shakun in the material plane. The magic of Shakun's Protection comes from the [[Red Mesa]], which is associated with the body of [[Shakun]] herself, and especially the sacred relic [[Heart of Shakun]]. When [[Heart of Shakun]] is in its proper place in the [[Temple of Shakun]] in secret chambers below the [[Red Mesa]], it provides a powerful source of divine magic, which is then channeled by the connected network of the mystai themselves to create Shakun's Protection. It is said that those who are not initiated into the mysteries cannot understand the full nature of this magic, and those who are cannot speak of it, willingly or unwillingly. But it is understood that, somehow, Shakun's Protection serves as a web of illusions that mask safe passages, making the desert appear as dead-end canyons, endless sands, and paths that twist and turn back to where they came from, for anyone with evil intent towards [[Dunmar]]. Those who persist, it is said, find themselves lost forever in Shakun's [[Shakun's Realm|divine realm]].  
%%^End%%
%%^Date:1748%%
In April 1748, the Shakun mystai, along with the rest of [[Karawa]] and [[Eastern Dunmar]], were attacked by rampaging gnolls during the [[Summer Gnoll Raids of 1748]]. More than a dozen mystai died in the attacks, and still, in November 1748, the mystai are diminished in strength and number. During this time, [[Dunmar Fellowship]] experienced the an abbreviated [[Session 26 (DuFr)#The Initiation Ritual of the Shakun Mystai|initiation rite of the Shakun Mystai]], while later, after the return of [[Heart of Shakun]], [[Kenzo]] and [[Drikod]] experienced the [[The Shakun Mystai Initiation|full initiation rite]]
%%^End%%

%%^Campaign:None%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
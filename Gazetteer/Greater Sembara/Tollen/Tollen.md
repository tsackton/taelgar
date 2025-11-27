---
headerVersion: 2023.11.25
tags: [place, status/needswork/old]
name: Free City of Tollen
typeOf: city
whereabouts: Western Green Sea
aliases: [Free City of Tollen, Tollen]
dm_owner: tim
dm_notes: important
---
# The Free City of Tollen
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Tollen is a bustling port on the [[Volta]], a growing naval power, a cultural mixing ground, an a entrepôt where goods from across the [[Green Sea]] are traded. Founded thousands of years ago, it has navigated the politics of the region and maintained its independent for centuries. It is a haven for merchants, traders, intellectuals, mages, poets, writers, and scholars, known for the [[University of Tollen]] and its powerful guilds. Tollen is a cosmopolitan city, where [[humans]], [[halflings]], [[dwarves]], [[stoneborn]], [[lizardfolk]], [[Kenku|kenku]], [[Elves|elves]], and more can be found living together, and where temples to many gods can be found, most prominently the [[Mos Numena|Eight Divines]] and the Skaer ocean goddess [[Kaikkea]]. 

## Geography and Hydrology
_See more: [[Hydrology of Tollen]]_

Tollen sits astride the [[Volta]] river, though most development is on the north side, which is generally rockier, less marshy, and generally less prone to flooding. Five tributaries of the Volta flow through the city and its environs, from west to east: the [[Little River]], the [[Muddy River]] (the only tributary that joins the Volta on the south bank), [[Fat Brook]], the [[Carnbrook]], and the [[Greywash]]. The area around the confluence of the Volta, Little, and Muddy rivers is swampy and prone to flooding; the area around the confluence of the Greywash and the Volta, east of the city proper, is even more so. The difficult terrain around the Greywash has long discouraged eastern expansion of the city. 

%% the marshes around the Greywash are a plausible place for a lizardfolk community if desired - this never really came up when the Dunmar campaign was in Tollen but might be nice to add for various reasons, though perhaps this is -- unusually -- a relatively new lizardfolk settlement (say, post Great War, or maybe just post plague), instead of a remnant of the ancient swamps %% 

## City Layout

%% design doc from OneNote here: [[Tollen - Design Note]] %%

Tollen sprawls astride the Volta, although most settlement is on the north bank. The oldest parts of the city are the eastern wards, which tend to have small, cramped streets and are home to the docks and the shipbuilding industry. The central part of the city, especially around the [[Tollen Bridge]], and extending west, is a major commercial hub, with markets, guildhalls, and broad boulevards. The western part of the city, clustered around the Little and Muddy rivers, is home to tanners, leatherworkers, dye-makers, and other industry; most of the recent expansion has been in this direction, including many sprawling slums outside the walls. 

### Wards of Tollen
_See more: [[Wards of Tollen]]_

Tollen is divided into 17 wards, mostly on the north bank of the [[Volta]] and largely contained within the city walls, though as the population has grown in recent years the city has swelled beyond its walls, particularly to the west. 

The oldest parts of the city -- the wards of [[Fiskurth]], [[Aesganstrad]], and [[Skepwalk]] -- are clustered along the banks of the Volta in the eastern (ocean-ward) part of [[Tollen]], reflecting the city's heritage as a Skaer port long ago. 

[[Magus Street]], where the [[University of Tollen]] is located; [[Bridgeward]], on the north side of the [[Tollen Bridge]]; and [[Nordgate]], now home to a substantial dwarven population, surround this inner core. The rich commercial districts of [[Gold Street]] and [[Guildgate]]; [[Godshome]], with many temples; [[Fairgate]], with many markets; [[Southbridge]], on the south bank of the Volta across from [[Bridgeward]]; [[Haurhill]], on the height of land above the [[Little River]] and the site of an ancient Drankorian fort; and [[Battery]], home to extensive naval fortifications, make up the rest of the city as it stood at the time of the [[Great War]]. 

More recently, as Tollen's prominence has grown, the marshy land on the south bank west of [[Southbridge]] has been drained and settled, forming the new wards of [[Fenslane]] and [[Tideswell]]; and the walls have been expanded to the west, enclosing the new wards of [[Brooklawn]] and [[Riversgate]]. 

### Bridges, Walls, and Gates

Only one bridge spans the [[Volta]]: the [[Tollen Bridge]], originally constructed by the [[Drankorian Empire]]. This broad stone span of many arches is a major commercial hub, lined with shops, houses, and activity, and also a defensive structure, with gatehouses at either end. Tall-masted oceanic ships cannot pass under the bridge. 

While the [[Walls of Tollen|walls of Tollen]] have expanded many times during its history, their are eight gates in the current walls, from east to west: Old Gate, Scholar's Gate, North Gate, Temple Gate, Guild Gate, Fair Gate, Tanner's Gate, and River Gate. 

### Landmarks

Tollen has many notable landmarks. The most famous is the [[Tollen Bridge]], a vast span across the wide [[Volta]] that dates to the days of the [[Drankorian Empire]], now lined with shops. There are also many temples, particularly the Temple of [[The Wanderer]], with its massive spire, the Temple of the [[The Sibyl|Sibyl]], with its colorful dome, and the Skaer [[Temple of Kaikkea]], one of the oldest buildings in Tollen. 

The guildhalls of Tollen are also notable, with several richer guilds constructing substantial palaces in the [[Gold Street]] and [[Guildgate]] districts, which are noted for their impressive architecture. 

%% 
Other landmarks could include a theater, government palace, major clock tower, other temples, and some weirder stuff like a strange dark tower associated with a lost god 
%%

%%^Campaign:None%%
### Places in Tollen
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter))
				.sort(s => util.s("<name:!>", s. file))
				.sort(s => util.s("<maintype>", s.file))
				.map(b => [util.s("<name:t>", b.file), util.s("<maintype>", b.file)]))
				
```

%%^End%%



--- 

# Old

## Governance and Laws

Tollen is, by long custom, an open city. No toll is levied merely for stepping through its gates; the great arches are unbarred from first bell until dusk, and strangers come and go as they please. The city grows rich not by taxing feet, but by taxing cargo: every barrel and bale, every wagon and barge, pays its due at the customs houses. Licenses to sell in the markets, to practice a craft, or to bear the seal of a guild bring in more coin still.

On paper, foreigners are forbidden to go “armed in the Tollish peace.” The city laws bar strangers from wearing armor or carrying war-blades larger than a dagger within the walls. In practice, the gate-guards turn a blind eye to single swords and the odd mail shirt, so long as no one marches in file or clanks about in full harness. The rule is enforced when it must be—against gangs, bravos, and rioters—but rarely against quiet travelers, and almost never against the Elder races, whom Tollenders do not truly fear.

Tollen is a republic, for certain values of the word. Power rests in the hands of the guilds, whose masters send men and women to the Great Council. From their number a smaller Inner Council is chosen to rule from day to day, and every few years the guilds elect a First Councillor to speak for the city abroad. In law, all citizens are equal before the council; in truth, gold, ships, and old names weigh heavily on the scales.

---


Tollen is an open city: there are no tolls to enter, and the gates are kept open from dawn until dusk. There are fees, tolls, and tariffs on goods crossing through Tollen, market sellers, and considerable income is made via licensure of guilds and other professions and crafts. But from an adventurer's perspective, there is little to stop someone from wandering in. 

Formally speaking, "foreigners", are prohibited from carrying blades larger than a dagger, and prohibited armor, but in practice this is rarely or never enforced as long as the rule is not flaunted, and especially it is unlikely to be enforced against members of the Elder races, who are perceived to be no threat to the city. The city gates are guarded, but not tightly.

The city is technically a republic, with government by a council elected from the various guilds.

## History
_See more: [[History of Tollen]]_

Tollenders are deeply proud of their long history, and many will claim that Tollen is the oldest continually occupied [[Humans|human]] city in the world. Whether true or not is hard to know, but regardless Tollen's history stretches deep into the past.
### Founding

Tollen was originally founded on the north bank of the [[Volta]] river by the first mariner migrants from [[Hkar]], before [[The Downfall]], in the year 3902 by the Dwarven reckoning. Although the western edge of the [[Green Sea]], and the [[Western Gulf]], is originally something of a frontier backwater, over the next 100 years Tollen becomes a center of commerce and trade, a place where the mariner culture, the northern culture of [[Highlands]], and the non-[[Humans]] ([[Lizardfolk]] and [[Halflings]], mostly) of the [[Western Green Sea]] mingle. Even in this early age, Tollen was a religiously open and cosmopolitan place, and the worship of [[Kaikkea]], the ocean goddess of the early mariners and now the Skaer people, coexisted with the developing Kestavan tradition.

### Downfall and Rebirth

In 4050s, [[The Downfall]] Wars begin, and Tollen is cut off from the [[Eastern Green Sea]], as long voyages become too dangerous. The ocean itself turns violent, as storms wrack the seas and the great swamps to the south start to dry. By 4122, when [[The Downfall]] Wars have ended, Tollen is virtually abandoned, and the land that will become [[Sembara]] depopulated, settled by scattered villages of farmers, with [[Embry]] and a few other river towns among the only significant population settlements.

By the 4200s, the Skaer have established themselves as the dominant mariner culture in the [[Western Green Sea]], and resettle and rebuild Tollen. Over the next 300 years, the Skaer grow stronger, spreading along the coast as far south as the mouth of the [[Semb]], raiding upriver for timber and impressed sailors to row their great ships, and seeking converts for their religion. Tollen develops as a major trade center for the emerging Skaer empire, and begins to grow again.

### Drankorian Influence

In 4491, the Drankorians reach the [[Mostreve Hills]], and over the next 50 years or so the Drankorians assimilate the inland people of [[Sembara]] and push the Skaer out, bringing with them the [[Mos Numena]] and the traditions of their vast southern empire. 

In 4535, the Drankorians and the Skaer sign a peace treaty, the [[Treaty of Marhavn]], establishing the [[Volta]] as the frontier of the [[Drankorian Empire]]. Tollen, on the north side of the [[Volta]], remains technically outside the Drankorian territorial claim. However, the Skaer are forbidden from bringing ships up the [[Volta]], and Tollen falls outside their sway and comes under the influence of [[Drankorian Empire|Drankor]]. While technically Tollen takes the name of the Free City of Tollen during this time, the [[Drankorian Empire]] controls its foreign policy as a protectorate.

By the 4600s, during the Long Peace, Tollen begins to assert more autonomy. By now it has become a mixing place of Drankorian, Skaer, and Highlander culture, with diverse religious practices and where many languages can be heard. During this era the first merchant houses are established, becoming rich off the trade of dyed cloth south to [[Drankorian Empire|Drankor]], and the development of magical tattoos, especially those that could help sailors control the wind and sea.

In the 4800s, as Drankorian expansion to the west begins in earnest and the might of the empire is focused to the east, the Tollen merchant houses have de facto control over Tollen, and Tollen has become a major city and one of the central mercantile powers of the [[Western Green Sea]]. It is during this era that the [[University of Tollen]] is founded.

### The Fall of [[Drankorian Empire|Drankor]] and the Growth of [[Sembara]]

When the Plague strikes, while Tollen is spared the worst of the chaos that envelopes the south, but plenty of chaos remains, and various wars and conflicts spiral out of control. While the university survives, and the city itself, most of its wealth is lost as trade is disrupted, and Tollen falls into a dark age. Little is recorded from the time between the Plague in 5192, and the late 5300s, when the Sembaran kings begin to grow in power.

As [[Sembara]] expands in the south, Tollen recovers, and over the 5400s and 5500s Tollen experiences a renaissance of sorts, based on the growing wool and linen trade from the Sembaran heartlands. The lost art of magical tattoos are rediscovered and most of the merchant houses of Tollen today are established during this time period.

In the 5600s, war comes to the [[Green Sea]], first the battles against the ancient white dragon Vimfrost, and then the [[Great War]] itself. Tollen, however, survives intact, and if anything grows in power and influence, as many of the Sembaran kings in the years after the [[Great War]] have ties by blood or marriage to the great houses of Tollen.

Now, in 5881, Tollen commands a significant navy and is the undisputed master of the Western Gulf, controlling the [[Straits of Cymea]] and asserting influence over much of western [[Cymea]].



## Guilds

Tollen is a city of guilds: the various trade associations, craft guilds, and producer's compacts are the center of power in the city. Particularly notable guilds include:
- [[Dyer's Guild]]
- [[Ancient and Honorable Guild of Philosophers]]

## Economy and Trade

Tollen is the master of the [[Western Gulf]], with significant fishing, merchant, and naval fleets. The Tollender navy controls the islands in the gulf of Tollen, as well as the Straits of [[Cymea]], and patrols the [[Western Gulf]], keeping it free of pirates. 

The Tollen economy is powered by trade. Tollenders produce [[Tollen Dyes|dyes]]. cloth, and fine clothes that are widely sought across the [[Green Sea]], and are also known for shipbuilding, fishing, [[Whaling]], and the fur trade. Tollender merchant fleets travel widely, bringing exotic goods back west, both as the raw ingredients for dyes (both mundane and magical) and for trade. Tollen is also a center for the production of [[Tollen Magical Tattoo|magical inks and tattoos]].

%%NOTES
1. Need to add a few more weird / magical details. For example, from an old email:

* I like the idea of Tollen being a place where people still talk, at least in certain contexts or certain guilds or schools within the university, about the ancient days, meaning the early 4000s. Why not have a place like London or Rome but where some philosopher's guild founded in Roman Londonium still survives? That's about the same timeframe. It seems like it would be one of the few places where that kind of thing really fits, and a rich source of interesting stuff. Of course half the 'we were founded in the dawn days of the city' things would really have been founded at various other times with ancient backstories, but some of them are probably real.

* I like the idea of Tollen always being on the 'edge' in the points where it wasn't powerful, and never being a major part of someone else's empire. That isn't to say it shouldn't have various ancient connections, but that it was never itself Sembaran, or Drankorian, or Skagen, at least not in an important sense.

* Is there a place for some kind of magical / extraplanar reason for why it is so religiously open? A connection to outer planes, or maybe it was defended during [[The Downfall]] Wars by an army of small gods, and something about that sacrifice magnifies the divine essence. Or something.

A few other times in history that you've outlined that seem fraught with possibility:

* The Drankorian peace treaty. My history below centers Tollen as the architects of the peace treaty, and maybe there are reasons why. A storm giant foretold [[The Downfall]] of [[Drankorian Empire|Drankor]] if they expanded past the Voltra, and Tollen had evidence? Some kind of divine intervention, the divinities of Mos Numera insisted Tollen remain free? Maybe there is something special about the place that makes all the various gods of Taelgar keen to ensure it is never fully controlled by a single set of gods. 

* Playing on the powerful-religion idea, maybe there are a set of worshippers of the old OceanGod floating around Tollen. Or various void-mind gods. 

Here's an idea for an alternative timeline that keeps Tollen independent the whole time... not sure if it fits with your vision, I won't be offended if you toss it :)

What if the earliest settlers of Tollen were explicitly the misfits and dissatisfied with the marnier culture (not sure what it is like exactly, but I imagine by the 3900s the OceanGod was dominant in a way that would allow some questioners or people not wedded to the mariner way of life to want to strike out). I'm thinking a bit of a Roger Williams or some of the other 'free thinker' early New England settlers vibe. 

From that earliest point, Tollen gains a reputation as a free-wheeling place of stories and misfits and those who are looking for a new life. And with them comes the curious from other cultures, and it turns out [[Highlands]] and the mariners have a lot to sell each other, so then comes the merchants.

In the 4050s, [[The Downfall]] War certainly unsettles things, but that doesn't mean Tollen has to be abandoned. The merchants flee, and the city shrinks dramatically, but it is not abandoned entirely.  

By the 4200s, the Skaer re-discover Tollen, and although it largely becomes a Skagen city, some ancient institutions of storytellers, knowledge seekers, and free-thinkers maintain their place in the city (need some kind of event to make this work out), and Tollen remains a place where the Skagen religion does not hold sway entirely.

Throughout the 300 years of the Skagen dominion Tollen grows as a marnier culture, and grows as a center of commerce. Many supposedly ancient institutions survive in the city however, although who really knows how many are truly ancient, as opposed to institutions that invented ancient roots to gain prestige or maintain independence from the Skagen protectorate.

By 4547, the Drankors are on the doorstep and the Skaer are at war with them. It is Tollen that brokers the peace treaty between the Drankorians and the Skaer, earning an uneasy freedom from both the Drankorians, who refrain from formally conqueoring the city in exchange for de facto control of its foreign policy, and from the Skaer, who are forbidden from sailing up the Voltra.

I do like the idea of Tollen as central to the treaty that stopped Drankorian expansion, and it makes sense for this to have some kind of magical "great powers" connection -- either divine, or perhaps something connected to dragons or [[Giants]] or elementals (fey are taken by [[Tyrwingha]]). Will think a bit more on this, again might be something best to see what happens during a game.

Notes from old GDrive doc, could be old/wrong/etc, here to incorporate/check/delete
#### Tollen

- Masters of the Western Gulf. Significant fishing and merchant fleet. Strongest navy in the Western Gulf and major fishing industry (whales? Cod? Not sure what the key fish would be. Also no lenten red meat rules to drive a cash crop fish industry, so maybe not quite as developed as say the Basque medieval fisherman who got rich on cod)
    
- Controls a narrow strip of land on the north bank of the Volta as well as the Tollen city proper, and the coastal islands in the greater Tollen harbor.
    
- Controls the Straits of Cymea, main seafarers in the Western Gulf
    
- Manufacturing esp of clothes key. Silk (or cotton or a made up fiber) from Tyrwingha and wool from Sembara comes to the Tollen + northlands region to turn into fine clothes
    
- Big dye industry in the hinterlands
    
- Influential in the northlands more than anywhere else and somewhat culturally connected to that region (although with a clear, distinct identity)
    
- Some significant far eastern trade, although that in general is probably more halfling/Cymean; Tollen is however a major market for Cymea traders, who exchange goods from around the Green Sea for Sembaran/Tollen cloth/silk/clothes.
    
- University in Tollen is major center of magical learning in the Sembara/Vostok region, only some parts of Cymea could compete in western Green Sea area. Dye industry + magic makes Tollen a center of development of magical tattoos.
    
- In many ways more cosmopolitan than Sembara; significant local halfling and dwarven communities, and stoneborn are not unheard of. Elves still super-rare, and lizardfolk if anything less common than in Sembara.




%%

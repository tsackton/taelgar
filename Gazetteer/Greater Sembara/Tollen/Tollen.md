---
headerVersion: 2023.11.25
tags:
  - place
name: Free City of Tollen
typeOf: settlement
whereabouts: Western Green Sea
aliases:
  - Free City of Tollen
  - Tollen
  - Tollender
dm_owner: tim
dm_notes: important
typeOfAlias: city
---
# The Free City of Tollen
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% 
dm_notes -> there are still a fair number of possibly-relevant notes to expose from Dunmar Campaign, including some relevant to major NPCS ([[Caelynn]]) and some overall vibes that may not be fully caputred
%%

Tollen is a bustling port on the [[Volta]], a growing naval power, a cultural mixing ground, and an entrepôt where goods from across the [[Green Sea]] are traded. Founded thousands of years ago, it has navigated the politics of the region and maintained its independence for centuries. It is a haven for merchants, traders, intellectuals, mages, poets, writers, and scholars, known for the [[University of Tollen]] and its powerful guilds. 

Tollen is a cosmopolitan city, where [[humans]], [[halflings]], [[dwarves]], [[stoneborn]], [[lizardfolk]], [[Kenku|kenku]], [[Elves|elves]], and more can be found living together, and where temples to many gods can be found, most prominently the [[Mos Numena|Eight Divines]] and the Skaer ocean goddess [[Kaikkea]]. 

Tollen is also a city of guilds: the various trade associations, craft guilds, and producer's compacts are the center of economic and political power in the city. Particularly notable guilds include the [[Dyer's Guild]], controlling the magical tattoo trade, and the mysterious [[Ancient and Honorable Guild of Philosophers]], but many other guilds exist in the city. 

## Geography and Hydrology
_See more: [[Hydrology of Tollen]]_

Tollen sits astride the [[Volta]] river, though most development is on the north side, which is generally rockier, less marshy, and generally less prone to flooding. Five tributaries of the Volta flow through the city and its environs, from west to east: the [[Little River]], the [[Muddy River]] (the only tributary that joins the Volta on the south bank), [[Fat Brook]], the [[Carnbrook]], and the [[Greywash]]. The area around the confluence of the Volta, Little, and Muddy rivers is swampy and prone to flooding; the area around the confluence of the Greywash and the Volta, east of the city proper, is even more so. The difficult terrain around the Greywash has long discouraged eastern expansion of the city. 

%% the marshes around the Greywash are a plausible place for a lizardfolk community if desired - this never really came up when the Dunmar campaign was in Tollen but might be nice to add for various reasons, though perhaps this is -- unusually -- a relatively new lizardfolk settlement (say, post Great War, or maybe just post plague), instead of a remnant of the ancient swamps %% 

## City Layout
_See more: [[Port of Tollen]]_, _[[Map of Tollen]]_

%% design doc from OneNote here: [[Tollen - Design Note]] %%

Tollen sprawls astride the Volta, although most settlement is on the north bank. The oldest parts of the city are the eastern wards, which tend to have small, cramped streets and are home to the docks and the shipbuilding industry. The central part of the city, especially around the [[Tollen Bridge]], and extending west, is a major commercial hub, with markets, guildhalls, and broad boulevards. The western part of the city, clustered around the Little and Muddy rivers, is home to tanners, leatherworkers, dye-makers, and other industry; most of the recent expansion has been in this direction, including many sprawling slums outside the walls. 

### Wards of Tollen
_See more: [[Wards of Tollen]]_

Tollen is divided into 17 wards, mostly on the north bank of the [[Volta]] and largely contained within the city walls, though as the population has grown in recent years the city has swelled beyond its walls, particularly to the west. 

The oldest parts of the city -- the wards of [[Fiskurth]], [[Aesganstrad]], and [[Skepwalk]] -- are clustered along the banks of the Volta in the eastern (ocean-ward) part of [[Tollen]], reflecting the city's heritage as a Skaer port long ago. 

[[Magus Street]], where the [[University of Tollen]] is located; [[Bridgeward]], on the north side of the [[Tollen Bridge]]; and [[Nordgate]], now home to a substantial dwarven population, surround this inner core. The rich commercial districts of [[Gold Street]] and [[Guildgate]]; [[Godshome]], with many temples; [[Fairgate]], with many markets; [[Southbridge]], on the south bank of the Volta across from [[Bridgeward]]; [[Haurhill]], on the height of land above the [[Little River]] and the site of an ancient Drankorian fort; and [[Battery]], home to extensive naval fortifications, make up the rest of the city as it stood at the time of the [[Great War]]. 

More recently, as Tollen's prominence has grown, the marshy land on the south bank west of [[Southbridge]] has been drained and settled, forming the new wards of [[Fenslane]] and [[Tideswell]]; and the walls have been expanded to the west, enclosing the new wards of [[Brooklawn]], a low-lying industrial area along the [[Little River]], and [[Riversgate]], along the new western gate of the city. 

### Bridges, Walls, and Gates

Only one bridge spans the [[Volta]]: the [[Tollen Bridge]], originally constructed by the [[Drankorian Empire]]. This broad stone span of many arches is a major commercial hub, lined with shops, houses, and activity, and also a defensive structure, with gatehouses at either end. Tall-masted oceanic ships cannot pass under the bridge. 

While the [[Walls of Tollen|walls of Tollen]] have expanded many times during its history, there are ten gates in the current walls, from east to west: Old Gate, Fort Gate, Scholar's Gate, North Gate, Temple Gate, Guild Gate, [[Fair Gate]], [[Tanner's Gate (Tollen)|Tanner's Gate]], River Gate, and West Gate. 

### Landmarks

Tollen has many notable landmarks. The most famous is the [[Tollen Bridge]], a vast span across the wide [[Volta]] that dates to the days of the [[Drankorian Empire]], now lined with shops. There are also many temples, particularly the [[Temple of The Wanderer (Tollen)|Temple of the Wanderer]], with its massive spire, the [[Temple of the Sibyl (Tollen)|Temple of the Sibyl]], with its colorful dome, and the Skaer [[Temple of Kaikkea]], one of the oldest buildings in Tollen. 

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

## Governance and Laws

By long custom, Tollen is an open city. No tolls are levied for entering the city or crossing the Tollen Bridge, the gates are unbarred from first light until dusk, and strangers come and go as they please. Goods for sale, however, are heavily taxed at the customs houses outside the gates and at the docks. 

%% 
The canonical fact to explain here is that the trade goods the Dunmar Fellowship brought back from Vetta were charged a high duty. 

However, need to consider the economic logic on three fronts:
- guilds would not want to pay taxes on raw materials they need for finishing, as that just drives up the costs of their inputs
- halflings likely have some kind of longstanding arrangement, but it cannot be one that would put human traders out of business
- tollen needs a way to get money - are custom duties a way to protect guilds, or a way to get city funds?

%%

City laws bar strangers from wearing armor or carrying war-blades larger than a dagger within the walls. In practice, the gate-guards will generally turn a blind eye to single swords and the odd mail shirt, so long as no one marches in file or clanks about in full harness. By custom, [[dwarves]], [[elves]], and [[stoneborn]] are treated as city residents and rarely questioned over armor or weapons, even in full plate, though city guards may ask pointed questions of armed groups of any species. 

%% Unclear how halflings and lizardfolk are treated - maybe part of this? but they are not likely to go about in full armor. The point is an elf with a halberd or a dwarf in plate mail would not be questioned, though a human might %%

Tollen is a republic, for certain values of the word. Power largely rests in the hands of the guilds, who send men and women to the Great Council. 

%% This is a brief sketch. Probably there is more complicated politics but nothing has been developed so far. The Great Council may have non-guild seats; there may be a Small Council or First Councillor or both chosen from the Great Council to wield executive power on a day to day basis; the exact allocation of seats on the Great Council is unclear. The only canonical bit is (a) there is a Great Council, and (b) most of the seats are allocated to guilds, and guilds are the basis of political power in Tollen. %%

Tollen is the dominant maritime power of the [[Western Gulf]], with significant fishing, merchant, and naval fleets. The Tollender navy controls the [[Straits of Cymea]], patrols the [[Western Gulf]], keeping it free of pirates, and maintains naval fortifications in the islands in the [[~Gulf of Tollen~]]. 

%% How the navy relates to the guilds is TBD %%

In recent years, Tollen has extended its reach, settling colonies and establishing political control over large swaths of [[Western Cymea]].

%% Exactly how this plays out politically is TBD; the extent to which Tollen has historically exerted control over the near hinterlands is also TBD, though canonically it has not extended control across the Western Gulf until recently. Whether it only has colonies in western Cymea, or also controls parts of Vostok, is TBD, awaiting further development of Vostok. %%

## Economy and Trade

The economy of Tollen is powered by trade. Tollenders produce [[Tollen Dyes|dyes]], cloth, and fine clothes that are widely sought across the [[Green Sea]], and are also known for shipbuilding, fishing, [[whaling]], and the fur trade. Tollen is also famous as a center for the production of [[Tollen Magical Tattoo|magical inks and tattoos]].  To support itself and these industries, Tollen imports significant grain, fine wool and other fibers, and timber. 

%% See below for more on trade. %%

Tollen is a major entrepôt on the Green Sea: its merchant fleets travel widely, bringing exotic goods back west. While many of these are used as raw ingredients for dyes (both mundane and magical), a large portion are exported south to the realms of the [[Greater Sembara]] region.

## History
_See more: [[History of Tollen]]_

Tollen was settled in ancient days on the north bank of the Volta, pre-dating even the [[Downfall Wars]] and the founding of the ruined city of [[Drankor]]. A cosmopolitan port from its earliest days, it was a place where elves, lizardfolk, halfling traders, and several human cultures met and mingled. Under the Skaer thalassocracy in the years after the [[The Downfall|Downfall]], it grew into a key harbor on the Western Green Sea, and the oldest wards—Fiskurth, [[Skepwalk]], [[Aesganstrad]]—mostly date to this era. 

Tollen’s first great turning point came with the Treaty of Marhavn in DR 402, when Skaer power yielded to the Drankorian Empire: the Volta became the imperial border, Tollen gained stone walls and the Tollen Bridge, and the city slid into de facto status as a Drankorian protectorate, though it was never formally governed by the Empire. 

The Fall of Drankor and the First Plague in DR 1059 left Tollen suddenly independent. Spared the worst of the fallout from the collapse of the [[Drankorian Empire]], Tollen grew over the following centuries into a guild-ruled free city, its walls creeping outward in rings while trade made its merchant houses rich. 

The city weathered the [[Great War]] without ever being sacked, and in the last century it has stepped onto the wider stage as a naval power in its own right. With Cymea’s decline, Tollish fleets now dominate the Western Gulf and the Straits of Cymea, and Tollish free ports in Western Cymea function as colonies. Now, Tollen is both an ancient, stubbornly independent river-city and a young, hungry maritime republic, looking ever further from its old Skaer quays toward the open sea.


%%^Campaign:none%%
## DM Notes

### Basic Vibes
Tollen should feel a little like a mix of Renaissance / early modern London and medieval Venice. It is a major port, with a semi-democratic form of government, guilds as the primary base of political power, and a growing and ambitious navy. 

Tollen is an old city. It is a place where people still talk, at least in certain contexts (e.g. certain guilds) about the ancient days (meaning pre-Downfall). The Philosopher's Guild likely legitimately traces its origin to "ancient days" (though tread carefully with canonical invention around the Philosopher's Guild; it is best it remain very mysterious); other guilds may claim an ancient heritage (meaning either Drankorian or pre-Downfall) and in some cases may even be correct. 

Tollen is also deeply independent. While it was a Skaer port, and then deeply influenced by Drankor, and then connected to Sembaran politics, it has never been central to anyone's empire, and has always retained a cosmopolitan identity. This is likely a point of pride for many Tollenders.

Tollen is unusual in Taelgar in being a city with many religious traditions. Only Mos Numena and the Skaer worship of [[Kaikkea]] have been introduced in play, but there is space for kestavan worship and perhaps other stranger things. Tollen is a good place for a strange temple to a forgotten god to still exist, for example. 

One possibility is that there is some kind of magical or extraplanar reaason why it is so religiously open. Perhaps it has a connection to outer planes, or it was defended during the [[Downfall Wars]] by an army of small gods and something about that sacrifice magnifies the divine essence. Or something else. 

### Economic Logic

Tollen is not primarily a producer city; it’s a finisher and redistributor.

 It pulls in raw or semi-processed materials from:
- the Volta hinterland (hides, timber, furs, flax, some wool),
- Sembaran uplands (raw wool especially, plus grain, wine),
- its own colonies and trading fleets (exotic dye-stuffs, magical reagents, rare woods, oils).

 It turns those into high-value, high-prestige goods, especially:
-  dyed cloth (Tollen red and friends),    
- fine garments,
- leather goods,
- magical inks and tattoos,
- ships and rigging.

Basically Bruges / Ghent / Venice / London mashed together.

Tollen's key resources are: cheap fuel from timber upriver; plenty of water. Cloth is particularly logical because raw wool ships well. 

This implies that some goods -- timber, raw hides, maybe some flax/linen -- come from the north, so maybe enter the city via Tanner's Gate or River Gate. 

#### Trade Flows

Grain, wine, foodstuffs -> largely imported from Sembaran heartlands; some from Western Cymea, Tyrwingha, Addermarch via ship, perhaps? But seems clear Sembara is the breadbasket of Tollen.

Fine wool, linen, flax -> while some may come from local hinterlands, ~Volta Hills~, etc, the best wool comes from Wisford and Cheimen. This is dyed and re-exported as fine cloth and clothes. 

Timber -> the Volta watershed is very rich in timber, so this largely comes downriver. Probably from a mix of colonies and Telham merchants, but this is not entirely clear. Breva is not a very trade-oriented society. This is crucial to Tollen prosperity, especially shipbuilding, so decent chance for colonial control of some hinterlands, but this might be a recent development. 

Hides and especially furs may be more likely to come in from Brevan hunters and various other small operators, but this is not clear either. It is possible there is something like the Hudson Bay Company organized out of Tollen. 

Unclear where metal comes from. It is possible there are mines in the ~Volta Hills~, or this is an import Tollen relies on. Tollen might have its own mint, which implies the need for a source of silver at least. 

### Territory

An open question is exactly to what extent Tollen controls its hinterlands. It must, to a certain extent? And of course more recently it presumably controls the entire [[~Gulf of Tollen~]] in addition to the immediate hinterlands. 

%%^End%%

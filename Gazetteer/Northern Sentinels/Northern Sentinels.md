---
headerVersion: 2023.11.25
tags: [place, status/check/mike]
typeOf: region
whereabouts: [{type: home, location: Taelgar, linkText: "in" }]
dm_owner: tim
dm_notes: important
---
# The Northern Sentinels
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% rewrite in the "halfling style", fill in a few additional details %%

Even among the halflings, few reliable tales come from the northern reaches of the great [[Sentinel Range]]. This is a wild and unpeopled land, haunted by the scars of the [[Great War]], and spoken of uncertainly, in hushed tones even among the adventurous. What stories do drift south speak of vast pine forests, uninhabitable bogs, and the tall mountain peaks of the [[Sentinel Range#Northern Sentinels|northern Sentinels]], painting a picture of a rugged and beautiful, but inhospitable and dangerous, landscape. 

```leaflet 
id: region-map-taelgar
image: [[north-sentinels-map.png]]
bounds: 
- [0,0]
- [2503, 2188]
height: 500px  
width: 500px
lat: 1250
long: 1150
minZoom: -2
maxZoom: 0
defaultZoom: -2
unit: miles 
scale: 0.5
draw: false
darkMode: false
markerTag: location-source
```


## Topography and Major Features

%% _See more: [[Sentinel Range#Northern Sentinels|North Sentinels]]_  I'm not sure the North Sentinels section of the Sentinels is useful as a see more.  There is almost nothing there, and it seems more sensible to repeat it here. %%

Even among the halflings, few have dared to map this region, nestled on the west side of the [[Sentinel Range]], and even among the most daring traders, few find profit traveling these dangerous lands. Much of the region dominated by the northern [[Sentinel Range|Sentinels]] and the forests and rivers on their western slopes, making travel slope and difficult. The mountains themselves are snowy and rocky, with the highest peaks cold and frozen year round. 

The information reported here largely derives from the [[Northern Tribes|scattered human tribes]] in the area speak of the dangerous forests and swamps:

- The [[~Pandar Volcanic Range~]], once the borders of [[Cha'mutte]]'s realm, now a place all sensible folk fear.
* The [[Forest of Nightmares]], said to be haunted, cursed by [[Cha'mutte]] during the [[Great War]].
* The [[Blackwater Fens]], a dank bog from which the [[Nahadi]] arises.

There are two major river systems that originate in this region:

- The [[K'eye]] in the local language, and translated by halflings as the Red River, flows from the [[Sentinel Range|Sentinels]] to the [[~North Bay~]]. 
- The [[Nahadi]] in the local language, and translated by halflings at the Great River, flows from its origins in the [[Blackwater Fens]] south to [[Lake Valandros]] and beyond. %% see note in Nahadi page about naming %%
## Civilizations and Cultures

%% *See more: [[Northern Tribes]]* I wouldn't actually put this as "see more" - it is immediately linked below. I tend to think of the see more pages as expanded overviews more than links to highlight. %%

There are few humans in this region, although the [[Northern Tribes|northern Deno'qai tribes]] make their home here. The dwarven kingdom of [[Fahnukan]] lies beneath the northern Sentinels, and [[Stoneborn|stoneborn]] are known to live in the highlands and foothills of the [[Sentinel Range|Sentinels]].

%%
Elves:  None
Dwarves:  [[Fahnukan]]
Lizardfolk: ??
Humans:  [[Deno'qai]]
Stoneborn:  Yes, should be defined more?
Hobgoblins: ??
Dangerous Wildernesses: Yes
%%
## Major Historical Eras
_See more: [[Pandar]]_

In the ancient days before [[The Downfall]] it is said that the [[~Northerner~|northerners]] crossed the [[Sentinel Range|Sentinels]] at the [[~Unnamed North Sentinel Pass~]]  in their eastward migrations, but the truth of this is unclear.

In the long years leading up to the [[Great War]] the land of [[Pandar]] was [[Cha'mutte|Cha'mutte's]] home, and hobgoblins and enslaved [[Kenku|kenku]] were common sights. Since the [[Great War]] this area has been lightly populated and full of dangers.
## Climate
The mountains here are snowy, rocky, and volcanic, marked by pine forests on the western slopes and long, bitter winters. The forests and fens to the west are marked by cold, snowy winters and short, wet summers. There is little farmable land here.

%%^Campaign:none%%
***Real world analogs:*** This region is at approx. 52 degrees north, and probably has some similarities with the Canadian Rockies, especially Banff and Jasper national parks, including the flat plains to the east of the mountains (in the [[Far North]]). The volcanic mountains of [[Pandar]] share some similarities with the Pacific Ring of Fire, but with a much more magical vibe, and less moderating coastal influence on climate. 

- [[Blackwater Fens]]: *not really developed; was the home to a black dragon in the [[Great Library Campaign]], unpleasant but not frozen in the winter. Around 50 degrees North. There is probably not a great real world analogy, the basic idea is something like a temperate version of a [peat swamp forest](https://en.wikipedia.org/wiki/Peat_swamp_forest). Maybe a place like [here](https://www.visitestonia.com/en/where-to-go/west-estonia/soomaa-national-park) or just a more northerly version of the Great Dismal Swamp or something like that. Notably wooded, although generally a fairly open forest, not dense and tangled, with most of the obstacles to travel coming from bogs and unstable ground.* 

The fens probably have a similar ecosystem to the [Hudson Bay bog](https://en.wikipedia.org/wiki/Southern_Hudson_Bay_taiga), although perhaps a little bit warmer -- an "insect-infested landscape of bog and fog". 
%%^End%%

%%^Campaign:None%%
## DM Notes and Meta

*Canonical Development and Constraints:* [[Pandar]] was canonically [[Cha'mutte]]'s primary permanent territory, and a large number of kenku enslaved by Cha'mutte lived here prior to the [[Great War]]. The history of the [[History of the Northern Deno'qai|northern Deno'qai]], including some details of the Great War era, and their current [[Northern Tribes|culture and territory]] is well developed. The [[Forest of Nightmares]], and the [[Blackwater Fens]], have some canonical details. Stoneborn, at least, canonically live in the [[Sentinel Range|Sentinels]] in this region. 

*Brainstorming and Potential Canon:* Some basic overview of the history of Pandar and Cha'mutte's activities exist, but these are largely brainstorming, or at best weakly canonical. 

*Needs Development:* None.

*Intentionally Blank:*  Much of this region is functionally a blank spot. In general, this region was dominated by [[Cha'mutte]] during the [[Great War]] and is best kept relatively empty as a setting for dark and dangerous things.

*Adventures:* The Delwath solo arc of the Dunmar Frontier campaign was set in the northern Deno'qai territory and the Forest of Nightmares; the black dragon arc of the Great Library campaign was set in the [[Blackwater Fens]]. 

### Unnamed In-Links
Pages that link to a Northern Sentinels page and are currently unnamed. 
```dataview
TABLE 
    length(file.inlinks) AS Backlinks
FROM ""
WHERE 
    startswith(file.name, "~") AND
    any(filter(file.inlinks, (b) => contains(meta(b).path, "Northern Sentinels")))
SORT length(file.inlinks) DESC

```

### Staging
These are staging pages linked to a Northern Sentinels page
```dataview
TABLE 
    length(file.inlinks) as Backlinks
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Northern Sentinels")))
SORT length(file.inlinks) DESC
```
%%^End%%
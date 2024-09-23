---
headerVersion: 2023.11.25
tags: [place, status/cleanup/internal]
name: Xurkhaz
created: 1583
typeOf: realm
whereabouts: Garamjala Desert
pronunciation: ZURK-kaz
---
# Xurkhaz
*(ZURK-kaz)*
>[!info]+ Information
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%%rewrite in the style of the Dunmar page%%

Xurkhaz, the Land of the Peaceful Sun, is the kingdom of the [[People of the Rainbow]].
## Geography

Xurkhaz is roughly a triangle, wedged between the [[Kulthul]] and the [[Istaros]] rivers (both tributaries of the [[Istaros]], to the Dunmari). The borders of Xurkhaz start in the northeast at a point on the Drogar about 120 miles north of the confluence, where the terrain on the east bank rises sharply into a series of jagged, broken hills, and the river rushes through a series of waterfalls and gorges. It follows the line of the Drogar south, remaining on the western bank until the hills to the east flatten into dry, cracked plains, about 60 miles north of the confluence. Here the river valley itself is hospitable, and the [[orcs]] of Xurkhaz settle both sides of the Drogar densely, continuing south to a point about 40 miles downriver of the confluence with the Kulthul. Here, the river turns and flows slowly through sandy deserts, and the inhospitable land further south is not settled. To the west, Xurkhaz follows the course of the Kulthul, which forms a defensible western border against the dangers of the [[Nashtkar]], end in a series of forts about 100 miles north of the confluence. 

%% comment
at some point need to work out the hierarchy of [[Nashtkar]], [[Garamjala Desert|Garamjala]], [[Plaguelands]], and [[Desolation of Cha'mutte]]
%%

The heart of the kingdom is the land between the two rivers, which is heavily irrigated; the land is more densely settled to the east, and especially the western banks of the Drogar. This is a dry, arid land of rolling hills and deserts, sustained by heavy irrigation and desert-adapted, long-horned cattle. Cattle and wheat are prominent in both the culture and the landscape. 

%% notes 
this is inspired / influenced by ancient Egypt to a certain extent
might need to figure out why the [[Istaros]] river system has so much water flowing through the desert even in 1750, when western rivers are kind of dried up / seasonal
%%
## Settlements

Most of the population is heavily rural living in small farming and herding villages, densely concentrated within a day's walk of the rivers. That said, there are some notable settlements: 

- [[Uzgukhar]], the capitol, at the confluence of the [[Istaros]] and [[Kulthul]]
- [[Khumarz]], a fortified border town on the eastern banks of the [[Kulthul]], guarding one of the major fords of the river and serving as the lynchpin of the western defenses of Zurkhaz
- [[Drogoloth]], a mining town on the western banks of the [[Istaros]], near the hills and at the furthest point north boats can travel on the [[Istaros]] before hitting the rapids
- [[Gorzum]], a peaceful oasis in the middle of the country

%% rough population notes
While these are "towns", only the capitol has more than 1000 people living it in. Total population of the country is maybe 20,000, of which about 16,000 (or 80%) are rural , about 1500 live in the capitol, about 500 live in each of the "major" towns, and other 500 live in planned border forts. Most of the rural population lives in numerous (200 or so) small villages of 50-100 people.
%%
## People

The orcs of Xurkhaz have tried to hide themselves from the world for a long time. While some speak Common, or Sylvan, most speak only Orcish, and are extremely wary of outsiders. 

%% notes
There are few taverns and no inns in Xurkhaz. 

Mostly speak Orcish; a few speak Common or Sylvan, so communication not trivial except via Tongues. 

Common "villager" types: cattle herder, farmer, brewer, leatherworker
Common "fort" types: solider, blacksmith, sergeant

%%

%%^Campaign:DuFr%%
## Events

%% still need to add
- arrival of Chardonians, discovery of their purpose, death of one who was killed
- arrival of party
- War of the Cloak
%%

```dataview
TABLE events.text as Event from -"_MoC" AND -"_DM_" flatten file.lists as events where contains(events.text, this.file.name) sort events.DR
```

%%^End%%
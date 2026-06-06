---
headerVersion: 2023.11.25
tags: [group, status/cleanup/text, status/gameupdate/dufr]
displayDefaults: {defArt: 'the', boxInfo: ""}
name: Rangers
typeOf: army
whereabouts: Greater Sembara
dm_notes: none
dm_owner: mike,tim
---
# The Rangers
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% needs some updating to make less specific to 1720, and expand a little to capture vibes; e.g., well established that rangers are highly diverse species-wise and also fairly loose organizationally 

There is some brainstorming of a potential relationship to Isingue in [[2023-08-08 - Isingue]] and some more thoughts in [[2023-11-05 - Rangers, Elves, Great War]]
%%

The Rangers are a loose collection of wanders, warriors, scouts, and others dedicated to keeping dark things from peaceful villages, and keeping the ways between towns safe. There is no formal leadership, by many look to Johanne the Younger, of [[Valarin]] for guidance. Small groups, or individual Rangers, are often seen on the Dunmari Road, keeping it safe for trade, or scouting the edges of the Plaguelands or the [[Darkwood]] near Addermarch. Many Rangers look to Beryl - once a hero, now a constellation and demi-god, the [[Fox and Hunter]] - for inspiration and comfort. In the frontier, of [[Duchy of Maseau|Maseau]], the Aurbez, and other places along the Plaguelands, Rangers often are the ones trying to keep the peace. 

%% Cleenseau notes:

The Rangers have not come up much; but they have been established as being vaguely based in the "south" (Maseau/Addermarch) much more than Sembara, although with some presence along the Enst valley. And they have enough of a communications network that they came north to help with the undead attacks in several groups

The [[Report on the Bogblight]] has some in world vibes about the rangers as well, they seem to have had  an extra-special concern about other worldly dangers, although conceptually that could have just be [[Vahaiya]]

%%

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%


%%^Campaign:None%%
### Historical Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Born", "Died"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.sort(b => b.born)
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<startStatus> <startDate>",b.file, dv.current().pageTargetDate), util.s("<endStatus> <endDate>",b.file, dv.current().pageTargetDate)]))
```
%%^End%%


%%^Campaign:none%%

There are two significant lines of invention around the history of the Rangers:

- The Rangers are clearly connected to [[Isingue]] and the ancient magic associated with the [[Heartroot]].
- The Rangers are clearly connected to the guerrilla wars against Avatus during the [[Serpentine Wars]].

Both of these facts are clearly established canon introduced in game. 

One possible explanation is that Beryl joined together two disparate, but philosophically similar, groups that had grown out of opposite to Avatus - the more magically inclined Isingue folks who used the Heartroot to grow magical walls to defend against Avatus, and the more nature/scout inclined folks from Addermarch. 

It is also possible there is aid flowing from Isingue to Addermarch and back during the Serpentine Wars, since the route along the Valmont between the two realms is likely open at this time. 

This could fit into Beryl's backstory as my recollection was he wasn't really a city person so probably would have been from somewhere in the Isingue sphere of influence but not the city itself. 

However other stories are possible, and it is also possible that current-day Rangers shade their history a little depending on where they are from (so, e.g. the Addermarch rangers play up connect to Addermarch history more than maybe is strictly true - though my Addermarch PCs met a stoneborn who remembered some of the history so there can't be no connection). 

%%^End%%
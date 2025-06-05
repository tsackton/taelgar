---
headerVersion: 2023.11.25
tags: [place, status/cleanup/text]
name: Tyrwingha
typeOf: realm
whereabouts: Greater Sembara
aliases: [Tyrwinghan]
dm_notes: important
dm_owner: shared,mike
---
# Tyrwingha
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% I have various session planning and especially intra-session emails that impinge on Tyrwingha %%

The land of Tyrwingha, nestled on the southern shores of the [[Green Sea]], is ruled by the monarch of [[Sembara]] in a personal union of the crowns.  Over its history, it has been been united with Sembara on two separate occasions, the most recently by [[Elaine I]].

Although they share a monarch, Tyrwingha and [[Sembara]] see themselves as distinct monarchies with unique histories and cultures.

It is a land of few cities beyond the capital, [[Tafolwern]], but is a land rich in magic and tradition. The [[Archfey Ethlenn]], the Queen of the Evening Mist, is said to have been watching over Tyrwingha since time immemorial, and the Tyrwinghans see themselves as the inheritors of an ancient and sacred tradition.  

Bordered by the [[Green Sea]] in the north and the [[Mostreve Hills]] in the south, it is an agriculturally fertile land and thrives on rich harvests of wheat and wine, as well as timber from the northern slopes of the [[Mostreve Hills]]. Although not a backwater exactly, it is economically somewhat isolated from the main trade routes of Greater Sembara, and mostly lives and dies with the harvest.

Politically, it is a monarchy, although the monarch is formally elected by the [[Oracle of the Riven]] (or as they are more prosaically known, the royal electors). Traditionally, the Oracles are warlocks, although like Ethlenn's vote, this tradition is not always observed in the modern day. Second in importance to the oracles are the earls, high lords of the realm. Today, the title has been exported to has lost some of its traditional meaning -- a noble who had pledged loyalty to Ethlenn in her court. Nonetheless the earls are powerful lords in Tyrwingha, and often control significant landholdings, although freeholds are also more common here than elsewhere in Greater Sembara, and small, independent villages without a lord are not so rare. 

%% Note: There are some important details about earls not captured here; nothing is wrong per-se but use with caution - the conversation was mostly in Discord but some of [[Celyn]] background stories shed light as well %%

The Army of Mostreve is another major part of Tyrwingha, led by the fearsome eldritch knights and an elite cadre of warlocks. The Army was organized by [[Derik I]] after his victories over the [[Dominion of Avatus]], and it today provides a significant route of social mobility. Three major garrisons dot the [[Mostreve Hills]] - the garrison of the Aben, in the headwaters of the [[Aben]] River, the garrison of Cyfarthfa closest to the capital, and the garrison of Deganwy on the borders of Addermarch. The Aben garrison sees action most years, and is a gathering spot for [[The Rangers]].

Religiously, little is remembered about the ancient gods of Tyrwingha, such as they were. The [[Mos Numena|Eight Divines]] are worshipped here much as they are elsewhere in [[Sembara]]. It is said that when Ethlenn made her bargain with the Drankorians (see below), she acknowledged the suzerainty of the Drankorian gods. However, the fey are remembered and honored alongside the gods -- the people of Tyrwingha have a deep respect for the traditions of the fey and what others might call superstition is here seen as simple common sense. The temple stewards in Tyrwingha often have a second job, ensuring the fairy rings are not distributed, leaving out milk and brown bread for the pixies, and other such things.


%%^Campaign:None%%
### Places in Tyrwingha
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%
%%^Campaign:None%%
### Cities in Tyrwingha
```dataviewjs
const { util } = customJS
dv.table(["Place", "Region", "Type Of", "Population"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.file.frontmatter.typeOf == "settlement"))
				.sort(f => util.s("<home:1>", f.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<home:1>", b.file, dv.current().pageTargetDate), util.s("<maintype>", b.file, dv.current().pageTargetDate), util.s("<population>", b.file, dv.current().pageTargetDate)]))
```

%%^End%%
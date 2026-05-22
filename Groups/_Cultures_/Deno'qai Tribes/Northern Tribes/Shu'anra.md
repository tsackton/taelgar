---
headerVersion: 2023.11.25
tags: [ancestry]
displayDefaults: {defArt: the, boxInfo: One of the <partOf:1UA>, wHome: ""}
name: Shu'anra
typeOf: tribe
partOf: Northern Tribes
dm_notes: none
dm_owner: none
---
# The Shu'anra
>[!info]+ Information  
> One of the the [[Northern Tribes|Northern Tribes of the Deno'qai]]

The Shu'anra are one of the [[Northern Tribes|northern]] [[Deno'qai]] tribes. Like other northern Deno'qai tribes, the Shu'anra are descended from the survivors of the [[Great War]]. They survived the [[Conclave War]] and the [[Blood Years]] in hiding, before emerging from the marginal lands in the low passes of the mountains, and now largely live in the forests east of the [[Blackwater Fens]] and west of the [[Sentinel Range|Sentinels]]. 

Less isolated than the [[Ko'zula]], a number of Shu'anra familes have drifted south over the years, some settling as far south as the [[Elderwood]]. 

## Members of the Shu'anra Tribe

```dataview
TABLE WITHOUT ID file.link AS Person, affiliations AS Affiliations
FROM #person
WHERE contains(affiliations, this.file.link) OR contains(affiliations.org, this.file.link) OR contains(affiliations, this.name) OR contains(affiliations.org, this.name)
SORT file.name ASC
```



%%^Campaign:none%%

Session notes:
- [[Session 52 (DuFr)]]: [[Ariel]] met the [[Dunmar Fellowship]] in the [[~Te'kula village~|Te'kula village]] and told [[Delwath]] stories of the northern Deno'qai and the [[Meswati]].
- [[Ariel]] is a Shu'anra woman whose home was in the [[Forest of Dreams]], between the Blackwater Fens and the [[Sentinel Range|Sentinels]], before settling with the [[Te'kula]]. Source: [[Ariel]].
- Ariel preserves stories of the Shu'anra surviving the [[Great War]], fleeing into the Sentinels during the [[Blood Years]], dragonfire from the sky, and later migration south for better prospects. Source: [[Ariel]].
- Ariel knows northern stories of [[Yezali]] and the lost tanshi called the [[Meswati]]. Source: [[Ariel]].

%%^End%%

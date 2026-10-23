---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the, boxInfo: "One of the <partOf:1UA>", wHome: ""}
tags: [ancestry, status/check/lint]
typeOf: tribe
partOf: Elderwood Tribes
name: "Baz'aku"
pronunciation: bahz-ah-KOO
whereabouts: Elderwood
dm_owner: none
dm_notes: none
POV: 1749
---
```taelgar-header
```

 %% Written from DR 1749 point of view %%

The Baz'aku are a [[Deno'qai]] tribe living on the edges of the [[Elderwood]], near the [[Chasa River Valley]]. Historically, they were traders and merchants and middlemen, acting as intermediaries between the [[Chardonian Empire]] and the [[Bek'eni]], [[Te'kula|Te'kula]], and other forest tribes, trading furs, rare herbs, and other forest products. Under [[Mezzar|Grimbaskal]]'s influence, the Baz'aku increasingly turned to raiding, targeting merchant caravans and Chardonian forester camps, and prompting Chardonian military buildup. Now, following [[Mezzar|Grimbaskal]]'s defeat, the tribe has fallen into conflict. While many Baz'aku wish to return to a peaceful coexistence with Chardon, a vocal faction sees profit in continuing to raid.

## Territory and Settlements

The Baz'aku live on the edges of the [[Elderwood]], south and west of the [[Kayan]], stretching to the edges of the [[Chasa]]. 

Like other [[Elderwood]] tribes, Baz'aku villages cluster around a central gathering hall and a green or clearing, with a scattering of buildings dispersed among cleared land and the nearby forest, which is tended with care to provide food, shelter, and defenses. The Baz'aku have stronger river connections than other Elderwood tribes, and settlements along the [[Kayan]] and the [[Chasa]] keep docks for boats and rafts, including large dugout canoes hewn from single trees.

The Baz'aku are among the larger of the Elderwood tribes, and historically the most prosperous. There are at least ten large villages of a few hundred people each, and numerous smaller villages that consider themselves part of the Baz'aku tribe. 
 
## Local Culture

[[On the Lost People of the Forests|Older Chardonian accounts]] describe the tribe as traders and intermediaries: gatherers of forest wealth, including timber, crafted wood, rare herbs, and the products of hunting, who exchange what the Elderwood provides for metalwork and goods from the river towns. 

More recently, under [[Mezzar|Grimbaskal]]'s influence, the Baz'aku began to see themselves primarily as warriors, fighting against the encroachment of Chardonian interests into the [[Elderwood]]. While a vocal minority of the tribe still believes in this warrior ethos, others push for a return to peaceful coexistence with [[Chardonian Empire|Chardonians]]. 

## Recent history

In 1748 DR, [[Mezzar|Grimbaskal]] was slain in the depths of the [[Elderwood]] by the [[Dunmar Fellowship]].   Among the Baz'aku, the end of Grimbaskal's influence has sharpened the debate over raiding and war, and strengthened those who argue for a return to trade and diplomacy along the [[Chasa River Valley]].

## Members of the Baz'aku Tribe
```dataview
LIST WITHOUT ID file.link
FROM #person
WHERE contains(affiliations, this.file.link) OR contains(affiliations.org, this.file.link) OR contains(affiliations, this.name) OR contains(affiliations.org, this.name)
SORT file.name ASC
```



%% *Preserving old DM notes for posterity*

## Interactions with Grimbaskal
 
This is the tribe that, when Gnaeus was here, had historically traded with Arendum, been merchants and middlemen between the Deno'qai people and the rest of the world. In the past 20 years, relations with Chardon have significantly soured, driven in part by Chardonian encroachment on Baz'aku territory, primarily for better old growth forest for timber, and in part by Baz'aku beligerence encouraged by Grimbaskal (who goes by Arenga, the spirit of vengeance, among the Baz'aku).
 
Grimbaskal trains giant apes, which he gives to the Baz'aku to assist in their raiding parties. In exchange, they give him tribute from raids, couched in terms of sacrifices to create power, and give promising young warriors into service. These warriors never return, but the Baz'aku are convinced this is a great honor and they are fighting with the gods for justice.
 
There are two factions within the Baz'aku - the war faction and the peace faction.
 
War faction under full sway of Grimbaskal, eager to escalate against Chardon, possessive of the giant apes, and generally believe the Te'kula have fallen into corruption and evil, they are isolationist and will not help with the coming struggle against Chardonian imperialism.
 
Peace faction, the few that remain, are wary of Grimbaskal. They remind the people that not long ago, the Chardonians and the Deno'qai and the Elves were close allies, and without Chardon's might the Deno'qai may have been completely wiped from the face of the Earth. Yes, be wary, watch for signs of imperial aggression, and defend our homes if need be. But if Chardon wants to trade instead of fight, we should embrace that. This faction also believes that the Te'kula are hiding for a good reason, although they are not sure what. Don't agree with the increasing demonization of the Te'kula.
 
## Interactions with the Party
 
In most cases, party should probably be led to the main village / "capitol" when they first meet the Baz'aku. Certainly if they aid the war party, they will be taken to "main" village. Can just narrate this, etc. Hidden paths through the forests, little prayers and burnt leaves as offerings. People dressed in hides, red/blonde hair, sometimes brown, generally worn long. Shields/spears with lots of color on the shields, but covered with dull leather when not in battle. Maybe some with face paint? Mix of skin colors, ranging from pale to olive/brown, but most tended towards a ruddy, light tan complexation.
 
Mostly will be happy to see elf, especially curious about where he is from and if the elves are coming back to the Elderwood ever. Depends of course on exact means of introduction.

%%

%%^Metadata:names:v1%%
- {"name": "Baz'aku", "language": "unknown", "pronunciation": "bahz-ah-KOO", "status": "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 snapshot of the Baz'aku after Grimbaskal's death in DR 1748, with earlier trade and raiding history; the preserved DM notes describe the earlier period of his influence.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Quoted the display template containing a colon so the existing frontmatter parses, then normalized field order without changing the template's value.
- Added persistent name metadata with the accepted pronunciation and migrated the legacy inline POV to `POV: 1749`, recording the post-Grimbaskal snapshot.
- Removed the duplicated “the” in the header and corrected plural “middleman” to “middlemen”.

### Validated judgments
- The visible account supplies a proportionate account of territory, settlements, commerce, factional divisions, and the aftermath of Grimbaskal's death.
- The ordinary historical-POV comment is editorial guidance. The preserved DM section was reviewed separately from local-only evidence; local recoveries remain in the private handoff and do not change `dm_notes: none`.

### Open findings

- [ ] **Suggestion — editorial.shared_material_redundant:** In the comment headed “Preserving old DM notes for posterity”, the opening historical-trade account and the statement “There are two factions within the Baz'aku - the war faction and the peace faction” repeat the visible introduction and Local Culture section. Retain the archival intent while separating repeated reference facts from distinct earlier-period DM guidance. Bounded proposal: replace the repeated trade-and-faction summary with “Historical trade and the war/peace division are summarized in the visible article above; the following notes preserve earlier DM context.” Keep the remaining distinct private guidance and encounter possibilities hidden and explicitly historical; do not promote them automatically.

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Elderwood Arc NPCs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part II Finding the Te'kula/Arendum (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part II Finding the Te'kula/Baz'aku (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part II Finding the Te'kula/Flowchart - Elderwood Part 2]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part II Finding the Te'kula/Tinitaka (Elderwood)]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
%%^End%%

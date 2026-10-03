---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: lizardfolk
ancestry: null
campaignInfo:
  - {campaign: dufr, person: Kenzo, date: 1748-09-30, type: met}
  - {campaign: dufr, person: Kenzo, date: 1748-11-04, type: last seen}
born: 1665
gender: male
activeYear: 1735
name: Elazar
whereabouts: Bedez
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Elazar
>[!info]+ Biographical Info
> a [[Lizardfolk|lizardfolk]], he/him
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by [[Kenzo]] on September 30th, 1748 in [[Bedez]], [[Orekatu]], the [[Far South]] %%^End%%
>> %%^Campaign:dufr%% Last seen by [[Kenzo]] on November 4th, 1748 in [[Bedez]], [[Orekatu]], the [[Far South]] %%^End%%

![[elazar-portrait.png|right|400]]A lizardfolk man in the prime of his life, a prophet, seer, and spirit guide who has deeply felt visions and exceptional perception into the spirit realms. A bit of an outcast in his village, seen as someone who sees trouble in everything.

%%^Date:1748%%
- (DR:: 1748). Elazar began to acquire a reputation as far-sighted and wise, after he warned of the troubles of the [[Azta Lekua]]. 
- (DR:: 1748-09-30). Elazar met [[Kenzo]] when [[Kenzo]] appeared in [[Orekatu]]. Taught [[Kenzo]] the lizardfolk language and introduced him to lizardfolk spiritual practices over the next month.

%%^End%%

%%^Campaign:None%%
## Relationships
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link FROM #person OR #organization  
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link) 
SORT choice(contains(file.tags,"organization"), "Organization", "Person"), choice(species, species, typeof)
```
%%^End%%


%% One Note

About 80, in the prime of his life, Elazar is a prophet, a seer, and a spirit guide. He has deeply felt visions, and exceptional perception into the spirit realms.
 
However, he is also something of an outcast in his village of [[Bedez]], and in Orekatu, and has a bit of a Cassandra-like reputation.
 
Not that he is not believed, not exactly. The nature of divination magic and the power of the ancestor's augury means that no one totally discounts him, and the village elders don't mistrust his words or anything.
 
However, he is always pushing for action, for forward momentum, while the elders counsel patience, balance is the action of years and decades, not moments.
 
## Notes / Info
 
Can tell Kenzo about lizardfolk life in Berdez and Orekatu; about the land, how it is ancient and the old ways still weigh on the land here, the visions of balance lost, of the fires below overwhelming the land.
 
Something was wrong with dinosaurs, must tell the elders.

%%

%%^Metadata:names:v1%%
- {"name": "Elazar", "language": "unknown", "pronunciation": "eh-LAH-sahr", "notes": "Proposed from the Lizardling Basque analogue in [[Languages]]: e as eh, both a vowels as ah, z as an unvoiced s, and a tapped final r; middle stress is a tentative practical choice, not an established Lizardling rule.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Elazar in the prime of his life; the dated entries record his growing reputation and teaching of Kenzo during that year.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected “the elders council patience” to “the elders counsel patience” within the existing comment.
- Added `knownTo: [dufr]`, a proposed pronunciation, and supported DR 1748 temporal metadata; normalized frontmatter.

### Validated judgments
- [[Session 57 (DuFr)]] supports his spiritual expertise, initially unheeded warning, and teaching of Kenzo; the visible note already captures the defining role and reputation change.
- Confirmed the positive dm_notes attestation against the supplied source clusters.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `eh-LAH-sahr` in `Metadata:names:v1`. The Lizardling Basque analogue in [[Languages]] informs eh, open ah vowels, unvoiced s for z, and a tapped r. Middle stress is provisional because no exact Lizardling stress rule is adopted. Accept it into frontmatter and mark the entry documented, or supply the intended form.
- [ ] **Suggestion — editorial.shared_material_redundant:** The “One Note” comment's opening two paragraphs (“About 80, in the prime of his life…” and “However, he is also something of an outcast…”) substantially repeat the visible description of his life stage, spiritual gifts, and outcast reputation. Remove those two duplicate paragraphs while retaining the distinct guidance beginning “Not that he is not believed…” and the subsequent “Notes / Info” material in the comment. This leaves one account of the public identity and preserves the private portrayal guidance; do not publish the remainder automatically.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The Relationships block uses `%%^Campaign:None%%`; the canonical private sentinel is lowercase `none`. Replace that opening marker with `%%^Campaign:none%%`, preserving the generated query and closing marker.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Kenzo Solo Arc/Prequel - Kenzo]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Kenzo Solo Arc/Session 1 - Kenzo]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Timelines - Solo Arcs]]
%%^End%%

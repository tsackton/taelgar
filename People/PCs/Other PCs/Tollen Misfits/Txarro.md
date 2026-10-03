---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: lizardfolk
gender: male
born: 1717
player: Tim Sackton
name: Txarro
pronunciation: CHAH-roh
whereabouts:
  - {type: home, location: Greywash}
  - {type: home, location: Tollen}
  - {type: away, start: 1740-10-05, location: Twilight Kingdom}
knownTo: [feywild]
dm_owner: player
dm_notes: none
POV: 1740
---
# Txarro
*(CHAH-roh)*
>[!info]+ Biographical Info  
> A [[Lizardfolk|lizardfolk]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[txarro.png|right|350]]Txarro was born in a small lizardfolk village along the Greywash. His community was fairly isolated, even from other lizardfolk, in a marshy curve about a day and a half walk from Tollen. The Greywash provided a rich abundance for his village, and as a child and young adult he rarely interacted with other species, preferring to wander upriver along the marshy banks of the river, searching for hidden life among the reeds and rushes. He discovered he had some skill with animals, and could often charm small birds into his hand, or convince the shy mammals of the riverbank to be still in his presence.

Over the years, he often wandered further and further afield, traveling for days along the Volta and its tributaries, exploring aimlessly, never sure what he was looking for. He learned to observe quietly, coax animals to do his bidding, and even began to sense the flow of extraplanar energy moving through Taelgar, experimenting with channeling the ambient [[soulstuff]] that accretes in small quantities to all sentient things. Slowly, through these experiments, he began to learn a bit of magic, and increasingly spent his time wandering, often venturing a week or more from home, sometimes to the dismay of the elders of his village who wished for him to contribute more productively to the community. %% Note: this is representing background: Perception, Animal Handling, and Magic Initiate (Druid)%%

A year or two ago, everything changed. Exploring several days upriver from Tollen along the eastern banks of the Volta, Txarro stumbled across an abandoned woodcutter's homestead, and was attacked by several cursed tree blights. He fled for his life, but soon found himself surrounded and outmatched. It was only the timely arrival of a (pair/trio) of adventurers from Tollen that saved him. 

The experience shook him. In gratitude, he promised to help these travelers however he could, and ended up agreeing to travel with them for the next three months. Three months turned to six, which turned to a year, as he realized he liked these people, and had found in this group of misfits and outcasts a community that had been missing all his life. He decided to move to Tollen and join this group, even though he disliked the noise and crowds of the city. 

This was not a popular decision with his village: the elders and his ancestors did not think it right for him to devote his talents to these strangers and not his own people. His parting was difficult, and some harsh words were said that he sometimes regrets. But for now, he continues, searching for something to give his life direction and purpose.

%%^Metadata:names:v1%%
- {"name": "Txarro", "language": "unknown", "pronunciation": "CHAH-roh", "status": "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740 pre-expedition backstory with earlier village life and the move to Tollen; the existing dated whereabouts adds the later Feywild journey, while the prose retains the earlier ancestor relationship.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added explicit `name: Txarro` and `knownTo: [feywild]`.
- Added documented name metadata from the existing pronunciation and a DR 1740 temporal frame.
- Corrected “has a child” to “as a child” and supplied “that” in the final relative clause.

### Validated judgments
- The two undated home entries validly encode origin and later home; the dated Twilight Kingdom entry already represents the expedition and was preserved.
- The inline background/mechanics comment remains DM-only.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The third paragraph still leaves the rescuer count as “(pair/trio).” [[Lost in the Feywild - Episode 01]] explicitly identifies Kaito and Tarek as the rescuers in Txarro's campfire account. Replace the bounded phrase “a (pair/trio) of adventurers from Tollen” with “[[Kaito Min]] and [[Tarek]], two adventurers from Tollen.” This resolves the unfinished defining relationship without changing the rest of his backstory.

- [ ] **Warning — coverage.later_material_change:** The final paragraph preserves the ancestors' disapproval, but [[Lost in the Feywild - Episode 07]] records their acknowledgment, through Txarro, that they had needed to let him go. This changes the central relationship without establishing that the living village elders have reconciled with him. Choose to update the article and POV, defer with a human-selected game-update tag, or intentionally keep the earlier snapshot. For an update, the smallest dated addition is:

```markdown
%%^Date:1740-10-06%%
During the events in the [[27th House]], Txarro's ancestors spoke through him and acknowledged that their efforts to keep him in the village had threatened to destroy the person they loved. They said they had needed to let him go.
%%^End%%
```

This visibility-changing block is a proposal only.
%%^End%%

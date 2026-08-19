---
activeYear: 1740
headerVersion: 2023.11.25
lintedAt: "2026-08-19T16:23:04-04:00"
lintVersion: "2.3"
tags: [person, status/check/lint]
species: orc
born: 1698
gender: female
image: nuzkar-small.png
name: Nuzkar
pronunciation: NUZ-car
whereabouts:
  - {type: home, location: Gorzum}
  - {type: home, location: Uzgukhar}
  - {type: away, location: Vindristjarna, end: 9999}
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: 1749
---
# Nuzkar
*(NUZ-car)*
>[!info]+ Biographical Info
> An [[Orcs|orc]] (she/her)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[nuzkar-potrait.png|right|320]]An orc scholar, loremaster, and archivist, seeking stories, rumors, and information about other free orcs, about how [[Thark]]'s enslavement works, and how to free more of her people. 

She has a twin sister, [[Aygul]], as well as a husband and large family in Uzgukhar. 

%%^Date:1748%%
Inspired by [[Riswynn]] and the [[Battle for Uzgukhar]] to rededicate herself to her childhood dream of doing more for all orcs who suffer, unfree, in [[Thark]]'s control. 
%%^End%%

%% notes
## History

Nuzkar and Aygul are 51 years old, born near Gorzum oasis, to relatively poor farmers. Their parents were both born chained orcs and both struggle. In their father, this manifested as nightmares, weeks sometimes in bed with migraines. In their mother, who was freed when she was 8, this manifests as violent outbursts, where she often has to be restrained. Despite this, the parents are fervant believers in Xurkhaz and envision there salvation will be in their children, born free and unchained and untouched by [[Thark]].

The twins are born first, then their three siblings, soon after. However, tragedy strikes when the twins are 8. They are at this point old enough to help out on the farm, and one afternoon when their father can't work due to his headaches, their mother goes into a rage and kills the three younger children.

After this tragedy, their mother goes to live with the Hezguli, a group that helps support orcs who struggle with being freed after birth, or that end up in situations like this. Their father is left to raise them, but his headaches and depression really don’t get better and they basically raise themselves. Still, their father each morning gets up and thanks the miracle of the cloak, because this is better. Having a wife who kills 3 of your kids- better than being chained. Having crushing headaches and nightmares 2-3 times a week? Better than being chained.

The twins grow close to each other in this time, both responding to the tragedy in different ways. Nuzkar wants to **understand**. How are orcs chained? Where did her parents come from (all she knows it that they are from the same horde). Aygul, on the other hand, just wants to learn to defend herself. She never wants to be in the position where someone else can hurt her

They bounce around orcish society for a while, eventually growing into adults. Nuzkar is the more outgoing one, and ends up meeting ~husband~, the 8th son of a large family who proudly traces their lineage back 10 generations, proclaiming they were part of the founding generation of Xurkhaz. They marry, have kids, and Nuzkar becomes fascinated by the histories her adoptive family tells. Nuzkar and her husband have a large family, the youngest of whom is an oldish teenage when Grash attacks

Much of the family ends up in war - by this time they are living in the capital and have some moderately promiment position

Nuzkar and Aygul both worry -- Aygul perhaps even joins up, despite being a bit on the older side, she is wiry and skilled with weapons and unarmed combat techniques. Both worry about the end of their people. Nuzkar, for much of her life, has felt like she could be doing more. The drive to learn/understand/help the chained orcs, and find more orcs to unchain/more People of the Rainbow who are lost kept being put aside due to the basic joy of her life, and the busy-ness of raising a family, etc

But something happens during the conflict with Grash - my original idea was a prayer but that doesn't really make sense here -- that inspires her to rededicate herself to this childhood dream of learning how [[Thark]] chains people and finding others

So when a flying ship appears, looking for a loremaster and archivist, and willing to carry her around the known world, she jumps

Her sister is eager to go with her -- Aygul has always been the type who would have gone into the world, but she would not leave her sister, even though her sister kept talking about exploring/looking for stories/etc

%%

%%^Metadata:names:v1%%
- {name: Nuzkar, role: primary, language: Orcish, pronunciation: NUZ-car, status: inferred, notes: pronunciation is documented; source language is inferred from her Orcish context}
%%^End%%

%%^Metadata:article:v1%%
mode: character reference with dated fact and shared development history
povNotes: "Accuracy range: approximately DR 1748–1749. The visible biography and Vindristjarna whereabouts fit Nuzkar's Dunmar Frontier involvement, while the rededication is explicitly bounded to DR 1748 and the commented history remains unfinished development rather than article prose."
%%^End%%

%%^Lint%%
## Taelgar note lint

### Open findings

- [ ] **suggestion — `frontmatter.deprecated_field`:** `activeYear: 1740` is obsolete. If it only meant “this article is useful around the current campaign era,” remove it because `POV: 1749` now records that viewpoint. If it was intended as publication gating, choose the appropriate Date block or `audience` rule instead; its original meaning is not mechanically recoverable.
- [ ] **suggestion — `whereabouts.temporal_start_unclear`:** The two undated homes are compatible with origin/family homes, and `end: 9999` is a supported ongoing-away sentinel, but the Vindristjarna entry has no start. If the Session 83 meeting marks the start of her travel, the copy-ready replacement is `{type: away, start: 1748-12-30, end: 9999, location: Vindristjarna}`; otherwise use the supported departure date.
- [ ] **suggestion — `editorial.shared_development_placeholders`:** The shared history still contains `~husband~`, an explicitly tentative causal idea, and unfinished sentences. These are development placeholders rather than cross-note factual conflicts; complete or clear them during human review.

### Applied changes

- Added `knownTo: [dufr]`, `POV: 1749`, current article metadata, migrated the name block to v1, and canonicalized the nondeprecated frontmatter.

### Validated

- Local hidden material supports `dm_notes: color`; no color-versus-important judgment is needed. The DR 1748 fact block remains properly bounded.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
displayDefaults: {endStatus: murdered by bandits}
tags: [person, status/check/lint]
species: lizardfolk
born: 1681
gender: female
died: 1719-10-27
name: Gentza
whereabouts:
  - {type: home, location: Ganboa}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1719
---
# Gentza
>[!info]+ Biographical Info
> A [[Lizardfolk|lizardfolk]] (she/her)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[lizardfolk-gentza.png|right|320]]An apprentice lizardfolk herbalist, said to be skilled at experimenting with remedies. She is a regular at the [[Cleenseau]] market where she sells herbal cures to humans, and is always interested in new maladies or remedies for them. She often sells to [[Mermin Stonebridge]], a budding halfling merchant.

%%^Date:1719%%
In October of 1719, she was working on a new remedy for stomach ailments in humans, which was unfortunately mostly causing, rather than curing, sickness in her early tests. She was murdered by [[Francois the Bandit|François the Bandit]] and his accomplices as part of the [[Attempted Poisoning of Cleenseau]], when she refused to accept their bribe to misuse a remedy of hers.
%%^End%%

%%^Metadata:names:v1%%
- {name: Gentza, language: unknown, pronunciation: GEHN-tsah, status: proposed, notes: "Proposal informed by the Basque analogue for Lizardling in Languages: hard g before e, e as eh, tz as a single ts sound, and final a as ah; light first-syllable stress is provisional. The name language and exact in-world phonology are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1719 portrait of Gentza as a working apprentice before her October 27 murder, followed by the dated account of her death; earlier apprenticeship and later consequences are not comprehensively described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected the objective typo "stomach aliments" to "stomach ailments."
- Added `knownTo: [clee]`, primary name metadata with a proposed pronunciation, `POV: 1719`, and temporal notes; normalized frontmatter.

### Validated judgments
- The note sufficiently identifies Gentza's work, local relationships, and defining fate; [[Cleenseau - Session 03]] and [[Attempted Poisoning of Cleenseau]] corroborate the murder investigation and misuse of her research.
- Preserved `dm_owner: mike` and `dm_notes: color`; the local DM-attestation review does not apply to that owner.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise `GEHN-tsah`. The [[Languages]] Basque analogue for Lizardling supports a hard g before e, e as eh, tz as a single ts sound, and final a as ah. The light first-syllable stress is provisional because exact in-world stress is not established. The name's language remains unknown; this is a contextual analogue-informed proposal. If accepted, copy it into frontmatter and mark the name entry documented.
- [ ] **Suggestion — temporal.date_block_precision:** The `Date:1719` block currently makes the October experiments and October 27 murder visible from the beginning of the year. The note itself establishes the month of the experiments and records `died: 1719-10-27`. For day-sensitive publication, change the opening marker from `Date:1719` to `Date:1719-10-27`, retaining both sentences and the closing marker unchanged. This makes the retrospective paragraph visible from her recorded death; no earlier exact date for the experiments is established. Apply only after approving the visibility change.
%%^End%%

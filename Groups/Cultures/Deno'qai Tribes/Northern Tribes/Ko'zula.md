---
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the, boxInfo: "One of the <partOf:1UA>", wHome: ""}
tags: [ancestry, status/check/lint]
typeOf: tribe
partOf: Northern Tribes
name: "Ko'zula"
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Ko'zula are one of the [[Northern Tribes|northern]] [[Deno'qai]] tribes, in the current day largely consisting of the descendants of the people who fled into the mountains to escape the ravages of the [[Great War]]. The Ko'zula live in the far north, in the mountains and cold forests of the [[Northern Sentinels]]; they have remained in the peaks and icy pine forests of the high slopes, where they have prospered in relative safety. Though they are largely isolated from other human cultures, including other [[Deno'qai]], they trade extensively with the [[stoneborn]] and [[dwarves]] of the [[Northern Sentinels]], and have adopted many of the stoneborn farming customs and magic for survival in the high alpine environments. 

The [[Forest of Nightmares]] lies on the western border of Ko'zula territory, and connections to the stories and history of the [[Great War]], including the lost tanshi known as the [[Meswati]], have long been part of their cultural and oral traditions. 

## Members of the Ko'zula Tribe
```dataview
LIST WITHOUT ID file.link
FROM #person
WHERE contains(affiliations, this.file.link) OR contains(affiliations.org, this.file.link) OR contains(affiliations, this.name) OR contains(affiliations.org, this.name)
SORT file.name ASC
```

%%^Campaign:none%%
### Notes

People:
- [[Balati]] was a Ko'zula Deno'qai hero of the [[Great War]]; his shield and armor were preserved by the Ko'zula. Sources: [[Balati]], [[Deno'qai Lynx Shield]], [[Deno'qai Scale Mail]].
- [[Ninu]] is chief of the largest Ko'zula village; [[Enon]] is Godcaller of the Ko'zula. Sources: [[Ninu]], [[Enon]].
- [[Jotha]] was born Ko'zula, served as scout and defender, and vanished after touching a shadow armband in DR 1743. Source: [[Jotha]].
- [[Iascaire]] is a Deno'qai druid and devotee of [[Istari]]. Source: [[Iascaire]].

Session notes:
- [[Session 53 (DuFr)]]: [[Delwath]] met a Ko'zula hunting camp led by [[Kaslan]].
- [[Session 53 (DuFr)]]: [[Zevi of the Ko'zula]] guided Delwath to the main Ko'zula village.
- [[Session 53 (DuFr)]]: [[Ninu]] told Delwath the story of the [[Meswati]], [[Cha'mutte’s Shadow Armband|shadow armbands]], the deathless warlock, and [[Jotha]]'s disappearance.
- [[Session 53 (DuFr)]]: [[Enon]] gave Delwath [[Balati]]'s [[Deno'qai Scale Mail]] and [[Deno'qai Lynx Shield]].
- [[Session 54 (DuFr)]] and [[Session 55 (DuFr)]]: Ko'zula forests and village served as safe return and rest points during the Meswati quest.
- [[Interlude (Delwath Postscript)]]: Delwath rested, celebrated, and communed with the [[Meswati]] at the Ko'zula village, learning local history and tanshi stories.

Open questions/comments:
- (From Mike): Not clear how many people are in this tribe or this territory
- (From Mike): Not clear if there are specific Ko'zula traditions

%%^End%%

%%^Metadata:names:v1%%
- {"name": "Ko'zula", "language": "unknown", "pronunciation": "koh-zoo-LAH", "status": "proposed", "notes": "Proposed from the tribe's Deno'qai context and the Hebrew branch of the Hebrew-or-Arabic analogue in [[Languages]]: hard k, o as oh, voiced z, u as oo, a as ah, and tentative final stress. The apostrophe marks a syllable boundary without an assumed extra consonant. An Arabic-informed penultimate-stress koh-ZOO-lah is also possible; the name's language, vowel lengths, and in-world stress are not explicitly recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern Ko'zula settlement, trade, and inherited traditions after the Great War; the hidden source notes include specific DR 1748 encounters without establishing a dated article-wide snapshot.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Quoted the displayDefaults boxInfo scalar to repair YAML and added name and temporal metadata.
- Removed the duplicated “the” from the information callout.

### Validated judgments
- The visible account sufficiently establishes the tribe's identity, alpine setting, trade, and traditions. The shared Notes block is a research index; incidental campaign events are not required cultural coverage.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The proposed reading `koh-zoo-LAH` uses the Hebrew branch of the Deno'qai Hebrew-or-Arabic analogue in [[Languages]]: hard k, full oh/oo/ah vowels, voiced z, and tentative final stress. The apostrophe is treated as a syllable boundary; it does not establish an extra consonant. An Arabic-informed `koh-ZOO-lah` is also possible. The name's language and exact in-world stress are unrecorded. Accept with `pronunciation: koh-zoo-LAH` and `status: documented`, or provide a correction.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Delwath Solo Arc/Prequel - Delwath]]
%%^End%%

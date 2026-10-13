---
headerVersion: 2023.11.25
lintedAt: "2026-10-13T12:24:51-04:00"
lintVersion: "3.5"
tags: [power, status/review, status/check/lint]
typeOf: archfey
gender: male
name: Lord Umbraeth
aliases: [Gloomshaper]
affiliations:
  - {org: Duskmire, type: leader, title: Master}
whereabouts:
  - {type: home, location: "Twilight's Grace"}
  - {type: home, location: Duskmire}
knownTo: [adma, clee, dufr]
excludePublish: [clee]
dm_owner: mike
dm_notes: important
POV: modern
---
# Lord Umbraeth
>[!info]+ Biographical Info  
> A [[Fey|fey]] (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% status/review ->  significant in multiple games (Addermarch, and especially Cleenseau) and page is currently very under-detailed for importance %%

![[Lord_Umbraeth_Potrait.png|right|320]]Lord Umbraeth, the Gloomshaper, is the ruler of [[Duskmire]].

%%^Metadata:names:v1%%
- {"name": "Lord Umbraeth", "language": "unknown", "pronunciation": "lord um-BRAYTH", "notes": "Cautious spelling-based proposal: Lord has its ordinary English reading; Umbraeth uses an unstressed um, ae as ay, final th as in thin, and stress on BRAYTH. Sylvan has no fixed real-world analogue, and no accepted pronunciation or source language for this name was located.", "status": "proposed"}
- {"name": "Gloomshaper", "role": "alias", "language": "Common", "notes": "Plain-English descriptive epithet; its Common form is inferred.", "status": "inferred"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern identification of the enduring ruler of Duskmire, supported in both the DR 1720s and DR 1740s; the visible article does not yet describe his earlier history or changing relations with neighboring realms.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- None.

### Validated judgments
- `status/review` is supported: [[Duskhounds]], [[Greymalkin's Story]], and [[Addermarch - Session 22]] establish a recurring power whose defining account is absent.
- The new Addermarch appearance corroborates his use of hunters; their particular pursuit belongs in the session record. The later shared encounter draft remains unplayed preparation.
- The broadly modern identification is compatible with the modern campaign sources. The two undated home entries encode origin and current home and do not themselves require invented move dates.

### Editorial assessment
**Underdeveloped** — The central gaps are his characteristic dealings and servants, his earlier relationship with Ethlenn and reported exile, and the conquest of the Refuge of the Gossamer Veil. A short sourced account of those dimensions is the smallest useful scope; the precise exile chronology remains unsettled.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The article identifies only the ruler of [[Duskmire]]. [[Duskmire]] describes his cruel, misleading bargains and former place in Ethlenn’s court; [[An Excerpt from On Creation and Destruction of Extra-Material Realms]] attributes his exile to the elves of [[Orenlas]]; [[Greymalkin's Story]] recounts his conquest of the [[Refuge of the Gossamer Veil]]; and [[Duskhounds]] identifies his hunters and enforcers. These describe the subject’s defining behavior, history, and reach rather than incidental party encounters. Bounded candidate: “Umbraeth delights in cruel sport and misleading bargains, honoring his agreements while concealing how unfair they are. The [[Duskhounds]] serve him as hunters and enforcers. He was once a powerful courtier of [[Archfey Ethlenn]]. An old account attributed to the elves of [[Orenlas]] says he was banished from [[Twilight's Grace]] for misdeeds among humans, and that [[Duskmire]] formed around his bitterness and envy. [[Greymalkin]] recounts that Umbraeth conquered the [[Refuge of the Gossamer Veil]], where [[Aelirios Sunblade]] fell.” Preserve the source attribution and existing publication exclusions; do not assign an exact exile date or turn provisional realm-expansion plans into history.

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry remains proposed. Review `lord um-BRAYTH`, preserving the current entry until acceptance. Its recorded derivation is a cautious spelling-based reading: ordinary English “Lord,” unstressed “um,” “ae” as “ay,” final “th” as in “thin,” and stress on “BRAYTH”; it is not an established Sylvan pronunciation. Accept by adding `pronunciation: lord um-BRAYTH` to frontmatter and setting the entry to `status: documented`, or supply the intended reading and update the entry accordingly.
%%^End%%

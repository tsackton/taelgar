---
lintedAt: "2026-10-20T07:49:48-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [object, status/check/lint]
typeOf: figurine
subTypeOf: magic
ancestry: fey
rarity: rare
image: "[[agata-obsidian-fly.jpg]]"
pcOwner: Wellby
ddbLink: https://www.dndbeyond.com/magic-items/4831-figurine-of-wondrous-power-ebony-fly
name: "Agata's Obsidian Fly"
whereabouts: Wellby
knownTo: [dufr]
POV: modern
---
```taelgar-header
```

%% there are many figurines of wondrous power across Taelgar, created via a variety of means. this is an example. these items are fairly easy to create, and while some may be unique others that are standard forms exist.%%
![[agata-obsidian-fly.jpg|right|400]]A sculpture of a small black obsidian fly, small enough to fit in the palm of a human hand. When a command word is spoken, it animates, turning into a giant fly; whoever summons it can speak the same word to turn it back into a figurine. The fly is hostile to anyone it does not recognize as its owner, and attacks immediately. It is kind of an asshole.

%%^Campaign:DuFr%%
The [[Dunmar Fellowship]] found this figurine on [[Agata|Agata Dustmother]] after [[Session 28 (DuFr)|defeating her]] in [[Shakun’s Wellspring]]. Despite several attempts, they have not been able to convince it to recognize a new owner. [[Session 34 (DuFr)|Was fed to a giant velvet worm]] in the [[Elven Arborea Workshop]], but survived. [[Wellby]] learned from [[Arryn]], the mirror wizard at the edge of the [[Outer Ocean]] that it cannot serve a new owner until its old owner is dead.
%%^End%%

%%SECRET[v2:29e63cb26c9e0c0a2ca6ff76c5c7e53b]%%

%%^Metadata:names:v1%%
- {name: "Agata's Obsidian Fly", language: unknown, pronunciation: "AH-gah-tahz ob-SID-ee-un FLY", status: proposed, notes: "The Agata component follows the still-proposed spelling-based reading in [[Agata]]: hard g, ah vowels, and initial stress. Obsidian Fly uses ordinary English sounds and stress. The full possessive rendering is proposed; no accepted pronunciation or name-language identification is established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference to the figurine's appearance and behavior; the campaign layer recounts its recovery and unsuccessful attempts to establish a new owner.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the recorded recovery and campaign interactions; normalized frontmatter ordering without changing existing values.
- Added persistent name metadata with a proposed full pronunciation and a modern article viewpoint with temporal interpretation.
- Corrected objective grammar: “whomever summons it” → “whoever summons it”; supplied the missing subject in “Despite several attempts, they have not been able…”.

### Validated judgments
- Reviewed the local-only SECRET block; its content and recovery proposal remain private.
- The figurine’s hostility and command-word dismissal are supported by [[Session 30 (DuFr)]]; [[Session 34 (DuFr)]] supports the velvet-worm episode.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or revise `AH-gah-tahz ob-SID-ee-un FLY` in `Metadata:names:v1`. The Agata component follows the still-proposed spelling-based reading in [[Agata]]: hard g, ah vowels, and initial stress; Obsidian Fly uses ordinary English sounds and stress. Neither an accepted Agata pronunciation nor the title’s source language is established. If accepted, mark the entry documented and copy the full pronunciation to frontmatter; otherwise supply the intended reading.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The campaign opening marker remains `%%^Campaign:DuFr%%`. [[Campaign Registry]] requires the canonical lowercase code. Replace only that marker with `%%^Campaign:dufr%%`, keeping its contents and closing marker. The visibility-sensitive change remains a human proposal.
- [ ] **Suggestion — editorial.public_material_candidate:** The ordinary header comment beginning “there are many figurines of wondrous power across Taelgar” contains a coherent account of the wider item class that is absent from visible prose. It is a shared editorial account, not independent canonical evidence. For human adoption, add: “Figurines of wondrous power are created by several methods across Taelgar; some are unique, while others follow standard forms.” This would situate this figurine within its wider class. Retain the comment’s unadopted claim about ease of creation as editorial guidance unless separately approved.
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: elemental
subspecies: djinn
gender: male
campaignInfo:
  - {campaign: grli, type: met, date: 1747-07-23}
name: Mehrangeesa
whereabouts:
  - {type: home, location: Sulmana}
  - {type: away, end: 1747-07-23, location: "Airion's Floating Tower"}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: modern
---
# Mehrangeesa
>[!info]+ Biographical Info  
> An [[Elementals|elemental]] ([[Djinn|djinn]]) (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Met by the [[Silver Tempests]] on July 23th, 1747 in [[Airion's Floating Tower|Airion’s Floating Tower]], [[Blacksilver Peak]], the [[Fiatara Mountains]] %%^End%%

Mehrangeesa is a djinni from [[Sulmana]], a city of the [[Elemental Plane of Air]]. He was imprisoned in [[Airion's Floating Tower]] for many years, and later returned to the Plane of Air after he was freed by the [[Silver Tempests]]. In gratitude for their aid, he assisted them in the [[Battle of Voltara|defense]] of [[Voltara]] against [[Grumella's Horde]]. 

%%^Campaign:none%%
## DM notes

- (DR:: 1747-07-23): The [[Silver Tempests]] found Mehrangeesa in [[Airion's Floating Tower]], restrained by enchanted manacles. He identified himself as a djinni from [[Sulmana]] and explained parts of [[Airion]]'s history and the politics around [[Zadkai]]. **Sources:** [[Great Library Session Notes - Arc 1]]; [[Airion Tower - DM Notes]].
- DM notes say Airion had captured and enslaved Mehrangeesa years earlier, using his magic to learn about the Plane of Air and power the tower. Mehrangeesa wanted freedom, a return home, and the breaking of wizardly power to enslave elementals. **Source:** [[Airion Tower - DM Notes]].
- After being freed, Mehrangeesa gave [[Aelar]] a wind-related blessing and disappeared. DM notes indicate that freeing him would close the portal in the tower and that he would warn the party against misusing elemental power. **Sources:** [[Great Library Session Notes - Arc 1]]; [[Airion Tower - DM Notes]].
- In Arc 2, [[Brelith]] contacted Mehrangeesa for help before the battle for [[Voltara]]. Mehrangeesa refused to fight directly, but sent a powerful wind that helped break the enemy arrow and manticore assault. **Source:** [[Great Library Session Notes - Arc 2]].

%%^End%%

%%^Metadata:names:v1%%
- {"name": "Mehrangeesa", "language": "unknown", "pronunciation": "meh-ran-GEE-sah", "notes": "Cautious spelling-based proposal: four syllables, hard g, ee as in see, and proposed stress on GEE. The Primordial entry in [[Languages]] has no determined analogue or pronunciation rules; elemental identity alone does not establish the name's language.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective account of Mehrangeesa's origin, captivity, and release, with his release and later aid to Voltara established in DR 1747; subsequent activities are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, added `knownTo: [grli]`, and canonicalized equivalent campaign codes.
- Added a proposed name pronunciation and a modern retrospective POV with DR 1747 event coverage.

### Validated judgments
- The visible origin, captivity, liberation, and aid provide a sufficient account of this minor ally.
- The local timeline cluster duplicates the shared session record and adds no recoverable material; dm_notes remains unchanged.
- Later shared Arc 6 planning leaves Mehrangeesa's role open and does not establish a change to this account.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed pronunciation `meh-ran-GEE-sah` in the primary name entry. This is a cautious four-syllable spelling reading, with hard g, ee as in see, and proposed stress on GEE. [[Languages]] explicitly leaves the Primordial analogue undetermined, so it supplies no stronger pronunciation rule. If accepted, copy it to frontmatter `pronunciation` and mark the entry `documented`; otherwise revise the proposal.

- [ ] **Suggestion — editorial.shared_material_redundant:** In the `Campaign:none` block, the first bullet repeats the public origin/captivity account and the last repeats his assistance at Voltara. Make a bounded split: remove those repeated summaries, retain their source pointers and distinct context, and leave the other private guidance in place. The optional public detail supported by [[Great Library Session Notes - Arc 2]] is: “At the [[Battle of Voltara]], his wind kept arrows from reaching the walls and grounded the attacking manticores.” This preserves the useful distinction in how he aided the defense without duplicating the visible history.
%%^End%%

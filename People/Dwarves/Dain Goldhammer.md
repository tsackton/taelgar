---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: dwarf
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-10-23, type: met}
born: 1704
gender: male
name: Dain Goldhammer
whereabouts:
  - {type: away, start: 1748-10-23, end: "", location: Illoria}
  - {type: home, start: "", end: "", location: Chardon}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Dain Goldhammer
>[!info]+ Biographical Info
> a [[Dwarves|dwarf]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on October 23rd, 1748 in [[Illoria]], the [[Nevos Sea]] %%^End%%

%% clean up whereabouts, add notes from OneNote %%

An adventurer, working for the [[Society of the Open Scroll]], funded by [[Fausto]]. Often travels with [[Dee Wildcloak]]. 

Part of the group that explored [[Stormcaller Tower]] and brought [[Hralgar's Eyes]] and the [[Binding Stones]] back to [[Chardon]].

%% One Note

**Trait (Aspiration):** to be famous, as discussed below
 
Dwarven Oath of Glory paladin, often found hanging out with Dee Wildcloak.
## Appearance
 
Young dwarf, strong build, buff and athletic. Braided blonde beard, long blond hair in a ponytail. Dresses in traveling clothes usually, or plate armor on adventures. Warrior caste.
## Mannerisms
 
Boastful, but kind of in an awkward teenage way in the sense that he is always like cutting into stories to talk about his deeds / adventures but in a way that often falls flat. But this comes across as charming not annoying, and there is something about him that holds your attention.
 
## Motivation
 
Dain wants to be famous. He grew up in Chardon and the tales the humans tell of the great heroes of the past age are all about humans and elves and even lizardfolk and stranger creatures but never really about dwarves. What’s worse is that the dwarven elders don't seem to care, they just tell their stories of ancient days and never give a second thought to the humans.
 
So he is adventuring to become the dwarven hero for the modern age, the larger-than-life figure dwarven children can look up to and recount the great deeds of Dain Goldhammer.
 
He thought working for the Open Scroll explorer's guild would give him opportunities for glory, but so far it has been disappointing. Fausto (his and Dee's patron) is too secretive, never boasts of their exploits, even asks them to slip in quietly when they return.

%%

%%^Metadata:names:v1%%
- {name: "Dain Goldhammer", language: "unknown", pronunciation: "DINE GOHLD-ham-er", notes: "Tolkien-inspired Dwarvish analogue from Languages; preferred ai diphthong as in eye, with pronounced d and n; English compound surname retained. DAYN is an alternative spelling-based reading, and no accepted in-world pronunciation is recorded.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 adventuring portrait, including the Stormcaller Tower expedition; the exact Illoria interaction and whereabouts chronology still need review.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent name and temporal-viewpoint metadata; unestablished name languages remain `unknown`.
- Added the campaign knowledge code supported by existing interactions or finalized session evidence.
- Canonicalized the existing campaign code in metadata and its generated header without changing the campaign scope.
- Corrected the unambiguous possessive typo “there stories” to “their stories” in the shared comment.

### Validated judgments
- The visible professional role and expedition identify the subject adequately; the developed hidden portrait remains a human adoption choice.
- `status/cleanup/metadata` is supported by the still-unresolved interaction/whereabouts chronology and is preserved.
- Confirmed local DM source matches support the existing positive attestation; no private source content was added to shared output.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise the proposed pronunciation `DINE GOHLD-ham-er` in `Metadata:names:v1`. The [[Languages]] Tolkien Dwarvish analogue motivates an ai diphthong as in eye and fully sounded d/n; the English compound surname is retained. DAYN is a plausible alternative from the unaccented spelling. These are analogue-informed proposals, not documented in-world phonology. On acceptance, set the entry to `status: documented` and copy the accepted primary pronunciation to frontmatter; no frontmatter pronunciation has been asserted.
- [ ] **Suggestion — editorial.public_material_candidate:** The shared “One Note” comment contains a developed appearance and aspiration that would make this adventuring contact easier to portray. Consider adopting only this public-safe subset: “Dain is a young, athletic dwarf with a braided blond beard and long blond hair worn in a ponytail. His boastful stories have an awkward charm. Raised in [[Chardon]], he hopes to become a celebrated dwarven hero whose deeds children will retell.” Retain the class/build and patron-related DM guidance separately; omit repeated appearance and aspiration text from the remaining comment only after adoption.
- [ ] **Warning — temporal.campaign_interaction_conflict:** The header and campaignInfo say the Fellowship met Dain in Illoria on DR 1748-10-23. [[Session 48 (DuFr)]] explicitly records meeting him in Chardon on DR 1748-08-22, while [[Scrying Delwath Oct 21]] describes an October 21–25 scrying observation at sea, without an exact day or identified island. Decide whether the October entry was meant as a scry or an additional meeting. The established meeting candidate is `{campaign: dufr, date: 1748-08-22, type: met}` with Chardon whereabouts covering that date; retain an October record only with its supported type, location, and precision. Update the generated header together with any accepted metadata change; do not infer an exact October location from the vision.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Chardon NPC Flowchart]]
%%^End%%

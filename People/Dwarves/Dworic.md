---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
ancestry: null
campaignInfo:
  - {campaign: dufr, person: Riswynn, type: met, date: 1748-08-25}
born: 1502
gender: male
name: Dworic
whereabouts:
  - {type: home, location: Ardith}
  - {type: away, start: 1575-09-19, end: 1748-08-26, location: Bleakhold}
  - {type: away, start: 1748-08-26, end: 1748-10-05, location: Dunmari Basin}
  - {type: home, start: 1748-10-05, location: Nardith}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Dworic
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by [[Riswynn]] on August 19th, 1748 in [[Bleakhold]], [[Morkalan]], the [[Shadowfolds]] %%^End%%

A dwarven smith, born in [[Ardith]] before the [[Great War]]. He was trapped there after the war, but rescued by an expedition sent from [[Nardith]] in DR 1575, led by [[Nora Silverspark|Nora]] Silverspark and [[Hagrim]] Firebrand. Trapped in the [[Shadowfolds]] realm of [[Bleakhold]] after the rescue mission failed. 

In DR 1748, he was freed from [[Bleakhold]] by [[Riswynn]] and her companions, after the [[Chalice of the Runepriest]] was recovered. He joined the [[Bleakhold]] refugees who traveled with [[Riswynn]] to [[Nardith]], and is now settled there. While time passes differently in the [[Shadowfolds]], the years were hard on those trapped there, and he looks his chronological age. 

He has a nervous habit of sharpening his sword to the point of there being no edge at all, which he has found hard to shake even after being freed from [[Bleakhold]].

%% Status note: Seems potentially complete, setting status tim to confirm %%

%%^Metadata:names:v1%%
- {"name": "Dworic", "language": "unknown", "pronunciation": "DWOH-reek", "notes": "Proposal informed by the Tolkien Dwarvish analogue in [[Languages]]: retain the dw onset, use a rounded oh vowel, clear ee for i, a hard final k for c, and initial stress. These are tentative adaptations, not adopted in-world sound rules; the name language is not established.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-DR 1748 portrait after Dworic settles in Nardith, with earlier captivity and rescue summarized; his later life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized frontmatter ordering and collection formatting.
- Added the primary name entry and persistent temporal coverage metadata.
- Added `knownTo: [dufr]` and `POV: 1748`; corrected “their being” to “there being.”

### Validated judgments
- The note sufficiently identifies Dworic’s origin, captivity, release, and settlement in Nardith.
- The late-1748 viewpoint preserves the article’s explicit current settlement; no visibility-changing date block was applied.
- The existing status reminder is preserved as editorial context without recreating a check tag.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name entry proposes **DWOH-reek**, informed by the Tolkien Dwarvish analogue in [[Languages]]: retain dw, use a rounded oh vowel and clear ee, read final c as hard k, and tentatively stress the first syllable. These choices are an adaptation, not adopted in-world phonology. If accepted, copy the proposed pronunciation to frontmatter and change the name entry to `status: documented`; otherwise revise the proposal and its derivation. The name language remains `unknown` pending evidence.
- [ ] **Warning — temporal.internal_conflict:** The generated header says Riswynn met Dworic on August 19th, 1748, but `campaignInfo` records `1748-08-25`; [[Session 56 (DuFr)]] places the Bleakhold visit on August 25th. Regenerate or correct the header to: “Met by [[Riswynn]] on August 25th, 1748 in [[Bleakhold]], [[Morkalan]], the [[Shadowfolds]].” The date has been left unchanged for human review.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The current value `color` may still represent remembered information or an off-vault source. Retain it if that attestation remains accurate; change it to `none` only if the owner confirms no useful private remainder.
%%^End%%

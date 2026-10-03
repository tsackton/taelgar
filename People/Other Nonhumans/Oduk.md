---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: demon
campaignInfo:
  - {campaign: dufr, date: 1748-04-12, type: Banished back to the Abyss}
gender: male
name: Oduk
whereabouts:
  - {type: home, location: Abyss}
  - {type: away, start: 1748-03-19, end: 1748-04-12, location: "Raven's Hold"}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: modern
---
# Oduk
>[!info]+ Biographical Info  
> A demon (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Banished back to the Abyss by the [[Dunmar Fellowship]] on April 12th, 1748 in [[Raven's Hold]], the [[Sentinel Range]] %%^End%%

Oduk is a demon created with the ability to corrupt animals into gnolls. 

%% Potentially one of the many spawn of Yeenoghu, the Demon Lord of Gnolls, but haven't decided about what demon lords exist in Taelgar particularly or if Yeenoghu is one of them %%

%%^Date:1748-03-01%%
He was summoned into the material plane, in the abandoned Dunmari stronghold of [[Raven's Hold]], in the spring of 1748, where he was charged by his summoner to spawn as many gnoll warbands as possible and release them into the Dunmari frontier. He was [[Session 11 (DuFr)|banished back to the Abyss]] by the [[Dunmar Fellowship]] in April, 1748 DR. 
%%^End%%

%%^Campaign:DuFr%%
Later, the [[Dunmar Fellowship]] learned he had been summoned with the aid of the [[Ivory Scroll Cap Vision|demonic summoning scroll]] provided by the hag [[Agata|Agata Dustmother]] as payment in exchange for the [[Scepter of Command]]. This was part of a complicated plan by the [[Fraternity of the Empty Moon]] to sneak into [[Tokra]] with a flood of refugees, and complete a ritual to summon the madness of [[Jinnik]] into the material plane using the [[Extraplanar Weak Point]] north of [[Tokra]], connected to [[Pandemonium]], as a focal point.
%%^End%%

%%^Metadata:names:v1%%
- {name: Oduk, language: unknown, pronunciation: OH-duhk, notes: "Cautious spelling-based proposal: two syllables with initial stress, long o in OH and a short uh vowel in duhk. No name-specific pronunciation or name-language evidence is established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern demon identity, with a dated DR 1748 summoning and banishment account; the existing date boundary needs refinement to avoid revealing those events prematurely.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting; added the explicit name and `knownTo: [dufr]` from the recorded campaign interaction.
- Added persistent name metadata with a proposed pronunciation, leaving frontmatter pronunciation unset.
- Added `POV: modern` and temporal coverage notes for the durable identity and dated DR 1748 account.
- Moved the word-separating space from inside the “demonic summoning scroll” link label to between the link and “provided.”

### Validated judgments
- [[Session 11 (DuFr)]] confirms the April 12, 1748 confrontation, and [[Fraternity of the Empty Moon]] confirms the March 19 summoning. [[Ivory Scroll Case]] corroborates the scroll exchange and refugee scheme.
- Matching local sources support the positive `dm_notes` attestation; their contents remain outside this report.
- The ordinary comment explicitly preserves an undecided origin, so it remains noncanonical and unchanged.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes `OH-duhk`, using a cautious spelling-based reading with initial stress, long o, and a short uh vowel in the second syllable. No established pronunciation or name-language evidence supplies a stronger basis. Confirm or replace the proposal; if accepted, add `pronunciation: OH-duhk` to frontmatter and set the name entry to `status: documented`.
- [ ] **Warning — temporal.date_visibility:** The `Date:1748-03-01` block exposes the summoning and April banishment before either happened: [[Fraternity of the Empty Moon]] dates the summoning to March 19, and [[Session 11 (DuFr)]] dates the banishment to April 12. For date-filtered publication, replace the opening marker with `%%^Date:1748-03-19%%`, close that block after the sentence ending “Dunmari frontier,” and place the following banishment sentence in a separate `%%^Date:1748-04-12%%` block. Preserve the prose and use the standard closing marker for each block. These visibility changes require human approval.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The final paragraph uses `%%^Campaign:DuFr%%`. Replace that opening marker with `%%^Campaign:dufr%%`, retaining the enclosed paragraph and its closing boundary. The existing visibility marker is preserved for human review.

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Oduk (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Raven's Hold Demon Roster]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Raven’s Hold Text]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Session 11]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Session 12]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Session 13]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Leveling Up]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Player Questions]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Leveling]]
%%^End%%

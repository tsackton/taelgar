---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-03-29, type: met}
  - {campaign: dufr, date: 1748-07-09, type: last seen}
born: 1722
gender: female
name: Callie Charmheart
affiliations:
  - {org: Charmhearts, type: primary}
whereabouts:
  - {type: away, start: 1748-03-19, end: 1748-03-19, location: "Raven's Hold"}
  - {type: away, start: 1748-03-28, end: 1748-04-07, location: Karawa}
  - {type: away, start: 1748-04-07, end: 1748-04-13, location: traveling to Tokra}
  - {type: away, start: 1748-04-13, end: 1748-07-18, location: Tokra}
  - {type: away, start: 1748-07-18, end: 1748-08-13, location: Tokra-Darba Road}
  - {type: away, start: 1748-08-13, location: Darba}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Callie Charmheart
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her), of the [[Charmhearts]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on March 29th, 1748 in [[Karawa]], [[Eastern Dunmar]], [[Dunmar]] %%^End%%  
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on July 9th, 1748 in [[Tokra]], [[Dunmar]] %%^End%%

One of the Charmhearts, a halfling family of long-distance merchants and traders, who make a living trading between [[Dunmar]] and [[Sembara]]. 

## Relationships
- [[Ander Charmheart]], younger brother and traveling companion
- [[Bree Charmheart]], grandmother and traveling companion
%%^Date:1748%%
- [[Garret Tealeaf]], occasional traveling companion 
%%^End%%

%%^Campaign:none%%
### Relationships
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person or #organization or #item")
				.where(f => util.isLinkedToPerson(f.file, dv.current().file))		
				.sort(f => util.s("<maintype:n>", f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```

%%^End%%

%% One Note

A halfling trader from Sembara, granddaughter of Bree and sister to Ander. Concerned about her brother, sees herself as the caretaker of the family.
 
Age: early 40s 
Current location (June 1748): In Tokra, with the rest of the Charmheart family, trying to find a cure for Ander's madness

  PC Interactions
 
Has spoken to Wellby a fair bit, and asked him for help. Disagreed with Bree, her grandmother's, decision to try to keep Ander's illness a secret.

%%

%%^Metadata:names:v1%%
- {"name": "Callie Charmheart", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Callie traveling with her brother and grandmother, with dated whereabouts through August; earlier and later family circumstances are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and recorded supported `knownTo`, a primary name entry, and `POV`/`povNotes`.
- Normalized the equivalent `Campaign:None` sentinel to `Campaign:none` and corrected `grandaughter` to `granddaughter` in the existing comment.

### Validated judgments
- Callie’s trading and family role is sufficient. Her ordinary given name is explicitly listed in [[Playing a Halfling]]; the complete readable name needs no pronunciation guide, and its source language is left unknown.
- Confirmed local-only evidence supports the positive `dm_notes` attestation; the relationship query remains an operational index.

### Open findings

- [ ] **Warning — temporal.internal_conflict:** The hidden `One Note` comment says “Age: early 40s” in its June 1748 portrait, but `born: 1722` yields about 26 in 1748. Confirm which value is intended. If the birth year is correct, the copy-ready comment correction is `Age: about 26 in DR 1748`; otherwise supply the intended birth year. Neither value has been changed automatically.

- [ ] **Suggestion — editorial.public_material_candidate:** The shared `One Note` passage describing Callie as concerned for Ander and as the family’s caretaker is a coherent public-safe characterization beyond the current kinship list. Consider adopting: “Callie sees herself as her family’s caretaker and is particularly protective of her younger brother, [[Ander Charmheart]].” Retain the unresolved age and any dated source notes separately in the comment; after adoption, remove the duplicated kinship/caretaker wording while preserving distinct editorial guidance. This is an adoption proposal, not established new canon.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Festival Visitors and NPCs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Individual Scenes]]
%%^End%%

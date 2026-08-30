---
headerVersion: 2023.11.25
lintedAt: "2026-08-28T16:53:46-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-03-29, type: met}
  - {campaign: dufr, date: 1748-07-09, type: last seen}
born: 1644
gender: female
name: Bree Charmheart
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
# Bree Charmheart
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her), of the [[Charmhearts]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on March 29th, 1748 in [[Karawa]], [[Eastern Dunmar]], [[Dunmar]] %%^End%%  
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on July 9th, 1748 in [[Tokra]], [[Dunmar]] %%^End%%

The matriarch of the Charmheart trading clan of halflings.

## Relationships
- [[Callie Charmheart]], granddaughter
- [[Ander Charmheart]], grandson
%%^Date:1748%%
- [[Garret Tealeaf]], occasional traveling companion
%%^End%%
%%^Campaign:none%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%



%% One Note

 
A halfling trader from Sembara, grandmother of Callie and Ander. Matriarch of the clan, concerned about trading and market access, doesn't want to get a reputation of bringing strange disease. But does care for her grandchildren.
 
Age: 110ish, old but hale
Current location (June 1748): In Tokra, with the rest of the Charmheart family, trying to find a cure for Ander's madness

PC Interactions
 
Was reluctant to speak with PCs and discuss Ander. But will be extremely grateful if they quietly heal Ander.

%%

%%^Metadata:names:v1%%
- {name: Bree Charmheart, role: primary, language: Common, status: inferred, notes: "Charmheart follows the plain-English Common naming pattern documented for halfling family names."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Bree as matriarch of the Charmheart caravan; earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added `knownTo: [dufr]`, a DR 1748 `POV`, and persistent name and temporal metadata.
- Normalized the legacy `Campaign:None` marker to `Campaign:none`.

### Validated judgments
- `Bree Charmheart` follows a plain-English Common naming pattern and does not need a pronunciation guide.
- Confirmed local-only evidence supports the positive `dm_notes` attestation; its contents remain private.
- The `Campaign:none` block is an operational relationship index rather than narrative material.

### Open findings

- [ ] **Suggestion — editorial.public_material_candidate:** The hidden `One Note` comment contains a coherent public-safe characterization that would make Bree more useful as a reference without exposing DM mechanics. Copy-ready candidate: `Bree is protective of the Charmhearts' reputation and reluctant to discuss Ander's illness with outsiders. Despite that caution, she is deeply concerned for her grandchildren.`

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Festival Visitors and NPCs]]
%%^End%%

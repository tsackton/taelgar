---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
gender: female
name: Callie Riverstone
affiliations:
  - {org: Riverstones, type: primary}
whereabouts: Aslain
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1720s
---
# Callie Riverstone
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her), of Riverstones  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[callie-riverstone.jpg|right|200]]A leatherworker specializing in fine colors.

%%^Campaign:Clee%%
Has a friendly relationship with [[Bartholomew Meeke]], who she hid for a time.  
%%^End%%


%%
Roleplaying Notes:
* The Riverstones are not otherwise used, and she is a bit odd and eccentric. Probably someone separated from her family or otherwise with something unusual in her background
* Older. Loves colors. 
%%

%%^Metadata:names:v1%%
- {name: Callie Riverstone, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the early-1720s portrait of Callie as an Aslain leatherworker, including her friendship with and sheltering of Bartholomew Meeke in DR 1720; earlier and later circumstances are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting and added the explicit name Callie Riverstone.
- Added knownTo: [clee], a minimal persistent name entry, and the supported early-1720s viewpoint.

### Validated judgments
- The leatherworking role and sheltering relationship make this a sufficient reference for a minor local contact; the ordinary displayed name needs no pronunciation.
- The roleplaying comment preserves an explicitly tentative background and characterization; it is not adopted as public biography.

### Open findings

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The relationship section begins with `%%^Campaign:Clee%%`; the canonical registry code is `clee`. Replace that opening marker with `%%^Campaign:clee%%`, retaining the existing boundaries and contents. This remains a proposal because campaign markers control filtered visibility.

- [ ] **Warning — coverage.established_fact_missing:** [[Cleenseau - Session 17 - Original]] describes the leatherworker sheltering the messenger as deeply distrustful of humans after the previous baron killed members of her family for uncovering his embezzlement. The session's prepared recap identifies that leatherworker as Callie, but her present note omits this consequential personal history. Confirm the family attribution before adopting the bounded addition: `Callie is wary of humans after members of her family were killed by the former Baron of Aveil for uncovering his embezzlement.` The shared notes in [[Merriweathers]] associate the killings with that family, while [[Riverstones]] leaves a possible connection undecided. Preserve the Riverstone identity and do not infer an unrecorded kinship; if the played recap conflates the families, record that attribution uncertainty instead of adding the sentence as settled fact.
%%^End%%

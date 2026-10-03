---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/ai, status/check/lint]
species: dwarf
gender: male
name: Kazak Ferrystone
affiliations:
  - {org: Ferrystones, type: primary}
whereabouts:
  - {type: home, location: Rinburg}
  - {type: away, location: on the road to Aslain, start: 1720-02-08, end: 1720-02-10}
  - {type: away, location: Aslain, start: 1720-02-10, end: 1720-03-10}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Kazak Ferrystone
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him), of the [[Ferrystones]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[kazak-ferrystone.png|left|200]]

Kazak Ferrystone is a dwarf of the [[Ferrystones]], based in [[Rinburg]]. While traveling to [[Aslain]] with [[Bolgrim Ferrystone]], he was badly injured by [[The Hunter|the Hunter’s]] bears. The [[Heroes of Cleenseau]] subsequently healed him.

In Aslain, Kazak and [[Vondal Ferrystone]] helped investigate the ruined [[Night Queen Temple (Aslain)|Night Queen temple]]. They identified the supposed necromantic chamber as recent, poorly built stonework inconsistent with the older temple.

%% Source discrepancy: [[Into Aslain (Email)]] identifies Kazak as the injured dwarf and Bolgrim as uninjured, while [[April Around Asineau]] attributes the injury and healing to Bolgrim. The DM confirmed that Kazak was the dwarf healed; this account follows that correction. Temple investigation: [[Cleenseau - Session 17]], with details preserved in its session recap. %%

%%^Metadata:names:v1%%
- {"name": "Kazak Ferrystone", "language": "unknown", "pronunciation": "KAH-zahk FAIR-ee-stohn", "notes": "Proposal informed by the Tolkien Dwarvish analogue in [[Languages]]: both a vowels are ah, k remains hard, z remains voiced, and initial stress is tentative; Ferrystone is read as the ordinary English compound. Exact in-world pronunciation and the name language are not established.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 portrait of Kazak based in Rinburg, including the bear attack and subsequent Aslain temple investigation; later life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized frontmatter ordering and collection formatting.
- Added the primary name entry and persistent temporal coverage metadata.
- Added the explicit name, `knownTo: [clee]`, and `POV: 1720`.

### Validated judgments
- The refreshed note’s full account and source-discrepancy comment are preserved, including the explicit DM correction identifying Kazak as the injured dwarf.
- [[Into Aslain (Email)]] supports the corrected injury attribution, and the Session 17 recap supports the temple investigation; the conflicting derivative injury attribution does not override the stated DM correction.
- The note is sufficient for Kazak’s supporting reference role. Contextual local `dm_notes` review is not applicable to `dm_owner: mike`.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name entry proposes **KAH-zahk FAIR-ee-stohn**, informed by the Tolkien Dwarvish analogue in [[Languages]]: a becomes ah, k stays hard, z stays voiced, and first-syllable stress is tentative; Ferrystone is the ordinary English compound. Exact in-world phonology is not recorded. If accepted, copy the proposed pronunciation to frontmatter and change the name entry to `status: documented`; otherwise revise the proposal and its derivation. The name language remains `unknown` pending evidence.
%%^End%%

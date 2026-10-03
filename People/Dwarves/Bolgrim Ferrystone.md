---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/ai, status/check/lint]
species: dwarf
gender: male
name: Bolgrim Ferrystone
affiliations:
  - {org: Ferrystones, type: primary}
whereabouts:
  - {type: home, location: Rinburg}
  - {type: away, location: on the road to Aslain, start: 1720-02-08, end: 1720-02-10}
  - {type: away, location: Aslain, start: 1720-02-10, end: 9999}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720s
---
# Bolgrim Ferrystone
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him), of the [[Ferrystones]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[bolgrim-ferrystone.jpg|left|200]]

Bolgrim Ferrystone is a dwarf of the [[Ferrystones]], based in [[Rinburg]]. He and [[Kazak Ferrystone]] were attacked by [[The Hunter|the Hunter’s]] bears while traveling to [[Aslain]]. Bolgrim escaped injury, while Kazak was badly hurt and subsequently healed by the [[Heroes of Cleenseau]].

In April DR 1720, Bolgrim brought Ferrystone masons and cartloads of stone to [[Asineau]] in gratitude. His cousin [[Roaric Ferrystone]] accompanied them to establish a smithy.

%% Source discrepancy: [[Into Aslain (Email)]] identifies Kazak as the injured dwarf and Bolgrim as uninjured, while [[April Around Asineau]] attributes the injury and healing to Bolgrim. The DM confirmed that Kazak was the dwarf healed; this account follows that correction. %%

%%^Metadata:names:v1%%
- {"name": "Bolgrim Ferrystone", "language": "unknown", "pronunciation": "BOL-grim FAIR-ee-stohn", "status": "proposed", "notes": "Proposed using the Tolkien Dwarvish naming analogue in [[Languages]] for Bolgrim, with a short o, hard g, and initial stress; Ferrystone follows its transparent English spelling. The complete name language and accepted pronunciation are unrecorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early DR 1720s portrait of Bolgrim based in Rinburg, with specific events in February and April 1720; later residence is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and recorded supported `knownTo`, a primary name entry, and `POV`/`povNotes`.
- Added the explicit display name and a proposed pronunciation.

### Validated judgments
- The account is sufficient for Bolgrim’s role. The authored DM correction identifying Kazak as the injured dwarf is preserved; its source-discrepancy comment remains useful provenance.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm `BOL-grim FAIR-ee-stohn` in `Metadata:names:v1`. The [[Languages]] Tolkien Dwarvish analogue informs a short o, hard g, pronounced consonants, and provisionally initial stress in Bolgrim; Ferrystone uses its transparent English spelling. The analogue supplies guidance, not exact adopted phonology. If accepted, copy `pronunciation: BOL-grim FAIR-ee-stohn` to frontmatter and set the entry to `status: documented`; otherwise revise the proposal.

- [ ] **Warning — temporal.internal_conflict:** The `whereabouts` entry keeps Bolgrim away in Aslain from 1720-02-10 through 9999, while the visible April paragraph and [[April Around Asineau]] place him in Asineau in mid-April 1720. Confirm a bounded Asineau visit and close or interrupt the Aslain entry accordingly; neither an exact arrival day nor a return date is established. A month-level candidate is `{type: away, start: 1720-04, location: Asineau}`, but review the intended date bounds before adopting it so the earlier Aslain stay is preserved.
%%^End%%

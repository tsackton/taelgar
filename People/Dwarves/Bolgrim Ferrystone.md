---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:24-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
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
- None.

### Validated judgments
- The existing DM correction identifying Kazak as the injured dwarf is consistent with [[Into Aslain (Email)]] and remains documented in the source-discrepancy comment. The April account is supported by [[April Around Asineau]] and [[Cleenseau - Session 29]].

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The existing pronunciation `BOL-grim FAIR-ee-stohn` in `Metadata:names:v1` remains `status: proposed`. Preserve its recorded derivation while a human accepts or revises it. If accepted, add `pronunciation: BOL-grim FAIR-ee-stohn` to frontmatter and set the entry to `status: documented`; otherwise revise the persistent proposal. The name language remains `unknown` pending evidence.

- [ ] **Warning — temporal.internal_conflict:** The `whereabouts` entry keeps Bolgrim away in Aslain from 1720-02-10 through 9999, while the visible April paragraph and [[April Around Asineau]] place him in Asineau in mid-April 1720. Confirm the end of the Aslain stay and the bounds of the Asineau visit, then replace the indefinite Aslain range with supported intervals while preserving the February history and Rinburg home. Exact travel dates are not established, so an exact-date YAML correction requires human input; a month-only start would not reliably encode the mid-April visit.
%%^End%%

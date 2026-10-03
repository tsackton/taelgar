---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
campaignInfo:
  - {campaign: dufr, date: 1748-08-06, type: met}
gender: female
name: Torgga Redpeak
affiliations:
  - {org: Redpeaks, type: primary}
whereabouts: Darba
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Torgga Redpeak
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (she/her), of the [[Redpeaks]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on August 6th, 1748 in [[Darba]], [[Dunmar]] %%^End%%

The matriarch of the Redpeak dwarves of [[Darba]].

%%^Metadata:names:v1%%
- {name: "Torgga Redpeak", language: "unknown", pronunciation: "TOR-gah RED-peek", status: "proposed", notes: "Analogue-informed adaptation of the Dwarvish guidance in Languages; exact name language and pronunciation are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Torgga’s matriarchal role and home in Darba as encountered in DR 1748; earlier and later tenure are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent name and temporal-viewpoint metadata; unestablished name languages remain `unknown`.
- Added `knownTo: [dufr]` and normalized the existing campaign code and equivalent block marker to `dufr`.

### Validated judgments
- The single-sentence matriarch identification is sufficient for this bounded person note; [[Session 46 (DuFr)]] substantiates the role. Confirmed local evidence supports the positive `dm_notes` attestation.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise `TOR-gah RED-peek` in `Metadata:names:v1`. The [[Languages]] Dwarvish analogue is Tolkien Dwarvish; the proposal retains audible t/r and a hard, slightly held double g, with a distinct final a and initial stress. The transparent surname uses “red-peak.” Exact vowel quality and stress are not supplied by the analogue, so this is a proposed adaptation, not established in-world phonology. On acceptance, mark the entry `documented` and copy the accepted primary pronunciation to frontmatter.
- [ ] **Warning — correctness.cross_note_conflict:** `campaignInfo` and the generated meeting line say August 6th, 1748, while [[Session 46 (DuFr)]] places the arrival in Darba and meeting with Torgga on August 8th. Confirm the chronology; the source-supported candidate is `date: 1748-08-08`, with the generated meeting line refreshed to “August 8th, 1748.” No date has been changed.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Darba/Darba (OneNote)]]
%%^End%%

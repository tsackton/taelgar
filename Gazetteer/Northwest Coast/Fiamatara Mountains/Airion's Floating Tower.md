---
headerVersion: 2023.11.25
lintedAt: 2026-08-19T22:25:06-04:00
lintVersion: "2.5"
displayDefaults:
  defArt: ""
  wCurrent: "<ancestry:UA> <typeof:UA> (current location: <current:1s>)"
tags:
  - place
  - status/gameupdate/gl
  - status/check/lint
typeOf: building
typeOfAlias: floating tower
name: Airion's Floating Tower
whereabouts:
  - type: home
    location: Blacksilver Peak
    end: 1748-01-11
  - type: home
    location: Blacksilver Peak
    end: 1748-01-11
dm_owner: tim
dm_notes: none
POV: 1748
---
# Airion's Floating Tower
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The floating tower of [[Airion|Airion Mistspeaker]]. For many years after the [[Great War]], it could be found on [[Blacksilver Peak]], in the [[Fiatara Mountains]], but it vanished in early DR 1748. 

%%
Major role in GL Arc 1, see especially: [[Airion Tower - DM Notes]]
%%

%%^Metadata:article:v1%%
mode: historical site snapshot
povNotes: "Accuracy range: DR 1748. The article describes the tower after it vanished from Blacksilver Peak; Great Library Arc 5 establishes its return to the Erbalta Plains by DR 1752."
%%^End%%

%%^Lint%%
## Taelgar note lint


- [ ] **suggestion — status.gameupdate_historical_snapshot:** `POV: 1748` makes the vanished-tower article a coherent historical snapshot, but [[Great Library Session Notes - Arc 5]] establishes that the tower had returned to the [[Erbalta Plains]] by DR 1752. If the snapshot is intended, a human may remove `status/gameupdate/gl`; otherwise add a dated/current update such as: `By DR 1752, reports placed Airion's Floating Tower on the Erbalta Plains again.`
- [ ] **warning — name.pronunciation_missing:** The inherited name `Airion` has no accepted pronunciation or established source language. A cautious spelling-based full-name proposal is `AIR-ee-onz FLOH-ting TOW-er`; no stronger analogue in [[Languages]] applies until Airion's linguistic origin is established. If accepted, copy `pronunciation: AIR-ee-onz FLOH-ting TOW-er`.

### Applied changes

- Normalized frontmatter order and collection formatting without changing parsed values.
- Added the note-specific `POV` field and persistent `Metadata:article:v1` interpretation required by linter 2.5.

### Validated

- Existing status tags were retained; their required human dispositions are listed above.
%%^End%%

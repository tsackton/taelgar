---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Ampelion River
aliases: [Revelwater, Everpouring Draught]
whereabouts: Emberwine
dm_owner: tim
dm_notes: none
POV: modern
---
# The Ampelion River
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Ampelion River, also known as the Revelwater or the Everpouring Draught, is a major river that runs through Emberwine. It is wide and slow-flowing, and typically navigated by large river barges. The water itself has the scent and appearance of wine, and the fey of Emberwine often drink its draughts. The effects of this fey wine on natives of the Material Plane -- if any -- are not recorded.

%%SECRET[v2:b1e2ffc5d24fe42d922ad4f8531d5a0d]%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: , map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Ampelion River", "language": "unknown", "pronunciation": "am-PEH-lee-on RIV-er", "status": "proposed", "notes": "Proposed from the lyrical Fey naming guidance in [[Languages]], which notes Classical Greek influence among existing Fey names but leaves the Sylvan analogue undetermined: ordinary m, p, l, and n; e as in bet; i as ee; separate final on; provisional stress on PEH; River retains its ordinary English reading. This is neither an established source language nor an accepted pronunciation."}
- {"name": "Revelwater", "role": "alias", "language": "unknown"}
- {"name": "Everpouring Draught", "role": "alias", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference geography and use of the river in Emberwine; the article does not establish the effects of a particular draught on a traveller.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter; added the explicit primary name and metadata for its two recorded aliases.
- Added a proposed primary-name pronunciation with derivation, a broadly modern POV and temporal note.
- Added the required two-entry waterway map skeleton, leaving both unknown locators blank.
- Corrected subject–verb agreement in “The effects ... are not recorded.” The substantive claim remains for human revision.

### Validated judgments
- [[Session 119 (DuFr)]] and [[Aenaphos]] corroborate the wine river and barge use; routine party travel has not been added to reference prose.
- The SECRET block was reviewed and preserved. Its private encounter draft has not been used as a public factual source or copied into this report.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The final public sentence says effects on Material Plane natives are not recorded, but [[Session 119 (DuFr)]] describes mortal travellers growing drowsy and mentally clouded while walking beside the river, under the combined warmth and intoxicating wine-scented air. Replace the no-record statement with: ‘Along the riverbank, the warmth and intoxicating wine-scented air can make travellers from the Material Plane drowsy and cloud their minds.’ [[Session 120 (DuFr)]] separately records that overindulgence in Emberwine's fey wine gradually erodes memories; it does not establish that a single draught of river water immediately causes memory loss. Keep that distinction if adding the latter information, and preserve any campaign knowledge restriction selected by the human.

- [ ] **Warning — metadata.names_unresolved_status:** The new primary name entry proposes `am-PEH-lee-on RIV-er`. The packet's [[Languages]] guidance leaves the Sylvan analogue undetermined, asks for lyrical names, and notes Classical Greek influence among existing Fey names, with Polynesian or Hawaiian only possible inspiration. This proposal uses ordinary m/p/l/n, e as in ‘bet’, i as ‘ee’, a separate final ‘on’, provisional stress on PEH and the ordinary English ‘River’. No name-specific language or accepted pronunciation was found. Confirm or replace the proposal; if accepted, copy it to frontmatter and mark the entry `documented`. The transparent English aliases need no separate pronunciation guides.

- [ ] **Warning — metadata.map_location_missing:** The required source and outlet entries are present but both `locator` values are blank. The consulted place and campaign records do not supply supported mapped endpoints. Have a human supply the appropriate map/locator for each endpoint; keep the existing typed skeleton until positions are known rather than guessing world hexes.
%%^End%%

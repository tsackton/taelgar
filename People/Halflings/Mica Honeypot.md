---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
gender: male
campaignInfo:
  - {campaign: dufr, person: Riswynn, type: met, date: 1748-05-31}
name: Mica Honeypot
whereabouts:
  - {type: home, location: Yuvanti Mountains, linkText: on the roads of, format: "<name:q>", startFilter: "1"}
  - {type: away, start: 1748-05-31, end: 1748-05-31, location: Yuvanti Mountains, alias: road between Tharn Todor and Nayahar, linkText: "on", format: "<name:q>", startFilter: "1"}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Mica Honeypot
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by [[Riswynn]] on May 31st, 1748 on the [[Yuvanti Mountains|road between Tharn Todor and Nayahar]] %%^End%%

Mica Honeypot is a halfling trader, and the husband and traveling companion of [[Jenny Honeypot]].

%%^Metadata:names:v1%%
- {name: Mica Honeypot, language: unknown, pronunciation: "MEE-kah HUN-ee-pot", notes: "Tentative adaptation of Mica using the provisional Halfling analogue in [[Languages]], with an ordinary English reading of the transparent surname; the complete name's language and exact pronunciation are not attested.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of Mica as a trader and Jenny Honeypot's husband and traveling companion, anchored by their DR 1748 encounter; earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Recorded `knownTo: [dufr]`, the late-1740s article viewpoint, and its supported temporal limits in `povNotes`.
- Added a primary name entry with a proposed pronunciation and `language: unknown` because the complete name's language is not attested.
- Normalized `DuFr` to `dufr` in campaign metadata and the existing campaign marker, preserving the campaign identity and audience.
- Corrected the header's ordinal from “May 31th” to “May 31st” without changing the date; quoted the existing `linkText: "on"` preposition to preserve it as text.

### Validated judgments
- The concise trading role and family relationship agree with [[Jenny Honeypot]] and [[Oskar in Tharn Todor]] and adequately identify this minor subject.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `MEE-kah HUN-ee-pot` for Mica Honeypot. The Halfling analogue in [[Languages]] is provisional: Igbo, but may change or be diverse. This proposed adaptation reads Mica's i as ee, c as k, and final a as ah; initial emphasis is a tentative reading aid, with no lexical tone asserted. The transparent surname retains its ordinary English reading. The complete name's language and exact pronunciation remain unattested. Accept or revise the proposal in `Metadata:names:v1`; on acceptance, change its status to `documented` and copy the accepted primary pronunciation to frontmatter.
%%^End%%

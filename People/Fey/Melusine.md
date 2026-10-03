---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: fey
subspecies: nymph
campaignInfo:
  - {campaign: dufr, type: met, date: 1748-11-15}
born: null
gender: female
name: Melusine
whereabouts: Amberglow
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Melusine
>[!info]+ Biographical Info
> A [[Fey|fey]] ([[Fey|nymph]]) (she/her)
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:DuFr%% Met by the [[Dunmar Fellowship]] on November 15th, 1748 in [[Amberglow]], the [[Feywild]] %%^End%%

A water nymph in [[Amberglow]]. She resides in a small, secluded grotto near a river, overgrown with vines and foliage. 

%%SECRET[v2:dc41ddc4626ec2c2a439355b65706d99]%%

%%^Metadata:names:v1%%
- {"name": "Melusine", "language": "unknown", "pronunciation": "meh-loo-SEEN", "notes": "Cautious spelling-based proposal using short meh, oo for u, s as s, and stressed seen for sine; [[Languages]] supplies no fixed Sylvan analogue, and no name-specific pronunciation is recorded.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 snapshot of Melusine residing in her Amberglow grotto; the exact encounter date differs between the header and [[Session 67 (DuFr)]].
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` and normalized its campaignInfo code.
- Added a proposed pronunciation and DR 1748 temporal metadata; normalized frontmatter.

### Validated judgments
- Confirmed the positive dm_notes attestation against the supplied source cluster; reviewed the local-only SECRET block separately without promoting it.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `meh-loo-SEEN` in `Metadata:names:v1`: meh, an oo vowel, an s consonant, and final stressed seen are a cautious spelling-based proposal. [[Languages]] explicitly gives Sylvan no fixed analogue; its Greek examples and possible Polynesian or Hawaiian inspirations do not establish this name's pronunciation. Accept it into frontmatter and mark the entry documented, or supply the intended form.
- [ ] **Warning — campaign.encounter_date_conflict:** The campaignInfo date and generated header say November 15, 1748, but the Timeline of [[Session 67 (DuFr)]] places the water-nymph meeting on November 14 and the exit from the Feywild on November 15. Confirm the intended material-plane date. If following the session timeline, use `{campaign: dufr, type: met, date: 1748-11-14}` and update the displayed encounter date to November 14; retain the current date only with a documented reason for the distinction.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The header block uses `%%^Campaign:DuFr%%`; the canonical registry code is `dufr`. Replace that opening marker with `%%^Campaign:dufr%%`, preserving the enclosed text and closing marker.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Feywild (Session 61)/Session 61/Session 61]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Raw Notes - Agata Feywild]]
%%^End%%

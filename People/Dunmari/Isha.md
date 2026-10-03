---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, date: 1748-06-08, type: freed, format: "<met:u> <person:q> on <target> from <current:2>"}
born: null
gender: male
name: Isha
whereabouts:
  - {type: away, location: Mirror of Soul Trapping, end: 1748-06-08}
  - {type: home, location: Karawa, start: 1748-06-09}
knownTo: [dufr]
dm_owner: none
dm_notes: important
POV: 1748
---
# Isha
>[!info]+ Biographical Info
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Freed by the [[Dunmar Fellowship]] on June 8th, 1748 from the [[Mirror of Soul Trapping]], [[Karawa]] %%^End%%

A Dunmari man trapped for many years in the [[Mirror of Soul Trapping]] by [[Agata]]. Missing one eye, with gray hair, incoherent. Most recently under the care of [[Cintra]] after his ordeal. 

%%SECRET[v2:4364e7feceda6544a2a74f787ca9100d]%%

%%^Metadata:names:v1%%
- {name: "Isha", language: "unknown", pronunciation: "EE-shah", notes: "Proposed using the Hindi side of the Dunmari cultural guidance in [[Languages]]: initial ee, sh as one consonant, and final ah, with first-syllable emphasis. The name's language and exact vowel lengths are not independently established.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a June DR 1748 snapshot after Isha's release from the mirror and placement in Cintra's care; his condition and whereabouts after that period are not established here.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the established campaign interaction.
- Added a persistent primary-name entry with a proposed pronunciation; retained `language: unknown` because the name language is not independently documented.
- Added `POV: 1748` and a persistent explanation of the article’s temporal frame.
- Normalized frontmatter field order and collection formatting without changing existing values.

### Validated judgments
- Session 31 (DuFr) and Mirror of Soul Trapping Vision corroborate captivity, injury, liberation, and Cintra taking the freed prisoners into care.
- Confirmed subject-specific local evidence supports the positive `dm_notes` attestation. The SECRET block was reviewed separately.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary-name pronunciation `EE-shah` is a proposal. Proposed using the Hindi side of the Dunmari cultural guidance in [[Languages]]: initial ee, sh as one consonant, and final ah, with first-syllable emphasis. The name's language and exact vowel lengths are not independently established. Accept it by setting the name entry to `status: documented` and adding `pronunciation: EE-shah` to frontmatter, or supply the preferred pronunciation; leave the proposal open until then.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
%%^End%%

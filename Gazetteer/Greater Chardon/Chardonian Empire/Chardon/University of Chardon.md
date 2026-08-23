---
timelineDescriptor: University of Chardon
headerVersion: 2023.11.25
lintedAt: "2026-08-23T16:50:31-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: building
typeOfAlias: university
created: 939
name: University of Chardon
whereabouts:
  - {type: home, start: 980, location: Chardon}
dm_owner: tim
dm_notes: important
POV: modern
---
# The University of Chardon
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[university-of-chardon.png|600]]

The University of Chardon is a famous center of learning and teaching, renowned as one of the great centers of magical knowledge in the world. It occupies much of [[Precinct IV]] in Chardon, and is among the oldest and most powerful institutions in the city. The university is closely affiliated with the [[Great Library]], as well as the [[Hetaeri Magica]] and the [[Society of the Open Scroll]], but has its own independent rules and governance. 

*In the middle of the oldest part of Chardon, the towers and spires of the Chardonian Lecti, the halls and colleges that make up the University of Chardon, rise above the bustle of the students, faculty, tutors, and others, sharing the skyline with the towers of famous wizards dancing with subtle magic.*
## Facilities and Organization

### Undergraduate Lecti

The University is organized primarily into a series of undergraduate colleges, known collectively as the Chardonian Lecti, that employ masters to teach undergraduates. Each college, known as a lectum (plural: lecti), is functionally independent, maintaining their own hall, sometimes with student housing, and arranging their own source of funds to pay masters to teach. Funds come from diverse sources, including, but not limited to, student fees, the imperial state, rich benefactors, the temple, and endowments. The halls of the Chardonian Lecti are almost exclusively located in [[Precinct IV]], and tend to cluster around the prominent Great Library campus, with its massive spire, but there is no formal central organization that allots space, and competition among lecti for space, masters, and students is often contentious.

%% note
While the university controls the largest portion of land in the Academia Quarter ([[Precinct IV]]), it is somewhat disorganized as there is often considerable competition among the various halls and lecti for students and masters, and thus it generally wields less real political power than the Hetaeri Magica or the Great Library. The disorganization is probably subtly encouraged by the Imperial state to keep the University from becoming a major alternate power base.
%%

Architecturally, most lecti mimic the Great Library, with towers rising above the main building or building complex, which gives the university district a distinctive and impressive skyline. 

Some of the more famous lecti include [[Sibyl's Hall]], one of the original colleges of the University, and Maruso Lectum, endowed by and named after an extremely wealthy adventurer. 

%% note
The lecti are named XXX Hall or XXX Lectum. The halls are associated with various external orders, whether gods or something else, while the lecti are patronage based, although this is not a perfect rule.
%%
### Graduate Faculties

In addition to the undergraduate lecti, the University of Chardon has five graduate faculties: the [[Faculty of Magic]], the [[Faculty of Law]], the [[Faculty of Theology]] (which includes medicine and healing), the [[Faculty of History]], and the [[Faculty of Metaphysics]] (which includes supernatural and planar studies). These higher faculties are governed independently from the undergraduate lecti, with their own departmental facilities and policies.
### Governance

The University of Chardon operates under its original Drankorian Charter granted in DR 939, and thus claims to be above and outside the laws and politics of the current day city. Students who are accused of crimes are, according to the university, only able to be tried and punished by university courts (although the Imperial bureaucracy claims the ability to confine students to university grounds without trial, which is occasionally contentious).

The [[Hetaeri Magica]], which draws members from both the University of Chardon and the [[Great Library]], controls and propagates rules on the use of magic within [[Precinct IV]], the academic quarter of Chardon.
## History

- (DR:: 939): The University of Chardon is founded in Chardon on the authority of an Imperial Charter from Eiphis the Blind, the Emperor of Drankor.
- (DR:: 1065): The University of Chardon expands, absorbing many refugees from the destruction of Drankor during the [[First Plague|First Plague]].

%%^Metadata:names:v1%%
- {name: "University of Chardon", role: "primary", language: "Chardonian", pronunciation: "university of KAR-dohn", notes: "Latinate Chardonian reading for Chardon with an English descriptive frame.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern account of the university's organization and governance; its DR 939 founding and DR 1065 expansion are separate historical layers.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the missing comma after `[[Great Library]]` in the Hetaeri Magica sentence.

### Validated judgments
- `POV: modern` and the existing `povNotes:v1` accurately describe a broadly modern institutional account with separate DR 939 and DR 1065 historical layers.
- Newer-source candidates corroborate the university's academic role and relationships without establishing a separate material change to the institution.
- Confirmed local `_DM_` matches support the existing positive `dm_notes: important` attestation; their source links will be appended mechanically without exposing private contents.

### Open findings

- [ ] **Suggestion — frontmatter.deprecated_field:** `timelineDescriptor: University of Chardon` is deprecated and duplicates chronology already carried by `created: 939`, the History timeline, and persistent POV metadata. Candidate: remove `timelineDescriptor: University of Chardon` while retaining those current temporal fields.
- [ ] **Warning — metadata.whereabouts_conflict:** The sole whereabouts entry begins the University's Chardon location in DR 980, but `created: 939`, the visible founding history, and [[Chardon]] all place its founding in Chardon in DR 939. Candidate: determine whether DR 980 marks an undocumented relocation; if it does not, replace `{type: home, start: 980, location: Chardon}` with `{type: home, start: 939, location: Chardon}`.
- [ ] **Warning — metadata.names_unresolved_status:** The persistent `University of Chardon — university of KAR-dohn` entry remains `status: proposed`. Candidate: review the recorded Chardonian language and Latinate derivation, then either accept it by copying the full pronunciation to frontmatter and setting the entry to `documented`, or correct the proposal while preserving its derivation note.
- [ ] **Suggestion — editorial.shared_material_redundant:** The comment beginning `While the university controls the largest portion of land` substantially repeats the visible account of decentralized, contentious competition, while its claims about comparative political power and imperial encouragement remain unresolved. Candidate: remove the repeated explanation and retain only `%% Research before adoption: determine whether the University's fragmented governance limits its political power relative to the Great Library and Hetaeri Magica, and whether imperial policy encourages that fragmentation. %%`
- [ ] **Suggestion — editorial.public_material_candidate:** The comment beginning `The lecti are named XXX Hall or XXX Lectum` contains a coherent public-facing naming distinction absent from the article. Copy-ready candidate: Halls are generally associated with external orders, while lecti more often take the names of their patrons, though the distinction is not absolute.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Power Structures]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 48]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 49]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Elderwood Arc NPCs]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 125 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 126 - Brainstorming]]
%%^End%%

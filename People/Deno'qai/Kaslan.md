---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: "Deno'qai"
born: 1699
gender: male
name: Kaslan
affiliations:
  - {org: "Ko'zula", type: primary}
whereabouts:
  - {type: home, start: "", end: "", location: "Ko'zula village"}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Kaslan
>[!info]+ Biographical Info  
> A [[Deno'qai]] [[Humans|human]] (he/him), of the [[Ko'zula]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Kaslan is a middle-aged man, with long experience in woodcraft; he is leader of the hunting camp [[Delwath]] first found after arriving in the north. 

He has a long salt-and-pepper tangled beard, despite a bald head. He is a skilled archer, and tends to spend his time at camp fletching arrows or working on scrimshaw on a piece of mammoth tusk. Kaslan favors [[A'gaza]], the spirit of deer, reindeer, and caribou, who watches over the hunt and particularly likes offerings from the reindeer hunt, especially things carved from antler.

%%^Metadata:names:v1%%
- {name: Kaslan, language: "Deno'qai", pronunciation: kahs-LAHN, notes: "Proposed from the Hebrew or Arabic analogue in Languages: two open a vowels, unvoiced s, and final stress; approximate rather than established in-world phonology.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of Kaslan as a middle-aged Ko'zula hunting-camp leader; the dates when that role began or ended are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added `knownTo: [dufr]` from [[Session 53 (DuFr)]].
- Added the name proposal and a late-1740s temporal interpretation.
- Corrected the duplicated words “spend spends” to “spend”.

### Validated judgments
- `status/cleanup/metadata` is supported while the proposed pronunciation awaits human acceptance.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes `kahs-LAHN` for Kaslan. [[Languages]] gives Deno'qai a Hebrew or Arabic analogue: the proposal uses two open a vowels, unvoiced s, and final stress. This is an analogue-informed approximation, not recorded in-world phonology. Accept it by setting frontmatter `pronunciation: kahs-LAHN` and the entry to `status: documented`, or supply the intended pronunciation.
%%^End%%

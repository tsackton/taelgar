---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: "Deno'qai"
born: 1691
title: Chief
gender: male
campaignInfo:
  - {campaign: grli, type: met, date: 1747-11-21}
name: Hakar
affiliations:
  - {org: Raha, title: chief, type: leader}
whereabouts:
  - {type: home, location: Raha}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Chief Hakar
>[!info]+ Biographical Info  
> A [[Deno'qai]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:GL%% Met by the [[Silver Tempests]] on November 21st, 1747 in [[Raha]], the [[Highveil Forest]] %%^End%%

Hakar is the chief of [[Raha]], a [[Deno'qai]] village in the [[Highveil Forest]]. He represents the village in local councils and manages relations with outsiders who reach Raha. 

He is an older man, in his late 50s, with a graying beard, but still wiry and strong. He tends to dress in buckskin and furs and prefers practical clothes over elaborate dress. 

He is devoted to his village and community and concerned about Chardonian incursions. 

%%^Metadata:names:v1%%
- {"name": "Hakar", "language": "unknown", "pronunciation": "hah-KAHR", "notes": "Using the Deno'qai cultural context and the Hebrew-or-Arabic analogue in [[Languages]], this proposal prefers a Hebrew-like final stress: both a vowels as in father, plain h and k, and an audible r. The exact name language and in-world stress are unrecorded; an Arabic-informed first-stressed reading is also possible.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of Hakar as Raha's chief, with an approximate age description and a dated DR 1747 encounter; the beginning and end of his leadership are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [grli]` from the recorded campaign interaction and normalized frontmatter formatting.
- Added `POV: 1740s` and a persistent temporal-coverage note.
- Added a primary name entry with a proposed pronunciation and its derivation; retained `language: unknown` because the source language of the name is not recorded.
- Converted the Great Library campaign alias `GL` to its canonical code `grli` in `campaignInfo`.
- Corrected the ordinal typo “November 21th” to “November 21st.”

### Validated judgments
- [[Great Library Session Notes - Arc 3]] supports his leadership and concern about Chardonian incursions; [[Raha]] supports his local role.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation `hah-KAHR` for Hakar awaits human acceptance. Using the Deno'qai cultural context and the Hebrew-or-Arabic analogue in [[Languages]], this proposal prefers a Hebrew-like final stress: both a vowels as in father, plain h and k, and an audible r. The exact name language and in-world stress are unrecorded; an Arabic-informed first-stressed reading is also possible. Accept this form by setting the name entry to `status: documented` and adding `pronunciation: hah-KAHR` to frontmatter, or provide a corrected pronunciation.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated met-by header uses `Campaign:GL`; [[Campaign Registry]] defines the canonical value `grli`. The site builder’s `website/site_builder/comment_blocks.py` compares campaign identifiers directly after case-folding and does not resolve aliases, so changing this marker can change which exports display the line. Proposal for human approval: after confirming the intended Great Library export visibility, replace only `Campaign:GL` with `Campaign:grli` in that header marker, leaving the enclosed text and closing marker unchanged.
%%^End%%

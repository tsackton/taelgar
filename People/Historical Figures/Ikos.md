---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Chardonian
gender: male
died: 1
campaignInfo:
  - {campaign: GL, type: learned of, date: 1747-07-24}
name: Ikos
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: modern
---
# Ikos
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> %%^Campaign:GL%% Learned of by the [[Silver Tempests]] on July 24th, 1747 %%^End%%

Ikos was a Chardonian warrior who fought during the [[Great War]]. He is remembered among many [[Northerners|Northerners]] as the faithful friend and companion to [[Azzan]], another hero of the Great War. Though, as the Northerners tell it, this story has a tragic end: Ikos pleaded desperately with his fellow citizens for more Chardonian aid to the north in the aftermath of the Great War, but these pleas fell on deaf ears. Much of the north was swept away by the hobgoblin hordes.

History does not record precisely Ikos' fate, though many believe he died fighting to protect [[Amani]] with [[Azzan]].

%%^Metadata:names:v1%%
- {"name": "Ikos", "language": "unknown", "pronunciation": "EE-koss", "notes": "The Chardonian analogue in [[Languages]] is Italian or Latin with occasional Classical Greek loans. This proposal keeps the written k hard, reads i as ee and o as a pure short o, and stresses the first syllable of the two-syllable name. Exact in-world vowel length is unrecorded.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: modern retrospective account of Great War tradition and its aftermath; Ikos’s precise fate remains uncertain.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the primary name entry and the article’s POV and temporal-coverage note.
- Recorded supported campaign knowledge in `knownTo`.
- Corrected `[[Northerners|Northerner]]` → `[[Northerners|Northerners]]`; `Ikos plead desperately` → `Ikos pleaded desperately`; `hobgoblin hoards` → `hobgoblin hordes`.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The header uses `%%^Campaign:GL%%`, and `campaignInfo` uses `GL`; [[Campaign Registry]] resolves both to `grli`. Replace those two values with `grli` together, preserving the date and enclosed header text. This proposal leaves the existing campaign block unchanged until the representation is approved.

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `EE-koss`. The Chardonian analogue in [[Languages]] is Italian or Latin with occasional Classical Greek loans. This proposal keeps the written k hard, reads i as ee and o as a pure short o, and stresses the first syllable of the two-syllable name. Exact in-world vowel length is unrecorded. Confirm or revise the pronunciation, then mark the entry documented and copy the accepted primary pronunciation to frontmatter.
%%^End%%

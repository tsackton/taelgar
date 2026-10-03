---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: aberration
subspecies: beholder
died: 1748-03-17
campaignInfo:
  - {campaign: grli, type: killed, date: 1748-03-17}
name: Vilaxes
whereabouts:
  - {type: home, end: 1748-03-17, location: Goldpeak Mountain, alias: the lower Goldpeak ruins}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1748
---
# Vilaxes
>[!info]+ Biographical Info  
> An aberration (beholder)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:GL%% Killed by the [[Silver Tempests]] on March 17th, 1748 in [[Goldpeak Mountain|the lower Goldpeak ruins]], the [[Fiatara Mountains]] %%^End%%

Vilaxes was a beholder who made a lair in the dwarven ruins deep beneath [[Goldpeak Mountain]], below the surface mines. 

Vilaxes dreamed many dreams of aberrations emerging from the deeps, and believed himself destined to become one of the Great Old Ones who would usher in an era of nightmares he controlled. In order to transform himself, he enslaved the local kobold population and forced them to worship him, constructing a massive statue of melted treasure to herald his rise in power. 

In the spring of DR 1748, [[Cassia]], [[Alton]], and [[Brottor]], a small group of Chardonian adventurers, ventured into depths beneath [[Goldpeak Mines]]. Brottor was killed by aberrations; Cassia and Alton were found by the [[Silver Tempests]]. Together, they destroyed Vilaxes and his corrupted minions.

%%^Campaign:none%%

## AI Vault Summary

- The [[Silver Tempests]] encountered signs of Vilaxes while exploring lower [[Goldpeak Mountain]], including gibbering mouthers whispering his name, kobolds under his control, and a statue raised to his glory. **Source:** [[Great Library Session Notes - Arc 4]].
- (DR:: 1748-03-17): [[Adrik]] killed Vilaxes with Thunderbrand. [[Samso]] and [[Cassia]] died in the fight, but [[Brelith]] revived them. **Source:** [[Great Library Session Notes - Arc 4]].
- DM notes describe Vilaxes as a deranged beholder who dreamed of aberrations emerging from the deeps, believed himself destined to become one of the great old ones or elder evils, and used corrupted kobolds, minotaurs, dolgaunts, and frightened slaves as servants. **Source:** [[Goldpeak Mines - DM Notes]].
- DM notes place a grotesque statue made of melted treasure in Vilaxes's central sanctum and say the chamber writings heralded his rise. **Source:** [[Goldpeak Mines - DM Notes]].

%%^End%%

%%^Metadata:names:v1%%
- {"name": "Vilaxes", "language": "unknown", "pronunciation": "vil-AK-seez", "status": "proposed", "notes": "Cautious spelling-based proposal: initial v, short i and a, x as ks, final es as eez, and stress on the middle syllable; no established name language or pronunciation rule was found."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a retrospective DR 1748 account of Vilaxes in the lower Goldpeak ruins through his defeat on March 17; earlier history is not dated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, including the unambiguous `campaignInfo` alias to `grli`; added `knownTo: [grli]`, name metadata with a proposed pronunciation, and a DR 1748 viewpoint with temporal notes.
- Corrected the missing auxiliary in “Cassia and Alton were found by the Silver Tempests.”

### Validated judgments
- The public note gives a sufficient account of Vilaxes’s identity, ambition, control of the kobolds, and fate; [[Great Library Session Notes - Arc 4]] corroborates the central outcome.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes `vil-AK-seez`, a cautious spelling-based reading with short i and a, x as ks, final es as eez, and middle-syllable stress. No established name language or stronger pronunciation rule was found in the reviewed sources. Confirm or replace this proposal; if accepted, copy it to frontmatter and mark the entry documented.
- [ ] **Suggestion — editorial.shared_material_redundant:** The `Campaign:none` section titled “AI Vault Summary” substantially repeats the public account of Vilaxes’s lair, dominated kobolds, ambitions, statue, and defeat. Remove the repeated summaries, retaining the two source links ([[Great Library Session Notes - Arc 4]] and [[Goldpeak Mines - DM Notes]]) as a compact source-pointer comment. If the distinct remaining private minion guidance is useful, keep only that guidance in a separate bounded `Campaign:none` section; the ancillary combat details need not be added to the public reference note.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated header uses `Campaign:GL`; [[Campaign Registry]] specifies `Campaign:grli`. Replace the existing marker’s code with `grli` when regenerating the header; preserve the block’s boundaries.
%%^End%%

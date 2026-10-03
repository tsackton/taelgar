---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: "Deno'qai"
gender: male
campaignInfo:
  - {campaign: grli, type: met, date: 1748-02-01}
name: Izkir
affiliations:
  - {org: Bita, title: godcaller, type: member}
whereabouts:
  - {type: home, location: Highveil Forest}
  - {type: away, start: 1748-02-01, end: 1748-02-08, location: Zarnato, linkText: along the}
  - {type: away, start: 1748-02-09, end: 1748-02-18, location: Blackwater Fens}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Izkir
>[!info]+ Biographical Info  
> A [[Deno'qai]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:GL%% Met by the [[Silver Tempests]] on February 1st, 1748 along the [[Zarnato]] %%^End%%

Izkir is a Deno'qai godcaller from the [[Highveil Forest]], associated with [[Bita]], the tanshi of bears. He served as a guide and divine spellcaster during the [[Silver Tempests]]' campaign against [[Nymthrax]] in the [[Blackwater Fens]].

%% Note:  Izkir likely comes from the poorly developed [[Deno'qai]] communities of the [[Highveil Forest]], with [[Raha]] as a southern example. This appears to be the "middle tribes" area between the Elderwood Deno'qai and the [[Northern Tribes]], but no specific tribe name is established. Sources: [[Deno'qai]], [[Highveil Forest]], [[Raha]], [[Great Library Session Notes - Arc 4]]. %%

%%^Campaign:none%%

## DM notes

- (DR:: 1748-01-29): The [[Silver Tempests]] encountered Deno'qai scouts at a portage on the [[Zarnato]] while tracking the dragon that had displaced [[Bullywugs]] and threatened the Chardonian border. The Deno'qai council also wanted the dragon killed. **Source:** [[Great Library Session Notes - Arc 4]].
- (DR:: 1748-02-01): After council discussion along the [[Zarnato]], the party left with Izkir, heading for the [[Blackwater Fens]]. **Source:** [[Great Library Session Notes - Arc 4]].
- Izkir was specifically associated with [[Bita]], the tanshi of bears. **Sources:** [[Great Library Session Notes - Arc 4]]; [[Bita]].
- During the first fight with [[Nymthrax]], Izkir's magic hastened [[Adrik]] and [[Aelar]] as they attacked the dragon. **Source:** [[Great Library Session Notes - Arc 4]].
- After the dragon's death, Izkir thanked the party deeply and told them they would always be welcome among his people. **Source:** [[GL - Session 56 - DM Notes]].

%%^End%%

%%^Metadata:names:v1%%
- {"name": "Izkir", "language": "unknown", "pronunciation": "iz-KEER", "notes": "Using the Deno'qai cultural context and the Hebrew-or-Arabic analogue in [[Languages]], this proposal prefers a Hebrew-like final stress: initial i as in bit, z as in zoo, k as in key, and final ir approximately eer with an audible r. The vowel length and exact name language are unrecorded, so this remains a proposal.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Izkir's godcaller role is described from the late-1740s campaign era, with a retrospective account of the DR 1748 Nymthrax expedition; earlier and later life are not covered.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [grli]` from the recorded campaign interaction and normalized frontmatter formatting.
- Added `POV: 1740s` and a persistent temporal-coverage note.
- Added a primary name entry with a proposed pronunciation and its derivation; retained `language: unknown` because the source language of the name is not recorded.
- Converted the Great Library campaign alias `GL` to its canonical code `grli` in `campaignInfo`.

### Validated judgments
- [[Great Library Session Notes - Arc 4]] supports Izkir’s association with Bita and his role in the expedition against Nymthrax. No specific tribal identity is established; the existing editorial uncertainty is preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation `iz-KEER` for Izkir awaits human acceptance. Using the Deno'qai cultural context and the Hebrew-or-Arabic analogue in [[Languages]], this proposal prefers a Hebrew-like final stress: initial i as in bit, z as in zoo, k as in key, and final ir approximately eer with an audible r. The vowel length and exact name language are unrecorded, so this remains a proposal. Accept this form by setting the name entry to `status: documented` and adding `pronunciation: iz-KEER` to frontmatter, or provide a corrected pronunciation.
- [ ] **Suggestion — editorial.shared_material_redundant:** The third bullet under the `Campaign:none` DM notes repeats the public opening sentence’s identification of Izkir with [[Bita]]. Replace only that bullet with `- Sources for the public description: [[Great Library Session Notes - Arc 4]]; [[Bita]].` This preserves its provenance without repeating the public fact. Retain the distinct dated chronology and other private campaign guidance separately; no private guidance is proposed for public adoption.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated met-by header uses `Campaign:GL`; [[Campaign Registry]] defines the canonical value `grli`. The site builder’s `website/site_builder/comment_blocks.py` compares campaign identifiers directly after case-folding and does not resolve aliases, so changing this marker can change which exports display the line. Proposal for human approval: after confirming the intended Great Library export visibility, replace only `Campaign:GL` with `Campaign:grli` in that header marker, leaving the enclosed text and closing marker unchanged.
%%^End%%

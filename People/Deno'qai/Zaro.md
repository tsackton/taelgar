---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: "Deno'qai"
campaignInfo:
  - {campaign: dufr, type: met, date: 1748-09-06}
gender: male
name: Zaro
affiliations:
  - {org: "Bek'eni", type: primary}
whereabouts: "Bek'eni village"
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Zaro
>[!info]+ Biographical Info  
> A [[Deno'qai]] [[Humans|human]] (he/him), of Bek'ena  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on September 6th, 1748 in [[Talem|Bek'eni village]], the [[Elderwood]], [[Ainumarya]] %%^End%%

Zaro is an older man, hale and hearty with a commanding voice. He is bald, with a gray beard, blue eyes, and a prominent nose. He is the chief of the largest [[Talem|Bek'eni village]] in the [[Elderwood]]. 

%%^Campaign:dufr%%
Zaro was a loyal follower of [[Mezzar]], who he believed to be an elf seeking to return the [[Deno'qai]] to glory and power. His fate after the death of [[Mezzar|Grimbaskal]] is unknown. 
%%^End%%


%%SECRET[v2:40c42aa8dffbf2b90763994c7960db21]%%

%%^Metadata:names:v1%%
- {"name": "Zaro", "language": "unknown", "pronunciation": "zah-ROH", "notes": "Proposed from the Hebrew side of the Deno'qai analogue in Languages: z remains voiced, a is ah, o is oh, and final stress is preferred; the Arabic alternative gives no name-specific stress rule, so this remains tentative.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Zaro's village leadership and appearance are a September DR 1748 snapshot; the campaign passage looks back after Grimbaskal's death, when Zaro's own fate is unknown.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added `knownTo: [dufr]` from the recorded campaign interaction.
- Added persistent name metadata and a DR 1748 viewpoint distinguishing the observed chief from his unknown later fate.

### Validated judgments
- Confirmed local-only sources support the existing positive `dm_notes` attestation; their contents are not reproduced here.
- Reviewed the SECRET block separately; its material remains private and the uncertain fate is not resolved.
- [[Session 51 (DuFr)]] supports the village-leadership account. Its routine encounter details do not require a campaign log in this reference note.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation is `zah-ROH`, using voiced z, ah and oh vowels, and final stress from the Hebrew side of the Deno'qai analogue in [[Languages]]. The Arabic alternative does not establish this particular name's stress, and no accepted name-specific pronunciation was found. Accept it in frontmatter and mark the entry `documented`, or provide a correction.
- [ ] **Warning — identity.header_mismatch:** The header says “of Bek'ena,” while the affiliation metadata, visible prose, [[Bek'eni]], and [[Session 51 (DuFr)]] identify Zaro with the Bek'eni. Regenerate or correct that header phrase to “of Bek'eni”; preserve the existing affiliation metadata.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Elderwood Arc NPCs]]
%%^End%%

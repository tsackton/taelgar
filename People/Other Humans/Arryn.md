---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Tollender
campaignInfo:
  - {campaign: dufr, person: Wellby, type: "rescued from the [[Mirror Realm]]", date: 1748-11-13}
born: null
gender: male
name: Arryn of Tollen
aliases: [Arryn the Wanderer]
whereabouts:
  - {type: home, start: "", end: 1730, location: Tollen}
  - {type: away, start: "", end: "", location: Eastern Green Sea}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Arryn of Tollen
>[!info]+ Biographical Info  
> A [[Tollen|Tollender]] [[Humans|human]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% The rescued from the [[Mirror Realm]] by [[Wellby]] on November 13th, 1748 in the [[Eastern Green Sea]] %%^End%%

![[arryn-the-wanderer-portrait.png|right|400]]A wizard of significant power. Originally from [[Tollen]], but now dwells in a tower in the northern part of the [[Eastern Isles]]. Fascinated by other dimensions, recently the hypothesized [[Mirror Realm]] in particular. 

%%^Campaign:dufr%%
In the fall of 1748, vanished into the [[Mirror Realm]] after an experiment went wrong. Arryn was later freed by [[Wellby]], [[Alimash]], and [[Shoal]] during [[Session 60 (DuFr)|Wellby's adventures in the eastern Green Sea]]. After his rescue, he sent Wellby to the [[Feywild]] to reunite with the [[Dunmar Fellowship]]; [[Alimash]] joined Arryn's service.
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Arryn of Tollen", "language": "unknown", "pronunciation": "AIR-in uhv TOL-en", "status": "proposed", "notes": "Tollender context supplies the Tollish English analogue in [[Languages]]; proposed first-syllable stress, Arryn rhyming with Aaron, and Tollen with a short o and unstressed final syllable. The exact name language and pronunciation are unrecorded."}
- {"name": "Arryn the Wanderer", "role": "alias", "language": "unknown", "pronunciation": "AIR-in thuh WAHN-der-er", "status": "proposed", "notes": "Name attested in [[Session 66 (DuFr)]]. Uses the same proposed Tollish-English reading of Arryn as the primary form and the ordinary English epithet."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Arryn at his Eastern Isles tower, with his recent Mirror Realm research and the campaign account of his November rescue; earlier travels and later activity are not comprehensively described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the existing campaign interaction and the documented alias Arryn the Wanderer.
- Added persistent name metadata with proposed pronunciations and a DR 1748 POV and temporal interpretation.
- Normalized frontmatter and the existing `Campaign:DuFr` marker to canonical `dufr`, preserving its scope.

### Validated judgments
- Confirmed local DM sources support the positive `dm_notes` attestation.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or replace the proposed `AIR-in uhv TOL-en` and `AIR-in thuh WAHN-der-er`. [[Languages]] supplies an English analogue for the Tollish cultural context: the proposal uses initial stress, Arryn like Aaron, short `o` in Tollen, and the ordinary English epithet. The exact name language remains unknown. If accepted, copy the primary pronunciation to frontmatter and mark the entries `documented`.
- [ ] **Warning — link.incorrect_target:** The rescue paragraph links “Wellby's adventures in the eastern Green Sea” to [[Session 60 (DuFr)]], which covers the earlier escape from pirates; [[Session 66 (DuFr)]] records Arryn's rescue on DR 1748-11-13. Replace just that link with `[[Session 66 (DuFr)|Wellby's adventures in the eastern Green Sea]]`, preserving the sentence and campaign block.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Timelines - Solo Arcs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Session 1 - Wellby]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Session 2 - Wellby]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
%%^End%%

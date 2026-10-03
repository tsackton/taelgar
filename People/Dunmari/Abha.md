---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, type: met, date: 1749-02-02}
gender: female
image: abha-v2.jpg
name: Abha
affiliations: [Sonkar Mystai]
whereabouts:
  - {type: away, start: 1748-11-06, end: 1748-12-01, location: Nayahar}
  - {type: away, start: 1748-12-25, end: 1749-03-02, location: Copper Hills}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Abha
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on February 2nd, 1749 in the [[Copper Hills]], [[Dunmar]] %%^End%%

![[abha-v2.jpg|right|400]]Abha is a [[Sonkar Mystai|mystai of Sonkar]], a truthspeaker who has the divine ability to see the true nature of the world. She is a powerful spellcaster and is often called to resolve difficult or complicated requests for judgement and justice. 

Abha, like [[Sonkar]], sometimes appears cold and distant, but her isolating demeanor masks a deep concern for the world and for [[Dunmar]]. 

%%^Campaign:dufr%%
During the [[Sibling War]], Abha served as an ally and advisor to [[Nayan Karnas]], using her divine powers to attempt to disentangle the truth, or lies, of rumors of [[Agata]]'s influence on [[Sura]]. She was increasingly discredited by [[Nayan Karnas]] as he descended into paranoia, until the [[Dunmar Fellowship]] was able to at least partially get through to him. In the aftermath, she helped negotiate the end of the [[Sibling War]] between [[Sura|Nayan Sura]] and [[Nayan Karnas]]. 
%%^End%%

%%^Metadata:names:v1%%
- {name: Abha, language: Dunmari, pronunciation: "AH-bhah", notes: "Proposed from the Dunmari analogue in [[Languages]], preferring a Hindi-informed reading: long open ah vowels and bh as a breathy b; first-syllable emphasis is provisional. No accepted pronunciation is recorded.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740s portrait of Abha as a mystai, with a retrospective account of her mediation during the Sibling War. Original whereabouts qualifications are preserved: Nayahar end 1748-12-01, "#end is approx"; Copper Hills start 1748-12-25 and end 1749-03-02, "#start and end are approx".
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the recorded meeting and normalized frontmatter.
- Normalized `image` to the documented filename form `abha-v2.jpg`; the existing asset and body embed are unchanged.
- Added proposed name metadata and `POV: 1740s` with temporal guidance. Preserved the exact whereabouts estimate comments in `povNotes`, attached to their original locations and dates, so frontmatter can be normalized without losing uncertainty.

### Validated judgments
- [[Session 90 (DuFr)]] and [[Scrying Delwath Tollen Downtime]] support Abha's role in mediation; the reference account captures that central role.
- Confirmed local source matches support the positive `dm_notes` attestation; no private contents were incorporated.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation `AH-bhah` in `Metadata:names:v1` needs human acceptance. [[Languages]] gives Dunmari a Hindi or other Indo-Iranian (Persian) analogue; the preferred Hindi-informed reading uses long open ah vowels and `bh` as a breathy b, with provisional first-syllable emphasis. The analogue does not establish exact in-world phonology. If accepted, set `pronunciation: AH-bhah` in frontmatter and change the entry to `status: documented`; otherwise revise the proposal.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 111 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 112 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 113 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 114 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Timeline]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
%%^End%%

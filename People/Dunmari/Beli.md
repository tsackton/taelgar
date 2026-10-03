---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, type: met, date: 1748-03-22}
born: 1720
gender: female
name: Beli
affiliations: [Shakun Mystai]
whereabouts: Karawa
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Beli
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on March 22nd, 1748 in [[Karawa]], [[Eastern Dunmar]], [[Dunmar]] %%^End%%

An initiate of the [[Shakun Mystai]], a young woman skilled in healing and midwifery, with a hint of divine magic about her.

%%SECERT In Dec 1745, assisted in the birth of Cintra's daughter, [[Jumi]].  %%

%%^Campaign:dufr%%
In March 1748, helped the [[Dunmar Fellowship]] battle giant hyenas attacking Karawa. 
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Beli", "language": "unknown", "pronunciation": "BAY-lee", "notes": "Using the Dunmari cultural context and the Hindi-or-other-Indo-Iranian analogue in [[Languages]], this proposal prefers a Hindi-like reading: e is a clear eh/ay vowel without a strong English glide, i is ee, b and l retain their ordinary consonant sounds, and the first syllable receives light emphasis. A Persian-influenced beh-LEE reading is also possible; the exact name language is unrecorded.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Beli as a young Shakun initiate in Karawa; her later religious role and magical abilities are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the recorded campaign interaction and normalized frontmatter formatting.
- Added `POV: 1748` and a persistent temporal-coverage note.
- Added a primary name entry with a proposed pronunciation and its derivation; retained `language: unknown` because the source language of the name is not recorded.
- Corrected the ordinal typo “March 22th” to “March 22nd.”

### Validated judgments
- The current [[Dunmar Frontier - Session 01]] supports Beli’s role as a Shakun initiate and healer. The external local-source cluster supports the existing positive `dm_notes` attestation; no attestation change was made.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation `BAY-lee` for Beli awaits human acceptance. Using the Dunmari cultural context and the Hindi-or-other-Indo-Iranian analogue in [[Languages]], this proposal prefers a Hindi-like reading: e is a clear eh/ay vowel without a strong English glide, i is ee, b and l retain their ordinary consonant sounds, and the first syllable receives light emphasis. A Persian-influenced beh-LEE reading is also possible; the exact name language is unrecorded. Accept this form by setting the name entry to `status: documented` and adding `pronunciation: BAY-lee` to frontmatter, or provide a corrected pronunciation.
- [ ] **Error — privacy.secret_marker_misspelled:** The comment immediately after the opening paragraph starts with the misspelled marker word `SECERT`, which is an ordinary Git-shared comment rather than a recognized local-only secret marker. Confirm the intended privacy and, if local-only was intended, replace only `SECERT` with `SECRET` immediately after the opening percent signs, leaving the enclosed text and closing delimiter unchanged. This visibility-changing correction requires human approval.
- [ ] **Warning — coverage.established_fact_missing:** The opening description mentions “a hint of divine magic,” but [[Dunmar Frontier - Session 01]] records her repeated failure to call on that power during the March 1748 attack. Qualify the account so her magical ability is not left without this material limitation. A bounded addition within the existing campaign paragraph is: “Her divine magic failed during the fight, though she later treated the wounded with the temple’s red ochre healing paste.” The source establishes that event, not permanent loss of her powers.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 18]]
%%^End%%

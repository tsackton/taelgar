---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Mawaran
gender: male
name: Abelard
whereabouts:
  - {type: home, location: Chardonian Empire}
  - {type: home, start: 1737, location: Hamri}
knownTo: [mawar]
dm_owner: none
dm_notes: none
POV: 1747
---
# Abelard
>[!info]+ Biographical Info
> A Mawaran [[Humans|human]] (he/him)
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[abelard.png|right|300]]Abelard is a storyteller, singer, and tavern performer who hangs around the [[Leviathan Inn]] in [[Hamri]]. He is originally from a small town in the hinterland of the [[Chardonian Empire]], but has been a familiar presence in Hamri for the past ten years.

Abelard is a singer, gossip, and general hanger-on. He is known for extravagant stories of distant places, disasters, monsters, and improbable adventures, many of them likely embellished or wholly invented. But he tells his tales with a sharp wit and disarming smile, and his singing voice is strong. 

Abelard gives very little away about himself. He has no obvious steady work, beyond the coin from his performances, yet always seems able to pay his tab. He occasionally disappears for weeks or months at a time, returning with new stories but no clear account of where he has been, answering direct questions with more words than information. 

%%

Occasionally has been seen to cast a cantrip or two, and is probably a 1st level bard or so.

%%

%%^Metadata:names:v1%%
- {name: "Abelard", language: "unknown", pronunciation: "ah-beh-LARD", notes: "Proposed adaptation using the Mawaran Arabic cultural guidance in [[Languages]]: full ah vowels, an eh vowel for the written e, audible b/l/r/d, and stress on the final heavy syllable. This Chardonian-born man's name language is unestablished, so a different inherited reading remains possible.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1747 portrait of Abelard in Hamri; the relative phrase 'the past ten years' corresponds approximately to his recorded arrival in DR 1737, rather than to an advancing present.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized the existing campaign code to `knownTo: [mawar]`.
- Added a persistent primary-name entry with a proposed pronunciation; retained `language: unknown` because the name language is not independently documented.
- Added `POV: 1747` and a persistent explanation of the article’s temporal frame.
- Normalized frontmatter field order and collection formatting without changing existing values.

### Validated judgments
- Mawar Adventures Episode 03 corroborates his established role as a singer and rumor source; the routine conversation does not require an additional reference-note account.
- The two local evidence clusters offer no useful unshared addition, so `dm_notes: none` remains unchanged.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary-name pronunciation `ah-beh-LARD` is a proposal. Proposed adaptation using the Mawaran Arabic cultural guidance in [[Languages]]: full ah vowels, an eh vowel for the written e, audible b/l/r/d, and stress on the final heavy syllable. This Chardonian-born man's name language is unestablished, so a different inherited reading remains possible. Accept it by setting the name entry to `status: documented` and adding `pronunciation: ah-beh-LARD` to frontmatter, or supply the preferred pronunciation; leave the proposal open until then.
- [ ] **Suggestion — editorial.public_material_candidate:** The ordinary comment beginning “Occasionally has been seen to cast a cantrip or two” contains a definite observation alongside a tentative game-mechanical estimate. If adopted, the bounded public addition “Abelard has occasionally been seen casting a cantrip or two.” would make his minor magical abilities available in the reference portrait. Keep the tentative mechanical estimate in the existing nonpublic comment; do not promote that estimate or reorganize the comment automatically.
%%^End%%

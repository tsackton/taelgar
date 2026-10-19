---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:23:09-04:00"
lintVersion: "3.5"
tags: [event, status/check/lint]
typeOf: treaty
DR: 1429
name: Treaty of Wisford
whereabouts: Wisford
dm_owner: none
dm_notes: none
POV: modern
---
# The Treaty of Wisford
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Treaty of Wisford is a treaty signed by [[Derik I]] that established the [[House of Sewick]] and modern [[Sembara]]. 

%%^Campaign:None%%

Although no specific canonical details have been invented, the general idea is that this was the point at which the various independent duchies, including in particular Wisford and Brovna agreed to follow the Sembaran crown.

%%^End%%

%%^Metadata:names:v1%%
- {"name": "Treaty of Wisford", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective of the founding settlement of DR 1429; the date belongs to the event, while the article has no narrower current-state frame.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting; added the explicit subject name where absent.
- Added persistent name metadata and a modern retrospective POV with temporal coverage notes.

### Validated judgments
- The ordinary English title and readily readable Wisford component do not need pronunciation guidance.
- The legacy Campaign:None passage is explicitly tentative political planning, not adopted treaty terms. It was reviewed and preserved; its marker correction remains a proposal.
- The visible unification timeline and [[Derik I]] support the DR 1429 frame. The older DR 1428 narrative is inside an explicitly unfinished shared comment and is not adopted over the reference date.

### Editorial assessment
**Underdeveloped** — The note identifies the founding treaty but omits the joined crowns and participating authorities that explain its political settlement. A short, source-qualified account of that settlement would fill the central gap; a detailed invented constitution is unnecessary.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The one-sentence account does not explain what the treaty unified. The visible DR 1429 entry in [[Timeline of Sembaran History#The Unification]] names Derik I, the Duchess of Telham, and the Oracle of the Riven, and says the treaty confirmed the Joined Crowns; [[Derik I]] independently establishes his united rule of Sembara and Tyrwingha. Proposed addition: “The settlement confirmed the [[House of Sewick]] as rulers of the Joined Crowns of [[Sembara]], [[Tyrwingha]], and [[Duchy of Telham|Telham]]. The signatories included [[Derik I]], the Duchess of Telham, and the [[Oracle of the Riven]].” Confirm these details against the timeline’s review caveats before adoption; do not import its older hidden constitutional details or conflicting DR 1428 date.

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The private-planning wrapper is `%%^Campaign:None%%`; the adopted private sentinel is `%%^Campaign:none%%`. Replace only that opening marker after confirming the intended private visibility, keeping the planning text and End marker unchanged.
%%^End%%

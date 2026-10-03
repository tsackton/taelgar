---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
born: 1662
gender: female
name: Sabine de Brune
affiliations:
  - {org: Manor of Valit, type: leader, title: Castellan, end: 1720-02-15}
  - {org: de Brunes, type: primary}
whereabouts:
  - {location: Eskbridge, type: home, end: 1690}
  - {location: Valit, start: 1690, end: 1720-02-15}
knownTo: [clee]
dm_owner: mike
dm_notes: none
POV: 1720
---
# Sabine de Brune
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her), of the [[de Brunes]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% end date of Valit needs to be confirmed with session notes for Cleenseau - when she left Veltor %%

![[sabine-de-brune-valit.png|right|320]]Sabine de Brune was the castellan of the [[Manor of Valit]], a vassal of the [[Barony of Aveil|Baron of Aveil]], until her disappearance in early 1720. Organized about managing the manor, but with a soft spot for bardic tales and romance. Never married, although is rumored to have had several great loves in her youth. She was also the magistrate for the village of [[Valit]].

The de Brune family has long roots in the Enst river valley, and although [[Eskbridge]] is their primary area of operations, there are several outposts along the Enst including a longstanding one in the Cleenseau region. Recently, the family under [[Catherine de Brune]] has grown to include some more diverse mercantile interests in this region.

She was appointed as the castellan by [[Reginald Rusebek]] and still feels disgust and guilt that she was such a loyal supporter of his. She doesn't like to talk about baronial affairs much, and focuses on the village and doing her duties diligently. 

%%^Date:1720%%
In early February of 1720, she was summoned by [[Isabeau D'Aslain]] to [[Veltor]] and never returned to [[Valit]]. Although the reasons for her disappearance are unclear, rumors suggest that her health is poor and she returned to Eskbridge to die.
%%^End%%

%%^Campaign:clee%%
For much of the fall and winter of 1719, Sabine was the host to [[Istarias]], the Squire of the Whispering Wind, who was on a mission from his lord, [[Lord Serenveil]], to make sure Celyn made it to [[Cleenseau]] and stayed in the region. Who sent Istarias and why remains a mystery. 

Sabine and Istarias fled towards Tywingha after escaping from [[Areschera]] (who was really the one who had summoned them) with the help of the [[Merriweathers]] and the [[Heroes of Cleenseau]].
%%^End%%

%%^Campaign:none%%
Istarias was sent by his lord as a favor to [[Archfey Ethlenn]], who had a prophecy or foretelling that Celyn would save [[Elaine II]] if he grew attached to [[Cleenseau]].
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Sabine de Brune", "language": "Sembaran", "pronunciation": "sah-BEEN duh BRÜN", "status": "proposed", "notes": "The French strand of the Sembaran analogue in [[Languages]] gives Sabine ah and ee vowels, de a reduced duh, and Brune a rounded ü vowel with audible n and silent final e. Ü means an ee tongue position with rounded lips. This is analogue-based rather than adopted in-world phonology."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 portrait spanning her disappearance and escape; the subsequent resignation and return to the family estates are not yet incorporated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting; added supported name and temporal review blocks, `POV`, and `knownTo`.
- Normalized the existing campaign-block code from `%%^Campaign:None%%` to `%%^Campaign:none%%` without adding or moving content.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — coverage.later_material_change:** [[The Situation in Asineau (Email)]] establishes that by the party’s return around April 1, 1720, Sabine had resigned her post and returned to the de Brune estates near Eskbridge. The article stops at disappearance, rumor and flight toward Tyrwingha. Choose an updated account/POV, defer with a human-managed game-update tag, or preserve this earlier view intentionally. Candidate later sentence: “By early April 1720, Sabine had resigned as castellan and returned to the de Brune family estates near Eskbridge.” Preserve the earlier flight as an earlier stage rather than silently replacing it.

- [ ] **Warning — temporal.affiliation_end_unconfirmed:** The existing comment asks to confirm `end: 1720-02-15` against her departure from Veltor. [[Cleenseau - Session 18]] places her still in custody on February 20–21, while [[The Situation in Asineau (Email)]] establishes resignation only by early April. These are different transitions: departure from Valit, escape from Veltor, and resignation. Confirm which event each end field represents; do not mechanically change both affiliation and whereabouts to the escape date. Candidate comment clarification: “Confirm the final Valit residence date and the resignation date separately; escape from Veltor occurred later in February.”

- [ ] **Suggestion — identity.inconsistent_spelling:** The campaign paragraph says “Tywingha”; the established realm spelling is [[Tyrwingha]]. Proposed correction: “Sabine and Istarias fled towards Tyrwingha”.

- [ ] **Warning — metadata.names_unresolved_status:** The name-block pronunciation `sah-BEEN duh BRÜN` is proposed. The French strand of the Sembaran analogue in [[Languages]] gives Sabine ah and ee vowels, de a reduced duh, and Brune a rounded ü vowel with audible n and silent final e. Ü means an ee tongue position with rounded lips. This is analogue-based rather than adopted in-world phonology. Confirm it or supply the accepted full pronunciation before copying it to frontmatter and marking the entry documented.
%%^End%%

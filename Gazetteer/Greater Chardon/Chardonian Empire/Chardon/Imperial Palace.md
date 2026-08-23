---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T15:25:54-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/text, status/check/lint]
typeOf: building
typeOfAlias: palace
ancestry: Chardonian
name: Imperial Palace
whereabouts: Chardon
dm_owner: none
dm_notes: none
POV: 1749
---
# The Imperial Palace
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% to do, rewrite a bit to make less stilted and remove the shared comment %%

The Imperial Palace of [[Chardon]] crowns the [[South Bank]], occupying a prominent position among the city’s many towers and monuments. It serves as the [[Mitus Verina Auratan|Magistros]]’s seat and the administrative hub of the Empire’s heartland, receiving envoys, issuing decrees, and coordinating the defense and civic order.

Inside, the palace is a mix of grand, opulent halls used for state occasions, and inner passages that narrow toward working offices and the Magistros’ private spaces. The Magistros’ own chamber is kept austere and sunlit, favoring clarity and conversation over ornament. Colonnades, courtyards, and elevated galleries provide controlled movement between public audience spaces and secured inner wards.

%%
DM notes / sources
- Gazetteer/Chardon and South Bank pages: placement among landmarks; bridges and Vigiles on approaches; Magistros’ authority over Praecanti (Primis and Vigiles).
- Session 126 (DuFr): summons by Tiberius; gate protocol requiring surrender of weapons and foci; opulent halls; private chamber described as stark/sunlit; secrecy of orders; audience content (Fausto, chalyte, mission to Chataan Mountains).
- Worldbuilding/Staging/Dunmar Frontier/Praecanti Vigiles.md: Vigiles role; public vs. Primis distinction.
- Worldbuilding/Staging/Dunmar Frontier/Pandemonium Incursion in Chardon.md: context of unrest and emergency measures in 1749.
- Light extrapolation: courtyards/colonnades and division of public vs. secured inner wards are inferred from Chardon’s towered architecture and recorded audience logistics.

- [[Chardon]]; [[South Bank]]; [[Great Library]]
- [[Praecanti Vigiles]]; Praecanti Primis
- [[Mitus Verina Auratan]]; [[Tiberius]]

From campaign: Visitors surrender weapons and magical foci at the gates before guards escort them through opulent halls to private audiences. The Magistros's own chamber is stark, sunlit, and simply furnished
%%

%%^Metadata:names:v1%%
- {name: "Imperial Palace", role: "primary", language: "Common", status: "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 snapshot of the palace under Mitus Verina Auratan, including the audience spaces and security recorded during the Dunmar Fellowship's visit; earlier and later administrations are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- None.

### Validated judgments
- `status/cleanup/text` remains supported: the visible prose and its shared editorial comments still identify text and source-separation work for human review.
- Newer-source candidates were reviewed; they corroborate the palace's South Bank placement and DR 1749 framing without establishing a later material change.

### Open findings

- [ ] **Suggestion — editorial.reference_voice:** The sentences beginning `It serves as the Magistros's seat and the administrative hub` and `Colonnades, courtyards, and elevated galleries provide controlled movement` materially rely on generic institutional language and source-noted extrapolation. Preserve the established South Bank location, the Magistros's seat, the opulent audience halls, and the austere sunlit private chamber, but have a human rewrite or remove unsupported administrative functions, colonnades, courtyards, narrowing passages, galleries, and security zoning. A replacement is deliberately not supplied because this rule requires a human rewrite.

- [ ] **Suggestion — editorial.shared_material_redundant:** The long `DM notes / sources` comment substantially repeats the visible layout and audience details while mixing source provenance with explicit extrapolation. Replace it with a compact source-and-limits note, or remove the duplicated details while retaining distinct editorial guidance. Copy-ready candidate: `%% Sources and editorial limits
- [[Chardon]] and [[South Bank]] support the palace's skyline placement.
- [[Session 126 (DuFr)]] supports the gate protocol, opulent halls, and austere, sunlit private chamber.
- Courtyards, colonnades, narrowing passages, secured inner wards, and broader administrative functions are extrapolations rather than established facts.
%%`
%%^End%%

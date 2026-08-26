---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/gl, status/gameupdate/dufr, status/check/lint]
species: human
ancestry: Chardonian
gender: male
campaignInfo:
  - {campaign: grli, type: met, date: 1747-05-30}
name: Quintus Percomia
whereabouts:
  - {type: home, location: Voltara}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Quintus Percomia
>[!info]+ Biographical Info  
> A Chardonian [[Humans|human]] (he/him)
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Met by the [[Silver Tempests]] on May 30th, 1747 in [[Voltara]], [[Greater Voltara]], the [[Northern Provinces]] %%^End%%

Quintus Percomia is a wealthy caravan master and [[chalyte]] trader based in [[Voltara]]. He dresses well, and keeps his short black hair and beard neatly trimmed. 

His routes connect [[Voltara]] with [[Chardon]], carrying ore south and returning with grain, wine, salt, and other staple goods. He is known to purchase collectables, gems, and other valuables at times. 

%% Quintus will buy small, high-value goods, but typically underbids and tries to get great deals. Hates to pay full price but will if he highly desires item %%

%%^Campaign:none%%
## DM notes

- (DR:: 1747-05-30): The [[Silver Tempests]] met Quintus in [[Voltara]] as a traveling merchant, caravan master, and chalyte trader seeking adventurers to address trouble with centaurs. **Source:** [[Great Library Session Notes - Arc 1]].
- (DR:: 1747-06-06): The party returned to Quintus, [[Aglath]] apologized, and they learned more about the centaur trouble and cursed water. **Source:** [[Great Library Session Notes - Arc 1]].

%%^End%%

%%^Metadata:names:v1%%
- {name: Quintus Percomia, language: Chardonian, pronunciation: KWEEN-toos pehr-KOH-mee-ah, notes: "Proposed from Chardon's more Latinate Chardonian analogue: Latin-style qu as kw, final us in Quintus, and separately pronounced ia in Percomia; exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of Quintus's trade and business habits; his later circumstances are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added `knownTo: [grli]` and normalized the Great Library code in `campaignInfo` and the campaign header block.
- Corrected `A Chardonia human` to `A Chardonian human` in the header callout.
- Added persistent `Metadata:names:v1` metadata with a Chardonian language assignment and an analogue-derived pronunciation proposal.
- Added `POV: 1740s` and a `povNotes:v1` block describing the article as a late-1740s portrait.

### Validated judgments
- The matching local timeline material adds no useful information beyond the visible and shared record.
- The `Campaign:none` block is a source-linked campaign interaction record.
- `status/gameupdate/gl` and `status/gameupdate/dufr` are not assessable from the established evidence reviewed and were preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new `Metadata:names:v1` entry proposes `KWEEN-toos pehr-KOH-mee-ah` from Chardon's more Latinate Chardonian analogue: Latin-style *qu* as *kw*, final *us* in Quintus, and separately pronounced *ia* in Percomia. Exact in-world phonology is not established. If the proposal is accepted, add `pronunciation: KWEEN-toos pehr-KOH-mee-ah` to frontmatter and change the entry to `status: documented`; otherwise revise the pronunciation and derivation note.
- [ ] **Suggestion — editorial.public_material_candidate:** The shared comment `Quintus will buy small, high-value goods, but typically underbids and tries to get great deals. Hates to pay full price but will if he highly desires item` records a coherent business habit that would make this merchant more immediately reusable. Consider adopting: `Quintus is a shrewd buyer of compact valuables, usually offering below market value and paying full price only for items he especially wants.`
%%^End%%

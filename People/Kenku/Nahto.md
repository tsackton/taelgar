---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: kenku
ancestry: Islander
campaignInfo:
  - {campaign: dufr, person: Wellby, date: 1748-10-14, type: rescued, format: "<met:u> <person:q> on <target> from <current:3Frq>"}
born: 1700
activeYear: 1745
gender: male
name: Nahto
whereabouts:
  - {type: home, location: Wahacha}
  - {type: away, start: 1748-10-08, end: 1748-10-14, location: the aboleth lair east of Vermillion Isles}
  - {type: away, start: 1748-10-16, alias: sea elf village in Quanyi, location: Quanyi}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Nahto
>[!info]+ Biographical Info  
> An Islander [[Kenku|kenku]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Rescued by [[Wellby]] on October 14th, 1748 from the aboleth lair east of the [[Vermillion Isles]], [[Eastern Isles]] %%^End%%

![[nahto.png|right|400]]Kenku man in late middle age. Tinkerer, traveler, explorer; Nahto wanders over the islands of the Eastern [[Green Sea]] with his partner, Skoda. 

%%^Date:1748-10-14%%
In early October 1748, he was captured by a recently awakened aboleth and dragged to its undersea lair with Skoda. He was rescued, along with other captives, by Wellby and his companions on October 14, 1748. However, he suffered from the aboleth's curse, and could no longer survive without frequently being immersed in water. After repairing [[Wellby]]’s [[Kenku Glamoured Armor]] to restore its flight function, in gratitude for his rescue, he traveled with other victims of the aboleth to the sea elf village off the coast of Quanyi, where he remains a guest until a cure for the aboleth's curse can be found. 
%%^End%%

%%^Metadata:names:v1%%
- {name: Nahto, language: Kenku, pronunciation: "NAH-toh", notes: "Proposed from the Sioux analogue for Kenku in [[Languages]], using open ah and pure oh vowels, n and t as written, and h as a light breath before t. First-syllable emphasis follows the nearby accepted form MAH-kah in [[Makha]]; the broad analogue supplies no exact dialect or stress rule for this name.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740s portrait of Nahto in late middle age; the existing date block records his October 1748 rescue, curse, and refuge with the sea elves, without establishing a later cure.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the recorded rescue and normalized frontmatter.
- Added proposed name metadata and `POV: 1740s` with temporal guidance, preserving the existing dated account of the curse and refuge.

### Validated judgments
- [[Session 66 (DuFr)]] supports the rescue aftermath, lingering curse, sea-elf refuge, and armor repair already recorded here.
- Confirmed local source matches support the positive `dm_notes` attestation; no private contents were incorporated.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation `NAH-toh` in `Metadata:names:v1` needs human acceptance. The Sioux analogue for Kenku in [[Languages]] supports open ah and pure oh vowels; this proposal retains `n` and `t` and reads `h` as a light breath before `t`. First-syllable emphasis follows the local accepted form `MAH-kah` in [[Makha]], but the broad analogue establishes no exact dialect or stress rule for Nahto. If accepted, set `pronunciation: NAH-toh` in frontmatter and change the entry to `status: documented`; otherwise revise the proposal.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Session 1 - Wellby]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Session 2 - Wellby]]
%%^End%%

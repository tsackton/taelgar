---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:07:38-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [object, status/check/lint]
typeOf: material
ancestry: Skaer
name: Skaer Steel
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: modern
---
# Skaer Steel
>[!info]+ Information  
> ([[Skaer]] material)  
> `$=dv.view("_scripts/view/get_Affiliations")`

Skaer steel is a rare steel produced by secret means by the Skaer, using the heat of their volcanic islands and rare metals to create a material that is remarkably light and holds an edge exceptionally well.

A skilled smith can use Skaer steel to produce masterwork weapons, which are typically more accurate, more damaging, or both than normal weapons. 

%% mechanics from Dunmar game included as a comment here; these could potentially be refined

### Weapons
Example properties that can be added to weapons. Generally speaking, any weapon can have up to two properties. 

Basic properties for all weapons:
- Honed: A perfectly balanced weapon giving +1 to attack
- Keen: An exceptionally sharp or hard weapon, giving +1 to damage
- Masterwork (requires honed or keen): The weapon’s damage die increases one size. (For example, a halberd’s d10 damage die becomes a d12. A maul’s 2d6 damage dice become 2d8. If a die is already a d12, then add an extra 1d4 to damage rolls instead of increasing the size.) 

Additional properties for ammunition:
- Accurate: Ignore disadvantage when firing at long range. 
- Armor piercing (requires honed): Gain +1 to hit against armored targets
- Broadhead (requires keen): Do an additional 1d4 damage against unarmored targets

Additional properties for melee weapons:
- Light (weapons that lack the heavy property only): Gains the “finesse” property.
- Brutal (heavy weapons only): Attacks with this weapon score a critical hit on a roll of one lower than normal.

Additional properties that depend on damage type:
- Serrated (weapons that deal slashing damage only): When you score a critical hit with this weapon, the target loses 2d4 hit points at the start of their next turn.
- Weighted (weapons that deal bludgeoning damage only): When you score a critical hit with this weapon, you can choose to knock the target prone or push them up to 10 feet, as long as the target is no more than two sizes larger than you.
- Sharp (weapons that deal piercing damage only): If you make an attack roll with this weapon and miss by 1, the attack still deals half damage to the target.

### Shields and Armor

Shields and armor properties have a rating. The cost and time depends on the rating. Third-level ratings can only be applied to new items. Each shield or piece of armor can only have properties with ratings that sum to 3 or less. 

Example properties that can be added to armor:
- Agile (rating 1; armor only). Grants a +1 bonus to Dexterity saving throws
- Large (rating 1; shields only). Grants a +2 bonus to Dexterity saving throws against spells or harmful effects that target only you. 
- Spiked (rating 1; armor only). A creature that grapples you or you grapple takes 1d4 piercing damage at the start of your turns. 
- Sturdy (rating 2). Grants an additional +1 AC
- Parry (rating 2; shields only). When you take the Dodge action, you gain +2 to your AC until the start of your next turn. 
- Light (rating 2; armor only). If this armor would normally impose disadvantage on Dexterity (Stealth) checks, the light version of the armor does not. 
- Reinforced (rating 3; heavy armor only). Once per turn, you can reduce damage from an attack that deals bludgeoning, piercing, or slashing damage by 1d6

%%

%%^Metadata:names:v1%%
- {"name": "Skaer Steel", "language": "unknown", "pronunciation": "SKAIR STEEL", "status": "proposed", "notes": "Proposal uses the Norwegian branch of the Skaegish guidance in [[Languages]], treating ae as an ae/æ-like vowel, retaining sk and r, with ordinary English steel. A Finnish reading could separate a and e (SKAH-ehr); no exact Skaegish phonology or accepted pronunciation is recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference prose about Skaer production and the material's properties; the shared mechanics are preserved as Dunmar campaign guidance.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the explicit name and `knownTo: [dufr]` from the existing campaign evidence.
- Added persistent name metadata and `POV` with temporal coverage; normalized frontmatter order while preserving existing values.
- Corrected “A exceptionally” to “An exceptionally” in the existing mechanical comment.

### Validated judgments
- The visible account establishes the steel's producers, unusual manufacture, lightness, edge, and weapon use. The shared weapon and armor rules remain DM mechanics.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `SKAIR STEEL` in the persistent name block. No accepted pronunciation is recorded in [[Skaer]]. The proposal follows the Norwegian branch of the Skaegish analogue in [[Languages]] (“Finnish or Norwegian, with some Swedish influences”): it treats `ae` as an æ-like vowel rendered “AIR,” retains the written `sk` cluster and `r`, and uses ordinary English “steel.” A Finnish-oriented reading could instead separate `a` and `e`, approximately `SKAH-ehr`; the analogue does not settle exact Skaegish phonology. If accepted, set `pronunciation: SKAIR STEEL` and change the name entry to `status: documented`; otherwise supply the intended full reading.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-08-23T17:36:36-04:00"
lintVersion: "3.5"
displayDefaults: {boxInfo: ""}
tags: [group, status/check/mike, status/check/lint]
typeOf: army
typeOfAlias: warband
name: "Lord's Guard of Cleenseau"
whereabouts: Cleenseau
dm_owner: mike
dm_notes: color
POV: 1720
---
# The Lord's Guard of Cleenseau
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% see lint report to resolve errors; delete block and clear status/check/lint when finished%%

The Lord's Guard of Cleenseau is a troop of 18 people-at-arms who are responsible for protecting the [[Essford Manor]], watching the [[River Gate of Cleenseau|River Gate]] and [[North Gate of Cleenseau|North Gate]] and maintaining peace within the walls. These are not well trained, professional soldiers, but most of them can ride and shoot relatively well and have some practice with spears and wearing armor.

The guard is divided up into a household guard of 10, under the command of [[Ames Benthey]] and a town watch of 8, under the command of the sheriff [[Ysabel]]. The town watch is primarily responsible for guarding the [[River Gate of Cleenseau|River Gate]] and the [[North Gate of Cleenseau|North Gate]], and aides [[Nicholas Wysson|the magistrate]] when needed.

The household guard is responsible for the defense of the [[Essford Manor]], the personal safety of [[Wymar Essford]] and his family, and assists the town watch when needed.

The town watch is led by [[Beatrix Thorne]], and the current members are:
* [[Colin]], a guardsman
* [[Sarabeth]], a guardswoman
* [[Betsy Thorne]], a guardswoman
* [[Jon]], a guardsman
* Clarissa, a guardswoman, recently killed by zombies
* Jacques, a guardsman, recently killed by zombies

%%^Campaign:none%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {name: "Lord's Guard of Cleenseau", role: primary, language: Common, pronunciation: LORDZ gard of KLEN-sew, notes: "The title words follow their ordinary Common reading; the Cleenseau component uses the pronunciation documented in [[Cleenseau]].", status: inferred}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 snapshot whose leadership statements span incompatible states before and after the January undead attacks and require human reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- None.

### Validated judgments
- The `Campaign:none` block is an operational member index rather than narrative public material.
- Cleenseau campaign records corroborate the departure of most of the guard and [[Ames Benthey]], [[Robin of Abenfyrd]]'s appointment as acting captain, [[Ysabel]]'s death, and [[Beatrix Thorne]]'s later promotion.

### Editorial assessment

**Underdeveloped**. The visible article does not provide a coherent DR 1720 reference snapshot because its leadership, troop strength, and roster mix states from before and after the January departures and undead attacks.

### Open findings

- [ ] **Warning — coverage.later_material_change:** The article names [[Ysabel]] as sheriff, later calls [[Beatrix Thorne]] the current leader, still names [[Ames Benthey]] as household commander, and describes the guard as an eighteen-person troop even though campaign records establish major January DR 1720 changes. For a post-attack snapshot, use: `After [[Ames Benthey]] and most of the guard departed for [[Embry]] on January 3, [[Robin of Abenfyrd]] became acting captain. [[Ysabel]] was killed during the undead attacks, and [[Beatrix Thorne]] became sheriff on January 11.` Then reconcile the roster, troop strength, `POV`, and `povNotes` to that state; alternatively preserve a coherent earlier snapshot and use the applicable game-update status.
%%^End%%

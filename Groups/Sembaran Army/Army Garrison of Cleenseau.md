---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {partOf: "<typeof:Au> of <partof>", boxInfo: ""}
tags: [group, testcase, status/gameupdate/clee, status/check/lint]
typeOf: garrison
partOf: Dunfry Regiment
name: Army Garrison of Cleenseau
whereabouts:
  - {type: home, location: Cleenseau}
  - {type: away, end: 1720-01-10, location: Dunfry}
dm_owner: mike
dm_notes: important
POV: 1719
---
# The Army Garrison of Cleenseau

The Cleenseau Garrison is the furthest east-most garrison of the [[Army of the West]]. It is commanded by [[Ida Rosfeld|Captain Ida Rosfeld]] and consists of two patrols:

* The Bridge Patrol, responsible for the security of the bridge and the road, and for providing a reaction force that can march and respond to threats. The Bridge Patrol consists of approximately 20 soldiers, currently led by acting sergeant [[Ancer Benthey]]. Its soldiers are neither equipped nor trained for cavalry actions.
* The River Patrol, approximately 35 soldiers, responsible for responding to incursions along the river both up and down river, and occasionally called on to respond to incidents along the [[Bandit's Way]]. Led by [[Eveyln Totteridge|Sergeant Evelyn Totteridge]], it is a mounted patrol whose soldiers are trained to fight on horseback.

The garrison is situated in the east end of town, nestled into the gates. The garrison buildings themselves date from the final battles of the [[Third Hobgoblin War (Sembara)|Third Hobgoblin War]] and the members of the garrison have a proud history as Cleenseau was a key staging point during the hobgoblin wars. The garrison is much diminished from its heyday, but there is a lot of pride in the historical accomplishments.  Although the garrison is based in Cleenseau, it is not under the command of the Lord of Cleenseau and it is not part of the regular town guard. The command of the garrison reports to the [[Dunfry Regiment]] in [[Dunfry]] as part of the [[Army of the West]].
### Recent Events

* (DR:: 1719-11-05): [[Odo Cordwaner]] is dismissed as Sergeant of the Bridge Patrol for dereliction of duty after having failed to heed orders to stop [[Francois the Bandit]] during the [[Attempted Poisoning of Cleenseau]]
* (DR:: 1719-11-26): Receives orders to march to [[Dunfry]], apparently because of an imminent hobgoblin assault on the [[Western Wall of Sembara]] foretold by [[Robert I|King Robert I]]
* (DR:: 1719-11-27): Departs [[Cleenseau]] for [[Dunfry]] with all soldiers who are healthy enough to march
* (DR:: 1719-12-02): Arrives [[Dunfry]] after some confusion on the road
* (DR:: 1720-12-26): On the eve of [[Pyravela]], the River Patrol and a squad from the Bridge Patrol depart [[Dunfry]] for [[Cleenseau]] on the authority of [[Claude Leclerc]]. [[Ancer Benthey]] and part of the Bridge Patrol stay in [[Dunfry]] to await formal orders and bring further messages to [[Cleenseau]] when the situation clarifies
* (DR:: 1720-01-06): The garrison is ambushed on the [[South Watch Road]] by many zombies - at least 60. Approximately fifteen die in the combat, or from wounds shortly afterwards, and another ten are badly wounded and need healing and rest.
* (DR:: January 10, 1720): A day's ride outside of Cleenseau, the [[Heroes of Cleenseau]] heal and mend the garrison, using magical healing to restore to health the wounded. The troops ride the next morning as if on parade.

%% Chronology conflict: the 1720-12-26 departure is placed before the January 1720 return in this list; 1719-12-26 is a candidate year correction. The ambush is dated January 6 here and in [[Cleenseau Timeline (Email)]], but January 7 in [[Cleenseau Campaign - Timeline]]. The healing is dated January 10 here, while that timeline places it on January 9. Confirm these dates before changing them. %%

%% Dated force estimate: In “A Cavalry Raid?” (Mike Sackton email, February 6, 2024), Mike proposed approximate figures for the early January 1720 situation, after the garrison's losses on the road: originally 55 soldiers, 25 warhorses, and 15 pack animals; 10 soldiers left in Dunfry; about 15 soldiers, 5 horses, and 5 pack animals lost on the road; about 30 soldiers, 20 horses, and 10 pack animals then in Cleenseau. He estimated that about 25 of those 30 soldiers were trained mounted combatants. These were offered as working estimates (“so say something like”), not a fixed inventory. %%

%% Regional mounts in the same email were also rough estimates: about ten warhorses at Essford Manor before most left with Rosalind, leaving four there; about six in Beury and two in Valit; three fast riding horses reserved for crown messengers at the River's Blessing; and perhaps a few dozen other riding horses in Cleenseau and nearby villages, with varying training. Most farm animals were donkeys or draft horses and unsuitable for cavalry. Lorin had taken five good horses from Asineau; most of the manor's horses were recovered in [[Cleenseau - Session 12]]. %%

%% Additional context notes
The army was ordered away as part of a general plot by Malach to weaken the borders of Sembara, in general. He had been encouraging various forces in the borderlands to attack, with the goal of recreating a disaster like the early part of the 3rd hobgoblin war.

Due to the actions of the Cleenseau PCs, Rosalind, a relatively well respected noble, has put some effort into recalling part of the garrison and they are expected to return in a few weeks.
%%

%%^Campaign:none%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%% Bertram the quartermaster %%

%%^Metadata:names:v1%%
- {"name": "Army Garrison of Cleenseau", "language": "unknown", "pronunciation": "AR-mee GAR-ih-sun of Klen-sew", "status": "documented", "notes": "The place-name pronunciation Klen-sew is recorded in [[Cleenseau]]; the descriptive English words retain their ordinary pronunciations."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the undated patrol strengths and command describe the late-DR 1719 garrison, followed by dated events reaching early DR 1720; the later expansion, relocation, and command reorganization are omitted, and some event dates conflict.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added persistent name metadata and the article’s POV and temporal-coverage note.
- Normalized `Campaign:None` to `Campaign:none`; the current exporter casefolds both to the same private sentinel, preserving filtered visibility.
- Corrected the unambiguous “lead … is” grammar and plural subject–verb agreement in the departure entry.
- Added a nearby chronology-conflict comment without choosing between dates.

### Validated judgments
- `status/gameupdate/clee` is preserved and not assessable until the human chooses whether to update, defer, or retain the earlier article.
- The documented Cleenseau pronunciation comes from [[Cleenseau]]; English descriptive words use their ordinary readings.
- The shared force and mount estimates remain explicitly approximate; the plot context remains DM-only and the isolated quartermaster reminder is unfinished editorial material.

### Editorial assessment
**Underdeveloped** — The visible account ends before the garrison’s central DR 1720 changes: expansion and the Asineau base, followed by its return to Cleenseau and a vacant captaincy after Ida’s promotion. A short dated account plus a choice of article viewpoint would restore a usable account of the unit’s state. Conflicting event dates also need reconciliation.

### Open findings

- [ ] **Warning — coverage.later_material_change:** The opening still describes the approximately 55-soldier force under Captain Ida. [[Cleenseau - Session 11]] and [[Cleenseau Campaign - Timeline]] establish the January 10 decision to fund expansion to 100 soldiers and base the force at Asineau. [[The Situation in Asineau (Email)]] establishes that by around April 1, 1720, Ida had been promoted to major commanding the Enst Regiment and the garrison had returned to Cleenseau with its captaincy vacant. Choose to update prose, relationships and POV; defer using the existing game-update tag; or explicitly preserve the earlier snapshot. A bounded later layer is:

  ```markdown
  %%^Date:1720-01-10%%
  In January DR 1720, regional leaders funded an expansion of the garrison to 100 soldiers under [[Ida Rosfeld]], with [[Asineau]] as its base.
  %%^End%%
  ```

  This date boundary is a proposal only. A separate April candidate is: `By early April DR 1720, the garrison had returned to [[Cleenseau]] and needed a new captain after Ida’s promotion to major.` Establish the April transition date before giving that later passage a date-sensitive block. Date or otherwise bound the old patrol-strength snapshot when adopting the update, rather than presenting both strengths as current.

- [ ] **Warning — correctness.internal_conflict:** The departure entry is dated `1720-12-26` between November DR 1719 and January DR 1720 events. The narrative sequence requires an earlier departure; the bounded candidate is `(DR:: 1719-12-26)`. This is a date decision, so the linter retained the authored value and asks for confirmation before replacement.

- [ ] **Warning — correctness.cross_note_conflict:** The ambush is January 6 in this note and [[Cleenseau Timeline (Email)]], but January 7 in [[Cleenseau Campaign - Timeline]]. The healing is January 10 here, while that timeline places the ride and healing on January 9 before the next-morning council. Confirm the dates against the session source; retain or amend `(DR:: 1720-01-06)` for the ambush and `(DR:: 1720-01-09)` for the healing only after that choice. The nearby comment records both conflicts without resolving them.

%%^End%%

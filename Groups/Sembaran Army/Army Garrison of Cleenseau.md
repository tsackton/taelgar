---
headerVersion: 2023.11.25
tags: [group, testcase, status/gameupdate/clee, status/check/ai]
displayDefaults: {partOf: '<typeof:Au> of <partof>', boxInfo: ''}
name: Army Garrison of Cleenseau
partOf: Dunfry Regiment
typeOf: garrison
whereabouts:
- {type: home, location: Cleenseau }
- {type: away, end: 1720-01-10, location: Dunfry}
dm_notes: important
dm_owner: mike
---
# The Army Garrison of Cleenseau

The Cleenseau Garrison is the furthest east-most garrison of the [[Army of the West]]. It is commanded by [[Ida Rosfeld|Captain Ida Rosfeld]] and consists of two patrols:

* The Bridge Patrol, responsible for the security of the bridge and the road, and for providing a reaction force that can march and respond to threats. The Bridge Patrol consists of approximately 20 soldiers, currently lead by acting sergeant is [[Ancer Benthey]]. Its soldiers are neither equipped nor trained for cavalry actions.
* The River Patrol, approximately 35 soldiers, responsible for responding to incursions along the river both up and down river, and occasionally called on to respond to incidents along the [[Bandit's Way]]. Led by [[Eveyln Totteridge|Sergeant Evelyn Totteridge]], it is a mounted patrol whose soldiers are trained to fight on horseback.

The garrison is situated in the east end of town, nestled into the gates. The garrison buildings themselves date from the final battles of the [[Third Hobgoblin War (Sembara)|Third Hobgoblin War]] and the members of the garrison have a proud history as Cleenseau was a key staging point during the hobgoblin wars. The garrison is much diminished from its heyday, but there is a lot of pride in the historical accomplishments.  Although the garrison is based in Cleenseau, it is not under the command of the Lord of Cleenseau and it is not part of the regular town guard. The command of the garrison reports to the [[Dunfry Regiment]] in [[Dunfry]] as part of the [[Army of the West]].
### Recent Events

* (DR:: 1719-11-05): [[Odo Cordwaner]] is dismissed as Sergeant of the Bridge Patrol for dereliction of duty after having failed to heed orders to stop [[Francois the Bandit]] during the [[Attempted Poisoning of Cleenseau]]
* (DR:: 1719-11-26): Receives orders to march to [[Dunfry]], apparently because of an imminent hobgoblin assault on the [[Western Wall of Sembara]] foretold by [[Robert I|King Robert I]]
* (DR:: 1719-11-27): Departs [[Cleenseau]] for [[Dunfry]] with all soldiers who are healthy enough to march
* (DR:: 1719-12-02): Arrives [[Dunfry]] after some confusion on the road
* (DR:: 1720-12-26): On the eve of [[Pyravela]], the River Patrol and a squad from the Bridge Patrol departs [[Dunfry]] for [[Cleenseau]] on the authority of [[Colonel Claude Leclerc]]. [[Ancer Benthey]] and part of the Bridge Patrol stays in [[Dunfry]] to await formal orders and bring further messages to [[Cleenseau]] when the situation clarifies
* (DR:: 1720-01-06): The garrison is ambushed on the [[Old West Road]] by many zombies - at least 60. Approximately fifteen die in the combat, or from wounds shortly afterwards, and another ten are badly wounded and need healing and rest.
* (DR:: January 10, 1720): A day's ride outside of Cleenseau, the [[Heroes of Cleenseau]] heal and mend the garrison, using magical healing to restore to health the wounded. The troops ride the next morning as if on parade.

%% Dated force estimate: In “A Cavalry Raid?” (Mike Sackton email, February 6, 2024), Mike proposed approximate figures for the early January 1720 situation, after the garrison's losses on the road: originally 55 soldiers, 25 warhorses, and 15 pack animals; 10 soldiers left in Dunfry; about 15 soldiers, 5 horses, and 5 pack animals lost on the road; about 30 soldiers, 20 horses, and 10 pack animals then in Cleenseau. He estimated that about 25 of those 30 soldiers were trained mounted combatants. These were offered as working estimates (“so say something like”), not a fixed inventory. %%

%% Regional mounts in the same email were also rough estimates: about ten warhorses at Essford Manor before most left with Rosalind, leaving four there; about six in Beury and two in Valit; three fast riding horses reserved for crown messengers at the River's Blessing; and perhaps a few dozen other riding horses in Cleenseau and nearby villages, with varying training. Most farm animals were donkeys or draft horses and unsuitable for cavalry. Lorin had taken five good horses from Asineau; most of the manor's horses were recovered in [[Cleenseau - Session 12]]. %%

%% Additional context notes
The army was ordered away as part of a general plot by Malach to weaken the borders of Sembara, in general. He had been encouraging various forces in the borderlands to attack, with the goal of recreating a disaster like the early part of the 3rd hobgoblin war.

Due to the actions of the Cleenseau PCs, Rosalind, a relatively well respected noble, has put some effort into recalling part of the garrison and they are expected to return in a few weeks.
%%

%%^Campaign:None%%
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

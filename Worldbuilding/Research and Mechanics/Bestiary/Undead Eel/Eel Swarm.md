### Eel Swam
This is a swarm of eels, sharp toothed and hungry, that is also able to entangle and confuse enemies.

```statblock
name: Eel Swarm
ac: 14
hp: 36
speed: walk 30 ft, swim 30 ft
stats: [11, 14, 12, 3, 10, 7]
saves:
- WIS: +1
type: medium swarm of tiny beasts (group) 
condition_immunities: restrained, stunned, grappled, prone
damage_resistances: bludgeoning, piercing, slashing
senses: darkvision 60 ft, Passive Perception 13
traits:
  - name: Swarm
    desc: The swarm can occupy another creature's space and vice versa, and the swarm can move through any opening larger enough for a Tiny eel. The swarm cannot regain hit points or gain temporary hit points.
  - name: Morale
    desc: Bloodied, DC 17 Panic
actions:
   - name: Bite
     desc: "Melee weapon attack, +5 to hit, reach 0 ft, one target in the swarm's space. Hit: 10 piecing damage"
bonus_actions:
  - name: Obscure
    desc: "The swarm churns the water in its space, causing the area the swarm is in to be diffcult terrain. Anyone in the same square as the swarm is blinded."
  - name: Grapple
    desc: After a successful bite attack, the swarm can use a bonus action to entangle the creature it bite. The creature is grappled (escape DC 16). While grappling a creature, the swarm cannot use its Obscure action, and if it moves, the grapple is broken.
```



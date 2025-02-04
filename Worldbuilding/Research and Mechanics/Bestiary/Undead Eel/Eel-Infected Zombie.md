### Eel Infected Zombie
Some of the zombies have zombie-fied eels living inside them.

```statblock
name: Eel Infected Zombie
ac: 10
hp: 36
speed: swim 30 ft
stats: [16, 14, 16, 3, 8, 3]
type: medium undead (group) 
saves: 
- WIS: +1
- DEX: +3
damage_vulnerabilities: fire, radiant
damage_immunities: poison, psychic
damage_resistances: necrotic
senses: blindsense 40 ft, Passive Perception 12
traits:
  - name: Hard to Kill
    desc: If damage reduces the zombie to 0 HP, it must make a DC 10 CON saving throw unless the damage is fire, radiant, or a critical hit. On a success, the zombie drops to 1 HP instead
  - name: Sense Life
    desc: The zombie can smell living things in the water.
  - name: Morale
    desc: None
actions:
   - name: Grab
     desc: "Melee weapon attack, +5 to hit, reach 15 ft, one target. Hit: 8 (1d8+3) bludgeoning damage. If the target is Medium or smaller, it is grappled (escape DC 14). The zombie can move the creature up to 10 ft towards it as part of a successful grab attack. Only a single creature can be grabbed at a time."
   - name: Bite
     desc: "Melee weapon attack, +4 to hit, reach 5 ft, one grappled target. Hit: 12 (2d8+3) piercing damage."
```

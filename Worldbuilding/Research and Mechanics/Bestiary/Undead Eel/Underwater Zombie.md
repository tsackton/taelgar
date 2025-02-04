### Underwater Zombie
These creatures are the remains of sailors, fisherfolk, and others, enchanted and awakened by dark magic. They swim badly and stumble about slowly. Their main tactic is to swarm an enemy, grapple them, and feast. 

```statblock
name: Underwater Zombie
ac: 10
hp: 24
speed: walk 15 ft, swim 15 ft
stats: [16, 8, 16, 3, 8, 3]
type: medium undead (gang) 
saves: 
- WIS: +1
damage_vulnerabilities: fire, radiant
damage_immunities: poison, psychic
damage_resistances: necrotic
senses: blindsense 15 ft, Passive Perception 12
traits:
  - name: Hard to Kill
    desc: If damage reduces the zombie to 0 HP, it must make a DC 10 CON saving throw unless the damage is fire, radiant, or a critical hit. On a success, the zombie drops to 1 HP instead
  - name: Sense Life
    desc: The zombie can smell living things in the water.
  - name: Morale
    desc: None
actions:
   - name: Grab
     desc: "Melee weapon attack, +5 to hit, reach 5 ft, one target. Hit: 3 bludgeoning damage. If the target is Medium or smaller, it is grappled (escape DC 14). Only a single creature can be grabbed at a time."
   - name: Bite
     desc: "Melee weapon attack, +4 to hit, reach 5 ft, one grappled target. Hit: 10 (2d6+3) piercing damage."
```

Lenora Belles

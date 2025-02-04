## Raven
A raven ensorcelled by a fey.

```statblock
name: Encorcelled Swarm of Ravens
ac: 13
hp: 13
type: medium swarm of tiny beasts (mob) 
speed: walk 10 ft, fly 50 ft
stats: [19,10,14,2,12,7]
condition_immunities: restrained, stunned, grappled, prone
damage_resistances: bludgeoning, piercing, slashing
skillsaves:
  - Perception: +3
type: medium monstrosity (gang) 
senses: Passive Perception 13
traits:
  - name: Morale
    desc: Damaged, DC 17 Rout    
actions:
  - name: Attack
    desc: "The swarm makes one attack or defends an ally"
  - name: Claws
    desc: "Melee weapon attack, +4 to hit, reach 5 ft, one target in the swarms space. Hit: 2d6 piercing damage"
  - name: Defend
    desc: "If the swarm is sharing a space with an ally, it can use its action to defend the ally, granting Disadvantage on any attacks, or half-cover on any ranged attacks that pass through the space"    
```


## Bear

```statblock
name: Ensorcelled Bear
ac: 15
hp: 24
type: large beast (gang) 
speed: walk 40 ft, climb 30 ft
stats: [19,10,14,2,12,7]
skillsaves:
  - Perception: +3
senses: Passive Perception 13
traits:
  - name: Morale
    desc: Bloodied, DC 12 Rage    
actions:
  - name: Multi-attack
    desc: "The bear makes two attacks one with each claw."
  - name: Claws
    desc: "Melee weapon attack, +6 to hit, reach 5 ft, one target. Hit: 2d6+4 slashing damage"
bonus_actions:
 - name: Knock Prone
   desc: If the bear hits with both claws on the same target, the target is knocked prone
```

## Vulture

```statblock
name: Ensorcelled Giant Vulture
ac: 15
hp: 24
type: large beast (gang) 
speed: walk 10 ft, fly 60 ft
stats: [15,10,15,6,12,7]
skillsaves:
  - Perception: +3
senses: Passive Perception 13
traits:
  - name: Morale
    desc: Bloodied, DC 12 Panic    
  - name: Vicious Predator
    desc: The vulture has advantage when attacking a prone target
  - name: Keen Senses
    desc: The vulture has advantage on Perception checks that rely on sight or smell
actions:
  - name: Attack
    desc: "The vulture makes one attack with its beak or two attacks with its talons"
  - name: Beak
    desc: "Melee weapon attack, +3 to hit, reach 5 ft, one target. Hit: 2d8+2 slashing damage"
  - name: Talons
    desc: "Melee weapon attack, +6 to hit, reach 5 ft, one target. Hit: 2d4+2 slashing damage"    
```
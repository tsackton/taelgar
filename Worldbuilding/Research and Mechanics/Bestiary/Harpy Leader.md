

```statblock
name: Harpy Leader
ac: 14
hp: 53
speed: walk 20 ft, fly 40 ft
stats: [14, 14, 12, 12, 10, 15]
saves:
 - WIS: +3
 - DEX: +5
type: medium monstrosity (pair) 
senses: Passive Perception 12
traits:
  - name: Morale
    desc: Bloodied, DC 7 Rout    
  - name: Flyby
    desc: While flying, it can attack and move without provoking opportunity attacks
actions:
  - name: Multi-attack
    desc: The harpy makes two attacks with its claws or uses its Hideous Laughter
  - name: Claws
    desc: "Melee weapon attack, +7 to hit, reach 5 ft, one target. Hit: 1d8+4 slashing damage. Advantage against prone targets."
  - name: Hideous Laughter
    desc: "The harpy sings a piercing melody, and a creature within 30 feet perceives everything as hilariously funny and must make a DC 13 Wisdom saving throw or fall prone and become incapacitated and unable to stand for the duration. At the end of each turn and whenever it takes damage the target can repeat the saving throw, which has advantage if triggered by damage. This effect ends the Luring Song."    
bonus_actions:
  - name: Luring Song
    desc: "Every humanoid within 500 feet makes a DC 15 Wisdom save or is entranced"
  - name: Sapping Shriek
    desc: "The harpy shrieks and saps the enegry from one target within 30 feet. The target must make a DC 13 Constitution saving throw or take 1d4 pyschic damage and fall prone. This action ends the Luring Song when used."    
```


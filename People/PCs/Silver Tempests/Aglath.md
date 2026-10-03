---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/gl, status/check/lint]
species: stoneborn
gender: male
born: 1721
name: Aglath
affiliations:
  - {org: Silver Tempests, end: 1747-11-22}
whereabouts:
  - {type: home, start: 1735, end: 1747-01-01, location: Chardon}
  - {type: home, start: 1747-04-08, end: 1747-12-01, location: Voltara}
  - {type: away, start: 1747-11-22, end: 9999, location: Sentinel Range}
knownTo: [grli]
dm_owner: tim
dm_notes: none
POV: 1747
---
# Aglath
>[!info]+ Biographical Info  
> A [[Stoneborn|stoneborn]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Aglath was born in a distant land. What little he remembers of his childhood was peaceful; he displayed a natural aptitude for fighting, and even while young would often spend long days practicing with his sword.

One day, when returning from a day of hard practice, he came home to find his parents dead, covered in blood. He saw two glowing bestial eyes in the distance, which then vanished, and fled immediately in shock and terror, not stopping to learn more. While wandering alone, and struggling to survive, he met a wizard, [[Eutus]], searching for ancient ruins. This wizard was from the [[Great Library]] in [[Chardon]], and befriended Aglath, eventually bringing him back to [[Chardon]].

In [[Chardon]], Aglath was lost for a while, not sure what to do with himself, but met another [[Stoneborn]] who encouraged him to join the [[Chardonian Legion]]. After several years training as a soldier, the wizard [[Eutus]] found Aglath and asked him to join the [[Great Library]] as an adventurer. He agreed, and was sent north to [[Voltara]] where he soon connected with [[Brelith]], [[Aelar]], [[Adrik]], and [[Samso]].

After traveling with the [[Silver Tempests]] for almost nine months, Aglath departed the group after meeting the [[Deno'qai]] of [[Raha]], and headed into the [[Sentinel Range|Sentinels]] to search for meaning and a place to belong.

%%^Metadata:names:v1%%
- {name: Aglath, language: Stoneborn, pronunciation: AH-glat, notes: "Listed among Stoneborn birth names in [[Stoneborn#Stoneborn Names]]; proposed reading derived from the analogue in [[Languages#Stoneborn]], adapted to this constructed spelling with an aspirated final t and first-syllable prominence. No accepted pronunciation is recorded.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1747 biography ending with Aglath's departure for the Sentinels, with selected childhood and Chardonian backstory; later life is not covered.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected “solider” to “soldier”.
- Normalized frontmatter and added `knownTo: [grli]`, supported by [[Great Library Session Notes - Arc 1]].
- Added a primary name entry with a proposed pronunciation, plus `POV: 1747` and temporal coverage describing the biography's existing endpoint.

### Validated judgments
- The childhood, training, recruitment, and departure narrative performs a bounded early-life reference role; individual encounters do not require a campaign log here.
- `status/gameupdate/gl` is not assessable until the later-life coverage choice below is made. It is preserved unchanged.
- [[Stoneborn#Stoneborn Names]] explicitly lists Aglath as a Stoneborn birth name, supporting the name-language inference.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new name entry remains `proposed`. Proposed pronunciation: `AH-glat`, with the final t followed by a small puff of air. [[Languages#Stoneborn]] supplies the Xhosan analogue; the adaptation uses two open a vowels, a hard g, ordinary l, aspirated th rather than English th, and first-syllable prominence approximating penultimate lengthening. The consonant cluster and final consonant are adaptations of a constructed name, so this is not established in-world phonology. The aspiration distinction is documented in [this isiXhosa pronunciation guide](https://sweetvalleyprimary.co.za/wp-content/uploads/2020/01/Pronunciation-guide.pdf), and penultimate lengthening in [this Xhosa phonetics study](https://www.scielo.org.za/scielo.php?pid=S2224-33802017000200005&script=sci_arttext). Accept or correct the proposal; after acceptance, copy it to frontmatter and mark the name entry `documented`.
- [ ] **Warning — correctness.chronology:** “After traveling with the Silver Tempests for almost nine months” does not agree with [[Great Library Session Notes - Arc 1]], which places Aglath's first meeting with Samso and Adrik on DR 1747-04-15, and this note's affiliation end and departure whereabouts on DR 1747-11-22: about seven months. Confirm the interval and replace `for almost nine months` with `for about seven months`, or use `for several months` if the exact interval is not intended. If the recorded departure date is retained, the smallest visibility proposal is to enclose only the corrected final paragraph in a `Date:1747-11-22` block; this remains a human choice and has not been applied.
- [ ] **Warning — coverage.later_material_change:** The biography ends with Aglath seeking meaning and belonging in the Sentinels, while [[Silver Tempests]] states that he subsequently turned to a life of crime. This changes his later identity even though the existing biography is anchored to DR 1747. Choose whether to update the article and its temporal coverage, defer the update while retaining `status/gameupdate/gl`, or intentionally preserve the earlier biography and have a human remove that game-update tag. Bounded addition if updating: `After leaving the [[Silver Tempests]] to seek his kin in the [[Sentinel Range|Sentinels]], Aglath later turned to a life of crime.` The source does not date or explain that change; do not invent either or assign a narrower date block to it without evidence.
%%^End%%

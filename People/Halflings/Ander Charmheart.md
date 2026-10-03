---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
ancestry: null
timelineDescriptor: Charmhearts
campaignInfo:
  - {campaign: dufr, date: 1748-03-29, type: met}
  - {campaign: dufr, date: 1748-07-09, type: last seen}
born: 1728
gender: male
name: Ander Charmheart
affiliations:
  - {org: Charmhearts, type: primary}
whereabouts:
  - {type: away, start: 1748-03-19, end: 1748-03-19, location: "Raven's Hold"}
  - {type: away, start: 1748-03-28, end: 1748-04-07, location: Karawa}
  - {type: away, start: 1748-04-07, end: 1748-04-13, location: traveling to Tokra}
  - {type: away, start: 1748-04-13, end: 1748-07-18, location: Tokra}
  - {type: away, start: 1748-07-18, end: 1748-08-13, location: Tokra-Darba Road}
  - {type: away, start: 1748-08-13, location: Darba}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Ander Charmheart
>[!info]+ Biographical Info
> A [[Halflings|halfling]] (he/him), of the [[Charmhearts]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on March 29th, 1748 in [[Karawa]], [[Eastern Dunmar]], [[Dunmar]] %%^End%%
>> %%^Campaign:dufr%% Last seen by the [[Dunmar Fellowship]] on July 9th, 1748 in [[Tokra]], [[Dunmar]] %%^End%%

A young, rambunctious and excessively curious halfling, traveling with the Charmheart trading caravan as a scout and general hand. 
## Relationships
- [[Callie Charmheart]], older sister and traveling companion
- [[Bree Charmheart]], grandmother and traveling companion
%%^Date:1748%%
- [[Garret Tealeaf]], occasional traveling companion 
%%^End%%

%%^Campaign:None%%

```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%

%%^Campaign:DuFr%%
## Events
In March 1748, Ander was taken with a demonic curse as a result of accidental contact with Abyssal energy during the demon summoning at [[Raven's Hold]]. The curse caused him to suffer from an overwhelming hunger for raw flesh. When the demon [[Oduk]] was killed by the [[Dunmar Fellowship]], Ander was released from the worst of the curse. As of the summer of 1748, he still suffered from occasional confusion and difficulty speaking and finding the right word, describing the feeling as the wounds left by the shrapnel from a chaotic bomb that exploded in his mind. 

### Chronology
- (DR:: 1748-03-19): While exploring the ruined Dunmari fort of [[Raven's Hold]], Ander Charmheart heard a strange chanting, and was grabbed by a thorny vine while trying to flee. He later described this as like a wave of chaotic dark energy washing over him, and then exploding in his mind like a bomb. 
- (DR:: 1748-03-22): Ander Charmheart begins to display signs of madness, feeling either consumed by a ravenous hunger for raw flesh, or raving about the coming master who would consume the world. 
- (DR:: 1748-04-12): Ander Charmheart is released from the demonic curse possessing him, when the demon [[Oduk]] is killed by the [[Dunmar Fellowship]] in [[Raven's Hold]]

%%^End%%


%% One Note
 
A halfling trader from Sembara, grandson of Bree and brother to Callie. Curious. Explored Raven's Hold, got caught in a wave of Abyssal energy, and went mad.
 
Currently, the madness is not getting worse. He has not turned into a gnoll or anything like that. But also he is not exactly better. Mostly conscious. Can describe more clearly what happened -- felt like a wave of something, washing over him, this chaotic dark energy, almost like a bomb and then the shrapnel embedded in his mind. Now the shrapnel has faded but the wounds remain. Speaks slowly, cautiously, struggles for words. Has horrible dreams at night, can't really sleep.
 
A few options for healing:

1. Kenzo's cleansing touch could heal him with a DC 14 Wisdom check -- maybe?
2. With the demon ichor, a priest could figure out how to use Lesser Restoration to cure him.
3. Dispel magic - maybe?
 
Think about options, see what they try.
 
Age: late 30s
Current location (June 1748): In Tokra, with the rest of the Charmheart family, trying to find a cure for his madness

PC Interactions
 
Has spoken to Wellby telepathically, and if cured may remember him vaguely.

%%

%%^Metadata:names:v1%%
- {name: Ander Charmheart, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of a young caravan scout, with the curse and partial recovery explicitly dated to DR 1748; the chronology and whereabouts do not establish his later condition.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added persistent name metadata and a supported temporal viewpoint.
- Added knownTo: [dufr] from the existing campaignInfo.
- Corrected two unambiguous transcription typos in the shared One Note comment: “and when mad” to “and went mad,” and “turned in a gnoll” to “turned into a gnoll.”

### Validated judgments
- [[Charmhearts]] and the June DR 1748 encounter in [[Wellby]] support the published partial recovery; no full cure is established.
- The positive dm_notes attestation has confirmed local source matches.

### Open findings

- [ ] **Warning — correctness.internal_conflict:** The shared One Note comment says “Age: late 30s” in its June DR 1748 frame, but `born: 1728` implies an age of about 20. Choose the intended age; if the birth year is retained, replace that comment line with `Age: about 20 in DR 1748`. Otherwise supply the intended birth year. Neither value was silently preferred.
- [ ] **Suggestion — editorial.shared_material_redundant:** The first two paragraphs of the shared One Note comment repeat the published Relationships and Events account, including the curse and the image of wounds remaining after the shrapnel has faded. Remove the duplicated family/curse material or retain only distinct editorial guidance; keep the separate private healing options and PC-interaction guidance nonpublic, and retain the disputed age until it is resolved. This bounded split would leave one reference account of his partial recovery.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated relationship-query block uses `%%^Campaign:None%%`, and the Events block uses `%%^Campaign:DuFr%%`. Canonical replacements are `%%^Campaign:none%%` and `%%^Campaign:dufr%%` respectively; retain all enclosed content and closing boundaries. The existing visibility markers were preserved for human review.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Festival Visitors and NPCs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Old Notes 1]]
%%^End%%

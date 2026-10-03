---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: elf
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-01-15, type: met}
born: 1532
ka: 36
gender: enby
name: Vahaiya
pronunciation: va-HAI-ya
affiliations:
  - {org: Rangers, start: 1640, end: 1720}
whereabouts:
  - {type: home, start: "", end: 1545, location: Ainumarya}
  - {type: away, start: 1545, end: 1720-07-30, location: traveling around greater Sembara}
  - {type: home, start: 1720-07-31, location: Erelion}
knownTo: [dufr, clee]
dm_owner: joint
dm_notes: none
POV: 1740s
---
# Vahaiya
*(va-HAI-ya)*
>[!info]+ Biographical Info  
> An [[Elves|elf]] (they/them), ([[Elven Cycle of Generations|ka]] 36)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on January 15th, 1748 in [[Erelion]], [[Orenlas]] %%^End%%

%% Original frontmatter annotation between `born: 1532` and `ka: 36`:
# leya of ka 36
%%

![[vahaiya-portrait.png|right|400]]Vahaiya is a warrior, traveler, adventurer, and veteran of the [[Great War]]. They fought with the Sembaran Army in the [[Battle of Urlich Pass]], and survived. After the Great War, they traveled extensively around [[Addermarch]], the [[Aurbez Plateau]], [[Duchy of Maseau|Maseau]], and other Sembaran borderlands for many years. They made a name for themselves in the Sembaran hobgoblin wars.

%%^Date:1720-07-30%%
Growing tired of fighting after many years, they settled in [[Erelion]], where they now live, spending time as an artist and art collector.
%%^End%%

![[vahaiya-2.jpg|right|400]] %% notes below
A well-connected collector of elven painting, of the 36th ka. They survived the Great War, fighting alongside Sembarans in the Battle of [[Urlich Pass]]. After the war, could not settle, and did not return to have children during his first mela. Traveled and fought with the rangers for a time, spent time around Massau, Addermarch, fighting hobgoblins, until by 1700 was tired of fighting. Had amassed some considerable skill in arms, and favors and knowledge from a wide swath of people, including many rangers. Word of their deeds spread, and returns to [[Orenlas]] - which is particularly close to Addermarch - in the early 1700s, tired, feeling out of cycle, uncertain about having missed their first mela, wanting the strength of Aldanor's roots just as Elmerca's winds are scattering the newly awakened elves of the small and uncertain 37th ka. Decides to stay in [[Orenlas]]. Given their fame, attracts a number of gifts, and finds particular joy in painting. Even has one of Beryl's paintings, a very rare piece if not particularly amazingly crafted, and a gift from the Rangers. 

 the elf, a skilled fighter, proud of their bow and clearly quite good with it. They tell you several tales of the Great War, especially the [[Battle of Urlich Pass]], when it seemed like an endless horde of hobgoblins would overwhelm the elven and Sembaran armies, until the earth and mountains shook as the great skeletal dragon Cha'mutte died, and everyone hobgoblin and human and elf alike fled from the battle as the mountains started to fall. They also tell smaller stories, of their attempts at painting, of a victory over a dust creature on the plains south of Cleenseau (you gather they have some magical ability related to their bow, as part of this story). They also tell of the fine walking in the woods of Addermarch, of the kindness of Marcel de Valarin, a paladin of the Wanderer who spent much time in the 1660s and 1670s in the northern reaches of Maseau, trying to help the war torn land recover. They speak highly of the order he founded, the Order of the Charitable Wanderer.
%%

%%^Metadata:names:v1%%
- {name: Vahaiya, language: unknown, pronunciation: va-HAI-ya, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-modern portrait of a Great War veteran and traveler, with settlement in Erelion isolated in the existing DR 1720 date block and retirement independently attested in DR 1749; the earlier career is selective rather than continuous.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported name and temporal metadata; normalized frontmatter without changing the header version.
- Added `knownTo: [dufr, clee]` from the campaign interaction and [[Rangers in Champimont]].
- Resolved the existing Rangers affiliation to `Rangers` and normalized the existing campaign code to `dufr`.
- Removed the duplicated “in the” and corrected “Growing tiring” to “Growing tired”.
- Preserved the exact YAML annotation “# leya of ka 36” in a hidden comment below the complete header, with its original birth/ka field context, as explicitly approved.

### Validated judgments
- The matching local source duplicates material already in the shared comment; it does not justify changing `dm_notes: none`.
- The existing date block isolates settlement in Erelion; retirement is corroborated by [[Session 87 (DuFr)]].

### Open findings

- [ ] **Warning — correctness.conflicting_dates:** The DuFr interaction metadata and header say January 15, 1748. [[Session 87 (DuFr)]] places the arrival and dinner with Vahaiya on January 15, 1749. Candidate: `{campaign: dufr, date: 1749-01-15, type: met}` and “January 15th, 1749” in the corresponding header. This chronology correction requires human approval.
- [ ] **Suggestion — editorial.public_material_candidate:** The shared comment beginning “A well-connected collector of elven painting” contains a developed detail omitted from the artist/collector description. Candidate for adoption: “Vahaiya collects elven paintings, including a rare painting by Beryl given to them by the [[Rangers]].” This makes their collection specific. After deciding whether to adopt that sentence, shorten the repeated Great War and wandering biography in the comment; retain separately the unconfirmed first-mela and settlement chronology, which should not be promoted merely because the passage is coherent.
%%^End%%

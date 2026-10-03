---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/gl, status/check/lint]
species: human
ancestry: "Yo'nari"
gender: male
campaignInfo:
  - {campaign: grli, type: met, date: 1748-10-14}
name: Joram of Eshlem
whereabouts: Eshlem
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1748
---
# Joram of Eshlem
>[!info]+ Biographical Info  
> A [[Yo'nari]] [[Humans|human]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:GL%% Met by the [[Silver Tempests]] on October 14th, 1748 in [[Eshlem]], [[Cairn Dor]], [[Shadowfolds]] %%^End%%

Joram of Eshlem is an elderly [[Yo'nari]] veteran from [[Eshlem]] in [[Cairn Dor]]. He learned Goblin while fighting in an ancient war, now faded in his memory, from before [[Yeshara]] saved the [[Yo'nari]] from the curse of sleep and brought them to [[Cairn Dor]] to live safely under the protection of the [[Shemra Azem]]. 

%% implication is that time passes differently somehow in Cairn Dor, but not entirely clear exactly how. possibly it is that time only passes in the brief periods when Cairn Dor is "awake", in the run up to wars %%

%%^Metadata:names:v1%%
- {"name": "Joram of Eshlem", "language": "unknown", "pronunciation": "yoh-RAHM of ESH-lem", "notes": "Proposed from the Hebrew side of the Deno'qai cultural analogue in Languages: J is read as y, a as ah, and sh as sh; final stress on Joram follows the Hebrew name pattern, while Eshlem's stress is tentative. The Yo'nari source language and exact in-world pronunciation are unestablished.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Joram's elderly, waking-veteran portrait at Eshlem in DR 1748, before Yeshara's fall; his ancient memories are undated, and the later sleep of Cairn Dor's inhabitants is not incorporated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, used `grli` in `campaignInfo`, and added `knownTo: [grli]` from the recorded encounter.
- Added persistent name metadata and a DR 1748 viewpoint for the waking-veteran portrait.

### Validated judgments
- `status/gameupdate/gl`: not assessable until the later-state choice below is made; the tag is preserved.
- The ordinary comment preserves unresolved ideas about time in Cairn Dor and is not adopted as canon.

### Open findings

- [ ] **Warning — coverage.later_material_change:** [[Great Library Session Notes - Arc 5#Session 63]] records that Cairn Dor's native inhabitants fell asleep when Yeshara fell in DR 1748 and remained asleep when the visitors awoke in DR 1752; [[Cairn Dor]] confirms this later state. Decide whether to update Joram's article and POV, defer the update while retaining `status/gameupdate/gl`, or intentionally preserve this earlier portrait and remove that tag by human choice. A bounded addition, if updating, is: “When [[Yeshara]] fell in DR 1748, the native inhabitants of [[Cairn Dor]] fell asleep. They remained asleep when the [[Silver Tempests]] departed in DR 1752; Joram's individual later fate is not recorded.” If retaining both temporal layers, place this addition in `Date:1752-06-28` with its matching closing marker only after deciding the intended visibility.
- [ ] **Warning — source.claim_attribution:** The phrase “Yeshara saved the Yo'nari from the curse of sleep” presents the inhabitants' doctrine as an unqualified fact. [[Yo'nari#History]] describes a rite that created Cairn Dor, while [[Great Library Session Notes - Arc 5#Session 63]] establishes the villagers' fear of sleep. Preserve the belief by replacing the second sentence with: “He learned Goblin while fighting in an ancient war, now faded in his memory, before [[Yeshara]] brought the [[Yo'nari]] into [[Cairn Dor]]. He regards Yeshara and the [[Shemra Azem]] as protectors against the dangers of sleep.”
- [ ] **Warning — metadata.names_unresolved_status:** The complete proposed pronunciation is `yoh-RAHM of ESH-lem`. The Hebrew side of the Deno'qai analogue in [[Languages]] supports reading J as y, a as ah, sh as sh, and final stress in Joram; Eshlem's stress remains tentative. The Yo'nari name's exact language and phonology are not established. Accept the proposal by copying it to frontmatter and marking the entry `documented`, or provide a correction.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The header retains `Campaign:GL`; [[Campaign Registry]] maps this alias to `grli`. Replace the opening marker with `Campaign:grli` when reviewing the generated header; leave its text and closing marker intact.
%%^End%%

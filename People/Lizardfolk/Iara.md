---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/gl, status/check/lint]
species: lizardfolk
gender: female
campaignInfo:
  - {campaign: grli, type: met, date: 1747-06-22}
name: Iara
whereabouts:
  - {type: home, location: Northwest Coast, end: 1747-06-01}
  - {type: away, start: 1747-06-01, end: "1747-10", location: Voltara}
  - {type: home, start: "1748-03", location: Lake Valandros, alias: a lizardfolk community near Lake Valandros}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1748
---
# Iara
>[!info]+ Biographical Info  
> A [[Lizardfolk|lizardfolk]] (she/her)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Met by the [[Silver Tempests]] on June 22nd, 1747 in [[Voltara]], [[Greater Voltara]], the [[Northern Provinces]] %%^End%%

Iara is a lizardfolk woman from an unnamed village west of [[Voltara]]. Her village vanished under [[Lizardfolk Village Disappearances|mysterious circumstances]], though she survived and asked for help from [[Samso]] and the [[Silver Tempests]].

Later, she moved to the area around [[Lake Valandros]]. 

%% AI note: Iara's unnamed village was presumably somewhere in the western foothills of the [[Fiatara Mountains]], roughly 100-140 miles west of [[Voltara]], rather than all the way to the coast. The frontmatter keeps the location broad as [[Northwest Coast]] because no more specific village or subregion has been established. %%


%%^Campaign:none%%

## DM notes

- (DR:: 1747-06-22): Iara approached [[Samso]] in [[Voltara]] and asked for help after the people of her village west of Voltara mysteriously disappeared. **Sources:** [[Great Library Session Notes - Arc 1]]; [[Lizardfolk Village Disappearances]].
- (DR:: 1747-06-26): [[Samso]], [[Brelith]], [[Aelar]], and [[Adrik]] reached the empty village, encountered shadowy evil echoes of lizardfolk, and killed the leading creature without learning the underlying cause. **Sources:** [[Great Library Session Notes - Arc 1]]; [[Lizardfolk Village Disappearances]].
- DM notes for the follow-up session say Iara was thankful and sent the party back with praise and some gold. **Source:** [[Session 9-10 - GL - Flesh Eaters]].
- During later downtime, Iara wrote to [[Samso]] that she was traveling south with the few other survivors of her village to settle near [[Lake Valandros]]. The letter included lilypad flour. **Sources:** [[Great Library Session Notes - Arc 4]]; [[GL - Session 56 - DM Notes]].
- In DR 1748 downtime, Samso visited Iara at the lizardfolk community near [[Lake Valandros]] and learned more about the mysterious attacks. **Source:** [[Great Library Session Notes - Arc 4]].
- Arc 5 background connects Iara's village to the first on-screen lizardfolk attack in the broader disappearance plot, but cautions that some details, including the "ten villages" figure, come from DM background rather than cleaned session record. **Sources:** [[Session 63 Background]]; [[Lizardfolk Village Disappearances]].

%%^End%%

%%^Metadata:names:v1%%
- {"name": "Iara", "language": "unknown", "pronunciation": "ee-AH-rah", "status": "proposed", "notes": "No accepted pronunciation or name language is recorded. The lizardfolk context suggests the Basque analogue for Lizardling in [[Languages]]: i as ee, open a vowels, and a lightly tapped r; the three syllables and middle stress are a tentative adaptation."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Iara’s DR 1747 displacement and her subsequent settlement near Lake Valandros, viewed from DR 1748 before the disappearance mystery was resolved; later consequences for Iara herself are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added supported campaign knowledge, primary-name metadata, and temporal POV metadata.
- Normalized legacy campaign codes to the registry’s canonical lowercase codes without changing their audience.
- Corrected “ask” to “asked” and the ordinal “22th” to “22nd.”

### Validated judgments
- The existing status/gameupdate/gl is not assessable until the human chooses whether to update the article or retain its earlier POV; the tag is preserved.
- The existing broad origin metadata remains explicitly qualified by the author’s location-uncertainty comment.
- The ordinary comment preserves uncertain geography; the Campaign:none block is a sourced chronology and editorial provenance record, not an instruction to promote its DM details.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new name entry proposes `ee-AH-rah`; no accepted pronunciation is recorded. The lizardfolk context suggests the Basque analogue for Lizardling in [[Languages]], motivating i as ee, open a vowels, and a lightly tapped r; the three-syllable reading and middle stress remain provisional. Accept by setting `pronunciation: ee-AH-rah` in frontmatter and `status: documented` on the entry, or supply the intended pronunciation.

- [ ] **Warning — coverage.later_material_change:** The opening frames the disappearance as mysterious, and the shared chronology ends before its resolution. [[Lizardfolk Village Disappearances]] and [[Great Library Session Notes - Arc 5]] establish that Yeshara’s forces held lizardfolk as dreamers in Cairn Dor; the raids stopped in September 1748, and surviving captives returned in June 1752. This resolves the phenomenon defining Iara’s displacement, but does not identify which people from her particular village survived or establish a reunion with her. Decide whether to update the account and POV, defer with the existing status/gameupdate/gl, or intentionally retain the earlier snapshot and review that tag. A bounded later-facing addition is: “The [[Lizardfolk Village Disappearances|disappearances]] were later traced to [[Yeshara]]’s forces, who held abducted lizardfolk in enchanted sleep in [[Cairn Dor]]. The surviving captives returned to the [[Material Plane]] in DR 1752.” If adopted while retaining the earlier article frame, put the first sentence inside a `Date:1748-10-14` block and the second inside a `Date:1752-06-28` block; these visibility changes require approval.
%%^End%%

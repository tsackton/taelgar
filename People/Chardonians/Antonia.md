---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T09:29:24-04:00"
lintVersion: "3.5"
tags: [person, testcase, status/gameupdate/dufr, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, date: 1748-12-08, type: imprisoned, format: "<met:U> by <person:Q> on <target>, in <current:3Qr>"}
born: 1714
gender: female
name: Antonia
pronunciation: An-ton-ia
affiliations:
  - {org: Society of the Open Scroll}
whereabouts:
  - {type: away, start: 1748-11-10, location: Dunmar}
  - {type: away, start: 1748-12-08, end: 9999, location: Mirror of Soul Trapping}
  - {type: home, location: Chardon}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Antonia
*(An-ton-ia)*
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Imprisoned by the [[Dunmar Fellowship]] on December 8th, 1748, in the [[Mirror of Soul Trapping]], [[Uzgukhar]], [[Xurkhaz]] %%^End%%

%% update to reflect events in DuFr game; copy notes from OneNote %%

![[antonia-portrait.jpg|right|320]]A lanky, red-haired Chardonian woman, wearing a probably-magical heavy suit of plate armor that seems perfectly molded to fit her body. 

%%^Campaign:dufr%%
Seemed to have mixed feelings about [[Kadmos]] actions to charm the party in [[Session 44 (DuFr)]], and was not involved in the battle in [[Session 45 (DuFr)]]. 

As far as you know, still traveling with [[Kadmos]]. 
%%^End%%

%%SECRET[v2:17cba8c7a742a4a893ac6262fd38c1f6]%%

%%^Metadata:names:v1%%
- {name: Antonia, language: Chardonian, pronunciation: An-ton-ia, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a discontinuous DR 1748 portrait spanning the July road encounter and December imprisonment; the visible campaign prose still requires a game-update decision after her capture.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter collection formatting and canonical Dunmar Frontier campaign identifiers.
- Added `knownTo: [dufr]`, persistent name metadata for the accepted pronunciation, and DR 1748 temporal POV metadata.

### Validated judgments
- Confirmed local-only sources support the positive `dm_notes: important` attestation.
- `status/gameupdate/dufr` is supported because the visible campaign prose predates Antonia's capture and interrogation in Sessions 78–79.
- The `SECRET` block was reviewed and remains private; its own editorial label says the material is outdated or wrong.

### Editorial assessment
- **Underdeveloped**. The visible article does not provide a reliable central account of Antonia: it gives her appearance and an early encounter, but omits her established role as an artificer, member of the Society of the Open Scroll, and follower of Kadmos, while its latest visible state is superseded by her capture, interrogation, and possible future exile. The smallest useful development scope is one campaign-scoped replacement paragraph covering those established facts.

- Discussion research: multiple non-Staging Worldbuilding notes discuss this subject. Query `_scripts/worldbuilding_discussion_index.json` before developing the missing material.

### Open findings
- [ ] **Warning — coverage.later_material_change:** The visible DuFr prose says Antonia is still traveling with Kadmos, but [[Session 78 (DuFr)]] records Kadmos's death and Antonia's capture in the [[Mirror of Soul Trapping]], and [[Session 79 (DuFr)]] records her interrogation, cooperation after learning the truth about [[Apollyon]], and the party's conditional plan for eventual exile. [[Dunmar Fellowship Associates]] also identifies the central role missing from the article: she is an artificer, member of the [[Society of the Open Scroll]], and follower of [[Kadmos]]. Decide whether to update the article and POV, defer the update while retaining `status/gameupdate/dufr`, or intentionally preserve an earlier snapshot and then remove that status after human review. Copy-ready replacement for the existing campaign prose:

  `%%^Campaign:dufr%%`

  Antonia is a Chardonian artificer, a member of the [[Society of the Open Scroll]], and a follower of [[Kadmos]]. In DR 1748, she joined Kadmos's attack on the palace at [[Uzgukhar]], was captured by the [[Dunmar Fellowship]], and was imprisoned in the [[Mirror of Soul Trapping]]. After learning that [[Apollyon]] was undead and that [[Fausto]] sought to free rather than resurrect him, she told the Fellowship what she knew. They agreed to hold her in the mirror for one or two years and possibly release her into exile near [[Voltara]] after [[Grash]] and Fausto were dead.

  `%%^End%%`

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 43]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 44]]
- [[_DM_/_Dunmari Frontier/Equipment Info DM Notes]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 71 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 72 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 73 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/In Game Notes]]
%%^End%%

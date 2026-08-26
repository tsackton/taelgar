---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, date: 1748-12-09, type: captured}
born: 1722
gender: male
name: Valius
affiliations: [Chardonian Legion, Society of the Open Scroll]
whereabouts:
  - {type: home, location: Chardon}
  - {type: away, start: 1748-08-01, end: 1748-12-09, location: Xurkhaz}
  - {type: away, start: 1748-12-08, end: 1748-12-09, location: Uzgukhar}
  - {type: away, start: 1748-12-10, end: 9999, location: Mirror of Soul Trapping}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Valius
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Captured by the [[Dunmar Fellowship]] on December 9th, 1748 in [[Uzgukhar]], [[Xurkhaz]], the [[Garamjala Desert]] %%^End%%

%% cleanup header, copy DM notes, reformat text %%

![[valius.png|right|300]]A former mercenary and adventurer, Valius now finds himself ensnared by the machinations of [[Fausto]] and trapped in the [[Mirror of Soul Trapping]]. Alongside his twin, [[Vargus]], he once sought treasures and wealth, but now seeks only to free his brother from [[Fausto]]'s curse.

%%^Metadata:names:v1%%
- {name: Valius, language: Chardonian, pronunciation: VAH-lee-oos, status: proposed, notes: "Proposed from the Italian and Latin analogue for Chardonian, with an open initial vowel and -ius as ee-oos."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late DR 1748 snapshot after Valius's capture in the Mirror of Soul Trapping; his DR 1749 release and later life are not reflected in the visible article.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized frontmatter; added `knownTo: [dufr]`, persistent name metadata, and late-DR-1748 POV metadata; normalized the campaign code from `DuFr` to `dufr` in both `campaignInfo` and the campaign block.

### Validated judgments
- The existing `status/cleanup/metadata` tag remains supported by the unresolved name-metadata decision and the note's outstanding update work.
- Confirmed local-only sources support the positive `dm_notes: important` attestation; private contents remain outside this shared report.

### Editorial assessment
- **Underdeveloped**: the visible article stops at Valius's late-DR-1748 captivity and omits the established DR 1749 release, his departure near Tokra with Vargus, and the brothers' intention to begin a quieter life in Dunmar.

### Open findings

- [ ] **Warning — coverage.later_material_change:** [[Session 124 (DuFr)]] establishes that the Fellowship freed Valius and Vargus from the Mirror of Soul Trapping on DR 1749-06-19 and left them near Tokra the next day with coin and a letter of introduction. Choose whether to update the article and `POV` to 1749, defer the update and add `status/gameupdate/dufr`, or explicitly preserve a late-1748 historical snapshot. For an update, replace the current final sentence with: `The Dunmar Fellowship freed Valius and Vargus from the Mirror of Soul Trapping on DR 1749-06-19. The following day, the brothers left near Tokra with coin and a letter of introduction, intending to begin a quieter life in Dunmar.` Also end the Mirror whereabouts on `1749-06-19` and add `{type: away, start: 1749-06-20, end: 9999, location: Tokra}`.
- [ ] **Warning — metadata.names_unresolved_status:** The new Valius name entry records `VAH-lee-oos` as a proposed pronunciation based on the Italian and Latin analogue for Chardonian. Review the proposal; if accepted, change the entry to `status: documented` and add `pronunciation: VAH-lee-oos` to frontmatter.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 116 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 125 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 71 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 72 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 73 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Statblocks - Grash Battle]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/In Game Notes]]
%%^End%%

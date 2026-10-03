---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
ancestry: null
campaignInfo:
  - {campaign: dufr, person: Delwath, date: 1748-07-01, type: Cured of lycanthropy}
born: 1729
gender: male
name: Dag Hardstone
affiliations:
  - {type: primary, org: Hardstones}
whereabouts: Tokra
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Dag Hardstone
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him), of the [[Hardstones]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Cured of lycanthropy by [[Delwath]] on July 1st, 1748 in [[Tokra]], [[Dunmar]] %%^End%%

Dag is the youngest member of the Hardstone clan, an extended family of dwarves that have lived at and worked for the [[Tokra]] [[Archives]] for generations, helping to maintain the building. 

%%^Campaign:dufr%%
In the summer of 1748 DR, Dag was caught by werewolves when the [[Archives]] were raided, and wounded, becoming cursed by lycanthropy. After he was subdued by the [[Dunmar Fellowship]], he was cured by [[Delwath]], with the blessing of [[Yezali]]. 
%%^End%%

%% One Note
Kid, not yet learned his caste. Cursed by lycanthropy and cured by Delwath. As of July 2nd, not yet ready to speak with party, but will be soon.
%%

%%^Metadata:names:v1%%
- {"name": "Dag Hardstone", "language": "unknown", "pronunciation": "DAHG HARD-stohn", "notes": "Using the Tolkien Dwarvish analogue in Languages: an open ah vowel and hard g in Dag; the translated clan name uses ordinary English Hardstone. The exact in-world vowel is unconfirmed. Dag is a child-name form in Dwarves; this note describes him before his naming pilgrimage.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Dag as a young member of the Hardstone clan in the late 1740s, with a separately dated account of his DR 1748 curse and cure.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported `knownTo`, a subject-name block, and article `POV`/`povNotes`; normalized frontmatter.

### Validated judgments
- [[Session 36 (DuFr)]] corroborates the curse and cure. Confirmed local source clusters support the existing positive `dm_notes` attestation.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `DAHG HARD-stohn` in `Metadata:names:v1`. [[Dwarves]] lists Dag as a child-name form and explains that clan names are commonly translated into the trade tongue. The Tolkien Dwarvish analogue in [[Languages]] supports a tentative open ah vowel and hard g; Hardstone uses ordinary English pronunciation. This is an analogue-informed proposal, not an adopted in-world rule. If accepted, copy `pronunciation: DAHG HARD-stohn` to frontmatter and change the entry to `status: documented`; otherwise amend the proposal.
- [ ] **Suggestion — editorial.shared_material_redundant:** In the ordinary `One Note` comment, “Cursed by lycanthropy and cured by Delwath.” repeats the immediately preceding campaign paragraph. Remove only that sentence, retaining the distinct caste and dated readiness notes. Leave the distinct remainder in its current private comment; no public promotion is proposed.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Clues]]
%%^End%%

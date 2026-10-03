---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Skaer
campaignInfo:
  - {campaign: dufr, date: 1748-12-22, type: fought and killed}
born: 1720
gender: male
died: 1748-12-22
name: Urgall the Black
aliases: [Urgall]
affiliations:
  - {place: Flaming Tempest, title: Captain, type: leader, start: 1}
whereabouts:
  - {type: home, end: 1741-01-01, location: Skaerhem}
  - {type: home, start: 1741-01-02, end: 1748-05-01, location: Western Green Sea}
  - {type: away, start: 1748-05-01, end: 1748-12-22, location: Vetta}
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: modern
---
# Urgall the Black
>[!info]+ Biographical Info  
> A [[Skaer]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Fought and killed by the [[Dunmar Fellowship]] on December 22th, 1748 in [[Vetta]], [[Skaerhem]] %%^End%%

Urgall, known as Urgall the Black, was a Skaer outcast and exile. As a young man, he felt constrained and bound by the conformist traditions of the Skaer, and chafed at being told where to work and what to contribute. Eventually, he refused to share his fishing bounty, and was excommunicated. He left, and wandered the [[Green Sea]], turning to piracy to support himself. Sometime during his pirate days, he made a pact with a demon known as [[Mashtu the Corruptor]], becoming a warlock in the service of the fiend's goals of corruption. 

%%^Date:1747%%
In the spring of DR 1747, Urgall's aims turned to the service of his demonic master, as recorded on a [[Urgall's scroll|ciphered scroll]] found on the [[Flaming Tempest]]. By the spring of 1748, this service took him to the holy island of [[Vetta]], where he was trapped and cursed by [[Jorma]], priest of the waters, and [[Kaikkea]], goddess of the ocean and protector of the [[Skaer]]. He wasted away on the island for months, unable to leave and unable to die, sacrificing his crew to summon his patron, the demon [[Mashtu the Corruptor]]. 

He was [[Session 81 (DuFr)|killed]] by [[Dunmar Fellowship]] in December 1748. 
%%^End%%

%%SECRET[v2:397dceda5ccd6a7e9379563d594fb808]%%

%%^Metadata:names:v1%%
- {name: Urgall the Black, language: unknown, pronunciation: OOR-gahl the BLACK, status: proposed, notes: 'Proposal informed by the Finnish option in the Skaegish analogues in [[Languages]]: initial stress in Urgall, u as oo, hard g, open a, and a held double l; the English epithet keeps its ordinary reading. Norwegian-influenced u could be more fronted; exact in-world phonology is not established.'}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective of Urgall's exile and piracy, with a dated layer beginning in DR 1747 and ending with his death in December DR 1748; the precise date of his arrival at Vetta remains a source conflict.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added knownTo from the existing campaign interaction record and normalized frontmatter ordering and collection formatting.
- Normalized the existing campaign aliases to canonical registry codes in campaignInfo and the matching header block.
- Added persistent name and temporal-viewpoint metadata; existing names, accepted pronunciations, and human attestations were preserved.

### Validated judgments
- The visible retrospective records Urgall’s defining exile, piracy, pact, and fate. The local-only SECRET block was reviewed; its contents remain private.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The pronunciation `OOR-gahl the BLACK` is recorded as `status: proposed` in Metadata:names:v1. The Skaegish guidance in [[Languages]] permits Finnish or Norwegian with Swedish influences. The proposal uses Finnish-like initial stress, u as oo, hard g, open a, and a held double l, with the English epithet read ordinarily. A Norwegian-influenced u could be more fronted; no exact in-world phonology settles the choice. Confirm or revise it; if accepted, copy `pronunciation: OOR-gahl the BLACK` to frontmatter and change the entry to `status: documented`.
- [ ] **Warning — consistency.cross_note_conflict:** Urgall’s whereabouts begins his stay in Vetta on `1748-05-01`, but [[Flaming Tempest]] gives arrival on `1748-05-03` in the reconstructed log and uses `Date:1748-05-22` for the docking passage. These records do not establish one consistent exact arrival date. Reconcile the whereabouts start with the ship chronology; if the reconstructed log is adopted, the bounded replacement is `{type: away, start: 1748-05-03, end: 1748-12-22, location: Vetta}`. Keep the spring-1748 prose until that human choice is made.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/In Game Notes]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Vetta/Docks Key]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Vetta/Encounters]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Vetta/Images]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Vetta/Temple Key]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Vetta/Vetta DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Zendra]]
%%^End%%

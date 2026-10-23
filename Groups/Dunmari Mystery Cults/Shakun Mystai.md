---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
tags: [group, status/check/lint]
typeOf: mystery cult
ancestry: Dunmari
name: Shakun Mystai
affiliations:
  - {org: Shakun, type: primary}
dm_owner: tim
dm_notes: important
POV: modern
---
```taelgar-header
```
One of the [[Dunmari Mystery Cults]], mystical organizations devoted to the [[Dunmari Religion|Dunmari gods]]. The [[Shakun]] Mystai, devoted to the goddess [[Shakun]], are based in the [[Temple of Shakun]] in the small village of [[Karawa]] in [[Eastern Dunmar]]. The temple in [[Karawa]] supports a community of somewhat over 100 initiates, along with a few dozen initiates-in-training and 40 or more lay associates of the mystai. The mystai are known for creating healing powders from the stone of the [[Red Mesa]], and for somehow misleading and waylaying those who attempt to cross the eastern borders of [[Dunmar]] with evil intent. 
%%^Campaign:dufr%%
The Shakun Mystai are primarily responsible for maintaining, in secret, the webs of protection and illusion that defend the eastern borders of [[Dunmar]], known as Shakun's Protection, as well as tending the living rock of the [[Red Mesa]], which is the embodied form of Shakun in the material plane. The magic of Shakun's Protection comes from the [[Red Mesa]], which is associated with the body of [[Shakun]] herself, and especially the sacred relic [[Heart of Shakun]]. When [[Heart of Shakun]] is in its proper place in the [[Temple of Shakun]] in secret chambers below the [[Red Mesa]], it provides a powerful source of divine magic, which is then channeled by the connected network of the mystai themselves to create Shakun's Protection. It is said that those who are not initiated into the mysteries cannot understand the full nature of this magic, and those who are cannot speak of it, willingly or unwillingly. But it is understood that, somehow, Shakun's Protection serves as a web of illusions that mask safe passages, making the desert appear as dead-end canyons, endless sands, and paths that twist and turn back to where they came from, for anyone with evil intent towards [[Dunmar]]. Those who persist, it is said, find themselves lost forever in Shakun's [[Shakun's Realm|divine realm]].  
%%^End%%
%%^Date:1748%%
In April 1748, the Shakun mystai, along with the rest of [[Karawa]] and [[Eastern Dunmar]], were attacked by rampaging gnolls during the [[Summer Gnoll Raids of 1748]]. More than a dozen mystai died in the attacks, and still, in November 1748, the mystai are diminished in strength and number. During this time, [[Dunmar Fellowship]] experienced an abbreviated [[The Shakun Mystai Initiation|initiation rite of the Shakun Mystai]], while later, after the return of [[Heart of Shakun]], [[Kenzo]] and [[Drikod]] experienced the [[The Shakun Mystai Initiation|full initiation rite]].
%%^End%%

%%^Campaign:none%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Shakun Mystai", "language": "unknown", "pronunciation": "SHAH-koon mis-TIE", "status": "proposed", "notes": "The Shakun component follows the accepted SHAH-koon in [[Temple of Shakun]]. No complete-name language or pronunciation is recorded. The Mystai proposal uses the Persian side of the Hindi/Persian Dunmari analogue in [[Languages]], adapting y to short i, retaining st, and reading ai as eye; final stress is a reading aid. A Hindi-oriented ai could instead suggest eh. The compound remains proposed, not adopted phonology."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern cult practices and responsibilities, with a separate retrospective account of the DR 1748 attacks, initiations, and reduced strength through November; the membership totals are not a dated census.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and affiliation formatting, and canonicalized the existing campaign markers to `dufr` and `none` without changing their scopes.
- Corrected “experienced the an abbreviated” to “experienced an abbreviated” and added the missing full stop after “full initiation rite”.
- Added a persistent full-name pronunciation proposal and a broadly modern article viewpoint with the separately dated 1748 account recorded in `povNotes`.

### Validated judgments
- The article provides the cult's home, scale, practices, central protective function, and consequences of the 1748 attacks. Its modern reference frame is distinct from the explicitly dated retrospective paragraph.
- The positive `dm_notes` attestation has confirmed local evidence; private source contents have not been incorporated into this report.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed complete pronunciation `SHAH-koon mis-TIE`. The Shakun component follows the accepted `SHAH-koon` in [[Temple of Shakun]]; the remaining component uses the Persian side of the Hindi/Persian Dunmari analogue in [[Languages]], adapting written y to short i, retaining st, and reading ai as eye. Final stress is a reading aid; a Hindi-oriented ai could suggest eh instead. No complete-name pronunciation or language is established. Accept or revise the proposal, then copy the accepted full pronunciation to frontmatter and mark the entry documented.
- [ ] **Suggestion — temporal.date_scope:** The existing `Date:1748` wrapper exposes the whole retrospective paragraph from the beginning of the year, including its November state and the initiations established in [[Session 26 (DuFr)]] on May 24 and [[Session 32 (DuFr)]] on June 17. Choose whether to preserve this as one November retrospective or separate its dated layers. The smallest copy-ready correction is to replace the opening marker's value `Date:1748` with `Date:1748-11`, preserving the paragraph and closing marker; this deliberately defers the entire retrospective until November. Alternatively split the April attacks, May 24 abbreviated ritual, June 17 initiation, and November strength assessment into separately dated passages. No visibility-changing edit has been applied.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Candrosa (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 17]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 18]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 1/Character Intros]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 1/The Attack and the Aftermath]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 43]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Karawa/Shakun Ritual]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 27]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 28/Session 28]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Shakun's Heart Overview]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra Arc Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Backstory]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Faction Action]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Secrets of Karawa]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/The Mystery Cult of Shakun]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/The Mystery of Shakun]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/DM Version - Shakun Initiation Rite]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
%%^End%%

---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
displayDefaults: {ruledBy: "Ruled by: <name> <((since )startDate())>"}
tags: [place, status/review, status/check/lint]
typeOf: realm
typeOfAlias: monarchy
name: Sembara
aliases: [Sembaran]
pronunciation: sem-BAH-rah
whereabouts: Greater Sembara
dm_owner: joint
dm_notes: important
POV: modern
---
# Sembara
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% status/review ->  significant in multiple games (Addermarch, and especially Cleenseau) and page is currently essentially a stub considering importance %%

Sembara is a large and prosperous realm in the [[Western Green Sea]] situated amongst five great rivers that pour down from the [[Sentinel Range|Sentinels]] to the [[Western Gulf]].  One of the few realms in the east to survive the Blood Years largely intact, Sembara is a hereditary monarchy with a large nobility and considerable prowess at arms. Sembara invests significantly in defensive fortifications in the [[Western Marches]], on the western (mountain) borders of the realm. These areas are under threat from hobgoblins, aberrations, and other incursions from the wilds, and the defense of these borders is a major concern for the ruling class. While most of the Sembaran population descends from the Drankorians who conquered the land, in the highlands traces of the original culture survive. And in Tyrwingha, ancient connections to the Archfey who once protected the realm still linger.

Lord's guards are common even in Sembaran villages. Larger towns have more guards and soldiers, and walled towns are more common than in [[Tyrwingha]].

Some important facts about Sembara:

- Inward agricultural focus. Sphere of influence pushing more west and interior than into the [[Western Gulf]] - limited or no real navy, small scale fishing but not a major part of the culture or economy (think China)
- Trade devalued -- historical analog: ancient Rome, where wealth from land was much more significant than wealth from trade
- Very fertile soil and rich agricultural harvests in the heart of Sembara drive the economy. Major exporter of foodstuffs and raw materials. Also higher population density than anywhere else between the good soil and the miracle that the heartland of Sembara has never been overrun by anything too bad since even before the Drankorians relatively gently took over
-   Landed barons and dukes dominate local politics
-   Very good relationship with halflings, who are the favored traders, and have formal rights of free passage and access to markets across Sembara.
-   Cooler relationship with dwarves -- not at all hostile, but dwarves are more aligned with the highland kingdoms, esp Ardlas and Lavnoch
-   Close relationship with lizardfolk, who have played an outsized role in Sembara’s history and establishment of [[House of Sewick]].
-   Elves very rare in Sembara, with little direct political contacts; largest Elven settlement nearby is the semi-mythical kingdom of [[Orenlas]] in the forests surrounding a supposedly enchanted lake south/southeast of Tyrwingha in the Cymea foothills.
-   Stoneborn are also very rare in Sembara; mostly in the high peaks north of Ulrich devastation; more common in Northlands than elsewhere, coming from the [[Vostok]] highlands
## Royal Council

The Royal Council brings together the monarch and major vassals, especially the dukes of Sembara, Wisford, Telham, Arnsbury, Cheimin, and Seham. Raising certain taxes, including a war tax, requires their assent. Major changes to the army, declarations of a new heir, certain legal decrees, and accusations against a duke would usually be presented to the council for its assent. In a crisis, counsel and support are also duties that vassals owe their lord.
## Learned Magic

Sembaran suspicion falls chiefly on learned magic: studying how magic works in order to use and extend that knowledge. It does not extend equally to all spellcasters. A lone wizard and apprentice may be regarded as eccentric or dangerous, but an organized school of magical research would face much stronger opposition. Wizards are not hunted on sight; some leave for places such as Tollen or Chardon, and the scarcity of teachers makes them rarer in Sembara. Innate magic, even wild sorcery, generally draws less suspicion.

Many Sembarans point to the story of Anne's attempt to use a geas against her twin sister [[Elaine I]], and to the Cursed Cold that followed the next year, as warnings about magical study. The belief that Anne's magic caused the Cursed Cold is not established fact.

## Map

```leaflet 
id: region-map-sembara
image: [[[sembara-regions.png]]] 
bounds: 
- [0,0]
- [2468, 2308]
height: 900px
lat: 1200
long: 1200
minZoom: -1
maxZoom: 3
defaultZoom: 0
unit: miles 
scale: 0.5
```

%%^Campaign:None%%
### Cities in Sembara
```dataviewjs
const { util } = customJS
dv.table(["Place", "Region", "Type Of", "Population"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.file.frontmatter.typeOf == "settlement"))
				.sort(f => util.s("<home:1>", f.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<home:1>", b.file, dv.current().pageTargetDate), util.s("<maintype>", b.file, dv.current().pageTargetDate), util.s("<population>", b.file, dv.current().pageTargetDate)]))
```

%%^End%%

%%^Metadata:names:v1%%
- {name: Sembara, language: unknown, pronunciation: sem-BAH-rah, status: documented, notes: "Explicit pronunciation of the Sembara component recorded in the frontmatter of [[Greater Sembara]]; the name's source language is not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the realm's geography, institutions, and culture, with selected older historical references; the article does not yet account for the DR 1720 devastation in southern Sembara.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting without changing the header version or existing field values.
- Added the pronunciation recorded for the Sembara component in [[Greater Sembara]], a persistent name entry retaining the unknown name-language, and a modern POV with temporal-coverage guidance.
- Corrected “properous” to “prosperous.”

### Validated judgments
- `status/review` remains supported by the central gaps identified below; the existing editorial reminder is preserved.
- Confirmed local `_DM_` matches support the positive human attestation; their contents remain private.
- The undated geography and institutional account has a broadly modern frame. The learned-magic section correctly distinguishes the reported attribution of the Cursed Cold from an established cause; [[Attempted Geas of Elaine I]] and [[Cursed Cold]] support the sequence of events.
- This realm does not require settlement, road, or waterway map metadata. The existing map and generated navigation table are preserved.

### Editorial assessment
**Underdeveloped** — The realm overview omits its capital and regional organization, the founding of the modern monarchy and its relationship with Tyrwingha, and the major DR 1720 disruption of southern Sembara. These are central established dimensions for this major realm, rather than a request for additional invented detail. The smallest useful scope is two short sourced overview paragraphs and a bounded treatment of the undead crisis.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** A major-realm overview needs its political and geographic center and the origins and present relationship of its crowns. The article names a council and a royal house but omits the capital, territorial outline, founding, and personal union. [[Embry]], [[Heartlands]], [[Northlands]], [[Western Marches]], [[Borderlands]], [[Derik I]], [[Treaty of Wisford]], and [[Tyrwingha]] establish these facts. Bounded addition: “[[Embry]], on the [[Semb]], is the capital and seat of the royal court. The fertile [[Heartlands]] form the agricultural core of the realm; the [[Northlands]] lie between the [[Teft]] and [[Volta]], while the [[Western Marches]] are a sparsely populated military frontier and the [[Borderlands]] south of the [[Enst]] comprise baronies largely established after the hobgoblin wars. [[Derik I]], founder of the [[House of Sewick]], established modern Sembara at the [[Treaty of Wisford]] in DR 1429. Sembara and [[Tyrwingha]] share a monarch in a personal union, while retaining distinct histories and cultures.” This supplies orientation and political identity without importing tentative treaty terms or a campaign log.
- [ ] **Warning — coverage.later_material_change:** The modern overview omits the [[Undead Attacks in Sembara|DR 1720 undead crisis]], whose visible event account records devastating attacks in southern Sembara, especially Wisford, Dunfry, and Ainwick, including destroyed villages. The economic bullet’s sweeping claim that the heartland has never been overrun by “anything too bad” needs qualification against that record. Choose whether to update the overview and its temporal framing, defer the crisis under the appropriate game-update status, or intentionally retain an earlier snapshot and narrow its POV. Bounded update candidate: “In early DR 1720, [[Undead Attacks in Sembara|undead attacks]] devastated parts of southern Sembara, especially [[Wisford]], [[Dunfry]], and [[Ainwick]], destroying entire villages in some places.” Replace the sweeping immunity claim with the supported point about fertile soil and agricultural wealth; the degree and timing of subsequent recovery are not established by that event account.
- [ ] **Suggestion — editorial.reference_voice:** The visible “Some important facts about Sembara” list retains author-facing shorthand and real-world comparisons, especially “(think China),” “historical analog: ancient Rome,” and “between the good soil and the miracle ... anything too bad.” Rewrite this bounded list into in-world reference prose, preserving its supported distinctions about agricultural wealth, landed political power, halfling rights, and the differing relationships with other peoples. Resolve the indefinite “limited or no real navy” against the small navy described in [[Sembaran Army]] and [[Northlands]], retaining the army note’s uncertainty about later organization. This is a human rewrite; the surrounding finished Royal Council and Learned Magic sections do not need a stylistic rewrite.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated cities table opens with `%%^Campaign:None%%`; the adopted private sentinel is `%%^Campaign:none%%`. Copy-ready proposal: replace only that opening marker with `%%^Campaign:none%%`, preserving the complete table and End marker. Apply after confirming equivalent private filtering or approving the visibility change; the existing block is preserved in this lint.

### DM evidence
- [[_DM_/Brainstorming/Campaigns Overview]]
- [[_DM_/Brainstorming/Family Campaign Ideas]]
- [[_DM_/Brainstorming/Misc Random Ideas]]
- [[_DM_/Brainstorming/One Shot Ideas/Monster Hunters]]
- [[_DM_/Brainstorming/One Shot Ideas/One Shot Ideas]]
- [[_DM_/Dunmar Epilogues]]
- [[_DM_/Lost in the Feywild World Notes]]
- [[_DM_/Meta/Map Notes]]
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/Secret Worldbuilding/Language and Culture From OneNote]]
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/_Campaign 3/Campaign 3 - Early Brainstorming - Overview]]
- [[_DM_/_Dunmari Frontier/Brainstorming - DM]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Apollyon (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Monastery of Bhishma/Text]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Festival Visitors and NPCs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Travel to Raven's Hold/Journey North]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 1/Character Intros]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Darba/Darba (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 45]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 26-0]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Wellby Solo Arc/Session 2 - Wellby]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Part II Finding the Te'kula/Baz'aku (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Lakan Monastery/Notes from Kassi]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 35]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 37]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra Area Map/Tokra Area Map]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Clues]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Brainstorming]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Pitch]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Summary]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Calendar Eras - DuFr Player Background]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Dates - Dunmar Campaign Player Background]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Kenzo (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Seeker (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Wellby (OneNote)]]
- [[_DM_/_Dunmari Frontier/Fox and Hunter Intro]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/DM Version - Bhishma Monastery]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Timeline for the End of Drankor]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Desolation of Cha'mutte Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Isingue Arc Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/The Story of Apollyon and Cha'mutte]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 64 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Tollen DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 81 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/North Coast Brainstorming]]
%%^End%%

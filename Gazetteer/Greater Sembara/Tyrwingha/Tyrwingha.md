---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/text, status/check/lint]
typeOf: realm
typeOfAlias: monarchy
name: Tyrwingha
aliases: [Tyrwinghan]
whereabouts: Greater Sembara
dm_owner: joint
dm_notes: important
POV: modern
---
# Tyrwingha
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% I have various session planning and especially intra-session emails that impinge on Tyrwingha %%

The land of Tyrwingha, nestled on the southern shores of the [[Green Sea]], is ruled by the monarch of [[Sembara]] in a personal union of the crowns.  Over its history, it has been united with Sembara on two separate occasions, most recently by [[Elaine I]].

Although they share a monarch, Tyrwingha and [[Sembara]] see themselves as distinct monarchies with unique histories and cultures.

It is a land of few cities beyond the capital, [[Tafolwern]], but is a land rich in magic and tradition. The [[Archfey Ethlenn]], the Queen of the Evening Mist, is said to have been watching over Tyrwingha since time immemorial, and the Tyrwinghans see themselves as the inheritors of an ancient and sacred tradition.  

Bordered by the [[Green Sea]] in the north and the [[Mostreve Hills]] in the south, it is an agriculturally fertile land and thrives on rich harvests of wheat and wine, as well as timber from the northern slopes of the [[Mostreve Hills]]. Although not a backwater exactly, it is economically somewhat isolated from the main trade routes of Greater Sembara, and mostly lives and dies with the harvest.

Politically, it is a monarchy, although the monarch is formally elected by the [[Oracle of the Riven]] (or as they are more prosaically known, the royal electors). Traditionally, the Oracles are warlocks, although like Ethlenn's vote, this tradition is not always observed in the modern day. Second in importance to the oracles are the earls, high lords of the realm. Today, the title has been exported to has lost some of its traditional meaning -- a noble who had pledged loyalty to Ethlenn in her court. Nonetheless the earls are powerful lords in Tyrwingha, and often control significant landholdings, although freeholds are also more common here than elsewhere in Greater Sembara, and small, independent villages without a lord are not so rare. 

%% Note: There are some important details about earls not captured here; nothing is wrong per-se but use with caution - the conversation was mostly in Discord but some of [[Celyn]] background stories shed light as well %%

The [[Army of Mostreve]] is another major part of Tyrwingha. 

Religiously, little is remembered about the ancient gods of Tyrwingha, such as they were. The [[Mos Numena|Eight Divines]] are worshipped here much as they are elsewhere in [[Sembara]]. It is said that when Ethlenn made her bargain with the Drankorians (see below), she acknowledged the suzerainty of the Drankorian gods. However, the fey are remembered and honored alongside the gods -- the people of Tyrwingha have a deep respect for the traditions of the fey and what others might call superstition is here seen as simple common sense. The temple stewards in Tyrwingha often have a second job, ensuring the fairy rings are not disturbed, leaving out milk and brown bread for the pixies, and other such things.


%%^Campaign:None%%
### Places in Tyrwingha
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%
%%^Campaign:None%%
### Cities in Tyrwingha
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
- {"name": "Tyrwingha", "language": "unknown", "pronunciation": "tuhr-WING-hah", "notes": "Proposed from the Welsh analogue for Tyrwinghan in [[Languages]]: a nonfinal y approximated by uh, consonantal w, ng as in sing followed by h, final a as ah, and penultimate stress. Segmentation and exact vowels are uncertain; the name-specific language is unconfirmed and this is not accepted in-world phonology.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the subject in the current campaign era; the article does not require a narrower temporal reading position.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported name and/or map metadata where absent and a temporal viewpoint with coverage guidance; normalized frontmatter where needed.
- Corrected “has been been united” to “has been united” (objective duplication).
- Corrected “the most recently by” to “most recently by” (objective grammar).
- Corrected “fairy rings are not distributed” to “fairy rings are not disturbed” (objective typo).

### Validated judgments
- `status/cleanup/text` remains supported by the damaged earls sentence and unresolved source synthesis; the tag is preserved.
- Confirmed local `_DM_` matches support the positive human attestation; their contents remain private.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or replace the proposed `tuhr-WING-hah` in the name block. The Welsh analogue for Tyrwinghan in [[Languages]] motivates nonfinal y as uh, consonantal w, ng as in sing followed by h, final a as ah, and penultimate stress. Segmentation, vowels, and the exact name-language are unconfirmed, so this remains a proposal rather than adopted phonology.
- [ ] **Warning — correctness.cross_note_conflict:** The political paragraph says freeholds are common and independent villages without a lord are not rare. [[Political Organization of Tyrwingha#Taxes and Land Organization]] instead says the freehold/crownhold distinction does not exist and land is held in trust for Ethlenn; its Village Organization section describes Courts of All and service owed through earls. Resolve how these terms and obligations fit together. The alternative folkland/service model in [[2024-03-17 - Tyrwingha]] is provisional Worldbuilding, not authority to replace either canonical account. Nearby comment candidate: `%% Political terminology unresolved: this article describes common freeholds and lordless villages, while [[Political Organization of Tyrwingha]] describes land held in trust for Ethlenn and villages owing service through earls. Reconcile tenure and village obligations; the alternative in [[2024-03-17 - Tyrwingha]] remains provisional. %%`
- [ ] **Warning — editorial.prose_clarity:** The earls paragraph contains the damaged sentence “Today, the title has been exported to has lost some of its traditional meaning -- a noble who had pledged loyalty to Ethlenn in her court.” The destination after “exported to” is missing. Confirm the intended export claim, or use the bounded candidate “Today, the title has lost some of its traditional meaning: a noble who had pledged loyalty to Ethlenn in her court.” Do not invent a destination.
- [ ] **Suggestion — editorial.prose_clarity:** The religious paragraph directs readers to Ethlenn’s Drankorian bargain “(see below),” but no account follows. Replace that broken reference with “(see [[Treaty of Tyrwingha]])”. The event note establishes the agreement and signatories, while its detailed terms remain explicitly dubious; the link must not be used to promote that hidden draft.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** Both private navigation tables use `%%^Campaign:None%%`. Proposed spelling for each is `%%^Campaign:none%%`, preserving every table and end marker. This lint leaves the originals intact because equivalent filtered visibility has not been established; apply only after human approval or such proof.

### DM evidence
- [[_DM_/Brainstorming/Family Campaign Ideas]]
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/_Campaign 3/Campaign 3 - Early Brainstorming - Overview]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Lakan Monastery/Notes from Kassi]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Seeker (OneNote)]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 129 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
%%^End%%

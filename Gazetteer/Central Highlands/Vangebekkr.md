---
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: building
typeOfAlias: castle
ancestry: frost giant
campaignInfo:
  - {campaign: GL, type: assaulted by, date: 1747-12-15, wParty: "<met:U> <person> on <target>"}
name: Vangebekkr
whereabouts: Sentinel Range
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

Vangebekkr is an old frost giant castle in the high peaks of the [[Sentinel Range]]. 

%%^Campaign:GL%%
In DR 1747, it was occupied by the frost hag [[Morgana Stoneclaw|Morgana Frostclaw]], and many of the frost giant inhabitants were turned to her evil ways. Upon her destruction by the [[Silver Tempests]], the castle was left under the control of several frost giant prisoners rescued from her dungeons. 
%%^End%%

%%
GL Arc 3: assault on the castle; freed giants retook the halls while the party pursued the hag below.

No real history developed. In the Great Library arc, a hag had corrupted the majority of the frost giants, but some remained imprisoned, who were freed by the party. More details in:
- [[GL - Session 44 - DM Notes|GL - Session 44 - DM Notes]]
- [[GL - Session 45 - DM Notes|GL - Session 45 - DM Notes]]
- [[GL - Session 47 - DM Notes|GL - Session 47 - DM Notes]]
- [[Vangebekkr - DM Notes]]

%%

%%^Metadata:names:v1%%
- {name: Vangebekkr, language: unknown, pronunciation: VAHNG-eh-bekr, status: proposed, notes: "Proposal informed by the Giant analogue to Old Norse in Languages: initial stress, a as ah, e as a short eh, retained ng, hard kk, and an audible final r. The name's language and exact in-world phonology are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern castle identity with a retrospective account of Morgana's occupation and the frost giants' recovery of the castle in DR 1747; later ownership is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Corrected the objective grammar error `who were free by the party` to `who were freed by the party` in the existing comment.
- Added persistent name metadata with a proposed pronunciation, plus `POV: modern` and temporal coverage.

### Validated judgments
- [[Great Library Session Notes - Arc 3]] corroborates Morgana's occupation and the prisoners' recovery of their castle. These are durable changes to the castle and appropriately remain part of its reference account.
- The reviewed local timeline cluster duplicates the shared campaign account or records incidental party events; it offers no useful additional castle material. `dm_notes: none` remains unchanged.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent entry proposes `VAHNG-eh-bekr`, informed by the Giant/Old Norse analogue in [[Languages]]: initial stress, a as ah, short eh vowels, retained ng, a hard kk, and an audible final r. This is an analogue-informed proposal; the name's own language and exact in-world phonology are unestablished. Accept or revise the stored proposal; if accepted, copy the primary pronunciation to frontmatter and set the entry to `status: documented`.
- [ ] **Suggestion — editorial.shared_material_redundant:** The ordinary comment's `GL Arc 3: assault on the castle` summary and its explanation that Morgana corrupted the giants while the party freed prisoners substantially repeat the visible campaign paragraph. Remove that repeated summary while retaining the distinct editorial limitation and the four source pointers. A bounded replacement comment is: `No earlier castle history developed. More details in [[GL - Session 44 - DM Notes]], [[GL - Session 45 - DM Notes]], [[GL - Session 47 - DM Notes]], and [[Vangebekkr - DM Notes]].` This retains the research route without duplicating the article or publishing encounter material.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** Both existing `%%^Campaign:GL%%` opening markers resolve to Great Library in [[Campaign Registry]], whose canonical code is `grli`. The exporter matches selected codes without resolving this alias, so changing them can change filtered visibility. Preserve the legacy markers until a human coordinates the export selections and consumers. The exact proposed migration is `%%^Campaign:GL%%` → `%%^Campaign:grli%%` at both the header interaction and body account; the matching `%%^End%%` markers remain unchanged.
- [ ] **Suggestion — campaign.noncanonical_code:** The existing campaignInfo entry uses `campaign: GL`; [[Campaign Registry]] specifies `campaign: grli`. Preserve the stored alias pending the coordinated marker/filter migration above, because header generation emits the entry's campaign value and campaign-specific runtime lookup can compare it literally. If adopting the migration, replace only `campaign: GL` with `campaign: grli` in the existing dictionary; retain its other values.
%%^End%%

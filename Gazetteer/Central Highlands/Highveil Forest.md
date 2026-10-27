---
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: forest
campaignInfo:
  - {campaign: GL, type: explored, date: 1747-10-21, wParty: "<met:u> by <person> on <target>"}
name: Highveil Forest
whereabouts: Central Highlands
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

A light, open forest on the western foothills of the [[Sentinel Range|Sentinels]], north of the [[Crimson Forest]] and south of the [[Forest of Nightmares]].  While once this forest was occupied by many elves, it is now only lightly settled by [[Deno'qai]] tribes. 

Called Saharlûn (sa-har-LOON) by the [[Deno'qai]], and Taurelóme (TAU-re-LO-meh) by the elves. 

%%^Campaign:GL%%
In DR 1747, the [[Silver Tempests]] met some [[Deno'qai]] here, and [[Great Library Session Notes - Arc 3|negotiated safe passage in exchange for dealing with a spider threat]]. 
%%^End%%

%% DM
GL Arc 3: southern approach to Am’khazar.

north of [[Crimson Forest]] and south of Forest of Nightmares. Deno'qai, from Great Library adventures.

Saharlûn (sa-har-LOON), “gentle slopes” that echo  dawnlight on the mountains.

(Elven) the forest of dusk.

Highveil Forest - Drankorian/Chardon name

See:
[[Travel Zones - Overview]]
[[Spider Woods - DM Notes]]
[[Northerners Territory - DM Notes]]

%%

%%^Metadata:names:v1%%
- {name: Highveil Forest, language: unknown, status: documented}
- {name: Saharlûn, role: "Deno'qai name", language: "Deno'qai", pronunciation: sa-har-LOON, status: documented, notes: "The visible article records this name and pronunciation."}
- {name: Taurelóme, role: elven name, language: Elvish, pronunciation: TAU-re-LO-meh, status: documented, notes: "The visible article records this name and pronunciation."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern forest geography and settlement, with a separate account of the Silver Tempests' DR 1747 passage; the recorded visit month requires reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Corrected the objective ordinal error `October 21th` to `October 21st`, preserving the recorded month pending review.
- Added persistent name entries for Highveil Forest, Saharlûn, and Taurelóme, retaining the two recorded pronunciations; added `POV: modern` and temporal coverage.

### Validated judgments
- Highveil Forest is an ordinary English compound needing no separate pronunciation guide; the two other displayed forms have explicit pronunciations in the visible article.
- The forest's geography, former elven occupation, and light Deno'qai settlement provide an adequate bounded reference account. No local `_DM_` candidates were found in the prepared dossier.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** The header and campaignInfo place the Silver Tempests' exploration on October 21, 1747, while [[Great Library Session Notes - Arc 3]] (Session 39 and its Events list) places entry into the forest and the agreement at Raha on November 21, 1747. Reconcile the target against that played chronology. If adopting the session date, replace the campaignInfo date with `1747-11-21` and the header phrase with `Explored by the [[Silver Tempests]] on November 21st, 1747`; keep the existing campaign visibility.
- [ ] **Suggestion — editorial.shared_material_redundant:** The ordinary `%% DM` comment repeats the north-of-Crimson/south-of-Forest-of-Nightmares geography, Deno'qai association, and the Saharlûn pronunciation already visible above. Remove those duplicate statements or retain only the distinct name-meaning/name-origin guidance and source pointers. A bounded retained comment could read: `GL Arc 3: southern approach to Am’khazar. Name guidance for review: Saharlûn, “gentle slopes”; Elven name, “forest of dusk”; Highveil Forest, Drankorian/Chardon name. Sources: [[Travel Zones - Overview]], [[Spider Woods - DM Notes]], [[Northerners Territory - DM Notes]].` The retained name guidance remains noncanonical pending human adoption.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** Both existing `%%^Campaign:GL%%` opening markers resolve to Great Library in [[Campaign Registry]], whose canonical code is `grli`. The exporter matches selected codes without resolving this alias, so changing them can change filtered visibility. Preserve the legacy markers until a human coordinates the export selections and consumers. The exact proposed migration is `%%^Campaign:GL%%` → `%%^Campaign:grli%%` at both the header interaction and body account; the matching `%%^End%%` markers remain unchanged.
- [ ] **Suggestion — campaign.noncanonical_code:** The existing campaignInfo entry uses `campaign: GL`; [[Campaign Registry]] specifies `campaign: grli`. Preserve the stored alias pending the coordinated marker/filter migration above, because header generation emits the entry's campaign value and campaign-specific runtime lookup can compare it literally. If adopting the migration, replace only `campaign: GL` with `campaign: grli` in the existing dictionary; retain its other values, with Highveil's date subject to its separate chronology finding.
%%^End%%

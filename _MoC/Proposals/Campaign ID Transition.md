# Campaign ID transition

November 20, 2026. The Taelgar vault and Taelgarverse Core changes are committed locally on `main`. The installed Obsidian plugin was rebuilt locally. Production deployment is separate.

## Where to edit a campaign

Use the key in `_sessions/campaign-registry.json` wherever a note or tool identifies a campaign. The value points to the editable Markdown note under `Campaigns/_Index`. Edit the note to change the display name, description, DM, canon, continuity, or configured paths and template. For example, `campaign: gsea` identifies The Green Sea Campaign. The existing `greensea` hostname continues to select its website homepage.

## What changed

| Area | Change |
|---|---|
| Vault tools | The session-note builder, templates, CustomJS headers, validator, entity review, transcript lookup, asset audit, place-name analysis and combat analysis read the index. Beat and recap preparation resolve the owner of an existing bundle on read. New registered source-preparation inputs use the ID and reruns locate an existing bundle by session, including fractional numbers. |
| Obsidian and website | Shared registry data supplies campaign views, session references, party pages, latest-session contexts and interaction ownership. Both Dataview materializers initialize the current campaign metadata. The local website and Cloudflare content-preparation path use the same website loader. Existing bookmarks resolve to canonical contexts. |
| Vault metadata | 530 Markdown files received 586 identifier substitutions. These comprise 419 ownership values, seven nested `campaignInfo` values, 23 `knownTo` values, 90 conditional blocks, 43 game-update tags, three dashboard tag references, and one homepage campaign selection. The Labyrinths Dataview comparison also changed to `lablost`. The ordinary-note edit rule added `status/check/ai` to 521 notes. |
| Operational data | Migrated 15 source-preparation configurations, 20 queued Addermarch manifests and the Dunmar timeline’s campaign field. The People Known To dashboard uses the registry. The campaign timeline shows index-note display names. |
| Derived data | Regenerated Name Explorer from the current vault. Its evidence now covers 753 places and 238 session records across ten campaigns. Reviewer decisions were preserved. The dated combat tables carry canonical IDs and display names for 160 session rows and 150 encounters. |
| Retirement | Removed `_scripts/session_note_campaigns.json` and the duplicate campaign array in `.obsidian/metadata.json`. Other Obsidian metadata is preserved. The original reviewed `_MoC/campaigns.json` is byte-identical to its checkpoint version. |

## Campaign-by-campaign crosswalk

The third column lists historical machine identifiers or lookup spellings. The final column counts the 586 changed Markdown values and references described above. A zero means the campaign had no such value to rewrite. Register-only spellings remain in the historical register.

| ID | Display name | Previous spellings | Changes |
|---|---|---|---:|
| `adma` | Addermarch Campaign | `addermarch`, `Addermarch`, `Addermarch Campaign`, `ADMA` | 28 |
| `clee` | Cleenseau Campaign | `cleenseau`, `Cleenseau`, `Cleenseau Campaign`, `Clee` | 114 |
| `dufr` | Dunmari Frontier Campaign | `dunmar-frontier`, `Dunmar Frontier`, `Dunmari Frontier`, `Dunmari Frontier Campaign`, `Dunmar Frontier Campaign`, `DuFr`, `dunmar`, `dunmari` | 290 |
| `grli` | Great Library Campaign | `great-library`, `Great Library`, `Great Library Campaign`, `GL`, `gl` | 88 |
| `greatwar` | Great War Campaign | — | 0 |
| `mawar` | Mawar Adventures | `mawar-adventures`, `Mawar Adventures`, `Mawar` | 9 |
| `oskar` | Oskar's Adventures | `oskars-adventures`, `Oskar's Adventures`, `oskar-s-adventures` | 2 |
| `chasm` | Into the Chasm | `into-the-chasm`, `itc`, `Into the Chasm` | 34 |
| `feywild` | Lost in the Feywild | `lost-in-the-feywild`, `Lost in the Feywild`, `litf` | 12 |
| `lablost` | Labyrinths of the Lost | `labyrinths-of-the-lost`, `Labyrinths of the Lost`, `ll`, `lab lost` | 5 |
| `dragonets` | Dragonets | `dragon`, `dgnt`, `Dragonets`, `Dragonets Campaign` | 4 |
| `elderwood` | The Elderwood Heist | — | 0 |
| `plaguelands` | The Plaguelands Campaign | — | 0 |
| `aucross` | The Murder at Ausson's Crossing | `ausson` | 0 |
| `stonetitan` | The Stone Titan Adventure | — | 0 |
| `mikefam` | Mike's Family Game | `mikefamily` | 0 |
| `informatics` | Informatics One Shot | — | 0 |
| `tollenfate` | The Curse on the Bridge | — | 0 |
| `tollendnd` | The Haunted Clocktower | — | 0 |
| `alex2017` | Taelgar-17 One Shot | `alexandria`, `alex2019` in an older backup | 0 |
| `gsea` | The Green Sea Campaign | `greensea` (the draft also proposed `grse`) | 0 |
| `stars` | Stars and Stories Crossover | `starsstories` | 0 |

## Compatibility and verification

- All 22 index entries loaded. For all ten formerly configured campaigns, the actual website selected the same latest published session source and DR date as before. Dragonets retained its source and its missing full DR date. The Great War landing page and the Green Sea intro gained the correct campaign owner. Every previously assigned website page retained its owner.
- The real Green Sea homepage selected `chasm`, `dufr`, `feywild` and `mawar` at DR 1752-05-10. Both the old Dunmar bookmark and the canonical one rendered identical HTML and interactions for Johar. All 58 website recaps parsed, matched a registered bundle directory and had no conflicting registered identity. Campaign index notes contributed no published articles.
- All 71 existing note session keys and 17 distinct audio embed destinations were verified in the migrated vault. The 530 changed Markdown files preserved all 23,457 wikilinks, including targets and aliases. No page, session directory or audio file was renamed. Oskar’s Adventures retains its note path and has no session bundle directory.
- The website and Obsidian suite passed all 1,878 tests. Vault checks passed for the builder (43), validator (62), batch lint (59), entity review (85), transcript processing (85), source preparation (9), beat annotation (15) and session summaries (35). Seven finalized bundles also passed the opt-in transcript resumption check on temporary copies as part of the transcript suite. A final identifier scan found no remaining substitutions in active Markdown and no frontmatter parse failures in the candidate set.
- Six lines touched by the ID edits already ended in whitespace, including Markdown hard breaks. The migration preserved their exact endings.

## Historical records and follow-up

**Prepared session records.** All 203 existing prepared manifests resolve to their canonical IDs through the registered bundle directories. Their original bytes and recorded campaign labels were preserved. A hash inventory found 163 manifests directly referenced by exact content fingerprints. Other review tools also compare a semantic digest of session metadata. Editing those source labels in place would invalidate existing evidence or call for new human acknowledgments. Published recaps and transcript source archives retain their historical wording. Newly generated beat and recap contexts receive the canonical ID.

**Existing gaps.** The earlier test copy found complete generated components for 29 of 71 keyed notes. The remaining 42 were Cleenseau notes. Cleenseau sessions 37 and 38 also lacked prepared manifests. This migration preserves existing keys and working paths and introduces no new components for those historical gaps. Dated proposals, older register backups, historical lint findings, and frozen test fixtures can still quote retired spellings.

**Combat analysis.** The current analysis code ran successfully to completion. A fresh calculation uses more recent segment and combat inputs for the same historical sessions and produces different timing figures and source hashes. The committed CSVs keep the published snapshot. A field-by-field comparison confirmed that only `campaign_key` and the human-readable `campaign` changed. Consequently `analyze.py --check` still detects older analysis data. A full analytical refresh is a separate decision.

**Release.** Reload Obsidian to pick up the locally installed plugin. When publishing, make the Core revision available on remote main before triggering vault content publication, because the vault workflow checks out the publisher from Core main. This transition included no push, release tag or production deployment.

## Commit trail

### Taelgar

- `b7f69f191` Checkpoint before campaign ID cutover
- `d2874f7a5` Use campaign index IDs in vault tools and session templates
- `4865ad64f` Retire the ten-campaign registry and route remaining vault tools through the index
- `a52be9620` Preserve campaign lookup in the standalone materializer and test bundle reruns
- `1afb142c4` Use registered IDs in new recap data from fingerprinted session sources
- `1425665e7` Migrate authored campaign IDs, review queries and session preparation inputs
- `324640e9d` Refresh campaign IDs in Name Explorer and historical combat tables
- `f1d7efff4` Exercise canonical transcript lookup against existing session bundles

### Taelgarverse Core

- `6389c49` Checkpoint before campaign ID cutover
- `f9ad368` Load Obsidian campaign views from the index notes
- `c915b53` Build website contexts and campaign histories from the vault index
- `3ead8cc` Keep the legacy header characterization fixture at its original revision
- `810c8df` Resolve historical campaign bookmarks to the new IDs
- `24f8b6b` Initialize campaign data during legacy Dataview materialization

## File inventory

Each entry is the net change from the pre-cutover revision through the implementation commits. The inventory omits this report itself. Paths are relative to their respective repositories. The affected code lives in Taelgar and Taelgarverse Core. The legacy static website and utilities repositories required no changes.

### Taelgar

<details><summary>.agents · 17 files</summary>

```text
M  .agents/skills/beat-annotator/scripts/extract_beat_context.py
M  .agents/skills/check-session-entities/references/review-workflow.md
M  .agents/skills/check-session-entities/scripts/entity_review.py
M  .agents/skills/check-session-entities/scripts/entity_review_staging.py
M  .agents/skills/check-session-entities/tests/test_entity_review_staging.py
M  .agents/skills/check-session-entities/tests/test_entity_review_table.py
M  .agents/skills/illustrate-note/SKILL.md
M  .agents/skills/lint-taelgar-note/SKILL.md
M  .agents/skills/prepare-session-source/SKILL.md
M  .agents/skills/prepare-session-source/assets/source_prep_config.template.yaml
M  .agents/skills/prepare-session-source/scripts/prepare_source.py
M  .agents/skills/prepare-session-source/tests/test_prepare_source.py
M  .agents/skills/process-transcript/SKILL.md
M  .agents/skills/process-transcript/scripts/transcript_pipeline.py
M  .agents/skills/process-transcript/tests/test_existing_bundles.py
M  .agents/skills/review-linked-notes/SKILL.md
M  .agents/skills/session-summary/scripts/build_session_summary_context.py
```

</details>

<details><summary>.obsidian · 2 files</summary>

```text
M  .obsidian/metadata.json
M  .obsidian/plugins/taelgar-dataview-materializer/main.js
```

</details>

<details><summary>(root) · 2 files</summary>

```text
M  AGENTS.md
M  SKILLS.md
```

</details>

<details><summary>Campaigns · 420 files</summary>

```text
M  Campaigns/Addermarch Campaign/Addermarch - Session 01.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 02.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 03.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 04.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 05.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 06.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 07.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 08.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 09.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 10.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 11.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 12.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 13.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 14.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 15.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 16.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 17.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 18.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 19.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 20.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 21.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 22.md
M  Campaigns/Addermarch Campaign/Addermarch - Session 23.md
M  Campaigns/Addermarch Campaign/Addermarch Campaign.md
M  Campaigns/Addermarch Campaign/Handouts/Letter from Elowen Duval.md
M  Campaigns/Addermarch Campaign/Handouts/Letter from Owen Tavish.md
M  Campaigns/Addermarch Campaign/Handouts/Marshal Brask's Letter.md
M  Campaigns/Addermarch Campaign/Handouts/The Story of Sweetwillow.md
M  Campaigns/Campaign Timeline.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/A Letter to the Magistrate.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/An Excerpt from On Creation and Destruction of Extra-Material Realms.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Celyn's Letter to His Brother Pryce.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Ida's Letter.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Letter from Alaric Lord Mayor of Rinburg.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Letter from Ellis to Celyn.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Letter from Enford.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Letter from Mahaut to Celyn.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Letter from Rosalind (January 14th).md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Letter from Rosalind (January 21st).md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Letter from Rosalind (January 26th).md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Letter from Rosalind (January 6th).md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Letter from Rosalind (January 8th).md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Letter from Susanne Garay to Viepuck.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Letter from the Oracle of the Red to the Mostreve Warlocks.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Report on the Bogblight.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Sendings/Viepuck - Feburary 9th, 1720.md
M  Campaigns/Cleenseau Campaign/Letters and Other Writings/Stories of Tyrwingha for Profit.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Interlude - After the Siege of Fellburn.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Interlude - After the Trial.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 01.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 02.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 03.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 04.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 05.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 06.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 07.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 08.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 09.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 10.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 11.1.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 11.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 12.1.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 12.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 13.1.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 13.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 14.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 15.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 16.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 17.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 18.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 19.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 20.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 21.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 22.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 23.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 24.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 25.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 26.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 27.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 28.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 29.1.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 29.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 30.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 31.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 32.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 33.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 34.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 35.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 36.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 37.md
M  Campaigns/Cleenseau Campaign/Sessions/Cleenseau - Session 38.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn As A Teenager.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn Learning Languages.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn Leaves Mahaut's.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn Narrative Bit.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn Sends Wine to His Sister.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn Teaches Izgil Sylvan.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn Training Guards.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn and Alys I.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn and Alys II.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn and Izgil Discuss the Moon.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn and Mahaut’s Miracle Players.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn and Marian After the Trial.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn and Robin I.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn and his Mama Discuss Children.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn and the Crowther Boys.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn and the Horses.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn and the Players I.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn and the Players II.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn on the Road to Tharwa Fea.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn's Adolescene II.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn's Childhood II.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn's Childhood.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn's Fey Safety and News.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn's Story of His Adolescence.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn's Story of Leaving Home.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Celyn's Time in Ruthin.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Clawyn After Celyn Leaves.md
M  Campaigns/Cleenseau Campaign/Stories/Authorial Narratives/Luck and Fate.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/Celyn and Perception.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/Celyn and the Cursed Room.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/Celyn's Miracle Story.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/Celyn's Musings on Magic.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/Celyn's Perceptions of Veltor.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/Celyn's Story of Getting His Name.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/El's Story.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/Elizabeth of Cassen's Story.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/Gareth's Story.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/Greymalkin's Story.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/Guy de Varan's Story.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/Robin's Miracle.md
M  Campaigns/Cleenseau Campaign/Stories/Told In World/Viepuck and Goodberries.md
M  Campaigns/Cleenseau Campaign/Treasure/Treasure.md
M  Campaigns/Cleenseau Campaign/home.md
M  Campaigns/Dragonets/Dragonets Campaign.md
M  Campaigns/Dragonets/Session Notes/Dragonets - Session 01.md
M  Campaigns/Dragonets/Session Notes/Dragonets - Session 02.md
M  Campaigns/Dragonets/The Shared Vision of Home.md
M  Campaigns/Dunmari Frontier Campaign/Collected Stories/Amar's Story.md
M  Campaigns/Dunmari Frontier Campaign/Collected Stories/Caulaus' Story.md
M  Campaigns/Dunmari Frontier Campaign/Collected Stories/Cecilia Lister's Story.md
M  Campaigns/Dunmari Frontier Campaign/Collected Stories/Iskra's Story.md
M  Campaigns/Dunmari Frontier Campaign/Collected Stories/Jorundr's Story.md
M  Campaigns/Dunmari Frontier Campaign/Collected Stories/Justan's Story.md
M  Campaigns/Dunmari Frontier Campaign/Collected Stories/Kirian's Story.md
M  Campaigns/Dunmari Frontier Campaign/Collected Stories/Nameless Chardonian Warrior's Story.md
M  Campaigns/Dunmari Frontier Campaign/Collected Stories/Tree’s story.md
M  Campaigns/Dunmari Frontier Campaign/Dreams and Visions/First Dream of Rai.md
M  Campaigns/Dunmari Frontier Campaign/Dreams and Visions/Kenzo Spirit Journey in Bedez.md
M  Campaigns/Dunmari Frontier Campaign/Dreams and Visions/Kenzo's Dream of Apollyon.md
M  Campaigns/Dunmari Frontier Campaign/Dreams and Visions/Kenzo's Dream of Monks.md
M  Campaigns/Dunmari Frontier Campaign/Dreams and Visions/Kenzo's Memories of Hraglar.md
M  Campaigns/Dunmari Frontier Campaign/Dreams and Visions/Order of the Awakened Soul Initiation.md
M  Campaigns/Dunmari Frontier Campaign/Dreams and Visions/Second Dream of Rai.md
M  Campaigns/Dunmari Frontier Campaign/Dreams and Visions/The Last Jade Vision.md
M  Campaigns/Dunmari Frontier Campaign/Dreams and Visions/The Shakun Mystai Initiation.md
M  Campaigns/Dunmari Frontier Campaign/Dreams and Visions/Vision of Rai and Apollyon.md
M  Campaigns/Dunmari Frontier Campaign/Dreams and Visions/Visions of the Sentient Ocean.md
M  Campaigns/Dunmari Frontier Campaign/Dunmar Fellowship Associates.md
M  Campaigns/Dunmari Frontier Campaign/Dunmari Frontier Campaign.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Agata's Treasure.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Apollyon's Tower Treasure.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Copper Hills Treasure.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Drankorian Treasure.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Elemental Forge Hoard.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Flaming Tempest Hoard.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Gifts and Purchases.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Grimbaskal's Hoard.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Hralgar's Palace Treasure.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Kadmos and Company Loot.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Merfolk Quest Treasure.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Nashtkar Treasures.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Ra'ghemdros' Hoard.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Raven's Hold Treasure.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Stormcaller Tower Treasure.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Tower of the Colossus Treasure.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Ursk Treasure.md
M  Campaigns/Dunmari Frontier Campaign/Hoards/Werewolf Lair Treasure.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/An Annotated (Partial) Map of Drankor.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Archives Letter.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Chalyte Rumors from Tiberius.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Chalyte Rumors from the Smiling Crab.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Faldrak's Journal Notes.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Hobgoblin Notes from Raven's Hold.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Lakan Monk Letter.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Letter from Candrosa.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Letter from Dee WIldcloak.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Letter from Govir.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Letter from Speaker Lara.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Nayan Marathu's Letter.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Papers from the Fraternity of the Empty Moon.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Philosopher's Information Concerning Binding Stones.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Philosopher's Information Concerning Extraplanar Wounds.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Philosopher's Information Concerning Frankar.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Philosopher's Information Concerning Limbo.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Philosopher's Information Concerning Rai's Hand.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Philosopher's Information Concerning Rodnya Voknaz.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Philosopher's Information Concerning Ursk.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Report of the Aagiri to Samraat Dasa.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Reports on Chalyte in Alta Tonaro.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Research about Ancient Sources on Limbo.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Research about Limbo and Cha'mutte.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Research about Limbo and the Plaguelands.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Research about Planar Connections.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Research from Kassi.md
M  Campaigns/Dunmari Frontier Campaign/Letters and Notes/Two letters from Stormcaller Tower.md
M  Campaigns/Dunmari Frontier Campaign/Party Treasure - Former.md
M  Campaigns/Dunmari Frontier Campaign/Party Treasure.md
M  Campaigns/Dunmari Frontier Campaign/Scrying and Spying/Grash May 13th.md
M  Campaigns/Dunmari Frontier Campaign/Scrying and Spying/Scrying Delwath Nov 15.md
M  Campaigns/Dunmari Frontier Campaign/Scrying and Spying/Scrying Delwath Oct 21.md
M  Campaigns/Dunmari Frontier Campaign/Scrying and Spying/Scrying Delwath Oct 26.md
M  Campaigns/Dunmari Frontier Campaign/Scrying and Spying/Scrying Delwath Tollen Downtime.md
M  Campaigns/Dunmari Frontier Campaign/Scrying and Spying/Scrying Late Dec 1748.md
M  Campaigns/Dunmari Frontier Campaign/Scrying and Spying/Vision of Govir's research.md
M  Campaigns/Dunmari Frontier Campaign/Scrying and Spying/Vision of Ulfgar's research.md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Dunmar Frontier - Session 01.md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Dunmar Frontier - Session 02.md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Dunmar Frontier - Session 03.md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Dunmar Frontier - Session 04.md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Dunmar Frontier - Session 05.md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Dunmar Frontier - Session 06.md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Interlude (Delwath Postscript).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Interlude (Preparations for Limbo).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Interlude (Tollen Downtime).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 1 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 10 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 100 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 101 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 102 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 103 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 104 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 105 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 106 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 107 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 108 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 109 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 11 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 110 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 111 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 112 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 113 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 114 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 115 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 116 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 117 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 118 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 119 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 12 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 120 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 121 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 122 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 123 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 124 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 125 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 126 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 127 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 128 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 129 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 13 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 130 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 131 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 132 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 133 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 134 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 14 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 15 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 16 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 17 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 18 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 19 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 2 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 20 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 21 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 22 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 23 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 24 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 25 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 26 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 27 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 28 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 29 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 3 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 30 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 31 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 32 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 33 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 34 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 35 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 36 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 37 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 38 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 39 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 4 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 40 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 41 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 42 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 43 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 44 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 45 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 46 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 47 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 48 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 49 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 5 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 50 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 51 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 52 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 53 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 54 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 55 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 56 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 57 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 58 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 59 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 6 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 60 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 61 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 62 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 63 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 64 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 65 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 66 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 67 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 68 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 69 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 7 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 70 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 71 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 72 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 73 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 74 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 75 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 76 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 77 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 78 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 79 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 8 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 80 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 81 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 82 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 83 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 84 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 85 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 86 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 87 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 88 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 89 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 9 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 90 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 91 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 92 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 93 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 94 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 95 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 96 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 97 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 98 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Session Notes/Session 99 (DuFr).md
M  Campaigns/Dunmari Frontier Campaign/Tales and Stories/Govir's Story.md
M  Campaigns/Dunmari Frontier Campaign/Tales and Stories/Hralgar's Story.md
M  Campaigns/Dunmari Frontier Campaign/Tales and Stories/Milo's Story.md
M  Campaigns/Dunmari Frontier Campaign/Tales and Stories/Murook's Story.md
M  Campaigns/Dunmari Frontier Campaign/Tales and Stories/Stories of the Freed Prisoners of the Cleansed.md
M  Campaigns/Dunmari Frontier Campaign/Tales and Stories/Story of Xurkhaz.md
M  Campaigns/Dunmari Frontier Campaign/Tales and Stories/Tale of the Cloak of Rainbows.md
M  Campaigns/Dunmari Frontier Campaign/Tales and Stories/The Dunmari Monsoon.md
M  Campaigns/Dunmari Frontier Campaign/Tales and Stories/The Werewolf Prisoner's Tale.md
M  Campaigns/Dunmari Frontier Campaign/Treasure/Chardon Fan.md
M  Campaigns/Dunmari Frontier Campaign/Treasure/Floating Disc Coin.md
M  Campaigns/Dunmari Frontier Campaign/Treasure/Forge Components.md
M  Campaigns/Dunmari Frontier Campaign/Treasure/Obsidian Fly.md
M  Campaigns/Dunmari Frontier Campaign/Vindristjarna Bastion Rules.md
M  Campaigns/Dunmari Frontier Campaign/Vindristjarna Mechanics.md
M  Campaigns/Dunmari Frontier Campaign/Vindristjarna Room Planning (Old).md
M  Campaigns/Great Library Campaign/Great Library Adventures.md
M  Campaigns/Great Library Campaign/Great Library Campaign.md
M  Campaigns/Great Library Campaign/Handouts/Letter from Chardon for Samso on the Umbral Covenant.md
M  Campaigns/Great Library Campaign/Session Notes/Great Library Session Notes - Arc 1.md
M  Campaigns/Great Library Campaign/Session Notes/Great Library Session Notes - Arc 2.md
M  Campaigns/Great Library Campaign/Session Notes/Great Library Session Notes - Arc 3.md
M  Campaigns/Great Library Campaign/Session Notes/Great Library Session Notes - Arc 4.md
M  Campaigns/Great Library Campaign/Session Notes/Great Library Session Notes - Arc 5.md
M  Campaigns/Great Library Campaign/Session Notes/Great Library Session Notes - Arc 6.md
M  Campaigns/Mawar Adventures/Episodes/Mawar Adventures Episode 01.md
M  Campaigns/Mawar Adventures/Episodes/Mawar Adventures Episode 02.md
M  Campaigns/Mawar Adventures/Episodes/Mawar Adventures Episode 03.md
M  Campaigns/Mawar Adventures/Episodes/Mawar Adventures Episode 04.md
M  Campaigns/Mawar Adventures/Episodes/Mawar Adventures Episode 05.md
M  Campaigns/Mawar Adventures/Mawar Adventures.md
M  Campaigns/Mawar Adventures/Notes/Azar's Tale.md
M  Campaigns/Mawar Adventures/Notes/The Ciphered Scroll.md
M  Campaigns/Mawar Adventures/Notes/Wazir's Gloss on the Ciphered Scroll.md
M  Campaigns/One Shots/Into the Chasm/Into the Chasm - Episode 01.md
M  Campaigns/One Shots/Into the Chasm/Into the Chasm - Episode 02.md
M  Campaigns/One Shots/Into the Chasm/Into the Chasm - Episode 03.md
M  Campaigns/One Shots/Into the Chasm/Into the Chasm - Episode 04.md
M  Campaigns/One Shots/Into the Chasm/Into the Chasm - Episode 05.md
M  Campaigns/One Shots/Into the Chasm/Into the Chasm - Episode 06.md
M  Campaigns/One Shots/Into the Chasm/Into the Chasm - People, Places, and Organizations.md
M  Campaigns/One Shots/Into the Chasm/Into the Chasm.md
M  Campaigns/One Shots/Labyrinths of the Lost/Labyrinths - Player Background.md
M  Campaigns/One Shots/Labyrinths of the Lost/Labyrinths of the Lost - Session 1.md
M  Campaigns/One Shots/Labyrinths of the Lost/Labyrinths of the Lost - Session 2.md
M  Campaigns/One Shots/Labyrinths of the Lost/Labyrinths of the Lost - Session 3.md
M  Campaigns/One Shots/Labyrinths of the Lost/Labyrinths of the Lost.md
M  Campaigns/One Shots/Lost in the Feywild/Aurae's Allegories.md
M  Campaigns/One Shots/Lost in the Feywild/Lost in the Feywild - Episode 01.md
M  Campaigns/One Shots/Lost in the Feywild/Lost in the Feywild - Episode 02.md
M  Campaigns/One Shots/Lost in the Feywild/Lost in the Feywild - Episode 03.md
M  Campaigns/One Shots/Lost in the Feywild/Lost in the Feywild - Episode 04.md
M  Campaigns/One Shots/Lost in the Feywild/Lost in the Feywild - Episode 05.md
M  Campaigns/One Shots/Lost in the Feywild/Lost in the Feywild - Episode 06.md
M  Campaigns/One Shots/Lost in the Feywild/Lost in the Feywild - Episode 07.md
M  Campaigns/One Shots/Lost in the Feywild/Lost in the Feywild - People, Places, and Organizations.md
M  Campaigns/One Shots/Lost in the Feywild/Lost in the Feywild.md
M  Campaigns/One Shots/Lost in the Feywild/The Story of a Fey Bargain Struck.md
M  Campaigns/One Shots/Lost in the Feywild/Transcriptions from the Prisoner.md
M  Campaigns/One Shots/Oskar's Adventures/Oskar in Tharn Todor.md
M  Campaigns/One Shots/Oskar's Adventures/Oskar's Adventures.md
```

</details>

<details><summary>Events · 1 files</summary>

```text
M  Events/1700s/1718/Awakened Soul Disaster.md
```

</details>

<details><summary>Gazetteer · 29 files</summary>

```text
M  Gazetteer/Central Highlands/Dwarven Kingdoms/Thordun.md
M  Gazetteer/Central Highlands/Dwarven Kingdoms/Tumukhar.md
M  Gazetteer/Central Highlands/Highveil Forest.md
M  Gazetteer/Central Highlands/Tirnessa.md
M  Gazetteer/Central Highlands/Vangebekkr.md
M  Gazetteer/Extraplanar/Feywild/Amberglow/Redsun Watch.md
M  Gazetteer/Extraplanar/Shadowfolds/Cairn Dor/Eshlem.md
M  Gazetteer/Extraplanar/Shadowfolds/Cairn Dor/Sarren Kir.md
M  Gazetteer/Extraplanar/Shadowfolds/Cairn Dor/Wolf Queen's Stillings.md
M  Gazetteer/Extraplanar/Shadowfolds/Zeyfa's Realm/Melusa.md
M  Gazetteer/Extraplanar/Shadowfolds/Zeyfa's Realm/Zeyfa's Labyrinth.md
M  Gazetteer/Faraway Places/Far South.md
M  Gazetteer/Greater Chardon/Chardonian Empire/Apporia/Urkabi.md
M  Gazetteer/Greater Chardon/Chardonian Empire/Chardon/Great Library.md
M  Gazetteer/Greater Chardon/Chardonian Empire/Chardonian Empire.md
M  Gazetteer/Greater Chardon/Chardonian Empire/Politics of Chalyte (Chardonian Empire).md
M  Gazetteer/Greater Chardon/Lake Valandros.md
M  Gazetteer/Greater Dunmar/Roads/Stoneway.md
M  Gazetteer/Greater Sembara/Zimkova/Great Chasm.md
M  Gazetteer/Greater Sembara/Zimkova/Kemeko Monastery.md
M  Gazetteer/Major Rivers/Chasa-Nahadi Watershed/Pykolon Lake.md
M  Gazetteer/Northwest Coast/Erbalta Plains/Erbalta Plains.md
M  Gazetteer/Northwest Coast/Northern Provinces/Fort Zarnato.md
M  Gazetteer/Northwest Coast/Northern Provinces/Greater Voltara.md
M  Gazetteer/Northwest Coast/Northern Provinces/Northern Provinces.md
M  Gazetteer/Northwest Coast/Northern Provinces/Order of Twilight Temple (Voltara).md
M  Gazetteer/Northwest Coast/Northern Provinces/Snake River Fort.md
M  Gazetteer/Northwest Coast/Northern Provinces/Voltara/The Hero's Feast.md
M  Gazetteer/Northwest Coast/Northern Provinces/Voltara/Voltara.md
```

</details>

<details><summary>Groups · 12 files</summary>

```text
M  Groups/Chardonian Organizations/Auratan Family.md
M  Groups/Chardonian Organizations/Caloren Family.md
M  Groups/Chardonian Organizations/Chalyte Oligarchs of Chardon.md
M  Groups/Chardonian Organizations/Chalyte Refining Corporation.md
M  Groups/Chardonian Organizations/Chardonian Legion.md
M  Groups/Chardonian Organizations/Patelios Family.md
M  Groups/Chardonian Organizations/Veldari Family.md
M  Groups/Orc Hordes/Grumella's Horde.md
M  Groups/Order of Twilight.md
M  Groups/Shemra Azem.md
M  Groups/Umbral Covenant.md
M  Groups/Vejo Vaikai.md
```

</details>

<details><summary>People · 61 files</summary>

```text
M  People/Chardonians/Arturo.md
M  People/Chardonians/Lyra.md
M  People/Deno'qai/Hakar.md
M  People/Deno'qai/Izkir.md
M  People/Deno'qai/Joram of Eshlem.md
M  People/Deno'qai/Loma.md
M  People/Dunmari/Candrosa.md
M  People/Dunmari/Johar.md
M  People/Dwarves/Diesa.md
M  People/Dwarves/Eldeth Redhammer.md
M  People/Elves/Elwis.md
M  People/Extraplanar Powers/Archfey/Cloudspinner.md
M  People/Extraplanar Powers/Forquarion.md
M  People/Extraplanar Powers/Yeshara.md
M  People/Fey/Agata.md
M  People/Fey/Illaran.md
M  People/Fey/Melusine.md
M  People/Halflings/Ander Charmheart.md
M  People/Halflings/Callie Riverstone.md
M  People/Halflings/Finoc Small.md
M  People/Halflings/Jasmine Sunmeadow.md
M  People/Halflings/Jenny Honeypot.md
M  People/Halflings/Oswalt Tealeaf.md
M  People/Halflings/Wendel Quickstep.md
M  People/Historical Figures/Ikos.md
M  People/Lizardfolk/Iara.md
M  People/Maseauns/Agnes of Evis.md
M  People/Orcs/Grumella.md
M  People/Orcs/Ravager of Winter.md
M  People/Other Humans/Ralvaz.md
M  People/Other Nonhumans/Aurelia.md
M  People/Other Nonhumans/Empress of Chaos.md
M  People/Other Nonhumans/Grash.md
M  People/Other Nonhumans/Oduk.md
M  People/Other Nonhumans/Samerki.md
M  People/Other Nonhumans/Vilaxes.md
M  People/PCs/Other PCs/Into the Chasm/Chasm Explorers.md
M  People/PCs/Other PCs/Into the Chasm/Ekko.md
M  People/PCs/Other PCs/Into the Chasm/Eolo.md
M  People/PCs/Other PCs/Into the Chasm/Finnan Oakstride.md
M  People/PCs/Other PCs/Into the Chasm/Jrain Fanlish.md
M  People/PCs/Other PCs/Into the Chasm/Justas Rhostrin.md
M  People/PCs/Other PCs/Into the Chasm/Rala.md
M  People/PCs/Other PCs/Oskar's Companions/Oskar.md
M  People/PCs/Silver Tempests/Aelar.md
M  People/PCs/Silver Tempests/Aglath.md
M  People/PCs/Silver Tempests/Alton.md
M  People/PCs/Silver Tempests/Friend.md
M  People/Sembarans/Eidrikas.md
M  People/Sembarans/Jonathon Henwyn.md
M  People/Sembarans/Kalima.md
M  People/Sembarans/Margaret Ashford.md
M  People/Sembarans/Pakrinek.md
M  People/Sembarans/Vincent de Arban.md
M  People/Tollenders/Hugo Dupont.md
M  People/Zimkovans/Iskander.md
M  People/Zimkovans/Khaled.md
M  People/Zimkovans/Nura.md
M  People/Zimkovans/Samir.md
M  People/Zimkovans/Taquin.md
M  People/Zimkovans/Zahara.md
```

</details>

<details><summary>Things · 3 files</summary>

```text
M  Things/Artifacts of Power/Ring of Undying.md
M  Things/Magic Items/Flamekeeper Scroll.md
M  Things/Materials/Chalyte.md
```

</details>

<details><summary>_MoC · 8 files</summary>

```text
M  _MoC/Campaign Registry.md
M  _MoC/Display Control.md
M  _MoC/Metadata Specification.md
M  _MoC/Pages to Review/Pages That Need Game Updates.md
M  _MoC/Pages to Review/People Known To Review.md
M  _MoC/Pages to Review/Session Recaps to Review.md
M  _MoC/Taelgar Note Linter.md
M  _MoC/Taelgarverse Code.md
```

</details>

<details><summary>_Plugins · 2 files</summary>

```text
M  _Plugins/Name Explorer/Place Name Evidence Summary.json
M  _Plugins/Name Explorer/Place Name Evidence.jsonl
```

</details>

<details><summary>_analysis · 4 files</summary>

```text
M  _analysis/sessions/combat/analyze.py
M  _analysis/sessions/combat/encounters.csv
M  _analysis/sessions/combat/metadata.yaml
M  _analysis/sessions/combat/sessions.csv
```

</details>

<details><summary>_dm_notes · 1 files</summary>

```text
M  _dm_notes/_Into the Chasm/Into the Chasm - Note Index.md
```

</details>

<details><summary>_scripts · 14 files</summary>

```text
M  _scripts/build_session_note_components.py
M  _scripts/campaign_registry.py
M  _scripts/customJS/loadMetadata.js
M  _scripts/customJS/nameManager.js
M  _scripts/customJS/outputs.js
M  _scripts/find_misplaced_images.py
M  _scripts/place_name_evidence.js
D  _scripts/session_note_campaigns.json
M  _scripts/test_build_session_note_components.py
M  _scripts/test_header_campaign_registry.js
M  _scripts/test_lint_taelgar_notes.rb
M  _scripts/test_validate_taelgar_note.rb
M  _scripts/tests/fixtures/taelgar_note_lint_trial.json
M  _scripts/validate_taelgar_note.rb
```

</details>

<details><summary>_sessions · 36 files</summary>

```text
M  _sessions/dunmar-frontier/_timeline/timeline.json
M  _sessions/feywild/feywild-ep01-source-prep.yaml
M  _sessions/feywild/feywild-ep02-source-prep.yaml
M  _sessions/feywild/feywild-ep03-source-prep.yaml
M  _sessions/feywild/feywild-ep04-source-prep.yaml
M  _sessions/feywild/feywild-ep05-source-prep.yaml
M  _sessions/feywild/feywild-ep06-source-prep.yaml
M  _sessions/feywild/feywild-ep07-source-prep.yaml
M  _sessions/lablost/lablost-ep01-source-prep.yaml
M  _sessions/lablost/lablost-ep02-source-prep.yaml
M  _sessions/lablost/lablost-ep03-source-prep.yaml
M  _sessions/mawar/mawar-ep01-source-prep.yaml
M  _sessions/mawar/mawar-ep02-source-prep.yaml
M  _sessions/mawar/mawar-ep03-source-prep.yaml
M  _sessions/mawar/mawar-ep04-source-prep.yaml
M  _sessions/mawar/mawar-ep05-source-prep.yaml
M  _sessions/to-process/addermarch/addermarch-001-session.yaml
M  _sessions/to-process/addermarch/addermarch-002-session.yaml
M  _sessions/to-process/addermarch/addermarch-003-session.yaml
M  _sessions/to-process/addermarch/addermarch-004-session.yaml
M  _sessions/to-process/addermarch/addermarch-005-session.yaml
M  _sessions/to-process/addermarch/addermarch-006-session.yaml
M  _sessions/to-process/addermarch/addermarch-007-session.yaml
M  _sessions/to-process/addermarch/addermarch-008-session.yaml
M  _sessions/to-process/addermarch/addermarch-009-session.yaml
M  _sessions/to-process/addermarch/addermarch-010-session.yaml
M  _sessions/to-process/addermarch/addermarch-011-session.yaml
M  _sessions/to-process/addermarch/addermarch-012-session.yaml
M  _sessions/to-process/addermarch/addermarch-013-session.yaml
M  _sessions/to-process/addermarch/addermarch-014-session.yaml
M  _sessions/to-process/addermarch/addermarch-015-session.yaml
M  _sessions/to-process/addermarch/addermarch-016-session.yaml
M  _sessions/to-process/addermarch/addermarch-017-session.yaml
M  _sessions/to-process/addermarch/addermarch-018-session.yaml
M  _sessions/to-process/addermarch/addermarch-019-session.yaml
M  _sessions/to-process/addermarch/addermarch-020-session.yaml
```

</details>

<details><summary>_templates · 8 files</summary>

```text
M  _templates/session-notes/cleenseau-narrative.md
M  _templates/session-notes/cleenseau-template.md
M  _templates/session-notes/dragonets-template.md
M  _templates/session-notes/dunmar-frontier-template.md
M  _templates/session-notes/feywild-template.md
M  _templates/session-notes/into-the-chasm-template.md
M  _templates/session-notes/lablost-template.md
M  _templates/session-notes/mawar-template.md
```

</details>

<details><summary>_website · 1 files</summary>

```text
M  _website/greensea.md
```

</details>

<details><summary>assets · 2 files</summary>

```text
M  assets/pc-references/seeker-early-campaign-reference.md
M  assets/pc-references/wellby-early-campaign-reference.md
```

</details>

### Taelgarverse Core

<details><summary>docs · 2 files</summary>

```text
M  docs/campaign-sites.md
M  docs/vault.md
```

</details>

<details><summary>obsidian · 7 files</summary>

```text
M  obsidian/taelgarverse/README.md
M  obsidian/taelgarverse/distribution-readme.md
M  obsidian/taelgarverse/features/calendar.mjs
M  obsidian/taelgarverse/features/interaction-data.mjs
M  obsidian/taelgarverse/materializer/legacy.cjs
A  obsidian/taelgarverse/services/campaign-registry.mjs
M  obsidian/taelgarverse/services/snapshots.mjs
```

</details>

<details><summary>scripts · 3 files</summary>

```text
M  scripts/dev.mjs
M  scripts/prepare-cloudflare.mjs
M  scripts/smoke-worker.mjs
```

</details>

<details><summary>src · 7 files</summary>

```text
M  src/campaign-calendar.mjs
M  src/campaign-interactions.mjs
A  src/campaign-registry.mjs
M  src/contexts.mjs
M  src/engine.mjs
M  src/header-core/names.mjs
A  src/vault-campaigns.mjs
```

</details>

<details><summary>tests · 30 files</summary>

```text
M  tests/api.test.mjs
M  tests/contexts.test.mjs
M  tests/dataview-export.test.mjs
M  tests/fixtures/backlinks.json
A  tests/fixtures/legacy-vault/Campaigns/_Index/adma.md
A  tests/fixtures/legacy-vault/Campaigns/_Index/clee.md
A  tests/fixtures/legacy-vault/Campaigns/_Index/dgnt.md
A  tests/fixtures/legacy-vault/Campaigns/_Index/dufr.md
A  tests/fixtures/legacy-vault/Campaigns/_Index/feywild.md
A  tests/fixtures/legacy-vault/Campaigns/_Index/grli.md
A  tests/fixtures/legacy-vault/Campaigns/_Index/itc.md
A  tests/fixtures/legacy-vault/Campaigns/_Index/lablost.md
A  tests/fixtures/legacy-vault/Campaigns/_Index/mawar.md
A  tests/fixtures/legacy-vault/_sessions/campaign-registry.json
M  tests/folder-exclusions.test.mjs
M  tests/header-core.test.mjs
M  tests/header-preparation.test.mjs
A  tests/helpers/indexed-campaigns.mjs
A  tests/helpers/write-campaign-index.mjs
M  tests/interactions-worker.test.mjs
M  tests/map-website.test.mjs
M  tests/note-publication.test.mjs
M  tests/obsidian-calendar.test.mjs
M  tests/obsidian-headers.test.mjs
M  tests/obsidian-indexes.test.mjs
M  tests/obsidian-interactions.test.mjs
M  tests/obsidian-relationships.test.mjs
M  tests/obsidian-services.test.mjs
M  tests/runtime-snapshot.test.mjs
M  tests/worker.test.mjs
```

</details>

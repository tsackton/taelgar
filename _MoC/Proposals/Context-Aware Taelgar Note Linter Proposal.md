---
tags: [meta, status/check/ai]
---
# Context-Aware Taelgar Note Linter Proposal

> [!warning] Proposal
> This note is an exploratory design, not an adopted linting or metadata specification. The expectations, field names, severities, structured blocks, and workflow described below must be tested against representative vault notes and revised through human review before they become authoritative.

## Design status

The proposed system is a context-aware, repeatable linter for individual Taelgar notes. It combines deterministic validation with agentic editorial judgment, then records a queryable summary and a shared, nonpublic structured to-do report on the note.

This proposal is the active exploratory direction for note-level editorial checking. It does not depend on a one-time grading system, durable ratings, or a dedicated review browser.

An initial deterministic prototype now exists at `_scripts/validate_taelgar_note.rb`, with reduced regression fixtures derived from the first six-note trial. Version 2.1 also has a narrowly bounded `--fix-frontmatter` mode. The prototype is evidence for refining the design, not a general authorization to migrate note metadata.

The prototype prints a Markdown report by default or structured JSON with `--format json`. A historical trial can use `--since-ref COMMIT`; a future note with `lintedAt` can use `--linted-at TIMESTAMP`. The formatter writes only frontmatter whose parsed values can be preserved safely; contextual metadata and reports still require a specifically authorized lint run.

No `lint-taelgar-note` skill or final note-data specification should be written yet. The next phase is to develop provisional expectations and try them on a varied collection of real notes. Those trials should determine which checks are useful, which generate false positives, which metadata concepts need refinement, and which structured data belongs in frontmatter, note-local blocks, or generated indexes.

## Problem

The vault contains several overlapping kinds of unfinished or uncertain state:

- legacy `status/*` tags whose original meaning or current validity may be unclear;
- notes that are technically valid but omit useful metadata or important established information;
- notes whose prose or metadata may have been superseded by later sessions or private planning;
- notes whose intended audience, in-world knowledge, point of view, or temporal scope is not explicit;
- notes that capture everything currently invented but are still underdeveloped relative to their setting or campaign importance;
- mechanically inconsistent frontmatter and special syntax;
- editorial weaknesses that cannot be detected by deterministic rules alone.

Existing status tags are evidence, but they are not a complete or consistently maintained inventory of these problems. A useful lint must inspect the note independently while also validating every existing status.

## Proposed outcome

A successful lint should leave four things:

1. deterministic findings about syntax, metadata, links, and other machine-checkable invariants;
2. contextual findings about correctness, coverage, continuity, clarity, and development needs;
3. a shared, nonpublic structured report attached to the note as a human-facing to-do list; and
4. a lint timestamp and rule version, together with `status/check/lint` when the report contains unresolved findings or suggestions.

The linter should not rewrite canonical prose, resolve lore questions, remove status tags, or silently adopt proposed metadata semantics. Addressing the report is a later human-reviewed editing task.

## Core principles

1. **Expectations come before judgment.** The linter must use explicit, reviewable expectations rather than inventing a standard anew for every note.
2. **Expectations are contextual.** Entity type is important, but article mode, audience, temporal point of view, structural role, and importance may change what a note should contain.
3. **Deterministic and agentic findings remain distinguishable.** A malformed field is different from an evidence-backed coverage gap or an editorial suggestion.
4. **Correctness, coverage, and invention are different questions.** Missing established information is not the same as an opportunity to invent more.
5. **Status tags require disposition.** A lint is incomplete unless it validates or questions every existing `status/*` tag on the note.
6. **Private and public meanings remain separate.** Campaign knowledge, player audience, page privacy, private information elsewhere, and authorial ownership are related but distinct.
7. **The lint report is replaceable and disposable.** It is the current human-review to-do list, not permanent article metadata. A later lint replaces it, and a human may delete it after disposition without losing the timestamp, rule version, article profile, mode, or temporal point of view.
8. **Lint state combines a timestamp with unresolved-work status.** `lintedAt` records the completed check. `status/check/lint` means that the check produced findings or suggestions that still require human disposition. A lint timestamp with no `status/check/lint` means the note was accepted as correct relative to the evidence examined in that lint.
9. **Automation must preserve meaning.** Any deterministic normalization must preserve values, comments, uncertainty, and special syntax exactly.
10. **Trials precede specification.** The skill, rule set, metadata schema, and note-local block formats remain provisional until they work on diverse real notes.

## Expectation model

A single note-type checklist is unlikely to be sufficient. The linter should derive a provisional profile from several axes.

### Entity or document type

Examples include:

- person;
- place, with more specific place profiles where useful;
- group;
- power;
- creature or bestiary entry;
- object, book, material, or artifact;
- event;
- ancestry or culture;
- background or framework topic;
- primary source;
- meta, campaign, or operational document where included.

Existing `tags`, `species`, and `typeOf` values should drive this classification. Folder location and content may provide supporting evidence or reveal a mismatch.

### Article mode and point of view

The categories described in [[Vault Organization]] provide a starting point:

- glossary;
- in-world;
- character-facing encyclopedia;
- player-facing encyclopedia;
- meta.

Primary sources and campaign records may require additional modes. Version 2.1 records the selected profile, article mode, and temporal point of view in a persistent article-metadata block. The linter should validate that prose, uncertainty, mechanics, and private material are appropriate to those selections.

### Knowledge, audience, and privacy

These answer different questions:

- `knownTo`: does a campaign party know this subject at the campaign's current or final state?
- `audience`: which players should be able or encouraged to read the page?
- `campaign`: which campaign owns a session note, campaign meta page, or campaign source document?
- `%%SECRET[v2:2813636d58fe60b6f07f9b3fae26e409]%%` blocks: which local secrets must not be shared through GitHub and may be hidden even from Taelgarverse collaborators?
- ordinary `%% ... %%` comments: which nonpublic DM or editorial material is shared with collaborators through Git?
- `Campaign:none` blocks: which structured nonpublic DM material is shared through Git but excluded from Taelgarverse?
- `audience: [none]`: is the entire page private and unpublished?
- `dm_notes`: has a human attested that relevant information exists outside Git-tracked files or only in someone's head?
- `dm_owner`: who has plans or ideas that require coordination?

The target meaning of `audience: [none]` is the replacement for `excludePublish: [all]`, but migration must respect any current publishing compatibility requirements until the new audience model is adopted by all consumers. A nonpublic page or block does not automatically have `dm_notes: important`; page visibility, Git sharing, collaborator visibility, and the existence of information the linter cannot inspect are separate facts.

Folder placement alone does not make `campaign` appropriate for an in-world entity. Places, people, groups, objects, events, and other world subjects use `knownTo` and `audience` even when their files happen to live under a campaign directory. `campaign` is reserved for session notes, campaign-specific meta pages, and source material whose document identity belongs to a campaign.

### Temporal point of view

Temporal review is principally a point-of-view question: from what in-world or editorial moment is this note speaking, and is each temporal claim suitable for that point of view? It is not a generic demand to date every changing fact.

The linter must distinguish:

- entity lifecycle dates such as `born`, `created`, `died`, and `destroyed`;
- dated relationships such as whereabouts and affiliations;
- changing prose controlled by date blocks;
- a glossary or encyclopedia article speaking from the setting's current campaign-independent present;
- a whole note intentionally speaking from a historical point of view, such as [[Tempest Towers]] at DR 1748;
- an event article retrospectively describing a bounded event;
- an in-world or primary-source document whose author, copyist, annotator, and underlying sources may have different dates and knowledge;
- a campaign block whose words such as “currently” are relative to that campaign's selected or final state; and
- campaign knowledge, which is not automatically backdated merely because the subject existed earlier.

Every completed contextual lint must state the inferred article mode, temporal point of view, confidence, and whether the prose is suitable for it, even when the result is “stable current reference; no temporal qualification needed.” The profile, mode, and POV persist as article metadata; confidence and suitability remain review judgments. A temporal defect exists when the note silently mixes incompatible points of view, uses an unanchored “currently” or similar claim whose truth changes under the intended view, exposes later knowledge in an earlier view, or applies date/campaign blocks inconsistently. Later truth does not make an explicitly earlier-POV article incorrect.

Trials should determine whether any whole-note metadata is needed. A candidate such as `asOf` is appropriate only when the point of view cannot be represented or reliably inferred by the article mode, event date, primary-source identity, or an existing explicit POV marker. It must not replace lifecycle dates or passage-level date blocks.

### Structural role and development importance

The same entity type can support very different expectations. A minor river, an important regional hub, a glossary person, and a recurring campaign NPC should not be measured by one depth standard.

The linter should distinguish:

- a note's role as a bounded reference, connector, overview, hub, or major subject;
- importance to the setting;
- importance to one or more campaigns; and
- whether additional invention would materially improve reference value, play, or world coherence.

These judgments guide expected coverage but should not become generic minimum word counts or mandatory headings.

## Rule classes

Each provisional lint rule should have:

- a stable rule identifier;
- a concise description;
- an applicability condition;
- a rule class;
- a default severity;
- a deterministic or agentic evaluation method;
- the evidence required for a finding;
- an explicit not-applicable path where appropriate; and
- whether a safe automatic repair is possible.

Proposed rule classes are:

- **required**: failure is an objective error for every applicable note;
- **conditional**: expected when a stated condition applies, with a recorded not-applicable judgment allowed;
- **recommended**: useful but not required for a valid note;
- **judgment**: contextual editorial or development assessment rather than a fixed field check.

The provisional severity vocabulary is:

- **error**: invalid structure, broken invariant, strong factual conflict, or clear privacy/publication failure;
- **warning**: likely missing information, unresolved continuity, questionable status, or unmet conditional expectation;
- **suggestion**: non-required improvement in presentation, metadata, or development.

Development opportunity may need its own scale rather than being counted as a defect.

## Preliminary lint areas

### Identity, naming, and classification

The linter should consider:

- canonical `name`, filename, title, aliases, and duplicate-subject risk;
- one appropriate descriptive category;
- `species` for people and documented `typeOf` for non-people where applicable;
- controlled or expected classification values;
- whether the primary name and aliases match the note's actual usage;
- pronunciation for named in-world subjects; and
- structured name-language and derivation information where it would be useful.

Pronunciation is a strict required rule for named in-world subjects. The contextual pass may record a justified not-applicable result for a plain-English title, a meta note, a genuinely obvious ordinary name such as Thomas Hawke, or an English compound whose only non-obvious component resolves to a named note with an accepted pronunciation. The subject note for that component still requires its own pronunciation. A missing applicable pronunciation is an error in the completed contextual lint; because applicability includes human judgment, the deterministic prototype emits a provisional warning until that judgment is made.

When pronunciation is missing, the linter should propose one from, in descending order, explicit authoritative evidence; adopted rules for the name's language; an established cultural or species naming rule; or a cautious phonological inference. The proposal must state its basis and uncertainty. It remains in the lint report until human acceptance and is not silently written as canonical metadata.

### Note-local name data

Subject-specific Name Explorer decisions may be easier to understand and validate when stored in a short, machine-readable block on the subject note rather than only in a path-keyed sidecar.

A provisional Git-shared, nonpublic block is deliberately short enough to author while inventing a name:

```yaml
%%^Metadata:names:v1%%
- {name: Istaros, language: unknown, derivedFrom: Aistanë, notes: likely corruption}
- {name: Aistanë, role: historical, language: Elvish, pronunciation: EYE-stah-neh, meaning: blessed water}
%%^End%%
```

The schema version belongs in the marker rather than consuming a payload field. Each entry requires only `name` and `language`; the first entry is primary unless another entry says `role: primary`. Optional `role`, `pronunciation`, `meaning`, `derivedFrom`, `notes`, and `status` cover the common cases. `status` may be `documented`, `inferred`, `proposed`, `disputed`, or `unresolved`. `language` is the in-world language of the displayed form. Reusable real-world or phonological inspiration belongs in language rules rather than being copied into every note.

The linter may create or extend this block with facts explicitly supported by the note or adopted global rules. It may record an inference only with an explicit `status` and explain its basis in the lint report. It must never invent an etymology merely to fill the block; `unknown` is a valid complete language. An accepted primary pronunciation remains in the existing frontmatter field. A proposed pronunciation may live in the name block until accepted. The literal pronunciation values `obvious`, `title`, `meta`, and `inherited from <name>` record reviewed exceptions without a second status vocabulary.

`Metadata:names:v1` is a reserved structured marker, not an ordinary comment, SECRET block, campaign block, or lint report. It should be tested against simple names, translated names, several aliases for one concept, genuinely separate name concepts, disputed names, and names governed mostly by a reusable language rule.

The likely long-term division is:

- note-local blocks are authoritative for human-curated subject-specific facts;
- centralized data stores contain reusable inference rules that should not be copied into every note; and
- the Name Explorer catalog is generated from the notes and global rules for efficient browsing.

The linter should validate, but not overwrite, human-owned name data. The name block must remain distinct from the replaceable lint report.

### Knowledge, audience, and campaign evidence

The first adopted knowledge check is deliberately narrow. `knownTo` is required and actively checked for people and objects; `[]` is the explicit value when no campaign knowledge is recorded. It remains optional for other notes, including places. `campaignInfo` on a person or object normally implies a matching `knownTo` value.

Positive campaign lists in `audience` remain underdesigned and should not create missing-audience findings during the linter trials. `audience: [none]` remains the candidate whole-page private/publication boundary. Campaign relevance should meanwhile be derived from applicable campaign-document identity, people-and-objects `knownTo`, sparse `campaignInfo`, session evidence, and campaign/date blocks rather than requiring a universal authored audience field.

The linter should consider:

- whether `knownTo` uses canonical campaign codes;
- whether `campaignInfo` suggests a missing `knownTo` value;
- whether person-level session backlinks suggest knowledge requiring human confirmation;
- whether an existing explicit audience value is valid and coherent;
- whether a whole-page publication exclusion contradicts intended publication without treating it as campaign knowledge;
- whether applicable session, meta, and source records identify their campaign correctly;
- whether an in-world entity incorrectly uses `campaign` merely because it lives in a campaign directory;
- whether `audience: [none]`, `excludePublish`, and private blocks have compatible meanings during migration; and
- whether private material is excluded from public output rather than merely hidden in a browser.

A session backlink is evidence that the subject appeared, not automatic proof that every character knows every fact on the page.

### Correctness, consistency, and freshness

The linter should consider two distinct conflict classes:

- **internal conflicts**, where two passages or metadata values in the target note disagree; these are usually high-confidence findings that a human can resolve quickly from the note itself; and
- **cross-note conflicts**, where the target disagrees with a stronger, more recent, or differently authoritative vault source; these require source comparison, authority judgment, and preservation of genuine uncertainty.

The distinction must be explicit in the report. An internal editorial note that questions visible prose is not, by itself, evidence of a cross-note conflict. The linter should also consider:

- unsupported certainty;
- incorrect treatment of campaign knowledge, primary-source claims, Worldbuilding material, or private DM material;
- lifecycle, relationship, and date inconsistencies;
- newer sessions or DM material that link to the note; and
- existing `status/gameupdate/*` tags and the events that might justify them.

Material newer than the previous lint is a prompt for examination, not proof that the note is outdated. The agent must read the relevant context and report whether it changes, supplements, contradicts, or does not affect the note.

Git history is the evidence boundary for this freshness check; the linter does not need a separate corpus snapshot. Starting from `lintedAt`, the deterministic pass should nominate later changes in any Git-tracked vault note that links or otherwise resolves to the target, while prioritizing campaign and session notes, `_DM_`, `_dm_notes`, and finalized `beat-facts.json` files. Ordinary reference notes remain candidates with their distinct authority labels. Worldbuilding material may be indexed as development context, but it cannot establish that a canonical note is incorrect, stale, or conflicted. A newer Worldbuilding note must never invalidate a clean canonical lint. When the target itself is in Worldbuilding, the report may describe internal inconsistency, divergence from current canon, or development status, but it must not issue an incorrectness statement merely because the proposal was not adopted or later canon differs.

Plain-text resolution should be conservative: exact, case-preserving matches to a distinctive filename or explicit `name` may nominate a source, while short/common names and loose aliases should require a wikilink or other stronger resolver evidence. The candidate record should preserve the source path, source kind, commit, changed-line counts, mention locations, and whether the mention itself was added or changed.

The candidate set may include harmless reformatting or a source whose changed material does not affect the target. Only the contextual pass decides materiality. Direct links are the first signal; trials should add bounded relationship propagation where needed, such as a newer note about a proprietor or containing location that bears on an inn. Binary assets and generated derivatives are not invention-bearing text sources.

Edits to the target note do not invalidate a clean lint merely because the target's Git timestamp changed. The working assumption is that a clean note is edited in a clean-preserving way. A later external source is what creates a reason to examine whether invention elsewhere has overtaken the article.

### Coverage and completeness

The linter should ask whether the note contains the minimum information appropriate to its role and whether established information elsewhere in the vault should be summarized or incorporated here.

It should distinguish:

- information that properly belongs in this note;
- evidence that is already represented adequately;
- information that should remain in campaign-specific or private sources;
- useful backlinks that do not need to be duplicated; and
- information whose relevance or authority is uncertain.

The linter should not require every note to repeat every mention or exhaust everything that could be said about the subject.

### Whereabouts and map data

Whereabouts are both current metadata and a future analytical data source. The eventual goal includes reconstructing and mapping journeys, especially PC journeys. A complete journey may require hundreds of dated whereabouts entries, which is incompatible with the goal of keeping ordinary frontmatter concise and easy to edit.

The current representation remains authoritative until a replacement is designed. The linter should presently validate:

- whether an applicable note has a useful location;
- whether location targets resolve;
- whether types, dates, ranges, and ordering are valid;
- whether entries overlap or contradict entity lifecycle;
- whether derived origin, home, current, secondary, and last-known locations make sense;
- whether important established movements are missing; and
- whether formatting follows the compact dictionary-list convention.

The linter should not invent an `overflow` field or move history automatically during the trial phase.

Any future representation must support:

- one authoritative data source rather than manually synchronized copies;
- hundreds of chronological entries;
- human editing from within Obsidian;
- machine parsing and map generation;
- precise and uncertain dates;
- stable note references and link resolution;
- multiple map identities and scales; and
- readable notes with short frontmatter.

Possible approaches to test later include:

- retaining all entries in frontmatter with better tooling;
- keeping a concise current or summary location in frontmatter and a full structured history in a note-local private data block;
- storing all whereabouts in a note-local body block and deriving frontmatter/header values;
- using a generated sidecar with a purpose-built Obsidian editor; or
- another representation discovered during map and journey prototyping.

Obsidian's inability to edit JSON sidecars natively is a significant constraint. A sidecar should not become the human source of truth without an adequate editing interface.

Map coordinates are related to, but not identical with, whereabouts. A useful map-location field needs a map identifier as well as a hex or coordinate because the same subject may appear on several regional and world maps. The map registry must define stable identifiers, authority/version, scale, grid convention, parent/detail relationships, and precision before a universal map position becomes required.

Version 2.1 requires map blocks for waterways, roads, and settlements. They remain optional for other places. A provisional block is:

```yaml
%%^Metadata:map:v1%%
locations:
  - {geometry: path, map: world, sourceHex: "13.07.F16", outletHex: "13.07.C18", precision: stated}
%%^End%%
```

Point-like features may use one coordinate or a small hex set; rivers and roads need ordered paths or at minimum source and endpoint; lakes, forests, watersheds, and realms need areas; ranges and coastlines may need paths or areas depending on use. Missing required data is represented explicitly with `status: missing` and `locations: []`, producing a lint finding rather than a suppression. A locator in the `13.07.F16` form always refers to the world hex map and therefore requires `map: world`. Coordinates should remain strings so leading zeroes and punctuation survive YAML parsing.

### DM notes and ownership

`dm_notes` was originally a collaboration signal for information the shared, Git-backed vault does not contain: material in untracked files, paper notes, another private store, or someone's head. Under that definition, the linter cannot establish that `dm_notes: none` is true and cannot infer `color` or `important` merely because it finds substantial material in `_DM_`, `_dm_notes`, an ordinary comment, a `Campaign:none` block, or another Git-tracked source. Those sources are inspectable shared DM evidence.

The deterministic pass can validate the documented vocabulary. The agentic report can:

- ask a human to confirm the current `dm_notes` attestation;
- explain when a declared value is contradicted by an explicit statement about off-vault material;
- inventory significant shared DM evidence separately; and
- judge whether `dm_owner` identifies the person or group whose plans require coordination.

The trials must decide whether significant shared DM material warrants any authored frontmatter at all. Because the linter can derive its existence and describe its substance, a generated report or index may be more reliable than another manually maintained summary key. If a frontmatter field is eventually adopted, it must not reuse or blur the collaboration meaning of `dm_notes`.

### Status validation

A successful lint must enumerate every existing `status/*` tag and assign a disposition such as:

- still valid, with the reason;
- likely resolved and ready for human removal;
- malformed or obsolete vocabulary;
- valid but too broad for the actual problem;
- superseded by a more specific finding; or
- unresolved because the available evidence is insufficient.

Outstanding status conditions count as lint issues. The linter does not remove or replace status tags automatically.

### Frontmatter and structural formatting

Deterministic validation should cover:

- exactly one parseable frontmatter block at the beginning of the file;
- documented field names and value shapes;
- field ordering;
- compact simple lists;
- one-line dictionaries within dictionary lists;
- consistent indentation and whitespace;
- valid links and relationship targets;
- valid campaign, date, and private block syntax;
- preserved special comments and generated constructs; and
- successful header rendering where applicable.

The 2.1 formatter uses one canonical frontmatter representation:

- deprecated or obsolete fields first, so they remain conspicuous;
- then `headerVersion`, `lintedAt`, `lintVersion`, and `displayDefaults`;
- then `tags`, `typeOf`, `typeOfAlias` or person equivalents, and `ancestry`;
- then unclassified fields in their stable original order;
- then `name`, `aliases`, and `pronunciation`;
- then `affiliations` and `whereabouts`;
- then `knownTo`, `excludePublish`, `audience`, `dm_owner`, and `dm_notes`;
- string-only lists on one line;
- dictionaries on one line; and
- lists of dictionaries expanded, with one single-line dictionary per list item.

The initial deprecated/obsolete set is `activeYear`, `subTypeOf`, `subTypeOfAlias`, `subspecies`, `speciesAlias`, `deity`, `timelineDescriptor`, `pcOwner`, `rarity`, `leaderOf`, `reignStart`, `aNoDate`, `aPast`, `aPastWithStart`, and `aCurrent`. The formatter preserves these values; it does not migrate or delete them. It refuses automatic rewriting when comments, duplicate keys, anchors, merges, or invalid YAML make round-trip preservation uncertain.

A future skill should expose three explicit modes: `check`, `safe-fix`, and opt-in `editorial-fix`. A safe formatter may automatically normalize representation, but only if it:

- preserves the parsed data exactly;
- preserves comments, quoting with semantic significance, and unknown fields;
- makes no classification or lore decision;
- records what it changed; and
- verifies semantic equivalence before accepting the result.

`safe-fix` presently covers semantic-preserving frontmatter order and representation. Later versions may add indentation, trailing whitespace, line endings, or canonical structured-marker spelling after separate round-trip tests. `editorial-fix` may address high-confidence typos, punctuation, duplicated words, and very light clarity problems, but never names, dates, classification, lore, uncertainty, private material, or conflict resolution.

Standalone meta comments about note quality or note-level POV belong immediately below frontmatter and the persistent metadata blocks, before the title and other prose. The linter may move only comments that unambiguously have that role, preserving their text exactly. Other comments remain where they are; an obvious clarity improvement is a lint suggestion rather than an automatic rearrangement.

Automatic normalization should occur before the final lint report and state are recorded. Every applied change must be listed separately from unresolved issues with its stable rule identifier, location, deterministic or agentic method, concise before/after description, and verification. The resulting note is re-linted before `lintedAt` is written.

### Editorial quality

Agentic review should turn general quality into actionable questions:

- Can a reader identify the subject and its significance quickly?
- Is the prose direct, coherent, and appropriately organized?
- Does the note maintain its intended point of view and audience?
- Is uncertainty attributed rather than silently resolved?
- Does it avoid unnecessary duplication and campaign recap?
- Are headings and sections proportionate to the note's length?
- Are links used where they materially improve understanding?
- Are private, mechanical, campaign-specific, and general information in the correct channels?

The report should identify particular passages or omissions rather than assign a generic quality grade.

### Development sufficiency

The linter should separately ask whether the subject is important enough to warrant additional invention.

This is not the same as a coverage finding:

- **coverage gap**: relevant information already exists and should be represented here;
- **development opportunity**: the information has not been invented, but developing it would materially improve play, reference value, or setting coherence.

Development opportunity should not be an error. Trials should determine whether it needs a queryable priority such as `none`, `low`, `medium`, or `high`, or whether a concise report section is sufficient.

## Proposed persistent lint state

The smallest useful frontmatter state is:

```yaml
lintedAt: "2026-08-18T14:32:11-04:00"
lintVersion: "2.1"
```

This combines with the presence or absence of `status/check/lint` to support review views for:

- notes with no completed lint;
- notes linted before a chosen date;
- notes linted under an older rule version;
- notes with unresolved lint work; and
- notes accepted as correct relative to their most recent lint.

The timestamp and report are initially written together, and a timestamp is written only after a complete lint. If the report contains any error, warning, or suggestion, the linter adds `status/check/lint`. A human removes that tag only after every finding has been corrected, accepted, or otherwise dispositioned. The report must not be compressed into frontmatter issue counts, but it may then be deleted: the timestamp plus absence of `status/check/lint` records that the note was accepted as of that lint.

This state is intentionally about the evidence examined at a particular time, not permanent correctness. Later material in relevant external sources can make the note a re-lint candidate. Editing the target note alone does not.

If development priority proves useful, it may receive a separate field rather than being folded into issue severity.

## Proposed persistent article metadata

Profile, article mode, and temporal POV are useful properties of the article rather than facts about the lint run. They live immediately below frontmatter in a persistent block:

```yaml
%%^Metadata:article:v1%%
profile: place
mode: geographic reference
pov: current setting reference
%%^End%%
```

These fields stay when the lint report is deleted. `pov` describes the note's speaking position, not merely the date of a fact. It may be a current setting reference, a bounded retrospective event account, an explicit historical viewpoint such as DR 1748, or the layered viewpoint of a primary source. When the best value remains uncertain, the block records that uncertainty and the lint report supplies a copy-ready replacement candidate.

## Proposed lint report

The report should be a shared, nonpublic, machine-recognizable block at the end of the note. It should be visible to GitHub collaborators but absent from Taelgarverse, so it must not use `SECRET`. The exact marker and internal schema must be tested. It should be readable in Obsidian, replaceable without touching human comments, SECRET blocks, or other shared DM blocks, and structurally distinct from human-curated note-local data such as name information.

The report should include:

- any uncertainty in the persistent profile, article mode, or temporal POV, plus POV suitability;
- open errors, warnings, and suggestions with stable rule identifiers;
- disposition of every existing status tag;
- relevant newer session or DM evidence;
- automatic normalization performed;
- name and map block additions or changes;
- copy-ready candidate metadata or comments for every suggested addition that can be represented safely;
- validated exceptions and not-applicable expectations;
- development opportunities; and
- concise evidence links or source explanations.

Open findings may be rendered as Markdown tasks so the report functions as a to-do list. Candidate material should appear in fenced YAML or Markdown that can be copied directly into the intended location; the validator ignores candidate syntax inside the lint block. The underlying note and sources remain authoritative. A human may use task state to record disposition, clear `status/check/lint` when no lint work remains, and delete the entire report. A later lint regenerates it from current state rather than accumulating another block.

Vault governance now permits an explicitly approved Taelgar linter run to add `status/check/lint` for deterministic frontmatter normalization, recognized lint and metadata blocks, approved meta-comment reordering, and logged lint fixes. It does not authorize the linter to remove any status tag or to use this exception for unrelated content work.

## Provisional lint workflow

1. Identify the target note and determine its provisional expectation profile.
2. Read the complete note, including frontmatter, comments, private blocks, and generated structures.
3. Run deterministic validation and optionally apply only approved safe formatting repairs.
4. Resolve names, aliases, links, backlinks, relationships, campaigns, and relevant dates.
5. Gather source context according to the vault's authority hierarchy.
6. Examine later sessions and DM material that may affect the note, especially sources newer than the previous lint.
7. Perform agentic review for correctness, coverage, editorial quality, status disposition, and development opportunity.
8. Write or update the persistent article, name, and map blocks; put any unresolved proposed value in a copy-ready lint candidate.
9. Validate the complete structured report.
10. Write the lint report, timestamp, and rule version together; add `status/check/lint` if any finding or suggestion remains open.
11. Re-read the note and confirm that no canonical prose, human-curated data block, or unrelated metadata changed.
12. After human review, remove `status/check/lint` only when every report item has been corrected or dispositioned; the lint report may then be deleted.

If the evidence search or report generation is incomplete, the lint fails and no completion timestamp is written.

## Trial-first development plan

### Phase 1: expectation discovery

Before linting notes, inventory:

- adopted `_MoC` metadata, categorization, status, organizational, and display rules;
- templates and header/runtime behavior;
- current data-cleaning queries and known legacy fields;
- the audience and date-control proposals without treating them as adopted;
- current Name Explorer decisions and inference rules;
- representative high-quality, sparse, status-tagged, campaign-heavy, and private notes; and
- examples with complex whereabouts, naming, chronology, or publication behavior.

Produce a provisional rule matrix with applicability, class, severity, evaluation method, evidence requirements, and safe-fix status.

### Phase 2: note trials

Run the draft lint manually or agentically on a deliberately varied set of notes. The set should cross-cut rather than merely sample one note from each directory. It should include:

- clearly strong and clearly weak notes;
- short notes that may be intentionally sufficient;
- notes carrying several kinds of legacy status;
- people and mobile objects with complex whereabouts;
- places at several structural scales;
- ordinary, translated, alternate, and contested names;
- private pages and public pages with private blocks;
- notes with extensive session or DM evidence;
- historical snapshots and changing-world-state prose;
- primary sources and notes with intentionally limited epistemic authority; and
- subjects that are complete relative to existing lore but may warrant more invention.

Trial reports should normally remain outside the notes, such as in chat or temporary trial artifacts. A specifically authorized live trial may write the provisional metadata and report blocks so their actual Obsidian behavior can be reviewed. Version 2.1 uses the adopted narrow `status/check/lint` governance exception for those live runs.

The first trial used six Great Library-related notes: [[Great Library]], [[Julius of Voltara]], [[The Purple Pig]], [[Order of Twilight]], [[Thunderbrand]], and [[Tempest Towers]]. It established several useful fixtures, followed by four semantic corrections from human review:

- basic YAML, link, block, and controlled-value checks can pass while important contextual findings remain;
- `campaignInfo` without matching `knownTo` and unresolved target audiences are deterministic provisional findings;
- campaign-directory placement does not make `campaign` valid for in-world entities; only session notes, campaign meta pages, and campaign source material use that field;
- SECRET blocks are valid local-only collaboration boundaries, while ordinary comments and `Campaign:none` blocks are shared DM material with different syntax and uses;
- `dm_notes` describes information outside Git-tracked material and therefore cannot be inferred from shared DM files or blocks;
- newer external backlinks are useful candidates but require materiality judgment;
- [[Tempest Towers]] is a clean temporal control because later truth is privately captured while visible prose has an explicit DR 1748 point of view;
- [[The Purple Pig]] demonstrates an internal conflict between visible prose and an in-note editorial comment; no independent cross-note contradiction was established;
- internal and cross-note conflicts need separate rule identifiers, evidence descriptions, and resolution paths; and
- the summary `typeOf` list's `buliding` spelling conflicts with the detailed place rules, which correctly accept `building`.

The reduced fixtures live in `_scripts/tests/fixtures/taelgar_note_lint_trial.json`. They are regression examples for the deterministic boundary, not frozen judgments about the live notes.

The second trial used fifteen deliberately adversarial notes rather than a random sample. It tested strict pronunciation with obvious-name and compound-name exceptions; the initial, more complex note-local naming block; simple and complex map coverage; people-only required `knownTo`; positive-audience deferral; temporal point of view across current references, bounded events, historical snapshots, campaign blocks, and layered primary sources; Worldbuilding as non-authoritative development context; and itemized safe or editorial fixes. Its written blocks remain historical version 2 trial output rather than being silently migrated.

The third live trial uses ten reproducibly random eligible content notes and version 2.1. Selection used seed `20260819` over 2,745 clean tracked content notes after excluding tool, governance, generated, and `_sessions` files, files with pre-existing worktree changes, and the earlier fifteen-note trial. It tests the simplified name block, persistent article metadata, copy-ready lint candidates, canonical frontmatter formatting, `knownTo` on people and objects, required map blocks on waterways, roads, and settlements, and `status/check/lint` under the new governance exception.

### Phase 3: calibration and correction

For each trial, record:

- useful findings;
- false positives;
- missed problems;
- unclear or overbroad expectations;
- severity disagreements;
- incorrect source treatment;
- profile uncertainty;
- fields that need explicit not-applicable handling;
- information that belongs in a note-local block rather than frontmatter;
- information better represented in a generated index; and
- checks that should be deterministic rather than agentic, or vice versa.

Revise the expectation matrix and trial again until the reports are consistently useful.

### Phase 4: prototype note-local data

Before adoption, prototype in chat or temporary files:

- name-language blocks for several naming patterns;
- the generated lint report block;
- the queryable lint timestamp, version, and `status/check/lint` workflow;
- candidate POV and temporal metadata;
- candidate map-location metadata; and
- at least one high-volume whereabouts representation when journey mapping work begins.

Human readability in Obsidian and round-trip machine parsing are both required.

### Phase 5: specification and skill

Only after the trials should the project:

1. adopt approved metadata and structured-block semantics into the relevant `_MoC` governance notes;
2. define the lint report schema and rule versioning;
3. promote the deterministic prototype and bounded frontmatter formatter into an adopted, fully tested tool;
4. create the `lint-taelgar-note` skill;
5. add an Obsidian Base or Dataview review surface; and
6. consider a custom plugin only if native review and editing are insufficient.

## Trial success criteria

The design is ready to become a specification only when:

- note expectations are explicit enough that the agent explains what standard it applied;
- deliberately good short notes are not penalized for brevity;
- every status tag receives a useful disposition;
- deterministic errors and editorial judgments are clearly distinguishable;
- missing existing information and opportunities for new invention remain separate;
- audience, knowledge, privacy, DM ownership, and POV are not conflated;
- report severities are consistent enough to support review filtering;
- automatic formatting preserves semantic data and comments exactly;
- note-local structured data is easy to inspect and edit in Obsidian;
- report and metadata summaries round-trip without disagreement;
- newer source material is examined contextually rather than treated as automatic invalidation; and
- the workflow produces a to-do list that a human can actually act on.

## Open questions

- What is the final expectation matrix for each entity or document type?
- Which profile, article-mode, and temporal-POV vocabularies are stable enough to validate as controlled values?
- Is a whole-note `accurateFrom` / `accurateUntil` model useful, and how does it interact with date blocks?
- What exact semantics and migration timing should govern `audience`?
- Does the simplified `Metadata:names:v1` schema preserve enough Name Explorer distinctions in practice?
- Which name information belongs in global rules rather than note-local blocks?
- Which copy-ready candidate types need a more structured lint-report representation?
- Should development priority be queryable metadata?
- Can the frontmatter formatter safely support commented YAML or anchors without losing human meaning?
- How should hundreds of historical whereabouts be stored and edited when journey mapping becomes an active project?
- What map registry and coordinate model can support world and regional maps?
- How should freshness candidates propagate through structured relationships without producing an unmanageable transitive graph?
- Should significant shared DM material receive an authored frontmatter key, or remain derived in lint reports and generated indexes?
- How large and diverse must the trial set be before the rule set is stable enough to adopt?

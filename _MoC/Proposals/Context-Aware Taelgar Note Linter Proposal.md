---
tags: [meta, status/check/ai]
---
# Context-Aware Taelgar Note Linter Proposal

> [!warning] Proposal
> This note is an exploratory design, not an adopted linting or metadata specification. The expectations, field names, severities, structured blocks, and workflow described below must be tested against representative vault notes and revised through human review before they become authoritative.

## Design status

The proposed system is a context-aware, repeatable linter for individual Taelgar notes. It combines deterministic validation with agentic editorial judgment, then records a queryable summary and a private, structured to-do report on the note.

This proposal is the active exploratory direction for note-level editorial checking. It does not depend on a one-time grading system, durable ratings, or a dedicated review browser.

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
3. a private structured report attached to the note as a human-facing to-do list; and
4. compact frontmatter metadata that supports review views for unlinted, old, clean, and issue-bearing notes.

The linter should not rewrite canonical prose, resolve lore questions, remove status tags, or silently adopt proposed metadata semantics. Addressing the report is a later human-reviewed editing task.

## Core principles

1. **Expectations come before judgment.** The linter must use explicit, reviewable expectations rather than inventing a standard anew for every note.
2. **Expectations are contextual.** Entity type is important, but article mode, audience, temporal stance, structural role, and importance may change what a note should contain.
3. **Deterministic and agentic findings remain distinguishable.** A malformed field is different from an evidence-backed coverage gap or an editorial suggestion.
4. **Correctness, coverage, and invention are different questions.** Missing established information is not the same as an opportunity to invent more.
5. **Status tags require disposition.** A lint is incomplete unless it validates or questions every existing `status/*` tag on the note.
6. **Private and public meanings remain separate.** Campaign knowledge, player audience, page privacy, private information elsewhere, and authorial ownership are related but distinct.
7. **The lint report is durable but replaceable.** It records the most recent completed check and its open findings; a later lint replaces it rather than accumulating reports indefinitely.
8. **Lint metadata describes the check, not the truth of the note.** A timestamp means that a complete lint ran, not that the note was approved or issue-free.
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

Primary sources and campaign records may require additional modes. Trials should determine whether this needs explicit metadata, can usually be inferred, or requires a combination of both. The linter should validate that prose, uncertainty, mechanics, and private material are appropriate to the intended mode.

### Knowledge, audience, and privacy

These answer different questions:

- `knownTo`: does a campaign party know this subject at the campaign's current or final state?
- `audience`: which players should be able or encouraged to read the page?
- `campaign`: which campaign owns a campaign record?
- `Campaign:none` blocks: which parts of an otherwise usable note are private?
- `audience: [none]`: is the entire page private and unpublished?
- `dm_notes`: is relevant private information recorded elsewhere or otherwise not shared?
- `dm_owner`: who has plans or ideas that require coordination?

The target meaning of `audience: [none]` is the replacement for `excludePublish: [all]`, but migration must respect any current publishing compatibility requirements until the new audience model is adopted by all consumers. A private page does not automatically have `dm_notes: important`; page visibility and the existence of additional private information are separate facts.

### Temporal stance

The linter must distinguish:

- entity lifecycle dates such as `born`, `created`, `died`, and `destroyed`;
- dated relationships such as whereabouts and affiliations;
- changing prose controlled by date blocks;
- a whole note that intentionally describes a historical snapshot or is only accurate during a particular period;
- campaign knowledge, which is not necessarily backdated.

Trials should determine whether whole-note metadata such as `accurateFrom`, `accurateUntil`, `asOf`, or another model is useful. Such fields should not replace lifecycle dates or passage-level date blocks.

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
- pronunciation for non-obvious named in-world subjects; and
- structured name-language and derivation information where it would be useful.

Pronunciation should not be required for every Markdown file. It is provisionally expected for named in-world subjects unless the pronunciation is genuinely obvious or the note type makes it irrelevant. The lint report can record a justified not-applicable result without adding artificial metadata.

### Note-local name data

Subject-specific Name Explorer decisions may be easier to understand and validate when stored in a short, machine-readable block on the subject note rather than only in a path-keyed sidecar.

A provisional block might record:

- name form;
- role, such as primary or alternate;
- language;
- derivation or relationship;
- source form or source language when relevant; and
- a short note for genuinely ambiguous cases.

The exact syntax is not settled. It should be tested against simple names, translated names, several aliases for one concept, genuinely separate name concepts, disputed names, and names governed mostly by a reusable language rule.

The likely long-term division is:

- note-local blocks are authoritative for human-curated subject-specific facts;
- centralized data stores contain reusable inference rules that should not be copied into every note; and
- the Name Explorer catalog is generated from the notes and global rules for efficient browsing.

The linter should validate, but not overwrite, human-owned name data. The name block must remain distinct from the replaceable lint report.

### Knowledge, audience, and campaign evidence

The linter should consider:

- whether `knownTo` uses canonical campaign codes;
- whether `campaignInfo` suggests a missing `knownTo` value;
- whether session backlinks suggest knowledge requiring human confirmation;
- whether explicit and inferred audiences resolve coherently;
- whether exclusions contradict `knownTo` without an intentional reason;
- whether campaign-directory notes identify their campaign correctly;
- whether `audience: [none]`, `excludePublish`, and private blocks have compatible meanings during migration; and
- whether private material is excluded from public output rather than merely hidden in a browser.

A session backlink is evidence that the subject appeared, not automatic proof that every character knows every fact on the page.

### Correctness, consistency, and freshness

The linter should consider:

- internal contradictions;
- conflicts with stronger or more recent vault sources;
- unsupported certainty;
- incorrect treatment of campaign knowledge, primary-source claims, Worldbuilding material, or private DM material;
- lifecycle, relationship, and date inconsistencies;
- newer sessions or DM material that link to the note; and
- existing `status/gameupdate/*` tags and the events that might justify them.

Material newer than the previous lint is a prompt for examination, not proof that the note is outdated. The agent must read the relevant context and report whether it changes, supplements, contradicts, or does not affect the note.

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

Map coordinates are related to, but not identical with, whereabouts. A useful map-location field will probably need a map identifier as well as a hex or coordinate because the same subject may appear on several regional and world maps. The map registry and coordinate schema must be designed before map position becomes a required lint expectation.

### DM notes and ownership

The linter should validate the semantics of `dm_notes` and `dm_owner`, not merely their presence.

Questions include:

- Are values in the documented vocabulary?
- Does `dm_notes` accurately describe important or color-only private information outside the shared note?
- Does ownership identify the person or group whose plans require coordination?
- Are `important` private notes combined with `none` ownership for a defensible reason?
- Are private blocks, private backlinks, and the declared DM metadata consistent?
- Are shared or joint-development cases represented coherently?

The presence of a private page or a `Campaign:none` block does not by itself determine `dm_notes`; the field describes additional private information relevant to the subject.

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

A safe formatter may automatically normalize representation, but only if it:

- preserves the parsed data exactly;
- preserves comments, quoting with semantic significance, and unknown fields;
- makes no classification or lore decision;
- records what it changed; and
- verifies semantic equivalence before accepting the result.

Automatic normalization should occur before the final lint counts are recorded. Successfully repaired formatting should be listed separately from unresolved issues.

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

The exact field names remain provisional. A compact, flat summary might be:

```yaml
lintedAt: "2026-08-18T14:32:11-04:00"
lintVersion: 1
lintIssueCount: 6
lintErrorCount: 1
lintWarningCount: 3
lintSuggestionCount: 2
```

This supports review views for:

- notes with no completed lint;
- notes linted before a chosen date;
- notes linted under an older rule version;
- notes with errors, warnings, or suggestions; and
- notes with no open findings at their last lint.

The summary must be derived from the attached report and written with it as one operation. A timestamp is written only after a complete lint. It means that the linter completed, not that the note is correct, complete, approved, or ready to publish.

If development priority proves useful, it may receive a separate field rather than being folded into issue severity.

## Proposed lint report

The report should be a private, machine-recognizable block at the end of the note. The exact marker and internal schema must be tested. It should be unpublished, readable in Obsidian, replaceable without touching other private blocks, and structurally distinct from human-curated note-local data such as name information.

The report should include:

- lint timestamp and rule version;
- selected expectation profile and any uncertainty;
- open errors, warnings, and suggestions with stable rule identifiers;
- disposition of every existing status tag;
- relevant newer session or DM evidence;
- automatic normalization performed;
- validated exceptions and not-applicable expectations;
- development opportunities; and
- concise evidence links or source explanations.

Open findings may be rendered as Markdown tasks so the report functions as a to-do list. The underlying note and sources remain authoritative: checking a generated task does not by itself resolve the finding. A later lint should regenerate the report from current state.

The current governance requirement to add `status/check/ai` to AI-edited content notes will need an explicit narrow exception if adopted. Updating only lint metadata and a clearly private generated lint block should not create a new canonical-content review obligation on every run. This exception must be approved in governing documentation before the linter writes to notes.

## Provisional lint workflow

1. Identify the target note and determine its provisional expectation profile.
2. Read the complete note, including frontmatter, comments, private blocks, and generated structures.
3. Run deterministic validation and optionally apply only approved safe formatting repairs.
4. Resolve names, aliases, links, backlinks, relationships, campaigns, and relevant dates.
5. Gather source context according to the vault's authority hierarchy.
6. Examine later sessions and DM material that may affect the note, especially sources newer than the previous lint.
7. Perform agentic review for correctness, coverage, editorial quality, status disposition, and development opportunity.
8. Validate the complete structured report.
9. Write the lint report and summary metadata together.
10. Re-read the note and confirm that no canonical prose, human-curated data block, or unrelated metadata changed.

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

### Phase 2: read-only note trials

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

Trial reports should remain outside the notes, such as in chat or temporary trial artifacts. They should not write lint metadata or permanent blocks before those formats are approved.

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
- the queryable lint-summary fields;
- candidate POV and temporal metadata;
- candidate map-location metadata; and
- at least one high-volume whereabouts representation when journey mapping work begins.

Human readability in Obsidian and round-trip machine parsing are both required.

### Phase 5: specification and skill

Only after the trials should the project:

1. adopt approved metadata and structured-block semantics into the relevant `_MoC` governance notes;
2. define the lint report schema and rule versioning;
3. implement and test deterministic lint and formatting scripts;
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
- Should article mode or point of view be explicit metadata, inferred state, or both?
- Is a whole-note `accurateFrom` / `accurateUntil` model useful, and how does it interact with date blocks?
- What exact semantics and migration timing should govern `audience`?
- What is the shortest human-readable schema that preserves the needed Name Explorer distinctions?
- Which name information belongs in global rules rather than note-local blocks?
- What exact marker and schema should identify the lint report?
- Should development priority be queryable metadata?
- Which frontmatter changes are safe to auto-fix without review?
- How should hundreds of historical whereabouts be stored and edited when journey mapping becomes an active project?
- What map registry and coordinate model can support world and regional maps?
- Which evidence timestamps are reliable for finding sources newer than the previous lint?
- How large and diverse must the trial set be before the rule set is stable enough to adopt?

---
tags: [meta, status/check/ai]
---
# Dynamic Taelgarverse Content and Metadata Transition Plan

> [!warning] Proposal
> This note records a proposed transition. It is not yet the authoritative metadata or content-block specification. Adopted rules must be incorporated into the appropriate `_MoC` documentation before this proposal is retired.

## Purpose

Prepare the vault for a single Taelgarverse site whose readers can select:

1. one global in-world date, controlling the displayed state of the world; and
2. one or more campaigns, controlling campaign-specific text and campaign-relevant browsing surfaces.

This phase is intentionally limited to source-note text, metadata, validation, and documentation. The dynamic website implementation is covered by [[Dynamic Taelgarverse Build and Implementation Plan]].

The transition must improve the source data without making the current static Taelgarverse builds unusable. New metadata should therefore be added before legacy publication fields are removed.

## Decisions

### Campaign and audience metadata

| Field | Target meaning | Transition treatment |
| --- | --- | --- |
| `knownTo` | Canonical current/final campaign knowledge | Normalize and fill |
| `campaignInfo` | Optional curated interaction highlights | Preserve; audit sparsity and usefulness |
| `audience` | Website visibility and relevance | Add |
| `campaign` | Campaign identity on campaign-directory and session records; also used for automatic campaign detection | Preserve; validate against the campaign registry |
| `excludePublish` | Legacy publication control | Retain until dynamic-site cutover, then remove |
| `activeYear` | Ambiguous legacy date gate | Audit individually; retain until dynamic-site cutover, then remove |

`knownTo`, `campaignInfo`, and session backlinks have related but distinct purposes:

- `knownTo` is the authoritative answer to “does this campaign, at its current or final state, know this subject?” It does not attempt to reconstruct knowledge as of an earlier session.
- `campaignInfo` records only selected interactions whose curated description is useful. It is not expected to contain every mention of a frequently recurring subject.
- Links from session notes are the comprehensive evidence for where a subject appeared. They support a generated Campaign Appearances display and may suggest missing `knownTo`, but do not silently change `knownTo`.
- `campaign` identifies the campaign to which a campaign note or session note belongs. This field is already widely used and is expected to remain the main input for classifying session backlinks and campaign-directory content.

### Date and campaign controls

- Date controls world state.
- Campaign selection controls campaign-specific text and campaign-relevant page, list, navigation, and search visibility.
- Campaign knowledge is not backdated. A campaign selection represents that campaign's current or final perspective, even if it is combined with an earlier global date.
- Campaign and audience filtering are reader-convenience features, not a security boundary.
- Private material must continue to be excluded from the published site rather than merely hidden in the browser.

## Canonical campaign registry

Create one machine-readable registry containing every supported active and archived campaign. The proposed authoritative path is:

`_scripts/config/campaigns.json`

The existing campaign configuration in `.obsidian/metadata.json` remains the compatibility source until all consumers can load the dedicated registry. During the transition, validation should report any difference between the two sources. After cutover, `.obsidian/metadata.json` should either load generated campaign configuration or cease to duplicate it.

The registry should contain identity and detection data, not website-specific date presets. A representative entry is:

```json
{
  "schemaVersion": 1,
  "campaigns": [
    {
      "code": "DuFr",
      "name": "Dunmari Frontier",
      "partyPage": "Dunmar Fellowship",
      "sessionNoteFolders": [
        "Campaigns/Dunmari Frontier Campaign/Session Notes"
      ],
      "aliases": [
        "dufr",
        "Dunmari Frontier",
        "Dunmari Frontier Campaign",
        "Dunmar Frontier",
        "Dunmar Frontier Campaign"
      ],
      "status": "archived"
    }
  ]
}
```

Required fields:

- `code`: canonical short code stored in `knownTo`, `campaignInfo`, and campaign blocks.
- `name`: canonical campaign name.
- `aliases`: accepted legacy codes, names, and `campaign` field values.
- `status`: at least `active` or `archived`.

Optional fields:

- `partyPage`: page representing the party.
- `sessionNoteFolders`: one or more folders whose notes count as session evidence for the campaign.

The registry must include, at minimum, Dunmari Frontier, Cleenseau, Great Library, Addermarch, Mawar, Lost in the Feywild, Into the Chasm, and Labyrinths of the Lost. Other campaign-like games should be added only after deciding that they are selectable Taelgarverse perspectives. Canonical short codes for entries not already established must be decided before metadata normalization.

Website date presets, display order, default profiles, and whether an archived campaign appears in the public selector belong in Taelgarverse site configuration, not this registry.

## Target metadata semantics

### `knownTo`

`knownTo` is a compact list of canonical campaign codes:

```yaml
knownTo: [DuFr, GL]
```

It means that, by the campaign's current or final state, the subject has appeared, been discussed, or otherwise become known to that campaign.

Rules:

- Use only canonical registry codes.
- Use `knownTo` principally on in-world entities such as people, places, groups, objects, and potentially events.
- Do not add dates or interaction logs to `knownTo`.
- Do not derive historical, session-specific knowledge views from it.
- Session backlinks can suggest missing values but are not automatically authoritative.

### `campaignInfo`

`campaignInfo` remains a list of optional curated interaction records:

```yaml
campaignInfo:
  - {campaign: DuFr, person: Seeker, type: killed, date: 1748-05-05}
```

Rules:

- The `campaign` value must be a canonical registry code.
- The same campaign should normally be present in `knownTo`; validation should report exceptions.
- Do not add an entry for every session mention.
- Preserve records that contain useful interaction type, actor, date, session link, or custom description.
- Generated Campaign Appearances should use session backlinks for completeness and `campaignInfo` for curated highlights.
- Existing `format` and `wParty` behavior remains supported during transition. Whether curated highlights remain in headers or move to a separate Campaign Appearances component is an implementation decision documented in [[Dynamic Taelgarverse Build and Implementation Plan]].

### `campaign`

The existing `campaign` field on campaign-directory and session notes remains authoritative for identifying the campaign to which the note belongs.

Rules:

- Accept existing human-readable campaign values through registry aliases.
- Do not require campaign notes to duplicate their campaign identity in `knownTo`.
- Use the resolved campaign code when grouping session backlinks, inferring the audience of campaign records, and validating campaign-directory placement.
- Audit missing or contradictory values, but do not mass-rewrite this field unless validation shows a real mismatch. It is believed to be largely complete.

### `audience`

`audience` controls website visibility and relevance. It does not assert in-world knowledge.

Examples:

```yaml
# General world or meta page
audience: [all]
```

```yaml
# Explicitly useful to another campaign in addition to inferred knownTo
knownTo: [DuFr]
audience: [GL]
```

```yaml
# General except for one campaign
audience: [all, "!Clee"]
```

```yaml
# Never publish
audience: [none]
```

Audience resolution:

1. Begin with campaigns listed in `knownTo`.
2. For campaign-directory and session records, add the campaign resolved from `campaign`.
3. Add positive campaign codes from `audience`.
4. Expand `all` to the complete selectable campaign set and general browsing.
5. Apply `!Campaign` exclusions.
6. Treat `none` as an empty audience and a hard instruction not to publish. `none` must not be combined with other values.

Consequences:

- A page with `knownTo: [DuFr]` and no explicit `audience` is DuFr-relevant.
- A page with `knownTo: [DuFr]` and `audience: [all]` is globally visible but can be ranked as directly relevant to DuFr.
- Excluding a campaign listed in `knownTo` is allowed only as an explicit exception and should generate a validation warning.
- A note with no explicit or inferred audience is unclassified. During transition it must not silently disappear from the current site; before cutover, every publishable note must resolve to an intentional audience.

### Legacy fields

`excludePublish` and `activeYear` must remain functional until the dynamic site uses `audience` and date-aware rendering.

For `excludePublish`:

- `excludePublish: [all]` normally maps to `audience: [none]`.
- A campaign-specific exclusion may map to `audience: [all, "!Campaign"]`, a narrower positive audience, or no replacement if the page's inferred audience already excludes that campaign.
- Add `audience` first; remove `excludePublish` only after old-versus-new visibility comparison at cutover.

For `activeYear`:

- Do not convert automatically.
- Classify each use as campaign knowledge, page audience, entity lifecycle, dated prose, or obsolete metadata.
- Move the information to `knownTo`, `audience`, lifecycle metadata, or a date block only when the intended meaning is clear.
- Retain `activeYear` until the current static exporter no longer relies on it.

## Content block specification

### Campaign blocks

An authored campaign block contains text visible only when one specific campaign is selected:

```markdown
%%^Campaign:DuFr%%

Campaign-specific text.

%%^End%%
```

Rules:

- The marker contains exactly one canonical campaign code.
- `all`, negation, and lists are not permitted in campaign blocks.
- Unmarked prose is general prose.
- Campaign blocks express campaign perspective or campaign-specific detail, not general world chronology.
- `%%^Campaign:none%%` is a special private-content block. It is never a selectable campaign and its contents must never be shipped to the public site.
- Generated campaign blocks in regenerated headers must be inventoried separately from authored body blocks. Source cleanup must not edit generated header output as if it were authored prose.

### Date blocks

The canonical date-block forms are:

```markdown
%%^Date:1740-10-07%%

Visible on and after October 7, 1740.

%%^End%%
```

```markdown
%%^Date:1740-10-07a%%

Visible before October 7, 1740.

%%^End%%
```

Formal semantics:

- `Date:X` is visible when the selected date is greater than or equal to `X`.
- `Date:Xa` is visible when the selected date is strictly less than `X`.
- Paired old/new states may use the same cutoff without overlapping.

Example:

```markdown
%%^Date:1740-10-07a%%

The house still stands.

%%^End%%

%%^Date:1740-10-07%%

The house has been destroyed.

%%^End%%
```

Rules:

- Date blocks express changing world-state prose.
- Use the smallest block that contains the changing passage; keep durable history and context unmarked.
- Prefer `YYYY-MM-DD` when the exact transition date is known.
- Preserve `YYYY` or `YYYY-MM` when the underlying evidence is genuinely less precise; do not invent dates merely to make markers uniform.
- Partial cutoff dates resolve to the beginning of the stated period for block visibility: `1740` means `1740-01-01`, and `1740-07` means `1740-07-01`.
- No same-type nesting.
- The eventual parser may allow a date block and campaign block to nest, meaning that both conditions must be satisfied. Do not introduce new cross-type nesting until the compatibility parser supports it.
- Exact marker spelling and an exact `%%^End%%` terminator are required.

### Choosing the correct mechanism

Use:

- lifecycle, whereabouts, and affiliation dates for structured header state;
- a date block for changing prose;
- a campaign block for campaign-specific perspective or detail;
- `knownTo` for current/final campaign knowledge;
- `audience` for page-level website relevance;
- `Campaign:none` or `audience: [none]` for content that must not be published.

Do not use a date block merely because a fact has a date. Additive historical prose can remain visible at later dates. A block is needed when the prose should not be shown in every date view.

## Audit outputs

Before bulk metadata or prose edits, create two reproducible sidecar reports.

### Campaign and audience audit

One record per note, including:

- path, tags, and page type;
- raw and canonical `campaign`;
- `knownTo`;
- campaigns represented in `campaignInfo`;
- campaigns inferred from session backlinks;
- explicit `audience`;
- proposed effective audience;
- `excludePublish` and proposed migration;
- `activeYear`;
- confidence and validation issues.

Report at least:

- unknown or noncanonical campaign values;
- `campaignInfo` campaigns missing from `knownTo`;
- session evidence suggesting missing `knownTo`;
- audience exclusions contradicting `knownTo`;
- unresolved audience;
- malformed `campaignInfo`;
- campaign-directory notes whose `campaign` is missing or inconsistent;
- legacy fields requiring semantic review.

### Content block audit

One record per authored campaign, date, or private block, including:

- path and line;
- raw and normalized marker;
- campaign or cutoff semantics;
- date precision;
- short content preview;
- paired state block, if detected;
- nesting, unmatched marker, invalid code, or invalid date;
- whether the block occurs in generated header material or authored body text;
- preliminary classification as world state, campaign perspective, private content, or unclear.

The existing audit baseline found campaign/date material in a minority of notes, but all occurrences should be re-counted by the reproducible audit before edits begin.

## Transition phases

### Phase 0: approve the specification and registry

- Decide canonical codes for every selectable active and archived campaign.
- Approve the registry location and schema.
- Approve `audience` expansion, negation, and `none` semantics.
- Approve exact date-block boundaries and partial-date handling.
- Add parser fixtures for representative campaign, private, from-date, before-date, and paired-state blocks.

### Phase 1: build read-only validation

- Generate both audit sidecars.
- Validate the current registry aliases against `campaign`, `knownTo`, `campaignInfo`, and authored campaign blocks.
- Identify generated header blocks so they are excluded from authored-content review.
- Compare current Python and JavaScript handling of partial dates and YAML date types; establish one documented normalization rule before rewriting date representations.

### Phase 2: normalize campaign identity

- Repair only confirmed campaign-code and campaign-field mismatches.
- Add `knownTo` when a valid `campaignInfo` interaction unambiguously proves knowledge.
- Use session backlinks only as review suggestions.
- Preserve existing `campaignInfo` entries pending the Campaign Appearances implementation.

### Phase 3: add audience metadata

- Add `audience: [none]` alongside unambiguous `excludePublish: [all]` cases.
- Classify clearly global reference and meta pages as `audience: [all]`.
- Allow `knownTo` and campaign-directory `campaign` to provide inferred campaign audiences rather than duplicating those values unnecessarily.
- Review campaign-specific exclusions and pages with no resolved audience by coherent category.
- Retain `excludePublish` for compatibility.

### Phase 4: audit and correct content blocks

- Correct invalid marker syntax without changing prose or meaning.
- Review every `Date:Xa` block and every paired old/new state.
- Review remaining from-date blocks for the distinction between additive history and replaceable state.
- Review every authored campaign block for a single canonical campaign and correct use as perspective rather than chronology.
- Review all `Campaign:none` blocks as publication boundaries without exposing or rewriting their private content.
- Do not introduce new nesting until the compatibility parser is ready.

### Phase 5: resolve legacy fields

- Classify every `activeYear` use individually and record its intended replacement.
- Record the exact new-audience equivalent for every `excludePublish` use.
- Produce an old-versus-new page visibility matrix for every campaign profile.
- Continue dual metadata until the dynamic build passes that comparison.

### Phase 6: declare content readiness

The source is ready for dynamic-engine cutover when:

- every campaign-bearing value resolves through the canonical registry;
- every publishable note has an explicit or safely inferred audience;
- `knownTo` is complete enough to serve as canonical current/final campaign knowledge;
- `campaignInfo` is intentionally sparse or explicitly marked for later review;
- every authored campaign/date/private block parses with documented semantics;
- every `activeYear` and `excludePublish` has an approved disposition;
- no private block is present in public export fixtures;
- current static builds still produce the intended content during the transition.

## Required documentation changes upon adoption

This proposal should not become policy merely by existing. Adoption requires updating the following authoritative and supporting notes.

### [[Metadata Specification]]

- Add `audience` to the Taelgarverse metadata fields, including `all`, `none`, positive campaigns, negation, inferred audience, and validation rules.
- State unambiguously that `knownTo` is canonical current/final campaign knowledge and is not backdated.
- Reframe `campaignInfo` as optional curated interaction highlights rather than a second source of campaign knowledge or a comprehensive log.
- Document the invariant that a `campaignInfo` campaign should normally be present in `knownTo`.
- Expand the `campaign` field documentation beyond session-note chronology to cover campaign identification and registry-based detection for campaign-directory content.
- Replace the inline description of `.obsidian/metadata.json` campaigns with the dedicated campaign-registry specification and compatibility note.
- Mark `excludePublish` and `activeYear` as legacy during transition and remove them after cutover.
- Add the formal campaign/date/private content-block grammar or link to a dedicated adopted block specification.
- Correct and test the Date Formats section so partial dates and YAML types have one consistent meaning.
- Update frontmatter patterns for people, places, groups, objects, events, campaign notes, background, and meta pages to show when `knownTo`, `campaignInfo`, `campaign`, and `audience` are appropriate.

### [[Taelgarverse Code]]

- Point all campaign detection to the canonical registry.
- Document effective-audience derivation.
- Document the generated Campaign Appearances component: `knownTo` as authority, session backlinks as evidence, and `campaignInfo` as curated highlights.
- Replace outdated instructions that require hand-adding the existing Dataview expression to individual pages if the component becomes automatic.
- Document validation reports and the eventual dynamic block-processing path.

### [[Display Control]]

- Remove the hard-coded “Known campaign codes” list and link to the registry.
- Clarify the future placement and formatting of `campaignInfo` highlights.
- Distinguish dated world-state header variants from campaign-specific appearance information.
- Update the documented header format if Campaign Appearances moves outside the biographical information box.
- Preserve token and format documentation for any still-supported `campaignInfo` highlight rendering.

### [[Note Categorization]]

- Clarify which in-world entity types may use `knownTo` and optional `campaignInfo`.
- Clarify that session and campaign-directory notes use `campaign` for campaign identity and need not duplicate it in `knownTo`.
- Add `audience` guidance for background, meta, primary-source, and campaign-specific pages without making empty fields mandatory in every template.

### [[Vault Organization]]

- Clarify that campaign-directory placement and `campaign` metadata jointly support campaign detection.
- Preserve `Campaign:none` as a private publication boundary.
- Add a short distinction among campaign perspective blocks, date-state blocks, and general prose.

### [[Map of Content]]

- Link the adopted campaign registry, audience documentation, block specification, and relevant data-quality reports.
- Link these proposal notes while the transition remains active, then replace the proposal links with adopted documentation.

### [[Data Quality/Campaign Info]]

- Replace the current `!campaignInfo` query with checks for `knownTo`, session evidence, missing registry mappings, and useful-but-optional `campaignInfo` highlights.
- Avoid treating absence of `campaignInfo` as an error by itself.

### [[Data Analysis/Campaign Known To Information]]

- Group by canonical registry code.
- Add comparisons among `knownTo`, session evidence, explicit audience, and effective audience.
- Surface contradictions and unclassified notes rather than only counts.

### [[Examples/Timelines]]

- Clarify that timeline rows generated from `campaignInfo` use curated highlights, not a comprehensive appearance log.
- Retain the feature only if it remains useful after Campaign Appearances is implemented.

### Templates and review pages

- Update active note templates so `knownTo`, `campaignInfo`, and `audience` are offered only where appropriate; do not add empty fields mechanically to all notes.
- Update Dataview review pages that filter on `excludePublish`, `activeYear`, or the mere presence of `campaignInfo`.
- Add review surfaces for unknown campaign codes, unresolved audiences, missing `knownTo` suggestions, legacy-field disposition, and invalid content blocks.

## Non-goals

- Reconstructing what a campaign knew at an arbitrary past session.
- Treating hidden campaign material as secret once it has been shipped to the browser.
- Populating `campaignInfo` with every session mention.
- Inventing exact dates where the source supports only a year or month.
- Removing compatibility fields before the dynamic site is ready.
- Implementing the dynamic site as part of the metadata cleanup.

---
name: illustrate-note
description: Iteratively illustrate an existing Taelgar note or session recap. Propose image targets, gather vault visual evidence, generate two initial alternatives outside the vault, refine with the user, and export only explicitly approved finals. Finish with captions and image callouts, optionally inserting them into notes or attaching images to recap scenes when requested. Use for people, places, sessions, histories, and other illustrated notes.
---

# Illustrate Note

Guide an interactive illustration session from an existing note to explicitly approved image files and insertion-ready suggestions. Follow the vault `AGENTS.md`. Keep target notes and recaps unchanged until the user authorizes specific insertions. Use the available `imagegen` skill for generation and visual edits; this skill owns selection, evidence gathering, iteration, and delivery.

## 1. Read the target and select image targets

Accept a note path/name, campaign and session identifier, full session note, or session recap. Resolve campaign identities and session paths through `../../../_scripts/session_note_campaigns.json`. A recap and a full session note are both valid starting points; neither requires creating the other. If both exist, identify the working source and the matching recap for possible later attachments. Preserve disagreements for review rather than silently reconciling them.

Read the complete target, including comments and frontmatter. For long documents, inspect all sections before proposing coverage. For recaps, read the current accepted or human-edited file; tolerate removed or changed fields and do not validate, rebuild, or repair its generated structure. Use the source's actual headings or recap scene IDs to anchor proposals.

Present a numbered shortlist with:

- the subject, moment, or scene and the source passage it illustrates;
- a proposed composition, such as a portrait, establishing landscape, action scene, or object detail;
- the suggested location and role in the note: aside, figure, or hero;
- existing art that could serve the same purpose, and important uncertainties.

For long histories, distinguish portraits, events, and changes across periods instead of proposing an image for every heading. Keep the list proportionate to the note. An illustration need not depict an action scene.

Iterate on the shortlist until the user selects targets. Establish shared style, framing/aspect preferences, export format, and any optional archive destination without re-asking preferences already supplied. Default export is WebP quality 90. Explicit selection to proceed authorizes the two initial variants for each selected target; an ideation-only request does not authorize generation. Do not generate additional subjects without selection.

## 2. Gather evidence for the selected images

Search the target and relevant vault notes for people, places, objects, clothing, architecture, environment, chronology, and action. For sessions, use relevant recap passages and cleaned session sources as needed. Do not count repeated pipeline artifacts as independent evidence.

Inspect useful existing images, including references linked from the note and established character references in `assets/pc-references` when applicable. Identify whether each input is an approved identity reference, a provisional depiction, a style reference, or the image being edited. Existing art is not automatically authoritative. Preserve original references unchanged.

Present a compact visual brief for each selected image:

- supported visual facts and their sources;
- the people, props, setting, period, and event to depict;
- composition/style choices that are artistic rather than established lore;
- consequential gaps or conflicts requiring the user's decision.

Keep identity and clothing consistent across scenes unless the evidence supports a change. Match historical depictions to the period shown. Avoid introducing new plot events or treating visual invention as written canon. Keep private information out of public-facing artwork, captions, and shared prompt files unless explicitly authorized for that audience.

Resolve consequential uncertainties before generation. Ordinary composition choices may proceed under the selected brief; do not add an unnecessary approval checkpoint when the user's choices already settle it.

## 3. Generate and present two initial alternatives

Load the available `imagegen` skill at generation time and follow its current tool instructions. Use the built-in tool by default, with one call per variant. Do not switch to a CLI/API path merely to control filenames or export format. Generation uses the image service; drafts are saved locally outside the vault, not generated with an assumed on-device model.

Generate **two separate initial images for each selected target**. Vary a useful visual choice, such as framing or composition, while preserving the same source facts and agreed style. Do not substitute a single contact sheet for two deliverable candidates.

Keep every draft and revision outside the vault. Built-in outputs normally live under `$CODEX_HOME/generated_images/`; use returned paths rather than guessing. If organizing them elsewhere, choose an off-vault working directory and verify its resolved path is outside the vault. The off-vault requirement overrides any generic project-copy instruction while candidates remain unapproved.

Use stable labels such as `scene-02-a-v1` and `scene-02-b-v1`. Keep a small working record outside the vault containing the target/source anchors, exact prompts, reference paths, variant labels, output paths, feedback, and approval state. Do not copy private source excerpts into shared provenance files.

Inspect each result for subject identity, composition, source fidelity, and requested constraints. Present both candidates visibly with their labels and a brief explanation of the differences. Record a generation failure as unfinished work; do not count a missing alternative as delivered.

## 4. Iterate and recognize explicit final approval

Work in the user's preferred scene order. Carry accepted details forward in each prompt and change only the requested aspects when revising a selected image. Inspect local edit targets before using them as tool inputs. Keep prior versions available and use new version labels.

The initial round requires two variants; subsequent rounds need only the revisions or alternatives the user requests. Additional revision requests authorize those revisions, not export of an earlier candidate.

Track each target as proposed, selected, awaiting feedback, revising, explicitly final, exported, or skipped. Approval must identify an exact version; the same labels must appear in the presentation and working record.

**Export only after the user explicitly approves that image as final.** A preference such as “I prefer B” selects a direction. A statement such as “B v2 is final; save it” approves delivery. Praise, silence, moving to another scene, or selecting a candidate for revision is not final approval. Ask if intent or version is unclear. A final approval of one image does not approve other variants or pending revisions.

## 5. Export each approved final

Export immediately after each explicit final approval; do not wait until the whole note's image session is finished. Check branch and working-tree state before vault writes under `AGENTS.md`. Final approval authorizes the derivative at the agreed/default format and destination, but does not authorize note edits.

Save to `assets/_incoming/generated/` with readable, collision-checked filenames:

- Session scenes: campaign/session prefix plus description, for example `dufr-007-the-centaurs-wheel-around.webp`. Resolve the canonical campaign code and preserve the session identifier, including fractional sessions. Include the session number once; an existing `sessionKey` may already contain it.
- Other notes: subject plus description, such as `raven-hold-western-approach.webp` or `kenzo-travel-portrait.webp`.
- Use a version suffix for a distinct later final. Never overwrite an existing asset without explicit replacement authorization, and never rename existing assets as part of this workflow.

Export choices:

| Choice | Encoding |
| --- | --- |
| WebP, default | Quality 90 |
| JPEG | Quality 90 |
| PNG | Lossless |
| Lossless WebP | Lossless |

Encoding quality is an export setting, separate from generation quality. Preserve dimensions unless the user requests resizing. Preserve alpha in PNG/WebP. If JPEG would discard transparency, ask for the intended background before flattening it. Convert from the selected original rather than recompressing a lossy derivative.

### Export helper

Use [scripts/export_image.py](scripts/export_image.py) with a Python environment containing Pillow and WebP support. If the system Python lacks these, discover the bundled runtime using the workspace-dependencies tool rather than hard-coding a machine-specific executable. Run from the vault root, substituting real absolute paths:

```sh
python /absolute/path/to/illustrate-note/scripts/export_image.py \
  /off-vault/selected-original.png \
  /absolute/path/to/vault/assets/_incoming/generated/dufr-007-scene-description.webp
```

The default is `--format webp`. Other choices are `--format png`, `--format jpg`, and `--format webp-lossless`. For transparent JPEG input, add `--background '#ffffff'` only after the user has selected that background. The helper never resizes or overwrites, validates the encoded output, and reports format, dimensions, alpha, byte count, and hashes as JSON. A filename extension must match its format. For an explicitly requested replacement, prepare a verified sibling export first and perform only the separately authorized replacement; do not bypass collision protection casually.

If requested, archive the **original PNG**, byte-for-byte, at the user's chosen off-vault or Git-ignored location. If it is inside the vault, verify the exact destination is ignored and untracked before copying; do not edit `.gitignore` automatically. Check collisions and verify the archive hash against the original. A tool cache path alone is not a completed requested archive. If the source is not PNG, explain that limitation instead of relabeling it or calling a conversion the original PNG.

Inspect the exported derivative visually, verify its actual format/dimensions, and record its final path, settings, hash, source version, and explicit approval in the off-vault working record. Report the vault path after each successful export. If export or archiving fails, retain the approved source and report which step remains incomplete. Revisions after export require new final approval before another vault delivery.

## 6. Finish and offer insertion

Wait for the user to explicitly confirm they are finished with images for this note before producing the final summary. Do not infer this from all initially selected scenes having an exported image. If the user is finished with some candidates still unapproved, leave them outside the vault and distinguish them from approved deliveries.

In chat, summarize each approved image with its final link, scene/subject, format, suggested placement, potential caption, and alt text. Briefly account for skipped or unfinished selections. Include the final prompt or a link to the off-vault prompt record and state which generation tool was used, following `imagegen`. Captions remain suggestions and must not introduce unsupported lore or disclose private evidence.

Read the current [Image Callouts](../../../_MoC/Image%20Callouts.md) authority before preparing copyable insertions. Provide ready-to-paste callouts using the actual delivered filenames and captions, for example:

```markdown
> [!image|figure standard]
> ![[dufr-007-the-centaurs-wheel-around.webp]]
> *The centaurs wheel around beneath the mountains.*
```

Use `right standard` for a typical aside, `figure standard` for a scene, or `hero` for a selected wide image. Resolve filename collisions before using bare image embeds. Offer a gallery only when the images belong together at the same point in the text.

Keep the summary in chat unless the user requests a Markdown file at a specified location. Preview the contents and any replacement scope before a write not already authorized. Follow that location's content-note metadata and status rules, including the no-tags exception for `Worldbuilding/Agentic Review`.

Offer to insert the selected images, captions, and placements. Obtain authorization for the concrete edits unless already provided:

- **Ordinary note:** show the relevant headings/paragraphs and proposed callouts. Preserve surrounding prose, special syntax, and existing images. Frontmatter image changes require their own explicit scope.
- **Session with a matching recap:** attach to the chosen recap scene using its `Image`, `Image Role`, `Image Size`, `Image Placement`, `Image Render`, `Image Caption`, and `Image Alt` fields. Preserve existing attachments and use contiguous numbered sets for additions. Leave default placement/render fields blank unless an override is selected. If no scene clearly fits, ask rather than inventing a scene or rewriting the recap.
- **Generated session note:** put approved attachments in the recap when available. Do not make durable placement changes only in generated output. Rebuilding/rendering the final session note is a separate authorized operation following the session workflow.

Read and verify every changed note/recap under `AGENTS.md`, including the `_sessions` status exemption. Do not apply the generated-recap schema validator to human-edited recaps. Confirm image paths resolve and report exactly which source files were updated.

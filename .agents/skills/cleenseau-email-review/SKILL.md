---
name: cleenseau-email-review
description: Review and retire Cleenseau Raw Emails by routing played exchanges to inter-session source bundles, character-voiced pieces to sources, authorial pieces to narratives, and disposable meta to deletion. Use for one email or an approved batch from the Cleenseau Raw Emails folder.
---

# Cleenseau Email Review

Work through `Campaigns/Cleenseau Campaign/Raw Emails` until each Markdown email has been accounted for and the raw file can be retired. Follow the vault `AGENTS.md`. The user's category definitions below govern this project; the existing `Email Source Index` is a starting inventory, not a final classification or proof that content has been preserved.

## Plan a Review Batch

Read each target email in full. Check its entry in `Campaigns/Cleenseau Campaign/Email Source Index.md`, any `Play by Email` reading copy, `_sessions/cleenseau` source and recap, related writing, relevant canonical notes, and backlinks to the raw file. Inspect attachments and whether their content is already preserved. Search actual mail when available and needed to resolve an incomplete or ambiguous local archive. Avoid creating a second copy of material already preserved elsewhere.

Before an interpretive batch, show the user a compact preview: raw files, proposed route and destination, useful content already covered, proposed note/link/index changes, attachments, and raw files to retire. Wait for approval of that scope under `AGENTS.md`. If a file proves materially more complicated than previewed, revise the preview before editing it.

## Classify the Authored Content

Classify substantive pieces within a thread, not merely its subject line or index label. One email archive may require more than one destination.

- **Disposable meta:** Scheduling, rules, process, or other out-of-game discussion with no unique useful campaign content. Retire after checking for links and attachments.
- **Play by email:** Actual GM and player turns with back-and-forth that advance or resolve play. Quoted reply history alone does not count as another turn. Put the full correspondence in a source bundle under `_sessions/cleenseau`; the session-note workflow builds the structured inter-session note.
- **In-world source:** A piece authored by one real person that speaks entirely or almost entirely from a character's perspective. This includes a tale the character tells, an in-world letter, and an internal monologue. Preserve the authored wording in `Stories/Told In World` or, for a letter or other document, `Letters and Other Writings`.
- **Authorial narrative:** A piece authored by one real person to describe an event from an authorial perspective, rather than in a character's voice. Preserve the authored wording in `Stories/Authorial Narratives` and use the `story` descriptive tag.

The number of real authors and whether they take turns decides play by email versus a separately authored piece. Dialogue between fictional characters in one person's story is not GM/player back-and-forth. The narrative voice decides source versus authorial narrative; length does not. Third-person narration that reports a character's thoughts is not by itself an in-world source: look for text presented as that character's own telling or thoughts. Keep proposals and theories distinct from established material. Under `Note Categorization`, `story` is an authorial campaign record with equivalent canonical weight to a session note, while `source` is for in-world text; do not copy the `source` tag onto an authorial narrative merely because neighboring story notes use it.

Out-of-game correspondence can also contain accepted setting or character facts. Extract those into the relevant notes before retiring the email, using vault evidence and the user's adoption of any proposal. Do not treat an old index label such as `Extractable Info` as permission to canonize a proposal. Ask the user when acceptance or the correct destination cannot be established.

## Preserve and Handoff

For play by email, establish the proper inter-session bundle and chronology from evidence; do not infer an in-world date or session number solely from email timestamps. Preserve the complete local source correspondence, including its sender and send-date evidence, in that bundle's `sources/` directory. Prepare the source manifest and authored-turn input as required by the current session pipeline. Then use `session-note-prep` and `cleenseau-note` for recap review and the final structured session note. For an email-based session, treat the correspondence as the primary play record and apply `cleenseau-note`'s Dreamwidth-specific steps only when a Dreamwidth post exists. If a suitable session already exists, add only missing source coverage and make durable corrections in its reviewed recap or upstream source, respecting the human-edited recap boundary. A `Play by Email` reading copy may help comparison, but it is not the new destination for this workflow.

For a source or authorial narrative, retain the full authored piece, its actual author and email date, and enough provenance to identify the original correspondence without leaving a link to a deleted raw note. Strip transport clutter and duplicate quoted history only when they are not part of the authored piece. Apply the vault's metadata, status-tag, uncertainty, and link rules to any content note created or edited. Link separate writings from the appropriate session recap's `Related Writings` section when relevant.

## Retire the Raw File

Retire a raw email only after every useful authored piece and accepted fact is accounted for, the replacement and any source bundle have been read back and verified, attachments have a disposition, and references to the raw note have been updated or deliberately removed. Update `Email Source Index.md` so its inventory, counts, and links describe the remaining files accurately. Handle duplicates by verifying the surviving copy, not by producing another destination. Confirm the changed paths and scoped diff, run `git diff --check`, and report what was preserved, extracted, and retired. Leave unresolved files in place with the specific decision needed from the user.

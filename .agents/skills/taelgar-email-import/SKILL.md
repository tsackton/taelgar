---
name: taelgar-email-import
description: Find Taelgar worldbuilding correspondence in connected Gmail and preserve it as readable, source-faithful notes under Worldbuilding/Chats and Emails/Emails. Use for new imports, completeness checks, and reformatting existing email notes.
---

# Taelgar Email Import

Preserve worldbuilding correspondence as development sources, not canon. Follow the vault `AGENTS.md` and the user's stated correspondents, dates, exclusions, and approval scope. This skill does not route Cleenseau play-by-email records; use `cleenseau-email-review` for those.

## Find and match the source

- Search both sent and received Gmail, in the requested date windows. When the user asks for six-month chunks, complete each January–June or July–December window before advancing. Search participant addresses, subject variants, and distinctive body phrases; inspect full threads, not snippets alone. Check forwards and messages to other recipients when a named vault note points to them. Do not infer that an email is absent from a failed exact-subject search.
- Exclude scheduling, access links, and other logistics unless a message also contains substantive worldbuilding. Preserve the substantive passage and its context. Keep exploratory ideas and disagreements explicitly tentative.
- Inventory `Worldbuilding/Chats and Emails/Emails` before writing. Match candidates by participants, date, body, forwarded source, and subject, including notes whose filename differs from Gmail's subject. Search note text and backlinks for a duplicate. A matching existing note is the destination even when its formatting is poor or its content incomplete; keep its filename. If the user has deleted a note, respect that choice and check whether a surviving note already holds the exchange.
- For each genuinely new subject, show the user the Gmail subject, dates, brief content description, and proposed note title; obtain approval for that subject before creating a file. Group proposed subjects into a compact batch when useful, but make each choice explicit. Replacing a matched note is covered by the authorized import or reformat scope. Follow `AGENTS.md` if the number or nature of edits grows beyond that scope.

## Build the reading copy

- Read every relevant message's full MIME body in chronological order. Give each original message a sender and send-date heading. Keep forwarded messages identifiable by their original sender, recipient, and date rather than assigning their text to the person who forwarded them. Use the original Gmail subject in the note heading or source context; retain an established filename when it differs.
- Keep each author's substantive wording, uncertainty, and sequence. Repair hard wraps and paragraph spacing, and convert simple emphasis, lists, and links into readable Markdown. Remove transport headers, signatures, footer noise, and repeated quoted history after confirming the original messages are represented. Do not silently merge different authors' words or treat a proposal as accepted canon.
- When a reply answers inline quotations, preserve enough of each quoted prompt beside the reply, or use a precise contextual heading, so short reactions such as “yes” or “this works” have a clear referent. Remove only redundant copies of the quoted text. If the original quoted message is unavailable, retain the quoted passage needed to understand the answer and identify its attribution.
- Save relevant attachments in `Emails/assets` with collision-safe names and link or embed them from the note. Verify that each saved file opens and each reference resolves. If an attachment cannot be retrieved, identify it in the handoff rather than presenting the import as complete. Do not save mail transport files or unrelated attachments as worldbuilding assets.
- Add `status/check/ai` to every new or edited content note, applying the current `Note Categorization` and `Metadata Specification` rules. Preserve any existing metadata and other status tags. Do not change canonical reference notes while importing development correspondence.

## Verify and report

Compare the finished note against the Gmail messages for complete substantive coverage, correct attribution, dates, inline-reply context, and attachment disposition. Re-read each changed file in full; check YAML, wikilinks, asset paths, the complete scoped diff, and `git diff --check`. Preserve unrelated working-tree changes and user deletions. Report which notes were created, replaced, already complete, unavailable in the connected account, or left for an approval decision. Gmail access for this workflow is read-only; do not label, archive, delete, draft, or send mail.

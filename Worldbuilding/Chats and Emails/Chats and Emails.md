# Chats and Emails

This folder preserves worldbuilding correspondence and older development documents as readable source notes. These exchanges record proposals, alternatives, disagreements, and decisions in their original context; inclusion here does not by itself make an idea canon. Imports should preserve authorship, dates, substantive wording, and uncertainty rather than turn conversations into lore summaries.

## Contents and coverage

- **Chats:** dated Discord and text-message exchanges. The Tim–Mike Discord archive is current through **Oct 01 2026**, with reviewed coverage tracked in `discord-export-state.json` using America/New_York calendar days.
- **Emails:** worldbuilding email threads and their relevant attachments. **Early Taelgar Emails (1997-2000)** holds the older correspondence collection.
- **Google Drive:** reading copies of development documents, including archived comment threads and relevant images.

iMessage should include all relevant worldbuilding texts between Tim and Mike. More campaign-relevant material could potentially be pulled from group chats and individual texts with Schwartz, Kong, and Eric for Dunmar campaign cleanup; that work has not been done.

## Pulling in more sources

### Discord

Use the `discord-chat-export` skill. For the established Tim–Mike archive, request a catch-up through a completed date, for example: “Use discord-chat-export to catch up the Tim–Mike worldbuilding chats through yesterday.” For another channel, specify the channel, participants, date range, destination, and whether to retain the complete conversation or only relevant worldbuilding.

The workflow uses the local exporter in `D:\personal\taelgar-utils`, or processes a supplied JSON export. Raw exports and downloaded media stay in private staging outside the vault. Review proceeds day by day: curated notes retain substantive worldbuilding and necessary reply context, mark omitted spans, and preserve relevant attachments. The checkpoint advances only after a whole day is reviewed, including days with nothing relevant. Catch-up runs stop at yesterday so the final day is complete; deliberate re-exports use a separate checkpoint and require approval before replacing existing notes.

Live export requires a locally supplied credential and a discussion of the user-account automation risk described in the skill. Do not put credentials in chat or vault notes. An existing JSON export can be processed without live Discord access.

### Email

Use the `taelgar-email-import` skill with connected Gmail. Specify correspondents, dates, and any topics or exclusions, for example: “Find Taelgar worldbuilding emails between Tim and Mike from January through June 2024, and propose any missing imports.”

Search sent and received mail, inspect full threads, and compare against existing notes before importing. New subjects are presented for approval with their dates, a short description, and proposed title. Reading copies preserve chronological attribution, forwarded-message identities, and inline-reply context while removing redundant quoted history and transport clutter. Relevant attachments go in `Emails/assets`. Gmail access is read-only. Cleenseau play-by-email material follows the separate `cleenseau-email-review` workflow.

### Google Drive

Use the `gdrive-doc-source` skill and provide the Google Doc URL or document ID, for example: “Import this Google Doc into the Google Drive source archive, including open and resolved comments.” Specify explicitly if an existing source copy should be replaced.

The workflow reads all document tabs and comment threads, including replies and resolved comments, and preserves a readable Markdown copy with provenance and a comment archive. It retains struck-through words while removing their strikeout formatting, records that treatment, and saves available inline images as local assets. Use this folder's established `Google Drive` area as the destination. Report inaccessible images or unresolved historical comment context as gaps. The import does not modify the original document or resolve its comments.

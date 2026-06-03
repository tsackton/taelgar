---
headerVersion: 2023.11.25
tags: [status/check/ai]
---

# Incoming Chats Classification Review Index

%% AI note: Created 2026-06-03. The review metadata has been moved into the incoming notes themselves under `## Incoming Cleanup Review`; this index is only for clicking through review groups. %%

## Summary

The incoming note metadata now lives on the notes themselves. These Dataview blocks auto-update from the `classification` and `action` YAML frontmatter fields in:

- `Worldbuilding/Chats and Emails/_discord_incoming`
- `Worldbuilding/Chats and Emails/_iMessage_incoming`

Open a note below, edit YAML `classification` and `action` if needed, then edit the `## Incoming Cleanup Review` YAML block for subject, split, target title, confidence, or notes. The old Discord source replacement map remains separate as a table.

## Metadata Checks

```dataview
TABLE classification AS "Classification", action AS "Action"
FROM "Worldbuilding/Chats and Emails"
WHERE (file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming")
  AND (classification = null OR action = null)
SORT file.path ASC
```

## Classification Counts

```dataview
TABLE length(rows) AS "Count"
FROM "Worldbuilding/Chats and Emails"
WHERE file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming"
GROUP BY classification
SORT classification ASC
```

## Action Counts

```dataview
TABLE length(rows) AS "Count"
FROM "Worldbuilding/Chats and Emails"
WHERE file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming"
GROUP BY action
SORT action ASC
```

## Needs Review

```dataview
TABLE action AS "Action"
FROM "Worldbuilding/Chats and Emails"
WHERE (file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming")
  AND classification = "needs-review"
SORT file.name ASC
```

## Worldbuilding Mixed

```dataview
TABLE action AS "Action"
FROM "Worldbuilding/Chats and Emails"
WHERE (file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming")
  AND classification = "worldbuilding-mixed"
SORT file.name ASC
```

## Worldbuilding

```dataview
TABLE action AS "Action"
FROM "Worldbuilding/Chats and Emails"
WHERE (file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming")
  AND classification = "worldbuilding"
SORT file.name ASC
```

## Tooling Meta

```dataview
TABLE action AS "Action"
FROM "Worldbuilding/Chats and Emails"
WHERE (file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming")
  AND classification = "tooling-meta"
SORT file.name ASC
```

## Campaign Logistics Only

```dataview
TABLE action AS "Action"
FROM "Worldbuilding/Chats and Emails"
WHERE (file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming")
  AND classification = "campaign-logistics-only"
SORT file.name ASC
```

## Non-DND

```dataview
TABLE action AS "Action"
FROM "Worldbuilding/Chats and Emails"
WHERE (file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming")
  AND classification = "non-dnd"
SORT file.name ASC
```

## Custom Or Unexpected Classifications

```dataview
TABLE classification AS "Classification", action AS "Action"
FROM "Worldbuilding/Chats and Emails"
WHERE (file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming")
  AND classification != "needs-review"
  AND classification != "worldbuilding-mixed"
  AND classification != "worldbuilding"
  AND classification != "tooling-meta"
  AND classification != "campaign-logistics-only"
  AND classification != "non-dnd"
SORT classification ASC, file.name ASC
```

## Manual Review Action

```dataview
TABLE classification AS "Classification"
FROM "Worldbuilding/Chats and Emails"
WHERE (file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming")
  AND action = "manual-review"
SORT file.name ASC
```

## Promote After Cleanup Action

```dataview
TABLE classification AS "Classification"
FROM "Worldbuilding/Chats and Emails"
WHERE (file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming")
  AND action = "promote-after-cleanup"
SORT file.name ASC
```

## Promote Action

```dataview
TABLE classification AS "Classification"
FROM "Worldbuilding/Chats and Emails"
WHERE (file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming")
  AND action = "promote"
SORT file.name ASC
```

## Leave Incoming Actions

```dataview
TABLE classification AS "Classification", action AS "Action"
FROM "Worldbuilding/Chats and Emails"
WHERE (file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming")
  AND (action = "leave-incoming" OR action = "leave-incoming/delete-later")
SORT action ASC, file.name ASC
```

## All Incoming

```dataview
TABLE classification AS "Classification", action AS "Action"
FROM "Worldbuilding/Chats and Emails"
WHERE file.folder = "Worldbuilding/Chats and Emails/_discord_incoming" OR file.folder = "Worldbuilding/Chats and Emails/_iMessage_incoming"
SORT classification ASC, action ASC, file.name ASC
```

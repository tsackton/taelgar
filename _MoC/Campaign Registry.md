# Campaign Registry

linterAudienceSpecialValues:: "all", "none"

The field above records the reserved non-campaign `audience` values recognized by the validator. It does not settle the positive campaign-audience design discussed below.

Each key in `_sessions/campaign-registry.json` is a campaign ID. Its value is the vault-relative path to that campaign’s index note. To register a game, create the index note and add the ID and path to the registry. Edit its display name and description in the index note.

## Campaign metadata

Use the lowercase ID anywhere authored data identifies a campaign, including session-note `campaign`, entries in `knownTo`, the `campaign` inside `campaignInfo`, and campaign blocks such as `%%^Campaign:dufr%%`. The `none` block remains reserved for DM material. Game-update tags use the same IDs. The positive semantics of `audience` remain open.

Index notes record `name`, `description`, `dm`, `canon`, and `continuity`. Set `campaignDirectory`, `partyPage`, `sessionBundleDirectory` and `notePattern` when applicable. Session-note patterns are relative to the campaign directory. Set `defaultTemplate` only for an override. The absence of a session bundle directory is valid.

Find a source bundle by its registered directory and its folder's session-number suffix. Each campaign and session number identifies one bundle folder, including folders that only contain raw sources. Bundle lookup reports conflicting paths when two folders identify the same session. A targeted lookup fails on a duplicate for the requested session. Full inventory scans, including publishing and Session Review, stop on a duplicate anywhere in the directories they scan.

Session-note components live in `_generated/session-notes/<campaign>-session-<number>/` under the registered campaign directory. The renderer finds the components from the note's `campaign` and `sessionNumber`. Keep party names, wikilinks, and page titles in their authored form.

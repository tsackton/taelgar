# Campaign Registry

linterAudienceSpecialValues:: "all", "none"

The field above records the reserved non-campaign `audience` values recognized by the validator. It does not settle the positive campaign-audience design discussed below.

Each key in `_sessions/campaign-registry.json` is a campaign ID. Its value is the vault-relative path to that campaign’s index note. To register a game, create the index note and add the ID and path to the registry. Edit its display name and description in the index note.

## Campaign metadata

Use the lowercase ID anywhere authored data identifies a campaign, including session-note `campaign`, entries in `knownTo`, the `campaign` inside `campaignInfo`, and campaign blocks such as `%%^Campaign:dufr%%`. The `none` block remains reserved for DM material. Game-update tags use the same IDs. The positive semantics of `audience` remain open.

Index notes record `name`, `description`, `dm`, `canon`, and `continuity`. Set `campaignDirectory`, `partyPage`, `sessionBundleDirectory` and `notePattern` when applicable. Session-note patterns are relative to the campaign directory. Set `defaultTemplate` only for an override. The absence of a session bundle directory is valid.

## Session bundles and notes

Look up the campaign ID in the registry and open its index note. Find the source bundle under `sessionBundleDirectory` by matching the complete session-number suffix of a numbered folder. In the other direction, the registry entry for the parent directory supplies the campaign ID, and the folder suffix supplies the session number. Leading zeros in the whole number are padding. Keep the entire point suffix so `12.1` and `12.10` remain distinct.

To preview a bundle path from the vault root, run:

```sh
python3 -B _scripts/session_bundles.py dufr 139
```

This prints the existing or proposed path without creating it. For work on a prepared session, verify that the folder and its single `cleaned/*-session.yaml` manifest exist. Use the actual manifest stem for adjacent artifacts. For example, the bundle `dunmari-frontier-139` contains `dunmar-frontier-139-session.yaml` and `dunmar-frontier-139-session-recap.md`.

Each campaign and session number identifies one bundle folder, including folders that only contain raw sources. Bundle lookup reports conflicting paths when two folders identify the same session. A targeted lookup fails on a duplicate for the requested session. Full inventory scans, including publishing and Session Review, stop on a duplicate anywhere in the directories they scan.

To find the final session note, use `notePattern` relative to `campaignDirectory` and verify the file exists. `{session}` uses the canonical session number. `{session_padded}` pads the whole part to at least two digits and keeps the point suffix.

Session-note components live in `_generated/session-notes/<campaign>-session-<number>/` under the registered campaign directory. The renderer finds the components from the note's `campaign` and `sessionNumber`. Keep party names, wikilinks, and page titles in their authored form.

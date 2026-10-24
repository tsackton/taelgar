# Taelgarverse Code

The maintained native header renderer and Obsidian plugin source live in
`taelgarverse-core`. See [[Native Headers]] for note authoring and local export,
and the core plugin README for feature settings and the build/install workflow.

## Vault code

- `_scripts/customJS` provides shared metadata, date, relationship, token, and
  query services used by existing Dataview queries and session templates.
- `_scripts/view` contains Dataview views for timelines, campaign interactions,
  and other query output.
- `_scripts/templater` contains the session-note renderer and query-date helper.
- `_scripts/build_session_note_components.py` owns session components and the
  associated campaign-note pipeline. Session presentation belongs in its
  templates rather than the generic biography renderer.

## Campaign interactions

`knownTo` records which campaign parties know a subject. Session recaps and
official session notes provide evidence for the plugin's interactions view.
An explicit native interaction block can be included when needed:

````markdown
```taelgar-interactions
```
````

Campaign identities, lowercase codes, party pages, and session paths are defined
in `_scripts/session_note_campaigns.json`; see [[Campaign Registry]].

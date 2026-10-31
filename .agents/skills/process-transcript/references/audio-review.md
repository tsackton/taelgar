# Optional audio review

Enter here directly for “generate an audio review page for X, Y, Z,” including when
the user names process-transcript. This mode builds a listening interface only.
Do not run initial transcript processing, cleanup, polishing, or quality jobs.
It can use quality-complete portable review questions, or open a bounded review for selected
UIDs from current finalized references. Never recreate the old processing queue.
If those references are unavailable, report the missing input instead of starting
unrequested processing. An unfinished provisional export must finish its existing
quality work before becoming a human-review page; this mode does not run that work.

## Select and prepare

Resolve the user's sessions/passages. Read the relevant exchange and existing
review questions, not every transcript again. Prefer existing issue IDs; when the
user selects new passages, supply their UIDs. A new selection opens questions only
for those UIDs; it does not automatically inventory all unresolved markers.

Verify the recording and its clock from the session's sourceAudioPath, recording
manifest, or preparation evidence. Do not guess offsets from filenames. The shared
audio helper accepts explicit UID ranges and offsets; split mappings at timestamp
resets or recording changes. `verified: true` records actual inspection of that
mapping, not a way to silence an error. Multi-recording passages need separate
review items. Ask for a recording/alignment only when available evidence cannot
resolve it. Local clipping does not upload audio.

The helper is `scripts/transcript_audio_review.py` in this skill. Commands below
run from the vault root with Python 3.10+ and PyYAML. Set `HELPER` to that script.
Use one fresh output directory outside the vault, such as beside the recordings
or under the system temporary directory. Existing owned cache directories may be
reused. The directory contains disposable HTML and clips, never decision state.

Supply this selection object on stdin to `prepare --selection -`; it is transient
command input, not another persisted review file:

```json
{
  "sessions": [
    {
      "bundle": "/absolute/path/to/session-bundle",
      "issueIds": ["issue-id-from-review"],
      "paddingSeconds": 10,
      "recordings": [
        {
          "startUid": "u0001", "endUid": "u2400",
          "audioPath": "/absolute/path/to/recording.m4a",
          "offsetSeconds": 0, "verified": true
        }
      ]
    }
  ]
}
```

Use `"uids": ["u0042", "u0105"]` instead of `issueIds` for selected passages.
Existing questions on those UIDs are reused; missing ones are added. Omitting both
selects the existing review questions; it cannot open an unspecified finalized
session. Add more session entries to create one combined page. Increase padding
when the user needs more listening context; preparation reuses unchanged clips and
keeps saved answers. Verified mappings and selections are saved in each review
Markdown header so resuming needs no companion JSON file. On repeated prepare,
`recordings` may be omitted to reuse that session's saved mapping.

```bash
python3 -B HELPER prepare --selection - --output-dir /path/outside/vault/audio-review
python3 -B HELPER serve --bundle /path/to/session-a --bundle /path/to/session-b --output-dir /path/outside/vault/audio-review
```

Start the local server and open its printed localhost URL. Keep it running while
the user listens. Do not wait for it to finish in a blocking command. The page shows
the current wording, proposal, full exchange, polished attribution, playback speed,
and an answer box. The user need not supply an entire corrected UID or any offsets.

## Answers and normal chat continuation

The page saves answers directly to the review Markdown under the session lock:

- **Save answer:** preserves the user's words verbatim for the agent to interpret.
- **Use proposed reading:** records acceptance of the displayed proposal.
- **Leave unresolved:** records a decision to retain the uncertainty.
- **Defer for later:** preserves an open question; it is not acceptance.

No transcripts are edited by the page. Changed questions/transcripts reject stale
saves while keeping the user's typed answer on screen. Navigation keeps unsaved
drafts in the open page; saved answers survive restarting the server.

When the user returns, read saved answers:

```bash
python3 -B HELPER answers --bundle /path/to/session-a --bundle /path/to/session-b
```

Continue [the normal review](review.md): record clear choices, update affected
polished turns, apply once, and finalize each completed session. Use the shared
correction helper when attribution or display changes need it, without invoking
a separate skill workflow. Ask only when the answer itself needs clarification;
do not ask the user to approve their exact answer again. Do not rerun full cleanup,
quality review, or repeat checks already performed by application/finalization.
For a page-only request, opening the page does not authorize applying answers
before the user returns. If all questions are deferred, keep the review open.

Stop the local server when listening is finished. Remove only its generated cache:

```bash
python3 -B HELPER clean --output-dir /path/outside/vault/audio-review
```

This refuses unrelated files and leaves saved answers intact. Rebuild clips later
from the review's mappings if needed. Normal session finalization retires completed
review Markdown. Never delete original recordings or unneeded-looking user files.

## Shared audio implementation

`_scripts/audio_tools.py` owns duration probing, verified UID-to-recording mapping,
clip extraction, and the ffmpeg/macOS fallback. Transcription speaker samples and
session audio highlights use the same extraction code. Review/sample clips use
compact speech settings; highlights retain their separate output profile. The
fallback preserves the source encoding when it is compatible with M4A. Keep this
code shared rather than introducing another clipper into the page helper.

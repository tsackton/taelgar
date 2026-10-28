# Agreed bulk extraction and review workflow

The [model overview](MODEL_OVERVIEW.md) defines schema version 5. This workflow targets 150–200 sessions with limited human review.

1. **Prepare:** reuse a cleaned transcript with stable UIDs and session metadata; build a reusable vault index of names, aliases, entity kinds and places. Do not use beats or beat-facts during initial extraction.
2. **Extract:** read the complete transcript and produce a draft session object, with honest confidence estimates and `unreviewed` status. Confidence may be high on clear evidence; no review has happened yet.
3. **Validate:** check structure, source hashes, ranges, references, vault paths and exact quote text mechanically. Validation never promotes confidence or review status.
4. **Automated review:** separately assess aggregate dates, PC attendance, linked locations and each entity. Review transcript evidence and candidate vault matches. Existing beats/beat-facts can identify omissions or conflicting chronology; use relevant portions when helpful and verify against the transcript. They are not required, and note-only events are excluded.
5. **Correct once:** revisit unresolved critical records with targeted source context, update dependent data and revalidate. Reassess the correction; do not mechanically raise confidence. At most one targeted correction attempt before queuing remaining critical uncertainty for humans.
6. **Continue the batch:** critical records at high confidence after automated/human review are ready for normal use. Unreviewed scene divisions and interactions can be used with their flags. Unresolved critical records remain explicitly provisional. Human review concentrates on the queue and a small sample of otherwise accepted sessions.

**Review units and meaning**

`review` on the session covers aggregate dates, PC attendance and linked locations. `sceneReview` covers the complete scene division. Each entity and each interaction has its own optional `review`. No per-field flags and no individual-scene confidence.

Confidence: `high` means clear support without material ambiguity; `medium` means supported but inferential or ambiguous; `low` means tentative, weakly supported or conflicting. Status: `unreviewed`, `automatedReviewed`, or `humanReviewed`. Human review does not automatically mean high confidence.

**Token use and provenance**

Reuse the vault index. Give the automated reviewer critical records, relevant source windows and candidate matches; expand context where needed. Some whole-session checks remain necessary because evidence-window review can miss omitted entities. Preserve source UIDs and keep complete conversational encounters through minor interjections. Do not regenerate an entire session to repair one match.

Once human edits exist, regeneration should produce a reviewable candidate and preserve the existing accepted file. Source changes invalidate prior evidence and require explicit reconciliation. Source coverage and reviewer rationale can be retained as execution artifacts; their general UI and long-term storage are implementation questions, not additions to canonical `session.json`.

The existing recap pipeline may supply useful review hints, but this extraction does not depend on completing that pipeline. No other-source extractor is included in this implementation.

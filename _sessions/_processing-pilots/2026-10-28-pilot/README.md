# Process Transcript: ten-session cloud pilot

This is the authorized pilot, not the overnight rollout. The controller may launch exactly the ten sessions in `manifest.json`, one fresh cloud chat per session, using `gpt-6-astra` at medium reasoning. Do not replenish the queue beyond these ten until the user reviews the pilot.

The code and input base is `56d8ff6e3e61de34a160d30a185710e956c0e214`. The integration branch is `cloud/process-transcript-pilot-20261028`; its single draft PR targets `main`. No merge to `main` is authorized.

Workers follow `worker-prompt.md` and their manifest row. They may modify only their assigned session bundle and publish only their assigned worker branch. Each worker starts from the pinned base, verifies the complete bundle fingerprint, and follows the current `process-transcript` skill. No compatibility cases are assigned. No worker edits this controller directory or launches another worker.

## Integration contract

1. The controller records each worker chat ID and launch time in the manifest. One assignment has one owner; do not overlap retries. A replacement resumes the existing worker branch/checkpoint after its previous owner has stopped.
2. Accept a result only with the worker ID, pinned base, branch, exact commit, changed paths, helper status, finalization state, and any manual-review path/counts. A publication failure is a blocked delivery, not a completed integration.
3. Fetch the worker branch and verify its commit descends from the pinned base. Check every changed path against the assigned bundle prefix. Verify that the integration checkout's current complete bundle file map still matches `baseFiles`; a discrepancy stops this session for reconciliation. Never reset, overwrite, or resolve conflicts by discarding newer work.
4. Integrate scoped worker commits sequentially. Recheck the helper's read-only `status` and source fingerprints on the integrated bundle, review the diff, and run scoped `git diff --check`. Confirm finalized references are current, or that a pending review checkpoint retains its work state and exported decision sheet. Stop on a structural, stale-source, or publication discrepancy while allowing independent sessions to finish.
5. Update this manifest and `decision-queue.md` after each result. Record the worker commit and resulting integration commit, outcome, verification, pending issue/group counts, and links. Keep usage observations in the controller; workers must not invent usage telemetry or trigger a reset themselves.
6. Push the integration branch incrementally and update the one draft PR with actual pilot outcomes. Keep the PR a draft for user review. Do not launch the overnight queue or merge to `main`.

`baseBundleSha256` is SHA-256 of the UTF-8 JSON serialization of `baseFiles`, using sorted keys, compact separators `,` and `:`, and `ensure_ascii=False`. `baseFiles` maps every bundle-relative regular-file path to the SHA-256 of its bytes. Reject unexpected added/deleted files at the initial worker and pre-integration checks; do not follow symlinks.

The worker must finalize when the actual helper reports current exports and `complete` or `complete_with_uncertainty` after all clean, polish, and quality jobs. Pending consequential decisions require a resumable checkpoint and a concrete review sheet, not fabricated acceptance. Finalized sessions retain only the workflow's permanent products plus unrelated pre-existing session artifacts. A manual-review checkpoint retains the complete session-local work directory; optional ignored HTML may be regenerated. Check checkpoint sizes before publishing and report any delivery limit rather than silently discarding state.

## Pending full-run queue

`full-run-queue.json` contains 147 verified sessions awaiting pilot review and separate full-run authorization. It includes the nine repaired compatibility cases from upstream commit `d74f8030f82b61d130b23f89df926d5c57a676b5`. All nine passed helper initialization on temporary copies, with live source hashes unchanged. The update changes neither the skill nor any active pilot bundle. The ten launched assignments retain their original base and fingerprints. No additional worker launch is authorized.

## Cases deliberately excluded from this pilot

- Already finalized and current: Dunmar 010 and 041.
- Repaired speaker-header cases, now in the pending full-run queue: Dunmar 004, Feywild 003, Dragonets 001.
- Repaired empty-unit cases, now in the pending full-run queue: Dunmar 059, 062, 065, 091, 092, 094.
- Non-transcript bundles: Dunmar 096, 107, 135; Mawar 001.

The manifest is the outer controller's authorized launch and integration ledger. Each processing worker continues to use only its own bundle-local work queue; it must not use this directory as a shared correction store.

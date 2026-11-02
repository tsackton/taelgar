# Pronunciation Audio API Proposal

> [!info] Proposal
> Prepared November 2, 2026. High-priority API tooling candidate. Implementation has not started; this document records the proposed scope and first experiment.

## Objective and API value

Provide playable pronunciation examples for Taelgar names, using adopted written pronunciations as the source. A player or DM should be able to hear a name rather than reconstruct its sound from a written guide.

The API supplies speech generation, a capability beyond the existing text-based name review. Codex can select names, prepare requests, and manage review, but the resulting audio requires a speech model. Approved clips can be reused indefinitely without a model call each time someone plays them.

## Existing foundation

[[Name Metadata]] defines accepted pronunciations and the distinction between documented, inferred, proposed, disputed, and unresolved name information. Accepted primary pronunciations belong in frontmatter; alternate forms and proposals can appear in `Metadata:names:v1` blocks.

Use those existing conventions. This tool does not invent pronunciations or adopt pending proposals. When the written sources disagree or a name lacks an accepted pronunciation, return it for ordinary name review. Placeholder values such as “obvious” are not speech-generation instructions.

## First useful version

Generate a small review batch for explicitly selected names with accepted pronunciations:

1. Read the exact name form, accepted pronunciation, and any adopted relevant language guidance.
2. Generate a short isolated pronunciation. Optionally include a neutral carrier phrase if it improves intelligibility.
3. Present playback beside the source pronunciation, with accept, reject, and regenerate actions.
4. Save an approved audio asset and its provenance. Keep rejected candidates out of the published collection.
5. Expose approved clips through a simple pronunciation list or existing note/website presentation, with the exact integration selected during implementation.

Start with a neutral stock voice. Voice cloning, character performances, and accent design are outside the initial scope. Spoken recaps are a possible later extension, not a prerequisite or part of the initial pronunciation deliverable.

## Pronunciation control and review

A written pronunciation guide does not guarantee that a speech model will pronounce the name correctly. Evaluate the selected endpoint's supported controls rather than assuming it accepts IPA, SSML, or a pronunciation dictionary. Where supported, use pronunciation instructions; otherwise evaluate phonetic respelling or suitable carrier phrases.

Keep generation-specific respellings separate from canonical name metadata. A workaround that makes one model say the right sound must not replace the accepted name or written pronunciation.

Human listening is the acceptance criterion. Automatic retranscription can provide a diagnostic but cannot prove correct stress, vowels, or consonants. Include names from different naming traditions in the pilot, especially sounds the chosen voice may render poorly. If a pronunciation cannot be reproduced adequately, retain the written guide and mark audio as unavailable.

## Assets and updates

Each asset needs the source note/name identity, accepted pronunciation, source fingerprint, model/version, voice, generation settings, and approval state. Cache on these inputs so unchanged names do not incur repeated generation charges.

When an adopted pronunciation changes, mark the previous clip stale and queue a replacement for review. Do not silently publish a new rendering. Keep an explicit mapping from approved asset to published name; choose final paths and note integration before bulk creation. Private language guidance or metadata used during generation must not be copied into public manifests.

Initially run on demand. A later build hook or scheduled job could discover changed adopted pronunciations and prepare a bounded review batch. Automatic discovery need not imply automatic publication.

## Pilot and acceptance

Choose a small batch of commonly encountered names whose pronunciations are settled. Test isolated names and carrier phrases, then assess pronunciation accuracy, time spent regenerating, usefulness to listeners, and cost per accepted clip.

Verify that accepted clips match their displayed names, rejected/stale clips are not published, repeated runs reuse unchanged results, and canonical metadata remains unchanged. Test playback in the intended website or Obsidian surface before expanding the collection.

## Cost and implementation decisions

Costs depend on the selected endpoint's text/audio billing and the number of candidate generations. Clip playback should use ordinary hosted files and incur no inference cost. Limit candidates per name and total batch spend; measure actual pilot usage before estimating a full-vault run.

Before implementation, choose the initial names, voice/model, review surface, asset location, and publication integration. The first milestone is a handful of approved clips that can be played beside their written pronunciation guides.

Related proposals: [[Transcript Audio Resolver API Proposal]] and [[Private Discord Chatbot API Proposal]].

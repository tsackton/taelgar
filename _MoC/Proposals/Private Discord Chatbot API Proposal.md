# Private Discord Chatbot API Proposal

> [!info] Proposal
> Prepared November 2, 2026. Implementation has not started. The existing website export already solves player-safe publication; this proposal consumes that export rather than designing another spoiler-filtering pipeline.

## Objective and API value

Let approved players ask questions about Taelgar in a private Discord server and receive concise answers with links to the supporting website pages. The service should be available without the DM starting or supervising a Codex session.

This is an ongoing application use of API credits: players' questions trigger retrieval and answer generation. Codex can build and maintain the application, but it is not the player-facing runtime. Search exists to support these answers; a standalone semantic-search product is not required.

## First useful version

Support one server, one campaign, one designated channel, and an explicit allowlist of player IDs. Provide a server-scoped command such as:

```text
/ask question: What do we know about the old watchtower?
```

Each request stands alone initially. The bot checks authorization and available usage allowance, searches the approved export, and returns an answer with source links. When sources are missing or ambiguous, it says so. It must not invent lore or treat character beliefs as established world facts.

Answer visibility follows the designated channel's permissions. Default to channel-visible answers for shared reference; decide whether private responses are useful during the pilot. The bot should not read ordinary conversations, accept direct-message queries, edit notes, browse arbitrary URLs, or execute general-purpose tools.

## Discord setup

The owner needs an ordinary Discord account and permission to manage the target server:

1. Open the [Discord Developer Portal](https://discord.com/developers/applications) and create an application, with a working name such as “Taelgar Archivist.”
2. Configure its bot account and generate a bot token. Store the token in local or hosting secrets, never in Git or a chat message.
3. Disable public installation through the Public Bot setting and configure server installation. Portal labels may change; confirm current settings when implementing.
4. Generate an installation link with the `bot` and `applications.commands` scopes. Grant only required channel and message permissions; no Administrator permission is needed.
5. Install it in the private server. Configure the allowed server, channel, and player IDs in the application.
6. Run a minimal bot and register `/ask` only in that server. First return a fixed acknowledgement to prove setup works without spending model credits.

Slash commands avoid needing the privileged Message Content intent. Disabling public installation is useful but does not replace application-level authorization on every request.

## Runtime and hosting

A small Python service using `discord.py`, or an equivalent maintained library, connects to Discord's Gateway over an outbound connection. No public HTTP endpoint, domain, or router port forwarding is required for this design. The program must remain running; a sleeping laptop makes the bot unavailable.

Test locally, then deploy to an existing always-on machine or a small cloud host that supports a continuous worker and outbound WebSockets. Static website hosting can supply the corpus but generally cannot host this worker. Hosting charges are separate from model API usage.

The service needs the Discord token, model API credentials, allowed IDs, corpus location, and usage limits. Persist usage accounting across restarts. Add restart management, bounded retries, basic health reporting, and an operator stop switch. Acknowledge/defer Discord interactions promptly while retrieval and generation run, then deliver the result within current platform limits.

## Corpus and retrieval

Use the existing website export as the publication boundary. The runtime gets exported player-safe content and canonical public URLs, not the raw vault, DM notes, or unpublished transcripts. Reuse the website's existing campaign perspective where applicable; do not infer access from a model prompt.

Start with a frozen export for the pilot. Split text into passages while retaining page titles, headings, and URLs. Combine exact-name/keyword retrieval with embeddings if semantic retrieval improves real questions. Embeddings are an optional API cost, not a prerequisite for the Discord connectivity milestone.

Generate answers from a bounded set of retrieved passages. Validate that returned citation URLs belong to the supplied source set, and distinguish evidence from unsupported inference. Treat retrieved text as data rather than tool instructions.

After the pilot, refresh the index on successful website export. Index only changed content, remove deleted pages, and atomically activate complete snapshots. Do not answer from superseded deleted content after a successful refresh. Store the export revision with diagnostics so answers can be traced to the corpus used.

## Access and cost controls

Enforce these in ordinary application code before model calls:

- Check server, channel, and user IDs on every request, and reject direct messages or unauthorized use.
- Bound question length, retrieved context, output length, concurrency, retries, and requests per player.
- Maintain per-player allowances and a global spending allowance. Reserve a conservative maximum cost atomically before each request, reconcile actual usage afterward, and stop accepting requests when the allowance is exhausted. Unknown usage after a timeout must not release a reservation prematurely.
- Persist accounting across restarts and deduplicate retried Discord interactions. Separate indexing costs from chat costs while keeping an overall limit.
- Keep credentials in server-side secrets and redact them from logs. Disallow generated mentions from pinging users or roles.

Provider budget alerts supplement these controls; they are not a guaranteed hard spending cap. The model cannot override the allowlist or application accounting. Prompt injection remains an answer-quality concern, but the bot cannot disclose private vault material it never receives.

## Delivery and validation

| Stage | Deliverable | Acceptance |
| --- | --- | --- |
| 1. Discord connection | Registered private bot and fixed `/ask` acknowledgement | Works in the intended channel; unauthorized users, servers, channels, and DMs cannot trigger model work. |
| 2. Grounded answers | Frozen website export, retrieval, model answer, citations | Useful answers to real player questions, valid source links, and clear handling of insufficient evidence. |
| 3. Reliable private service | Persistent limits, deployment, restart handling, diagnostics | Concurrent requests cannot exceed reserved allowance; retries do not duplicate work; restart preserves limits. |
| 4. Export refresh | Incremental index updates from successful website builds | Added, changed, and deleted content is reflected without partial snapshots or raw-vault access. |

Test exact names, vague recollections, ambiguous identities, unsupported questions, malicious instructions, and questions whose answers differ by campaign. Evaluate answers manually against sources. Test access and spending controls independently of model behavior.

An initial prototype is plausibly one or two focused engineering days with credentials, hosting, and export access ready; a dependable private deployment may take several additional days. These are rough estimates, not a delivery commitment. Retrieval quality will need feedback from actual play.

## Decisions needed before implementation

Choose the server/channel, initial campaign and player list, host, model, daily/monthly allowances, and export artifact location. Keep full conversation logging off by default; decide what limited diagnostics are needed and how long to retain them.

The owner creates and installs the Discord application and supplies credentials through secret settings. The implementation work builds the worker, retrieval, accounting, tests, and deployment configuration. The first milestone is Discord connectivity with no model calls; the next is a few cited answers from the already solved player-safe export.

Related proposals: [[Transcript Audio Resolver API Proposal]] and [[Pronunciation Audio API Proposal]].

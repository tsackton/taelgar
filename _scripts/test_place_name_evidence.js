"use strict";

const assert = require("node:assert/strict");

const analyzer = require("./analyze_place_names.js");
const evidence = require("./place_name_evidence.js");

function concept(subjectPath, preferredForm, forms = [preferredForm]) {
  return {
    subjectPath,
    preferredForm,
    forms: forms.map((text) => ({ text })),
  };
}

function run() {
  const defaults = analyzer.parseArgs([]);
  assert.equal(
    defaults.decisions,
    "_Plugins/Name Explorer/Name Decisions.jsonl",
  );
  assert.equal(
    defaults.output,
    "_Plugins/Name Explorer/Place Name Evidence.jsonl",
  );
  assert.equal(
    defaults.summary,
    "_Plugins/Name Explorer/Place Name Evidence Summary.json",
  );
  assert.equal(
    analyzer.parseArgs(["--decisions", "custom/decisions.jsonl"]).decisions,
    "custom/decisions.jsonl",
  );

  const catalog = {
    concepts: [
      concept("Gazetteer/Serrania.md", "Serranía"),
      concept("Gazetteer/Aben.md", "Aben"),
      concept("Gazetteer/Keye.md", "K'eye"),
      concept("Gazetteer/Hope A.md", "Hope"),
      concept("Gazetteer/Hope B.md", "Hope"),
    ],
  };
  const matcher = evidence.buildFormMatcher(catalog);

  const exact = evidence.exactMatchesInLine(
    "Serranía and Aben are named here; Serrania and Abenfyrd are not. K’eye is.",
    matcher,
  ).filter((item) => item.kind === "exact-form");
  assert.deepEqual(
    exact.map((item) => item.subject).sort(),
    ["Gazetteer/Aben.md", "Gazetteer/Keye.md", "Gazetteer/Serrania.md"],
  );

  const ambiguous = evidence.exactMatchesInLine("Hope", matcher);
  assert.equal(ambiguous.length, 1);
  assert.equal(ambiguous[0].kind, "ambiguous-form");

  const disambiguated = evidence.exactMatchesInLine("[[Hope A|Hope]]", matcher, [
    { subject: "Gazetteer/Hope A.md", display: "Hope" },
  ]);
  assert.equal(disambiguated.length, 1);
  assert.equal(disambiguated[0].subject, "Gazetteer/Hope A.md");
  assert.equal(disambiguated[0].disambiguatedByLink, true);

  const transcript = evidence.parseTranscriptLine(
    "[u0042 | 00:01:00.000-00:01:04.000 | DM] Welcome to Serranía.",
  );
  assert.equal(transcript.uid, "u0042");
  assert.equal(transcript.speaker, "DM");
  assert.equal(transcript.speakerRole, "dm");
  assert.equal(transcript.text, "Welcome to Serranía.");

  assert.equal(evidence.sessionNumberFrom("", "Lost in the Feywild - Episode 06"), 6);
  assert.equal(
    evidence.sessionIdentity("lost-in-the-feywild", 6, "", "unused"),
    "lost-in-the-feywild:6",
  );
  assert.equal(
    evidence.sessionIdentity("unknown", null, "special-session", "unused"),
    "key:special-session",
  );

  const campaignInfo = evidence.parseCampaignInfo([
    "tags: [place]",
    "campaignInfo:",
    "  - campaign: DuFr",
    "    type: visited",
    "    date: 1748-01-02",
    "name: Example",
  ]);
  assert.deepEqual(campaignInfo, [{ campaign: "DuFr", type: "visited", date: "1748-01-02" }]);

  const lines = evidence.contextualLines([
    "---",
    "tags: [place]",
    "---",
    "# Heading",
    "Visible text.",
    "%% naming brainstorming %%,",
    "%%^Campaign:DuFr%%",
    "Campaign text.",
    "%%^End%%",
  ].join("\n"));
  assert.ok(lines.some((line) => line.context === "comment" && /naming/.test(line.text)));
  assert.ok(lines.some((line) => line.campaignScope === "DuFr" && /Campaign text/.test(line.text)));

  assert.equal(
    evidence.renderVisibleText("At [[Gazetteer/Vostok|the region]], not the displayed name."),
    "At the region, not the displayed name.",
  );

  console.log("Place-name evidence unit tests passed.");
}

run();

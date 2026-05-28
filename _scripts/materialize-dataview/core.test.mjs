import assert from "node:assert/strict";
import test from "node:test";
import core from "./core.js";

test("scanFencedCodeBlocks handles ordinary Dataview fences", () => {
  const input = ["before", "```dataview", "LIST FROM #person", "```", "after"].join("\n");
  const blocks = core.scanFencedCodeBlocks(input);

  assert.equal(blocks.length, 1);
  assert.equal(blocks[0].language, "dataview");
  assert.equal(blocks[0].body, "LIST FROM #person\n");
  assert.equal(blocks[0].closed, true);
});

test("scanFencedCodeBlocks accepts longer closing fences", () => {
  const input = ["```dataview", "TABLE file.link", "````", "tail"].join("\n");
  const blocks = core.scanFencedCodeBlocks(input);

  assert.equal(blocks.length, 1);
  assert.equal(blocks[0].endLine, 3);
  assert.equal(input.slice(blocks[0].end), "tail");
});

test("scanFencedCodeBlocks strips callout quote prefixes from body", () => {
  const input = [
    "> [!info]",
    "> ```dataview",
    "> TABLE file.link",
    "> FROM #place",
    "> ```",
  ].join("\n");
  const blocks = core.scanFencedCodeBlocks(input);

  assert.equal(blocks.length, 1);
  assert.equal(blocks[0].quoteDepth, 1);
  assert.equal(blocks[0].body, "TABLE file.link\nFROM #place\n");
});

test("inline parser recognizes header views and campaign interaction calls", () => {
  const pageDate = core.parseKnownInlineExpression('dv.view("_scripts/view/get_PageDatedValue")');
  assert.equal(pageDate.kind, "pageDatedValue");

  const campaign = core.parseKnownInlineExpression(
    'customJS.OutputHandler.outputCampaignInteractions(dv.current().file.name, dv.current(), "DuFr")',
  );
  assert.equal(campaign.kind, "campaignInteractions");
  assert.equal(campaign.campaign, "DuFr");
});

test("findInlineDataviewExpressions ignores protected fenced ranges", () => {
  const input = [
    "`$=dv.view(\"_scripts/view/get_Whereabouts\")`",
    "```markdown",
    "`$=dv.view(\"_scripts/view/get_Whereabouts\")`",
    "```",
  ].join("\n");
  const protectedRanges = core.scanFencedCodeBlocks(input).map((block) => ({
    start: block.start,
    end: block.end,
  }));
  const expressions = core.findInlineDataviewExpressions(input, protectedRanges);

  assert.equal(expressions.length, 1);
  assert.equal(expressions[0].expression, 'dv.view("_scripts/view/get_Whereabouts")');
});

test("formatInlineReplacement carries quote prefix to continuation lines", () => {
  const [expression] = core.findInlineDataviewExpressions(
    '>> `$=dv.view("_scripts/view/get_Whereabouts")`',
  );

  assert.equal(
    core.formatInlineReplacement("one\ntwo", expression),
    "one\n>> two",
  );
});

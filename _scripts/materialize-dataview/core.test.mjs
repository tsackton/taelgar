import assert from "node:assert/strict";
import test from "node:test";
import core from "./core.js";

test("dynamic website headers use a stable marker without changing frontmatter or body prose", () => {
  const yaml = '---\r\nheaderVersion: 2023.11.25\r\ntags: [person]\r\nname: "Synthetic"\r\n---\r\n';
  const header = '# Synthetic\r\n*(sin-THET-ik)*\r\n>[!info]+ Biographical Info\r\n> A person\r\n>> `$=dv.view("_scripts/view/get_Whereabouts")`\r\n\r\n';
  const body = '> [!image|right standard]\r\n> ![[portrait.png]]\r\n\r\n## History\r\n\r\nKeep this prose.\r\n';
  const result = core.prepareDynamicWebsiteMarkdown(yaml + header + body);
  assert.equal(result.content,yaml + '<!-- taelgar:header -->\r\n\r\n' + body);
  assert.equal(result.headerMarkersInserted,1);
  assert.equal(core.prepareDynamicWebsiteMarkdown(result.content).content,result.content);
  assert.equal(core.prepareDynamicWebsiteMarkdown('# Plain title\n\nPlain text.\n').content,'# Plain title\n\nPlain text.\n');
});

test("marking a header preserves prose immediately following the title", () => {
  const original = '---\nheaderVersion: 2023.11.25\n---\n# Title\nDo not delete this paragraph.\n';
  assert.equal(core.prepareDynamicWebsiteMarkdown(original).content,'---\nheaderVersion: 2023.11.25\n---\n<!-- taelgar:header -->\n\nDo not delete this paragraph.\n');
});

test("JS-only headings and empty ancestors are pruned without deleting campaign/date delimiters", () => {
  const original = [
    '# Page', '', 'Introductory prose.', '', '%%^Campaign:none%%', '',
    '## Parent', '', '### First', '```dataviewjs', 'document.createElement("div");', '```', '',
    '### Second', '', '%%^Date:1730%%', '~~~dataviewjs', 'dv.list([])', '~~~', '%%^End%%', '',
    '%%^End%%', '', '## Already empty', '', '## Kept', '', 'A paragraph.', '',
  ].join('\n');
  const result = core.prepareDynamicWebsiteMarkdown(original);
  assert.equal(result.dataviewJsBlocksRemoved,2);
  assert.equal(result.sectionsRemoved,3);
  assert.doesNotMatch(result.content,/Parent|### First|### Second|dataviewjs/);
  for (const delimiter of ['%%^Campaign:none%%','%%^Date:1730%%']) assert.ok(result.content.includes(delimiter));
  assert.equal((result.content.match(/%%\^End%%/g) || []).length,2);
  assert.match(result.content,/## Already empty\n/);
  assert.match(result.content,/## Kept\n\nA paragraph\./);
  assert.equal(core.prepareDynamicWebsiteMarkdown(result.content).content,result.content);
});

test("sections containing prose, DQL, other code, or comments survive JS deletion", () => {
  for (const retained of ['A paragraph.','```dataview\nLIST FROM #person\n```','```js\nconsole.log("ordinary code");\n```','%% Keep this comment. %%']) {
    const original = '# Retained\n\n' + retained + '\n\n```dataviewjs\ndv.list([]);\n```\n';
    const result = core.prepareDynamicWebsiteMarkdown(original);
    assert.equal(result.sectionsRemoved,0);
    assert.ok(result.content.includes('# Retained\n'));
    assert.ok(result.content.includes(retained));
    assert.doesNotMatch(result.content,/dv\.list/);
  }
});

test("setext sections are pruned, while fenced examples and unrelated headings remain intact", () => {
  const example = '````markdown\n## Example heading\n```dataviewjs\nKeep this example.\n```\n````\n';
  const original = '# Page\n\n' + example + '\nGenerated section\n-----------------\n\n```dataviewjs\ndv.list([]);\n```';
  const result = core.prepareDynamicWebsiteMarkdown(original);
  assert.ok(result.content.includes(example));
  assert.doesNotMatch(result.content,/Generated section|dv\.list/);
  assert.equal(result.dataviewJsBlocksRemoved,1);
  assert.equal(result.sectionsRemoved,1);
});

test("unclosed JS fences remain available for strict error reporting", () => {
  const source = '## Unclosed\n\n```dataviewjs\nPossibly more prose.\n';
  const result = core.prepareDynamicWebsiteMarkdown(source);
  assert.equal(result.content,source);
  assert.equal(result.dataviewJsBlocksRemoved,0);
  assert.equal(result.sectionsRemoved,0);
});

test("a section containing only a quoted JS fence is also removed", () => {
  const source = '# Page\n\nRetained introduction.\n\n## Generated\n\n> ```dataviewjs\n> dv.list([]);\n> ```\n';
  const result = core.prepareDynamicWebsiteMarkdown(source);
  assert.equal(result.sectionsRemoved,1);
  assert.doesNotMatch(result.content,/## Generated|dv\.list/);
  assert.match(result.content,/# Page\n\nRetained introduction\./);
});

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

test("detectUnsupportedDataviewQuery flags global file-list chronology scans", () => {
  const query =
    'LIST WITHOUT ID events.text flatten file.lists as events where contains(events.text, this.file.name) sort events.DR';

  assert.deepEqual(core.detectUnsupportedDataviewQuery(query), [
    "scans all file lists for the current page name",
  ]);
  assert.deepEqual(core.detectUnsupportedDataviewQuery("LIST FROM #person"), []);
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

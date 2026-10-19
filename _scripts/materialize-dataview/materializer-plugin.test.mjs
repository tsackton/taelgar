import assert from "node:assert/strict";
import fs from "node:fs/promises";
import { createRequire } from "node:module";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import core from "./core.js";

const require = createRequire(import.meta.url);
const pluginPath = new URL("../../.obsidian/plugins/taelgar-dataview-materializer/main.js", import.meta.url);
const source = await fs.readFile(pluginPath, "utf8");

function createPlugin(vaultRoot) {
  const sandbox = {
    module: { exports: {} },
    require: (name) => name === "obsidian" ? { Plugin: class {}, Notice: class {} } : require(name),
    window: { setTimeout, clearTimeout },
  };
  vm.runInNewContext(source, sandbox);
  const plugin = new sandbox.module.exports();
  plugin.getVaultBasePath = () => vaultRoot;
  return plugin;
}

test("dynamic website output marks headers, deletes JS-only sections, and materializes DQL without running JavaScript", async () => {
  const plugin = createPlugin(os.tmpdir());
  const config = plugin.normalizeConfig({ dynamicWebsite: true, headerType: "website" });
  const file = { path: "Example.md", name: "Example.md", basename: "Example" };
  const original = [
    "---", "headerVersion: 2023.11.25", "tags: [person]", "---", "# Example",
    "*(example)*", ">[!info]+ Biographical Info", '> `$=dv.view("_scripts/view/get_PageDatedValue")`', "",
    "## Removed section", "```dataviewjs", 'document.createElement("div");', "```", "",
    "## Kept section", "", "Retained prose — including Unicode.", "",
    "~~~dataviewjs", 'dv.paragraph("Delete this too.");', "~~~", "",
    "## Query results", "```dataview", "LIST FROM #person", "```",
    "## Footer", "", "More retained prose.", "",
  ].join("\n");
  const calls = [];
  const runtime = { api: { async tryQueryMarkdown(body, sourcePath) {
    calls.push({ body, sourcePath });
    return "- [[Synthetic Person]]\n";
  } } };
  plugin.regenerateHeader = () => assert.fail("Headers must be marked instead of regenerated");
  plugin.renderDataviewJs = () => assert.fail("DataviewJS must not run");
  plugin.renderKnownInlineExpression = () => assert.fail("Inline JS must not run");

  const result = await plugin.materializeMarkdown(original, file, runtime, core, config);

  assert.equal(config.headerType, "none");
  assert.match(result.content,/^---\nheaderVersion: 2023\.11\.25\ntags: \[person\]\n---\n<!-- taelgar:header -->/);
  assert.doesNotMatch(result.content,/# Example|Biographical Info|\$=|dataviewjs|document\.|dv\.paragraph|Removed section/);
  assert.match(result.content,/## Kept section\n\nRetained prose — including Unicode\./);
  assert.match(result.content,/## Query results\n- \[\[Synthetic Person\]\]\n## Footer/);
  assert.match(result.content,/More retained prose\./);
  assert.deepEqual(calls,[{ body: "LIST FROM #person\n", sourcePath: file.path }]);
  assert.equal(result.report.counts.dataviewBlocks,1);
  assert.equal(result.report.counts.headerMarkersInserted,1);
  assert.equal(result.report.counts.dataviewJsBlocksRemoved,2);
  assert.equal(result.report.counts.sectionsRemoved,1);
  for (const key of ["dataviewJsBlocks","inlineExpressions","headersRegenerated","unsupported","errors"]) assert.equal(result.report.counts[key],0,key);
  assert.equal(result.report.remaining.dataviewFences,0);
  assert.equal(result.report.remaining.dataviewJsFences,0);
  assert.equal(result.report.remaining.inlineExpressions,0);
});

test("default mode still materializes DQL, DataviewJS, headers, and supported inline expressions", async () => {
  const plugin = createPlugin(os.tmpdir());
  const config = plugin.normalizeConfig({ headerType: "website" });
  const original = [
    "# Old header", "", "```dataview", "LIST FROM #person", "```", "",
    "```dataviewjs", 'dv.paragraph("JS");', "```", "",
    '`$=dv.view("_scripts/view/get_PageDatedValue")`', "",
  ].join("\n");
  plugin.regenerateHeader = (text) => text.replace("# Old header", "# New header");
  plugin.renderDataviewJs = async () => "JS output";
  plugin.renderKnownInlineExpression = () => "Inline output";
  const runtime = { api: { tryQueryMarkdown: async () => "DQL output" } };

  const result = await plugin.materializeMarkdown(original, { path: "Example.md" }, runtime, core, config);

  assert.equal(config.dynamicWebsite, false);
  assert.equal(result.content, "# New header\n\nDQL output\nJS output\nInline output\n");
  for (const key of ["dataviewBlocks", "dataviewJsBlocks", "inlineExpressions", "headersRegenerated"]) {
    assert.equal(result.report.counts[key], 1, key);
  }
  assert.equal(result.report.counts.errors, 0);
  assert.equal(result.report.counts.unsupported, 0);
});

test("dynamic-website runtime does not require CustomJS", async () => {
  const plugin = createPlugin(os.tmpdir());
  assert.equal(plugin.supportsDynamicWebsite, true);
  const api = { tryQueryMarkdown: async () => "DQL output" };
  plugin.app = { plugins: { plugins: { dataview: { api, index: { initialized: true } } } } };
  plugin.waitForLayout = async () => {};
  plugin.waitForCustomJs = () => assert.fail("CustomJS must not be awaited");
  plugin.installCompatibilityAliases = () => assert.fail("CustomJS must not be patched");
  plugin.installMaterializationCaches = () => assert.fail("CustomJS must not be patched");

  const runtime = await plugin.prepareRuntime(plugin.normalizeConfig({ dynamicWebsite: true }));

  assert.equal(runtime.api, api);
  runtime.restore();
});

function createAuditPlugin(original, query = async () => "DQL output") {
  const plugin = createPlugin(os.tmpdir());
  let restored = 0;
  plugin.app = { vault: {
    getMarkdownFiles: () => [{ path: "Example.md" }],
    cachedRead: async () => original,
  } };
  plugin.loadCore = () => core;
  plugin.prepareRuntime = async () => ({ api: { tryQueryMarkdown: query }, restore() { restored += 1; } });
  plugin.writeProgress = async () => {};
  plugin.copyVaultToOutput = () => assert.fail("Audit/check must not write vault output");
  return { plugin, restored: () => restored };
}

test("dynamic CLI writes stage Markdown and releases Obsidian without copying the vault", async t => {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), "taelgar-handoff-test-"));
  t.after(async () => {
    const relative = path.relative(os.tmpdir(), path.resolve(root));
    assert.ok(!path.isAbsolute(relative) && relative.startsWith("taelgar-handoff-test-") && !relative.includes(path.sep));
    await fs.rm(root, { recursive: true, force: true });
  });
  const vaultPath = path.join(root, "vault"), outputPath = path.join(root, "output");
  const stagedMarkdownPath = path.join(outputPath, ".stage.json");
  await fs.mkdir(vaultPath);
  const fixture = createAuditPlugin('---\nheaderVersion: 2023.11.25\n---\n# Example\n\n```dataview\nLIST FROM #person\n```\n');
  fixture.plugin.getVaultBasePath = () => vaultPath;
  assert.equal(fixture.plugin.supportsExternalCopy, true);
  const report = await fixture.plugin.runMaterialization({
    mode: "write", strict: true, dynamicWebsite: true, externalCopy: true,
    outputPath, stagedMarkdownPath, requestId: "handoff",
  });
  assert.equal(report.phase, "awaiting-copy");
  assert.equal(report.outputComplete, false);
  assert.equal(report.deferredCopy, stagedMarkdownPath);
  const bundle = JSON.parse(await fs.readFile(stagedMarkdownPath, "utf8"));
  assert.equal(bundle.requestId, "handoff");
  assert.equal(bundle.dynamicWebsite, true);
  assert.equal(report.publicationPolicy, "context-v1");
  assert.match(bundle.files[0].content, /<!-- taelgar:header -->/);
  assert.match(bundle.files[0].content, /DQL output/);
  assert.deepEqual(await fs.readdir(outputPath), [".stage.json"]);
  assert.equal(fixture.restored(), 1);
});

test("strict dynamic website check accepts deleted unsupported JS and retained inline expressions", async () => {
  const original = [
    "```dataview", "LIST FROM #person", "```", "",
    "`$=dv.current().unknownValue`", "", "```dataviewjs", 'document.createElement("div");', "```",
  ].join("\n");
  const fixture = createAuditPlugin(original);
  const report = await fixture.plugin.runMaterialization({ mode: "check", strict: true, dynamicWebsite: true });

  assert.equal(report.status, "ok");
  assert.equal(report.exitCode, 0);
  assert.equal(report.dynamicWebsite, true);
  assert.equal(report.counts.dataviewBlocks, 1);
  assert.equal(report.counts.errors, 0);
  assert.equal(report.counts.unsupported, 0);
  assert.equal(report.counts.remainingDataviewBlocks, 0);
  assert.equal(report.counts.remainingDataviewJsBlocks, 0);
  assert.equal(report.counts.dataviewJsBlocksRemoved, 1);
  assert.equal(report.counts.remainingInlineExpressions, 1);

  const defaultReport = await fixture.plugin.runMaterialization({ mode: "check", strict: true });
  assert.equal(defaultReport.status, "failed");
  assert.equal(defaultReport.dynamicWebsite, false);
  assert.equal(defaultReport.counts.errors, 0);
  assert.equal(defaultReport.counts.unsupported, 2);
  assert.equal(fixture.restored(), 2);
});

test("strict dynamic-website check still fails on DQL errors", async () => {
  const original = "```dataview\nLIST FROM #person\n```\n";
  const fixture = createAuditPlugin(original, async () => { throw new Error("Synthetic query failure"); });

  const report = await fixture.plugin.runMaterialization({ mode: "check", strict: true, dynamicWebsite: true });

  assert.equal(report.status, "failed");
  assert.equal(report.exitCode, 1);
  assert.equal(report.counts.errors, 1);
  assert.equal(report.counts.remainingDataviewBlocks, 1);
  assert.match(report.files[0].issues[0].message, /Synthetic query failure/);
  assert.equal(fixture.restored(), 1);
});

test("dynamic website mode reports unclosed JS fences instead of discarding possibly unrelated text", async () => {
  const fixture = createAuditPlugin('## Unclosed\n\n```dataviewjs\nPossibly more prose.\n');
  const report = await fixture.plugin.runMaterialization({ mode: "check", strict: true, dynamicWebsite: true });
  assert.equal(report.status,"failed");
  assert.equal(report.counts.errors,1);
  assert.equal(report.counts.dataviewJsBlocksRemoved,0);
  assert.match(report.files[0].issues[0].message,/Unclosed fenced code block/);
});

test("materializer excludes private asset directories without excluding neighboring names", () => {
  const plugin = createPlugin(os.tmpdir());
  const config = plugin.normalizeConfig({});
  for (const excluded of [
    "assets/dm",
    "assets/dm/scene.png",
    "assets/dm/maps/notes.md",
    "assets/worldbuilding",
    "assets/worldbuilding/chats/image.png",
    "Worldbuilding/Notes.md",
    "_DM_/Notes.md",
    "_dm_notes/Notes.md",
  ]) {
    assert.equal(plugin.shouldProcessVaultPath(excluded, config), false, excluded);
  }
  for (const included of [
    "assets/portrait.png",
    "assets/campaign/scene.png",
    "assets/_incoming/new.png",
    "assets/dm-map.png",
    "assets/dm-reference/portrait.png",
    "assets/worldbuilding-map.png",
    "assets/worldbuilding-reference/portrait.png",
  ]) {
    assert.equal(plugin.shouldProcessVaultPath(included, config), true, included);
  }
});

test("recursive materializer copy omits private assets and retains public assets", async (t) => {
  const temporaryRoot = await fs.mkdtemp(path.join(os.tmpdir(), "taelgar-asset-copy-test-"));
  t.after(() => fs.rm(temporaryRoot, { recursive: true, force: true }));
  const vaultRoot = path.join(temporaryRoot, "vault");
  const outputRoot = path.join(temporaryRoot, "output");
  const excluded = ["assets/dm/maps/secret.png", "assets/worldbuilding/chats/idea.png"];
  const included = ["assets/portrait.png", "assets/campaign/scene.png", "assets/_incoming/new.png"];
  for (const relativePath of [...excluded, ...included]) {
    const filePath = path.join(vaultRoot, relativePath);
    await fs.mkdir(path.dirname(filePath), { recursive: true });
    await fs.writeFile(filePath, relativePath);
  }
  const plugin = createPlugin(vaultRoot);
  const config = plugin.normalizeConfig({ outputPath: outputRoot });
  await plugin.copyVaultToOutput(outputRoot, [], config);

  for (const directory of ["assets/dm", "assets/worldbuilding"]) {
    await assert.rejects(fs.access(path.join(outputRoot, directory)), { code: "ENOENT" });
  }
  for (const relativePath of included) {
    assert.equal(await fs.readFile(path.join(outputRoot, relativePath), "utf8"), relativePath);
  }
  for (const relativePath of excluded) {
    assert.equal(await fs.readFile(path.join(vaultRoot, relativePath), "utf8"), relativePath);
  }
});

test("dynamic publication materializes every eligible note regardless of publish metadata", async () => {
  const fixture = createAuditPlugin('---\nexcludePublish: all\ntags: [excalidraw]\nborn: 1800-01-01\n---\nRetained body.\n');
  const included = ["Hidden.md", "_loose.md", "assets/dm-reference/Notes.md", "Worldbuilding-reference/Notes.md"];
  const omitted = ["assets/dm/Notes.md", "asset/dm/Notes.md", "ASSETS/DM/nested/Notes.md", "Worldbuilding/Notes.md", "nested/worldbuilding/Notes.md", "nested/_dm/Notes.md", ".obsidian/Notes.md", "AGENTS.md"];
  fixture.plugin.app.vault.getMarkdownFiles = () => [...included, ...omitted].map(path => ({path}));
  const report = await fixture.plugin.runMaterialization({mode: "audit", dynamicWebsite: true});
  assert.equal(report.status, "ok");
  assert.equal(report.counts.filesScanned, included.length);
  assert.equal(report.counts.filesSkipped, omitted.length);
  assert.equal(report.publicationPolicy, "context-v1");
});

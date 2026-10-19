import assert from "node:assert/strict";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import { execFile } from "node:child_process";
import { promisify } from "node:util";
import { fileURLToPath } from "node:url";
import { copyOutputBundle, finishDeferredCopy } from "./copy-output.mjs";

async function fixture(t) {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), "taelgar-output-test-"));
  t.after(async () => {
    const relative = path.relative(os.tmpdir(), path.resolve(root));
    assert.ok(!path.isAbsolute(relative) && relative.startsWith("taelgar-output-test-") && !relative.includes(path.sep));
    await fs.rm(root, { recursive: true, force: true });
  });
  const vaultPath = path.join(root, "vault"), outputPath = path.join(root, "output");
  await fs.mkdir(vaultPath);
  return { root, vaultPath, outputPath };
}

test("Node copy writes prepared notes and streams public assets while retaining exclusion boundaries", async t => {
  const { vaultPath, outputPath } = await fixture(t);
  const binary = Buffer.alloc(2 * 1024 * 1024 + 10, 17);
  const included = ["Note.md", "assets/scene.png", "assets/_incoming/new.png", "assets/dm-map.png", "assets/worldbuilding-reference/scene.png"];
  const omitted = [".obsidian/config.json", "_dm_notes/Secret.md", "Worldbuilding/Notes.md", "assets/dm/private.png", "assets/worldbuilding/private.png"];
  for (const relative of [...included, ...omitted]) {
    const target = path.join(vaultPath, relative);
    await fs.mkdir(path.dirname(target), { recursive: true });
    await fs.writeFile(target, relative === "assets/scene.png" ? binary : "Original " + relative);
  }
  const events = [];
  const copied = await copyOutputBundle({ vaultPath, outputPath, files: [{ path: "Note.md", content: "<!-- taelgar:header -->\nPrepared body.\n" }] }, async event => { events.push(event); });
  assert.match(await fs.readFile(path.join(outputPath, "Note.md"), "utf8"), /Prepared body/);
  assert.equal(await fs.readFile(path.join(vaultPath, "Note.md"), "utf8"), "Original Note.md");
  assert.deepEqual(await fs.readFile(path.join(outputPath, "assets/scene.png")), binary);
  for (const relative of included) await fs.access(path.join(outputPath, relative));
  for (const relative of omitted) await assert.rejects(fs.access(path.join(outputPath, relative)), { code: "ENOENT" });
  assert.equal(copied.filesCopied, included.length);
  assert.ok(copied.bytesCopied > binary.length);
  assert.ok(events.some(event => event.currentFile === "assets/scene.png"));
  assert.equal(events.at(-1).filesCopied, included.length);
});

test("Node copy rejects the source vault and its descendants as output", async t => {
  const { vaultPath } = await fixture(t);
  for (const outputPath of [vaultPath, path.join(vaultPath, "nested-output")]) {
    await assert.rejects(copyOutputBundle({ vaultPath, outputPath, files: [] }), /outside the source vault/);
  }
  await assert.rejects(fs.access(path.join(vaultPath, "nested-output")), { code: "ENOENT" });
});

async function stagedFixture(t) {
  const dirs = await fixture(t);
  await fs.mkdir(dirs.outputPath);
  await fs.writeFile(path.join(dirs.vaultPath, "Note.md"), "Original body.");
  const bundlePath = path.join(dirs.outputPath, ".stage.json");
  const reportPath = path.join(dirs.outputPath, ".report.json");
  const bundle = { schemaVersion: 1, requestId: "fixture", ...dirs, files: [{ path: "Note.md", content: "Prepared body." }] };
  const report = { id: "fixture", status: "ok", exitCode: 0, mode: "write", strict: false,
    vaultPath: dirs.vaultPath, outputPath: dirs.outputPath, deferredCopy: bundlePath, outputComplete: false,
    counts: { errors: 0, unsupported: 0 }, performance: { totalMs: 1, copyMs: 0 } };
  await fs.writeFile(bundlePath, JSON.stringify(bundle));
  return { ...dirs, bundlePath, reportPath, bundle, report };
}

test("successful handoff finalizes the report only after Node has copied the output", async t => {
  const f = await stagedFixture(t);
  const result = await finishDeferredCopy(f.report, f.reportPath);
  assert.equal(result.status, "ok");
  assert.equal(result.phase, "complete");
  assert.equal(result.outputComplete, true);
  assert.equal(await fs.readFile(path.join(f.outputPath, "Note.md"), "utf8"), "Prepared body.");
  assert.equal(JSON.parse(await fs.readFile(f.reportPath, "utf8")).outputComplete, true);
  await assert.rejects(fs.access(f.bundlePath), { code: "ENOENT" });
});

test("a stale handoff cannot copy a different request's notes", async t => {
  const f = await stagedFixture(t);
  await fs.writeFile(f.bundlePath, JSON.stringify({ ...f.bundle, requestId: "other-request" }));
  const result = await finishDeferredCopy(f.report, f.reportPath);
  assert.equal(result.status, "failed");
  assert.equal(result.outputComplete, false);
  assert.match(result.error.message, /does not match/);
  await assert.rejects(fs.access(path.join(f.outputPath, "Note.md")), { code: "ENOENT" });
  await fs.access(f.bundlePath);
});

test("copy errors persist a failure report and retain the prepared Markdown", async t => {
  const f = await stagedFixture(t);
  const result = await finishDeferredCopy(f.report, f.reportPath, async () => { throw new Error("Synthetic copy failure"); });
  assert.equal(result.exitCode, 1);
  assert.equal(result.phase, "copy-failed");
  assert.match(result.error.message, /Synthetic copy failure/);
  assert.equal(JSON.parse(await fs.readFile(f.reportPath, "utf8")).status, "failed");
  await fs.access(f.bundlePath);
});

test("the actual CLI completes a synthetic Obsidian handoff, copies output, and exits", async t => {
  const { vaultPath, outputPath } = await fixture(t);
  const corePath = path.join(vaultPath, "_scripts/materialize-dataview/core.js");
  await fs.mkdir(path.dirname(corePath), { recursive: true });
  await fs.copyFile(new URL("./core.js", import.meta.url), corePath);
  const source = '---\nheaderVersion: 2023.11.25\n---\n# Fixture\n\n```dataview\nLIST FROM #person\n```\n';
  await fs.writeFile(path.join(vaultPath, "Fixture.md"), source);
  await fs.mkdir(path.join(vaultPath, "assets/dm"), {recursive: true});
  await fs.writeFile(path.join(vaultPath, "assets/dm/map.png"), "map");
  await fs.writeFile(path.join(vaultPath, "assets/image.png"), Buffer.alloc(1024, 9));
  const pluginPath = fileURLToPath(new URL("../../.obsidian/plugins/taelgar-dataview-materializer/main.js", import.meta.url));
  // Node receives "eval" as a script filename in this fixture. The real Obsidian
  // executable is never launched, and no working vault data is used.
  await fs.writeFile(path.join(vaultPath, "eval"), `
    const fs = require('node:fs'), vm = require('node:vm'), path = require('node:path');
    const sandbox = {module: {exports: {}}, window: {setTimeout, clearTimeout},
      require: name => name === 'obsidian' ? {Plugin: class {}, Notice: class {}} : require(name)};
    vm.runInNewContext(fs.readFileSync(${JSON.stringify(pluginPath)}, 'utf8'), sandbox);
    const plugin = new sandbox.module.exports();
    plugin.getVaultBasePath = () => process.cwd();
    plugin.app = {workspace: {layoutReady: true}, vault: {
      getMarkdownFiles: () => [{path: 'Fixture.md', name: 'Fixture.md', basename: 'Fixture'}],
      cachedRead: file => fs.promises.readFile(path.join(process.cwd(), file.path), 'utf8')},
      plugins: {plugins: {dataview: {index: {initialized: true}, api: {tryQueryMarkdown: async () => '- Rendered fixture result'}}}}};
    const code = process.argv[2].slice('code='.length);
    Promise.resolve(vm.runInNewContext(code, {app: {plugins: {plugins: {'taelgar-dataview-materializer': plugin}}}}))
      .catch(error => {console.error(error); process.exitCode = 1;});
  `);
  const cliPath = fileURLToPath(new URL("./materialize-dataview.mjs", import.meta.url));
  const result = await promisify(execFile)(process.execPath, [cliPath, "--vault", vaultPath,
    "--out", outputPath, "--dynamic-website", "--obsidian-command", process.execPath, "--no-progress"],
    { cwd: vaultPath, timeout: 15000, windowsHide: true });
  assert.match(result.stdout, /Materialization complete/);
  assert.match(await fs.readFile(path.join(outputPath, "Fixture.md"), "utf8"), /<!-- taelgar:header -->[\s\S]*Rendered fixture result/);
  assert.deepEqual(await fs.readFile(path.join(outputPath, "assets/image.png")), Buffer.alloc(1024, 9));
  assert.equal(await fs.readFile(path.join(vaultPath, "Fixture.md"), "utf8"), source);
  const report = JSON.parse(await fs.readFile(path.join(outputPath, ".dataview-materialization-report.json"), "utf8"));
  assert.equal(report.status, "ok");
  assert.equal(report.outputComplete, true);
  assert.equal(report.phase, "complete");
  assert.equal(report.publicationPolicy, "context-v1");
  await assert.rejects(fs.access(path.join(outputPath, "assets/dm/map.png")), {code: "ENOENT"});
  await assert.rejects(fs.access(report.deferredCopy), { code: "ENOENT" });
});

test("dynamic copy retains flagged notes but omits DM assets, internal and worldbuilding folders", async t => {
  const {vaultPath, outputPath} = await fixture(t);
  const included = ["Hidden.md", "_loose.md", "assets/_portrait.png", "assets/dm-map.png", "assets/dm-reference/map.png", "worldbuilding-reference/Note.md"];
  const omitted = ["assets/dm/map.png", "assets/dm/nested/secret.png", "asset/dm/map.png", "_dm/Note.md", "nested/_dm/Note.md", "Worldbuilding/Note.md", "nested/worldbuilding/Note.md", "assets/worldbuilding/map.png", ".obsidian/config.json", "AGENTS.md"];
  for (const relative of [...included, ...omitted]) {
    const file = path.join(vaultPath, relative);
    await fs.mkdir(path.dirname(file), {recursive: true});
    await fs.writeFile(file, "original");
  }
  const content = '---\nexcludePublish: all\n---\n<!-- taelgar:header -->\nRetained biography.\n';
  const copied = await copyOutputBundle({vaultPath, outputPath, dynamicWebsite: true, files: [{path: "Hidden.md", content}]});
  assert.equal(copied.filesCopied, included.length);
  assert.equal(await fs.readFile(path.join(outputPath, "Hidden.md"), "utf8"), content);
  for (const relative of included) await fs.access(path.join(outputPath, relative));
  for (const relative of omitted) await assert.rejects(fs.access(path.join(outputPath, relative)), {code: "ENOENT"});
});

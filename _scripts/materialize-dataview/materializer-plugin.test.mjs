import assert from "node:assert/strict";
import fs from "node:fs/promises";
import { createRequire } from "node:module";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";

const require = createRequire(import.meta.url);
const pluginPath = new URL("../../.obsidian/plugins/taelgar-dataview-materializer/main.js", import.meta.url);
const source = await fs.readFile(pluginPath, "utf8");

function createPlugin(vaultRoot) {
  const sandbox = {
    module: { exports: {} },
    require: (name) => name === "obsidian" ? { Plugin: class {}, Notice: class {} } : require(name),
  };
  vm.runInNewContext(source, sandbox);
  const plugin = new sandbox.module.exports();
  plugin.getVaultBasePath = () => vaultRoot;
  return plugin;
}

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

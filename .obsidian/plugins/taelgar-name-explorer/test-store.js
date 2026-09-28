"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs/promises");
const os = require("node:os");
const path = require("node:path");
const Module = require("node:module");
const core = require("./core");

const STORE = "_Plugins/Name Explorer/Name Decisions.jsonl";
const SAVED = '{"type":"rule","id":"saved-rule","language":"Elvish"}\n';

class TFile {
  constructor(filePath) { this.path = filePath; }
}

async function fixture(run) {
  const root = await fs.mkdtemp(path.join(os.tmpdir(), "name-explorer-store-"));
  const notices = [];
  const indexed = new Map();
  const writes = [];
  const processQueues = new Map();
  const adapter = {
    async stat(filePath) {
      try {
        const stat = await fs.stat(path.join(root, filePath));
        return { type: stat.isDirectory() ? "folder" : "file" };
      } catch (error) {
        if (error.code === "ENOENT") return null;
        throw error;
      }
    },
    read: (filePath) => fs.readFile(path.join(root, filePath), "utf8"),
    process(filePath, callback) {
      const next = (processQueues.get(filePath) || Promise.resolve()).then(async () => {
        const text = callback(await adapter.read(filePath));
        await fs.writeFile(path.join(root, filePath), text);
        return text;
      });
      processQueues.set(filePath, next.catch(() => {}));
      return next;
    },
  };
  const vault = {
    adapter,
    on() {},
    getAbstractFileByPath: (filePath) => indexed.get(filePath) || null,
    async createFolder(filePath) {
      writes.push(filePath);
      await fs.mkdir(path.join(root, filePath));
      indexed.set(filePath, { path: filePath });
    },
    async create(filePath, text) {
      writes.push(filePath);
      await fs.writeFile(path.join(root, filePath), text, { flag: "wx" });
      const file = new TFile(filePath);
      indexed.set(filePath, file);
      return file;
    },
    read: (file) => adapter.read(file.path),
    process: (file, callback) => adapter.process(file.path, callback),
  };
  class Plugin {
    async loadData() { return {}; }
    registerView() {}
    addRibbonIcon() {}
    addCommand() {}
    addSettingTab() {}
    registerEvent() {}
    register() {}
  }
  const obsidian = {
    Plugin,
    TFile,
    ItemView: class {},
    Modal: class {},
    PluginSettingTab: class {},
    Notice: class { constructor(message) { notices.push(message); } },
  };
  const filename = path.join(__dirname, "main.js");
  const pluginModule = new Module(filename, module);
  pluginModule.filename = filename;
  pluginModule.require = (name) => name === "obsidian" ? obsidian : require(name);
  pluginModule._compile(await fs.readFile(filename, "utf8"), filename);
  const plugin = new pluginModule.exports();
  plugin.app = { vault, metadataCache: { on() {} } };
  plugin.loadCore = () => core;
  const seed = async (filePath, text) => {
    await fs.mkdir(path.dirname(path.join(root, filePath)), { recursive: true });
    await fs.writeFile(path.join(root, filePath), text);
  };
  try {
    await run({ plugin, vault, adapter, root, notices, writes, indexed, seed });
  } finally {
    await fs.rm(root, { recursive: true, force: true });
  }
}

async function run() {
  // Startup can run before Obsidian has indexed existing files and folders.
  await fixture(async ({ plugin, adapter, notices, writes, seed }) => {
    await seed(STORE, SAVED);
    await plugin.onload();
    assert.deepEqual(notices, [], "Startup must reuse the unindexed store");
    assert.equal(await adapter.read(STORE), SAVED);
    assert.deepEqual(writes, [], "Existing store and folders must not be recreated");
    assert.equal((await plugin.loadDecisionRecords())[0].id, "saved-rule");
    await Promise.all([
      plugin.mutateDecisionStore((records) => [...records, { type: "rule", id: "one" }]),
      plugin.mutateDecisionStore((records) => [...records, { type: "rule", id: "two" }]),
    ]);
    assert.deepEqual((await plugin.loadDecisionRecords()).map((r) => r.id).sort(),
      ["one", "saved-rule", "two"]);
  });

  // First use and simultaneous requests create exactly one default store.
  await fixture(async ({ plugin, notices, writes, adapter }) => {
    await plugin.onload();
    assert.deepEqual(notices, []);
    assert.equal((await plugin.loadDecisionRecords())[0].id, "halfling-person-names-common");
    plugin.settings.decisionStorePath = "New/Nested/Decisions.jsonl";
    await Promise.all(Array.from({ length: 8 }, () => plugin.loadDecisionRecords()));
    assert.equal(writes.filter((p) => p === plugin.settings.decisionStorePath).length, 1);
    assert.equal(core.parseDecisionStore(await adapter.read(plugin.settings.decisionStorePath)).length, 1);
  });

  await fixture(async ({ plugin, adapter, seed }) => {
    await seed(STORE, SAVED);
    await plugin.onload();
    await seed(STORE, "invalid JSON\n");
    await assert.rejects(plugin.ensureDecisionStore(), /Invalid JSON/);
    assert.equal(await adapter.read(STORE), "invalid JSON\n");
    await seed(STORE, SAVED);
    assert.equal((await plugin.loadDecisionRecords())[0].id, "saved-rule", "Failed initialization must allow retry");
  });

  await fixture(async ({ plugin, root, seed }) => {
    await seed(STORE, SAVED);
    await plugin.onload();
    await fs.mkdir(path.join(root, "Folder.jsonl"));
    plugin.settings.decisionStorePath = "Folder.jsonl";
    await assert.rejects(plugin.ensureDecisionStore(), /Decision store path is not a file/);
    await seed("Not a folder", "keep me");
    plugin.settings.decisionStorePath = "Not a folder/Decisions.jsonl";
    await assert.rejects(plugin.ensureDecisionStore(), /not a (folder|directory)/);
  });

  // Another writer can win after the existence check; keep its contents.
  await fixture(async ({ plugin, vault, adapter, seed }) => {
    await seed(STORE, SAVED);
    await plugin.onload();
    plugin.settings.decisionStorePath = "_Plugins/Name Explorer/Raced.jsonl";
    vault.create = async (filePath) => {
      await seed(filePath, SAVED);
      throw new Error("File already exists.");
    };
    assert.equal((await plugin.loadDecisionRecords())[0].id, "saved-rule");
    assert.equal(await adapter.read(plugin.settings.decisionStorePath), SAVED);
    plugin.settings.decisionStorePath = "_Plugins/Name Explorer/Denied.jsonl";
    vault.create = async () => { throw new Error("Permission denied"); };
    await assert.rejects(plugin.ensureDecisionStore(), /Permission denied/);
  });

  console.log("Name Explorer store regression tests passed.");
}

run().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});

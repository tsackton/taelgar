"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const ROOT = path.resolve(__dirname, "..");

function loadClass(relativePath, context) {
  const source = fs.readFileSync(path.join(ROOT, relativePath), "utf8");
  return vm.runInNewContext(`(${source})`, context, { filename: relativePath });
}

async function run() {
  // All metadata is test-owned; the real campaign roster may change freely.
  const legacyMetadata = {
    campaigns: [{ code: "voy", partyPage: "Wrong Party" }],
    linkmap: [{ from: "voy", to: "Wrong Party" }],
  };
  const registry = {voy: "Index/Voyage.md", other: "Index/Other.md"};
  const fields = new Map([
    ["Index/Voyage.md", {name: "Test Voyage", partyPage: "People/Fixture Fellowship.md",
      campaignDirectory: "Campaigns/Test Voyage", notePattern: "Records/Sessions/Session {session}.md"}],
    ["Index/Other.md", {name: "Other Campaign"}],
  ]);
  const files = new Map([
    [".obsidian/metadata.json", JSON.stringify(legacyMetadata)],
    ["_sessions/campaign-registry.json", JSON.stringify(registry)],
  ]);
  const context = {
    app: {
      metadataCache: { getFileCache: file => ({frontmatter: fields.get(file.path)}) },
      vault: {
        getAbstractFileByPath: path => fields.has(path) ? {path} : null,
        configDir: ".obsidian",
        adapter: {
          async read(filePath) {
            if (!files.has(filePath)) throw new Error(`Unexpected read: ${filePath}`);
            return files.get(filePath);
          },
        },
      },
    },
    customJS: { state: {} },
  };

  const Init = loadClass("_scripts/customJS/loadMetadata.js", context);
  await new Init().invoke();

  const NameManager = loadClass("_scripts/customJS/nameManager.js", context);
  const nameManager = new NameManager();
  context.customJS.NameManager = nameManager;

  assert.equal(nameManager.getCampaignPartyPage("voy"), "People/Fixture Fellowship");
  assert.equal(nameManager.getCampaignPartyPage("Test Voyage"), "People/Fixture Fellowship");
  assert.equal(nameManager.getCampaignConfig("voy").code, "voy");
  assert.equal(
    nameManager.getCampaignSessionNoteFolder("voy"),
    "Campaigns/Test Voyage/Records/Sessions",
  );
  assert.equal(context.customJS.state.coreMeta.campaigns[0].name, "Test Voyage");

  assert.equal(nameManager.getCampaignConfig("  TEST VOYAGE  ").code, "voy");
  assert.equal(nameManager.getCampaignConfig("missing"), undefined);
  assert.equal(nameManager.getCampaignSessionNoteFolder("other"), "");

  let resolvedPerson;
  context.customJS.NameManager = {
    getDisplayData() {
      return { wParty: "<person>" };
    },
    getPageType() {
      return "person";
    },
    getCampaignPartyPage(code) {
      return nameManager.getCampaignPartyPage(code);
    },
    getNameObject(target) {
      resolvedPerson = target;
      return { target };
    },
  };
  context.customJS.DateManager = {
    normalizeDate() {
      return { year: 1748 };
    },
  };
  context.customJS.WhereaboutsManager = {
    getWhereabouts() {
      return { current: { location: "Somewhere" } };
    },
  };
  context.customJS.TokenParser = {
    formatDisplayString() {
      return "Met the party";
    },
  };

  const EventManager = loadClass("_scripts/customJS/eventManager.js", context);
  const meetings = new EventManager().getPartyMeeting({
    frontmatter: {
      campaignInfo: [{ campaign: "voy", date: "1748-01-01", type: "met" }],
    },
  });

  assert.equal(resolvedPerson, "People/Fixture Fellowship");
  assert.equal(meetings[0].campaign, "voy");
  // Reinitializing follows edits/deletions in the supplied registry.
  delete registry.voy;
  fields.get("Index/Other.md").partyPage = "Replacement Party.md";
  files.set("_sessions/campaign-registry.json", JSON.stringify(registry));
  await new Init().invoke();
  assert.equal(nameManager.getCampaignConfig("Test Voyage"), undefined);
  assert.equal(nameManager.getCampaignPartyPage("other"), "Replacement Party");
  assert.equal(context.customJS.state.coreMeta.campaigns.length, 1);
  files.delete("_sessions/campaign-registry.json");
  await assert.rejects(new Init().invoke(), /Unexpected read/);

  console.log("Header campaign registry tests passed.");
}

run().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});

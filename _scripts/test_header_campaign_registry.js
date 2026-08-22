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
  const legacyMetadata = JSON.parse(
    fs.readFileSync(path.join(ROOT, ".obsidian/metadata.json"), "utf8"),
  );
  legacyMetadata.campaigns = [{ code: "dufr", partyPage: "Wrong Party" }];
  legacyMetadata.linkmap = [{ from: "dufr", to: "Wrong Party" }];

  const files = new Map([
    [".obsidian/metadata.json", JSON.stringify(legacyMetadata)],
    [
      "_scripts/session_note_campaigns.json",
      fs.readFileSync(path.join(ROOT, "_scripts/session_note_campaigns.json"), "utf8"),
    ],
  ]);
  const context = {
    app: {
      vault: {
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

  assert.equal(nameManager.getCampaignPartyPage("dufr"), "Dunmar Fellowship");
  assert.equal(nameManager.getCampaignPartyPage("Dunmari Frontier"), "Dunmar Fellowship");
  assert.equal(nameManager.getCampaignConfig("dunmar-frontier").code, "dufr");
  assert.equal(
    nameManager.getCampaignSessionNoteFolder("dufr"),
    "Campaigns/Dunmari Frontier Campaign/Session Notes",
  );
  assert.equal(context.customJS.state.coreMeta.campaigns[0].name, "Addermarch");

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
      campaignInfo: [{ campaign: "dufr", date: "1748-01-01", type: "met" }],
    },
  });

  assert.equal(resolvedPerson, "Dunmar Fellowship");
  assert.equal(meetings[0].campaign, "dufr");
  console.log("Header campaign registry tests passed.");
}

run().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});

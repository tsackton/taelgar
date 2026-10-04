// Run the vault's live Obsidian header logic with a read-only metadata adapter.
"use strict";
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
// Obsidian supplies these extensions to the live header classes. The adapter
// also returns host-realm arrays, so install them in both realms.
function installObsidianExtensions() {
  for (const [prototype, name, value] of [
    [Array.prototype, "first", function () { return this[0]; }],
    [Array.prototype, "last", function () { return this[this.length - 1]; }],
    [Array.prototype, "contains", Array.prototype.includes],
    [String.prototype, "contains", String.prototype.includes],
  ]) {
    if (typeof prototype[name] !== "function") {
      Object.defineProperty(prototype, name, {value, configurable: true, writable: true});
    }
  }
}
async function main() {
  installObsidianExtensions();
  const input = JSON.parse(fs.readFileSync(0, "utf8"));
  const files = input.files;
  const app = {
    vault: {
      configDir: ".obsidian",
      getRoot: () => ({path: ""}),
      getMarkdownFiles: () => files,
      adapter: {read: async p => fs.readFileSync(path.join(input.root, p), "utf8")},
    },
    metadataCache: {
      getFileCache: f => ({frontmatter: f.frontmatter}),
      getFirstLinkpathDest: target => {
        const normalized = target.replace(/\.md$/, "");
        const matches = files.filter(f => f.path.replace(/\.md$/, "") === normalized || f.basename === normalized);
        if (matches.length > 1) throw new Error(`Ambiguous header link: ${target}`);
        return matches[0];
      },
    },
  };
  const customJS = {state: {overrideDate: input.date}};
  const context = vm.createContext({app, window: {app}, customJS});
  vm.runInContext(`(${installObsidianExtensions.toString()})()`, context);
  const classes = {
    init: "loadMetadata", DateManager: "dataUtil", NameManager: "nameManager",
    TokenParser: "tokenParser", WhereaboutsManager: "whereabouts",
    AffiliationManager: "affiliationManager", EventManager: "eventManager",
    OutputHandler: "outputs",
  };
  for (const [name, filename] of Object.entries(classes)) {
    const source = fs.readFileSync(path.join(input.root, "_scripts/customJS", filename + ".js"), "utf8");
    const Class = vm.runInContext(`(${source})`, context, {filename});
    customJS[name] = new Class();
  }
  await customJS.init.invoke();
  process.stdout.write(customJS.OutputHandler.generateHeader(input.name, input.metadata, true));
}
main().catch(error => {console.error(error.message); process.exitCode = 1;});

"use strict";

const {
  ItemView,
  Modal,
  Notice,
  Plugin,
  PluginSettingTab,
  Setting,
  TFile,
  setIcon,
} = require("obsidian");
const nodePath = require("path");

let core;

const VIEW_TYPE = "taelgar-name-explorer-view";

const DEFAULT_SETTINGS = {
  decisionStorePath: "_MoC/Name Decisions.jsonl",
  exportPath: "_MoC/Name Explorer Catalog.jsonl",
  placeEvidencePath: "_MoC/Place Name Evidence.jsonl",
  scanTextEvidence: true,
  pageSize: 100,
};

const DEFAULT_HALFLING_RULE = {
  type: "rule",
  id: "halfling-person-names-common",
  label: "Halfling personal names default to Common",
  match: {
    noteType: "person",
    species: "halfling",
    role: "*",
  },
  language: "Common",
  priority: 50,
  enabled: true,
};

module.exports = class TaelgarNameExplorerPlugin extends Plugin {
  async onload() {
    core = this.loadCore();
    this.settings = { ...DEFAULT_SETTINGS, ...(await this.loadData()) };
    this.catalogCache = null;
    this.catalogPromise = null;
    this.refreshTimer = null;
    this.storeWriteInProgress = false;

    this.registerView(
      VIEW_TYPE,
      (leaf) => new NameExplorerView(leaf, this),
    );

    this.addRibbonIcon("languages", "Open Name Explorer", () => {
      void this.activateView();
    });

    this.addCommand({
      id: "open-name-explorer",
      name: "Open name explorer",
      callback: () => void this.activateView(),
    });
    this.addCommand({
      id: "refresh-name-explorer",
      name: "Refresh name index",
      callback: async () => {
        this.invalidateCatalog();
        await this.refreshOpenViews();
        new Notice("Name Explorer index refreshed.");
      },
    });
    this.addCommand({
      id: "export-name-explorer-catalog",
      name: "Export merged name catalog",
      callback: () => void this.exportCatalog(),
    });

    this.addSettingTab(new NameExplorerSettingTab(this.app, this));

    this.registerEvent(
      this.app.metadataCache.on("changed", (file) => {
        if (file?.extension === "md") this.scheduleRefresh();
      }),
    );
    this.registerEvent(
      this.app.vault.on("create", (file) => {
        if (file?.extension === "md") this.scheduleRefresh();
      }),
    );
    this.registerEvent(
      this.app.vault.on("delete", (file) => {
        if (file?.extension === "md") this.scheduleRefresh();
      }),
    );
    this.registerEvent(
      this.app.vault.on("rename", (file, oldPath) => {
        if (file?.extension === "md") {
          void this.migrateSubjectPath(oldPath, file.path);
        }
      }),
    );
    this.registerEvent(
      this.app.vault.on("modify", (file) => {
        if (
          file?.path === this.settings.decisionStorePath &&
          !this.storeWriteInProgress
        ) {
          this.scheduleRefresh();
        }
        if (file?.path === this.settings.placeEvidencePath) {
          this.scheduleRefresh();
        }
      }),
    );

    this.register(() => {
      if (this.refreshTimer) window.clearTimeout(this.refreshTimer);
    });

    try {
      await this.ensureDecisionStore();
    } catch (error) {
      console.error("Taelgar Name Explorer could not initialize its store", error);
      new Notice(`Name Explorer store error: ${error.message}`);
    }
  }

  onunload() {
    this.app.workspace.detachLeavesOfType(VIEW_TYPE);
  }

  loadCore() {
    const adapter = this.app.vault.adapter;
    if (typeof adapter.getBasePath !== "function") {
      throw new Error("Taelgar Name Explorer requires a desktop filesystem vault.");
    }
    const corePath = nodePath.join(
      adapter.getBasePath(),
      this.app.vault.configDir,
      "plugins",
      this.manifest.id,
      "core.js",
    );
    if (require.cache?.[corePath]) delete require.cache[corePath];
    return require(corePath);
  }

  async activateView() {
    let leaf = this.app.workspace.getLeavesOfType(VIEW_TYPE)[0];
    if (!leaf) {
      leaf = this.app.workspace.getLeaf("tab");
      await leaf.setViewState({ type: VIEW_TYPE, active: true });
    }
    await this.app.workspace.revealLeaf(leaf);
  }

  invalidateCatalog() {
    this.catalogCache = null;
    this.catalogPromise = null;
  }

  scheduleRefresh() {
    this.invalidateCatalog();
    if (this.refreshTimer) window.clearTimeout(this.refreshTimer);
    this.refreshTimer = window.setTimeout(() => {
      this.refreshTimer = null;
      void this.refreshOpenViews();
    }, 700);
  }

  async refreshOpenViews() {
    const views = this.app.workspace
      .getLeavesOfType(VIEW_TYPE)
      .map((leaf) => leaf.view)
      .filter((view) => view instanceof NameExplorerView);
    await Promise.all(views.map((view) => view.refresh()));
  }

  async ensureDecisionStore() {
    const path = this.settings.decisionStorePath;
    let file = this.app.vault.getAbstractFileByPath(path);
    if (!file) {
      await this.ensureParentFolder(path);
      file = await this.app.vault.create(
        path,
        core.serializeDecisionStore([DEFAULT_HALFLING_RULE]),
      );
      return file;
    }
    if (!(file instanceof TFile)) {
      throw new Error(`Decision store path is not a file: ${path}`);
    }
    core.parseDecisionStore(await this.app.vault.read(file));
    return file;
  }

  async ensureParentFolder(path) {
    const parts = path.split("/");
    parts.pop();
    let current = "";
    for (const part of parts) {
      current = current ? `${current}/${part}` : part;
      if (!this.app.vault.getAbstractFileByPath(current)) {
        await this.app.vault.createFolder(current);
      }
    }
  }

  async loadDecisionRecords() {
    const file = await this.ensureDecisionStore();
    return core.parseDecisionStore(await this.app.vault.read(file));
  }

  async loadPlaceEvidence() {
    const path = this.settings.placeEvidencePath;
    const file = this.app.vault.getAbstractFileByPath(path);
    if (!file) return core.parsePlaceEvidenceStore("");
    if (!(file instanceof TFile)) {
      throw new Error(`Place evidence path is not a file: ${path}`);
    }
    return core.parsePlaceEvidenceStore(await this.app.vault.read(file));
  }

  async mutateDecisionStore(mutator) {
    const file = await this.ensureDecisionStore();
    let nextRecords = null;
    this.storeWriteInProgress = true;
    try {
      await this.app.vault.process(file, (currentText) => {
        const current = core.parseDecisionStore(currentText);
        nextRecords = core.normalizeStoreRecords(mutator(current));
        return core.serializeDecisionStore(nextRecords);
      });
    } finally {
      this.storeWriteInProgress = false;
    }
    this.invalidateCatalog();
    return nextRecords || [];
  }

  async migrateSubjectPath(oldPath, newPath) {
    try {
      await this.mutateDecisionStore((records) =>
        records.map((record) =>
          record.subject === oldPath ? { ...record, subject: newPath } : record
        ),
      );
      await this.refreshOpenViews();
    } catch (error) {
      console.error("Name Explorer could not migrate a renamed subject", error);
      new Notice(`Name Explorer rename migration failed: ${error.message}`);
    }
  }

  async buildSubjects(onProgress) {
    const scanEligibleFiles = this.app.vault.getMarkdownFiles().filter((file) =>
      core.shouldScanPath(file.path)
    );
    this.knownMarkdownPaths = new Set(
      scanEligibleFiles.map((file) => file.path),
    );
    const files = scanEligibleFiles.filter((file) => {
      if (!core.shouldScanPath(file.path)) return false;
      const cache = this.app.metadataCache.getFileCache(file);
      const frontmatter = cache?.frontmatter;
      if (!frontmatter || !core.toStrings(frontmatter.tags).length) return false;
      return core.NOTE_TYPES.includes(
        core.chooseNoteType(core.toStrings(frontmatter.tags)),
      );
    });

    const subjects = [];
    const batchSize = 40;
    for (let start = 0; start < files.length; start += batchSize) {
      const batch = files.slice(start, start + batchSize);
      const built = await Promise.all(
        batch.map(async (file) => {
          const cache = this.app.metadataCache.getFileCache(file) || {};
          const frontmatter = cache.frontmatter || {};
          const tags = core.toStrings(frontmatter.tags).map((tag) =>
            String(tag).replace(/^#/, "").toLocaleLowerCase("en")
          );
          const rawName = core.toStrings(frontmatter.name)[0];
          const sourceName = rawName || file.basename;
          const nameInfo = core.provisionalNameInfo(sourceName);
          const noteType = core.chooseNoteType(tags);
          const subtypeInfo = core.subtypeForSubject(noteType, frontmatter);
          const body = this.settings.scanTextEvidence
            ? await this.app.vault.cachedRead(file)
            : "";
          const aliases = core.toStrings(frontmatter.aliases);
          return {
            path: file.path,
            linkTarget: file.path.replace(/\.md$/i, ""),
            fileName: file.basename,
            rawName: sourceName,
            name: nameInfo.text,
            provisionalName: nameInfo.provisional,
            noteType,
            subtypes: subtypeInfo.values,
            subtypeLabel: subtypeInfo.label,
            subtypeSource: subtypeInfo.source,
            tags,
            title: core.toStrings(frontmatter.title),
            species: [
              ...core.toStrings(frontmatter.species),
              ...core.toStrings(frontmatter.subspecies),
            ],
            ancestry: core.toStrings(frontmatter.ancestry),
            locations: core.toStrings(frontmatter.whereabouts),
            pronunciation: core.toStrings(frontmatter.pronunciation)[0] || "",
            aliases,
            textAliases: this.settings.scanTextEvidence
              ? core.extractTextAliases(body, nameInfo.text)
              : [],
            body,
          };
        }),
      );
      subjects.push(...built);
      if (onProgress) {
        onProgress({
          processed: Math.min(start + batch.length, files.length),
          total: files.length,
        });
      }
      await new Promise((resolve) => window.setTimeout(resolve, 0));
    }
    subjects.sort((left, right) => left.name.localeCompare(right.name));
    return subjects;
  }

  async getCatalog(force = false, onProgress) {
    if (force) this.invalidateCatalog();
    if (this.catalogCache) return this.catalogCache;
    if (this.catalogPromise) return this.catalogPromise;

    this.catalogPromise = (async () => {
      const [records, subjects, placeEvidence] = await Promise.all([
        this.loadDecisionRecords(),
        this.buildSubjects(onProgress),
        this.loadPlaceEvidence(),
      ]);
      const catalog = core.buildCatalog(subjects, records, {
        knownSubjectPaths: this.knownMarkdownPaths || new Set(),
      });
      core.attachPlaceEvidence(catalog, placeEvidence);
      this.catalogCache = catalog;
      this.catalogPromise = null;
      return catalog;
    })().catch((error) => {
      this.catalogPromise = null;
      throw error;
    });
    return this.catalogPromise;
  }

  async exportCatalog() {
    try {
      const catalog = await this.getCatalog();
      const records = core.catalogExportRecords(catalog);
      const text = records.map((record) => JSON.stringify(record)).join("\n") +
        (records.length ? "\n" : "");
      const path = this.settings.exportPath;
      await this.ensureParentFolder(path);
      const existing = this.app.vault.getAbstractFileByPath(path);
      if (existing instanceof TFile) {
        await this.app.vault.modify(existing, text);
      } else if (!existing) {
        await this.app.vault.create(path, text);
      } else {
        throw new Error(`Export path is not a file: ${path}`);
      }
      new Notice(`Exported ${records.length} name concepts to ${path}.`);
    } catch (error) {
      console.error("Name Explorer export failed", error);
      new Notice(`Name Explorer export failed: ${error.message}`);
    }
  }

  async saveSettings() {
    await this.saveData(this.settings);
    this.invalidateCatalog();
  }
};

class NameExplorerView extends ItemView {
  constructor(leaf, plugin) {
    super(leaf);
    this.plugin = plugin;
    this.catalog = null;
    this.error = null;
    this.loading = false;
    this.state = {
      viewMode: "names",
      query: "",
      language: "",
      status: "",
      noteType: "",
      subtype: "",
      componentRole: "",
      relationship: "",
      nameReview: "",
      embeddedness: "",
      campaignEvidence: "",
      namingDepth: "",
      namingReviewState: "",
      sortKey: "preferredForm",
      sortDirection: "asc",
      page: 1,
      expanded: new Set(),
      selected: new Set(),
    };
  }

  getViewType() {
    return VIEW_TYPE;
  }

  getDisplayText() {
    return "Name Explorer";
  }

  getIcon() {
    return "languages";
  }

  async onOpen() {
    this.contentEl.addClass("taelgar-name-explorer");
    await this.refresh();
  }

  async refresh(force = false) {
    if (this.loading) return;
    this.loading = true;
    this.error = null;
    this.renderLoading({ processed: 0, total: 0 });
    try {
      this.catalog = await this.plugin.getCatalog(force, (progress) => {
        this.renderLoading(progress);
      });
    } catch (error) {
      this.error = error;
      console.error("Name Explorer failed to build its catalog", error);
    } finally {
      this.loading = false;
      this.render();
    }
  }

  renderLoading(progress) {
    this.contentEl.empty();
    const wrapper = this.contentEl.createDiv({ cls: "tne-loading" });
    wrapper.createDiv({ cls: "tne-spinner" });
    const message = progress.total
      ? `Indexing names… ${progress.processed.toLocaleString()} / ${progress.total.toLocaleString()} notes`
      : "Loading Name Explorer…";
    wrapper.createEl("p", { text: message });
  }

  render() {
    this.contentEl.empty();
    if (this.error) {
      const errorBox = this.contentEl.createDiv({ cls: "tne-error" });
      errorBox.createEl("h2", { text: "Name Explorer could not load" });
      errorBox.createEl("p", { text: this.error.message });
      const retry = errorBox.createEl("button", { text: "Retry" });
      retry.addEventListener("click", () => void this.refresh(true));
      return;
    }
    if (!this.catalog) return;

    this.renderHeader();
    this.renderFilters();
    if (this.state.viewMode === "names") {
      this.renderBulkBar();
      this.renderTable();
    } else {
      this.renderComponentTable(this.state.viewMode === "corpus");
    }
  }

  renderHeader() {
    const header = this.contentEl.createDiv({ cls: "tne-header" });
    const heading = header.createDiv();
    heading.createEl("h1", { text: "Name Explorer" });
    const counts = summarizeCatalog(this.catalog);
    heading.createEl("p", {
      cls: "tne-subtitle",
      text: `${counts.concepts.toLocaleString()} name concepts · ` +
        `${counts.forms.toLocaleString()} observed forms · ` +
        `${counts.components.toLocaleString()} components · ` +
        `${counts.corpus.toLocaleString()} corpus entries · ` +
        `${counts.nameReview.toLocaleString()} need name review · ` +
        `${counts.placeEvidence.toLocaleString()} places with evidence · ` +
        `${counts.overridden.toLocaleString()} overridden · ` +
        `${counts.unknown.toLocaleString()} unknown`,
    });

    const actions = header.createDiv({ cls: "tne-header-actions" });
    actions.appendChild(iconButton("refresh-cw", "Refresh", () => {
      void this.refresh(true);
    }));
    actions.appendChild(iconButton("list-checks", "Rules", () => {
      new RulesModal(this.app, this.plugin, this.catalog).open();
    }));
    const orphanLabel = this.catalog.orphans.length
      ? `Orphans (${this.catalog.orphans.length})`
      : "Orphans";
    actions.appendChild(iconButton("unlink", orphanLabel, () => {
      new OrphansModal(this.app, this.plugin, this.catalog).open();
    }));
    actions.appendChild(iconButton("download", "Export", () => {
      void this.plugin.exportCatalog();
    }));
  }

  renderFilters() {
    const filters = this.contentEl.createDiv({ cls: "tne-filters" });
    filters.appendChild(makeSelect(
      [
        ["names", "Names"],
        ["components", "Components"],
        ["corpus", "Language corpus"],
      ],
      this.state.viewMode,
      (value) => {
        this.state.viewMode = value;
        this.state.page = 1;
        this.state.selected.clear();
        this.state.sortKey = value === "names" ? "preferredForm" : "text";
        this.render();
      },
      "Explorer view",
    ));
    const search = filters.createEl("input", {
      type: "search",
      placeholder: this.state.viewMode === "names"
        ? "Search names, subjects, variants, or paths…"
        : "Search components, display names, subjects, or paths…",
      value: this.state.query,
      cls: "tne-search",
    });
    search.addEventListener("input", () => {
      this.state.query = search.value;
      this.state.page = 1;
      this.render();
      const next = this.contentEl.querySelector(".tne-search");
      if (next) {
        next.focus();
        next.setSelectionRange(this.state.query.length, this.state.query.length);
      }
    });

    filters.appendChild(makeSelect(
      [
        ["", "All languages"],
        ...core.LANGUAGE_DEFINITIONS.map(([, language]) => [language, language]),
      ],
      this.state.language,
      (value) => {
        this.state.language = value;
        this.state.page = 1;
        this.render();
      },
      "Language",
    ));
    filters.appendChild(makeSelect(
      [
        ["", "All review states"],
        ["overridden", "Overridden"],
        ["confirmed", "Confirmed"],
        ["reviewed-unknown", "Reviewed unknown"],
        ["rule", "Catalog rule"],
        ["text-evidence", "Text evidence"],
        ["conflict", "Conflicting evidence"],
        ["convention", "Trade convention"],
        ["structural", "Language-neutral structure"],
        ["inferred", "Unreviewed inference"],
        ["unknown", "Unknown"],
      ],
      this.state.status,
      (value) => {
        this.state.status = value;
        this.state.page = 1;
        this.render();
      },
      "Review state",
    ));
    filters.appendChild(makeSelect(
      [
        ["", "All note types"],
        ...core.NOTE_TYPES.map((noteType) => [noteType, noteType]),
      ],
      this.state.noteType,
      (value) => {
        this.state.noteType = value;
        const availableSubtypes = new Set(
          core.subtypeChoices(this.catalog.subjects, value).map((subtype) =>
            core.normalizeLoose(subtype)
          ),
        );
        if (
          this.state.subtype &&
          !availableSubtypes.has(core.normalizeLoose(this.state.subtype))
        ) {
          this.state.subtype = "";
        }
        this.state.page = 1;
        this.render();
      },
      "Note type",
    ));
    filters.appendChild(makeSelect(
      [
        ["", "All subtypes"],
        ...subtypeOptions(this.catalog, this.state.noteType),
      ],
      this.state.subtype,
      (value) => {
        this.state.subtype = value;
        this.state.page = 1;
        this.render();
      },
      "Subtype",
    ));
    filters.appendChild(makeSelect(
      [
        ["", "All naming states"],
        ["needs-review", "Needs name review"],
        ["settled", "No name review flag"],
      ],
      this.state.nameReview,
      (value) => {
        this.state.nameReview = value;
        this.state.page = 1;
        this.render();
      },
      "Name review flag",
    ));
    if (this.state.viewMode !== "names") {
      filters.appendChild(makeSelect(
        [
          ["", "All component roles"],
          ...core.COMPONENT_ROLES.map((role) => [role, role]),
        ],
        this.state.componentRole,
        (value) => {
          this.state.componentRole = value;
          this.state.page = 1;
          this.render();
        },
        "Component role",
      ));
    }
    if (this.state.viewMode === "names") {
      filters.appendChild(makeSelect(
        [
          ["", "All name kinds"],
          ["endonym", "Endonym"],
          ["exonym", "Exonym"],
          ["conventional", "Conventional"],
          ["translation", "Translation"],
          ["literal-translation", "Literal translation"],
          ["conventional-translation", "Conventional translation"],
          ["historical", "Historical"],
          ["unclassified", "No kind assigned"],
        ],
        this.state.relationship,
        (value) => {
          this.state.relationship = value;
          this.state.page = 1;
          this.render();
        },
        "Name kind",
      ));
      filters.appendChild(makeSelect(
        [
          ["", "All embeddedness"],
          ["unlinked", "Unlinked"],
          ["low", "Low embeddedness"],
          ["medium", "Medium embeddedness"],
          ["high", "High embeddedness"],
          ["very-high", "Very high embeddedness"],
        ],
        this.state.embeddedness,
        (value) => {
          this.state.embeddedness = value;
          this.state.page = 1;
          this.render();
        },
        "Vault embeddedness",
      ));
      filters.appendChild(makeSelect(
        [
          ["", "All campaign evidence"],
          ["any", "Any mapped campaign evidence"],
          ["any-session", "Any session evidence"],
          ["confirmed-transcript", "Confirmed in transcript"],
          ["recurring", "Recurring in play"],
          ["campaign-core", "Campaign core"],
          ["campaign-context-only", "Campaign context only"],
          ["none", "No mapped campaign evidence"],
        ],
        this.state.campaignEvidence,
        (value) => {
          this.state.campaignEvidence = value;
          this.state.page = 1;
          this.render();
        },
        "Campaign evidence",
      ));
      filters.appendChild(makeSelect(
        [
          ["", "All naming depth"],
          ["none", "No naming documentation"],
          ["form-only", "Forms only"],
          ["documented", "Documented naming"],
          ["developed", "Developed naming"],
        ],
        this.state.namingDepth,
        (value) => {
          this.state.namingDepth = value;
          this.state.page = 1;
          this.render();
        },
        "Naming documentation",
      ));
      filters.appendChild(makeSelect(
        [
          ["", "All naming review states"],
          ["unreviewed", "Unreviewed"],
          ["no-debate-signal", "No debate signal"],
          ["curated", "Curated"],
          ["needs-review", "Needs review"],
          ["explicitly-provisional", "Explicitly provisional"],
          ["explicitly-debated", "Explicitly debated"],
          ["conflicting", "Conflicting"],
        ],
        this.state.namingReviewState,
        (value) => {
          this.state.namingReviewState = value;
          this.state.page = 1;
          this.render();
        },
        "Naming evidence state",
      ));
    }
  }

  renderBulkBar() {
    if (!this.state.selected.size) return;
    const bar = this.contentEl.createDiv({ cls: "tne-bulk-bar" });
    bar.createEl("strong", {
      text: `${this.state.selected.size} selected`,
    });
    let selectedLanguage = "";
    const languageSelect = makeSelect(
      [
        ["", "Choose language…"],
        ...core.LANGUAGE_DEFINITIONS.map(([, language]) => [language, language]),
      ],
      "",
      (value) => {
        selectedLanguage = value;
      },
      "Bulk language",
    );
    bar.appendChild(languageSelect);
    const apply = bar.createEl("button", { text: "Assign language" });
    apply.addEventListener("click", async () => {
      if (!selectedLanguage) {
        new Notice("Choose a language first.");
        return;
      }
      const targets = this.catalog.concepts.filter((concept) =>
        this.state.selected.has(conceptKey(concept))
      );
      await this.plugin.mutateDecisionStore((records) => {
        let next = records;
        for (const concept of targets) {
          const existing = next.find(
            (record) =>
              record.type === "concept" &&
              record.subject === concept.subjectPath &&
              record.concept === concept.id,
          );
          next = core.upsertStoreRecord(next, {
            ...(existing || {}),
            type: "concept",
            subject: concept.subjectPath,
            concept: concept.id,
            form: concept.preferredForm,
            language: selectedLanguage,
          });
        }
        return next;
      });
      this.state.selected.clear();
      await this.refresh(true);
      new Notice(`Assigned ${selectedLanguage} to ${targets.length} name concepts.`);
    });
    const clear = bar.createEl("button", { text: "Clear selection" });
    clear.addEventListener("click", () => {
      this.state.selected.clear();
      this.render();
    });
  }

  filteredConcepts() {
    const query = core.normalizeLoose(this.state.query);
    return this.catalog.concepts.filter((concept) => {
      if (
        this.state.language &&
        !concept.components.some((component) =>
          component.effectiveLanguage.language === this.state.language
        )
      ) return false;
      if (this.state.status && concept.status !== this.state.status) return false;
      if (
        this.state.nameReview === "needs-review" &&
        !concept.needsNameReview
      ) return false;
      if (
        this.state.nameReview === "settled" &&
        concept.needsNameReview
      ) return false;
      if (
        this.state.noteType &&
        concept.subject.noteType !== this.state.noteType
      ) return false;
      if (
        this.state.subtype &&
        !concept.subject.subtypes.some((subtype) =>
          core.normalizeLoose(subtype) === core.normalizeLoose(this.state.subtype)
        )
      ) return false;
      if (this.state.relationship) {
        if (
          this.state.relationship === "unclassified" &&
          (concept.relationship || concept.derivation || concept.usage)
        ) return false;
        if (
          this.state.relationship !== "unclassified" &&
          ![
            concept.relationship,
            concept.derivation,
            concept.usage,
          ].includes(this.state.relationship)
        ) return false;
      }
      const placeEvidence = concept.placeEvidence;
      const hasPlaceEvidenceFilter = Boolean(
        this.state.embeddedness ||
        this.state.campaignEvidence ||
        this.state.namingDepth ||
        this.state.namingReviewState
      );
      if (hasPlaceEvidenceFilter && !placeEvidence) return false;
      if (
        this.state.embeddedness &&
        placeEvidence?.embeddedness?.band !== this.state.embeddedness
      ) return false;
      if (
        this.state.namingDepth &&
        placeEvidence?.naming?.documentation_depth !== this.state.namingDepth
      ) return false;
      if (
        this.state.namingReviewState &&
        placeEvidence?.naming?.review_state !== this.state.namingReviewState
      ) return false;
      if (this.state.campaignEvidence) {
        const campaigns = placeEvidence?.campaigns || [];
        if (
          this.state.campaignEvidence === "any" &&
          !campaigns.length
        ) return false;
        if (
          this.state.campaignEvidence === "none" &&
          campaigns.length
        ) return false;
        if (
          this.state.campaignEvidence === "any-session" &&
          !campaigns.some((campaign) => campaign.session_count > 0)
        ) return false;
        if (
          this.state.campaignEvidence === "confirmed-transcript" &&
          !campaigns.some((campaign) =>
            campaign.introduced_in_play === "confirmed-transcript"
          )
        ) return false;
        if (
          this.state.campaignEvidence === "recurring" &&
          !campaigns.some((campaign) =>
            ["recurring", "campaign-core"].includes(campaign.recurrence)
          )
        ) return false;
        if (
          this.state.campaignEvidence === "campaign-core" &&
          !campaigns.some((campaign) => campaign.recurrence === "campaign-core")
        ) return false;
        if (
          this.state.campaignEvidence === "campaign-context-only" &&
          !campaigns.some((campaign) =>
            campaign.recurrence === "campaign-context-only"
          )
        ) return false;
      }
      if (query) {
        const haystack = core.normalizeLoose([
          concept.preferredForm,
          concept.subjectName,
          concept.subjectPath,
          concept.subject.subtypeLabel,
          concept.effectiveLanguage.language,
          concept.inferredLanguage.language,
          ...concept.forms.map((form) => form.text),
          ...concept.components.flatMap((component) => [
            component.text,
            component.role,
            component.effectiveLanguage.language,
          ]),
          placeEvidence?.embeddedness?.band,
          placeEvidence?.naming?.documentation_depth,
          placeEvidence?.naming?.review_state,
          ...(placeEvidence?.campaigns || []).flatMap((campaign) => [
            campaign.campaign,
            campaign.introduced_in_play,
            campaign.recurrence,
            ...(campaign.forms_exposed || []),
          ]),
        ].join(" "));
        if (!haystack.includes(query)) return false;
      }
      return true;
    });
  }

  sortedConcepts(concepts) {
    const direction = this.state.sortDirection === "asc" ? 1 : -1;
    const valueFor = (concept) => {
      switch (this.state.sortKey) {
        case "subjectName": return core.normalizeLoose(concept.subjectName);
        case "noteType": return concept.subject.noteType;
        case "subtype": return core.normalizeLoose(
          concept.subject.subtypeLabel,
        );
        case "effectiveLanguage": return concept.languageSummary;
        case "inferredLanguage": return concept.inferredLanguage.language;
        case "kindLabel": return concept.kindLabel;
        case "status": return concept.status;
        case "variants": return concept.forms.length;
        case "embeddedness": return concept.placeEvidence?.embeddedness?.percentile_all_places ?? -1;
        case "campaigns": return (concept.placeEvidence?.campaigns || []).reduce(
          (total, campaign) => total + (campaign.session_count || 0),
          0,
        );
        case "namingDepth": return ["none", "form-only", "documented", "developed"].indexOf(
          concept.placeEvidence?.naming?.documentation_depth || "none",
        );
        case "namingReviewState": return concept.placeEvidence?.naming?.review_state || "";
        default: return core.normalizeLoose(concept.preferredForm);
      }
    };
    return [...concepts].sort((left, right) => {
      const a = valueFor(left);
      const b = valueFor(right);
      if (typeof a === "number" && typeof b === "number") return (a - b) * direction;
      return String(a).localeCompare(String(b)) * direction ||
        left.subjectPath.localeCompare(right.subjectPath);
    });
  }

  renderTable() {
    const filtered = this.sortedConcepts(this.filteredConcepts());
    const pageSize = Number(this.plugin.settings.pageSize) || 100;
    const pageCount = Math.max(1, Math.ceil(filtered.length / pageSize));
    this.state.page = Math.min(this.state.page, pageCount);
    const start = (this.state.page - 1) * pageSize;
    const pageRows = filtered.slice(start, start + pageSize);

    const summary = this.contentEl.createDiv({ cls: "tne-result-summary" });
    summary.createSpan({
      text: `${filtered.length.toLocaleString()} results`,
    });
    summary.createSpan({
      text: `Showing ${filtered.length ? start + 1 : 0}–${Math.min(start + pageSize, filtered.length)}`,
    });

    const scroller = this.contentEl.createDiv({ cls: "tne-table-scroller" });
    const table = scroller.createEl("table", { cls: "tne-table" });
    const thead = table.createEl("thead");
    const headerRow = thead.createEl("tr");
    const selectHeader = headerRow.createEl("th", { cls: "tne-select-cell" });
    const selectAll = selectHeader.createEl("input", { type: "checkbox" });
    selectAll.checked = pageRows.length > 0 && pageRows.every((concept) =>
      this.state.selected.has(conceptKey(concept))
    );
    selectAll.addEventListener("change", () => {
      for (const concept of pageRows) {
        if (selectAll.checked) this.state.selected.add(conceptKey(concept));
        else this.state.selected.delete(conceptKey(concept));
      }
      this.render();
    });
    this.renderSortableHeader(headerRow, "preferredForm", "Name");
    this.renderSortableHeader(headerRow, "subjectName", "Subject");
    this.renderSortableHeader(headerRow, "noteType", "Type");
    this.renderSortableHeader(headerRow, "subtype", "Subtype");
    this.renderSortableHeader(headerRow, "effectiveLanguage", "Language");
    this.renderSortableHeader(headerRow, "inferredLanguage", "Inferred");
    this.renderSortableHeader(headerRow, "kindLabel", "Kind");
    this.renderSortableHeader(headerRow, "status", "Review");
    this.renderSortableHeader(headerRow, "variants", "Forms");
    this.renderSortableHeader(headerRow, "embeddedness", "Embedded");
    this.renderSortableHeader(headerRow, "campaigns", "Play");
    this.renderSortableHeader(headerRow, "namingDepth", "Naming");
    headerRow.createEl("th", { text: "" });

    const tbody = table.createEl("tbody");
    for (const concept of pageRows) {
      const key = conceptKey(concept);
      const row = tbody.createEl("tr");
      if (this.state.expanded.has(key)) row.addClass("is-expanded");

      const selectCell = row.createEl("td", { cls: "tne-select-cell" });
      const checkbox = selectCell.createEl("input", { type: "checkbox" });
      checkbox.checked = this.state.selected.has(key);
      checkbox.addEventListener("change", () => {
        if (checkbox.checked) this.state.selected.add(key);
        else this.state.selected.delete(key);
        this.render();
      });

      const nameCell = row.createEl("td", { cls: "tne-name-cell" });
      const expand = nameCell.createEl("button", {
        cls: "tne-disclosure",
        attr: { "aria-label": "Show observed forms" },
      });
      setIcon(
        expand,
        this.state.expanded.has(key) ? "chevron-down" : "chevron-right",
      );
      expand.addEventListener("click", () => {
        if (this.state.expanded.has(key)) this.state.expanded.delete(key);
        else this.state.expanded.add(key);
        this.render();
      });
      nameCell.createSpan({ text: concept.preferredForm });
      if (concept.needsNameReview) {
        nameCell.appendChild(nameReviewChip(concept.nameReviewReasons));
      }

      const subjectCell = row.createEl("td");
      const subjectButton = subjectCell.createEl("button", {
        text: concept.subjectName,
        cls: "tne-link-button",
      });
      subjectButton.title = concept.subjectPath;
      subjectButton.addEventListener("click", () => {
        const file = this.app.vault.getAbstractFileByPath(concept.subjectPath);
        if (file instanceof TFile) {
          void this.app.workspace.getLeaf(false).openFile(file);
        }
      });

      row.createEl("td", { text: concept.subject.noteType });
      row.createEl("td", {
        text: concept.subject.subtypeLabel || "—",
      });
      row.createEl("td").appendChild(languageChip(
        concept.languageSummary,
        concept.languageSource,
      ));
      const inferredCell = row.createEl("td");
      inferredCell.createSpan({
        text: concept.inferredLanguage.language,
        attr: { title: concept.inferredLanguage.basis },
      });
      row.createEl("td", { text: concept.kindLabel });
      row.createEl("td").appendChild(statusChip(concept.status));
      row.createEl("td", { text: String(concept.forms.length) });
      const placeEvidence = concept.placeEvidence;
      const embeddedCell = row.createEl("td", {
        text: placeEvidence
          ? embeddednessLabel(placeEvidence.embeddedness)
          : "—",
      });
      if (placeEvidence) {
        embeddedCell.title = `${placeEvidence.embeddedness.inbound.unique_notes} inbound notes · ` +
          `${placeEvidence.embeddedness.inbound.mentions} inbound mentions · ` +
          `${placeEvidence.embeddedness.outbound.unique_notes} outbound notes`;
      }
      const campaignCell = row.createEl("td", {
        text: campaignEvidenceLabel(placeEvidence?.campaigns || []),
      });
      if (placeEvidence?.campaigns?.length) {
        campaignCell.title = placeEvidence.campaigns.map((campaign) =>
          `${campaign.campaign}: ${campaign.session_count} sessions · ` +
          `${campaign.introduced_in_play} · ${campaign.recurrence}`
        ).join("\n");
      }
      const namingCell = row.createEl("td", {
        text: placeEvidence
          ? `${placeEvidence.naming.documentation_depth} · ${placeEvidence.naming.review_state}`
          : "—",
      });
      if (placeEvidence) {
        namingCell.title = `${placeEvidence.naming.languages.join(", ") || "Unknown language"} · ` +
          `${placeEvidence.naming.evidence.length} naming evidence excerpts`;
      }
      const editCell = row.createEl("td");
      editCell.appendChild(iconButton("pencil", "Edit", () => {
        new EditConceptModal(this.app, this.plugin, concept, this.catalog).open();
      }, true));

      if (this.state.expanded.has(key)) {
        const detailRow = tbody.createEl("tr", { cls: "tne-detail-row" });
        const detailCell = detailRow.createEl("td", {
          attr: { colspan: "14" },
        });
        this.renderConceptDetails(detailCell, concept);
      }
    }

    this.renderPagination(filtered.length, pageCount);
  }

  renderSortableHeader(row, key, label) {
    const cell = row.createEl("th");
    const button = cell.createEl("button", { cls: "tne-sort-button" });
    button.createSpan({ text: label });
    if (this.state.sortKey === key) {
      const icon = button.createSpan({ cls: "tne-sort-icon" });
      setIcon(icon, this.state.sortDirection === "asc" ? "arrow-up" : "arrow-down");
    }
    button.addEventListener("click", () => {
      if (this.state.sortKey === key) {
        this.state.sortDirection =
          this.state.sortDirection === "asc" ? "desc" : "asc";
      } else {
        this.state.sortKey = key;
        this.state.sortDirection = "asc";
      }
      this.render();
    });
  }

  renderConceptDetails(container, concept) {
    const grid = container.createDiv({ cls: "tne-detail-grid" });
    const evidence = grid.createDiv();
    evidence.createEl("strong", { text: "Language basis" });
    evidence.createEl("p", { text: concept.effectiveLanguage.basis });
    for (const item of concept.inferredLanguage.evidence || []) {
      if (!item.quote) continue;
      evidence.createEl("blockquote", {
        text: `Line ${item.line}: ${item.quote}`,
        cls: "tne-evidence-quote",
      });
    }
    if (
      concept.effectiveLanguage.language !== concept.inferredLanguage.language
    ) {
      evidence.createEl("p", {
        cls: "tne-muted",
        text: `Underlying inference: ${concept.inferredLanguage.language} — ${concept.inferredLanguage.basis}`,
      });
    }
    if (concept.community) {
      evidence.createEl("p", { text: `Naming community: ${concept.community}` });
    }
    if (concept.derivation) {
      evidence.createEl("p", {
        text: `Derivation: ${concept.derivation}` +
          `${concept.derivationSource ? ` (${concept.derivationSource})` : ""}`,
      });
    }
    if (concept.sourceLanguage || concept.sourceForm) {
      evidence.createEl("p", {
        text: `Source: ${[
          concept.sourceForm,
          concept.sourceLanguage,
        ].filter(Boolean).join(" · ")}`,
      });
    }
    if (concept.decisionNotes) {
      evidence.createEl("p", { text: concept.decisionNotes });
    }
    if (concept.needsNameReview) {
      evidence.createEl("p", {
        cls: "tne-name-review-note",
        text: `Needs name review: ${nameReviewReasonLabels(
          concept.nameReviewReasons,
        ).join("; ")}`,
      });
    }

    const forms = grid.createDiv();
    forms.createEl("strong", { text: "Name components" });
    const componentList = forms.createEl("ul", { cls: "tne-component-list" });
    for (const component of concept.components) {
      const item = componentList.createEl("li");
      item.createSpan({ text: component.text });
      item.createSpan({
        cls: "tne-form-meta",
        text: `${component.role} · ${component.effectiveLanguage.language}` +
          `${component.corpusEligible ? " · corpus" : ""}`,
      });
    }

    forms.createEl("strong", { text: "Observed forms" });
    const list = forms.createEl("ul", { cls: "tne-form-list" });
    for (const form of concept.forms) {
      const item = list.createEl("li");
      item.createSpan({ text: form.text });
      item.createSpan({
        cls: "tne-form-meta",
        text: `${form.variantKind} · ${form.sources.join(", ")} · ` +
          form.components.map((component) =>
            `${component.text} [${component.role}]`
          ).join(" + "),
      });
    }
    if (concept.placeEvidence) {
      const place = grid.createDiv({ cls: "tne-place-evidence" });
      place.createEl("strong", { text: "Place-name evidence" });
      place.createEl("p", {
        text: `${embeddednessLabel(concept.placeEvidence.embeddedness)} embeddedness · ` +
          `${concept.placeEvidence.embeddedness.inbound.unique_notes} inbound notes · ` +
          `${concept.placeEvidence.embeddedness.outbound.unique_notes} outbound notes · ` +
          `${concept.placeEvidence.embeddedness.semantic_edges.inbound_unique_notes} semantic inlinks`,
      });
      place.createEl("p", {
        text: `Naming: ${concept.placeEvidence.naming.documentation_depth} · ` +
          `${concept.placeEvidence.naming.review_state} · ` +
          `${concept.placeEvidence.naming.languages.join(", ") || "unknown language"}`,
      });
      if (concept.placeEvidence.campaigns.length) {
        place.createEl("strong", { text: "Campaign evidence" });
        const campaigns = place.createEl("ul", { cls: "tne-form-list" });
        for (const campaign of concept.placeEvidence.campaigns) {
          campaigns.createEl("li", {
            text: `${campaign.campaign}: ${campaign.session_count} sessions · ` +
              `${campaign.scene_session_count} scene sessions · ` +
              `${campaign.transcript_session_count} transcript sessions ` +
              `(${campaign.transcript_occurrences} mentions; ` +
              `${campaign.player_transcript_occurrences} player / ` +
              `${campaign.dm_transcript_occurrences} DM) · ` +
              `${campaign.recap_session_count} recap sessions · ` +
              `${campaign.published_note_session_count} published-note sessions · ` +
              `${campaign.introduced_in_play} · ${campaign.recurrence}`,
          });
        }
      }
      if (concept.placeEvidence.unattributed_campaign_material?.length) {
        place.createEl("p", {
          text: `${concept.placeEvidence.unattributed_campaign_material.length} ` +
            "additional campaign-context note(s) could not be assigned to one campaign.",
        });
      }
      if (concept.placeEvidence.naming.evidence.length) {
        place.createEl("strong", { text: "Naming passages" });
        for (const item of concept.placeEvidence.naming.evidence.slice(0, 8)) {
          place.createEl("blockquote", {
            cls: "tne-evidence-quote",
            text: `${item.context} · line ${item.line} · ${item.kind}: ${item.snippet}`,
          });
        }
      }
    }
  }

  filteredComponents(corpusOnly) {
    const query = core.normalizeLoose(this.state.query);
    const source = corpusOnly ? this.catalog.corpus : this.catalog.components;
    return source.filter((component) => {
      if (
        this.state.language &&
        component.effectiveLanguage.language !== this.state.language
      ) return false;
      if (this.state.status && component.status !== this.state.status) {
        return false;
      }
      if (
        this.state.nameReview === "needs-review" &&
        !component.needsNameReview
      ) return false;
      if (
        this.state.nameReview === "settled" &&
        component.needsNameReview
      ) return false;
      if (
        this.state.noteType &&
        component.noteType !== this.state.noteType
      ) return false;
      if (
        this.state.subtype &&
        !component.subtypes.some((subtype) =>
          core.normalizeLoose(subtype) === core.normalizeLoose(this.state.subtype)
        )
      ) return false;
      if (
        this.state.componentRole &&
        component.role !== this.state.componentRole
      ) return false;
      if (query) {
        const haystack = core.normalizeLoose([
          component.text,
          component.displayName,
          component.subjectName,
          component.subjectPath,
          component.subtypeLabel,
          component.role,
          component.effectiveLanguage.language,
          component.effectiveLanguage.family,
        ].join(" "));
        if (!haystack.includes(query)) return false;
      }
      return true;
    });
  }

  sortedComponents(components) {
    const direction = this.state.sortDirection === "asc" ? 1 : -1;
    const valueFor = (component) => {
      switch (this.state.sortKey) {
        case "displayName": return core.normalizeLoose(component.displayName);
        case "subjectName": return core.normalizeLoose(component.subjectName);
        case "noteType": return component.noteType;
        case "subtype": return core.normalizeLoose(component.subtypeLabel);
        case "role": return component.role;
        case "effectiveLanguage": return component.effectiveLanguage.language;
        case "status": return component.status;
        case "corpus": return component.corpusEligible ? 1 : 0;
        default: return core.normalizeLoose(component.text);
      }
    };
    return [...components].sort((left, right) => {
      const a = valueFor(left);
      const b = valueFor(right);
      if (typeof a === "number" && typeof b === "number") {
        return (a - b) * direction;
      }
      return String(a).localeCompare(String(b)) * direction ||
        left.subjectPath.localeCompare(right.subjectPath);
    });
  }

  renderComponentTable(corpusOnly) {
    const filtered = this.sortedComponents(
      this.filteredComponents(corpusOnly),
    );
    const pageSize = Number(this.plugin.settings.pageSize) || 100;
    const pageCount = Math.max(1, Math.ceil(filtered.length / pageSize));
    this.state.page = Math.min(this.state.page, pageCount);
    const start = (this.state.page - 1) * pageSize;
    const pageRows = filtered.slice(start, start + pageSize);

    const summary = this.contentEl.createDiv({ cls: "tne-result-summary" });
    summary.createSpan({
      text: `${filtered.length.toLocaleString()} ` +
        (corpusOnly ? "corpus entries" : "components"),
    });
    summary.createSpan({
      text: `Showing ${filtered.length ? start + 1 : 0}–${Math.min(
        start + pageSize,
        filtered.length,
      )}`,
    });

    const scroller = this.contentEl.createDiv({ cls: "tne-table-scroller" });
    const table = scroller.createEl("table", {
      cls: "tne-table tne-component-table",
    });
    const headerRow = table.createEl("thead").createEl("tr");
    this.renderSortableHeader(headerRow, "text", "Component");
    this.renderSortableHeader(headerRow, "displayName", "Display name");
    this.renderSortableHeader(headerRow, "subjectName", "Subject");
    this.renderSortableHeader(headerRow, "noteType", "Type");
    this.renderSortableHeader(headerRow, "subtype", "Subtype");
    this.renderSortableHeader(headerRow, "role", "Role");
    this.renderSortableHeader(headerRow, "effectiveLanguage", "Language");
    this.renderSortableHeader(headerRow, "status", "Review");
    this.renderSortableHeader(headerRow, "corpus", "Corpus");
    headerRow.createEl("th", { text: "" });

    const tbody = table.createEl("tbody");
    for (const component of pageRows) {
      const row = tbody.createEl("tr");
      row.createEl("td", {
        text: component.text,
        cls: "tne-component-text",
      });
      const displayCell = row.createEl("td");
      const displayButton = displayCell.createEl("button", {
        text: component.displayName,
        cls: "tne-link-button",
      });
      if (component.needsNameReview) {
        displayCell.appendChild(nameReviewChip(component.nameReviewReasons));
      }
      displayButton.addEventListener("click", () => {
        const concept = this.catalog.concepts.find((candidate) =>
          candidate.subjectPath === component.subjectPath &&
          candidate.id === component.conceptId
        );
        if (concept) {
          new EditConceptModal(
            this.app,
            this.plugin,
            concept,
            this.catalog,
          ).open();
        }
      });
      const subjectCell = row.createEl("td");
      const subjectButton = subjectCell.createEl("button", {
        text: component.subjectName,
        cls: "tne-link-button",
      });
      subjectButton.title = component.subjectPath;
      subjectButton.addEventListener("click", () => {
        const file = this.app.vault.getAbstractFileByPath(
          component.subjectPath,
        );
        if (file instanceof TFile) {
          void this.app.workspace.getLeaf(false).openFile(file);
        }
      });
      row.createEl("td", { text: component.noteType });
      row.createEl("td", { text: component.subtypeLabel || "—" });
      row.createEl("td", { text: component.role });
      const languageCell = row.createEl("td");
      const chip = languageChip(
        component.effectiveLanguage.language,
        component.languageSource,
      );
      chip.title = component.effectiveLanguage.basis;
      languageCell.appendChild(chip);
      row.createEl("td").appendChild(statusChip(component.status));
      row.createEl("td", {
        text: component.corpusEligible ? "Included" : "Excluded",
      });
      const editCell = row.createEl("td");
      editCell.appendChild(iconButton("pencil", "Edit component", () => {
        new EditComponentModal(
          this.app,
          this.plugin,
          component,
        ).open();
      }, true));
    }

    this.renderPagination(filtered.length, pageCount);
  }

  renderPagination(total, pageCount) {
    if (pageCount <= 1) return;
    const pagination = this.contentEl.createDiv({ cls: "tne-pagination" });
    const previous = pagination.createEl("button", { text: "Previous" });
    previous.disabled = this.state.page <= 1;
    previous.addEventListener("click", () => {
      this.state.page -= 1;
      this.render();
    });
    pagination.createSpan({
      text: `Page ${this.state.page} of ${pageCount} · ${total.toLocaleString()} results`,
    });
    const next = pagination.createEl("button", { text: "Next" });
    next.disabled = this.state.page >= pageCount;
    next.addEventListener("click", () => {
      this.state.page += 1;
      this.render();
    });
  }
}

class EditComponentModal extends Modal {
  constructor(app, plugin, component) {
    super(app);
    this.plugin = plugin;
    this.component = component;
    this.values = {
      language: component.decision &&
        Object.prototype.hasOwnProperty.call(component.decision, "language")
        ? component.decision.language
        : "",
      role: component.decision?.role || "",
      corpus: component.decision?.corpus || "auto",
      notes: component.notes || "",
    };
  }

  onOpen() {
    this.modalEl.addClass("tne-modal");
    const { contentEl } = this;
    contentEl.createEl("h2", { text: this.component.text });
    contentEl.createEl("p", {
      cls: "tne-modal-subtitle",
      text: `${this.component.displayName} · ${this.component.subjectName}`,
    });
    contentEl.createEl("p", {
      cls: "tne-muted",
      text: `Automatic role: ${this.component.role} · inferred ` +
        `${this.component.inferredLanguage.language} — ` +
        this.component.inferredLanguage.basis,
    });

    new Setting(contentEl)
      .setName("Component role")
      .setDesc("Override the automatic decomposition role when necessary.")
      .addDropdown((dropdown) => {
        dropdown.addOption("", `Automatic (${this.component.role})`);
        for (const role of core.COMPONENT_ROLES) {
          dropdown.addOption(role, role);
        }
        dropdown.setValue(this.values.role);
        dropdown.onChange((value) => {
          this.values.role = value;
        });
      });

    new Setting(contentEl)
      .setName("Language decision")
      .setDesc("Applies only to this component of the displayed name.")
      .addDropdown((dropdown) => {
        dropdown.addOption("", "Use evidence, rule, or inference");
        for (const [, language] of core.LANGUAGE_DEFINITIONS) {
          dropdown.addOption(language, language);
        }
        dropdown.setValue(this.values.language);
        dropdown.onChange((value) => {
          this.values.language = value;
        });
      });

    new Setting(contentEl)
      .setName("Language corpus")
      .setDesc("Automatic excludes Trade renderings, structural components, and unknowns.")
      .addDropdown((dropdown) => {
        addOptions(dropdown, [
          ["auto", "Automatic"],
          ["include", "Always include"],
          ["exclude", "Always exclude"],
        ]);
        dropdown.setValue(this.values.corpus);
        dropdown.onChange((value) => {
          this.values.corpus = value;
        });
      });

    new Setting(contentEl)
      .setName("Decision notes")
      .addTextArea((text) => {
        text.setValue(this.values.notes);
        text.onChange((value) => {
          this.values.notes = value.trim();
        });
      });

    const buttons = contentEl.createDiv({ cls: "tne-modal-buttons" });
    const clear = buttons.createEl("button", {
      text: "Clear component decision",
    });
    clear.addEventListener("click", () => void this.clearDecision());
    const save = buttons.createEl("button", {
      text: "Save",
      cls: "mod-cta",
    });
    save.addEventListener("click", () => void this.save());
  }

  componentRecordStub() {
    return {
      type: "component",
      subject: this.component.subjectPath,
      concept: this.component.conceptId,
      component: this.component.id,
      form: this.component.text,
    };
  }

  async clearDecision() {
    const stub = this.componentRecordStub();
    await this.plugin.mutateDecisionStore((records) =>
      core.removeStoreRecord(records, stub)
    );
    this.close();
    await this.plugin.refreshOpenViews();
  }

  async save() {
    const stub = this.componentRecordStub();
    await this.plugin.mutateDecisionStore((records) => {
      let next = core.removeStoreRecord(records, stub);
      const record = { ...stub };
      if (this.values.language) record.language = this.values.language;
      if (this.values.role) record.role = this.values.role;
      if (this.values.corpus !== "auto") record.corpus = this.values.corpus;
      if (this.values.notes) record.notes = this.values.notes;
      if (Object.keys(record).length > 5) {
        next = core.upsertStoreRecord(next, record);
      }
      return next;
    });
    this.close();
    await this.plugin.refreshOpenViews();
  }
}

class EditConceptModal extends Modal {
  constructor(app, plugin, concept, catalog) {
    super(app);
    this.plugin = plugin;
    this.concept = concept;
    this.catalog = catalog;
    this.values = {
      language: concept.decision &&
        Object.prototype.hasOwnProperty.call(concept.decision, "language")
        ? concept.decision.language
        : "",
      relationship: concept.relationship || "",
      derivation: concept.decision?.derivation || "",
      usage: concept.usage || "",
      community: concept.community || "",
      sourceLanguage: concept.decision?.sourceLanguage || "",
      sourceForm: concept.decision?.sourceForm || "",
      notes: concept.decisionNotes || "",
    };
    this.formChoices = new Map();
  }

  onOpen() {
    this.modalEl.addClass("tne-modal");
    const { contentEl } = this;
    contentEl.createEl("h2", { text: this.concept.preferredForm });
    contentEl.createEl("p", {
      cls: "tne-modal-subtitle",
      text: `${this.concept.subjectName} · inferred ${this.concept.inferredLanguage.language}`,
    });

    new Setting(contentEl)
      .setName("Language decision")
      .setDesc("Leave blank to use text evidence, catalog rules, or inference.")
      .addDropdown((dropdown) => {
        dropdown.addOption("", "Use rule or inference");
        for (const [, language] of core.LANGUAGE_DEFINITIONS) {
          dropdown.addOption(language, language);
        }
        dropdown.setValue(this.values.language);
        dropdown.onChange((value) => {
          this.values.language = value;
        });
      });

    new Setting(contentEl)
      .setName("Relationship")
      .setDesc("Optional relationship to the naming community.")
      .addDropdown((dropdown) => {
        addOptions(dropdown, [
          ["", "Not specified"],
          ["endonym", "Endonym"],
          ["exonym", "Exonym"],
          ["conventional", "Conventional name"],
        ]);
        dropdown.setValue(this.values.relationship);
        dropdown.onChange((value) => {
          this.values.relationship = value;
        });
      });

    new Setting(contentEl)
      .setName("Derivation")
      .setDesc("Separate from endonym/exonym so translated exonyms remain possible.")
      .addDropdown((dropdown) => {
        addOptions(dropdown, [
          ["", "Not specified"],
          ["original", "Original"],
          ["translation", "Translation"],
          ["literal-translation", "Literal translation"],
          ["conventional-translation", "Conventional translation"],
          ["unattested-translation", "Translation of an unattested form"],
          ["transliteration", "Transliteration"],
        ]);
        dropdown.setValue(this.values.derivation);
        dropdown.onChange((value) => {
          this.values.derivation = value;
        });
      });

    new Setting(contentEl)
      .setName("Source language")
      .setDesc("Optional language from which a translated form derives.")
      .addDropdown((dropdown) => {
        dropdown.addOption("", "Not specified");
        for (const [, language] of core.LANGUAGE_DEFINITIONS) {
          dropdown.addOption(language, language);
        }
        dropdown.setValue(this.values.sourceLanguage);
        dropdown.onChange((value) => {
          this.values.sourceLanguage = value;
        });
      });

    new Setting(contentEl)
      .setName("Source form")
      .setDesc("May be another invented form or “unattested”.")
      .addText((text) => {
        text.setValue(this.values.sourceForm);
        text.onChange((value) => {
          this.values.sourceForm = value.trim();
        });
      });

    new Setting(contentEl)
      .setName("Usage")
      .setDesc("Historical status is independent of linguistic kind.")
      .addDropdown((dropdown) => {
        addOptions(dropdown, [
          ["", "Not specified"],
          ["current", "Current"],
          ["historical", "Historical"],
          ["archaic", "Archaic"],
        ]);
        dropdown.setValue(this.values.usage);
        dropdown.onChange((value) => {
          this.values.usage = value;
        });
      });

    new Setting(contentEl)
      .setName("Naming community")
      .setDesc("Optional culture, people, or community associated with this form.")
      .addText((text) => {
        text.setValue(this.values.community);
        text.onChange((value) => {
          this.values.community = value.trim();
        });
      });

    new Setting(contentEl)
      .setName("Decision notes")
      .setDesc("Optional evidence or rationale stored with the catalog decision.")
      .addTextArea((text) => {
        text.setValue(this.values.notes);
        text.onChange((value) => {
          this.values.notes = value.trim();
        });
      });

    contentEl.createEl("h3", { text: "Name components" });
    contentEl.createEl("p", {
      cls: "tne-muted",
      text: "Language and corpus decisions can be made separately for the core name, titles, epithets, locatives, and other components.",
    });
    for (const component of this.concept.components) {
      const setting = new Setting(contentEl)
        .setName(component.text)
        .setDesc(
          `${component.role} · ${component.effectiveLanguage.language}` +
          `${component.corpusEligible ? " · included in corpus" : ""}`,
        );
      setting.addButton((button) => {
        button.setButtonText("Edit component");
        button.onClick(() => {
          this.close();
          new EditComponentModal(
            this.app,
            this.plugin,
            component,
          ).open();
        });
      });
    }

    contentEl.createEl("h3", { text: "Observed-form grouping" });
    contentEl.createEl("p", {
      cls: "tne-muted",
      text: "Automatic grouping is reversible. Use these controls when a short, titled, or similar-looking form is actually a distinct name.",
    });

    for (const form of this.concept.forms) {
      if (this.concept.id === "primary" && form.variantKind === "canonical") {
        continue;
      }
      this.renderFormSetting(contentEl, form);
    }

    const buttons = contentEl.createDiv({ cls: "tne-modal-buttons" });
    const clear = buttons.createEl("button", { text: "Clear concept decision" });
    clear.addEventListener("click", () => void this.clearDecision());
    const save = buttons.createEl("button", {
      text: "Save",
      cls: "mod-cta",
    });
    save.addEventListener("click", () => void this.save());
  }

  renderFormSetting(container, form) {
    const existing = this.catalog.records.find(
      (record) =>
        record.type === "form" &&
        record.subject === this.concept.subjectPath &&
        core.normalizeStrict(record.form) === core.normalizeStrict(form.text),
    );
    let current = "auto";
    if (existing?.action === "separate") current = "separate";
    else if (existing?.action === "group-primary") {
      current = `group-primary:${existing.variantKind || "manual"}`;
    }
    this.formChoices.set(core.normalizeStrict(form.text), {
      form: form.text,
      value: current,
    });

    new Setting(container)
      .setName(form.text)
      .setDesc(`Currently: ${form.variantKind} · ${form.sources.join(", ")}`)
      .addDropdown((dropdown) => {
        addOptions(dropdown, [
          ["auto", "Automatic"],
          ["separate", "Treat as a separate name"],
          ["group-primary:exact", "Group with primary — exact"],
          ["group-primary:titled", "Group with primary — titled"],
          ["group-primary:short", "Group with primary — short"],
          ["group-primary:orthographic", "Group with primary — orthographic"],
          ["group-primary:descriptor", "Group with primary — descriptor"],
          ["group-primary:abbreviation", "Group with primary — abbreviation"],
          ["group-primary:article", "Group with primary — article"],
          ["group-primary:manual", "Group with primary — other"],
        ]);
        dropdown.setValue(current);
        dropdown.onChange((value) => {
          this.formChoices.set(core.normalizeStrict(form.text), {
            form: form.text,
            value,
          });
        });
      });
  }

  async clearDecision() {
    await this.plugin.mutateDecisionStore((records) =>
      records.filter(
        (record) =>
          !(
            record.type === "concept" &&
            record.subject === this.concept.subjectPath &&
            record.concept === this.concept.id
          ),
      )
    );
    this.close();
    await this.plugin.refreshOpenViews();
  }

  async save() {
    const canonicalChoice = this.formChoices.get(
      core.normalizeStrict(this.concept.preferredForm),
    )?.value;
    const groupingCanonical =
      this.concept.id !== "primary" &&
      canonicalChoice?.startsWith("group-primary:");

    await this.plugin.mutateDecisionStore((records) => {
      let next = records.filter(
        (record) =>
          !(
            record.type === "concept" &&
            record.subject === this.concept.subjectPath &&
            record.concept === this.concept.id
          ),
      );

      const conceptRecord = {
        type: "concept",
        subject: this.concept.subjectPath,
        concept: this.concept.id,
        form: this.concept.preferredForm,
      };
      for (const key of [
        "language",
        "relationship",
        "derivation",
        "usage",
        "community",
        "sourceLanguage",
        "sourceForm",
        "notes",
      ]) {
        if (this.values[key]) conceptRecord[key] = this.values[key];
      }
      if (!groupingCanonical && Object.keys(conceptRecord).length > 4) {
        next = core.upsertStoreRecord(next, conceptRecord);
      }

      for (const choice of this.formChoices.values()) {
        const stub = {
          type: "form",
          subject: this.concept.subjectPath,
          form: choice.form,
        };
        next = core.removeStoreRecord(next, stub);
        if (choice.value === "separate") {
          next = core.upsertStoreRecord(next, {
            ...stub,
            action: "separate",
          });
        } else if (choice.value.startsWith("group-primary:")) {
          next = core.upsertStoreRecord(next, {
            ...stub,
            action: "group-primary",
            variantKind: choice.value.split(":")[1],
          });
        }
      }
      return next;
    });

    if (groupingCanonical && Object.values(this.values).some(Boolean)) {
      new Notice("The form was grouped with the primary name; its separate concept decision was not retained.");
    }
    this.close();
    await this.plugin.refreshOpenViews();
  }
}

class RulesModal extends Modal {
  constructor(app, plugin, catalog) {
    super(app);
    this.plugin = plugin;
    this.catalog = catalog;
    this.newRule = {
      label: "",
      noteType: "",
      species: "",
      ancestry: "",
      role: "*",
      componentRole: "",
      inferredLanguage: "",
      folder: "",
      language: "Common",
      priority: 50,
    };
  }

  onOpen() {
    this.modalEl.addClass("tne-modal");
    this.render();
  }

  render() {
    const { contentEl } = this;
    contentEl.empty();
    contentEl.createEl("h2", { text: "Catalog rules" });
    contentEl.createEl("p", {
      cls: "tne-muted",
      text: "Rules apply to current and future matching names. Individual decisions and high-confidence text evidence take precedence over rules.",
    });

    const rules = this.catalog.records
      .filter((record) => record.type === "rule")
      .sort((left, right) => Number(right.priority || 0) - Number(left.priority || 0));
    const list = contentEl.createDiv({ cls: "tne-rule-list" });
    for (const rule of rules) {
      const row = list.createDiv({ cls: "tne-rule-row" });
      const description = row.createDiv();
      description.createEl("strong", { text: rule.label || rule.id });
      description.createEl("p", {
        text: describeRule(rule),
        cls: "tne-muted",
      });
      const enabled = row.createEl("input", { type: "checkbox" });
      enabled.checked = rule.enabled !== false;
      enabled.title = "Enabled";
      enabled.addEventListener("change", async () => {
        await this.plugin.mutateDecisionStore((records) =>
          core.upsertStoreRecord(records, {
            ...rule,
            enabled: enabled.checked,
          })
        );
        this.catalog = await this.plugin.getCatalog(true);
        this.render();
        await this.plugin.refreshOpenViews();
      });
      row.appendChild(iconButton("trash-2", "Delete rule", async () => {
        await this.plugin.mutateDecisionStore((records) =>
          core.removeStoreRecord(records, rule)
        );
        this.catalog = await this.plugin.getCatalog(true);
        this.render();
        await this.plugin.refreshOpenViews();
      }, true));
    }

    contentEl.createEl("h3", { text: "Add a rule" });
    new Setting(contentEl)
      .setName("Label")
      .addText((text) => text.onChange((value) => {
        this.newRule.label = value.trim();
      }));
    new Setting(contentEl)
      .setName("Note type")
      .addDropdown((dropdown) => {
        dropdown.addOption("", "Any");
        for (const noteType of core.NOTE_TYPES) {
          dropdown.addOption(noteType, noteType);
        }
        dropdown.onChange((value) => {
          this.newRule.noteType = value;
        });
      });
    new Setting(contentEl)
      .setName("Species")
      .setDesc("Exact value, case-insensitive; blank matches any.")
      .addText((text) => text.onChange((value) => {
        this.newRule.species = value.trim();
      }));
    new Setting(contentEl)
      .setName("Ancestry")
      .setDesc("Exact value, case-insensitive; blank matches any.")
      .addText((text) => text.onChange((value) => {
        this.newRule.ancestry = value.trim();
      }));
    new Setting(contentEl)
      .setName("Name role")
      .addDropdown((dropdown) => {
        addOptions(dropdown, [
          ["*", "Any"],
          ["primary", "Primary"],
          ["alias", "Alternate"],
          ["text", "Text-derived"],
        ]);
        dropdown.setValue("*");
        dropdown.onChange((value) => {
          this.newRule.role = value;
        });
      });
    new Setting(contentEl)
      .setName("Only when inferred as")
      .addDropdown((dropdown) => {
        dropdown.addOption("", "Any inferred language");
        for (const [, language] of core.LANGUAGE_DEFINITIONS) {
          dropdown.addOption(language, language);
        }
        dropdown.onChange((value) => {
          this.newRule.inferredLanguage = value;
        });
      });
    new Setting(contentEl)
      .setName("Component role")
      .setDesc("Optional; rules are otherwise applied to lexical components only.")
      .addDropdown((dropdown) => {
        dropdown.addOption("", "Any lexical component");
        for (const role of core.COMPONENT_ROLES) {
          dropdown.addOption(role, role);
        }
        dropdown.onChange((value) => {
          this.newRule.componentRole = value;
        });
      });
    new Setting(contentEl)
      .setName("Folder prefix")
      .setDesc("Optional vault-relative prefix.")
      .addText((text) => text.onChange((value) => {
        this.newRule.folder = value.trim();
      }));
    new Setting(contentEl)
      .setName("Assign language")
      .addDropdown((dropdown) => {
        for (const [, language] of core.LANGUAGE_DEFINITIONS) {
          dropdown.addOption(language, language);
        }
        dropdown.setValue("Common");
        dropdown.onChange((value) => {
          this.newRule.language = value;
        });
      });
    new Setting(contentEl)
      .setName("Priority")
      .setDesc("Higher values win when multiple rules match.")
      .addText((text) => {
        text.setValue("50");
        text.inputEl.type = "number";
        text.onChange((value) => {
          this.newRule.priority = Number(value || 0);
        });
      });

    const add = contentEl.createEl("button", {
      text: "Add rule",
      cls: "mod-cta",
    });
    add.addEventListener("click", () => void this.addRule());
  }

  async addRule() {
    if (!this.newRule.label || !this.newRule.language) {
      new Notice("A rule needs a label and assigned language.");
      return;
    }
    const baseId = slugify(this.newRule.label) || "catalog-rule";
    const existingIds = new Set(
      this.catalog.records
        .filter((record) => record.type === "rule")
        .map((record) => record.id),
    );
    let id = baseId;
    let suffix = 2;
    while (existingIds.has(id)) {
      id = `${baseId}-${suffix}`;
      suffix += 1;
    }
    const match = {};
    for (const key of [
      "noteType",
      "species",
      "ancestry",
      "role",
      "componentRole",
      "inferredLanguage",
      "folder",
    ]) {
      if (this.newRule[key] && this.newRule[key] !== "*") {
        match[key] = this.newRule[key];
      }
    }
    const rule = {
      type: "rule",
      id,
      label: this.newRule.label,
      match,
      language: this.newRule.language,
      priority: Number(this.newRule.priority || 0),
      enabled: true,
    };
    await this.plugin.mutateDecisionStore((records) =>
      core.upsertStoreRecord(records, rule)
    );
    this.catalog = await this.plugin.getCatalog(true);
    this.render();
    await this.plugin.refreshOpenViews();
    new Notice(`Added catalog rule “${rule.label}”.`);
  }
}

class OrphansModal extends Modal {
  constructor(app, plugin, catalog) {
    super(app);
    this.plugin = plugin;
    this.catalog = catalog;
  }

  onOpen() {
    this.modalEl.addClass("tne-modal");
    this.render();
  }

  render() {
    const { contentEl } = this;
    contentEl.empty();
    contentEl.createEl("h2", { text: "Orphaned decisions" });
    if (!this.catalog.orphans.length) {
      contentEl.createEl("p", { text: "No orphaned decisions." });
      return;
    }
    contentEl.createEl("p", {
      cls: "tne-muted",
      text: "Orphans are retained rather than silently deleted when source notes or name forms change.",
    });
    for (const orphan of this.catalog.orphans) {
      const row = contentEl.createDiv({ cls: "tne-orphan-row" });
      const details = row.createDiv();
      details.createEl("strong", {
        text: orphan.record.form || orphan.record.subject || orphan.record.concept,
      });
      details.createEl("p", { text: orphan.reason, cls: "tne-muted" });
      details.createEl("code", {
        text: orphan.record.subject || "",
      });
      row.appendChild(iconButton("trash-2", "Delete decision", async () => {
        await this.plugin.mutateDecisionStore((records) =>
          core.removeStoreRecord(records, orphan.record)
        );
        this.catalog = await this.plugin.getCatalog(true);
        this.render();
        await this.plugin.refreshOpenViews();
      }, true));
    }
  }
}

class NameExplorerSettingTab extends PluginSettingTab {
  constructor(app, plugin) {
    super(app, plugin);
    this.plugin = plugin;
  }

  display() {
    const { containerEl } = this;
    containerEl.empty();
    containerEl.createEl("h2", { text: "Taelgar Name Explorer" });

    new Setting(containerEl)
      .setName("Decision store")
      .setDesc("Vault-relative JSONL file for rules and reviewed decisions.")
      .addText((text) => {
        text.setValue(this.plugin.settings.decisionStorePath);
        text.inputEl.addEventListener("change", async () => {
          const value = text.getValue();
          this.plugin.settings.decisionStorePath =
            value.trim() || DEFAULT_SETTINGS.decisionStorePath;
          await this.plugin.saveSettings();
          await this.plugin.ensureDecisionStore();
        });
      });

    new Setting(containerEl)
      .setName("Export path")
      .setDesc("Vault-relative path for a complete, disposable catalog export.")
      .addText((text) => {
        text.setValue(this.plugin.settings.exportPath);
        text.inputEl.addEventListener("change", async () => {
          const value = text.getValue();
          this.plugin.settings.exportPath =
            value.trim() || DEFAULT_SETTINGS.exportPath;
          await this.plugin.saveSettings();
        });
      });

    new Setting(containerEl)
      .setName("Place evidence")
      .setDesc("Vault-relative JSONL file generated by the place-name analyzer.")
      .addText((text) => {
        text.setValue(this.plugin.settings.placeEvidencePath);
        text.inputEl.addEventListener("change", async () => {
          const value = text.getValue();
          this.plugin.settings.placeEvidencePath =
            value.trim() || DEFAULT_SETTINGS.placeEvidencePath;
          await this.plugin.saveSettings();
          await this.plugin.refreshOpenViews();
        });
      });

    new Setting(containerEl)
      .setName("Scan text evidence")
      .setDesc("Read high-confidence, form-bound naming statements and conservative text-derived aliases. Disabling this makes indexing faster.")
      .addToggle((toggle) => {
        toggle.setValue(this.plugin.settings.scanTextEvidence);
        toggle.onChange(async (value) => {
          this.plugin.settings.scanTextEvidence = value;
          await this.plugin.saveSettings();
          await this.plugin.refreshOpenViews();
        });
      });

    new Setting(containerEl)
      .setName("Rows per page")
      .addDropdown((dropdown) => {
        addOptions(dropdown, [
          ["50", "50"],
          ["100", "100"],
          ["250", "250"],
          ["500", "500"],
        ]);
        dropdown.setValue(String(this.plugin.settings.pageSize));
        dropdown.onChange(async (value) => {
          this.plugin.settings.pageSize = Number(value);
          await this.plugin.saveSettings();
          await this.plugin.refreshOpenViews();
        });
      });
  }
}

function summarizeCatalog(catalog) {
  return {
    concepts: catalog.concepts.length,
    forms: catalog.concepts.reduce(
      (total, concept) => total + concept.forms.length,
      0,
    ),
    components: catalog.components.length,
    corpus: catalog.corpus.length,
    nameReview: catalog.concepts.filter(
      (concept) => concept.needsNameReview,
    ).length,
    placeEvidence: catalog.placeEvidence?.records?.length || 0,
    overridden: catalog.concepts.filter(
      (concept) => concept.status === "overridden",
    ).length,
    unknown: catalog.concepts.filter((concept) =>
      ["unknown", "reviewed-unknown"].includes(concept.status)
    ).length,
  };
}

function conceptKey(concept) {
  return `${concept.subjectPath}\u0000${concept.id}`;
}

function subtypeOptions(catalog, noteType = "") {
  return core.subtypeChoices(catalog.subjects, noteType).map((subtype) => [
    subtype,
    subtype,
  ]);
}

function makeSelect(options, value, onChange, label) {
  const select = document.createElement("select");
  select.className = "dropdown";
  if (label) select.setAttribute("aria-label", label);
  for (const [optionValue, optionLabel] of options) {
    const option = document.createElement("option");
    option.value = optionValue;
    option.textContent = optionLabel;
    select.appendChild(option);
  }
  select.value = value;
  select.addEventListener("change", () => onChange(select.value));
  return select;
}

function iconButton(iconName, label, onClick, iconOnly = false) {
  const button = document.createElement("button");
  button.className = iconOnly ? "clickable-icon" : "tne-icon-button";
  button.setAttribute("aria-label", label);
  button.title = label;
  const icon = document.createElement("span");
  setIcon(icon, iconName);
  button.appendChild(icon);
  if (!iconOnly) {
    const text = document.createElement("span");
    text.textContent = label;
    button.appendChild(text);
  }
  button.addEventListener("click", onClick);
  return button;
}

function languageChip(language, source) {
  const chip = document.createElement("span");
  chip.className = `tne-language-chip source-${source}`;
  chip.textContent = language;
  chip.title = `Language source: ${source}`;
  return chip;
}

function humanizeEvidenceValue(value) {
  return String(value || "")
    .split("-")
    .filter(Boolean)
    .map((part, index) => index ? part : part[0]?.toUpperCase() + part.slice(1))
    .join(" ");
}

function embeddednessLabel(embeddedness) {
  if (!embeddedness) return "—";
  const percentile = embeddedness.percentile_all_places;
  const percentage = typeof percentile === "number"
    ? ` · ${Math.round(percentile * 100)}%`
    : "";
  return `${humanizeEvidenceValue(embeddedness.band)}${percentage}`;
}

function campaignEvidenceLabel(campaigns) {
  if (!campaigns.length) return "—";
  return campaigns
    .slice()
    .sort((left, right) =>
      (right.session_count || 0) - (left.session_count || 0) ||
      left.campaign.localeCompare(right.campaign)
    )
    .slice(0, 3)
    .map((campaign) =>
      `${campaign.campaign} ${campaign.session_count || "context"}`
    )
    .join(" · ");
}

function statusChip(status) {
  const labels = {
    "reviewed-unknown": "Reviewed unknown",
    overridden: "Overridden",
    confirmed: "Confirmed",
    rule: "Rule",
    "text-evidence": "Text evidence",
    conflict: "Conflict",
    convention: "Trade convention",
    structural: "Structural",
    inferred: "Inferred",
    unknown: "Unknown",
  };
  const chip = document.createElement("span");
  chip.className = `tne-status-chip status-${status}`;
  chip.textContent = labels[status] || status;
  return chip;
}

function nameReviewReasonLabels(reasons) {
  const labels = {
    "status/check/name": "tagged status/check/name",
    "provisional-name-marker": "primary name is wrapped in ~",
  };
  return (reasons || []).map((reason) => labels[reason] || reason);
}

function nameReviewChip(reasons) {
  const chip = document.createElement("span");
  chip.className = "tne-name-review-chip";
  chip.textContent = "Name check";
  chip.title = `Potential naming issue: ${nameReviewReasonLabels(reasons).join(
    "; ",
  )}`;
  return chip;
}

function addOptions(dropdown, options) {
  for (const [value, label] of options) dropdown.addOption(value, label);
  return dropdown;
}

function describeRule(rule) {
  const match = rule.match || {};
  const conditions = [];
  if (match.noteType) conditions.push(`type ${match.noteType}`);
  if (match.species) conditions.push(`species ${match.species}`);
  if (match.ancestry) conditions.push(`ancestry ${match.ancestry}`);
  if (match.role && match.role !== "*") conditions.push(`role ${match.role}`);
  if (match.componentRole) {
    conditions.push(`component ${match.componentRole}`);
  }
  if (match.inferredLanguage) {
    conditions.push(`inferred ${match.inferredLanguage}`);
  }
  if (match.folder) conditions.push(`folder ${match.folder}`);
  return `${conditions.join(" · ") || "all names"} → ${rule.language} · priority ${rule.priority || 0}`;
}

function slugify(value) {
  return core.normalizeLoose(value).replace(/\s+/g, "-").replace(/^-+|-+$/g, "");
}

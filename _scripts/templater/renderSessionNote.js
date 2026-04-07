const COMPONENT_FILENAMES = [
    "01-session-info.md",
    "02-technical-updates.md",
    "03-narrative.md",
];

function splitFrontmatter(text) {
    const lines = text.split(/\r?\n/);
    if (!lines.length || lines[0].trim() !== "---") {
        return { frontmatterText: "", bodyText: text };
    }

    for (let index = 1; index < lines.length; index += 1) {
        if (lines[index].trim() === "---") {
            return {
                frontmatterText: lines.slice(0, index + 1).join("\n"),
                bodyText: lines.slice(index + 1).join("\n"),
            };
        }
    }

    return { frontmatterText: "", bodyText: text };
}

function stripYamlScalar(value) {
    const trimmed = String(value ?? "").trim();
    if (!trimmed) {
        return "";
    }
    if ((trimmed.startsWith('"') && trimmed.endsWith('"')) || (trimmed.startsWith("'") && trimmed.endsWith("'"))) {
        return trimmed.slice(1, -1);
    }
    return trimmed;
}

function parseSessionNoteConfig(sessionManifestText) {
    const match = sessionManifestText.match(/^sessionNote:\s*$(?<block>(?:\r?\n[ \t]+.*)+)/m);
    if (!match || !match.groups || !match.groups.block) {
        throw new Error("session.yaml is missing a parseable sessionNote block.");
    }

    const config = {};
    for (const rawLine of match.groups.block.split(/\r?\n/)) {
        const trimmed = rawLine.trim();
        if (!trimmed || trimmed.startsWith("#")) {
            continue;
        }
        const entryMatch = trimmed.match(/^([A-Za-z0-9_.-]+):\s*(.*)$/);
        if (!entryMatch) {
            continue;
        }
        config[entryMatch[1]] = stripYamlScalar(entryMatch[2]);
    }

    for (const key of ["templatePath", "generatedRoot", "publishedNotePath"]) {
        if (!config[key]) {
            throw new Error(`sessionNote.${key} is required in session.yaml.`);
        }
    }

    return config;
}

function normalizeVaultPath(inputPath) {
    const normalized = String(inputPath ?? "").trim().replace(/\\/g, "/");
    if (!normalized) {
        throw new Error("Encountered an empty path while rendering the session note.");
    }

    if (!normalized.startsWith("/")) {
        return normalized;
    }

    const basePath = String(app.vault.adapter.basePath ?? "").trim().replace(/\\/g, "/");
    if (!basePath) {
        throw new Error(`Cannot resolve absolute vault path without adapter.basePath: ${normalized}`);
    }
    if (normalized === basePath) {
        return "";
    }
    if (normalized.startsWith(`${basePath}/`)) {
        return normalized.slice(basePath.length + 1);
    }
    throw new Error(`Path is outside the current vault: ${normalized}`);
}

function joinVaultPaths(...parts) {
    return parts
        .filter(Boolean)
        .map((part) => String(part).replace(/\\/g, "/").replace(/^\/+|\/+$/g, ""))
        .filter(Boolean)
        .join("/");
}

function stemFromPath(inputPath) {
    const normalized = String(inputPath).replace(/\\/g, "/");
    const basename = normalized.split("/").pop() ?? normalized;
    return basename.endsWith(".md") ? basename.slice(0, -3) : basename;
}

function slugifyText(value) {
    const slug = String(value ?? "")
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, "-")
        .replace(/^-+|-+$/g, "");
    return slug || "session-note";
}

function extractSlots(markdownText, sourcePath) {
    const slotPattern = /<!-- SLOT: ([A-Za-z0-9._-]+) -->([\s\S]*?)<!-- \/SLOT -->/g;
    const slots = {};
    let match = slotPattern.exec(markdownText);

    while (match) {
        const slotName = match[1];
        if (Object.prototype.hasOwnProperty.call(slots, slotName)) {
            throw new Error(`Duplicate slot '${slotName}' found in ${sourcePath}.`);
        }
        slots[slotName] = match[2].replace(/^\n+/, "").replace(/\n+$/, "");
        match = slotPattern.exec(markdownText);
    }

    return slots;
}

function mergeSlots(target, incoming, sourcePath) {
    for (const [slotName, slotBody] of Object.entries(incoming)) {
        if (Object.prototype.hasOwnProperty.call(target, slotName)) {
            throw new Error(`Slot '${slotName}' was defined more than once while loading ${sourcePath}.`);
        }
        target[slotName] = slotBody;
    }
}

function renderTemplate(templateText, slots) {
    const templateBody = splitFrontmatter(templateText).bodyText.replace(/^\n+/, "");
    const placeholderPattern = /\{([A-Za-z0-9._-]+)\}/g;
    const referencedSlots = new Set();
    let match = placeholderPattern.exec(templateBody);

    while (match) {
        referencedSlots.add(match[1]);
        match = placeholderPattern.exec(templateBody);
    }

    for (const slotName of referencedSlots) {
        if (!Object.prototype.hasOwnProperty.call(slots, slotName)) {
            throw new Error(`Template references unknown or missing slot '{${slotName}}'.`);
        }
    }

    return templateBody.replace(placeholderPattern, (_fullMatch, slotName) => slots[slotName]);
}

async function readVaultText(vaultPath, label) {
    const normalizedPath = normalizeVaultPath(vaultPath);
    const target = app.vault.getAbstractFileByPath(normalizedPath);
    if (!target || !target.path) {
        throw new Error(`${label} not found at ${normalizedPath}.`);
    }
    return app.vault.adapter.read(target.path);
}

async function renderSessionNote(tp) {
    try {
        const currentFile = app.workspace.getActiveFile();
        if (!currentFile) {
            throw new Error("No active file is open.");
        }

        const cache = app.metadataCache.getFileCache(currentFile) ?? {};
        const frontmatter = cache.frontmatter ?? {};
        if (typeof frontmatter.sessionManifest !== "string" || !frontmatter.sessionManifest.trim()) {
            throw new Error("Current note frontmatter must include sessionManifest.");
        }

        const currentText = await app.vault.adapter.read(currentFile.path);
        const currentParts = splitFrontmatter(currentText);
        const sessionManifestText = await readVaultText(frontmatter.sessionManifest, "Session manifest");
        const sessionNote = parseSessionNoteConfig(sessionManifestText);

        const publishedStem = stemFromPath(sessionNote.publishedNotePath);
        const componentDir = joinVaultPaths(sessionNote.generatedRoot, slugifyText(publishedStem));
        const slots = {};

        const templateText = await readVaultText(sessionNote.templatePath, "Session note template");
        for (const componentFilename of COMPONENT_FILENAMES) {
            const componentPath = joinVaultPaths(componentDir, componentFilename);
            const componentText = await readVaultText(componentPath, "Session note component");
            mergeSlots(slots, extractSlots(componentText, componentPath), componentPath);
        }

        const renderedBody = renderTemplate(templateText, slots).replace(/\s+$/, "");
        const output = currentParts.frontmatterText
            ? `${currentParts.frontmatterText}\n\n${renderedBody}\n`
            : `${renderedBody}\n`;

        await app.vault.adapter.write(currentFile.path, output);
        new Notice(`Rendered session note from ${sessionNote.templatePath}.`);
        return "";
    } catch (error) {
        console.error(error);
        new Notice(`Session note render failed: ${error.message}`, 10000);
        throw error;
    }
}

module.exports = renderSessionNote;
module.exports._test = {
    extractSlots,
    joinVaultPaths,
    parseSessionNoteConfig,
    renderTemplate,
    slugifyText,
    splitFrontmatter,
    stemFromPath,
};

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

function extractFrontmatterBody(frontmatterText) {
    if (!frontmatterText) {
        return "";
    }
    const lines = frontmatterText.split(/\r?\n/);
    if (lines.length < 2 || lines[0].trim() !== "---") {
        return "";
    }
    const bodyLines = lines.slice(1);
    if (bodyLines.length && bodyLines[bodyLines.length - 1].trim() === "---") {
        bodyLines.pop();
    }
    return bodyLines.join("\n");
}

function parseFrontmatterChunks(frontmatterText) {
    const body = extractFrontmatterBody(frontmatterText);
    if (!body.trim()) {
        return [];
    }

    const chunks = [];
    let currentChunk = null;
    for (const line of body.split(/\r?\n/)) {
        const keyMatch = line.match(/^([A-Za-z0-9_.-]+):(?:\s|$)/);
        if (keyMatch) {
            if (currentChunk) {
                chunks.push(currentChunk);
            }
            currentChunk = { key: keyMatch[1], lines: [line] };
            continue;
        }
        if (!currentChunk) {
            continue;
        }
        currentChunk.lines.push(line);
    }
    if (currentChunk) {
        chunks.push(currentChunk);
    }
    return chunks;
}

function stringifyFrontmatterChunks(chunks) {
    if (!chunks.length) {
        return "";
    }
    return ["---", ...chunks.flatMap((chunk) => chunk.lines), "---"].join("\n");
}

function mergeFrontmatter(templateFrontmatterText, currentFrontmatterText) {
    const templateChunks = parseFrontmatterChunks(templateFrontmatterText);
    const currentChunks = parseFrontmatterChunks(currentFrontmatterText);
    const mergedChunks = [];
    const seenKeys = new Set();

    for (const chunk of templateChunks) {
        mergedChunks.push(chunk);
        seenKeys.add(chunk.key);
    }

    for (const chunk of currentChunks) {
        if (seenKeys.has(chunk.key)) {
            continue;
        }
        mergedChunks.push(chunk);
        seenKeys.add(chunk.key);
    }
    return stringifyFrontmatterChunks(mergedChunks);
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

function buildComponentDirName(sessionNoteConfig, sessionManifestPath) {
    return String(sessionNoteConfig.sessionKey ?? "").trim();
}

function resolveTemplatePath(templateValue) {
    const template = String(templateValue ?? "").trim();
    if (!template) {
        throw new Error("Current note frontmatter must include template.");
    }
    if (template.includes("/") || template.includes("\\")) {
        return normalizeVaultPath(template);
    }
    return joinVaultPaths("_templates", "session-notes", template.endsWith(".md") ? template : `${template}.md`);
}

function inferGeneratedRootFromNotePath(notePath) {
    const normalized = normalizeVaultPath(notePath);
    const parts = normalized.split("/").filter(Boolean);
    const campaignsIndex = parts.indexOf("Campaigns");
    if (campaignsIndex === -1 || campaignsIndex + 1 >= parts.length) {
        throw new Error(`Cannot infer campaign root from note path: ${normalized}`);
    }

    const noteContainerNames = new Set(["Sessions", "Session Notes", "Episodes"]);
    for (let index = campaignsIndex + 1; index < parts.length - 1; index += 1) {
        if (noteContainerNames.has(parts[index])) {
            return joinVaultPaths(...parts.slice(0, index), "_generated", "session-notes");
        }
    }

    if (parts[campaignsIndex + 1] === "One Shots" && campaignsIndex + 2 < parts.length - 1) {
        return joinVaultPaths(...parts.slice(0, campaignsIndex + 3), "_generated", "session-notes");
    }

    return joinVaultPaths(...parts.slice(0, campaignsIndex + 2), "_generated", "session-notes");
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

function renderPlaceholders(text, slots) {
    const sourceText = String(text ?? "");
    const placeholderPattern = /\{([A-Za-z0-9._-]+)\}/g;
    const referencedSlots = new Set();
    let match = placeholderPattern.exec(sourceText);

    while (match) {
        referencedSlots.add(match[1]);
        match = placeholderPattern.exec(sourceText);
    }

    for (const slotName of referencedSlots) {
        if (!Object.prototype.hasOwnProperty.call(slots, slotName)) {
            throw new Error(`Template references unknown or missing slot '{${slotName}}'.`);
        }
    }

    return sourceText.replace(placeholderPattern, (_fullMatch, slotName) => slots[slotName]);
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
        if (typeof frontmatter.sessionKey !== "string" || !frontmatter.sessionKey.trim()) {
            throw new Error("Current note frontmatter must include sessionKey.");
        }

        const currentText = await app.vault.adapter.read(currentFile.path);
        const currentParts = splitFrontmatter(currentText);
        const templatePath = resolveTemplatePath(frontmatter.template);
        const generatedRoot = inferGeneratedRootFromNotePath(currentFile.path);
        const componentDir = joinVaultPaths(generatedRoot, buildComponentDirName(frontmatter));
        const slots = {};

        const templateText = await readVaultText(templatePath, "Session note template");
        for (const componentFilename of COMPONENT_FILENAMES) {
            const componentPath = joinVaultPaths(componentDir, componentFilename);
            const componentText = await readVaultText(componentPath, "Session note component");
            mergeSlots(slots, extractSlots(componentText, componentPath), componentPath);
        }

        const renderedTemplate = renderPlaceholders(templateText, slots);
        const templateParts = splitFrontmatter(renderedTemplate);
        const renderedBody = templateParts.bodyText
            .replace(/^(?:[ \t]*\r?\n)+/, "")
            .replace(/(?:\r?\n[ \t]*)+$/, "");
        const mergedFrontmatter = mergeFrontmatter(templateParts.frontmatterText, currentParts.frontmatterText);
        const normalizedFrontmatter = mergedFrontmatter.replace(/\s+$/, "");
        const normalizedBody = renderedBody.replace(/^\s+/, "").replace(/\s+$/, "");
        const output = normalizedFrontmatter
            ? `${normalizedFrontmatter}\n${normalizedBody}\n`
            : `${normalizedBody}\n`;

        await app.vault.adapter.write(currentFile.path, output);
        new Notice(`Rendered session note from ${templatePath}.`);
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
    inferGeneratedRootFromNotePath,
    joinVaultPaths,
    mergeFrontmatter,
    parseFrontmatterChunks,
    buildComponentDirName,
    resolveTemplatePath,
    renderPlaceholders,
    slugifyText,
    splitFrontmatter,
    stemFromPath,
    stringifyFrontmatterChunks,
};

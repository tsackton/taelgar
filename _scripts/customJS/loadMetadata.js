class init {
    normalizeCampaignRegistry(payload) {
        const entries = payload?.campaigns
        if (!entries || Array.isArray(entries) || typeof entries !== "object") {
            throw new Error("Campaign registry must contain a campaigns object")
        }

        const normalized = []
        const codes = new Set()

        for (const [slug, raw] of Object.entries(entries)) {
            if (!raw || Array.isArray(raw) || typeof raw !== "object") {
                throw new Error(`Campaign ${slug} must be an object`)
            }

            const name = String(raw.name ?? "").trim()
            const code = String(raw.code ?? "").trim()
            const campaignRoot = String(raw.campaignRoot ?? "").trim().replace(/\/$/, "")
            const notePattern = String(raw.notePattern ?? "").trim()

            if (!name || !code) {
                throw new Error(`Campaign ${slug} must define name and code`)
            }
            if (codes.has(code.toLowerCase())) {
                throw new Error(`Campaign code ${code} is duplicated`)
            }
            codes.add(code.toLowerCase())

            const lastSlash = notePattern.lastIndexOf("/")
            const relativeSessionFolder = lastSlash >= 0 ? notePattern.slice(0, lastSlash) : ""
            const sessionNoteFolder = [campaignRoot, relativeSessionFolder]
                .filter(Boolean)
                .join("/")

            normalized.push({
                ...raw,
                slug,
                name,
                code,
                aliases: Array.isArray(raw.aliases) ? raw.aliases : [],
                sessionNoteFolder
            })
        }

        return normalized
    }

    async invoke() {
        const metadataFilePath = app.vault.configDir + "/metadata.json";
        const [metadataFile, indexFile] = await Promise.all([
            app.vault.adapter.read(metadataFilePath),
            app.vault.adapter.read("_sessions/campaign-registry.json")
        ])
        const index = JSON.parse(indexFile)
        if (!index || typeof index !== "object" || Array.isArray(index) || !Object.keys(index).length) {
            throw new Error("Expected a nonempty campaign index")
        }
        const entries = Object.create(null)
        const seenPaths = new Set()
        for (const [id, path] of Object.entries(index)) {
            if (!/^[a-z][a-z0-9]*$/.test(id) || typeof path !== "string" || !path.endsWith(".md") ||
                path.split("/").some(part => !part || part === ".." || part === ".") || seenPaths.has(path)) {
                throw new Error(id + ": invalid or duplicate index path " + path)
            }
            const file = app.vault.getAbstractFileByPath(path)
            const fields = file && app.metadataCache.getFileCache(file)?.frontmatter
            if (typeof fields?.name !== "string" || !fields.name.trim()) {
                throw new Error(id + ": missing index note or name in " + path)
            }
            seenPaths.add(path)
            entries[id] = {
                name: fields.name, code: id, campaignRoot: fields.campaignDirectory,
                notePattern: fields.notePattern, partyPage: fields.partyPage?.replace(/\.md$/, "")
            }
        }
        const coreMeta = JSON.parse(metadataFile)
        const campaignRegistry = this.normalizeCampaignRegistry({ campaigns: entries })
        coreMeta.campaigns = campaignRegistry
        customJS.state.coreMeta = coreMeta
        customJS.state.campaignRegistry = campaignRegistry
    }
}

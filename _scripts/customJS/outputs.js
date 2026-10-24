class OutputHandler {

    outputCampaignInteractions(fileName, page, campaignFilter) {
        // Intended for use from Dataview views (dv.current()) where file inlinks exist.
        // Produces a compact, stable summary so NPC pages don't need campaignInfo logs.

        const { DateManager, NameManager } = customJS

        const maxOtherMentions = 0 // 0 = no limit

        const normalizeStringList = (value) => {
            if (!value) return []
            if (Array.isArray(value)) return value.filter(v => typeof v === "string" && v.trim().length > 0)
            if (typeof value === "string" || value instanceof String) return [String(value)]
            return []
        }

        const normalizeTags = (value) => normalizeStringList(value).map(t => t.replace(/^#/, "").trim().toLowerCase())

        const getCoreCampaigns = () => {
            let campaigns = customJS?.state?.coreMeta?.campaigns
            return Array.isArray(campaigns) ? campaigns : []
        }

        const coreCampaigns = getCoreCampaigns()
        const knownTo = normalizeStringList(page?.knownTo).map(s => s.trim())

        const inlinks = page?.file?.inlinks ?? []
        if (!Array.isArray(inlinks) || inlinks.length === 0) {
            return `_No session-note links found._`
        }

        const isSessionNote = (linkedPage) => {
            if (!linkedPage?.file?.path) return false

            const tags = normalizeTags(linkedPage.tags ?? linkedPage.file?.tags ?? linkedPage.file?.etags)
            if (tags.includes("session-note")) return true

            // Fall back to configured session-note folders.
            for (let c of coreCampaigns) {
                if (c?.sessionNoteFolder && linkedPage.file.path.startsWith(c.sessionNoteFolder)) return true
            }

            // Common convention even when metadata.json isn't fully configured.
            return linkedPage.file.path.includes("/Session Notes/") || linkedPage.file.path.includes("/Sessions/")
        }

        const inferCampaignCode = (linkedPage) => {
            let path = linkedPage?.file?.path ?? ""

            for (let c of coreCampaigns) {
                if (c?.sessionNoteFolder && path.startsWith(c.sessionNoteFolder)) return (c.code ?? c.prefix)
            }

            // Session file names often end with "(DuFr)" style codes.
            let name = linkedPage?.file?.name ?? ""
            let m = name.match(/\(([^)]+)\)\s*$/)
            if (m && m[1]) {
                let cfg = NameManager.getCampaignConfig(m[1].trim())
                return cfg?.code ?? m[1].trim()
            }

            // Try any parens group if not at end.
            m = name.match(/\(([^)]+)\)/)
            if (m && m[1]) {
                let cfg = NameManager.getCampaignConfig(m[1].trim())
                return cfg?.code ?? m[1].trim()
            }

            // Fall back to campaign field if present (try to map to a known prefix).
            if (linkedPage.campaign) {
                let campaignName = String(linkedPage.campaign).trim()
                let cfg = NameManager.getCampaignConfig(campaignName)
                return cfg?.code ?? campaignName
            }

            return "Unknown"
        }

        const fmtSessionLink = (linkedPage) => {
            // Prefer a descTitle alias if present: [[Session X|Hyena Rampage]]
            let name = linkedPage?.file?.name ?? ""
            if (!name) return ""

            let alias = linkedPage?.descTitle
            if (alias && (typeof alias === "string" || alias instanceof String) && alias.trim().length > 0) {
                return `[[${name}|${alias.trim()}]]`
            }

            return `[[${name}]]`
        }

        let sessionEntries = []

        for (let link of inlinks) {
            let path = (typeof link === "string" || link instanceof String) ? String(link) : link?.path
            if (!path) continue

            let linkedPage = DataviewAPI.page(path)
            if (!linkedPage) continue
            if (!isSessionNote(linkedPage)) continue

            let campaign = inferCampaignCode(linkedPage)

            let dateRaw = linkedPage.DR ?? linkedPage.dr ?? linkedPage.DR_start ?? linkedPage.DR_end
            let date = undefined
            try {
                if (dateRaw) date = DateManager.normalizeDate(dateRaw, false)
            } catch (e) {
                date = undefined
            }

            let sort = date?.sort ?? Number.MAX_SAFE_INTEGER
            sessionEntries.push({
                campaign,
                linkedPage,
                date,
                sort
            })
        }

        if (sessionEntries.length === 0) {
            return `_No session-note links found._`
        }

        let canonicalFilter = undefined
        if (campaignFilter && (typeof campaignFilter === "string" || campaignFilter instanceof String)) {
            let cfg = NameManager.getCampaignConfig(campaignFilter)
            canonicalFilter = (cfg?.code ?? String(campaignFilter)).trim()
        }

        if (canonicalFilter) {
            sessionEntries = sessionEntries.filter(e => (e.campaign ?? "").toString().toLowerCase() === canonicalFilter.toLowerCase())
            if (sessionEntries.length === 0) return `_No session-note links found._`
        }

        // Group by campaign, then sort within each campaign.
        let byCampaign = new Map()
        for (let e of sessionEntries) {
            let key = e.campaign ?? "Unknown"
            if (!byCampaign.has(key)) byCampaign.set(key, [])
            byCampaign.get(key).push(e)
        }

        let campaignKeys = Array.from(byCampaign.keys()).sort((a, b) => String(a).localeCompare(String(b)))

        let out = ""
        for (let key of campaignKeys) {
            let entries = byCampaign.get(key) ?? []
            entries.sort((a, b) => {
                if (a.sort !== b.sort) return a.sort - b.sort
                // Stable tie-breakers.
                let an = a.linkedPage?.file?.name ?? ""
                let bn = b.linkedPage?.file?.name ?? ""
                return String(an).localeCompare(String(bn))
            })

            let first = entries[0]
            let last = entries[entries.length - 1]

            let campaignCode = String(key)

            let partyLabel = campaignCode
            try {
                let cfg = NameManager.getCampaignConfig(campaignCode)
                if (cfg?.partyPage) partyLabel = `[[${cfg.partyPage}]]`
            } catch (e) {
                // ignore
            }

            out += `### ${partyLabel}\n`

            let missingForKnownTo = !knownTo.some(x => x.toLowerCase() === campaignCode.toLowerCase())
            if (missingForKnownTo) out += `Suggested knownTo: ${campaignCode}\n`

            out += `First encountered: ${fmtSessionLink(first.linkedPage)}\n`
            if (entries.length > 1) out += `Most recent encounter: ${fmtSessionLink(last.linkedPage)}\n`

            let others = entries.slice(1, Math.max(1, entries.length - 1))
            if (entries.length > 2) {
                if (maxOtherMentions > 0) others = others.slice(Math.max(0, others.length - maxOtherMentions))

                out += "Other mentions:\n"
                for (let e of others) {
                    out += `- ${fmtSessionLink(e.linkedPage)}\n`
                }
            }

            out += "\n"
        }

        return out.trim()
    }

}

class OutputHandler {

    outputWhereabouts(fileName, metadata) {
        let vals = this.getWhereaboutsStrings(fileName, metadata)
        let displayString = `${vals.origin}${vals.home}${vals.current}${vals.lastKnown}`

        if (vals.secondary && vals.secondary.trim()) {
            displayString += "\n" + vals.secondary
        }

        return displayString.replace(/\n\n+/g, "\n");
    }

    getWhereaboutsStrings(fileName, metadata) {

        const { WhereaboutsManager } = customJS
        const { DateManager } = customJS
        const { NameManager } = customJS
        const { TokenParser } = customJS

        let strVals = { home: "", origin: "", lastKnown: "", current: "", isCurrentUnknown: false }
        let pageMetadata = metadata?.file?.frontmatter ?? metadata ?? {}

        // Dataview page objects include inline fields such as DR and DR_end from body text.
        // Those are timeline facts, not page lifecycle dates for whereabouts rendering.
        if (metadata?.file && !pageMetadata.tags) {
            let fileTags = metadata.file.tags ?? metadata.file.etags
            if (Array.isArray(fileTags)) {
                pageMetadata = {
                    ...pageMetadata,
                    tags: fileTags.map(t => typeof t === "string" ? t.replace(/^#/, "") : t)
                }
            }
        }

        let displayDefaults = NameManager.getDisplayData(pageMetadata)
        let file = { name: fileName, frontmatter: pageMetadata }

        let pageData = DateManager.getPageDates(pageMetadata);
        let pageYear = DateManager.getTargetDateForPage(pageMetadata)

        if (!pageData.isCreated) return strVals;

        let isPageAlive = pageData.isAlive

        // if page is dead/destroyed, get whereabouts as of died/destroyed date //
        // if we want to allow dead bodies to move around, would need to change this //
        // however, currently don't have a good location to track "Died at" so might be complicated //
        // but commenting to track for the future //
        if (!isPageAlive) pageYear = pageData.endDate

        let whereabout = WhereaboutsManager.getWhereabouts(pageMetadata, pageYear)

        let homeString = ""

        // knownLastKnown is false if either we have no awayEnd, or if the awayEnd is a hidden date (0001 or 9999)
        let knownLastKnown = whereabout.lastKnown.awayEnd && !whereabout.lastKnown.awayEnd.isHiddenDate

        let homeOverrides = undefined
        let originOverrides = undefined
        if (whereabout.home.location) {

            let dateInfo = {
                startDate: whereabout.home.start ?? pageData.startDate ?? whereabout.home.logicalStart,
                endDate: whereabout.home.end ?? pageData.endDate ?? whereabout.home.logicalEnd,
                isCreated: true,
                isAlive: undefined,
                age: undefined
            }

            DateManager.setPageDateProperties(dateInfo, pageYear)

            homeOverrides = {
                dateInfo: dateInfo
            }
        }

        if (whereabout.origin.location) {
            let dateInfo = {
                startDate: whereabout.origin.start ?? pageData.startDate ?? whereabout.origin.logicalStart,
                endDate: whereabout.origin.end ?? pageData.endDate ?? whereabout.origin.logicalEnd,
                isCreated: true,
                isAlive: undefined,
                age: undefined
            }

            DateManager.setPageDateProperties(dateInfo, pageYear)

            originOverrides = {
                dateInfo: dateInfo
            }
        }

        // origin string construction //
        // if origin is unknown, use unknown string //
        // don't care about alive/dead for origin //
        let originString = TokenParser.formatDisplayString(whereabout.origin.location ? (whereabout.origin.originFormat ?? displayDefaults.wOrigin) : displayDefaults.wOriginU, file, pageYear, originOverrides)

        // home string construction //
        if (isPageAlive) {
            homeString = TokenParser.formatDisplayString(whereabout.home.location ? (whereabout.home.homeFormat ?? displayDefaults.wHome) : displayDefaults.wHomeU, file, pageYear, homeOverrides)
        } else {
            homeString = TokenParser.formatDisplayString(whereabout.home.location ? (whereabout.home.pastHomeFormat ?? displayDefaults.wPastHome) : displayDefaults.wPastHomeU, file, pageYear, homeOverrides)
        }

        // current string construction //    
        let currentString = TokenParser.formatDisplayString((isPageAlive ? (whereabout.current.currentFormat ?? displayDefaults.wCurrent) : (whereabout.current.pastFormat ?? displayDefaults.wPast)), file, pageYear)

        // last known string construction //
        let knownString = TokenParser.formatDisplayString(knownLastKnown ? (whereabout.lastKnown.lastKnownFormat ?? displayDefaults.wLastKnown) : (whereabout.lastKnown.lastKnownFormat ?? displayDefaults.wLastNoDate), file, pageYear)


        if (!whereabout.origin.location || whereabout.origin.location != whereabout.home.location) {
            // display origin if it is not the same as home or it is unknown //
            strVals.origin = originString + "\n"
        }

        // always display home
        if (whereabout.home.location)
            strVals.home = homeString + "\n"

        if (!whereabout.current.location || whereabout.current.location != whereabout.home.location) {
            // display current if it is not the same as home or if current is unknown //
            strVals.current = currentString + "\n"
            strVals.isCurrentUnknown = !whereabout.current.location
        }

        if (!whereabout.current.location && whereabout.lastKnown.location && whereabout.lastKnown.location != whereabout.home.location) {
            // display last known if current is unknown and last known is known, as long as it isn't the same as home //        
            // note it is not clear last known can ever be same as home but this is added to just double-confirm we don't show 2x of the same thing //
            strVals.lastKnown = knownString + "\n"
        }

        if (whereabout.secondary.location) {
            strVals.secondary = TokenParser.formatDisplayString(whereabout.secondary.secondaryFormat ?? displayDefaults.wSecondary, file, pageData)
        } else {
            strVals.secondary = ""
        }

        // remove extra newlines //
        return strVals;
    }

    outputAffiliations(fileName, metadata) {
        const { AffiliationManager } = customJS

        let leadBy = AffiliationManager.getLeadBy(fileName)
        return (leadBy + "\n" + AffiliationManager.getFormattedNonPrimaryAffiliations(metadata)).trim()
    }


    outputPageDatedValue(fileName, metadata) {
        function isDisplayableDate(date) {
            return date && !date.isHiddenDate
        }

        const { DateManager } = customJS
        const { TokenParser } = customJS
        const { NameManager } = customJS

        let frontmatter = metadata?.file?.frontmatter ?? metadata ?? {}
        let dateInfo = DateManager.getPageDates(metadata)
        let pageDisplayData = NameManager.getDisplayData(frontmatter)
        let pageType = NameManager.getPageType(frontmatter)
        let hasCustomPastHasStart = Object.prototype.hasOwnProperty.call(frontmatter.displayDefaults ?? {}, "dPastHasStart")
        let hasExplicitEndDate = Object.prototype.hasOwnProperty.call(frontmatter, "DR_end") && frontmatter.DR_end
        let formatStr = ""

        if (!dateInfo.isCreated) return "**(page is future dated)**"

        if (dateInfo.isAlive) {
            if (isDisplayableDate(dateInfo.startDate)) {
                formatStr = pageDisplayData.dCurrent
            } else {
                // we have a death date in the future and displayable start date, output nothing
                return ""
            }
        }
        else if (isDisplayableDate(dateInfo.startDate) && isDisplayableDate(dateInfo.endDate)) {
            if (pageType === "event" && !hasCustomPastHasStart && (!hasExplicitEndDate || dateInfo.startDate.days === dateInfo.endDate.days)) {
                formatStr = "<startDate>"
            } else {
                formatStr = pageDisplayData.dPastHasStart
            }
        }
        else {
            formatStr = pageDisplayData.dPast
        }

        return TokenParser.formatDisplayString(formatStr, { name: fileName, frontmatter: metadata })

    }

    outputCampaignInteractions(fileName, page, campaignFilter) {
        // Intended for use from Dataview views (dv.current()) where file inlinks exist.
        // Produces a compact, stable summary so NPC pages don't need campaignInfo logs.

        const { DateManager, NameManager, util } = customJS

        const maxOtherMentions = 0 // 0 = no limit

        const normalizeStringList = (value) => {
            if (!value) return []
            if (Array.isArray(value)) return value.filter(v => typeof v === "string" && v.trim().length > 0)
            if (typeof value === "string" || value instanceof String) return [String(value)]
            return []
        }

        const normalizeTags = (value) => normalizeStringList(value).map(t => t.replace(/^#/, "").trim().toLowerCase())

        const inlinks = page?.file?.inlinks ?? []
        if (!Array.isArray(inlinks) || inlinks.length === 0) {
            return `_No session-note links found._`
        }

        const isSessionNote = (linkedPage) => {
            if (!linkedPage?.file?.path) return false

            const tags = normalizeTags(linkedPage.tags ?? linkedPage.file?.tags ?? linkedPage.file?.etags)
            if (tags.includes("session-note")) return true

            // Fall back to configured session-note folders.
            if (NameManager.getNoteCampaignCode(linkedPage.file.path, undefined, "sessionNoteFolder")) return true

            // Common convention even when metadata.json isn't fully configured.
            return linkedPage.file.path.includes("/Session Notes/") || linkedPage.file.path.includes("/Sessions/")
        }

        const inferCampaignCode = (linkedPage) => {
            const code = NameManager.getNoteCampaignCode(linkedPage.file.path, linkedPage.campaign, "sessionNoteFolder")
            if (code) return code

            // Older session notes sometimes identify the campaign in the filename.
            const name = linkedPage.file.name ?? ""
            const match = name.match(/\(([^)]+)\)\s*$/) ?? name.match(/\(([^)]+)\)/)
            if (match) return NameManager.getCampaignConfig(match[1])?.code ?? match[1].trim()

            return String(linkedPage.campaign ?? "").trim() || "Unknown"
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
                if (cfg?.partyPage) partyLabel = `[[${cfg.partyPage}|${cfg.partyPage.split("/").pop()}]]`
            } catch (e) {
                // ignore
            }

            out += `### ${partyLabel}\n`

            if (!util.isKnownToParty(fileName, page, campaignCode)) out += `Suggested knownTo: ${campaignCode}\n`

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

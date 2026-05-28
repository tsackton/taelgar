async function get_table(input) {
    input = input ?? {}

    const { NameManager } = customJS
    const LocationManager = customJS.LocationManager ?? { getLocationName: target => NameManager.getName(target) }
    const { DateManager } = customJS
    const { WhereaboutsManager } = customJS
    const { EventManager } = customJS
    const currentFile = (() => {
        try {
            return dv.current()?.file ?? {}
        } catch (e) {
            return {}
        }
    })()

    function targetName(target) {
        if (!target) return ""
        if (typeof target === "string" || target instanceof String) return target
        if (target.path) return target.path.split("/").pop().replace(/\.md$/, "")
        if (target.location) return target.location
        if (target.name) return target.name
        return String(target)
    }

    function formatName(target, format, alias, linkTextOverride, sourcePageType) {
        return NameManager.getName(targetName(target), format, alias, linkTextOverride, sourcePageType)
    }

    function safeFormatName(target, format, alias, linkTextOverride, sourcePageType) {
        try {
            return formatName(target, format, alias, linkTextOverride, sourcePageType)
        } catch (e) {
            return targetName(target)
        }
    }

    function formatLocation(target, format, depth, linkMode) {
        return LocationManager.getLocationName(targetName(target), format, depth, linkMode)
    }

    function safeFormatLocation(target, format, depth, linkMode) {
        try {
            return formatLocation(target, format, depth, linkMode)
        } catch (e) {
            return targetName(target)
        }
    }

    function normalizeDate(value, isEnd) {
        try {
            return DateManager.normalizeDate(value, isEnd)
        } catch (e) {
            return undefined
        }
    }

    function lastDayOfMonth(month) {
        switch (month) {
            case 2: return 28
            case 4:
            case 6:
            case 9:
            case 11: return 30
            default: return 31
        }
    }

    function splitRangeString(value) {
        if (!(typeof value === "string" || value instanceof String)) return undefined

        let parts = value.trim().split(/\s+to\s+/i)
        if (parts.length !== 2) return undefined

        return parts.map(part => part.trim()).filter(Boolean)
    }

    function normalizeEventDatePart(value, isEnd) {
        if (value === undefined || value === null || value === "") return undefined

        if (typeof value === "number") {
            return normalizeDate(value, isEnd)
        }

        if (typeof value === "string" || value instanceof String) {
            let trimmed = value.trim()

            if (/^\d{4}$/.test(trimmed)) {
                return normalizeDate(parseInt(trimmed, 10), isEnd)
            }

            let monthMatch = /^(\d{4})-(\d{1,2})$/.exec(trimmed)
            if (monthMatch) {
                let year = parseInt(monthMatch[1], 10)
                let month = parseInt(monthMatch[2], 10)
                let day = isEnd ? lastDayOfMonth(month) : 1
                let normalized = normalizeDate(year + "-" + String(month).padStart(2, "0") + "-" + String(day).padStart(2, "0"), isEnd)
                if (normalized) normalized.display = DateManager.DR_MONTHS?.[month] + " " + year
                return normalized
            }

            if (/^\d{4}-\d{1,2}-\d{1,2}$/.test(trimmed)) {
                return normalizeDate(trimmed, isEnd)
            }

            return undefined
        }

        return normalizeDate(value, isEnd)
    }

    function getEventDateRange(startValue, endValue) {
        let explicitRange = endValue !== undefined && endValue !== null && endValue !== ""
        let startRaw = startValue
        let endRaw = endValue
        let splitStart = splitRangeString(startValue)

        if (!explicitRange && splitStart?.length === 2) {
            startRaw = splitStart[0]
            endRaw = splitStart[1]
            explicitRange = true
        }

        let startDate = normalizeEventDatePart(startRaw, false)
        if (!startDate) return undefined

        let endDate = explicitRange
            ? normalizeEventDatePart(endRaw, true)
            : normalizeEventDatePart(startRaw, true)

        if (!endDate) endDate = startDate
        if (endDate.sort < startDate.sort) return undefined

        let isRange = explicitRange && startDate.display !== endDate.display
        let display = isRange ? startDate.display + " - " + endDate.display : startDate.display

        return {
            startDate: startDate,
            endDate: endDate,
            dateStart: startDate.display,
            dateEnd: endDate.display,
            display: display,
            sort: startDate.sort,
            sortEnd: endDate.sort,
            year: startDate.year,
            isRange: isRange
        }
    }

    function dateRangeOverlapsQuery(dateRange) {
        return dateRange?.startDate?.sort <= yearEnd.sort && dateRange.endDate?.sort >= yearStart.sort
    }

    function makeEventRow(dateRange, text, rawText, fileName) {
        return {
            year: dateRange.year,
            date: dateRange.display,
            text: text,
            rawText: rawText,
            file: fileName,
            sort: dateRange.sort,
            startDate: dateRange.startDate,
            endDate: dateRange.endDate,
            dateStart: dateRange.dateStart,
            dateEnd: dateRange.dateEnd,
            sortEnd: dateRange.sortEnd,
            isRange: dateRange.isRange,
            dateQualifier: dateRange.dateQualifier
        }
    }

    function withDateQualifier(dateRange, qualifier) {
        if (!dateRange || !qualifier) return dateRange

        return {
            ...dateRange,
            display: dateRange.display + ", " + qualifier,
            sort: dateRange.sort + qualifierSortOffset(qualifier),
            dateQualifier: qualifier
        }
    }

    function getDisplayData(frontmatter) {
        try {
            return NameManager.getDisplayData(frontmatter) ?? {}
        } catch (e) {
            return {}
        }
    }

    function pageTypeFor(frontmatter) {
        try {
            return NameManager.getPageType(frontmatter)
        } catch (e) {
            return "unknown"
        }
    }

    function inRange(jsDate) {
        return jsDate?.sort >= yearStart.sort && jsDate.sort <= yearEnd.sort
    }

    function rowInQueryRange(row) {
        let startSort = row.startDate?.sort ?? row.sort
        let endSort = row.endDate?.sort ?? row.sortEnd ?? startSort

        return startSort <= yearEnd.sort && endSort >= yearStart.sort
    }

    function shouldScanPage(item) {
        let path = item?.file?.path ?? ""
        let topLevel = path.split("/")[0]

        if (currentFile.path && path === currentFile.path) return false
        if (!currentFile.path && currentFile.name && item?.file?.name === currentFile.name) return false
        if (topLevel === "Worldbuilding") return false
        if (topLevel?.startsWith("_")) return false

        return true
    }

    function frontmatterFor(item) {
        return item?.file?.frontmatter ?? {}
    }

    function fileNameFor(item) {
        return item?.file?.name ?? item?.file?.path ?? ""
    }

    function dataWhere(collection, predicate) {
        if (!collection) return []
        if (typeof collection.where === "function") return collection.where(predicate)
        if (Array.isArray(collection)) return collection.filter(predicate)
        return []
    }

    function dataForEach(collection, callback) {
        if (!collection) return
        if (typeof collection.forEach === "function") {
            collection.forEach(callback)
        }
    }

    function hasRangeStringDate(frontmatter) {
        let fields = ["born", "died", "created", "destroyed", "DR", "DR_end", "pageTargetDate"]
        return fields.some(field => {
            let value = frontmatter?.[field]
            return (typeof value === "string" || value instanceof String) && /\s+to\s+/.test(value)
        })
    }

    function safeGetPageDates(frontmatter) {
        if (hasRangeStringDate(frontmatter)) {
            return {}
        }

        try {
            return DateManager.getPageDates(frontmatter) ?? {}
        } catch (e) {
            return {}
        }
    }

    const INLINE_DATE_VALUE_PATTERN = "-?\\d{1,4}(?:-\\d{1,2})?(?:-\\d{1,2})?(?:\\s+to\\s+-?\\d{1,4}(?:-\\d{1,2})?(?:-\\d{1,2})?)?"
    const INLINE_DATE_TOKEN_PATTERN = new RegExp(
        "(?:\\(\\(\\s*\\bDR(?:_end)?::\\s*" + INLINE_DATE_VALUE_PATTERN + "\\s*\\)\\)|\\(\\s*\\bDR(?:_end)?::\\s*" + INLINE_DATE_VALUE_PATTERN + "\\s*\\)|\\bDR(?:_end)?::\\s*" + INLINE_DATE_VALUE_PATTERN + ")\\s*",
        "g"
    )

    function stripInlineDateTokens(text) {
        return String(text ?? "")
            .replace(INLINE_DATE_TOKEN_PATTERN, "")
            .replace(/^\s*(?:[-–]\s*)?[,;:]?\s*/, "")
            .trim()
    }

    function hasUncertainInlineDateToken(text, fieldName) {
        let pattern = new RegExp("\\(\\(\\s*\\b" + fieldName + "::\\s*" + INLINE_DATE_VALUE_PATTERN + "\\s*\\)\\)")
        return pattern.test(String(text ?? ""))
    }

    function getInlineDateUncertainty(text) {
        return {
            start: hasUncertainInlineDateToken(text, "DR"),
            end: hasUncertainInlineDateToken(text, "DR_end")
        }
    }

    function withUncertainDateDisplay(dateRange, uncertainty) {
        if (!dateRange || !(uncertainty?.start || uncertainty?.end)) return dateRange

        let singleDateUncertain = !dateRange.isRange && (uncertainty.start || uncertainty.end)
        let dateStart = (uncertainty.start || singleDateUncertain) ? "(" + dateRange.dateStart + ")" : dateRange.dateStart
        let dateEnd = uncertainty.end ? "(" + dateRange.dateEnd + ")" : dateRange.dateEnd
        let display = dateRange.isRange ? dateStart + " - " + dateEnd : dateStart

        return {
            ...dateRange,
            display: display,
            dateStart: dateStart,
            dateEnd: dateEnd,
            uncertainStartDate: uncertainty.start,
            uncertainEndDate: uncertainty.end
        }
    }

    function isDateQualifier(value) {
        let qualifier = String(value ?? "").trim().toLowerCase()
        let simpleQualifiers = [
            "dawn",
            "morning",
            "midday",
            "noon",
            "afternoon",
            "evening",
            "night",
            "midnight",
            "pre-dawn",
            "predawn",
            "spring",
            "summer",
            "fall",
            "autumn",
            "winter"
        ]

        if (simpleQualifiers.includes(qualifier)) return true
        if (/^(early|late|mid)\s+(morning|afternoon|evening|night|spring|summer|fall|autumn|winter)$/.test(qualifier)) return true
        if (/^mid-?(morning|afternoon|day)$/.test(qualifier)) return true
        if (/^just after\s+(midnight|dawn|noon)$/.test(qualifier)) return true

        return false
    }

    function qualifierSortOffset(value) {
        let qualifier = String(value ?? "").trim().toLowerCase()
        let modifier = 0
        let modifierMatch = /^(early|mid|late)\s+(.+)$/.exec(qualifier)

        if (modifierMatch) {
            qualifier = modifierMatch[2]
            modifier = modifierMatch[1] === "early" ? -20 : (modifierMatch[1] === "late" ? 20 : 0)
        }

        switch (qualifier) {
            case "spring": return 90 + modifier
            case "summer": return 180 + modifier
            case "fall":
            case "autumn": return 270 + modifier
            case "winter": return 330 + modifier
            case "midnight": return 0
            case "just after midnight": return 0.01
            case "pre-dawn":
            case "predawn": return 0.04
            case "dawn": return 0.08
            case "morning": return 0.2
            case "midday":
            case "noon": return 0.5
            case "afternoon": return 0.65
            case "evening": return 0.8
            case "night": return 0.9
            default: return 0
        }
    }

    function escapeRegExp(value) {
        return String(value).replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
    }

    function linkTarget(link) {
        let path = link?.path ?? targetName(link)
        return path.replace(/\.md$/, "")
    }

    function linkDisplay(link) {
        if (link?.display) return link.display

        let path = linkTarget(link)
        return path.split("/").pop()
    }

    function wikiLink(link, display) {
        let target = linkTarget(link)
        let targetBase = target.split("/").pop()

        if (!display || display === targetBase) return "[[" + target + "]]"
        return "[[" + target + "|" + display + "]]"
    }

    function replaceOutsideWikiLinks(text, pattern, replacement) {
        return String(text)
            .split(/(\[\[[^\]]+\]\])/g)
            .map(segment => segment.startsWith("[[") ? segment : segment.replace(pattern, replacement))
            .join("")
    }

    function linkTimelineText(text, listItem) {
        if (!listItem?.outlinks) return text

        let linked = text
        let outlinks = Array.from(listItem.outlinks)
            .filter(link => linkTarget(link))
            .sort((a, b) => linkDisplay(b).length - linkDisplay(a).length)

        for (let link of outlinks) {
            let candidates = [linkDisplay(link), linkTarget(link).split("/").pop()]
                .filter(Boolean)
                .filter((candidate, index, array) => array.indexOf(candidate) === index)

            for (let candidate of candidates) {
                let pattern = new RegExp("\\b(?:[Tt]he\\s+)?" + escapeRegExp(candidate) + "\\b")
                let nextLinked = replaceOutsideWikiLinks(linked, pattern, match => wikiLink(link, match))
                if (nextLinked === linked) continue

                linked = nextLinked
                break
            }
        }

        return linked
    }

    function splitTimelineText(text) {
        let cleaned = stripInlineDateTokens(text)
        let qualifierMatch = /^([^:]{1,40}):\s*(.+)$/.exec(cleaned)

        if (qualifierMatch && isDateQualifier(qualifierMatch[1])) {
            return {
                qualifier: qualifierMatch[1].trim(),
                text: qualifierMatch[2].trim(),
                dateUncertainty: getInlineDateUncertainty(text)
            }
        }

        return {
            qualifier: undefined,
            text: cleaned,
            dateUncertainty: getInlineDateUncertainty(text)
        }
    }

    function normalizeRangeInput(value, isEnd, fieldName) {
        if (value === undefined || value === null || value === "") return undefined;

        if (typeof value === "number") {
            if (!Number.isInteger(value) || value < 0 || value > 9999) {
                throw new Error("get_EventsTable: " + fieldName + " must be a 4-digit year or YYYY-MM-DD date string.");
            }
            return normalizeDate(value, isEnd);
        }

        if (typeof value === "string" || value instanceof String) {
            const trimmed = value.trim();
            if (/^\d{4}$/.test(trimmed)) {
                return normalizeDate(parseInt(trimmed, 10), isEnd);
            }
            if (/^\d{4}-\d{2}-\d{2}$/.test(trimmed)) {
                return normalizeDate(trimmed, isEnd);
            }
            throw new Error("get_EventsTable: " + fieldName + " must be a 4-digit year or YYYY-MM-DD date string.");
        }

        throw new Error("get_EventsTable: " + fieldName + " must be a number or string.");
    }

    let yearStart = normalizeRangeInput(input.yearStart, false, "yearStart");
    if (!yearStart) throw new Error("get_EventsTable: yearStart is required.");
    let yearEnd = normalizeRangeInput(input.yearEnd ?? input.yearStart, true, "yearEnd");
    let pageWhere = input.where ?? (f => true)
    let map = input.map ?? (f => [f.date, f.text, dv.fileLink(f.file)])
    let header = input.header ?? ["Date", "Event", "File"]
    let includeAll = input.includeAll ?? input.includAll ?? false
    let options = {
        includeCreate: input.includeCreate ?? includeAll,
        includeEnd: input.includeEnd ?? includeAll,
        includeRegnal: input.includeRegnal ?? includeAll,
        includeTravel: input.includeTravel ?? includeAll,
        includePartyMeetings: input.includePartyMeetings ?? includeAll
    };

    let pages = undefined;
    if (input.pageFilter) pages = dv.pages(input.pageFilter.trim());
    else pages = dv.pages();

    let rows = pages.where(shouldScanPage).where(pageWhere).flatMap(item => {
        let events = [];
        let frontmatter = frontmatterFor(item)
        let fileName = fileNameFor(item)

        if (frontmatter.DR != null) {
            let eventDate = getEventDateRange(frontmatter.DR, frontmatter.DR_end)

            if (dateRangeOverlapsQuery(eventDate)) {
                let name = safeFormatName(fileName, "yt")
                if (frontmatter.summary) {
                    name = "*(" + name + ")*: " + frontmatter.summary
                }

                events.push(makeEventRow(eventDate, name, name, fileName))
            }
        }

        if ((options.includeCreate == true || options.includeEnd == true) && !(pageTypeFor(frontmatter) === "event" && frontmatter.DR != null)) {
            let name = safeFormatName(fileName, "yt")
            let pageDisplayData = getDisplayData(frontmatter)
            let pageExistenceData = safeGetPageDates(frontmatter)

            if (options.includeCreate && inRange(pageExistenceData.startDate)) {
                let origin = WhereaboutsManager.getWhereabouts(frontmatter).origin
                let text = name + " " + pageDisplayData.startStatus
                if (origin?.location) {
                    text += " in " + safeFormatLocation(origin.location, NameManager.PreserveCase, 2, NameManager.CreateLink)
                }

                events.push({ year: pageExistenceData.startDate.year, date: pageExistenceData.startDate.display, text: text, rawText: text, file: fileName, sort: pageExistenceData.startDate.sort })
            }

            if (options.includeEnd && inRange(pageExistenceData.endDate)) {
                let diedSpot = WhereaboutsManager.getWhereabouts(frontmatter, pageExistenceData.endDate).lastKnown
                let text = name + " " + pageDisplayData.endStatus
                if (diedSpot?.location) {
                    text += " in " + safeFormatLocation(diedSpot.location, NameManager.PreserveCase, 2, NameManager.CreateLink)
                }

                events.push({ year: pageExistenceData.endDate.year, date: pageExistenceData.endDate.display, text: text, rawText: text, file: fileName, sort: pageExistenceData.endDate.sort })
            }

        }

        if (options.includeRegnal == true && frontmatter.reignStart != null) {
            let regnalData = DateManager.getRegnalDates(frontmatter)
            let pageExistData = safeGetPageDates(frontmatter)
            let name = safeFormatName(fileName, "yt")
            if (inRange(regnalData.startDate)) {
                let text = name + " was crowned"
                events.push({ year: regnalData.startDate.year, date: regnalData.startDate.display, text: text, rawText: text, file: fileName, sort: regnalData.startDate.sort })
            }
            // only include end dates if (a) they don't match the death date or (b) we didn't include death dates
            if (inRange(regnalData.endDate) && (regnalData.endDate != pageExistData.endDate || !options.includeEnd)) {
                let text = name + " reign ended"
                events.push({ year: regnalData.endDate.year, date: regnalData.endDate.display, text: text, rawText: text, file: fileName, sort: regnalData.endDate.sort })
            }
        }
        if (options.includePartyMeetings) {
            EventManager.getPartyMeeting({ name: fileName, frontmatter: frontmatter }, undefined).forEach(element => {
                if (!inRange(element?.date)) return
                let name = safeFormatName(fileName, "yt")
                let uncap = element.text.charAt(0).toLowerCase() + element.text.slice(1)

                let processedText = name + " " + uncap

                events.push({ year: element.date.year, date: element.date.display, text: processedText, rawText: element.text, file: fileName, sort: element.date.sort })
            });
        }

        if (options.includeTravel && frontmatter.whereabouts && frontmatter.whereabouts.length > 0) {
            let name = safeFormatName(fileName, "yt")
            WhereaboutsManager.getWhereaboutsList(frontmatter).filter(e => e.start || e.end).forEach(element => {
                let parsedStart = element.start
                let parsedEnd = element.end
                let location = safeFormatLocation(element.location, NameManager.PreserveCase, 1, NameManager.CreateLink)

                let arriveVerb = "was at"
                let departVerb = "left"

                if (parsedEnd || element.type == "home") {
                    // we have a start and an end, or a start for a home -- show as a range 
                    arriveVerb = "arrived at"
                    if (element.type == "home") {
                        arriveVerb = "moved to"
                    }
                }

                if (inRange(parsedEnd)) {
                    let departText = name + " " + departVerb + " " + location
                    events.push({ year: parsedEnd.year, date: parsedEnd.display, text: departText, rawText: departText, file: fileName, sort: parsedEnd.sort })
                }

                if (inRange(parsedStart)) {
                    let atText = name + " " + arriveVerb + " " + location
                    events.push({ year: parsedStart.year, date: parsedStart.display, text: atText, rawText: atText, file: fileName, sort: parsedStart.sort })
                }
            });
        }

        dataForEach(dataWhere(item?.file?.lists, t => t.DR != null), t => {
            let eventDate = getEventDateRange(t.DR, t.DR_end)
            if (dateRangeOverlapsQuery(eventDate)) {

                let timelineText = splitTimelineText(t.text)
                let eventDateWithUncertainty = withUncertainDateDisplay(eventDate, timelineText.dateUncertainty)
                let eventDateWithQualifier = withDateQualifier(eventDateWithUncertainty, timelineText.qualifier)
                let realText = linkTimelineText(timelineText.text, t)

                let descriptor = frontmatter.timelineDescriptor ?? frontmatter.name

                if (frontmatter.type == "SessionNote") descriptor = frontmatter.campaign

                if (descriptor) {
                    realText = "*(" + String(descriptor) + ")*: " + realText
                }

                var obj = makeEventRow(eventDateWithQualifier, realText, t.text, fileName)

                events.push(obj)
            }

        })        

        return events;
    }
    ).where(rowInQueryRange).sort(f => f.sort).map(map)

    if ((rows?.length ?? 0) === 0) {
        return await dv.paragraph("_No events found._")
    }

    return await dv.table(header, rows)
}

return await get_table(input);

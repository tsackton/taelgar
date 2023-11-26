
class WhereaboutsManager {

    #getNormalizedWhereabout(w) {
        const { DateManager } = customJS

        function isValidLocPiece(l) {
            if (l == undefined) return false
            if (l == "") return false
            if (l == "unknown") return false
            return true
        }

        let endDate = DateManager.normalizeDate(w.end, true)
        let startDate = DateManager.normalizeDate(w.start, false)
        if (!startDate) startDate = DateManager.normalizeDate(w.date, false)

        // shouldn't these just be 0001 and 9999? //
        let dateMin = DateManager.normalizeDate('0001-01-01', false)
        let dateMax = DateManager.normalizeDate('9999-01-01', true)

        let type = w.type

        // backwards compatability //
        // as far as I can tell no files require these //
        if (!type) {
            if (w.excursion == true) type = "away"
        }

        if (type == "excursion") type = "away"
        if (type == "origin") type = "home"

        let location = w.location
        if (!location) {
            let hasPlace = isValidLocPiece(w.place)
            let hasRegion = isValidLocPiece(w.region)

            if (hasPlace && hasRegion) location = w.place + ", " + w.region
            else if (hasPlace) location = w.place
            else if (hasRegion) location = w.region
        }
        // end backwards compatability //

        // set undefined locations to "Unknown" //
        if (!location) location = "Unknown"

        let logicalEnd = endDate ?? dateMax
        let logicalStart = startDate ?? dateMin
        let awayEnd = endDate ?? (w.type == "home" ? dateMax
            : DateManager.normalizeDate(w.start, true) ?? dateMax)

        return {
            start: startDate,
            type: type,
            end: endDate,
            location: location,
            logicalEnd: logicalEnd,
            logicalStart: logicalStart,
            awayEnd: awayEnd,
            format: w.format
        }
    }

    #get_distance_to_target(item, target) {
        if (item.logicalEnd.sort < target.sort) {
            return target.jsDate - item.logicalEnd.jsDate
        }
        else return target.jsDate - item.logicalStart.jsDate
    }

    #filterWhereabouts(whereaboutsList, type, target, allowPast) {
        let candidateSet = whereaboutsList.filter(w => (!type || w.type == type) && (w.logicalStart.sort <= target.sort)).filter(w => allowPast || target.sort <= w.logicalEnd.sort)
        let soonestPossible = Math.min(...candidateSet.map(w => this.#get_distance_to_target(w, target)))
        return candidateSet.filter(w => this.#get_distance_to_target(w, target) == soonestPossible)
    }

    getPartyMeeting(metadata, campaign) {
        const { StringFormatter } = customJS
        const { NameManager } = customJS
        const { DateManager } = customJS

        let results = []

        let displayData = NameManager.getDisplayData(metadata)

        let format = displayData.whereaboutsParty

        if (metadata.campaignInfo) {
            metadata.campaignInfo.filter(e => e.campaign && e.date).forEach(element => {

                let displayDate = DateManager.normalizeDate(element.date)
                let locForThisDate = this.getWhereabouts(metadata, element.date).current;

                if (locForThisDate && (element.campaign == campaign || !campaign)) {
                    let person = element.person ?? element.campaign                    
                    if (person) {
                        let type = element.type ?? "seen"
                        let text = StringFormatter.getFormattedString(format, {frontmatter: metadata, file: ""}, displayDate, undefined, {met: type, person: person})
                        results.push({ text: text, campaign: element.campaign, date: displayDate, location: locForThisDate.location })
                    }
                }
            });
        }

        return results
    }

    getWhereaboutsList(metadata) {
        const {NameManager} = customJS

        if (metadata && metadata.whereabouts && metadata.whereabouts.length > 0) {
            let wb = metadata.whereabouts
            if (typeof metadata.whereabouts === 'string' || metadata.whereabouts instanceof String) {
                wb = [{ type: "home", location: metadata.whereabouts }]
            }

            return wb.map(f => this.#getNormalizedWhereabout(f))
        // backwards compatability // 
        // if place has partOf but no whereabouts, use partOf for whereabouts //
        } else if (metadata && NameManager.getPageType(metadata) == "place") {
            let wb = [{ type: "home", location: metadata.partOf }]
            return wb.map(f => this.#getNormalizedWhereabout(f))
        }

        return []
    } 

    getWhereabouts(metadata, targetDate) {
        const { DateManager } = customJS

        targetDate = DateManager.normalizeDate(targetDate)
        if (!targetDate) targetDate = DateManager.getTargetDateForPage(metadata)

        // default to unknown //
        let unknownWhereabout = { location: "Unknown" }
        let whereaboutResult = { current: unknownWhereabout, home: unknownWhereabout, origin: unknownWhereabout, lastKnown: unknownWhereabout }

        let originDate = DateManager.normalizeDate(metadata.born, false) ?? DateManager.normalizeDate(metadata.created, false) ?? DateManager.normalizeDate("0001-01-01", false)
        let normalized = this.getWhereaboutsList(metadata)

        // home is lexically last valid home //
        whereaboutResult.home = this.#filterWhereabouts(normalized, "home", targetDate, false).last() ?? whereaboutResult.home
        // origin is lexically first valid home //
        whereaboutResult.origin = this.#filterWhereabouts(normalized, "home", originDate, false).first() ?? whereaboutResult.origin
        // current is lexically last valid location //
        whereaboutResult.current = this.#filterWhereabouts(normalized, undefined, targetDate, false).last() ?? whereaboutResult.current
        // lastknown is assumed to be current for now //
        whereaboutResult.lastKnown = whereaboutResult.current

        if (whereaboutResult.current.location != "Unknown" && targetDate.sort > whereaboutResult.current.awayEnd.sort) {
            // our current location is our best guess as to our location, but we are not still there //
            whereaboutResult.current = unknownWhereabout
        }
        else {
            // this means we don't have a current whereabout - everything is in the past
            whereaboutResult.lastKnown = this.#filterWhereabouts(normalized, undefined, targetDate, true).last() ?? unknownWhereabout

        }

        return whereaboutResult
    }
}


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

        let dateMin = DateManager.normalizeDate('0001-01-01', false)
        let dateMax = DateManager.normalizeDate('9999-01-01', true)

        let type = w.type
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
            awayEnd: awayEnd
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
        let soonestPossible =   Math.min(...candidateSet.map(w =>  this.#get_distance_to_target(w, target)))           
        return candidateSet.filter(w =>  this.#get_distance_to_target(w, target) == soonestPossible)
    }

    getPartyMeeting(metadata, campaign) {
        const {metadataUtils} = customJS
        const { DateManager } = customJS

        let results = []
       
        if (metadata.campaignInfo) {
            metadata.campaignInfo.filter(e => e.campaign && e.date).forEach(element => {           
                                      
                let displayDate = DateManager.normalizeDate(element.date)                  
                let locForThisDate = this.getWhereabouts(metadata, element.date).current;

                if (locForThisDate && (element.campaign == campaign || !campaign)) {                    
                    let partyName = metadataUtils.get_party_name_for_party(element.campaign)                    
                    if (partyName) {
                        let type = element.type ?? "seen"
                        let capitalized = type.charAt(0).toUpperCase() + type.slice(1);                        
                        results.push ({ text: `${capitalized} by ${partyName} on ${displayDate.display} in: ${metadataUtils.get_Location(locForThisDate, false)}`, campaign: element.campaign, date: displayDate, location: locForThisDate.location })
                    }
                }
            });
        }

        return results
    }

    getWhereabouts(metadata, targetDate) {
        const { DateManager } = customJS

        targetDate = DateManager.normalizeDate(targetDate)        
        if (!targetDate) targetDate = DateManager.getTargetDateForPage(metadata)
     
        let whereaboutResult = { current: undefined, home: undefined, origin: undefined, lastKnown: undefined }

        if (metadata && metadata.whereabouts && metadata.whereabouts.length > 0) {

            let originDate = DateManager.normalizeDate(metadata.born, false) ?? DateManager.normalizeDate("0001-01-01", false)
            let normalized = metadata.whereabouts.map(f => this.#getNormalizedWhereabout(f))
           
            let homes = this.#filterWhereabouts(normalized, "home", targetDate, false)
            let origins = this.#filterWhereabouts(normalized, "home", originDate, false)
           
            whereaboutResult.home = homes.last()
            whereaboutResult.origin = origins.first()

            if (whereaboutResult.origin && whereaboutResult.origin.startDate) whereaboutResult.origin = undefined

            let current = this.#filterWhereabouts(normalized, undefined, targetDate, false).last()
        
            if (current) {
                if (targetDate.sort <= current.awayEnd.sort) {
                    // this away is truely valid
                    whereaboutResult.current = current
                    whereaboutResult.lastKnown = undefined;
                } else {
                    // this away is our best guess as to location, but we are not still there
                    whereaboutResult.current = undefined
                    whereaboutResult.lastKnown = current;
                }

                return whereaboutResult
            }

            // this means we don't have a current whereabout - everything is in the past
            whereaboutResult.lastKnown = this.#filterWhereabouts(normalized, undefined, targetDate, true).last()                   
        }

        return whereaboutResult  
    }
}
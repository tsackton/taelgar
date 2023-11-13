function get_Whereabouts(metadata) {
   
    const { metadataUtils } = customJS

    if (!metadataUtils.isPageCreated(metadata)) return "";

    let isPageAlive =  metadataUtils.isPageAlive(metadata);
    let pageYear = metadataUtils.get_pageEventsDate(metadata)

    if (metadata.whereabouts) {        
        let lastKnownWhereabouts = metadataUtils.get_lastKnownWhereabouts(metadata, pageYear)
        let homeWhereabouts = metadataUtils.get_homeWhereabouts(metadata, pageYear)
        let currentWhereabouts = metadataUtils.get_currentWhereabouts(metadata, pageYear)

        if (homeWhereabouts) {
            // we have a home
            if (currentWhereabouts == undefined || homeWhereabouts.location == currentWhereabouts.location) return "";            
        }
        
        if (currentWhereabouts && currentWhereabouts.location) {
            return "Current location: (as of " + pageYear.display + "): " + metadataUtils.get_Location(currentWhereabouts)
        }

        let outputString = "";

        if (lastKnownWhereabouts && lastKnownWhereabouts.location) {
            let eventDateForLastKnown = lastKnownWhereabouts.type == "home"  ?
                    metadataUtils.parse_date_to_events_date(lastKnownWhereabouts.end, true) :
                    metadataUtils.parse_date_to_events_date(lastKnownWhereabouts.start, false)

            outputString = "Last known location: (as of " + eventDateForLastKnown.display + "): " + metadataUtils.get_Location(lastKnownWhereabouts)
        }

        if (isPageAlive) {
             outputString += "\n Current location: Unknown";
        }
        return outputString;

    }

    return ""
}

return get_Whereabouts(dv.current());
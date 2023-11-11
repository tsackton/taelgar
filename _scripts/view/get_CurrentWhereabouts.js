function compare_event_dates(older, younger) {    
    return older.sort.localeCompare(younger.sort)
}


function get_Whereabouts(metadata) {
   
    const { metadataUtils } = customJS

    let pageYear = metadataUtils.get_pageEventsDate(metadata)
    let existYear = metadataUtils.get_existEventsDate(metadata)
    let endYear = metadataUtils.get_endEventsDate(metadata)

    if (metadata.whereabouts) {
        if (existYear && pageYear.sort < existYear.sort) return "";
        let lastKnownWhereabouts = metadataUtils.get_lastKnownWhereabouts(metadata, pageYear)
        let homeWhereabouts = metadataUtils.get_homeWhereabouts(metadata, pageYear)
        let currentWhereabouts = metadataUtils.get_currentWhereabouts(metadata, pageYear)

        if (homeWhereabouts) {
            // we have a home
            if (homeWhereabouts.location == currentWhereabouts.location) return "";            
        }

        let pageExists = !endYear || (endYear && pageYear.sort <= endYear.sort)

        if (currentWhereabouts.location && pageExists) {
            return "Current location: (as of " + pageYear.display + "): " + metadataUtils.get_Location(currentWhereabouts)
        }

        let outputString = "";

        if (lastKnownWhereabouts && lastKnownWhereabouts.location) {
            let eventDateForStart = metadataUtils.parse_date_to_events_date(lastKnownWhereabouts.start)
            outputString = "Last known location: (as of " + eventDateForStart.display + "): " + metadataUtils.get_Location(lastKnownWhereabouts)
        }

        if (pageExists) {
             outputString += "\n Current location: Unknown";
        }
        return outputString;

    }

    return ""
}

return get_Whereabouts(dv.current());
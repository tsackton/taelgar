function compare_event_dates(older, younger) {    

    let sortOlder = older == undefined ? "" : older.sort;
    let youngerSort = younger == undefined ? "" : younger.sort;

    return sortOlder.localeCompare(youngerSort)
}


function get_HomeWhereabouts(metadata) {
   
    const { metadataUtils } = customJS
   
    let current = metadataUtils.get_pageEventsDate(metadata);
    let pageExist = metadataUtils.get_existEventsDate(metadata)
    let pageEnd = metadataUtils.get_endEventsDate(metadata);

    if (pageExist && current.sort < pageExist.sort) return "";

    let pageIsEnded = pageEnd && pageEnd.sort < current.sort;

    if (metadata.whereabouts) {

        let origin = metadataUtils.get_originWhereabouts(metadata);
        let home =  metadataUtils.get_homeWhereabouts(metadata, current);

        let showOrigin = origin && ( !home || origin.location != home.location)
        let showHome = home;

        let displayString = "";

        if (showOrigin) {
            displayString = "Originally from: " + metadataUtils.get_Location(origin);
        }

        if (showHome && pageIsEnded) {
            displayString += "\nLived in: " + metadataUtils.get_Location(home);
        }

        if (showHome && !pageIsEnded) {
            displayString += "\nBased in: " + metadataUtils.get_Location(home);
        }
        

        return displayString;
    }

    return ""
}

return get_HomeWhereabouts(dv.current());
function compare_event_dates(older, younger) {    

    let sortOlder = older == undefined ? "" : older.sort;
    let youngerSort = younger == undefined ? "" : younger.sort;

    return sortOlder.localeCompare(youngerSort)
}


function get_HomeWhereabouts(metadata) {
   
    const { metadataUtils } = customJS
   
    if (!metadataUtils.isPageCreated(metadata)) return "";

    let isPageAlive =  metadataUtils.isPageAlive(metadata);
    
    if (metadata.whereabouts) {

        let origin = metadataUtils.get_originWhereabouts(metadata);
        let home =  metadataUtils.get_homeWhereabouts(metadata);

        let showOrigin = origin && ( !home || origin.location != home.location)
        let showHome = home ;

        let displayString = "";

        if (showOrigin) {
            displayString = "Originally from: " + metadataUtils.get_Location(origin);
        }

        if (showHome && !isPageAlive) {
            displayString += "\nLived in: " + metadataUtils.get_Location(home);
        }

        if (showHome && isPageAlive) {
            displayString += "\nBased in: " + metadataUtils.get_Location(home);
        }
        

        return displayString;
    }

    return ""
}

return get_HomeWhereabouts(dv.current());
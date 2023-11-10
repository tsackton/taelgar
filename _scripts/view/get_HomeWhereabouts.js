function compare_event_dates(older, younger) {    

    let sortOlder = older == undefined ? "" : older.sort;
    let youngerSort = younger == undefined ? "" : younger.sort;

    return sortOlder.localeCompare(youngerSort)
}


function get_HomeWhereabouts(metadata) {
   
    const { metadataUtils } = customJS
   
    let current = metadataUtils.get_currentEventsDate();

    if (metadata.whereabouts) {

        let home = metadata.whereabouts.sort((a,b) => compare_event_dates(metadataUtils.parse_date_to_events_date(a.date),metadataUtils.parse_date_to_events_date(b.date))).findLast(s => (s.date == undefined || metadataUtils.parse_date_to_events_date(s.date).sort <= current.sort) && s.type === "home");
        if (home && (home.place || home.region)) {

            if (metadata.died && (metadataUtils.parse_date_to_events_date(metadata.died).sort < metadataUtils.get_pageEventsDate(metadata).sort)) {
                return "Lived in: " + metadataUtils.get_Location(home) + "\n";
            }

            return "Based in: " + metadataUtils.get_Location(home) + "\n";
        } 
    }

    if (metadata.origin) {
            
        if (metadata.died && (metadataUtils.parse_date_to_events_date(metadata.died).sort < metadataUtils.get_pageEventsDate(metadata).sort)) {
            return "Lived in: " + metadataUtils.get_Location(metadata.origin) + "\n";
        }

        return "Based in: " + metadataUtils.get_Location(metadata.origin) + "\n";
    }

    return ""
}

return get_HomeWhereabouts(dv.current());
function get_RegnalValue(metadata) {
    
    const { metadataUtils } = customJS

    let yearStart = metadataUtils.parse_date_to_events_date(metadata.reignStart, false);
    let yearEnd = metadata.reignEnd ? metadataUtils.parse_date_to_events_date(metadata.reignEnd, true) : undefined;
    if (yearEnd == undefined) yearEnd =  metadataUtils.parse_date_to_events_date(metadata.died, true);
    
    let currentYear =  metadataUtils.get_pageEventsDate(metadata);
    
    if (!yearStart) return "";
    if (yearStart.sort > currentYear.sort) return "";

    let reignLength = metadataUtils.get_Age(currentYear, yearStart);

    // reign hasn't ended yet
    if (yearEnd == undefined || currentYear.sort < yearEnd.sort) {               
        return "reigning since " + yearStart.display + " (" + reignLength + " years)";        
    }

    // reign has ended
    return "reigned " + yearStart.display + " - " + yearEnd.display + " (" + reignLength + " years)";
}
return get_RegnalValue(dv.current() )
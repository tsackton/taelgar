function get_RegnalValue(metadata) {
    
    const { metadataUtils } = customJS
    
    let yearStart = metadataUtils.parse_date_to_events_date(metadata.reignStart);
    let yearEnd = metadata.reignEnd ? metadataUtils.parse_date_to_events_date(metadata.reignEnd) : undefined;
    if (yearEnd == undefined) yearEnd =  metadataUtils.parse_date_to_events_date(metadata.died);
    
    currentYear =  metadataUtils.get_pageEventsDate(metadata);
    
    if (!yearStart) return "";
    if (yearStart && yearEnd && yearStart.sort > yearEnd.sort) return "**(timetraveler, check your YAML)**";
    
    // reign hasn't started yet
    if (yearStart.sort > currentYear.sort) return "";

    // reign hasn't ended yet
    if (yearEnd == undefined || yearEnd.sort >= currentYear.sort) {               
        let reignLength = metadataUtils.get_Age(currentYear, yearStart);
        return "reigning since " + yearStart.display + " (" + reignLength + " years)";        
    }

    // reign has ended
    return "reigned " + yearStart.display + " - " + yearEnd.display + " (" + (metadataUtils.get_Age(yearEnd, yearStart)) + " years)";
}
return get_RegnalValue(dv.current() )
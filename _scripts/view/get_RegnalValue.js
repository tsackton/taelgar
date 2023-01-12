function get_RegnalValue(metadata, currentYear) {
     
    let yearStart = metadata.reignStart;
    let yearEnd = metadata.reignEnd;
    if (yearEnd == undefined) yearEnd = metadata.died;
    
    currentYear = metadata.yearOverride ? metadata.yearOverride : currentYear
    
    if (!yearStart) return "";
    if (yearStart && yearEnd && yearStart > yearEnd) return "**(timetraveler, check your YAML)**";
    
    // reign hasn't started yet
    if (yearStart > currentYear) return "";

    // reign hasn't ended yet
    if (yearEnd == undefined || yearEnd >= currentYear) {               
        let reignLength = currentYear - yearStart;
        return "reigning since " + yearStart + " (" + reignLength + " years)";        
    }

    // reign has ended
    return "reigned " + yearStart + " - " + yearEnd + " (" + (yearEnd-yearStart) + " years)";
}
return get_RegnalValue(dv.current(), input.currentYear)
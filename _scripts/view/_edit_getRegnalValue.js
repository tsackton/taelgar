function getRegnalValue(tp) {
     
    let yearStart = tp.frontmatter.reignStart;
    let yearEnd = tp.frontmatter.reignEnd;
    if (yearEnd == undefined) yearEnd = tp.frontmatter.died;
    
    let currentYear = tp.frontmatter.yearOverride;
    if (currentYear == undefined) currentYear =  window.FantasyCalendarAPI.getCalendars()[0].current.year


    if (!yearStart) return "";
    if (yearStart && yearEnd && yearStart > yearEnd) return "(timetraveler, check your YAML)";
    
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
module.exports = getRegnalValue;
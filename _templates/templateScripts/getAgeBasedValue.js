function getPageDatedValue(tp, strings) {
            
    let preExistError = strings.preExistError;
    let startPrefix = strings.startPrefix;
    let endPrefix = strings.endPrefix;
    let yearStart = tp.frontmatter.born;
    let yearEnd = tp.frontmatter.died;

    if (preExistError == undefined) preExistError = "(not yet born)";    
    if (startPrefix == undefined) startPrefix = "b.";
    if (endPrefix == undefined) endPrefix = "d.";
    
    // setup some other common patterns
    if (yearStart == undefined) yearStart = tp.frontmatter.built;
    if (yearStart == undefined) yearStart = tp.frontmatter.created;
    if (yearEnd == undefined) yearEnd = tp.frontmatter.destroyed;
    
    let currentYear = tp.frontmatter.yearOverride;
    if (currentYear == undefined) currentYear =  window.FantasyCalendarAPI.getCalendars()[0].current.year


    if (!yearStart && !yearEnd) return "";
    if (yearStart && yearEnd && yearStart > yearEnd) return "(timetraveler, check your YAML)";
    
    // we have a created year, no ended year
    if (yearStart && !yearEnd) {
        if (yearStart > currentYear) return preExistError;
        
        let age = currentYear - yearStart;

        return startPrefix + " " + yearStart + " (" + age + " years old)";
    }

    // we have a death year, no born year
    if (yearEnd && !yearStart) {
        if (yearEnd < currentYear) return endPrefix + " " + yearEnd;
        // they have a death date, and it hasn't happened yet, but no born date, so nothing to show
        return "";
    }

    if (yearStart > currentYear) return preExistError;

    // we have both a start and end date - and they died before now
    if (yearEnd < currentYear) {       
        return startPrefix + " " + yearStart + " - " + endPrefix + " " + yearEnd +  " at age " + (yearEnd-yearStart);
    }

    return startPrefix + " " + yearStart + " (" + (currentYear-yearStart) + " years old)";
}
module.exports = getPageDatedValue;
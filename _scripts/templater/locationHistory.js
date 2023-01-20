function locationHistory(tp) {

    // copied from getLocation for now; should be considated
    function get_Location(place, region) {

        // construct variables //
        loc = place
        locRegion = region

        if (loc) {
            if (locRegion) {
                locArray = loc.split(',')
                locArray.push(locRegion)
            } else {
                locArray = loc.split(',')
            }
        } else {
            if (locRegion) {
                locArray = locRegion.split(',')
            } else {
                // no values
                return ""
            }
        }

        let locArrayValues = locArray.map(function (f) {
            pieceValue = f.trim();

            file = window.app.vault.getFiles().find(f => f.basename == pieceValue);
            if (file != undefined) { return "[[" + pieceValue + "]]"; }
            return pieceValue;
        });

        return locArrayValues.join(', ');
    }

    function get_displayDateFromYaml(yamlDate) {         
        let pieces = yamlDate.split('-');
        
        if (pieces.length != 3 || pieces[0] == 1) return "(unknown)";
        

        return get_displayDate(pieces[0], pieces[1]-1, pieces[2]);
    }
   
    function get_displayDate(year, month, day) {
        let currentFantasyCal = window.FantasyCalendarAPI.getCalendars()[0];        
        let date = {year: year, month: month, day: day};
        return window.FantasyCalendarAPI.getDay(date, currentFantasyCal).displayDate;      
    }
   
    if (tp.frontmatter.whereabouts) {
               
        let outputString = "\n>[!info]+ Location History\n";
        
        tp.frontmatter.whereabouts.forEach(element => {            
            outputString += "> On " + get_displayDateFromYaml(element.date);
            if (element.excursion)  {
                outputString += " a trip to: ";
            } else {
                outputString += ": ";
            }

            outputString += get_Location(element.place, element.region) + "\n";
        });
    
        return outputString;
    }

    return ""
}

module.exports = locationHistory
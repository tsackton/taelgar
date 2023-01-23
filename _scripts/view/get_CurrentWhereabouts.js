function get_Whereabouts(metadata, input) {
   
    // this converts a yamlDate to a string and a jsDate to a string and then compares them as strings
    // returns 1 if yaml is greater than js, 0 if equal, -1 if less
    function compare_dates(yamlDate, jsDate) {
        if (!yamlDate) console.log("no yaml date");
        if (!jsDate) console.log("no yaml date");

        let yamlDateStr = yamlDate.year.toString().padStart(4, '0') + yamlDate.month.toString().padStart(2,'0') + yamlDate.day.toString().padStart(2,'0');
        let jsDateStr = jsDate.getUTCFullYear().toString().padStart(4, '0') + (jsDate.getUTCMonth()+1).toString().padStart(2,'0') + jsDate.getUTCDate().toString().padStart(2,'0');

        console.log("yamldate: " + yamlDateStr + " jsDate: " + jsDateStr);

        if (yamlDateStr == jsDateStr) return 0;
        return yamlDateStr > jsDateStr ? 1 : -1;
    }

    function get_displayDateFromYaml(yamlDate) {         
        return get_displayDate(yamlDate.year, yamlDate.month-1, yamlDate.day);
    }

    function get_currentDisplayDate() {
        let currentYear = window.FantasyCalendarAPI.getCalendars()[0].current.year;
        let currentMonth = window.FantasyCalendarAPI.getCalendars()[0].current.month;
        let currentDay = window.FantasyCalendarAPI.getCalendars()[0].current.day;
    
        return get_displayDate(currentYear, currentMonth, currentDay);
    }

    function get_displayDate(year, month, day) {
        let currentFantasyCal = window.FantasyCalendarAPI.getCalendars()[0];
        console.log(`${year} ${month} ${day}`)
        let date = {year: year, month: month, day: day};
        return window.FantasyCalendarAPI.getDay(date, currentFantasyCal).displayDate;      
    }

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

    let currentYear = window.FantasyCalendarAPI.getCalendars()[0].current.year;
    let currentMonth = window.FantasyCalendarAPI.getCalendars()[0].current.month;
    let currentDay = window.FantasyCalendarAPI.getCalendars()[0].current.day;
    let currentJsDate = new Date(currentYear, currentMonth, currentDay, 0, 0, 0);
    
    let config = {};

    if (input.config != undefined) {
        config = JSON.parse(input.config);    
    }

    if (!config.whereaboutsSettings) config.whereaboutsSettings = {};

    if (metadata.whereabouts) {
        if (metadata.born > currentYear) return "";

        let current = metadata.whereabouts.findLast(s => s.type != "origin" && (s.date == undefined || compare_dates(s.date, currentJsDate) <= 0));
        let home = metadata.whereabouts.findLast(s => (s.date == undefined || compare_dates(s.date, currentJsDate) <= 0) && s.type === "home");
        
        if (current) {
            // we have a current place -- show if it doesn't match home
            let alwaysShowLocation = config.whereaboutsSettings.alwaysShowLocation;
            let outputString = "Current location (as of " + get_currentDisplayDate() + "): " + get_Location(current.place, current.region);

            if (alwaysShowLocation) return outputString;
            if (!home) return outputString;
            if (current.region != home.region) return outputString;
            if (current.place !=  home.place) return outputString;
        }
    }

    return ""
}

return get_Whereabouts(dv.current(), input);
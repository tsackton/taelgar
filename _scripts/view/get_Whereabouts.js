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
    let lastSeenString = "";     
   
    if (metadata.whereabouts) {
        if (metadata.born > currentYear) return "";

        let bornDate = new Date(1, 0, 0, 0, 0, 0, 0);
        bornDate.setFullYear(1);
        bornDate.setMonth(0);
        bornDate.setDate(1);
        if (metadata.born) {
            bornDate.setFullYear(metadata.born);            
        }
      
        let lastSeen = undefined;
        let lastSeenByPartyDate = undefined;
        
        if (input.configData != undefined) {
            let config = JSON.parse(input.configData);
            lastSeenByPartyDate = metadata["lastSeenByParty_" + config.campaignPrefix];
        }
        
        if (!lastSeenByPartyDate) {
            lastSeenByPartyDate = metadata.lastSeenByParty;
        }

        if (lastSeenByPartyDate) {
            lastSeen = metadata.whereabouts.findLast(s => compare_date(s.date,lastSeenByPartyDate) <= 0);
        }

        let current = metadata.whereabouts.findLast(s => compare_dates(s.date, currentJsDate) <= 0);
        let home = metadata.whereabouts.findLast(s => compare_dates(s.date, currentJsDate) <= 0 && !s.excursion);
        let original = metadata.whereabouts.find(s => compare_dates(s.date, bornDate) >= 0);


        if (home) console.log("home: " + home.date.year + " " + home.date.month + " " + home.date.day);
        if (original) console.log("original: " + original.date.year + " " + original.date.month + " " + original.date.day);
        if (current) console.log("current: " + current.date.year + " " + current.date.month + " " + current.date.day);

        let outputString = "";

        if (!home) {
            if (current) {
                // no home, but have a current location; implies all locations are tagged excursion
                outputString += input.prefix + "Current Location (as of " + get_currentDisplayDate() + "): " + get_Location(current.place, current.region) + input.suffix;
                return outputString
            }
            // something has gone wrong -- we should have a current place at all times
            return "(unknown location)";
        }

        if (original) {
            // we have an original place -- show it if it doesn't match home place
            if (original.place != home.place || original.region != home.region) {
                outputString = input.prefix + "Originally from: " + get_Location(original.place, original.region) + input.suffix + "\n";
            }
        }

        if (lastSeen) {
            let matchesHome = lastSeen.place == home.place && lastSeen.region == home.region;
            let matchesCurrent = lastSeen.place == current.place && lastSeen.region == current.region;
            // we PC place -- show if it is not the same as either home or current
            if (!matchesHome && !matchesCurrent) {
                outputString += input.prefix + "Party last known location (as of " + get_displayDateFromYaml(lastSeenByPartyDate) + "): " +   get_Location(lastSeen.place, lastSeen.region) + input.suffix + "\n";
            }
        }

        if (current) {
            // we have a current place -- show if it doesn't match home
            if (current.place != home.place || current.region != home.region) {
                outputString += input.prefix + "Current Location (as of " + get_currentDisplayDate() + "): " + get_Location(current.place, current.region) + input.suffix + "\n";
            }
        }

        outputString += input.prefix + "Based in: " + get_Location(home.place, home.region)  + input.suffix + "\n";
        return outputString;
    }

    return ""
}

return get_Whereabouts(dv.current(), input);
function compare_event_dates(older, younger) {    
    return older.sort.localeCompare(younger.sort)
}


function get_Whereabouts(metadata) {
   
    const { metadataUtils } = customJS

    let pageYear = metadataUtils.get_pageEventsDate(metadata)
    let existYear = metadataUtils.get_existEventsDate(metadata)
    let endYear = metadataUtils.get_endEventsDate(metadata)

    if (metadata.whereabouts) {
        if (existYear && pageYear.sort < existYear.sort) return "";
        if (endYear && pageYear.sort > endYear.sort) return "";

        let validWhereabouts = [];
        let homeWhereabouts;

        for (w of metadata.whereabouts) {
            if (w.date == undefined) {
                if (w.type == "home") homeWhereabouts = w;
                continue;
            }

            if (metadataUtils.parse_date_to_events_date(w.date).sort > pageYear.sort) {
                console.log("skipping - too late")
                continue;
            };
            
            let date_end = w.date_end;
            if (date_end == undefined && w.type == "visit") date_end = w.date;

            if (date_end != undefined)
            {
                if (metadataUtils.parse_date_to_events_date(date_end).sort < pageYear.sort) {
                    console.log("skipping - already over")
                    continue;
                }   
            } 

            validWhereabouts.push(w);
            validWhereabouts.sort((a,b) =>  compare_event_dates(metadataUtils.parse_date_to_events_date(a.date),metadataUtils.parse_date_to_events_date(b.date)))
        }

        let outputString = "Current location: (as of " + pageYear.display + "): ";
        if (validWhereabouts.length > 0) {
            let actualWhereabout = validWhereabouts.slice(-1)[0]
            console.log(actualWhereabout)
            let whereaboutsName = "";
            if (actualWhereabout.region || actualWhereabout.place) whereaboutsName = metadataUtils.get_Location(actualWhereabout);
            else if (actualWhereabout.type == "travel") whereaboutsName = "travelling";
            else if (actualWhereabout.type == "visit") whereaboutsName = "(unknown stop)"           
            else if (actualWhereabout.type == "home") whereaboutsName = "(unknown home)"           

            outputString += whereaboutsName;           
        } 
        else if (homeWhereabouts != undefined) {
            outputString += metadataUtils.get_Location(homeWhereabouts);
        } else {
            outputString += "(unknown)"
        }

        return outputString;
    }

    return ""
}

return get_Whereabouts(dv.current());
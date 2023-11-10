class metadataUtils {
    
    get_date_sort_string(jsDate) {
        return jsDate.getUTCFullYear().toString().padStart(4, '0') + (jsDate.getUTCMonth() + 1).toString().padStart(2, '0') + jsDate.getUTCDate().toString().padStart(2, '0');
    }
    
    get_currentYear() {
        return window.FantasyCalendarAPI.getCalendars()[0].current.year;
    }

    get_currentEventsDate() {        
        return this.parse_date_to_events_date(window.FantasyCalendarAPI.getCalendars()[0].current);
    }


    get_displayDate(jsDate) {
        return this.get_displayDateFromPieces(jsDate.getUTCDate(),  jsDate.getUTCMonth(), jsDate.getUTCFullYear() )
    }

    get_displayDateFromPieces(day, month, year) {
        let currentFantasyCal = FantasyCalendarAPI.getCalendars()[0];
        let date = { year: year, month: month, day: day };        
        return FantasyCalendarAPI.getDay(date, currentFantasyCal).displayDate;
    }

    parse_date_to_events_date(inputDate) {
        let jsDate = new Date(1, 0, 0, 0, 0, 0, 0);
     
        switch (typeof (inputDate)) {
            case "number":
                // this is a bare year           
                jsDate.setDate(1)
                jsDate.setMonth(0)    
                jsDate.setFullYear(inputDate)            
                return { display: "DR " + inputDate, sort: this.get_date_sort_string(jsDate), year: inputDate, jsDate : jsDate };
    
            case "string":
                // this is a string which we expect is either yyyy-mm-dd or yyyy-mm but something is wrong, most likely the actual year is not 4 digits
                let splitString = inputDate.split("-")            
                if (splitString.length == 3) {                
                    jsDate.setDate(parseInt(splitString[2]))
                    jsDate.setMonth(parseInt(splitString[1]) - 1)                 
                    jsDate.setFullYear(parseInt(splitString[0]))
                    return { display: this.get_displayDate(jsDate), sort: this.get_date_sort_string(jsDate), year: jsDate.getUTCFullYear(), jsDate : jsDate };
                }
                else if (splitString.length == 2) {
                    let monthInt =parseInt(splitString[1]) - 1;
                    jsDate.setDate(1)
                    jsDate.setMonth(monthInt)
                    jsDate.setFullYear(parseInt(splitString[0]))      

                    let display = FantasyCalendarAPI.getCalendars()[0].static.months[monthInt].name + " " + splitString[0];
                
                    return { display: display, sort: this.get_date_sort_string(jsDate), year: jsDate.getUTCFullYear(), jsDate : jsDate };
                }
    
            case "object":
                if (inputDate.year == undefined) {
                    console.log("Error - unable to parse input date that is an object but doesn't have a year: " + inputDate)
                    return undefined;
                }
            
                if (inputDate.isLuxonDateTime) {
                    jsDate.setDate(inputDate.day ?? 1)
                    jsDate.setMonth(inputDate.month - 1 ?? 0)
                    jsDate.setFullYear(inputDate.year)                
                } else {
                    // fantasy calendar, don't subtract 1
                    jsDate.setDate(inputDate.day ?? 1)
                    jsDate.setMonth(inputDate.month ?? 0)
                    jsDate.setFullYear(inputDate.year)   
                }
                return { display: this.get_displayDate(jsDate), sort: this.get_date_sort_string(jsDate), year: jsDate.getUTCFullYear(), jsDate : jsDate };
        }
    
        console.log("Error - unable to parse input date: " + inputDate)
        return undefined;
    }

    get_currentDisplayDate() {
        let currentYear = window.FantasyCalendarAPI.getCalendars()[0].current.year;
        let currentMonth = window.FantasyCalendarAPI.getCalendars()[0].current.month;
        let currentDay = window.FantasyCalendarAPI.getCalendars()[0].current.day;

        return this.get_displayDateFromPieces(currentDay, currentMonth, currentYear);
    }

    reformat_metadata_item(metadata, value, front_string, end_string, unknown_value) {
        if (metadata[value]) {
            return front_string + metadata[value] + end_string
        }
        else {
            return unknown_value
        }
    }

    get_Location (place) {
        
        if (place == undefined) return "";        
        if (place.region == undefined && place.place == undefined) return this.get_LocationFromPieces("", place)
       
        return this.get_LocationFromPieces(place.place, place.region)
    } 

    get_LocationFromPieces (place, region) {
        // construct variables //
        let loc = place
        let locRegion = region
        let locArray = []
    
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
    
        let locArrayValues = locArray.map(function(f) {
            let pieceValue = f.trim();

            let file = window.app.vault.getFiles().find(f => f.basename == pieceValue);
            if (file != undefined) { return "[[" + pieceValue + "]]";  }
            return pieceValue;
        });
        
        return locArrayValues.join(', ');
    }

    get_pageEventsDate(metadata) {
        
        if (metadata.yearOverride) {
            return this.parse_date_to_events_date(metadata.yearOverride);
        }

        return this.get_currentEventsDate();
    }

    get_pageYear(metadata) {
        return this.get_pageEventsDate(metadata).year
    }

    get_existYear(metadata) {
        let date = this.get_existEventsDate(metadata)
        if (date) return date.year;
        return date;
    }

    get_endYear(metadata) {
        let date = this.get_endEventsDate(metadata)
        if (date) return date.year;
        return date;
    }

    get_Age(older, younger) {

        let jsOlder = older.jsDate ?? older
        let jsYounger = younger.jsDate ?? younger
        var yearsDiff = jsOlder.getFullYear() - jsYounger.getFullYear();
                
        if (jsYounger.getMonth() > jsOlder.getMonth()) return yearsDiff - 1;
        else if (jsYounger.getMonth() == jsOlder.getMonth() && jsYounger.getDate() > jsOlder.getDate()) return yearsDiff - 1;

        return yearsDiff;
    }

    get_existEventsDate(metadata) {

        if (metadata.type == "Ruler" || metadata.type == "NPC" || metadata.type == "PC") {
            if (!metadata.born) return undefined;
            return this.parse_date_to_events_date(metadata.born);
        }
        if (metadata.type == "Building") {
            if (!metadata.built) return undefined;
            return this.parse_date_to_events_date(metadata.builtn);
        }
        if ( metadata.type == "Item") {
            if (!metadata.created) return undefined;
            return this.parse_date_to_events_date(metadata.created);
        }
        if (metadata.type == "Place") {
            if (!metadata.founded) return undefined;
            return this.parse_date_to_events_date(metadata.founded);
        }

        if (metadata.born) {
            return this.parse_date_to_events_date(metadata.born);
        }
        else if (metadata.built) {
            return this.parse_date_to_events_date(metadata.built);
        }
        else if (metadata.created) {
            return this.parse_date_to_events_date(metadata.created);
        } else if (metadata.founded) {
            return this.parse_date_to_events_date(metadata.founded);
        } else {
            return undefined;
        }
    }

    get_endEventsDate(metadata) {
        if (metadata.type == "Ruler" || metadata.type == "NPC" || metadata.type == "PC") {
            if (!metadata.died) return undefined;
            return this.parse_date_to_events_date(metadata.died);
        }
        else if (metadata.type == "Building" || metadata.type == "Item" || metadata.type == "Place") {
            if (!metadata.destroyed) return undefined;
            return this.parse_date_to_events_date(metadata.destroyed);
        }
      
        if (metadata.died) {
            return this.parse_date_to_events_date(metadata.died);
        }
        else if (metadata.destroyed) {
            return this.parse_date_to_events_date(metadata.destroyed);
        }

        return undefined;
    }

    get_Pronouns(metadata) {
        
        // if pronouns are defined in note metadata, use those

        if (metadata.pronouns) {
            return metadata.pronouns
        }
    
        // otherwise calculate pronouns from note metadata gender
        
        if (metadata.gender == "male") {
            return "he/him"
        } else if (metadata.gender == "female") {
            return "she/her"
        } 
    
        // if no gender or nonbinary, use they/them pronouns
        return "they/them"
    }
}

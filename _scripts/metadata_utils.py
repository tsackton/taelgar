## IMPLEMENT FUNCTIONS FROM metadataUtils.js ##
import os
import json
from pathlib import Path
import urllib.parse 
import datetime

def get_Age(older, younger):
    # Check if the inputs are datetime objects or integers (years)
    if isinstance(older, datetime) and isinstance(younger, datetime):
        years_diff = older.year - younger.year
        if younger.month > older.month or (younger.month == older.month and younger.day > older.day):
            return years_diff - 1
    elif isinstance(older, int) and isinstance(younger, int):
        years_diff = older - younger
    else:
        raise ValueError("Both parameters must be either datetime objects or integers representing years.")

    return years_diff


def get_link(string, file, links):
    if string in links:
        dest = links[string]
        orig = links[Path(file).stem].parent
        linkpath = os.path.relpath(dest,orig)
        return "[" + string + "](" + urllib.parse.quote(linkpath) + ")"
    else:
        return string

def get_date_sort_string(py_date):
    '''     
    get_date_sort_string(jsDate) {
        return jsDate.getUTCFullYear().toString().padStart(4, '0') + (jsDate.getUTCMonth() + 1).toString().padStart(2, '0') + jsDate.getUTCDate().toString().padStart(2, '0');
    }
    '''
    return py_date.strftime('%Y%m%d')

def get_currentYear(directory):   
    '''
    get_currentYear() {
        return window.FantasyCalendarAPI.getCalendars()[0].current.year;
    }
    ''' 
    with open(os.path.join(directory, 'plugins', 'fantasy-calendar', 'data.json'), 'r', 2048, "utf-8") as f:
        data = json.load(f)
        return data['calendars'][0]['current']['year']

def get_currentEventsDate(directory):
    '''
    get_currentEventsDate() {        
        return this.parse_date_to_events_date(window.FantasyCalendarAPI.getCalendars()[0].current);
    }
    '''    
    with open(os.path.join(directory, 'plugins', 'fantasy-calendar', 'data.json'), 'r', 2048, "utf-8") as f:
        data = json.load(f)
        return parse_date_to_events_date(data['calendars'][0]['current'])

def get_displayDate(py_date):
    '''
    get_displayDate(jsDate) {
        return this.get_displayDateFromPieces(jsDate.getUTCDate(),  jsDate.getUTCMonth(), jsDate.getUTCFullYear() )
    }
    '''
    return get_displayDateFromPieces(py_date.day, py_date.month, py_date.year)

def get_displayDateFromPieces(directory, day, month, year):
    '''
    get_displayDateFromPieces(day, month, year) {
        let currentFantasyCal = FantasyCalendarAPI.getCalendars()[0];
        let date = { year: year, month: month, day: day };        
        return FantasyCalendarAPI.getDay(date, currentFantasyCal).displayDate;
    }
    '''
    with open(os.path.join(directory, 'plugins', 'fantasy-calendar', 'data.json'), 'r', 2048, "utf-8") as f:
        data = json.load(f)
        currentFantasyCal = data['calendars'][0]
        displayMonth = currentFantasyCal['static']['months'][month]["name"]
        displayYear = year
        displayDay = day
        return(displayMonth + " " + displayDay + ", " + displayYear)

def get_currentDisplayDate(directory):
    '''
    get_currentDisplayDate() {
        let currentYear = window.FantasyCalendarAPI.getCalendars()[0].current.year;
        let currentMonth = window.FantasyCalendarAPI.getCalendars()[0].current.month;
        let currentDay = window.FantasyCalendarAPI.getCalendars()[0].current.day;

        return this.get_displayDateFromPieces(currentDay, currentMonth, currentYear);
    }
    '''
    with open(os.path.join(directory, 'plugins', 'fantasy-calendar', 'data.json'), 'r', 2048, "utf-8") as f:
        data = json.load(f)
        currentFantasyCal = data['calendars'][0]['current']
        return get_displayDateFromPieces(currentFantasyCal['day'], currentFantasyCal['month'], currentFantasyCal['year'])

def reformat_metadata_item(metadata, value, front_string, end_string, unknown_value):
    '''
    reformat_metadata_item(metadata, value, front_string, end_string, unknown_value) {
        if (metadata[value]) {
            return front_string + metadata[value] + end_string
        }
        else {
            return unknown_value
        }
    }
    '''
    if value in metadata and metadata[value] is not None:
        return front_string + str(metadata[value]) + end_string
    else:
        return unknown_value

def get_Location(place, file, links):
    '''
    get_Location (place) {
        
        if (place == undefined) return "";        
        if (place.region == undefined && place.place == undefined) return this.get_LocationFromPieces("", place)
       
        return this.get_LocationFromPieces(place.place, place.region)
    } 
    '''
    if place is None: return ""
    if (place['region'] is None and place['place'] is None): return get_LocationFromPieces("", place)
    return get_LocationFromPieces(place['place'], place['region'], file, links)

def get_LocationFromPieces(place, region, file, links):
    '''
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
    '''
    loc = place
    locRegion = region
    locArray = []
    loc_array_values = []
    if (loc is not None):
        if (locRegion is not None): 
            locArray = loc.split(',')
            locArray.append(locRegion)
        else:
            locArray = loc.split(',')
    else:
        if (locRegion is not None): 
            locArray = locRegion.split(',')
        else:   
            # no values
            return ""

    for f in locArray:
        piece_value = f.strip()
        loc_array_values.append(get_link(piece_value, file, links))
    
    return ', '.join(loc_array_values)


def get_pageEventsDate(metadata): 
    '''
    get_pageEventsDate(metadata) {
        
        if (metadata.yearOverride) {
            return this.parse_date_to_events_date(metadata.yearOverride);
        }

        return this.get_currentEventsDate();
    }
    '''
    if 'yearOverride' in metadata and metadata['yearOverride'] is not None:
        return parse_date_to_events_date(metadata['yearOverride'])
    return get_currentEventsDate()

def get_RegnalValue(metadata):
    
    currentYear = int(metadata["curYear"])

    yearStart = metadata.get("reignStart")
    yearEnd = metadata.get("reignEnd")
    
    if yearEnd == None: yearEnd = metadata.get("died")
    
    if yearStart is None: 
        return ""
    else:
        if (yearEnd is None) or (yearEnd is not None and yearEnd >= currentYear):
            reignLength = currentYear - yearStart
            return "reigning since " + str(yearStart) + " (" + str(reignLength) + " years)"
        else:
            if yearStart and yearEnd and yearStart > yearEnd: return "**(timetraveler, check your YAML)**"
            if yearStart > currentYear: return ""
    
    return "reigned " + str(yearStart) + " - " + str(yearEnd) + " (" + str(yearEnd-yearStart) + " years)"

def get_PageDatedValue(metadata):

    currentYear = int(metadata["curYear"])

    if metadata.get("type") == "NPC":
        yearStart = metadata.get("born")
        yearEnd = metadata.get("died")
        preExistError = metadata.get("preExistError", "**(not yet born)**")
        startPrefix = metadata.get("startPrefix", "b.")
        endPrefix = metadata.get("endPrefix", "d.")
        endStatus = metadata.get("endStatus", "died")
    elif metadata.get("type") == "Ruler":
        yearStart = metadata.get("born")
        yearEnd = metadata.get("died")
        preExistError = metadata.get("preExistError", "**(not yet born)**")
        startPrefix = metadata.get("startPrefix", "b.")
        endPrefix = metadata.get("endPrefix", "d.")
        endStatus = metadata.get("endStatus", "died")
    elif metadata.get("type") == "Building":
        yearStart = metadata.get("built")
        yearEnd = metadata.get("destroyed")
        preExistError = metadata.get("preExistError", "**(not yet built)**")
        startPrefix = metadata.get("startPrefix", "built")
        endPrefix = metadata.get("endPrefix", "destroyed")
        endStatus = metadata.get("endStatus", "destroyed")
    elif metadata.get("type") == "Item":
        yearStart = metadata.get("created")
        yearEnd = metadata.get("destroyed")
        preExistError = metadata.get("preExistError", "**(not yet created)**")
        startPrefix = metadata.get("startPrefix", "created")
        endPrefix = metadata.get("endPrefix", "destroyed")
        endStatus = metadata.get("endStatus", "destroyed")
    else: 
        yearStart = None
        yearEnd = None
    
    if yearStart is None: 
        if yearEnd is None: 
            return "unknown age"
        else:
            if yearEnd <= currentYear: return endPrefix + " " + str(yearEnd) + ", " + endStatus + " at unknown age"
            return "unknown age"
    else:
        if yearEnd is None:
            if yearStart > currentYear: return preExistError
            age = currentYear - yearStart
            return startPrefix + " " + str(yearStart) + " (" + str(age) + " years old)"
        else:
            if yearStart > yearEnd: return "**(timetraveler, check your YAML)**"
            if yearStart > currentYear: return preExistError
            if yearEnd <= currentYear:
                return startPrefix + " " + str(yearStart) + " - " + endPrefix + " " + str(yearEnd) +  ", " + endStatus + " at " + str(yearEnd-yearStart) + " years old"
            return startPrefix + " " + str(yearStart) + " (" + str(currentYear-yearStart) + " years old)"

def get_HomeWhereabouts(metadata,file_name,links):
    cur_year = datetime.date(int(metadata["curYear"]),1,1)
    
    if "whereabouts" not in metadata:
        return ""
    
    home_whereabouts = [w for w in metadata["whereabouts"] if w["type"] == "home" and w.get("date",datetime.date(1,1,1)) <= cur_year]
    if home_whereabouts:
        most_recent_home = max(home_whereabouts, key=lambda x: x.get("date",datetime.date(1,1,1)))
        home =  most_recent_home["place"] + ","  + most_recent_home["region"]
        home_parts =  [x.strip() for x in home.split(',')]
        home_text = [get_link(x,file_name,links) for x in home_parts]
        return "Based in: " + ", ".join(home_text)
    else:
        return ""

def get_Existence(metadata):
    # get start year
    
    yearStart = None

    if metadata.get("type") == "NPC":
        yearStart = metadata.get("born")
    elif metadata.get("type") == "Ruler":
        yearStart = metadata.get("born")
    elif metadata.get("type") == "Building":
        yearStart = metadata.get("built")
    elif metadata.get("type") == "Item":
        yearStart = metadata.get("created")

    if yearStart and (yearStart > int(metadata["curYear"])):
        return False
    else:
        return True


def parse_date_to_events_date():
    # NOT IMPLEMENTED
    return None

## FUNCTIONS TO IMPLEMENT BELOW ##

'''



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

'''
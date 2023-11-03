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

function get_date_sort_string(jsDate) {
    return jsDate.getUTCFullYear().toString().padStart(4, '0') + (jsDate.getUTCMonth() + 1).toString().padStart(2, '0') + jsDate.getUTCDate().toString().padStart(2, '0');
}

function get_displayDate(jsDate) {

    let currentFantasyCal = window.FantasyCalendarAPI.getCalendars()[0];
    let date = { year: jsDate.getUTCFullYear(), month: jsDate.getUTCMonth(), day: jsDate.getUTCDate() };
    return window.FantasyCalendarAPI.getDay(date, currentFantasyCal).displayDate;
}

function parse_date_to_events_date(inputDate) {
    let jsDate = new Date(1, 0, 0, 0, 0, 0, 0);

    switch (typeof (inputDate)) {
        case "number":
            // this is a bare year           
            jsDate.setMonth(0)
            jsDate.setDate(1)
            jsDate.setFullYear(inputDate)

            return { display: "DR " + inputDate, sort: get_date_sort_string(jsDate), year: inputDate };

        case "string":
            // this is a string which we expect is either yyyy-mm-dd or yyyy-mm but something is wrong, most likely the actual year is not 4 digits
            let splitString = inputDate.split("-")
            if (splitString.length == 3) {
                jsDate.setFullYear(parseInt(splitString[0]))
                jsDate.setMonth(parseInt(splitString[1]) - 1)
                jsDate.setDate(parseInt(splitString[2]))

                return { display: get_displayDate(jsDate), sort: get_date_sort_string(jsDate), year: jsDate.getUTCFullYear() };
            }
            else if (splitString.length == 2) {
                jsDate.setFullYear(parseInt(splitString[0]))
                jsDate.setMonth(parseInt(splitString[1]) - 1)
                jsDate.setDate(1)

                return { display: get_displayDate(jsDate), sort: get_date_sort_string(jsDate), year: jsDate.getUTCFullYear() };
            }

        case "object":
            if (inputDate.year == undefined) {
                console.log("Error - unable to parse input date that is an object but doesn't have a year: " + inputDate)
                return undefined;
            }

            jsDate.setFullYear(inputDate.year)
            jsDate.setMonth(inputDate.month - 1 ?? 0)
            jsDate.setDate(inputDate.day ?? 1)
            return { display: get_displayDate(jsDate), sort: get_date_sort_string(jsDate), year: jsDate.getUTCFullYear() };
    }

    console.log("Error - unable to parse input date: " + inputDate)
    return undefined;
}



async function get_table(input) {

    const metadataFilePath = app.vault.configDir + "/metadata.json";

    let metadataFile = await app.vault.adapter.read(metadataFilePath);
    let metadata = JSON.parse(metadataFile);

    let yearStart = input.yearStart;
    let yearEnd = input.yearEnd ?? input.yearStart;
    let pageFilter = input.pageFilter ?? "#event-source";
    let map = input.map ?? (f => [f.date, f.text, dv.fileLink(f.file)])
    let header = input.header ?? ["Date", "Event", "File"]
    let options = {
        includeBirth: input.includeBirth ?? input.includeAll ?? false,
        includeDeath: input.includeDeath ?? input.includeAll ?? false,
        includeRegnal: input.includeRegnal ?? input.includeAll ?? false,
        includeExcursions: input.includeExcursions ?? input.includeAll ?? false,
        includePartyMeetings: input.includePartyMeetings ?? input.includeAll ?? false
    };

    return dv.table(header, dv.pages(pageFilter).flatMap(item => {
        let events = [];

        if (item.file.frontmatter.DR != null) {
            let jsDate = parse_date_to_events_date(item.file.frontmatter.DR)
            events.push({ year: jsDate.year, date: jsDate.display, text: item.file.name, rawText: item.file.name, file: item.file.name, sort: jsDate.sort })
        }

        if (options.includeBirth == true && item.file.frontmatter.born != null) {
            let jsDate = parse_date_to_events_date(item.file.frontmatter.born)

            let text = "[[" + item.file.name + "]] was born"
            if (item.file.frontmatter.whereabouts != null) {
                let origin = item.file.frontmatter.whereabouts.find(w => w.type === "origin");
                if (origin != undefined) {
                    text += " in " + get_Location(origin.place, origin.region)
                }
                else {
                    let homeCount = item.file.frontmatter.whereabouts.filter(w => w.type === "home").length;
                    if (homeCount == 1) {
                        let home = item.file.frontmatter.whereabouts.find(w => w.type === "home");
                        text += " in " + get_Location(home.place, home.region)
                    }
                }
            }
            events.push({ year: jsDate.year, date: jsDate.display, text: text, rawText: text, file: item.file.name, sort: jsDate.sort })
        }
        if ((options.includeDeath == true || (options.includeRegnal && item.file.frontmatter.reignEnd == null)) && item.file.frontmatter.died != null) {
            let jsDate = parse_date_to_events_date(item.file.frontmatter.died)
            let dieString = item.file.frontmatter.endStatus ?? "died";
            let text = "[[" + item.file.name + "]] " + dieString
            events.push({ year: jsDate.year, date: jsDate.display, text: text, rawText: text, file: item.file.name, sort: jsDate.sort })
        }
        if (options.includeRegnal == true && item.file.frontmatter.reignStart != null) {
            let jsDate = parse_date_to_events_date(item.file.frontmatter.reignStart)
            let text = "[[" + item.file.name + "]] was crowned"
            events.push({ year: jsDate.year, date: jsDate.display, text: text, rawText: text, file: item.file.name, sort: jsDate.sort })
        }
        if (options.includeRegnal == true && item.file.frontmatter.reignEnd != null) {
            let jsDate = parse_date_to_events_date(item.file.frontmatter.reignEnd)
            let text = "[[" + item.file.name + "]] reign ended"
            events.push({ year: jsDate.year, date: jsDate.display, text: text, rawText: text, file: item.file.name, sort: jsDate.sort })
        }
        if (options.includePartyMeetings && item.file.frontmatter.lastSeenByParty != null) {
            item.file.frontmatter.lastSeenByParty.filter(e => e.prefix != undefined).forEach(element => {
                let loc = item.file.frontmatter.whereabouts.findLast(s => s.date <= element.date);
                let locDisplay = "at unknown"
                if (loc != undefined) {
                    locDisplay = " at " + get_Location(loc.place, loc.region)
                }

                let partyName = "the party";
                let campaignData = metadata.campaigns;
                if (campaignData) {
                    let thisCampaign = campaignData.find(search => search.prefix == element.prefix);
                    if (thisCampaign) {
                        partyName = thisCampaign.partyName;
                        console.log(thisCampaign)
                        if (thisCampaign.partyFile) partyName = "[[" + thisCampaign.partyFile + "|" + partyName + "]]"
                    }
                }

                let jsDate = parse_date_to_events_date(element.date)
                let text = "[[" + item.file.name + "]] meet " + partyName + locDisplay
                events.push({ year: jsDate.year, date: jsDate.display, text: text, rawText: text, file: item.file.name, sort: jsDate.sort })
            });
        }

        if (options.includeExcursions == true && item.file.frontmatter.whereabouts != null) {
            console.log("whereabouts from " + item.file.name)
            let origin = item.file.frontmatter.whereabouts.find(w => w.type === "origin");
            let  homeCount = 0;
            item.file.frontmatter.whereabouts.forEach(element => {
                if (element.type == "home") {                    
                    if (origin == undefined && homeCount == 0) {
                       console.log("Skipping first home event as we don't have an origin, so first home is treated as origin")                    
                    }                    
                    else if (element.date == undefined) {
                        console.log("Whereabouts doesn't have a date. Skipping. " + item.file.name + " " + element);
                    }                    
                    else {
                        let push = true;
                        let verb = "moved"
                        if (origin.place == element.place && origin.region == element.region)
                        {
                            if (homeCount > 0) verb = "returned"                            
                            else push = false;
                        }      

                        let jsDate = parse_date_to_events_date(element.date)
                        let text = "[[" + item.file.name + "]] " + verb + " to "+ get_Location(element.place, element.region)
                        if (push) events.push({ year: jsDate.year, date: jsDate.display, text: text, rawText: text, file: item.file.name, sort: jsDate.sort })
                    }
                    homeCount++
                }
                if (element.type == "excursion" || element.excursion == true ) {
                    if (element.date == undefined) {
                        console.log("Whereabouts doesn't have a date. Skipping. " + item.file.name + " " + element);
                    }
                    else {
                        let jsDate = parse_date_to_events_date(element.date)
                        let text = "[[" + item.file.name + "]] went to " + get_Location(element.place, element.region)
                        events.push({ year: jsDate.year, date: jsDate.display, text: text, rawText: text, file: item.file.name, sort: jsDate.sort })
                    }
                }
            });
        }

        item.file.lists.where(t => t.DR != null).forEach(t => {

            let textWithDate = t.text;
            let pattern = /\(\w+:: \d{4}(?:-\d{2})?(?:-\d{2})?\):?/;
            let realText = textWithDate.replace(pattern, '').trim(); // trim() is used to remove any leading or trailing whitespace that may be left after the replacement

            if (t.DR != undefined) {
                let jsDate = parse_date_to_events_date(t.DR)
                var obj = { year: jsDate.year, date: jsDate.display, file: item.file.name, text: realText, rawText: t.text, sort: jsDate.sort };
            }

            events.push(obj)
        })

        return events;
    }
    ).where(f => f.year >= yearStart && f.year <= yearEnd).sort(f => f.sort).map(map))
}

return get_table(input);
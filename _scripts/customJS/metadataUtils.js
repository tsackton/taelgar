class metadataUtils {

    parse_date_to_events_date(inputDate, isEnd) {
        function daysInMonth(dm, dy) {
            return new Date(dy, dm, 0).getDate();
        }

        function get_date_sort_string(jsDate) {
            return jsDate.getFullYear().toString().padStart(4, '0') + (jsDate.getMonth() + 1).toString().padStart(2, '0') + jsDate.getDate().toString().padStart(2, '0');
        }

        function get_displayDate(jsDate) {

            let currentFantasyCal = FantasyCalendarAPI.getCalendars()[0];
            let date = { year: jsDate.getFullYear(), month: jsDate.getMonth(), day: jsDate.getDate() };
            return FantasyCalendarAPI.getDay(date, currentFantasyCal).displayDate;
        }


        let jsDate = new Date(1, 0, 0, 0, 0, 0, 0);

        if (inputDate== undefined) return undefined;

        switch (typeof (inputDate)) {
            case "number":
                // this is a bare year           
                jsDate.setDate(isEnd ? 31 : 1)
                jsDate.setMonth(isEnd ? 11 : 0)
                jsDate.setFullYear(inputDate)
                return { display: "DR " + inputDate, sort: get_date_sort_string(jsDate), year: inputDate, jsDate: jsDate };

            case "string":
                // this is a string which we expect is either yyyy-mm-dd or yyyy-mm but something is wrong, most likely the actual year is not 4 digits
                let splitString = inputDate.split("-")
                if (splitString.length == 3) {
                    jsDate.setDate(parseInt(splitString[2]))
                    jsDate.setMonth(parseInt(splitString[1]) - 1)
                    jsDate.setFullYear(parseInt(splitString[0]))
                    return { display: get_displayDate(jsDate), sort: get_date_sort_string(jsDate), year: jsDate.getFullYear(), jsDate: jsDate };
                }
                else if (splitString.length == 2) {
                    let monthInt = parseInt(splitString[1]);
                    let dayInMonth = daysInMonth(monthInt, 1999)
                    if (dayInMonth == 29) dayInMonth = 28;

                    jsDate.setMonth(monthInt - 1)
                    jsDate.setDate(isEnd ? dayInMonth : 1)
                    jsDate.setFullYear(parseInt(splitString[0]))

                    let display = FantasyCalendarAPI.getCalendars()[0].static.months[monthInt - 1].name + " " + splitString[0];

                    return { display: display, sort: get_date_sort_string(jsDate), year: jsDate.getFullYear(), jsDate: jsDate };
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
                return { display: get_displayDate(jsDate), sort: get_date_sort_string(jsDate), year: jsDate.getFullYear(), jsDate: jsDate };
        }

        console.log("Error - unable to parse input date: " + inputDate)
        return undefined;
    }

    get_Location(place) {
        function get_LocationFromPieces(singleLoc) {

            let locArrayValues = singleLoc.split(",").map(function (f) {
                let pieceValue = f.trim();

                let file = window.app.vault.getFiles().find(f => f.basename == pieceValue);
                if (file != undefined) { return "[[" + pieceValue + "]]"; }
                return pieceValue;
            });

            return locArrayValues.join(', ');
        }


        if (place == undefined) return "";
        if (place.region && !place.place) return get_LocationFromPieces(place.region)
        if (!place.region && place.place) return get_LocationFromPieces(place.place)
        if (place.region && place.place) return get_LocationFromPieces(place.place + "," + place.region)
        if (place.location) return get_LocationFromPieces(place.location)

        return get_LocationFromPieces(place)
    }


    get_pageEventsDate(metadata) {

        if (metadata.pageTargetDate) {
            return this.parse_date_to_events_date(metadata.pageTargetDate, false);
        }

        return this.parse_date_to_events_date(window.FantasyCalendarAPI.getCalendars()[0].current, false);
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
            return this.parse_date_to_events_date(metadata.born, false);
        }

        return this.parse_date_to_events_date(metadata.created, false);
    }

    get_endEventsDate(metadata) {
        if (metadata.type == "Ruler" || metadata.type == "NPC" || metadata.type == "PC") {
            if (!metadata.died) return undefined;
            return this.parse_date_to_events_date(metadata.died, true);
        }

        return this.parse_date_to_events_date(metadata.destroyed, true);
    }

    parseWhereabouts_to_datedWhereabouts(whereaboutItem) {
        let start = this.parse_date_to_events_date(whereaboutItem.start, false);
        let end = this.parse_date_to_events_date(whereaboutItem.end, true);
        let logicalEnd = end ?? start;
        let jsDateMin = new Date(0)
        

        return {
            item: whereaboutItem,
            normalizedStart: start ? start.jsDate : jsDateMin,
            startDate: start,
            endDate: end,
            logicalEnd: logicalEnd,
            duration: logicalEnd == undefined || start == undefined ? 0 : logicalEnd.jsDate - start.jsDate,
            type: whereaboutItem.type
        }
    }

    get_currentWhereabouts(metadata, targetDate) {
        let exactKnown = this.get_exactWhereabouts(metadata, targetDate)
        let home = this.get_homeWhereabouts(metadata, targetDate)
        let lastKnown = this.get_lastKnownWhereabouts(metadata, targetDate)

        if (exactKnown) return exactKnown;
        if (home && lastKnown) {
            let lastKnownEnd = this.parse_date_to_events_date(lastKnown.end)
            if (lastKnownEnd) {
                if (lastKnownEnd.sort < targetDate.sort) {
                    return home
                }
            }
        }
        else if (home) {
            return home;
        }

        return { location: undefined, type: "away"  }
    }

    get_lastKnownWhereabouts(metadata, targetDate) {
        function filter_lastKnown(f) {
            if (f.type == "away") {
                return (f.startDate != undefined && f.startDate.sort <= targetDate.sort)
            }
            else if (f.type == "home") {
                if (f.endDate) return f.endDate.sort < targetDate.sort;
            }

            return false;
        }
        let allowedWhereabouts = metadata.whereabouts.map(f => this.parseWhereabouts_to_datedWhereabouts(f))
            .filter(filter_lastKnown)
            .toSorted((a, b) => a.normalizedStart.jsDate - b.normalizedStart.jsDate);

        if (allowedWhereabouts.length > 0) return allowedWhereabouts.first().item;
        return undefined;
    }

    get_originWhereabouts(metadata) {
        let allowedWhereabouts = metadata.whereabouts.map(f => this.parseWhereabouts_to_datedWhereabouts(f)).filter(f => f.type == "home" && f.startDate == undefined);

        if (allowedWhereabouts.length > 0) return allowedWhereabouts.first().item;
        return undefined;
    }

    get_homeWhereabouts(metadata, targetDate) {
        function sort_date(a, b) {
            let indexA = a[0];
            let indexB = b[0];

            let startA = a[1].startDate;
            let startB = b[1].startDate;
            let endA = a[1].endDate;
            let endB = b[1].endDate;

            if (startA && startB)
                return startA.jsDate - startB.jsDate;
            
            if (startA)
                return 1;
            if (startB)
                return -1;

            if (!endA && !endB)
                return indexB - indexA;

            if (endA && endB)
                return endB.jsDate - endA.jsDate;

            if (endA)
                return -1;
            if (endB)
                return 1;

            // should be unreachable
            return 0;    
        }

        let allowedWhereabouts = metadata.whereabouts.map((f, index) => [index, this.parseWhereabouts_to_datedWhereabouts(f)]).filter(f => f[1].type == "home"
            && (f[1].startDate == undefined || f[1].startDate.sort <= targetDate.sort)
            && (f[1].endDate == undefined || (f[1].endDate && f[1].endDate.sort >= targetDate.sort)))
            .toSorted(sort_date)

        let hasOtherHomes = metadata.whereabouts.filter(f => f.type == "home").length > 1;

        if (allowedWhereabouts.length == 0) return undefined;

        let homePoss = allowedWhereabouts.first()[1];

        if (hasOtherHomes && allowedWhereabouts.length == 1 && !homePoss.startDate && !homePoss.endDate)
            return undefined;

        if (!homePoss.item.location)
            return undefined;

        return homePoss.item;
    }

    get_exactWhereabouts(metadata, targetDate) {
        let allowedWhereabouts = metadata.whereabouts.map(f => this.parseWhereabouts_to_datedWhereabouts(f)).filter(f => f.type == "away"
            && f.startDate
            && f.startDate.sort <= targetDate.sort
            && f.logicalEnd.sort >= targetDate.sort).toSorted((a, b) => a.duration - b.duration);


        if (allowedWhereabouts.length > 0) return allowedWhereabouts.first().item;
        return undefined;

    }
}

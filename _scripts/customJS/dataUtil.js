class DateManager {
    
    #getAge(older, younger) {

        if (older == undefined || younger == undefined) return undefined;

        let jsOlder = older.jsDate ?? older
        let jsYounger = younger.jsDate ?? younger
        var yearsDiff = jsOlder.getFullYear() - jsYounger.getFullYear();

        if (jsYounger.getMonth() > jsOlder.getMonth()) return yearsDiff - 1;
        else if (jsYounger.getMonth() == jsOlder.getMonth() && jsYounger.getDate() > jsOlder.getDate()) return yearsDiff - 1;

        return yearsDiff;
    }

    getPageDates(metadata, targetDate) {
        
        if (!targetDate) targetDate = this.getTargetDateForPage(metadata)

        let status = {
            startDate: undefined,
            startDescriptor: undefined,
            endDate: undefined,
            endDescriptor: undefined,
            isCreated: true,
            isAlive: true,
            age: undefined
        }

        if (metadata.displayDefaults) {
            status.startDescriptor = metadata.displayDefaults.startStatus
            status.endDescriptor = metadata.displayDefaults.endStatus
            status.startPrefix = metadata.displayDefaults.startPrefix
            status.endPrefix = metadata.displayDefaults.endPrefix
        }

        if (metadata.born) {
            status.startDate = this.normalizeDate(metadata.born, false);
            if (!status.startDescriptor) status.startDescriptor = "born";
        } else if (metadata.created) {
            status.startDate = this.normalizeDate(metadata.created, false);
            if (!status.startDescriptor) status.startDescriptor = "created";
        }

        if (metadata.died) {
            status.endDate = this.normalizeDate(metadata.died, true);
            if (!status.endDescriptor) status.endDescriptor = "died";
        } else if (metadata.destroyed) {
            status.endDate = this.normalizeDate(metadata.destroyed, true);
            if (!status.endDescriptor) status.endDescriptor = "destroyed";
        }

        if (status.startDate) {
            status.isCreated = status.startDate.sort < targetDate.sort;
        }

        if (status.endDate) {
            status.isAlive = status.endDate.sort >= targetDate.sort;
        } else {
            status.isAlive = status.isCreated
        }


        if (status.startDate) {
            if (status.isAlive) {
                status.age = this.#getAge(targetDate, status.startDate)
            }
            else if (status.endDate) {
                status.age = this.#getAge(status.endDate, status.startDate)
            }
        }


        if (!status.startPrefix && status.startDescriptor) status.startPrefix = status.startDescriptor[0] + "."
        if (!status.endPrefix && status.endDescriptor) status.endPrefix = status.endDescriptor[0] + "."

        return status;
    }
    
    getRegnalDates(metadata, targetDate) {
        
        if (!targetDate) targetDate = this.getTargetDateForPage(metadata)
        let status = { isStarted: undefined, isCurrent: undefined, startDate: undefined, endDate: undefined, length: undefined }

        status.endDate = this.normalizeDate(metadata.reignEnd, true) ?? this.normalizeDate(metadata.died, true);
        status.startDate = this.normalizeDate(metadata.reignStart, false)
        status.isStarted = status.startDate && status.startDate.sort <= targetDate.sort
        status.isCurrent = status.isStarted && (status.endDate == undefined || targetDate.sort < status.endDate.sort)

        if (status.startDate) {
            if (status.isCurrent) {
                status.length = this.#getAge(targetDate, status.startDate)
            }
            else if (status.endDate) {
                status.length = this.#getAge(status.endDate, status.startDate)
            }
        }

        return status;
    }

    getTargetDateForPage(metadata) {
        if (metadata && metadata.pageTargetDate) {
            return this.normalizeDate(metadata.pageTargetDate, false);
        }
        return this.normalizeDate(window.FantasyCalendarAPI.getCalendars()[0].current, false);
    }

    normalizeDate(inputDate, isEnd) {
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

        if (inputDate == undefined) return undefined;
        if (inputDate == "") return undefined;

        if (inputDate.isEventsDate) return inputDate

        switch (typeof (inputDate)) {
            case "number":
                // this is a bare year           
                jsDate.setDate(isEnd ? 31 : 1)
                jsDate.setMonth(isEnd ? 11 : 0)
                jsDate.setFullYear(inputDate)
                return { display: "DR " + inputDate, sort: get_date_sort_string(jsDate), year: inputDate, jsDate: jsDate, isEventsDate: true };

            case "string":
                // this is a string which we expect is either yyyy-mm-dd or yyyy-mm but something is wrong, most likely the actual year is not 4 digits
                let splitString = inputDate.split("-")
                if (splitString.length == 3) {
                    jsDate.setDate(parseInt(splitString[2]))
                    jsDate.setMonth(parseInt(splitString[1]) - 1)
                    jsDate.setFullYear(parseInt(splitString[0]))
                    return { display: get_displayDate(jsDate), sort: get_date_sort_string(jsDate), year: jsDate.getFullYear(), jsDate: jsDate, isEventsDate: true };
                }
                else if (splitString.length == 2) {
                    let monthInt = parseInt(splitString[1]);
                    let dayInMonth = daysInMonth(monthInt, 1999)
                    if (dayInMonth == 29) dayInMonth = 28;

                    jsDate.setMonth(monthInt - 1)
                    jsDate.setDate(isEnd ? dayInMonth : 1)
                    jsDate.setFullYear(parseInt(splitString[0]))

                    let display = FantasyCalendarAPI.getCalendars()[0].static.months[monthInt - 1].name + " " + splitString[0];

                    return { display: display, sort: get_date_sort_string(jsDate), year: jsDate.getFullYear(), jsDate: jsDate, isEventsDate: true };
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
                return { display: get_displayDate(jsDate), sort: get_date_sort_string(jsDate), year: jsDate.getFullYear(), jsDate: jsDate, isEventsDate: true };
        }

        console.log("Error - unable to parse input date: " + inputDate)
        return undefined;
    }

}
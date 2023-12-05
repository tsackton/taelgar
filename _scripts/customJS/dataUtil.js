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

    setPageDateProperties(pageDates, targetDate) {

        if (pageDates.startDate) {
            pageDates.isCreated = pageDates.startDate.sort <= targetDate.sort;
        } else {
            pageDates.isCreated = true
        }

        if (pageDates.endDate) {
            pageDates.isAlive = pageDates.endDate.sort >= targetDate.sort;
        } else {
            pageDates.isAlive = pageDates.isCreated
        }

        if (pageDates.startDate) {
            if (pageDates.isAlive) {
                pageDates.age = this.#getAge(targetDate, pageDates.startDate)
            }
            else if (pageDates.endDate) {
                pageDates.age = this.#getAge(pageDates.endDate, pageDates.startDate)
            }
        }
    }

    getPageDates(metadata, targetDate) {

        if (!targetDate) targetDate = this.getTargetDateForPage(metadata)

        let status = {
            startDate: undefined,
            endDate: undefined,
            isCreated: undefined,
            isAlive: undefined,
            age: undefined
        }

        let useDR = true;
        if ("born" in metadata || "died" in metadata || "created" in metadata || "destroyed" in metadata) {
            useDR = false;
        }

        if (metadata.born) {
            status.startDate = this.normalizeDate(metadata.born, false);
        } else if (metadata.created) {
            status.startDate = this.normalizeDate(metadata.created, false);
        } else if (metadata.DR && useDR) {
            status.startDate = this.normalizeDate(metadata.DR, false);
        }

        if (metadata.died) {
            status.endDate = this.normalizeDate(metadata.died, true);
        } else if (metadata.destroyed) {
            status.endDate = this.normalizeDate(metadata.destroyed, true);
        } else if ("DR_end" in metadata && useDR) {
            // this is to allow a blank DR_end to mean "unknown"
            if (metadata.DR_end) status.endDate = this.normalizeDate(metadata.DR_end, true);
        } else if (metadata.DR && useDR) {
            status.endDate = this.normalizeDate(metadata.DR, true);
        }

        this.setPageDateProperties(status, targetDate)

        return status;
    }


    getTargetDateForPage(metadata) {
        if (customJS.state.overrideDate) {
            return this.normalizeDate(customJS.state.overrideDate, false);
        }

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

            if (date.year == 9999) return ""
            if (date.year == 1 && ((date.month == 0 && date.day == 1) || (date.month == 11 && date.day == 31))) return ""

            return FantasyCalendarAPI.getDay(date, currentFantasyCal).displayDate;
        }


        let jsDate = new Date(1, 0, 0, 0, 0, 0, 0);

        if (inputDate == undefined) return undefined;
        if (inputDate == "") return undefined;

        let isString = typeof inputDate === 'string' || inputDate instanceof String

        if (!isString && inputDate.isNormalizedDate) return inputDate

        if (isString) {
            // this is a string which we expect is either yyyy-mm-dd or yyyy-mm but something is wrong, most likely the actual year is not 4 digits
            let splitString = inputDate.split("-")
            if (splitString.length == 3) {
                jsDate.setDate(parseInt(splitString[2]))
                jsDate.setMonth(parseInt(splitString[1]) - 1)
                jsDate.setFullYear(parseInt(splitString[0]))
                return { display: get_displayDate(jsDate), sort: get_date_sort_string(jsDate), year: jsDate.getFullYear(), jsDate: jsDate, isNormalizedDate: true,  isHiddenDate: false  };
            }
            else if (splitString.length == 2) {
                let monthInt = parseInt(splitString[1]);
                let dayInMonth = daysInMonth(monthInt, 1999)
                if (dayInMonth == 29) dayInMonth = 28;

                jsDate.setMonth(monthInt - 1)
                jsDate.setDate(isEnd ? dayInMonth : 1)
                jsDate.setFullYear(parseInt(splitString[0]))

                let display = FantasyCalendarAPI.getCalendars()[0].static.months[monthInt - 1].name + " " + splitString[0];

                return { display: display, sort: get_date_sort_string(jsDate), year: jsDate.getFullYear(), jsDate: jsDate, isNormalizedDate: true,  isHiddenDate: false };
            } else if (splitString.length == 1) {
                // bare year
                jsDate.setDate(isEnd ? 31 : 1)
                jsDate.setMonth(isEnd ? 11 : 0)
                jsDate.setFullYear(parseInt(splitString[0]))

                let display = "DR " + inputDate
            
                return { display: display, sort: get_date_sort_string(jsDate), year: inputDate, jsDate: jsDate, isNormalizedDate: true, isHiddenDate: splitString[0] == "9999" || splitString[0] == "0001" };
            } else {
                console.log("Unexpected incoming string: " + inputDate)
                return undefined
            }
        }

        switch (typeof (inputDate)) {
            case "number":
                // this is a bare year           
                jsDate.setDate(isEnd ? 31 : 1)
                jsDate.setMonth(isEnd ? 11 : 0)
                jsDate.setFullYear(inputDate)

                let display = "DR " + inputDate

                return { display: display, sort: get_date_sort_string(jsDate), year: inputDate, jsDate: jsDate, isNormalizedDate: true, isHiddenDate: inputDate == 9999 || inputDate == 1 };

            case "object":
                if (inputDate.year == undefined) {
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
                return { display: get_displayDate(jsDate), sort: get_date_sort_string(jsDate), year: jsDate.getFullYear(), jsDate: jsDate, isNormalizedDate: true, isHiddenDate: false };
        }
    
        return undefined;
    }

}
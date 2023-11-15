class DateManager {

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

        if (inputDate == undefined) return undefined;
        if (inputDate == "") return undefined;

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

}
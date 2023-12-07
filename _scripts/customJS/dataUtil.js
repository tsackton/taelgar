
// @ts-check
class DateManager {


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
                pageDates.age = targetDate.days - pageDates.startDate.days
            }
            else if (pageDates.endDate) {
                pageDates.age = pageDates.endDate.days - pageDates.startDate.days
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

    // DR counts from the 291st day of the 4132nd year in the Dwarven count
    // The 4132nd year of the dwarven calendar started on March 17th the year before Drankor was founded
    // March 17 - Jan 1 is 290 days. Easier to not include DR 1/1/1 in the count so we don't have to correct later
    // So DR 1/1/1 = (4132*365) + 291 but we want DROneDays to be the day before 1/1/1

    DROneDays = (4132 * 365) + 290

    #getDayInMonth(month) {
        switch (month) {
            case 1: return 31
            case 2: return 28
            case 3: return 31
            case 4: return 30
            case 5: return 31
            case 6: return 30
            case 7: return 31
            case 8: return 31
            case 9: return 30
            case 10: return 31
            case 11: return 30
            case 12: return 31
            default: return 0
        }
    }

    #getDaysSinceCreation(year, month, day) {

        // there is no 0 year, so year 1 day 1 is the first day of time
        let days = ((year - 1) * 365) + day

        if (month > 1) days += this.#getDayInMonth(1)
        if (month > 2) days += this.#getDayInMonth(2)
        if (month > 3) days += this.#getDayInMonth(3)
        if (month > 4) days += this.#getDayInMonth(4)
        if (month > 5) days += this.#getDayInMonth(5)
        if (month > 6) days += this.#getDayInMonth(6)
        if (month > 7) days += this.#getDayInMonth(7)
        if (month > 8) days += this.#getDayInMonth(8)
        if (month > 9) days += this.#getDayInMonth(9)
        if (month > 10) days += this.#getDayInMonth(10)
        if (month > 11) days += this.#getDayInMonth(11)

        return days
    }

    #getMonthName(month) {
        switch (month) {
            case 1: return "January";
            case 2: return "February";
            case 3: return "March";
            case 4: return "April";
            case 5: return "May";
            case 6: return "June";
            case 7: return "July";
            case 8: return "August";
            case 9: return "September";
            case 10: return "October";
            case 11: return "November";
            case 12: return "December";
        }
    }

    #getDisplayForDate(daysSinceCreation, targetFormat, error) {
        let convertedDays = 0

        if (error >= Number.MAX_SAFE_INTEGER) return ""

        if (targetFormat == "DR") {
            convertedDays = daysSinceCreation - this.DROneDays
        } else if (targetFormat == "CY") {
            convertedDays = daysSinceCreation
        }

        let startDays = convertedDays - error
        let endDays = convertedDays + error
        let year = Math.ceil(convertedDays / 365)

        if (startDays == endDays) {            
            return this.#getDisplayForDaysSinceCreation(startDays, targetFormat)
        }

        return targetFormat + " " + year

    }


    #getDisplayForDaysSinceCreation(daysSinceCreation, dateFormat) {

        let currentFantasyCal = FantasyCalendarAPI.getCalendars()[0];
        let convertedDays = daysSinceCreation

        
        let year = Math.ceil(convertedDays / 365)
        let day = 0
        let month = 0
        let remaining = convertedDays - ((year - 1) * 365)

        // DR calculation //

        if (dateFormat == "DR") {
            for (let mCount = 1; mCount <= 12; mCount++) {
                let daysInThisMonth = this.#getDayInMonth(mCount)
                if (remaining <= daysInThisMonth) {
                    day = remaining
                    month = mCount
                    break
                }

                remaining -= daysInThisMonth
            }
            let date = { year: year, month: month - 1, day: day };
            return FantasyCalendarAPI.getDay(date, currentFantasyCal).displayDate;
        }

        if (dateFormat == "CY") {
            let cycle = Math.ceil(remaining/73)
            remaining =  remaining - ((cycle-1) * 73)

            return "CY " + year + "." + cycle + "." + remaining
        }


        /* CY calculation 

        //if (dateFormat == "CY") {

            // each block of 73 days is 2 months (35 days each) plus 3 intercalary days

            let block = Math.ceil(remaining / 73)
            let remainingInBlock = remaining - ((block - 1) * 73)
            // month is block-1 * 2 + Math.ceil(remainingInBlock/35)
            console.log(remainingInBlock)
            let intercalDays = remainingInBlock > 70 ? remainingInBlock - 70 : 0
            console.log(intercalDays)
            remainingInBlock = remainingInBlock - intercalDays
            let blockPart = Math.ceil(remainingInBlock / 35)
            console.log(blockPart)
            month = ((block - 1) * 2) + blockPart
            let extraDays = remainingInBlock - ((blockPart - 1) * 35)
            let dayString = extraDays.toString().padStart(2, "0")
            if (intercalDays) {
                dayString = extraDays.toString().padStart(2, "0") + "." + intercalDays.toString()
            }
            return "CY " + year.toString() + "-" + month.toString().padStart(2, "0") + "-" + dayString
        }
*/
    }

    #getTargetDaysAndErrorFromString(dateStr) {

        let splitString = dateStr.split("-")

        if (splitString.length == 3) {
            let year = parseInt(splitString[0])
            let month = parseInt(splitString[1])
            let days = parseInt(splitString[2])
            return { days: this.#getDaysSinceCreation(year, month, days) }
        }
        else if (splitString.length == 2) {
            let year = parseInt(splitString[0])
            let month = parseInt(splitString[1])
            let daysInMonth = this.#getDayInMonth()
            return { days: this.#getDaysSinceCreation(year, month, daysInMonth / 2), error: daysInMonth / 2 }
        } else if (splitString.length == 1) {
            let year = parseInt(splitString[0])

            if (year == 1) return { days: 0, error: Number.MAX_SAFE_INTEGER }
            else if (year == 9999) return { days: Number.MAX_SAFE_INTEGER, error: Number.MAX_SAFE_INTEGER }
            return { days: this.#getDaysSinceCreation(year, 0, 183), error: 182 }
        } else {
            console.log("Unexpected incoming string: " + dateStr)
            return undefined
        }
    }

    normalizeDate(inputDate, isEnd, source) {

        if (inputDate == undefined) return undefined;
        if (inputDate == "") return undefined;

        let isString = typeof inputDate === 'string' || inputDate instanceof String

        if (!isString && inputDate.isNormalizedDate) return inputDate

        let format = "DR"
        if (source == "CY" || source == "CY_end") format = "CY"

        if (isString) {
            inputDate = { date: inputDate, format: source == "CY" || source == "CY_end" ? "CY" : "DR", error: 0 }
        } else if (typeof (inputDate) == "number") {
            inputDate = { date: inputDate.toString(), format: source == "CY" || source == "CY_end" ? "CY" : "DR", error: 0 }
        } else if (typeof (inputDate) == "object" && !inputDate.date) {
            if (inputDate.isLuxonDateTime) {
                inputDate = { date: inputDate.year + "-" + inputDate.month + "-" + inputDate.day, format: source == "CY" || source == "CY_end" ? "CY" : "DR", error: 0 }
            } else {
                // fantasy calendar, zero-counts months, add one             
                inputDate = { date: inputDate.year + "-" + (inputDate.month + 1) + "-" + inputDate.day, format: source == "CY" || source == "CY_end" ? "CY" : "DR", error: 0 }
            }
        }

        if (!inputDate.date) return undefined

        let daysSinceCreate = this.#getTargetDaysAndErrorFromString(inputDate.date)
        if (daysSinceCreate == undefined) return undefined

        if (daysSinceCreate.error) inputDate.error = daysSinceCreate.error

        let sort = daysSinceCreate.days
        let actualDays = daysSinceCreate.days
        if (daysSinceCreate.days < Number.MAX_SAFE_INTEGER && daysSinceCreate.days > 0) {
            actualDays = inputDate.format == "DR" ? (daysSinceCreate.days + this.DROneDays) : daysSinceCreate.days
            sort = actualDays + (isEnd ? inputDate.error : (inputDate.error * -1));
        }

        return {
            display: this.#getDisplayForDate(actualDays, "DR", inputDate.error),
            displayCY: this.#getDisplayForDate(actualDays, "CY", inputDate.error),
            sort: sort,
            days: actualDays,
            error: inputDate.error,
            isNormalizedDate: true,
            isHiddenDate: inputDate.error === Number.MAX_SAFE_INTEGER
        };
    }

}
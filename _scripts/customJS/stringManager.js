class StringFormatter {

    formats = "tsUUaAxQqny"

    #getDefaultTypeOf(metadata) {

        if (metadata.typeOf) return metadata.typeOf
        if ("typeOf" in metadata) return ""

        if (metadata.tags && metadata.tags.length > 0) {
            let baseTag = metadata.tags.filter(f => f.startsWith("item") || f.startsWith("place") || f.startsWith("organization") || f.startsWith("person")).first()
            if (baseTag) {
                let value = baseTag.split("/")
                if (value.length == 2) return value[1]
                return value[0]

            }
        }

        return undefined;
    }


    #getFormattedWhereaboutsString(whereabout, formatString, targetDate, sourcePageType) {

        const { LocationManager } = customJS

        const formatRegex = /^[!UutsaAnyxqQ]+$/;

        let format = "q"
        let filter = ""
        let firstFormat = ""

        let followDate = targetDate

        // if the away end date of the whereabout is before the target date, use that as the follow date
        if (whereabout.awayEnd && targetDate && whereabout.awayEnd.sort < targetDate.sort) {
            followDate = whereabout.awayEnd
        }

        let parsedFormat = formatString.split(";")
        if (parsedFormat.length == 1) {
            let containsFormatter = formatRegex.test(parsedFormat[0])
            if (containsFormatter) {
                firstFormat = parsedFormat[0]
            } else {
                filter = parsedFormat[0]
            }
        }
        else if (parsedFormat.length == 2) {
            firstFormat = parsedFormat[1]
            filter = parsedFormat[0]
        } else if (parsedFormat.lengtg == 3) {
            firstFormat = parsedFormat[1]
            filter = parsedFormat[0]
            format = parsedFormat[2]
        }

        if (whereabout.startFilter && !filter.includes("!")) {
            filter = whereabout.startFilter
        }

        return LocationManager.getCurrentLocationName(whereabout, targetDate, filter, sourcePageType, format, firstFormat)
    }


    getFormattedString(formatString, file, targetDate, dateOverride, additionalData, nameAlias, nameLinkTextOverride, sourcePageType) {

        const { NameManager } = customJS
        const { WhereaboutsManager } = customJS
        const { DateManager } = customJS
        const { AffiliationManager } = customJS

        let metadata = file.frontmatter
        let name = file.name

        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)

        let displayDefaults = NameManager.getDisplayData(metadata)
        let pageDateInfo = dateOverride ?? DateManager.getPageDates(metadata, targetDate)
        let pageType = NameManager.getPageType(metadata)

        let typeOf = this.#getDefaultTypeOf(metadata)


        // bcdeghjkmvwyz

        // r p l i o f reserved for location stuff

        // t: title case; s: lower case, u: initial upper case
        // a: indefinite article, A: indefinite article if first, x: no article, q: preposition
        // n: never link, y: always link
        // !: ignore the whereabouts format
        const regexp = /<(\([()a-zA-Z-:\s]+\))?([a-zA-Z]+):?([!0-9UutsaAnyRrPpLlIiOoFfxqQ;]+)?(\([()a-zA-Z-:\s]+\))?>/g;

        let resultString = formatString

        for (let matchItem of resultString.matchAll(regexp)) {

            //1: prefix, 2: key, 3: format, 4: suffix

            let key = matchItem[2].toLowerCase()
            let format = matchItem[3] ?? ""
            let prefix = matchItem[1]
            let suffix = matchItem[4]

            let beforeThis = resultString.substr(0, resultString.indexOf(matchItem[0])).trim()
            let isFirstPart = beforeThis.length == 0

            // replace A with a
            if (isFirstPart) format = format.replace("A", "a")
            if (isFirstPart) format = format.replace("U", "u")

            let value = metadata[key]
            if (additionalData && !value) {
                value = additionalData[key]
            }

            if (key == "name") {
                value = NameManager.getName(name, format, nameAlias, nameLinkTextOverride, sourcePageType)
            } else if (key == "pronunciation") {
                value = metadata.pronunciation
            } else if (key == "pronouns") {
                if (value == undefined) {
                    if (metadata.gender == "male") value = "he/him"
                    else if (metadata.gender == "female") value = "she/her"
                    else if (metadata.gender) value = "they/them"
                }
            } else if (key == "subtypeof" || key == "subtype") {
                value = NameManager.getName(metadata.subTypeOf, format, undefined, nameLinkTextOverride, sourcePageType)
            } else if (key == "maintype" || key == "typeof" || key == "type") {
                value = NameManager.getName(metadata.species, format, metadata.speciesAlias, nameLinkTextOverride, sourcePageType) ?? NameManager.getName(typeOf, format, metadata.typeOfAlias, nameLinkTextOverride, sourcePageType)
            } else if (key == "species") {
                value = NameManager.getName(metadata.species, format, metadata.speciesAlias, nameLinkTextOverride, sourcePageType)
            } else if (key == "current") {
                let wb = WhereaboutsManager.getWhereabouts(metadata, targetDate).current
                value = this.#getFormattedWhereaboutsString(wb, format, targetDate, pageType)
            } else if (key == "lastknowndate") {
                let wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
                if (wb.lastKnown.location && wb.lastKnown.awayEnd.sort <= targetDate.sort) {
                    value = wb.lastKnown.awayEnd.display
                } else {
                    if (targetDate) {
                        value = targetDate.display
                    } else {
                        value = DateManager.getTargetDateForPage(metadata).display
                    }
                }
            } else if (key == "lastknown") {
                let wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
                value = this.#getFormattedWhereaboutsString(wb.lastKnown, format, targetDate, pageType)
            } else if (key == "home") {
                let wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
                value = this.#getFormattedWhereaboutsString(wb.home, format, targetDate, pageType)
            } else if (key == "origin") {
                let wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
                value = this.#getFormattedWhereaboutsString(wb.origin, format, pageDateInfo.startDate ?? DateManager.normalizeDate("0001"), pageType)
            } else if (key == "loc" || key == "loclist") {
                value = " ( loc and loclist are no longer supported; use partof or current/home/origin depending )"
            } else if (key == "startdate") {
                if (pageDateInfo.startDate) {
                    value = pageDateInfo.startDate.display
                } else {
                    value = ""
                }
            } else if (key == "target" || key == "targetdate" || key == "currentdate") {
                if (targetDate) {
                    value = targetDate.display
                } else {
                    value = DateManager.getTargetDateForPage(metadata).display
                }
            } else if (key == "enddate") {
                if (pageDateInfo.endDate) {
                    value = pageDateInfo.endDate.display
                } else {
                    value = ""
                }
            } else if (key == "age" || key == "length") {
                if (pageDateInfo.age == 0) value = "0 years"
                else if (pageDateInfo.age == 1) value = "1 year"
                else if (pageDateInfo.age) value = pageDateInfo.age + " years"
                else value = ""
            } else if (key == "start") {
                value = NameManager.getName(displayDefaults.startStatus, format, undefined, nameLinkTextOverride, sourcePageType)
            } else if (key == "end") {
                value = NameManager.getName(displayDefaults.endStatus, format, undefined, nameLinkTextOverride, sourcePageType)
            } else if (key == "ka") {
                if (metadata.species != "elf" && !metadata.ka) {
                    value = ""
                } else {
                    value = NameManager.getName("ka") + " " + (metadata.ka ?? "unknown")
                }
            } else if (key == "population") {
                if (metadata.population) {
                    let intPop = parseInt(metadata.population)
                    if (intPop) value = "pop. " + metadata.population.toLocaleString()
                    else value = metadata.population
                } else {
                    value = ""
                }
            }
            else if (key == "partof") {
                value = AffiliationManager.getAffiliationPartOf(metadata, format)
            }
            else if (key == "primary") {
                value = AffiliationManager.getFormattedPrimaryAffiliations(metadata, targetDate)
            }
            else {
                value = NameManager.getName(value, format, undefined, nameLinkTextOverride, sourcePageType)
            }


            if (value) {
                if (prefix) {
                    value = prefix.substr(1, prefix.length - 2) + value
                }

                if (suffix) {
                    value = value + suffix.substr(1, suffix.length - 2)
                }
            }

            resultString = resultString.replace(matchItem[0], value ?? "")
        }

        resultString = (resultString.split(' ').map(f => f.trim()).filter(f => f.length > 0).join(' ')).trim()

        resultString = resultString.replace(new RegExp("\\*\\(\\s*\\)\\*", "g"), "")
        resultString = resultString.replace(new RegExp("\\(\\s*\\)", "g"), "")
        resultString = resultString.replace(new RegExp("\\(\\s*", "g"), "(")
        resultString = resultString.replace(new RegExp("\\s*\\)", "g"), ")")

        while (resultString.startsWith(',')) resultString = resultString.substr(1).trim()
        while (resultString.startsWith(':')) resultString = resultString.substr(1).trim()

        resultString = resultString.trim()

        while (resultString.endsWith(" of") || resultString.endsWith(" in") || resultString.endsWith(" on") || resultString.endsWith(":") || resultString.endsWith(",")) {
            let len = resultString.endsWith(",") || resultString.endsWith(":") ? 1 : 2
            resultString = resultString.substr(0, resultString.length - len).trim()
        }

        if (resultString == "**") return ""

        return resultString.trim()
    }
}
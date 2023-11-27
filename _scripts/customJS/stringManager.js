class StringFormatter {


    #getCasing(format) {

        let casing = customJS.NameManager.PreserveCase

        if (format.includes("a")) casing = customJS.NameManager.PreserveCase
        else if (format.includes("s")) casing = customJS.NameManager.LowerCase
        else if (format.includes("t")) casing = customJS.NameManager.TitleCase

        return casing
    }

    #getLinkType(format) {

        let linkType = customJS.NameManager.LinkIfExists
        if (format.includes("n")) linkType = customJS.NameManager.NoLink
        else if (format.includes("y")) linkType = customJS.NameManager.CreateLink

        return linkType
    }

    #getDefaultTypeOf(metadata) {

        if (metadata.typeOf) return metadata.typeOf;

        if (metadata.tags && metadata.tags.length > 0) {
            let baseTag = metadata.tags.filter(f => f.startsWith("item") || f.startsWith("place")).first()
            if (baseTag) {
                return baseTag.split("/")[0]
            }
        }

        return undefined;
    }

    #getSubTypeOf(metadata, type) {

        if (metadata.subTypeOf) return metadata.subTypeOf
        if ("subTypeOf" in metadata) return ""

        if (metadata.tags && metadata.tags.length > 0) {
            let baseTags = metadata.tags.filter(f => f.startsWith("item/") || f.startsWith("place/"))
            if (baseTags) {
                for (let tag of baseTags) {
                    if (tag.endsWith(type)) {
                        continue
                    }
                    else {
                        return tag.split('/')[1]
                    }
                }
            }
        }

        return undefined
    }

    #getFormattedLocationString(locValue, formatString, targetDate) {

        const { LocationManager } = customJS

        let linkType = this.#getLinkType(formatString)
        let casing = this.#getCasing(formatString)

        return LocationManager.getCurrentLocationName(locValue, targetDate, casing, formatString, linkType)
    }

    #getFormattedWhereaboutsString(whereabout, formatString, targetDate) {

        let followDate = targetDate

        // if the away end date of the whereabout is before the target date, use that as the follow date
        if (whereabout.awayEnd && targetDate && whereabout.awayEnd.sort < targetDate.sort) {
            followDate = whereabout.awayEnd
        } 

        let formatStringToUse = whereabout.format ?? formatString
        if (formatString.includes("!")) formatStringToUse = formatString

        return this.#getFormattedLocationString(whereabout.location, formatStringToUse, followDate)
    }


    getFormattedString(formatString, file, targetDate, dateOverride, additionalData) {

        const { NameManager } = customJS
        const { WhereaboutsManager } = customJS
        const { DateManager } = customJS
        const { AffiliationManager } = customJS

        let metadata = file.frontmatter
        let name = file.name

        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)

        let displayDefaults = NameManager.getDisplayData(metadata)
        let pageDateInfo = dateOverride ?? DateManager.getPageDates(metadata, targetDate)
        let defaultType = this.#getDefaultTypeOf(metadata);
        let actualType = metadata.typeOf
        let type = actualType ?? defaultType
        let subType = this.#getSubTypeOf(metadata, type)

        // r p l i o f reserved for location stuff

        // t: title case; s: lower case, u: initial upper case
        // a: indefinite article, A: indefinite article if first
        // n: never link, y: always link
        // !: ignore the whereabouts format
        const regexp = /<[a-zA-Z]+:*[!0-9UutsaAnyRrPpLlIiOoFf]*>/g;

        let resultString = formatString

        for (let matchItem of resultString.matchAll(regexp)) {

            let match = matchItem[0].replace("<", "").replace(">", "")
            let split = match.split(':')
            let key = split[0].toLowerCase()
            let format = ""

            if (split.length == 2) {
                format = split[1]
            }

            let linkType = this.#getLinkType(format)
            let casing = this.#getCasing(format)

            let value = metadata[key]
            if (additionalData && !value) {
                value = additionalData[key]
            }


            if (key == "name") {
                value = NameManager.getName(name, linkType, casing)
            } else if (key == "pronunciation") {
                value = metadata.pronunciation
            } else if (key == "typeof" || key == "type") {
                value = NameManager.getName(type, linkType, casing)
            } else if (key == "pronouns") {
                if (value == undefined) {
                    if (metadata.gender == "male") value = "he/him"
                    else if (metadata.gender == "female") value = "she/her"
                    else if (metadata.gender) value = "they/them"
                }
            } else if (key == "subtypeof" || key == "subtype") {
                value = NameManager.getName(subType, linkType, casing)
            } else if (key == "maintype") {
                value = NameManager.getName(metadata.subspecies ?? metadata.species ?? actualType ?? subType ?? defaultType, linkType, casing)
            } else if (key == "current") {
                let wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
                if (wb.current.location) {
                    value = this.#getFormattedWhereaboutsString(wb.current, format, targetDate)
                } else {
                    value = "Unknown"
                }
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
                if (wb.lastKnown.location) {
                    value = this.#getFormattedWhereaboutsString(wb.lastKnown, format, targetDate)
                } else {
                    value = "Unknown"
                }
            } else if (key == "home") {
                let wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
                if (wb.home.location) {
                    value = this.#getFormattedWhereaboutsString(wb.home, format, targetDate)
                } else {
                    value = "Unknown"
                }
            } else if (key == "origin") {
                let wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
                if (wb.origin.location) {
                    value = this.#getFormattedWhereaboutsString(wb.origin, format, pageDateInfo.startDate ?? DateManager.normalizeDate("0001"))
                } else {
                    value = "Unknown"
                }
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
                value = NameManager.getName(displayDefaults.startStatus, linkType, casing)
            } else if (key == "end") {
                value = NameManager.getName(displayDefaults.endStatus, linkType, casing)
            } else if (key == "ka") {
                if (metadata.species != "elf" && !metadata.ka) {
                    value = ""
                } else {
                    value = NameManager.getName("ka", linkType, casing) + " " + (metadata.ka ?? "unknown")
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
                value = AffiliationManager.getAffiliationPartOf(metadata, linkType, casing)
            }
            else if (key == "primary") {
                value = AffiliationManager.getFormattedPrimaryAffiliations(metadata, targetDate)
            }
            else {
                value = NameManager.getName(value, linkType, casing)
            }

            let beforeThis = resultString.substr(0, resultString.indexOf(matchItem[0])).trim()
            let isFirstPart = beforeThis.length == 0

            if (value) {
                let trimmedValue = value.replace("[[", "").replace("]]", "").replace("[", "").replace("]", "").toLowerCase()
                let firstChar = trimmedValue[0]
                let article = "a"
                if (firstChar == "a" || firstChar == "e" || firstChar == "i" || firstChar == "o" || firstChar == "u") {
                    article = "an"
                }

                if (format.includes("a") || (format.includes("A") && isFirstPart)) {
                    value = article + " " + value
                }

                if (format.includes("u") || (format.includes("U") && isFirstPart)) {
                    value = value.charAt(0).toUpperCase() + value.slice(1)
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
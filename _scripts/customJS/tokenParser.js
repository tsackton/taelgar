class TokenParser {

    // This class is responsible for parsing tokens and returning formatted strings
    // There are three main functions:
    // 1. parseDisplayString: takes a display string with words and tokens ("This is a <token>, print it."), 
    //      replaces each token with a formatted version, and returns a formatted string
    // 2. getFormattedToken: takes a token string (<token:format>) and returns a formatted string
    // 3. formatToken: takes a token object and returns a formatted string
    // Both functions take a string as the first argument, a file object as the second argument,
    // a targetDate as the third argument, and an overrides object as the fourth argument

    // Define the allowable filter and format characters
    // unused characters: b c d e g h j k m v w z
    // * format definitions * //
    /*** 
        t: title case; s: lower case, u: initial upper case
        a: indefinite article, A: indefinite article if first, x: no definite article, q: preposition, Q: no preposition
        n: never link, y: always link
        !: prefer this format if possible
    ***/

    formatChars = "qQaAxnytsUu!"

    // * filter definitions * //
    /*** 
        R = include regions only; r = exclude regions (i.e. places with typeOf region)
        L = include locations only; l = exclude locations
        P = include people only; p = exclude people
        I = include items only; i = exclude items
        F = include first step only; f = exclude first step
        O = include organizations only; o = exclude organizations
    ***/

    filterChars = "rRpPlLiIoOfF!"

    // isFirst allows for special handling of certain format specifiers which need to be conditional on the value being
    //  first 
    #parseTokenString(input, isFirst) {

        // extracts format and filter strings from the token string
        // Initial structure of the result
        let token = {
            token: null,
            prefix: null,
            suffix: null,
            filter: null,
            format: null, // format for the item, or if a chain, the first item in the chain
            chainFormat: null, // if a chain format for all items in the chain
            fullTokenText: input
        };

        // this is a complicated regex, but basically it is 6 groups:
        //      first, prefix: contained in (), any letters or spaces
        //      second, token: letters only
        //      third, filter: digit-digit, plus filter options
        //      fourth, first item format string: the standard format string options. Can be separated from the filter with an optional semi-colon
        //      fifth, the all item format string: the standard format string options. Must be separated from the filter with a semi colon
        //      sixth, suffix: contained in (), any letters or spaces
        const regexp = /<(\([()a-zA-Z-:*\s]+\))?([a-zA-Z]+):?([0-9]*[-]?[0-9]*[RrPpLlIiOoFf!]*)?;?([UutsaAnyxqQ]+)?;?([UutsaAnyxqQ]+)?(\([()a-zA-Z-:*\s]+\))?>/g;

        if (((input || '').match(regexp) || []).length !== 1) {
            return null;
        }

        let match = regexp.exec(input)
        if (match) {
            token.prefix = match[1] ?? ""
            token.token = match[2] ?? ""
            token.filter = match[3] ?? ""
            token.format = match[4] ?? ""
            token.chainFormat = match[5] ?? match[4] ?? ""
            token.suffix = match[6] ?? ""
        }

        // clean up tokens //
        // target, targetdate, and currentdate are all the same thing
        if (token.token == "target" || token.token == "currentdate") token.token = "targetdate"
        // length and age are the same //
        if (token.token == "length") token.token = "age"
        // end is shorthand for endStatus //
        if (token.token == "end" || token.token == "endstatus") token.token = "endStatus"
        // start is shorthand for startStatus //
        if (token.token == "start" || token.token == "startstatus") token.token = "startStatus"
        // subtype is the same as subtypeof //
        if (token.token == "subtype") token.token = "subtypeof"
        // typeof and type are the same as maintype //        
        if (token.token == "typeof" || token.token == "type") token.token = "maintype"

        if (token.format.includes("U") && isFirst) token.format.replace("U", "u")
        else token.format.replace("U", "")

        if (token.format.includes("A") && isFirst) token.format.replace("A", "a")
        else token.format.replace("A", "")

        return token
    }

    #getParameterCaseInsensitive(object, key) {
        // get case insensitive parameter from object
        const asLowercase = key.toLowerCase();
        return object[Object.keys(object)
            .find(k => k.toLowerCase() === asLowercase)
        ];
    }

    #getFormattedPrimaryAffiliations(value, token) {

    }

    #getFormattedCaseString(value, token) {
        // this is something that can never be meaningfully linked
        // and never has an article
        // but which might need casing rules

        const { NameManager } = customJS;

        // this probably just returns itself, but...
        let name = { name: value, linkText: "", indefiniteArticle: "", definiteArticle: "", linkTarget: undefined }

        return NameManager.formatName(name, token.format)
    }

    #getFormattedName(value, token) {
        // returns a formatted name
        // pass the format and the name to the name manager to generate a formatted name

        const { NameManager } = customJS;

        // this probably just returns itself, but...
        let name = NameManager.getNameObject(value)

        return NameManager.formatName(name, token.format)
    }

    #getFormattedWhereabout(whereabout, token, targetDate, metadata) {

        const { NameManager } = customJS;
        const { LocationManager } = customJS;

        // returns a formatted location chain
        let followDate = targetDate

        // if the away end date of the whereabout is before the target date, use that as the follow date
        if (whereabout.awayEnd && targetDate && whereabout.awayEnd.sort < targetDate.sort) {
            followDate = whereabout.awayEnd
        }
        if (whereabout.startFilter && !token.filter.includes("!")) {
            token.filter = whereabout.startFilter
        }

        let sourcePageType = NameManager.getPageType(metadata)

        return LocationManager.getCurrentLocationName(whereabout, followDate, token.filter, sourcePageType, token.chainFormat, token.format)

    }

    #getFormattedDate(value, token) {

        const { DateManager } = customJS;

        // returns a formatted date
        // right now this just normalizes the date and returns the display value
        return DateManager.normalizeDate(value).display
    }

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

    #formatToken(token, file, targetDate, overrides) {

        const { NameManager } = customJS
        const { WhereaboutsManager } = customJS
        const { DateManager } = customJS
        const { AffiliationManager } = customJS

        // Takes a token object and returns a formatted string

        // reused from https://stackoverflow.com/questions/171251/how-can-i-merge-properties-of-two-javascript-objects-dynamically

        function merge_options(obj1, obj2) {
            var obj3 = {};
            if (obj1) for (var attrname in obj1) { obj3[attrname] = obj1[attrname]; }
            if (obj2) for (var attrname in obj2) { obj3[attrname] = obj2[attrname]; }
            return obj3;
        }

        // overrides that are used elsewhere //
        // overrides.dateInfo replaces the dateInfo object that is computed by DateManager //

        let metadata = merge_options(file.frontmatter, overrides)

        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)
        let pageDateInfo = metadata.dateInfo ?? DateManager.getPageDates(metadata, targetDate)
        let displayDefaults = NameManager.getDisplayData(metadata)

        let value = "";


        // set formatting options //  
        // define four types of formatters //
        // none: no formatting, just return the value //
        // string: find the file represented by this string and apply linking and formatting //
        // date: apply date formatting //
        // locchain: build a location chain from this starting point //

        let formatter = "none"

        switch (token.token) {
            // date options //
            case "startdate":
                if (pageDateInfo.startDate) value = pageDateInfo.startDate
                formatter = "date"
                break;
            case "targetdate":
                if (targetDate) value = targetDate
                else value = DateManager.getTargetDateForPage(metadata)
                formatter = "date"
                break;
            case "enddate":
                if (pageDateInfo.endDate) value = pageDateInfo.endDate
                formatter = "date"
                break;
            case "lastknowndate":
                let wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
                if (wb.lastKnown.location && wb.lastKnown.awayEnd.sort <= targetDate.sort) {
                    value = wb.lastKnown.awayEnd
                } else {
                    if (targetDate) {
                        value = targetDate
                    } else {
                        value = DateManager.getTargetDateForPage(metadata)
                    }
                }
                formatter = "date"
                break;
            // end date options //

            // start name options //
            case "name":
                // special-case: lets us pick up a name object with the appriopriate aliases and such
                // from the overrides
                value = metadata.name?.isNormalizedName ? metadata.name : file.name
                formatter = "name"
                break;
            case "ancestry":
                value = NameManager.getNameObject(metadata.ancestry, undefined, undefined)
                formatter = "name"
                break
            case "subtypeof":
                value = NameManager.getNameObject(metadata.subTypeOf, undefined, undefined)
                formatter = "name"
                break
            case "maintype":
                // special case where we define a specific main type based on metadata //
                if (metadata.species) {
                    value = NameManager.getNameObject(metadata.species, undefined, { alias: metadata.speciesAlias })
                } else {
                    let typeOfStr = this.#getDefaultTypeOf(metadata)
                    value = NameManager.getNameObject(typeOfStr, undefined, { alias: metadata.typeOfAlias })
                }
                formatter = "name"
                break;
            case "subspecies":
                value = NameManager.getNameObject(metadata.subspecies)
                formatter = "name"
                break
            case "species":
                value = NameManager.getNameObject(metadata.species, undefined, { alias: metadata.speciesAlias })
                formatter = "name"
                break
            case "person":
                value = NameManager.getNameObject(metadata.person, undefined, undefined)
                formatter = "name"
                break
            // end name options //

            // casing only options //
            case "rarity":
                value = metadata.rarity
                formatter = "casing"
                break
            // end casing only options //

            // start none options //
            case "pronouns":
                if (metadata.pronouns) value = metadata.pronouns
                else if (metadata.gender == "male") value = "he/him"
                else if (metadata.gender == "female") value = "she/her"
                else if (metadata.gender) value = "they/them"
                formatter = "none"
                break;
            case "age":
                if (pageDateInfo.age == 0) value = "0 years"
                else if (pageDateInfo.age == 1) value = "1 year"
                else if (pageDateInfo.age) value = pageDateInfo.age + " years"
                formatter = "none"
                break;
            case "population":
                if (metadata.population) {
                    let intPop = parseInt(metadata.population)
                    if (intPop) value = "pop. " + metadata.population.toLocaleString()
                    else value = metadata.population
                }
                formatter = "none"
                break;
            // end none options //

            // start whereabout options //
            case "current":
                value = WhereaboutsManager.getWhereabouts(metadata, targetDate).current
                formatter = "whereabout"
                break;
            case "lastknown":
                value = WhereaboutsManager.getWhereabouts(metadata, targetDate).lastKnown
                formatter = "whereabout"
                break;
            case "home":
                value = WhereaboutsManager.getWhereabouts(metadata, targetDate).home
                formatter = "whereabout"
                break;
            case "origin":
                value = WhereaboutsManager.getWhereabouts(metadata, targetDate).origin
                targetDate = pageDateInfo.startDate ?? DateManager.normalizeDate("0001")
                formatter = "whereabout"
                break;

            // end locchain options //
            // various complicated options //
            case "ka":
                // ka is unusual because we want to link the word 'ka' to the page for the ka
                // but we don't want to link the number
                if (metadata.species != "elf" && !metadata.ka) {
                    value = ""
                }
                else {
                    value = this.#getFormattedName("ka") + " " + (metadata.ka ?? "unknown")
                }
                formatter = "none"
                break;
            // end complicated options //

            // REFACTOR OPTIONS //
            // these might need to be refactored but I don't really understand the affiliation code yet //

            case "partof":
                // currently we just use the affliation manager here to get a fully formatted string
                value = AffiliationManager.getAffiliationPartOf(metadata, token, targetDate)
                break;
            // END REFACTOR OPTIONS //

            default:
                // if no special processing, check to see if it is a key in metadata, or failing that, displayDefaults
                value = (this.#getParameterCaseInsensitive(metadata, token.token) ?? this.#getParameterCaseInsensitive(displayDefaults, token.token)) ?? ""
                // default formatter is casing
                formatter = "casing"
        }

        if (value) {

            let finalStr = token.prefix.slice(1, -1)
            if (formatter == "name") {
                finalStr += this.#getFormattedName(value, token)
            } else if (formatter == "date") {
                finalStr += this.#getFormattedDate(value, token, targetDate, metadata)
            } else if (formatter == "whereabout") {
                finalStr += this.#getFormattedWhereabout(value, token, targetDate, metadata)
            } else if (formatter === "casing") {
                finalStr += this.#getFormattedCaseString(value, token)
            } else {
                finalStr += value
            }

            finalStr += token.suffix.slice(1, -1)

            return finalStr.trim();
        } else {
            return ""
        }
    }


    parseDisplayString(input, file, targetDate, overrides) {

        let resultString = input

        for (let tokenMatch of input.matchAll(/<[^<>]+>/g)) {

            let beforeThis = resultString.substr(0, resultString.indexOf(tokenMatch[0])).trim()
            let isFirstPart = beforeThis.length == 0

            let token = this.#parseTokenString(tokenMatch[0], isFirst);    
            let tokenValue = "";
            if (!token) {
                tokenValue =  "(invalid token: " + token.replace("<", "[").replace(">", "]") + ")"
            } else {
                tokenValue = this.#formatToken(token, file, targetDate, overrides) ?? ""
            }

            resultString = resultString.replace(tokenMatch[0], tokenValue)
        }

        resultString = (resultString.split(' ').map(f => f.trim()).filter(f => f.length > 0).join(' ')).trim()

        resultString = resultString.replace(new RegExp("\\*\\(\\s*\\)\\*", "g"), "")
        resultString = resultString.replace(new RegExp("\\(\\s*\\)", "g"), "")
        resultString = resultString.replace(new RegExp("\\(\\s*", "g"), "(")
        resultString = resultString.replace(new RegExp("\\s*\\)", "g"), ")")

        while (resultString.startsWith(',')) resultString = resultString.substr(1).trim()
        while (resultString.startsWith(':')) resultString = resultString.substr(1).trim()

        while (resultString.endsWith(":") || resultString.endsWith(",")) {
            resultString = resultString.substr(0, resultString.length - 1).trim()
        }

        return resultString.trim()
    }
}
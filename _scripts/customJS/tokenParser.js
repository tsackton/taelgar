class TokenParser  {

    debug = true

    // Define the allowable filter and format characters
    // unused characters: b c d e g h j k m v w z
    // * format definitions * //
    /*** 
        t: title case; s: lower case, u: initial upper case
        a: indefinite article, A: indefinite article if first, x: no article, q: preposition, Q: no preposition
        n: never link, y: always link
        !: prefer this format if possible
    ***/

    formatChars = "qQaAxnytsu!"

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

    // defines a regex for parsing tokens //

    tokenRegex = /<(\(.*?\))?([a-zA-Z]+):?([^:()\s<>]+?)?(\(.*?\))?>/g

    #parseTokenString(input) {

        // from https://stackoverflow.com/questions/50649912/remove-duplicate-character-in-string-and-make-unique-string
        const remDup= e => [...new Set(e)].sort().join("");
        let tokenRegex = this.tokenRegex
        let filterChars = this.filterChars
        let formatChars = this.formatChars

        // extracts format and filter strings from the token string
        // Initial structure of the result
        let result = {
            token: null,
            filter: "",
            format: "",
            firstformat: "",
            mindepth: 1,
            maxdepth: null,
            prefix: "",
            suffix: ""
        };

        // parse the prefix, suffix, token, and format
        let matches = input.matchAll(tokenRegex);
        let tokenMatch = [...matches][0]
        if (this.debug) console.log(tokenMatch)
        // match1 is the prefix, match2 is the token, match3 is the filter/format, match4 is the suffix
        if (tokenMatch) {
            result.prefix = tokenMatch[1]?.slice(1, -1) ?? "";
            result.suffix = tokenMatch[4]?.slice(1, -1) ?? "";
            result.token = tokenMatch[2] ?? "";

            // parse filterFormat string //

            let filterFormatString = tokenMatch[3]?.split(";");

            // Separate filter and format based on allowable characters
            let filter = "";
            let format = "";
            let firstformat = "";

            // Check for a numerical range or limit at the beginning of the filter
            if (filterFormatString) {
                let rangeRegex = /^(\d+-\d+|\d+-|-?\d+)/;
                let rangeMatch = filterFormatString[0].match(rangeRegex) ?? "";
                if (rangeMatch) {
                    let rangeParts = rangeMatch[0].split("-");
                    if (rangeParts.length === 2) {
                        // If both parts are present in the range
                        // interpret as min-max
                        result.mindepth = rangeParts[0] ? parseInt(rangeParts[0]) : 1;
                        result.maxdepth = rangeParts[1] ? parseInt(rangeParts[1]) : null;
                    } else {
                        // If only one part is present (shorthand for "-number")
                        // interpret as max
                        result.maxdepth = parseInt(rangeParts[0]);
                    }
                    // Remove the range from the filter string
                    filterFormatString[0] = filterFormatString[0].substring(rangeMatch[0].length);
                }

                // a full formatfilter string is defined as filter;format;firstformat
                // if the string is only two parts, it is filter+format;firstformat
                // if the string is only one part, it is filter+(firstformat=format)

                if (filterFormatString.length === 1) {
                    // we just have a string, what is it?
                    // we will parse it as a filter+format string, and assume that the format applies to all steps
                    for (let char of filterFormatString[0]) {
                        if (filterChars.includes(char)) filter += char;
                        if (formatChars.includes(char)) firstformat += char;
                        if (formatChars.includes(char)) format += char;
                    }
                } else if (filterFormatString.length === 2) {
                    // we have a filter and a format
                    // we will parse it as a filter+format string, and a first format string
                    for (let char of filterFormatString[0]) {
                        if (filterChars.includes(char)) filter += char;
                        if (formatChars.includes(char)) format += char;
                    } 
                    for (let char of filterFormatString[1]) {
                        if (filterChars.includes(char)) filter += char;
                        if (formatChars.includes(char)) firstformat += char;
                    }
                } else if (filterFormatString.length === 3) {
                    // we have a filter, a first format, and a format
                    // part 1 is the filter, part 2 is the format, part 3 is the first format
                    for (let char of filterFormatString[0]) {
                        if (filterChars.includes(char)) filter += char;
                    } 
                    for (let char of filterFormatString[1]) {
                        if (formatChars.includes(char)) format += char;
                    }
                    for (let char of filterFormatString[2]) {
                        if (formatChars.includes(char)) firstformat += char;
                    }
                }

                result.filter = remDup(filter);
                result.format = remDup(format);
                result.firstformat = remDup(firstformat) ?? result.format;
            }

        }

        return result;
    }

    #getParameterCaseInsensitive(object, key) {
        // get case insensitive parameter from object
        const asLowercase = key.toLowerCase();
        return object[Object.keys(object)
        .find(k => k.toLowerCase() === asLowercase)
        ];
    }

    #getFormattedName(value, token, targetDate, metadata) {
        // returns a formatted name
        // pass the format and the name to the name manager to generate a formatted name

        const { NameManager } = customJS;

        let possibleAliasKey = token.token + "Alias"
        let alias = metadata.alias ?? this.#getParameterCaseInsensitive(metadata, possibleAliasKey)
        let sourcePageType = metadata.sourcePageType ?? NameManager.getPageType(metadata)
        let format = token.format ?? ""

        return NameManager.getName(value, format, alias, metadata.linkText, sourcePageType)
    }

    #getFormattedLocChain(whereabout, token, targetDate, metadata) {

        const { NameManager } = customJS;
        const { LocationManager } = customJS;

        // returns a formatted location chain
        let followDate = targetDate

        // set q as default if missing //
        // not sure this is right //
        if (!token.filter.includes("q")) {
            token.filter += "q"
        }

        // if the away end date of the whereabout is before the target date, use that as the follow date
        if (whereabout.awayEnd && targetDate && whereabout.awayEnd.sort < targetDate.sort) {
            followDate = whereabout.awayEnd
        }
        if (whereabout.startFilter && !token.filter.includes("!")) {
            token.filter = this.#parseTokenString("<" + token.token + ":" + whereabout.startFilter + ">").filter
        }

        let sourcePageType = metadata.sourcePageType ?? NameManager.getPageType(metadata)

        // this doesn't currently work because we have mindepth and maxdepth parsed but not used //
        // need to refactor getCurrentLocationName to accept token object and pass along mindepth and maxdepth //

        return LocationManager.getCurrentLocationName(whereabout, token, followDate, sourcePageType)

    }

    #getFormattedDate(value, token, targetDate, metadata) {

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

    formatToken(token, file, targetDate, overrides) {

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
        // overrides.sourcePageType sets the source type in name formatting (default otherwise is page type) //
        // overrides.alias sets the alias in name formatting (default otherwise is metadata.<token.token>Alias) //
        // overrides.linkText sets the link text in name formatting (default otherwise is computed by NameManager) //
        // overrides.dateInfo replaces the dateInfo object that is computed by DateManager //

        let metadata = merge_options(file.frontmatter, overrides)

        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)
        let pageDateInfo = metadata.dateInfo ?? DateManager.getPageDates(metadata, targetDate)
        let displayDefaults = NameManager.getDisplayData(metadata)

        let value = "";

        // clean up tokens //
        // target, targetdate, and currentdate are all the same thing
        if (token.token == "target" || token.token == "currentdate") token.token = "targetdate"
        // length and age are the same //
        if (token.token == "length") token.token = "age"
        // end is shorthand for endStatus //
        if (token.token == "end") token.token = "endStatus"
        // start is shorthand for startStatus //
        if (token.token == "start") token.token = "startStatus"
        // subtype is the same as subtypeof //
        if (token.token == "subtype") token.token = "subtypeof"

        // set formatting options //  
        // define four types of formatters //
        // none: no formatting, just return the value //
        // string: find the file represented by this string and apply linking and formatting //
        // date: apply date formatting //
        // locchain: build a location chain from this starting point //

        let formatter = "none"

        switch (token.token.toLowerCase()) {
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

            // start string options //
            case "name":
                value = file.name
                formatter = "name"
                break;
            case "maintype":
                // special case where we define a specific main type based on metadata //
                value = metadata.species ?? this.#getDefaultTypeOf(metadata)
                formatter = "name"
                break;
            // end string options //

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

            // start locchain options //
            case "current":
                value = WhereaboutsManager.getWhereabouts(metadata, targetDate).current
                formatter = "locchain"
                break;
            case "lastknown":
                value = WhereaboutsManager.getWhereabouts(metadata, targetDate).lastKnown
                formatter = "locchain"
                break;
            case "home":
                value = WhereaboutsManager.getWhereabouts(metadata, targetDate).home
                formatter = "locchain"
                break;
            case "origin":
                value = WhereaboutsManager.getWhereabouts(metadata, targetDate).origin
                targetDate = pageDateInfo.startDate ?? DateManager.normalizeDate("0001")
                formatter = "locchain"
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
            case "primary":
                // currently we just use the affliation manager here to get a fully formatted string
                value = AffiliationManager.getFormattedPrimaryAffiliations(metadata, targetDate)
                formatter = "none"
                break;
            case "partof":
                // currently we just use the affliation manager here to get a fully formatted string
                value = AffiliationManager.getAffiliationPartOf(metadata, token.format)
                break;
            // END REFACTOR OPTIONS //

            default:
                // if no special processing, check to see if it is a key in metadata, or failing that, displayDefaults
                value = (this.#getParameterCaseInsensitive(metadata, token.token) ?? this.#getParameterCaseInsensitive(displayDefaults, token.token)) ?? ""
                // default formatter is string
                formatter = "name"
            }

        if (formatter == "name") {
            return this.#getFormattedName(value, token, targetDate, metadata)
        } else if (formatter == "date") {
            return this.#getFormattedDate(value, token, targetDate, metadata)
        } else if (formatter == "locchain") {
            return this.#getFormattedLocChain(value, token, targetDate, metadata)
        } else {
            return value
        }
    }

    formatTokenString(input, file, targetDate, overrides) {
        // Takes a string, which is a token, and returns a formatted string
        // If no token is present, returns the original string
        if (this.debug) console.log("Formatting token string: " + input)

        // Parse the token string into a token object
        let token = this.#parseTokenString(input);
        let formattedToken = "";

        if (this.debug) console.log("Parsed token: " + JSON.stringify(token))

        // If the token is valid, get the formatted string
        if (token.token) {
            formattedToken = this.formatToken(token, file, targetDate, overrides);
        }

        if (this.debug) console.log("Formatted token: " + formattedToken) 

        if (formattedToken) {
            return (token.prefix + formattedToken + token.suffix).trim()
        } else {
            return ""
        }
    }

    formatDisplayString(input, file, targetDate, overrides) {
        if (this.debug) console.log("Formatting display string: " + input);

        // Replace each token in the string with its formatted version
        let formattedString = input.replace(this.tokenRegex, (token) => {
            let formattedToken = this.formatTokenString(token, file, targetDate, overrides);
            return formattedToken || '';
        }).trim();

        // remove extraneous characters from the end of the string//

        const removeCharsRegex = /[,;:]+$/;
        formattedString = formattedString.replace(removeCharsRegex, '');

        if (this.debug) console.log("Formatted display string: " + formattedString);
        // Return the formatted string if it contains alphanumeric characters, else return an empty string
        return /[A-Za-z0-9]+/.test(formattedString) ? formattedString : "";
    }
    
}





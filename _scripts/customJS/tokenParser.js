class TokenParser  {

    // class to take a token in the format of <token:filter;format> or <token:formatfilter> and return an appropriate formatting string //

    #parseTokenString(input, filterChars, formatChars) {

        // extracts format and filter strings from the token string
        // Initial structure of the result
        let result = {
            token: null,
            filter: null,
            format: null,
            firstformat: null,
            mindepth: 1,
            maxdepth: null
        };

        // Check if the input is in the expected format
        if (input.startsWith("<") && input.endsWith(">")) {
            let innerContent = input.slice(1, -1).split(":");
            
            if (innerContent.length === 1) {
                // Case for only token
                result.token = innerContent[0];
            } else if (innerContent.length === 2) {
                // Case for token with filter and format
                result.token = innerContent[0];
                let filterFormatString = innerContent[1].split(";");

                // Separate filter and format based on allowable characters
                let filter = "";
                let format = "";

                // Check for a numerical range or limit at the beginning of the filter
                let rangeRegex = /^(\d+-\d+|\d+-|-?\d+)/;
                let rangeMatch = filterFormatString[0].match(rangeRegex);
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
                // if the string is only two parts, it is filter+firstformat;format
                // if the string is only one part, it is filter+firstformat

                if (filterFormatString.length === 1) {
                    // we just have a string, what is it?
                    // we will parse it as a filter+format string, and assume that the format applies to the first step only
                    for (let char of filterFormatString[0]) {
                        if (filterChars.includes(char)) filter += char;
                        if (formatChars.includes(char)) firstformat += char;
                    }
                } else if (filterFormatString.length === 2) {
                    // we have a filter and a format
                    // we will parse it as a filter+format string, and assume that the format to all steps
                    for (let char of filterFormatString[0]) {
                        if (filterChars.includes(char)) filter += char;
                        if (formatChars.includes(char)) firstformat += char;
                    } 
                    for (let char of filterFormatString[1]) {
                        if (filterChars.includes(char)) filter += char;
                        if (formatChars.includes(char)) format += char;
                    }
                } else if (filterFormatString.length === 3) {
                    // we have a filter, a first format, and a format
                    // part 1 is the filter, part 2 is the format, part 3 is the first format
                    for (let char of filterFormatString[0]) {
                        if (filterChars.includes(char)) filter += char;
                    } 
                    for (let char of filterFormatString[1]) {
                        if (filterChars.includes(char)) filter += char;
                        if (formatChars.includes(char)) format += char;
                    }
                    for (let char of filterFormatString[2]) {
                        if (filterChars.includes(char)) filter += char;
                        if (formatChars.includes(char)) firstformat += char;
                    }
                }

                result.filter = filter;
                result.format = format;
                result.firstformat = firstformat ?? result.format;
            }
        }

        return result;
    }

    #getFormattedPiece(value, token) {
        // Takes a value and a token object and returns a formatted string
        pass
    }

    #getDefaultTypeOf(metadata) {
        // returns the default typeOf for a given metadata
        pass
    }

    #getMainType(metadata, typeOf) {
        // returns the main type for a given metadata
        pass
    }

    #getFormattedWhereaboutsString(whereabout, token, targetDate, sourcePageType) {
        // returns a formatted whereabouts string
        pass
    }

    #getFormattedToken(token, file, targetDate) {
        // Takes a token object and returns a formatted string

        function getParameterCaseInsensitive(object, key) {
            // get case insensitive parameter from object
            const asLowercase = key.toLowerCase();
            return object[Object.keys(object)
            .find(k => k.toLowerCase() === asLowercase)
            ];
        }

        let metadata = file.frontmatter
        let name = file.name
        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)
        let displayDefaults = NameManager.getDisplayData(metadata)
        let pageDateInfo = DateManager.getPageDates(metadata, targetDate)
        let pageType = NameManager.getPageType(metadata)
        let typeOf = this.#getDefaultTypeOf(metadata)

        // if token is not valid, return empty string
        let value = "";
        let formatValue = true

        //***
        //    `name`: the name as generated by NameManager.getName. This will be linked and cased as per the format specifier (see below) and will include the correct definitiveArticle and title from the page
        //    * `pronunciation`: the pronunciation from the page
        //    * `pronouns`: the pronouns or calculated pronouns from gender
        //    * `typeof` or `type` or `maintype`: the page type. This is either the actual `typeOf` or `species` from the frontmatter, or a calculated value based on tags. The calculated value is the first subtag of a `place`, `person`, `item`, or `organization` tag, or the main tag if there are no subtags. i.e. `place\river`  generates a river typeOf, whereas `place` generates a place typeOf. If there is a `typeOfAlias` or `speciesAlias` in the front matter, that is used as the display value
        //    * `subtypeof` or `subtype`:  the `subTypeOf` metadata element
        //    * `current`: The current whereabouts, or unknown if there is not one. This will follow whereabouts chains to generate a comma-separated list of locations at the current date
        //    * `home`: The home whereabouts, or unknown if there is not one. This will follow whereabouts chains to generate a comma-separated list of locations at the current date
        //    * `origin`: The origin whereabouts, or unknown if there is not one. This will follow whereabouts chains to generate a comma-separated list of locations at the create date or `0001` if there is no create date
        //    * `lastKnown`: The last known whereabouts, or if there isn't one, the current whereabouts, or if there isn't one, unknown. This will follow whereabouts chains to generate a comma-separated list of locations at the last known date
        //    * `lastknowndate`: The date of the last known whereabout, or the current date if there is no last known whereabout. Unknown if there is no date.
        //    * `currentdate` or `targetdate` or `target`: the current date, from Fantasy Calendar or the target date of the string format operation, if one was provided
        //    * `startdate`: the page start date. This uses the display value of the date. Blank if there is no start date
        //    * `enddate`: the page end date. This uses the display value of the date. Blank if there is no enddate
        //    * `end`: the end status from the display defaults
        //    * `start`: the start status from the display defaults
        //    * `age` or `length`: the age/length between the start and end dates, including units (currently, only years supported). Blank if cannot be calculated
        //    * `ka`: the ka of an elf; unknown if no ka and the species is elf; blank if no ka and the species is not elf
        //    * `population`: the population from the front matter, formatted as "pop. value" if the value is numeric, just the value otherwise
        //    * `partof`: the partOf value from the front matter, following the change. Note that partOf for locations terminate the chain as they are considered whereabouts not partOfs. 
        //    * `primary`: the list of primary affiliations, in the form:  `affiliation, affiliation, and affiliation`
        //


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

        switch (token.token) {
            case "name":
                value = NameManager.getName(name, metadata, token);
                break;
            case "pronouns":
                if (metadata.pronouns) value = metadata.pronouns
                else if (metadata.gender == "male") value = "he/him"
                else if (metadata.gender == "female") value = "she/her"
                else if (metadata.gender) value = "they/them"
                break;
            case "maintype":
                // special case where we define a specific main type based on metadata //
                value = this.#getMainType(metadata, typeOf);
                break;
            case "startdate": 
                if (pageDateInfo.startDate) value = pageDateInfo.startDate.display
                break;
            case "targetdate":
                if (targetDate) value = targetDate.display
                else value = DateManager.getTargetDateForPage(metadata).display
                break;
            case "enddate":
                if (pageDateInfo.endDate) value = pageDateInfo.endDate.display
                break;
            case "lastknowndate":
                wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
                if (wb.lastKnown.location && wb.lastKnown.awayEnd.sort <= targetDate.sort) {
                    value = wb.lastKnown.awayEnd.display
                } else {
                    if (targetDate) {
                        value = targetDate.display
                    } else {
                        value = DateManager.getTargetDateForPage(metadata).display
                    }
                }
                break;
            case "current":
                wb = WhereaboutsManager.getWhereabouts(metadata, targetDate).current
                value = this.#getFormattedWhereaboutsString(wb, token, targetDate, pageType)
                formatValue = false
                break;
            case "lastknown":
                wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
                value = this.#getFormattedWhereaboutsString(wb.lastKnown, token, targetDate, pageType)
                formatValue = false
                break;
            case "home":
                wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
                value = this.#getFormattedWhereaboutsString(wb.home, token, targetDate, pageType)
                formatValue = false
                break;
            case "origin":
                wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
                value = this.#getFormattedWhereaboutsString(wb.origin, token, pageDateInfo.startDate ?? DateManager.normalizeDate("0001"), pageType)
                formatValue = false
                break;
            case "age":
                if (pageDateInfo.age == 0) value = "0 years"
                else if (pageDateInfo.age == 1) value = "1 year"
                else if (pageDateInfo.age) value = pageDateInfo.age + " years"
                break;
            case "ka":
                if (metadata.species != "elf" && !metadata.ka) {
                    value = ""
                }
                else {
                    value = NameManager.getName("ka") + " " + (metadata.ka ?? "unknown")
                }
                break;
            case "population":
                if (metadata.population) {
                    let intPop = parseInt(metadata.population)
                    if (intPop) value = "pop. " + metadata.population.toLocaleString()
                    else value = metadata.population
                }
                break;
            case "partof":
                value = AffiliationManager.getAffiliationPartOf(metadata, token)
                break;
            case "primary":
                value = AffiliationManager.getFormattedPrimaryAffiliations(metadata, targetDate)
                break;
            default:
                // if no special processing, check to see if it is a key in metadata, or failing that, displayDefaults
                value = (getParameterCaseInsensitive(metadata, token.token) ?? getParameterCaseInsensitive(displayDefaults, token.token)) ?? ""
            }

        if (formatValue) {
            return this.#getFormattedPiece(value, token);
        } else {
            return value
        }
    }

    getFormattedString(input, metadata, targetDate) {
        // Takes a string, which may contain a token, and returns a formatted string
        // If no token is present, returns the original string

        let resultString = input;

        // Define the allowable filter and format characters
        // unused characters: b c d e g h j k m v w z
        // * format definitions * //
        /*** 
            t: title case; s: lower case, u: initial upper case
            a: indefinite article, A: indefinite article if first, x: no article, q: preposition, Q: no preposition
            n: never link, y: always link
            !: prefer this format if possible
        ***/

        let formatChars = "qQaAxnytsu!"

        // * filter definitions * //
        /*** 
            R = include regions only; r = exclude regions (i.e. places with typeOf region)
            L = include locations only; l = exclude locations
            P = include people only; p = exclude people
            I = include items only; i = exclude items
            F = include first step only; f = exclude first step
            O = include organizations only; o = exclude organizations
         ***/

        let filterChars = "rRpPlLiIoOfF!";

        // Parse the token string
        let token = this.#parseTokenString(input, filterChars, formatChars);

        // If the token is valid, get the formatted string
        if (token.token) {
            resultString = this.#getFormattedToken(token, metadata, targetDate);
        }

        return resultString;
    }
}
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

    #getFormattedString(value, token) {
        // Takes a value and a token object and returns a formatted string
        pass
    }

    #getMainType(metadata, typeOf) {
        // returns the main type for a given metadata
        pass
    }

    #getFormattedLocChain(value, token) {
        // returns a formatted location chain
        pass
    }

    #getFormattedDate(value, token) {
        // returns a formatted date
        // right now this just normalizes the date and returns the display value
        return DateManager.normalizeDate(value).display
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
        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)
        let pageDateInfo = DateManager.getPageDates(metadata, targetDate)
        // condsider: consolidate displayData in Token Parser class, or make a new class to manage display strings
        // not really related to name management?
        let displayDefaults = NameManager.getDisplayData(metadata)

        // if token is not valid, return empty string
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

        formatter = "none"

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
                wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
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
                if (metadata.name) value = metadata.name
                else value = file.name
                formatter = "string"
                break;
            case "maintype":
                // special case where we define a specific main type based on metadata //
                value = this.#getMainType(metadata);
                formatter = "string"
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
                    value = this.#getFormattedString("ka") + " " + (metadata.ka ?? "unknown")
                }
                formatter = "none"
                break;
            // end complicated options //
            // REFACTOR OPTIONS //
            // these need to be refactored but I don't really understand the affiliation code yet //
            case "primary":
                // currently we just use the affliation manager here to get a fully formatted string
                value = AffiliationManager.getFormattedPrimaryAffiliations(metadata, token, targetDate)
                formatter = "none"
                break;
            case "partof":
                // currently we just use the affliation manager here to get a fully formatted string
                value = AffiliationManager.getAffiliationPartOf(metadata, token, targetDate)
                break;
            default:
                // if no special processing, check to see if it is a key in metadata, or failing that, displayDefaults
                value = (getParameterCaseInsensitive(metadata, token.token) ?? getParameterCaseInsensitive(displayDefaults, token.token)) ?? ""
                // default formatter is string
                formatter = "string"
            }

        if (formatter == "string") {
            return this.#getFormattedString(value, token, targetDate)
        } else if (formatter == "date") {
            return this.#getFormattedDate(value, token)
        } else if (formatter == "locchain") {
            return this.#getFormattedLocChain(value, token, targetDate)
        } else {
            return value
        }
    }

    getDisplayString(input, metadata, targetDate) {
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
class TokenParser {

    debug = true

    // Define the allowable filter and format characters
    // unused characters: b c d e g h j k m v w z

    // * format definitions * //
    /*** 
        t: title case; s: lower case, u: initial upper case
        a: indefinite article, A: indefinite article if first, x: no definite article, q: preposition, Q: no preposition
        n: never link, y: always link
        !: prefer this format if possible
    ***/

    formatChars = "qQaAxnytsUu!";

    // * filter definitions * //
    /*** 
        R = include regions only; r = exclude regions (i.e. places with typeOf region)
        L = include locations only; l = exclude locations
        P = include people only; p = exclude people
        I = include items only; i = exclude items
        F = include first step only; f = exclude first step
        O = include organizations only; o = exclude organizations
    ***/

    filterChars = "rRpPlLiIoOfF!";

    // defines a regex for parsing tokens //

    tokenRegex = /<(\(.*?\))?([a-zA-Z]+):?([^:()\s<>]+?)?(\(.*?\))?>/g;

    #parseTokenString(input, isFirst) {
        // isFirst allows for special handling of certain format specifiers which need to be conditional on the value being the first in the chain //

        // from https://stackoverflow.com/questions/50649912/remove-duplicate-character-in-string-and-make-unique-string
        const remDup = e => [...new Set(e)].sort().join("");
        let tokenRegex = this.tokenRegex
        let filterChars = this.filterChars
        let formatChars = this.formatChars

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

        // parse the prefix, suffix, token, and format
        let tokenMatches = [...input.matchAll(tokenRegex)];
        // if there is more than one match, don't process the token
        let tokenMatch = tokenMatches.length === 1 ? tokenMatches[0] : null;
        // match1 is the prefix, match2 is the token, match3 is the filter/format, match4 is the suffix
        if (tokenMatch) {
            token.prefix = tokenMatch[1]?.slice(1, -1) ?? "";
            token.suffix = tokenMatch[4]?.slice(1, -1) ?? "";
            token.token = tokenMatch[2] ?? "";

            // parse filterFormat string //

            let filterFormatString = tokenMatch[3]?.split(";");

            // Separate filter and format based on allowable characters
            let filter = "";
            let format = "";
            let chainFormat = "";

            if (filterFormatString) {
                // Check for a numerical range or limit at the beginning of the filter //
                let rangeRegex = /^(\d+-\d+|\d+-|-?\d+)/;
                let rangeMatch = filterFormatString[0].match(rangeRegex) ?? "";
                if (rangeMatch) {
                    // If a range is present, add it to filter and move on //
                    filter += rangeMatch[0];
                    // Remove the range from the filter string
                    filterFormatString[0] = filterFormatString[0].substring(rangeMatch[0].length);
                }

                // a full formatfilter string is defined as filter;format;chainFormat
                // if the string is only two parts, it is filter+format;chainFormat
                // if the string is only one part, it is filter+format

                if (filterFormatString.length === 1) {
                    // we just have a string, what is it?
                    // parse it as a filter + format string
                    for (let char of filterFormatString[0]) {
                        if (filterChars.includes(char)) filter += char;
                        if (formatChars.includes(char)) format += char;
                    }
                } else if (filterFormatString.length === 2) {
                    // we have a;b
                    // part a is parsed as a filter + format string; part b is parsed as chainFormat
                    for (let char of filterFormatString[0]) {
                        if (filterChars.includes(char)) filter += char;
                        if (formatChars.includes(char)) format += char;
                    }
                    for (let char of filterFormatString[1]) {
                        if (formatChars.includes(char)) chainFormat += char;
                    }
                } else if (filterFormatString.length === 3) {
                    // we have a;b;c
                    // a is filter, b is the format, c is chainFormat
                    for (let char of filterFormatString[0]) {
                        if (filterChars.includes(char)) filter += char;
                    }
                    for (let char of filterFormatString[1]) {
                        if (formatChars.includes(char)) format += char;
                    }
                    for (let char of filterFormatString[2]) {
                        if (formatChars.includes(char)) chainFormat += char;
                    }
                }

                token.filter = remDup(filter);
                token.format = remDup(format);
            }

        };

        // clean up tokens //
        // target, targetdate, and currentdate are all the same thing
        if (token.token == "target" || token.token == "currentdate") token.token = "targetdate"
        // length and age are the same //
        if (token.token == "length") token.token = "age"
        // end is shorthand for endStatus //
        if (token.token == "end" || token.token == "endStatus") token.token = "endstatus"
        // start is shorthand for startStatus //
        if (token.token == "start" || token.token == "startStatus") token.token = "startstatus"
        // subtype is the same as subtypeof //
        if (token.token == "subtype") token.token = "subtypeof"
        // typeof and type are the same as maintype //        
        if (token.token == "type") token.token = "typeof"


        if (token.format?.includes("U") && isFirst) {
            token.format = token.format.replace("U", "u")
        } else {
            token.format = token.format?.replace("U", "")
        }

        if (token.format?.includes("A") && isFirst) {
            token.format = token.format.replace("A", "a")
        } else {
            token.format = token.format?.replace("A", "")
        }

        // all tokens are lower case //
        token.token = token.token.toLowerCase()

        return token

        // complicated regex kept as a comment for reference //

        // this is a complicated regex, but basically it is 6 groups:
        //      first, prefix: contained in (), any letters or spaces
        //      second, token: letters only
        //      third, filter: digit-digit, plus filter options
        //      fourth, first item format string: the standard format string options. Can be separated from the filter with an optional semi-colon
        //      fifth, the all item format string: the standard format string options. Must be separated from the filter with a semi colon
        //      sixth, suffix: contained in (), any letters or spaces
        // const regexp = /<(\([()a-zA-Z-:*\s]+\))?([a-zA-Z]+):?([0-9]*[-]?[0-9]*[RrPpLlIiOoFf!]*)?;?([UutsaAnyxqQ]+)?;?([UutsaAnyxqQ]+)?(\([()a-zA-Z-:*\s]+\))?>/g; 
        // 
        // 
        // if (((input || '').match(regexp) || []).length !== 1) {
        //    return null;
        // }
        //
        // let match = regexp.exec(input)
        // if (match) {
        //    token.prefix = match[1] ?? ""
        //    token.token = match[2] ?? ""
        //    token.filter = match[3] ?? ""
        //    token.format = match[4] ?? ""
        //    token.chainFormat = match[5] ?? match[4] ?? ""
        //    token.suffix = match[6] ?? ""
        //}

    }

    #getParameterCaseInsensitive(object, key) {
        // get case insensitive parameter from object
        const asLowercase = key.toLowerCase();
        return object[Object.keys(object)
            .find(k => k.toLowerCase() === asLowercase)
        ];
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

        return NameManager.formatName(value, token.format)
    }

    #getWhereaboutChain(whereabout, targetDate, filter, sourcePageType) {

        const { WhereaboutsManager } = customJS

        // returns a formatted location chain
        let followDate = targetDate

        // if the away end date of the whereabout is before the target date, use that as the follow date
        if (whereabout.awayEnd && targetDate && whereabout.awayEnd.sort < targetDate.sort) {
            followDate = whereabout.awayEnd
        }

        return WhereaboutsManager.getWhereaboutChain(whereabout, followDate, whereabout.startFilter ?? filter, sourcePageType, false)
    }

    #getFormattedWhereaboutList(value, token, targetDate) {

        if (!Array.isArray(value)) return ""

        let results = []
        let index = 0;

        for (let whereabout of value) {

            let formatStr = ""
            if (index++ === 0 && token.format) {
                formatStr = token.format
            } else if (token.chainFormat) {
                formatStr = token.chainFormat
            } else {
                formatStr = ""
            }

            const { NameManager } = customJS;
            results.push(this.formatDisplayString(whereabout.format ?? "<name:" + formatStr + ">", {}, targetDate, whereabout))
        }

        return results.join(', ')
    }

    #getFormattedAffiliationList(value, token) {

        if (!Array.isArray(value)) return ""

        let results = []

        for (let affiliation of value) {

            const { NameManager } = customJS;
            results.push(NameManager.formatName(affiliation.name, token.format))
        }

        return results.join(' and ')
    }

    #getFormattedDate(value, token) {

        const { DateManager } = customJS;

        // returns a formatted date
        // right now this just normalizes the date and returns the display value
        return DateManager.normalizeDate(value).display
    }

    #getTypeOfOrDefault(metadata) {

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

        // prevent undefined ref errors below
        if (!overrides) overrides = {}

        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)
        let pageDateInfo = metadata.dateInfo ?? DateManager.getPageDates(metadata, targetDate)
        let displayDefaults = NameManager.getDisplayData(metadata)
        let sourcePageType = NameManager.getPageType(metadata)

        let value = "";


        // set formatting options //  
        // define four types of formatters //
        // none: no formatting, just return the value //
        // name: apply name formatting, expects a nameObject object //
        // date: apply date formatting, expects a normalizeDate object //
        // whereabout: build a location chain from this starting point //
        // casing: just apply casing //

        let formatter = "none"

        switch (token.token) {
            // date options - value is expected to be a normalizedDate object //
            // to do: actually check this //
            case "startdate":
                if (pageDateInfo.startDate) value = pageDateInfo.startDate
                formatter = "date"
                break;
            case "targetdate":
                value = targetDate ? targetDate : DateManager.getTargetDateForPage(metadata)
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

            // start name options - value is expected to be a name object //
            case "name":
                // this is a special case; we want to use the metadata name only if it is overridden
                // usually we prefer the merged data, but in this case, we want the name only if it represents 
                // an override
                value =  NameManager.getNameObject(overrides.name ?? file.name, sourcePageType)
                formatter = "name"
                break;
            case "ancestry":
            case "subtypeof":
            case "subspecies":
            case "species":
            case "person":
                let valueFromMetadata = this.#getParameterCaseInsensitive(metadata, token.token)
                let possibleAliasKey = token.token + "alias"
                let alias = this.#getParameterCaseInsensitive(metadata, possibleAliasKey)

                value = valueFromMetadata ? NameManager.getNameObject(valueFromMetadata, sourcePageType, { alias: alias }) : ""
                formatter = "name"
                break
            case "typeof":
                let typeOf = this.#getTypeOfOrDefault(metadata)
                value = typeOf ? NameManager.getNameObject(typeOf, sourcePageType, { alias: metadata.typeOfAlias }) : ""
                break
            case "maintype":
                // special case where we define a specific main type based on metadata //
                if (metadata.species) {
                    token.token = "species"
                    return this.#formatToken(token, file, targetDate, overrides)
                } else {
                    token.token = "typeof"
                    return this.#formatToken(token, file, targetDate, overrides)
                }
            // end name options //

            // start none or casing only options //
            case "pronouns":
                if (metadata.pronouns) value = metadata.pronouns
                else if (metadata.gender == "male") value = "he/him"
                else if (metadata.gender == "female") value = "she/her"
                else if (metadata.gender) value = "they/them"
                formatter = "casing"
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
                value = this.#getWhereaboutChain(WhereaboutsManager.getWhereabouts(metadata, targetDate).current, targetDate, token.filter, sourcePageType)
                formatter = "whereabout-list"
                break
            case "lastknown":
                value = this.#getWhereaboutChain(WhereaboutsManager.getWhereabouts(metadata, targetDate).lastKnown, targetDate, token.filter, sourcePageType)
                formatter = "whereabout-list"
                break
            case "home":
                value = this.#getWhereaboutChain(WhereaboutsManager.getWhereabouts(metadata, targetDate).home, targetDate, token.filter, sourcePageType)
                formatter = "whereabout-list"
                break
            case "origin":
                targetDate = pageDateInfo.startDate ?? DateManager.normalizeDate("0001")
                value = this.#getWhereaboutChain(WhereaboutsManager.getWhereabouts(metadata, targetDate).origin, targetDate, token.filter, sourcePageType)
                formatter = "whereabout-list"
                break
            // end whereabout options //

            // start affiliation options //
            case "primary":
                value = metadata.primaryAffiliations ?? AffiliationManager.getPrimaryAffiliations(metadata, targetDate)
                formatter = "affiliation-list"
                break
            case "affiliations":
                // this is a bit of a hack, but we can't just look at the metadata.affiliations as that will always be true
                value = (metadata.affiliations && Array.isArray(metadata.affiliations) && metadata.affiliations.some(f => f.name?.isNormalizedName === true)) ? metadata.affiliations : AffiliationManager.getAffiliations(metadata, targetDate)
                formatter = "affiliation-list"
                break
            case "nonprimary":
                value = metadata.nonPrimaryAffiliations ?? AffiliationManager.getNonPrimaryAffiliations(metadata, targetDate)
                formatter = "affiliation-list"
                break
            // end affiliation options //

            // various complicated options //
            case "ka":
                // ka is unusual because we want to link the word 'ka' to the page for the ka
                // but we don't want to link the number
                if (metadata.species != "elf" && !metadata.ka) {
                    value = ""
                }
                else {
                    value = this.#getFormattedName(NameManager.getNameObject("ka"), token) + " " + (metadata.ka ?? "unknown")
                }
                formatter = "none"
                break;
            // end complicated options //

            // REFACTOR OPTIONS //
            // these might need to be refactored but I don't really understand the affiliation code yet
            case "partof":
                // currently we just use the affliation manager here to get a fully formatted string
                value = AffiliationManager.getAffiliationPartOf(metadata, token.format)
                formatter = "none"
                break;
            // END REFACTOR OPTIONS //

            default:
                // if no special processing, check to see if it is a key in metadata, or failing that, displayDefaults
                value = (this.#getParameterCaseInsensitive(metadata, token.token) ?? this.#getParameterCaseInsensitive(displayDefaults, token.token)) ?? ""
                // default formatter is casing
                formatter = "casing"
        }

        if (value && (!Array.isArray(value) || value.length > 0)) {

            let finalStr = token.prefix
            if (formatter == "name") {
                finalStr += this.#getFormattedName(value, token, metadata)
            } else if (formatter == "date") {
                finalStr += this.#getFormattedDate(value, token, targetDate, metadata)
            } else if (formatter === "casing") {
                finalStr += this.#getFormattedCaseString(value, token)
            } else if (formatter == "affiliation-list") {
                finalStr += this.#getFormattedAffiliationList(value, token)
            } else if (formatter == "whereabout-list") {
                finalStr += this.#getFormattedWhereaboutList(value, token, targetDate)
            }
            else {
                finalStr += value
            }

            finalStr += token.suffix

            return finalStr.trim();
        } else {
            return ""
        }
    }

    formatDisplayString(input, file, targetDate, overrides) {

        function cleanUpResultString(resultString) {
            // Normalize spaces (collapse multiple spaces to one) and trim the string
            resultString = resultString.replace(/\s+/g, ' ').trim();

            // Remove occurrences of `*( )*` and `( )` (with any number of spaces inside the parentheses)
            resultString = resultString.replace(/\*\(\s*\)\*|\(\s*\)/g, '');

            // Clean up spaces around parentheses
            resultString = resultString.replace(/\(\s+/g, '(').replace(/\s+\)/g, ')');

            // Trim leading and trailing commas and colons
            resultString = resultString.replace(/^[:\s,]+|[:\s,]+$/g, '');

            return resultString;
        }

        if (this.debug) console.log("Formatting display string: " + input);

        let formattedString = '';
        let lastIndex = 0;

        for (let tokenMatch of input.matchAll(this.tokenRegex)) {
            let tokenStartIndex = input.indexOf(tokenMatch[0], lastIndex);

            // Append the part of the string before the current token
            formattedString += input.substring(lastIndex, tokenStartIndex);
            let isFirst = (formattedString.trim().length === 0);
            if (this.debug) console.log("Token match: " + tokenMatch[0] + ", current string:" + formattedString + ", which is " + isFirst);
    
            let token = this.#parseTokenString(tokenMatch[0], isFirst);
            if (this.debug) console.log(token);
            let tokenValue = token ? this.#formatToken(token, file, targetDate, overrides) ?? "" : "(invalid token: " + tokenMatch[0].replace("<", "[").replace(">", "]") + ")";
            if (this.debug) console.log("Formatted value:" + tokenValue + ";");
    
            formattedString += tokenValue;
            lastIndex = tokenStartIndex + tokenMatch[0].length;
        }

        formattedString += input.substring(lastIndex);

        return cleanUpResultString(formattedString);
    }

}

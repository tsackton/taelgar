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

    // defines a regex for parsing tokens //

    tokenRegex = /<(\(.*?\))?([a-zA-Z]+):?([^:()\s<>]+?)?(\(.*?\))?>/g

    #parseTokenString(input, isFirst) {
         // isFirst allows for special handling of certain format specifiers which need to be conditional on the value being the first in the chain //

        // from https://stackoverflow.com/questions/50649912/remove-duplicate-character-in-string-and-make-unique-string
        const remDup= e => [...new Set(e)].sort().join("");
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

                result.filter = remDup(filter);
                result.format = remDup(format);
            }

        };

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

        let possibleAliasKey = token.token + "Alias"
        let alias = metadata.alias ?? this.#getParameterCaseInsensitive(metadata, possibleAliasKey)
        let sourcePageType = metadata.sourcePageType ?? NameManager.getPageType(metadata)
        let format = token.format ?? ""

        return NameManager.getName(value, format, alias, metadata.linkText, sourcePageType)
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

        let sourcePageType = metadata.sourcePageType ?? NameManager.getPageType(metadata)

        // this doesn't currently work because we have mindepth and maxdepth parsed but not used //
        // need to refactor getCurrentLocationName to accept token object and pass along mindepth and maxdepth //

        return LocationManager.getCurrentLocationName(whereabout, token, followDate, sourcePageType)
  
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





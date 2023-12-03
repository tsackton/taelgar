class TokenParser  {

    // class to take a token in the format of <token:filter;format> or <token:formatfilter> and return an appropriate formatting string //

    #parseTokenString(input, filterChars, formatChars) {

        // extracts format and filter strings from the token string
        // Initial structure of the result
        let result = {
            token: null,
            filter: null,
            format: null
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
                let initialFormat = innerContent[1].split(";");

                // Separate filter and format based on allowable characters
                let filter = "";
                let format = "";

                for (let formatString of initialFormat) {
                    for (let char of formatString) {
                        if (filterChars.includes(char)) filter += char;
                        if (formatChars.includes(char)) format += char;
                    }
                }

                result.filter = filter;
                result.format = format;
            }
        }

        return result;
    }

    #getFormattedToken(token, metadata, targetDate) {
        // Takes a token object and returns a formatted string
        let resultString = "";

        switch (token.token) {
            case "name":
                resultString = NameManager.getName(token.token, token.format);
                break;
            case "ka":
                if (metadata.species != "elf" && !metadata.ka) {
                    resultString = "";
                } else {
                    resultString = NameManager.getName("ka") + " " + (metadata.ka ?? "unknown");
                }
                break;
            case "population":
                if (metadata.population) {
                    let intPop = parseInt(metadata.population);
                    if (intPop) resultString = "pop. " + metadata.population.toLocaleString();
                    else resultString = metadata.population;
                } else {
                    resultString = "";
                }
                break;
            case "partof":
                resultString = AffiliationManager.getAffiliationPartOf(metadata, token.format);
                break;
            case "primary":
                resultString = AffiliationManager.getFormattedPrimaryAffiliations(metadata, targetDate);
                break;
            default:
                resultString = "";
        }

        return resultString;
    }

    #getFormattedTokenString(token, metadata, targetDate) {
        // Takes a token object and returns a formatted string
        let resultString = "";

        // Define the allowable tokens
        let tokens = ["name", "ka", "population", "partof", "primary"];

        // If the token is valid, get the formatted string
        if (tokens.includes(token.token)) {
            resultString = this.#getFormattedToken(token, metadata, targetDate);
        }

        return resultString;
    }

    getFormattedString(input, metadata, targetDate) {
        // Takes a token string and returns a formatted string
        let resultString = input;

        // Define the allowable filter and format characters
        let filterChars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];
        let formatChars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"];

        // Parse the token string
        let token = this.#parseTokenString(input, filterChars, formatChars);

        // If the token is valid, get the formatted string
        if (token.token) {
            resultString = this.#getFormattedTokenString(token, metadata, targetDate);
        }

        return resultString;
    }
}
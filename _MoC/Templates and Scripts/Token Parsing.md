Token Parsing notes:

three format functions

formatDisplayString takes a string that may contain one or more tokens, removes leading/trailing whitespace, 
splits on whitespace into words
    for each word which contains a token, attempts to format the token with formatTokenString
    if formatTokenString returns "", does not output word containing token
if entire string is non-alpha-numeric, returns ""
otherwise returns string with tokens replaced

formatTokenString takes a word that contains a token, converts the token into an object, and attempts to format with formatToken
if successful, returns formatted string
if not successful, returns ""

formatToken takes a token object and attempts to format the token
if successful, returns formatted string
if not successful, returns ""


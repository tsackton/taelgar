function getPronouns(gender,pronouns) {
        
    // if pronouns are defined in note metadata, use those
    
    if (pronouns) {
        return pronouns
    }

    // otherwise calculate pronouns from note metadata gender
    
    if (gender == "male") {
        return "he/him"
    } else if (gender == "female") {
        return "she/her"
    } 

    // if no gender or nonbinary, use they/them pronouns
    return "they/them"
}
module.exports = getPronouns;
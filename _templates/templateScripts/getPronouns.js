function getPronouns(tp) {
        
    // if pronouns are defined in note metadata, use those
    
    if (tp.frontmatter.pronouns) {
        return pronouns
    }

    // otherwise calculate pronouns from note metadata gender
    
    if (tp.frontmatter.gender == "male") {
        return "he/him"
    } else if (tp.frontmatter.gender == "female") {
        return "she/her"
    } 

    // if no gender or nonbinary, use they/them pronouns
    return "they/them"
}
module.exports = getPronouns;
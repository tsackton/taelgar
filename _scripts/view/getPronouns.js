function get_Pronouns(metadata) {
        
        // if pronouns are defined in note metadata, use those

        if (metadata.pronouns) {
            return pronouns
        }
    
        // otherwise calculate pronouns from note metadata gender
        
        if (metadata.gender == "male") {
            return "he/him"
        } else if (metadata.gender == "female") {
            return "she/her"
        } 
    
        // if no gender or nonbinary, use they/them pronouns
        return "they/them"
}

return get_Pronouns(dv.current())
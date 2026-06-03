class npcUtils {
    getPronouns(gender,pronouns) {
        
        // if pronouns are defined in note metadata, use those
        
        if (pronouns) {
            return pronouns
        }

        // otherwise calculate pronouns from note metadata gender
        
        if (gender == "male") {
            return "he/him"
        } else if (gender == "female") {
            return "she/her"
        } else if (gender == "nonbinary") {
            return "they/them"
        }

        // if no gender, return unknown gender

        return "unknown gender"
    }
    getSpecies(species) {
        if (!species) {
            return "unknown species"
        } else {
            return species
        }
    }
    getAncestry(ancestry) {
        if (ancestry) {
            return " (" + ancestry + ")"
        }
        return ""
    }
}

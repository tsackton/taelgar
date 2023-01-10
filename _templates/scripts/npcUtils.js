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
    getAgeString(yearBorn,yearDied,noteYear) {
        
        // get current year from fantasy calendar API //
        
        let currentYear =  window.FantasyCalendarAPI.getCalendars()[0].current.year

        if (noteYear) {
            currentYear = noteYear
        }

        let age;
        let ageString;
        
        // calculate age as current year - year born, or deceased year - year born if deceased year is < current year //
        
        if (!yearBorn) {
            age = "unknown age"
        } else if (yearDied && (yearDied < currentYear)) {
            age = yearDied - yearBorn
        } else {
            age = currentYear - yearBorn
        }
        
        // calculate strings //
        
        if (!yearBorn && !yearDied) {
            // don't know birth year or death year
            ageString = "unknown age"
        } else if (!yearBorn && yearDied) {
            // know year died, but not year born
            if (yearDied > currentYear) {
                // will die in the future //
                ageString = "unknown age"
            } else {
                // has died in or before current year
                ageString = "d. " + yearDied + "\ndeceased at unknown age"
            }
        } else if (yearBorn && !yearDied) {
            // known birth year, no death year
            ageString = "b. " + yearBorn + "\n" + age + " years old"
        } else if (yearBorn && yearDied) {
            // both birth and death are defined
            if (yearDied > currentYear) {
                // will die in the future //
                ageString = "b. " + yearBorn + "\n" + age + " years old" 
            } else if (yearDied <= currentYear) {
                // has died in or before current year
                ageString = "b. " + yearBorn + ", d. " + yearDied + "\ndeceased at " + age
            } else {
                // shouldn't get here
                ageString = "ERROR1"
            }
        } else {
            // shouldn't get here
            ageString = "ERROR2"
        }
        return ageString
    }
    getHomeLoc(home,homeRegion,origin,originRegion) {
        
        // check if files exist and link if they do //
        // currently cannot figure out how check if a file with a specific name exists //

        let homeCheck = 0
        let homeRegCheck = 0
        let origCheck = 0
        let origRegCheck = 0

        if (homeCheck) {
            home = "[[" + home + "]]"
        }
        if (homeRegCheck) {
            homeRegion = "[[" + homeRegion + "]]"
        }
        if (origCheck) {
            origin = "[[" + origin + "]]"
        }
        if (origRegCheck) {
            originRegion = "[[" + originRegion + "]]"
        }
        
        let homeLoc
        
        if (!home && !homeRegion) {
            homeLoc = "unknown"
        } else if (!home && homeRegion) {
            homeLoc = homeRegion
        } else if (home && !homeRegion) {
            homeLoc = home
        } else {
            homeLoc = home + ", " + homeRegion
        }

        let originLoc
        
        if (!origin && !originRegion) {
            originLoc = ""
        } else if (!origin && originRegion) {
            originLoc = "\n>Originally from: " + originRegion
        } else if (origin && !originRegion) {
            originLoc = "\n>Originally from: " + origin
        } else {
            originLoc = "\n>Originally from: " + origin + ", " + originRegion
        }

        return "Based in: " + homeLoc + originLoc
    }
}

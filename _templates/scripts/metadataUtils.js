// still to do:
// figure out how to handle current location. For most NPCs, this is just home location //
// however some NPCs travel around and it is useful to know where they are at any time //
// so ideally want to autogenerate chronology/location sections //
// this would be based I guess on separate notes? probably can't do it with frontmatter //
// would query to get all the list items that occur before current day, and return those //
// in an ideal world this would allow a single NPC Timelines and NPC Relationships doc and could query those. //
// more likely need separate notes per NPC at least //

class metadataUtils {
    get_existYear(metadata) {
        let yearStart = metadata.born;
        if (yearStart == undefined) yearStart = metadata.built;
        if (yearStart == undefined) yearStart = metadata.created;
        return yearStart
    }
    get_Pronouns(metadata) {
        
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
    get_Species(metadata) {
        if (!metadata.species) {
            return "unknown species"
        } else {
            return metadata.species
        }
    }
    get_Ancestry(metadata) {
        if (metadata.ancestry) {
            return " (" + metadata.ancestry + ")"
        }
        return ""
    }
    get_PageDatedValue(metadata, existYear, strings) {

        if (!strings) {
            strings = ""
        }
                
        let preExistError = "(not yet born)";
        let startPrefix = "b.";
        let endPrefix = "d.";
        let yearEnd = metadata.died;
        let yearStart = existYear

        if (strings != undefined) {
            if (strings.preExistError != undefined) preExistError = strings.preExistError;    
            if (strings.startPrefix != undefined) startPrefix = strings.startPrefix;
            if (strings.endPrefix != undefined) endPrefix = strings.endPrefix;
        }
        
        if (yearEnd == undefined) yearEnd = metadata.destroyed;
        
        let currentYear = metadata.yearOverride;
        if (currentYear == undefined) currentYear =  window.FantasyCalendarAPI.getCalendars()[0].current.year
    
    
        if (!yearStart && !yearEnd) return "";
        if (yearStart && yearEnd && yearStart > yearEnd) return "(timetraveler, check your YAML)";
        
        // we have a created year, no ended year
        if (yearStart && !yearEnd) {
            if (yearStart > currentYear) return preExistError;
            
            let age = currentYear - yearStart;
    
            return startPrefix + " " + yearStart + " (" + age + " years old)";
        }
    
        // we have a death year, no born year
        if (yearEnd && !yearStart) {
            if (yearEnd < currentYear) return endPrefix + " " + yearEnd;
            // they have a death date, and it hasn't happened yet, but no born date, so nothing to show
            return "";
        }
    
        if (yearStart > currentYear) return preExistError;
    
        // we have both a start and end date - and they died before now
        if (yearEnd < currentYear) {       
            return startPrefix + " " + yearStart + " - " + endPrefix + " " + yearEnd +  " at age " + (yearEnd-yearStart);
        }
    
        return startPrefix + " " + yearStart + " (" + (currentYear-yearStart) + " years old)";
    }
    async get_CampaignValue(metadata, frontmatterItem) {

        const configFilePath = app.vault.getRoot().path  + ".obsidian/taelgarConfig.json";
    
        let configFile = await app.vault.adapter.read(configFilePath);
    
        
        let parsed = JSON.parse(configFile);
            
        const campaignValue = parsed.campaignPrefix;
                
        let valueToUse = metadata[frontmatterItem + "_" + campaignValue];
        if (!valueToUse) {
            valueToUse = metadata[frontmatterItem];
        }
    
        return valueToUse;
    }
    get_RegnalValue(metadata) {
     
        let yearStart = metadata.reignStart;
        let yearEnd = metadata.reignEnd;
        if (yearEnd == undefined) yearEnd = metadata.died;
        
        let currentYear = metadata.yearOverride;
        if (currentYear == undefined) currentYear =  window.FantasyCalendarAPI.getCalendars()[0].current.year
    
    
        if (!yearStart) return "";
        if (yearStart && yearEnd && yearStart > yearEnd) return "(timetraveler, check your YAML)";
        
        // reign hasn't started yet
        if (yearStart > currentYear) return "";
    
        // reign hasn't ended yet
        if (yearEnd == undefined || yearEnd >= currentYear) {               
            let reignLength = currentYear - yearStart;
            return "reigning since " + yearStart + " (" + reignLength + " years)";        
        }
    
        // reign has ended
        return "reigned " + yearStart + " - " + yearEnd + " (" + (yearEnd-yearStart) + " years)";
    }
    get_HomeLoc(home,homeRegion,origin,originRegion) {
        
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

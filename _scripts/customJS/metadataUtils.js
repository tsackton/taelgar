class metadataUtils {
    Reformat(metadata, value, front_string, end_string, unknown_value) {
        if (metadata[value]) {
            return front_string + metadata[value] + end_string
        }
        else {
            return unknown_value
        }
    }

    get_existYear(metadata) {
        if (metadata.born) {
            return metadata.born;
        }
        else if (metadata.built) {
            return metadata.built;
        }
        else if (metadata.created) {
            return metadata.created;
        } else {
            return 0
        }
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
    get_PageDatedValue(metadata, existYear, startPrefix, endPrefix, preExistError) {

        preExistError = preExistError ? preExistError : "(not yet born)";
        startPrefix = startPrefix ? startPrefix : "b.";
        endPrefix = endPrefix ? endPrefix : "d.";
        let yearEnd = metadata.died ? metadata.died : metadata.destroyed
        let yearStart = existYear ? existYear : 0
        
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
    TP_get_Location(metadata, frontmatterItem) {

        // construct variables //
        loc = metadata[frontmatterItem];
        locRegion = metadata[frontmatterItem + "Region"];
        
        // find links //

        let locArray = loc.split(',');
        locArray.push(locRegion)
        let locArrayValues = locArray.map(function(f) {
            pieceValue = f.trim();
            file = tp.file.find_tfile(pieceValue);
            if (file != undefined) { return "[[" + pieceValue + "]]";  }
            return pieceValue;
        });
        
        return locArrayValues.join(', ');
    }
}

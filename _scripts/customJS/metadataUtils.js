class metadataUtils {
    Reformat(metadata, value, front_string, end_string, unknown_value) {
        if (metadata[value]) {
            return front_string + metadata[value] + end_string
        }
        else {
            return unknown_value
        }
    }
    
    get_Location (place, region) {
    
        // construct variables //
        loc = place
        locRegion = region
    
        if (loc) {
            if (locRegion) {
                locArray = loc.split(',')
                locArray.push(locRegion)
            } else {
                locArray = loc.split(',')
            }
        } else {
            if (locRegion) {
                locArray = locRegion.split(',')
            } else {
                // no values
                return ""
            }
        }
    
        let locArrayValues = locArray.map(function(f) {
            pieceValue = f.trim();

            file = window.app.vault.getFiles().find(f => f.basename == pieceValue);
            if (file != undefined) { return "[[" + pieceValue + "]]";  }
            return pieceValue;
        });
        
        return locArrayValues.join(', ');
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
            return metadata.pronouns
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
}
